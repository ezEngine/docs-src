# Jolt Actors

In EZ objects that are part of the physical simulation are referred to as **actors**. Note that inside Jolt Physics, they are called *bodies*. Every actor has its own simulation state, such as position, velocity, torque, contact points with other actors, and so on. Everything that should participate in the simulation, be it static background geometry, or fully simulated bodies, has to be an actor.

In some special cases, for instance for [greyboxing geometry](../../../scenes/greyboxing.md), the engine takes care to create collision meshes and actors automatically for you. However, for the most part, you have to set up physics actors yourself.

We distinguish between three types of actors: *static* actors, *dynamic* actors and *triggers*. Additionally, dynamic actors can be *kinematic*.

Actors themselves don't have a physical shape. Instead they have to be made up of pieces which hold [shape components](../collision-shapes/jolt-shapes.md). Upon creation, every actor traverses the node hierarchy below its owner [game object](../../../runtime/world/game-objects.md) to search for shape components. All shapes that are found are added to the actor as a *compound shape*. If another actor is found in the process, shapes below that node are ignored, though. This way a single actor can have a complex shape, even if every single piece is only a sphere, box, capsule or other simple shape.

## Static Actors

Static actors represent physical objects that never move. This should be the case for the vast majority of the scene geometry. Static actors are much more efficient to deal with. Also, they are the only actors that can use **concave collision geometry**, meaning arbitrary triangle meshes. Obviously, those meshes cannot be animated.

Static actors are set up by attaching a [static actor component](jolt-static-actor-component.md) to a [game object](../../../runtime/world/game-objects.md).

## Dynamic Actors

Dynamic actors represent all physical objects that move. The physics simulation furthermore distinguishes between **kinematic** actors and fully simulated (non-kinematic) actors.

**Kinematic actors** are objects whose transform is determined by the game logic. That means you can freely move them around your scene and they will always end up exactly where you moved them to.

**Regular actors** (non-kinematic ones) are simulated using rigid body simulation. These objects collide with other objects, react to forces such as gravity, bounce off of objects that they collide with and slide or roll across surfaces realistically.

Regular actors are used to represent all the physical objects in a world that should react realistically to external stimuli. Kinematic actors are used for everything that needs to move, and should affect the simulated objects, but should itself be under full control of the game logic. Kinematic actors will push other actors out of their way relentlessly. If a kinematic actor moves into another kinematic or static actor, the two will simply pass through each other.

Whether a dynamic actor is treated as a kinematic actor or not, is an on/off switch. It is possible to switch this property back and forth at will.

Dynamic actors are set up by attaching a [dynamic actor component](jolt-dynamic-actor-component.md) to a [game object](../../../runtime/world/game-objects.md).

### Video: How to create a physics object

[![video](https://img.youtube.com/vi/hlEUdO5yVig/0.jpg)](https://www.youtube.com/watch?v=hlEUdO5yVig)

## Triggers

Triggers are a special type of actor. Triggers don't interfere with the simulation, meaning nothing ever collides with them. Instead, triggers monitor whether any other actor overlaps with their volume. If so, they raise an [event message](../../../runtime/world/world-messaging.md#event-messages) to inform other code.

Triggers are an efficient solution to detect overlaps, when it is imperative that no overlap is ever missed. If on the other hand you only want to check for overlapping objects at some time or only every couple of seconds, it can be more efficient to just do an *overlap check* through the physics API.

Triggers are set up by attaching a [trigger component](jolt-trigger-component.md) to a [game object](../../../runtime/world/game-objects.md).

## Other Actors

ezEngine comes with a couple of additional components that end up as physics actors in the simulation, but have additional functionality for specific use cases. For example the [query shape actor](jolt-queryshape-actor-component.md) and the [hitbox component](../ragdolls/jolt-hitbox-component.md) can be used to define hit-boxes and the [ragdoll component (TODO)](../ragdolls/jolt-ragdoll-component.md) is used to physically simulate creatures.

### Character Controller

A [character controller](../special/jolt-character-controller.md) is a special kind of kinematic actor that has convenience functions to move around a scene, slide along obstacles and slopes, and so on. Character controllers are used as very abstract representations of creatures and players and implement the important aspect of moving and colliding properly throughout a physical scene.

## See Also

* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
* [Jolt Static Actor Component](jolt-static-actor-component.md)
* [Jolt Dynamic Actor Component](jolt-dynamic-actor-component.md)
* [Jolt Trigger Component](jolt-trigger-component.md)
