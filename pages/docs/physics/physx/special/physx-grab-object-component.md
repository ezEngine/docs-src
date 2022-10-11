# PhysX Grab Object Component

The *PhysX grab object component* enables a [character controller](physx-character-controller.md) to pick up physical items to carry around, drop or throw.

<video src="media/grab-items.webm" width="600" height="600" autoplay loop></video>

The component is typically attached to the same object as the [camera component](../../../graphics/camera-component.md). When triggered, it uses a raycast along its X axis to determine which physical object to potentially pick up. When it finds a non-kinematic [dynamic actor](../actors/physx-dynamic-actor-component.md), it checks whether a [grabbable item component](../../../gameplay/grabbable-item-component.md) is available. If so, the information from that component is used to determine the best anchor at which to hold the object, otherwise it uses the object's bounding box to approximate a grab point.

When it finds a suitable grab point, it attaches a [6DOF joint](../joints/physx-6dof-joint-component.md) to an object that is specified to be the pivot point (see `AttachTo` property). That object has to have a [**kinematic** actor](../actors/physx-dynamic-actor-component.md) and a dummy [shape](../collision-shapes/physx-shapes.md). The joint will then pull the grabbed item towards it and try to align its orientation according to the grabbed anchor.

The grabbed item can then be dropped, or thrown away. All actions must be triggered from code, either [C++](../../../custom-code/cpp/cpp-overview.md) or [TypeScript](../../../custom-code/typescript/typescript-overview.md).

The grabbed item still physically interacts with the environment. If such collisions hold the object too far back, the grab object component may decide to 'break' the joint and drop the object. In this case a `ezMsgPhysicsJointBroke` event message is sent.

## Component Properties

* `MaxGrabPointDistance`: The maximum distance from this object for an individual *grab point* to be considered as a candidate.
* `CollisionLayer`: The [collision layer](../collision-shapes/physx-collision-layers.md) to use for raycasting to detect which object to pick.
* `SpringStiffness`, `SpringDamping`: The stiffness and damping of the internally used [6DOF joint](../joints/physx-6dof-joint-component.md). Affects how stiff the object is held. **Careful:** This also determines how much force the held object can apply to other objects when you push against them. High values mean that the held object can push objects, that the [character controller](physx-character-controller.md) itself may not be able to push.
* `BreakDistance`: If the held object deviates more than this distance from the anchor point it is attached to, the hold will break. In this case a `ezMsgPhysicsJointBroke` event message is raised. Set to zero to disable this feature.
* `AttachTo`: A reference to another game object, to which the held object will be attached to. The target object **must have** a kinematic [PhysX actor](../actors/physx-dynamic-actor-component.md) (and a dummy [PhysX shape](../collision-shapes/physx-shapes.md)), such that a [joint](../joints/physx-joints.md) can be attached. The reference may point to this component's owner object. However, using a different object allows you to place the held object in a more suitable location.
* `GrabAnyObjectWithSize`: If this is non-zero, objects that have no [grabbable item component](../../../gameplay/grabbable-item-component.md) can be picked up as well, as long as their bounding box is smaller than this value.

## See Also


* [Physics Joints](../joints/physx-joints.md)
* [PhysX Actors](../actors/physx-actors.md)
