# Jolt Slider Constraint Component

The *Jolt slider constraint component* is a [constraint](jolt-constraints.md) that links two actors such that they can only slide along one axis relative to each other.

<video src="media/prismatic-joint.webm" width="600" height="600" autoplay loop></video>

Optionally, how for the joined actors can slide can be limited.

## Component Properties

* [Shared Constraint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

* `LimitMode`: Specifies whether the distance of sliding is limited.
  * `NoLimit`: The actors can slide unlimited far. Since they will still collide with other objects, there may be no need to limit the slide distance through the joint.
  * `HardLimit`: When the actors reach the end of the joint range, they will be stopped.
* `LowerLimit`, `UpperLimit`: How far the actor can deviate from the start position in either direction.
* `Friction`: How easy it is to slide along the constraint. Higher values make the joint stiffer.
* `DriveMode`: Specifies whether the constraint will apply a force to push the actors.
  * `NoDrive`: The slider will not push the actors.
  * `ReachVelocity`: The constraint will try to push at a speed of `DriveTargetValue`.
  * `ReachPosition`: The constraint will try to push towards the relative position `DriveTargetValue`.
* `DriveStrength`: The maximum force the constraint can apply to try to reach its target.

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
