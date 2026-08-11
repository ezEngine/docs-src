# Voxel Navigation Component

This component moves a game object through 3D space, using [voxel grids](voxel-grid-component.md) to path around obstacles. It is meant for objects that fly or swim, rather than walk on ground. For characters that move over a [navmesh](runtime-navmesh.md), use the [AI navigation component](navigation-component.md) instead.

The component is controlled through [code](../../custom-code/custom-code-overview.md). Call `SetDestination()` with a world-space position, and the component searches a path and then steers its owner object along it. `GetState()` tells whether it is idle, moving, or whether the last path search failed.

Alternatively, set the `NavigationTarget` property to another game object. The component then paths towards that object's current position on its own, and recomputes the path while moving, when the target has moved far enough away from where the path was last aimed at.

## Movement Behavior

The component tracks two positions. The *path position* is the ground truth. It always lies on the computed path, which only runs through free voxels, and advances along it by arc length. The *steering position* is what is applied to the game object. It steers nose-first towards a point further ahead on the path (`LookAheadDistance`), instead of snapping onto the waypoints, which produces smooth movement through curves. It is not validated against the voxel grid, but it is kept within a corridor around the path position: once it strays further than `MaxPathOffset`, it is smoothly pulled back (`CorridorCorrectionRate`).

Because the path position can never leave the cleared path, following a path can't get stuck. The `Failed` state only occurs when no path could be found at all.

Turning is rate-limited by `MaxAngularSpeed`, and speed is reduced while turning sharply and while approaching the end of the path. The object stays upright, but banks into turns while it is turning.

The object doesn't necessarily have to come to a stop at its destination. Use `IsApproachingDestination()` to detect when it would start braking, and set a new destination at that moment to keep it moving continuously.

## Component Properties

* `NavigationTarget`: A [reference](../../concepts/object-references.md) to another object to move towards. Optional, if the destination is set through code instead.
* `Speed`: The target movement speed.
* `Acceleration`, `Deceleration`: How quickly to gain speed and how quickly to brake. The deceleration value also determines how far ahead of the destination the object starts slowing down.
* `ReachedDistance`: The distance at which the destination counts as reached.
* `ApplySteering`: If disabled, the component computes everything but doesn't move the game object. Used when another system applies the movement.
* `LookAheadDistance`: How far ahead along the path the object steers towards. Larger values cut corners more and produce smoother movement.
* `MaxPathOffset`: How far the visual position may stray from the path before it is pulled back.
* `CorridorCorrectionRate`: How quickly the visual position is pulled back once it exceeds `MaxPathOffset`.
* `MaxAngularSpeed`: The maximum turning speed.
* `BankAmount`: How strongly to bank into turns. Zero disables banking, negative values flip the direction.
* `MaxBankAngle`: The maximum angle to bank by.
* `DebugFlags`: `PrintState` displays the current state as text at the object's position, `VisPath` draws the current path.

## Component Script Functions

* `SetDestination(destination)`: Searches a path to the given world-space position and starts moving along it.
* `SetDestinationDirect(destination)`: Moves straight towards the position without doing a path search and without checking for obstacles. Used to recover from situations where a regular path search isn't possible, for instance when the object ended up inside an occupied voxel.
* `SetNavigationTarget(object)`: Sets the object to follow, same as the `NavigationTarget` property.
* `CancelNavigation()`: Stops the navigation.
* `GetState()`: Returns whether the component is `Idle`, `Moving`, or `Failed`.
* `IsNavigating()`: Whether a path is currently being followed.
* `IsApproachingDestination()`: Whether the object is close enough to the end of the path that it would start braking.
* `TurnTowards(direction)`: Rotates the object towards a direction, limited by `MaxAngularSpeed`, and returns the angle that is still left to turn. Has no lasting effect while a path is being followed, since the path steering overwrites the rotation.
* `GetTurnAngleTowards(direction)`: Returns the same angle as `TurnTowards()`, but without rotating anything.
* `FindRandomPointAroundSphere(center, radius, maxAttempts, point)`: Searches for a random navigable position within a sphere. Returns false if no such position was found within the given number of attempts.
* `GetValidCellNearby(start, searchRadius, point)`: Returns the given position if it is navigable, otherwise the closest navigable position within the search radius. Returns false if there is none. Combine this with `SetDestinationDirect()` to get an object out of a blocked position.

Positions count as navigable if they are in a free voxel, or if they are not covered by any voxel grid at all.

## See Also

* [3D Voxel Navigation](voxel-navigation.md)
* [Voxel Grid Component](voxel-grid-component.md)
* [Voxel Path Test Component](voxel-path-test-component.md)
