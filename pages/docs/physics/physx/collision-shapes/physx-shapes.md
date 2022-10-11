# PhysX Shapes

A [PhysX actor](../actors/physx-actors.md) configures how an object behaves in the physics simulation. However, every physical presence also requires to have a 3D shape. The shape of actors is set up using PhysX shape components.

[Dynamic actors](../actors/physx-dynamic-actor-component.md) can only be simulated with convex shapes. Therefore concave [collision meshes](physx-collision-meshes.md) are exclusive to [static actors](../actors/physx-static-actor-component.md). All shape components represent convex geometry and work with all physics actor types.

## Shape Components

The following shape components are available:

* [PhysX Sphere Shape Component](physx-sphere-shape-component.md)
* [PhysX Box Shape Component](physx-box-shape-component.md)
* [PhysX Capsule Shape Component](physx-capsule-shape-component.md)
* [PhysX Convex Shape Component](physx-convex-shape-component.md)

## Actor Shape Setup

The easiest kind of actor shape setup is to simply attach a shape component to the same [game object](../../../runtime/world/game-objects.md) that the actor component is attached to. This way the position of the game object is also the center of the shape, which is often sufficient.

For more complex shapes, you can add child nodes below the actor node, attach the shapes to those nodes, and position the nodes as needed.

When an actor is initialized for the simulation, it traverses the hierarchy below its owner game object and gathers all shape components. When it encounters another actor component, all shapes below that node are ignored.

All shapes that are found this way are added to the actor as one *compound shape*. This way you can build a single actor that has a complex shape, made up of many parts.

You can't add or remove individual shapes during simulation. If you need pieces to be destructible, you need to turn them into separate actors. To still have those actors move in unison, you need to join them using a [fixed joint](../joints/physx-fixed-joint-component.md).

## Center Of Mass

The *center of mass* (COM) is the point in space around which an actor spins when a force is applied to it. The COM is computed automatically from the shapes and their masses. It often ends up too high and makes objects tip over too easily. You can adjust the center of mass by placing a child node with a [center of mass component](physx-center-of-mass-component.md) in the hierarchy of the actor.

## Friction and Restitution

*Friction* and *restitution* are the two physical properties that affect a shape's physical behavior the most. See [this section](../../../materials/surfaces.md#physics-properties) for details.

## OnContact Reactions

TODO

## Shared Shape Component Properties

All shape components share these properties:

* `Surface`: The [surface](../../../materials/surfaces.md) configures the **friction** and **restitution** of the physics material. It also specifies what effects ([prefabs](../../../prefabs/prefabs-overview.md)) to spawn when objects collide or interact in other ways.
* `CollisionLayer`: The [collision layers](physx-collision-layers.md) configures which shapes collide with each other, and which shapes pass through each other. Note that each shape has its own collision layer, even in a complex compound object.
* `OnContact`: This option specifies what should happen when this shape collides with another shape, in addition to the regular physical reaction. See the 'OnContact Reactions' section above.  

## See Also


* [PhysX Actors](../actors/physx-actors.md)
* [Surfaces](../../../materials/surfaces.md)
* [Collision Layers](physx-collision-layers.md)
