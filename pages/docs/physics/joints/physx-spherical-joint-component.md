# PhysX Spherical Joint Component

The *PhysX spherical joint component* is a [joint](physx-joints.md) that links two actors with a *ball and socket constraint*, meaning the actors can rotate around the joint pivot point, but cannot move apart.

<video src="media/spherical-joint.webm" width="600" height="600" autoplay loop></video>

Optionally the amount of rotation that is possible can be limited along the X and Y axis.

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

* `LimitMode`: Specifies whether the cone limit and spring values are used at all, and which effect they have.
  * `NoLimit`: The limit and spring values are not used and the joint can rotate freely.
  * `HardLimit`: The cone limit values are a hard boundary and the joined child actor cannot rotate farther than this. In this mode the `SpringStiffness` acts as a *restitution* value (`[0; 1]` range), meaning it affects how much the actor bounces back when hitting the limit. With a value of zero, the actor will stop dead and not bounce back at all. `SpringDamping` defines a force threshold. If the actor hits the limit with less force than this, it will not bounce back (the limit will act sticky at low speeds).
  * `SoftLimit`: When the joint rotates outside the cone limit, a spring will pull it back. In this mode `SpringStiffness` (`[0; inf]` range) defines the strength of the spring pulling the actor back. `SpringDamping` specifies how much to dampen the spring, to prevent oscilation.
* `ConeLimitY`, `ConeLimitZ`: These two angles make the joint limit how for the child actor may tilt relative to the parent actor. This sets up a cone shape within which the child actor may be. This can be used to prevent unrealistic rotations for stiff objects. Note that the cone limit makes the joint more prone to instability during simulation, so only use it when really needed.
* `SpringStiffness`, `SpringDamping`: See `LimitMode`.

## See Also


* [Physics Joints](physx-joints.md)
* [PhysX Actors](../actors/physx-actors.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Spherical Joint (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html#spherical-joint)
