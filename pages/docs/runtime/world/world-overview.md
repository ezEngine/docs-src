# The World / Scenegraph System

When you build a scene in the editor or through code, the structure of all the objects is stored in something that is commonly referred to as a *scenegraph*. In EZ the scenegraph is implemented by the class `ezWorld`, which is why the terms *scenegraph* and *world* are used interchangeably in our documentation.

## ECS

In EZ we use a variation of an **E**ntity **C**omponent **S**ystem ([ECS](https://en.wikipedia.org/wiki/Entity_component_system)). It doesn't matter whether you are familiar with ECSs, but if you are, the main difference of our implementation to a pure ECS is, that in EZ there is always exactly one *system* to handle each *component type*. You can have additional systems (see [World Modules](world-modules.md)), however, this is not as common as in other engines.

The main classes involved are `ezWorld`, `ezGameObject`, `ezComponent` and `ezWorldModule` / `ezComponentManager`.

### ezWorld

Each `ezWorld` represents the entire state of a scene. Worlds hold all [game objects](game-objects.md) and all [world modules](world-modules.md), which in turn hold all [components](components.md).

Each world has its own simulation state, such as a clock and a random number generator. Through the world modules, worlds also hold their own state for other simulation aspects, such as [physics](../../physics/physx-overview.md).

You can have multiple worlds in parallel and they will be completely separated. This is for example the case when you have multiple [documents](../../editor/editor-documents.md) open in the editor.

Worlds are described in more detail in [this chapter](worlds.md).

### ezGameObject

`ezGameObject` is our *entity* class. The terms *entity*, *game object* and *node* are used interchangeably. Every game object has a position, rotation and scale. It may be attached to a single *parent* game object and it may have multiple game objects attached as children. The game object hierarchy is a directed acyclic graph (DAG).

Game objects by themselves do not have any *behavior*. Instead, each game object can have an arbitrary number of [components](components.md) attached.

The object's *transform* (position, rotation, scale) is local to its parent node, but it also holds a *global* transform, which is computed by concatenating the transformations of all parent nodes. Every time a game object or any of its parent nodes is moved, this global transform is updated.

Game objects are described in more detail in [this chapter](game-objects.md).

### ezComponent

Components can be attached to game objects. They bring their own data and functionality. Components are used to implement behavior. For example light source components are used to tell the renderer how to light the scene, physics components are used to make objects collide with each other and AI components let creatures run around. By attaching components to game objects, you configure how that game object behaves. Components can interact with or depend on each other. For example a physics *actor* component would make an object fall to the ground, but it also needs a physics *shape* component to know whether the object should behave like a box, a sphere or something else.

Components are described in more detail in [this chapter](components.md).

### ezWorldModule / ezComponentManager

World modules are the *systems* of the ECS pattern. Worlds are updated in multiple phases. Some phases are multi-threaded, others aren't. World modules can hook into these phases and make sure that they are called at the right time. World modules implement things like stepping third party code (e.g. physics). The most common type of world modules are *component managers*. Each component type has its own component manager, which is responsible for updating those components. The manager can leverage knowledge from other sources for determining which components need updating, and it can easily update components in a multi-threaded fashion, if it is save to do so.

World modules are described in more detail in [this chapter](world-modules.md) and component managers in [this chapter](component-managers.md).

## Object Lifetime

The EZ scenegraph does not use any kind of reference counting or garbage collection, however it does provide weak reference semantics through *handles*, to enable you to delete objects exactly when you need them to be removed, while still being able to detect whether an object is still alive.

See the [object lifetime chapter](object-lifetime.md) for details.

## Custom Components

A large part of writing your own game, is to write your own components. If you need maximum control and performance, you need to write your [components in C++](../../custom-code/cpp/custom-cpp-component.md).

You can also write components in [TypeScript](../../custom-code/typescript/typescript-overview.md). Their functionality is very similar but a bit more limited. It is possible to use both and communicate between Typescript and C++ components using [messages](world-messaging.md).

## Messaging

When a component gets updated, it can access other components and call functions on them. Of course that requires that the other component type is known at compile time. In practice, that is often not the case.

Take the [projectile component](../../gameplay/projectile-component.md) as an example. Whenever a projectile hits something, it should apply damage to the hit object. However, what it hit was just the physical representation of an object (e.g. a [physics actor](../../physics/actors/physx-actors.md)). The physics object doesn't have a concept of 'receiving damage' and therefore calling some 'OnDamage' function on the physics component makes no sense.

Instead, on the object that has the physics component, there may be another component which knows how it would react to damage, so we want to send the information there. That component may be a custom component, though, which the projectile component knows nothing about, so there is no way to call a function on that.

To solve this problem, you can send *messages* to components. A message is a class derived from `ezMessage` and it can contain arbitrary data. Each component registers *message handlers* for all the types of messages that it wants to receive.

When our projectile component now hits some object, it simply sends a *damage message* to that object. The engine will then deliver that message to all components which have a matching message handler. The message can be delivered right away, in which case a result can be written back to the message, or with a delay.

Using messages decouples code, as components that know nothing of each other can still communicate and interact. The message system is also highly optimized for best performance.

Messages are described in more detail in [this chapter](world-messaging.md).

## Spatial System

The world also sorts objects into a spatial system, to enable efficient queries for which objects are within a certain area. Although this is the basis for frustum culling in the renderer, it is also available to other systems.

See [this chapter](spatial-system.md) for details.

## See Also


* [Worlds](worlds.md)
* [Game Objects](game-objects.md)
* [Components](components.md)
* [World Modules](world-modules.md)
* [Component Managers](component-managers.md)
* [Messaging](world-messaging.md)
* [Custom Code](../../custom-code/custom-code-overview.md)
