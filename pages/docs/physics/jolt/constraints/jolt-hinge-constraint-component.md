# Jolt Hinge Constraint Component

The *Jolt hinge constraint component* is a [constraint](jolt-constraints.md) that links two actors such that they can only rotate around one axis relative to each other.

<video src="media/revolute-joint.webm" width="600" height="600" autoplay loop></video>

How far the joined objects can rotate can be limited.

The hinge can also be powered with a *drive*, meaning it will rotate on its own with a maximum force. The drive can also be configured to effectively act like a spring, pulling the hinge towards a desired rotation.

## Component Properties

* [Shared Constraint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

* `LimitMode`: Defines whether the constraint can spin freely, or is restricted by `LowerLimit` and `UpperLimit`.
  * `NoLimit`: The constraint can spin without restriction.
  * `HardLimit`: The constraint cannot rotate farther than `LowerLimit` and `UpperLimit`. If it hits the boundary, it may bounce back.
* `LowerLimit`, `UpperLimit`: The lower and upper allowed rotation angles, if `LimitMode` is enabled.
* `Friction`: How easy it is to rotate the hinge. Higher values make the constraint stiffer.
* `DriveMode`: Specifies whether the constraint will apply a force to rotate the actors.
  * `NoDrive`: The constraint will not rotate on its own.
  * `ReachVelocity`: The constraint will try to rotate at a speed of `DriveTargetValue`.
  * `ReachPosition`: The constraint will try to rotate towards the angle `DriveTargetValue`.
* `DriveStrength`: The maximum force the constraint can apply to try to reach its target.

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
