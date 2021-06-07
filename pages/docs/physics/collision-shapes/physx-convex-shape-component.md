# PhysX Convex Shape Component

The *PhysX convex shape component* adds a [convex mesh](collision-meshes.md) as a [shape](physx-shapes.md) to the [PhysX actor](../actors/physx-actors.md) that is attached to the closest parent node.

![Convex Mesh](media/convex-shape.jpg)

You can attach this component to the same node where the actor component is attached, or you can create a child object to attach it to, which allows you to position the shape relative to the actor.

Convex mesh shapes are the least efficient shape to handle for the physics engine, but it is also the only shape that allows you to define your own (convex) collision geometry. For many kind of objects this is necessary, for example for cylindrical objects.

The convex shape component references a [convex collision mesh](collision-meshes.md), which you need to create first.

Note that the editor doesn't visualize convex shape components in any way. The image above was taken by using a [collision mesh visualizer component](collision-meshes.md#visualizing-collision-meshes).

## Component Properties

* [Shared Shape Component Properties](physx-shapes.md#shared-shape-component-properties)
* `CollisionMesh`: The [convex collision mesh](collision-meshes.md) to use.

## See Also


* [PhysX Shapes](physx-shapes.md)
* [PhysX Actors](../actors/physx-actors.md)
