# PhysX Revolute Joint Component

The *PhysX revolute joint component* is a [joint](physx-joints.md) that links two actors such that they can only rotate around one axis relative to each other.

<video src="media/revolute-joint.webm" width="600" height="600" autoplay loop></video>

How far the joined objects can rotate can be limited, either with a *hard limit* that prevents the actor from rotating farther, or with a *soft limit*, which pulls the actor back with a spring.

The revolute joint can also be powered with a *drive*, meaning it will rotate on its own with a maximum force.

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

* `LimitMode`: Defines whether the joint can spin freely, or is restricted by `LowerLimit` and `UpperLimit`.
  * `NoLimit`: The joint can spin without restriction.
  * `HardLimit`: The joint cannot rotate farther than `LowerLimit` and `UpperLimit`. If it hits the boundary, it may bounce back. In this mode `SpringStiffness` acts as a *restitution* value (`[0; 1]` range). At value zero, it will stop dead, with higher values, the actor will bounce back. `SpringDamping` defines a force threshold. If the joint hits the limit with less force than this, it will not bounce back, at all.
  * `SoftLimit`: The joint can spin freely, but when it rotates farther than the limits, a spring will pull it back. In this mode `SpringStiffness` (`[0; inf]` range) specifies how strongly the spring will pull, and `SpringDamping` is used to dampen the spring to prevent oscilation.
* `LowerLimit`, `UpperLimit`: The lower and upper allowed rotation angles, if `LimitMode` is enabled.
* `SpringStiffness`, `SpringDamping`: See `LimitMode`.
* `DriveMode`: Specifies whether the joint will apply a constant force to rotate the actors.
  * `NoDrive`: The joint will not rotate on its own.
  * `DriveAndSpin`: The joint will try to rotate at `DriveVelocity`. If an external force makes it spin even faster, the joint will not brake.
  * `DriveAndBrake`: The joint will try to rotate and `DriveVelocity`. If an external force makes it spin even faster, it will brake to try to not exceed the velocity. 
* `DriveVelocity`: The target velocity to spin at, when `DriveMode` is enabled.
* `MaxDriveTorque`: The maximum force the joint can apply to try to reach `DriveVelocity`. If something blocks the joined actor, the torque affects whether the obstacle can be pushed away.

## See Also


* [Physics Joints](physx-joints.md)
* [PhysX Actors](../actors/physx-actors.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Revolute Joint (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html#revolute-joint)
