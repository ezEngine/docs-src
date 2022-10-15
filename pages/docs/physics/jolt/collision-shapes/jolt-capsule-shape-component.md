# Jolt Capsule Shape Component

The *Jolt capsule shape component* adds a capsule as a [shape](jolt-shapes.md) to the [Jolt actor](../actors/jolt-actors.md) that is attached to the closest parent node.

![Capsule Shape](media/jolt-capsule-shape.jpg)

You can attach this component to the same node where the actor component is attached, or you can create a child object to attach it to, which allows you to position the shape relative to the actor.

Capsules are relatively efficient for the physics engine to handle. Prefer them over the [convex shape component](jolt-convex-shape-component.md) when possible. For long thin objects, especially static collision geometry, capsules may also be more efficient and yield better results, than [box shapes](jolt-box-shape-component.md).

## Component Properties

* `Radius`: The radius of the capsule, ie its thickness.
* `Height`: The height or length of the capsule.

## See Also

* [Jolt Shapes](jolt-shapes.md)
* [Jolt Actors](../actors/jolt-actors.md)
