# Jolt Box Shape Component

The *Jolt box shape component* adds a box as a [shape](jolt-shapes.md) to the [Jolt actor](../actors/jolt-actors.md) that is attached to the closest parent node.

![Box Shape](media/jolt-box-shape.jpg)

You can attach this component to the same node where the actor component is attached, or you can create a child object to attach it to, which allows you to position the shape relative to the actor.

Boxes are relatively efficient for the physics engine to handle. Prefer them over the [convex shape component](jolt-convex-shape-component.md) when possible.

## Component Properties

* `HalfExtents`: The width, height and depth of the box shape, from its center position.

## See Also

* [Jolt Shapes](jolt-shapes.md)
* [Jolt Actors](../actors/jolt-actors.md)
