# Detour Crowd Agent Component

The *Detour Crowd Agent* component provides navigation and local obstacle avoidance for characters, using the Recast/Detour crowd system. Unlike the [AI Navigation Component](navigation-component.md), it handles multiple agents simultaneously and resolves collisions between them through a shared crowd simulation.

All agents that share the same [navmesh configuration](runtime-navmesh.md) are grouped into a single crowd internally. Each agent avoids others in the same crowd while following its own path.

## Usage

Call `SetDestination()` from [script](../../custom-code/custom-code-overview.md) or C++ to make the agent navigate toward a position. If the destination is not exactly on the navmesh, the nearest reachable point is used as the actual target; `GetActualDestination()` returns that point.

`HasDestination()` returns true while the agent is still navigating. `CancelNavigation()` stops movement and clears the destination.

If `AllowPartialPath` is false and pathfinding fails entirely, the `SteeringFailed` bit is set on the component.

## Component Properties

* **NavmeshConfig:** Which [navmesh type](runtime-navmesh.md#navmesh-types) the agent walks on.
* **Radius:** The agent's horizontal radius, used for navmesh queries and inter-agent avoidance.
* **Height:** The agent's vertical extent.
* **MaxSpeed:** Maximum movement speed in meters per second.
* **MaxAcceleration:** How quickly the agent reaches its target speed.
* **StoppingDistance:** When the agent is within this distance of the destination, it considers the destination reached and stops.
* **MaxAngularSpeed:** Maximum rotation speed in degrees per second.
* **RotationMode:** Controls how the agent orients itself while moving:
  * `LookAtNextPathCorner` — rotates toward the next waypoint on the path.
  * `MatchVelocityDirection` — rotates to match the current velocity direction.
* **Pushiness:** Determines priority in agent-to-agent collisions. An agent pushes others with lower pushiness and gets pushed by agents with higher pushiness.

## Debug CVars

The following [CVars](../../debugging/cvars.md) can be used to visualize crowd state at runtime:

* `DetourCrowd.Debug.VisAgents` — draws agent shapes.
* `DetourCrowd.Debug.VisCorners` — draws the next few path corners for each agent.
* `DetourCrowd.Debug.VisDestination` — draws agent destination points.

## See Also

* [AI Navigation Component](navigation-component.md)
* [Runtime Navmesh](runtime-navmesh.md)
* [AiPlugin Overview](ai-plugin-overview.md)
