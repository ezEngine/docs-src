# PhysX Fixed Joint Component

The *PhysX fixed joint component* is the most simple [joint](physx-joints.md) type. It links two [actors](../actors/physx-actors.md) together, such that they move in unison. If all you want is to merge two [shapes](../collision-shapes/physx-shapes.md), you should just attach them to the same actor. The main use case for fixed joints is to make them *breakable*.

<video src="media/fixed-joint.webm" width="600" height="600" autoplay loop></video>

Fixed joints can be used to set up very simple destructible objects.

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

## See Also


* [Physics Joints](physx-joints.md)
* [PhysX Actors](../actors/physx-actors.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Fixed Joint (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html#fixed-joint)