# Jolt Sphere Shape Component

The *Jolt sphere shape component* adds a sphere as a [shape](jolt-shapes.md) to the [Jolt actor](../actors/jolt-actors.md) that is attached to the closest parent node.

![Sphere Shape](media/jolt-sphere-shape.jpg)

You can attach this component to the same node where the actor component is attached, or you can create a child object to attach it to, which allows you to position the shape relative to the actor.

Spheres are very efficient for the physics engine to handle. Therefore you should prefer them over all other shapes, especially [convex shapes](jolt-convex-shape-component.md), when you can approximate the geometry of an object with one or a couple sphere shapes.

## Component Properties

* `Radius`: The radius of the sphere shape.

## See Also

* [Jolt Shapes](jolt-shapes.md)
* [Jolt Actors](../actors/jolt-actors.md)
