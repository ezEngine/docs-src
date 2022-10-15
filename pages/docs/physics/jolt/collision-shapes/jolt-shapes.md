# Jolt Shapes

A [Jolt actor](../actors/jolt-actors.md) configures how an object behaves in the physics simulation. However, every physical presence also requires to have a 3D shape. The shape of actors is set up using Jolt shape components.

[Dynamic actors](../actors/jolt-dynamic-actor-component.md) can only be simulated with convex shapes. Therefore concave [collision meshes](jolt-collision-meshes.md) are exclusive to [static actors](../actors/jolt-static-actor-component.md). All shape components represent convex geometry and work with all physics actor types.

## Shape Components

The following shape components are available:

* [Jolt Sphere Shape Component](jolt-sphere-shape-component.md)
* [Jolt Box Shape Component](jolt-box-shape-component.md)
* [Jolt Capsule Shape Component](jolt-capsule-shape-component.md)
* [Jolt Cylinder Shape Component](jolt-cylinder-shape-component.md)
* [Jolt Convex Shape Component](jolt-convex-shape-component.md)

## Actor Shape Setup

The easiest kind of actor shape setup is to simply attach a shape component to the same [game object](../../../runtime/world/game-objects.md) that the actor component is attached to. This way the position of the game object is also the center of the shape, which is often sufficient.

For more complex shapes, you can add child nodes below the actor node, attach the shapes to those nodes, and position the nodes as needed.

When an actor is initialized for the simulation, it traverses the hierarchy below its owner game object and gathers all shape components. When it encounters another actor component, all shapes below that node are ignored.

All shapes that are found this way are added to the actor as one *compound shape*. This way you can build a single actor that has a complex shape, made up of many parts.

You can't add or remove individual shapes during simulation. If you need pieces to be destructible, you need to turn them into separate actors. To still have those actors move in unison, you need to join them using a [fixed joint](../constraints/jolt-fixed-constraint-component.md).

## Friction and Restitution

*Friction* and *restitution* are the two physical properties that affect a shape's physical behavior the most. See [this section](../../../materials/surfaces.md#physics-properties) for details.

## See Also

* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Collision Layers](jolt-collision-layers.md)
* [Surfaces](../../../materials/surfaces.md)
