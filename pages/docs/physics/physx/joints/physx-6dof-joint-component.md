# PhysX 6DOF Joint Component

The *PhysX 6DOF joint component* is the most versatile [joint](physx-joints.md) type. *6DOF* stands for *six degrees of freedom*, meaning that this joint can be configured separately for each linear axis (movement) and angular axis (rotation).

<video src="media/6dof-joint.webm" width="600" height="600" autoplay loop></video>

This joint component is based on the [PhysX 6DOF joint](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Manual/Joints.html#d6-joint). However, the EZ 6DOF joint component does not expose all of the many configuration options of the PhysX 6DOF joint. Instead it condenses some of these options down to a most commonly useful set of options.

Consequently some very specialized scenarios would be possible to do with PhysX, but are currently not possible with the available joint component types. In such a case, it most likely makes sense to add a joint type for the specialized use case, which utilizes the 6DOF joint functionality accordingly.

## 6DOF Joint Features

### Movement

With the `FreeLinearAxis` option the 6DOF joint can be configured to allow movement along each axis, similar to the [prismatic joint](physx-prismatic-joint-component.md). Contrary to the prismatic joint, movement can be allowed along two or all three axis, such that the joint can move in a plane or volume. Using the `LinearLimitMode` and `LinearRangeX/Y/Z` you can also restrict the area in which the joint can be. `LinearStiffness` and `LinearDamping` configure the spring (soft limit mode) that pulls the joint back, or the restitution and force threshold (hard limit mode), in the same way as for other joint types, like the [prismatic joint](physx-prismatic-joint-component.md).

### Rotation

With the `FreeAngularAxis` option the joint can be configured to allow rotation around each of the axis. Note that the X axis is considered to be the *twist* axis and the Y and Z axis are considered to be the *swing* axis.

With `SwingLimitMode` and `TwistLimitMode` you can choose whether twisting and swinging should be limited and whether it should be a hard limit or a soft (springy) limit. There are separate options to configure the swing and twist behavior (angle limits, stiffness, damping) which act the same way as for other joint types, like the [spherical joint](physx-spherical-joint-component.md) or the [revolute joint](physx-revolute-joint-component.md).

## Features Not Exposed

The following PhysX features are currently not exposed by the `ezPx6DOFJointComponent`:

* Seperate spring configuration values for each linear and angular axis.
* Circular/spherical distance limits.
* Pyramid swing limit.
* Linear and angular drives.
* Drive target transforms.

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

* `FreeLinearAxis`: Along which axis the joint is allowed to move.
* `LinearLimitMode`: Whether movement is limited in any way.
* `LinearRangeX/Y/Z`: If movement is limited, this is the area in which the joint can move.
* `LinearStiffness`, `LinearDamping`: Spring/damping or restitution/force-threshold values for when the joint reaches the limit boundary. Works the same way as for other joint types, for instnace the [prismatic joint](physx-prismatic-joint-component.md).
* `FreeAngularAxis`: Around which axis the joint is allowed to rotate. X is the *twist* axis, Y and Z are the *swing* axis.
* `SwingLimitMode`: Whether swinging rotations are limited in any way.
* `SwingLimit`: How far the joint can swing.
* `SwingStiffness`, `SwingDamping`: Same as for the [spherical joint](physx-spherical-joint-component.md).
* `TwistLimitMode`: Whether twisting rotations are limited in any way.
* `LowerTwistLimit`, `UpperTwistLimit`: Lower and upper angular limits for rotations around the twist axis.
* `TwistStiffness`, `TwistDamping`: Same as for the [revolute joint](physx-revolute-joint-component.md).

## See Also


* [Physics Joints](physx-joints.md)
* [PhysX Actors](../actors/physx-actors.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [6DOF Joint (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html#d6-joint)
