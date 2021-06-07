# PhysX Capsule Shape Component

The *PhysX capsule shape component* adds a capsule as a [shape](physx-shapes.md) to the [PhysX actor](../actors/physx-actors.md) that is attached to the closest parent node.

![Capsule Shape](media/capsule-shape.jpg)

You can attach this component to the same node where the actor component is attached, or you can create a child object to attach it to, which allows you to position the shape relative to the actor.

Capsules are relatively efficient for the physics engine to handle. Prefer them over the [convex shape component](physx-convex-shape-component.md) when possible. For long thin objects, especially static collision geometry, capsules may also be more efficient and yield better results, than [box shapes](physx-box-shape-component.md).

## Component Properties

* [Shared Shape Component Properties](physx-shapes.md#shared-shape-component-properties)
* `Radius`: The radius of the capsule, ie its thickness.
* `Height`: The height or length of the capsule.

## See Also


* [PhysX Shapes](physx-shapes.md)
* [PhysX Actors](../actors/physx-actors.md)
