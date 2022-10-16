# Worlds

For an introduction what a world is and how it fits into the overall picture, see [The World / Scenegraph System](world-overview.md).

This documentation focuses on the C++ `ezWorld` class. The functionality exposed through other mechanisms, such as [TypeScript](../../custom-code/typescript/typescript-overview.md), may be more limited in scope, but ultimately maps to the C++ implementation.

## Game Objects

Game objects are allocated, destroyed and accessed through the world. For these details, see the chapter about [game objects](game-objects.md).

## Components

Components are not directly managed by a world. Instead, worlds manage [world modules](world-modules.md) and [component managers](component-managers.md), which in turn manage components. For details, see the chapter about [components](components.md).

## World Modules

World modules are bigger systems that manage aspects like [particle effects](../../effects/particle-effects/particle-effects-overview.md), the [Jolt integration](../../physics/jolt/jolt-overview.md), [wind](../../effects/wind.md) and so on. [Component managers](component-managers.md) are a special type of world modules that take care of updating the various component types.

## Simulation State

Each world has its own simulation state, to not affect other worlds.

### Simulation Enabled

Every world can be actively simulated, or paused. `ezWorld::SetWorldSimulationEnabled()` is used to toggle this.

### Clock

Each world has its own `ezClock` which can be retrieved through `ezWorld::GetClock()`. The clock is used to speed up or slow down the simulation or to set a fixed update rate. The clock keeps track of the 'game time', so when a component needs to know the current time, it should query this from the world's clock.

### Random Number Generator

When a component needs a random number, it should query this from the world via `ezWorld::GetRandomNumberGenerator()`. Components or better, [component managers](component-managers.md) can of course also have their own random number generator, for example when they need multi-threaded access to it, or when they want to control the seed value for determinism. The [particle systems](../../effects/particle-effects/particle-effects-overview.md), for example, do this to achieve deterministic results.

### Coordinate System

The default coordinate system in EZ is:

* `+X` is 'forwards'
* `+Y` is 'right`
* `+Z` is 'up'

That makes it a left-handed coordinate system. You can query these axis in the space of a [game object](game-objects.md), if you need to.

The coordinate system can be changed through `ezWorld::SetCoordinateSystemProvider()`. The `ezCoordinateSystemProvider` can potentially return a different coordinate system at different locations, so you could implement a provider that changes the coordinate system to follow a sphere.

> **Warning:**
>
> Although components are supposed to not hard-code assumptions about which axis is 'forward', etc, using a non-default coordinate system is not well tested. Using a dynamic coordinate system even less so.

## Read / Write Access Control

Some aspects of the world are updated in a multi-threaded fashion. For instance, rendering generally happens in parallel to other updates. To prevent you from accessing the world in a problematic way, you need to *lock* the world for reading or writing when you work with it.

From within a component update function you don't need to worry, you always have write access to the world while components are being updated. However, if for example you want to load a level or otherwise set it up procedurally at launch, you need to lock it for write access:

```cpp
EZ_LOCK(pWorld->GetWriteMarker());
pWorld->CreateObject(...)
```

In developer builds the world will check that you have properly locked it when you try to do certain operations. Therefore, the best way to know where to add such locks, is simply to run your code without a lock and see whether the engine asserts. If so, you can just traverse your callstack to find a reasonable place to insert the lock.

## World Update

To step your world, call `ezWorld::Update()`. The time delta that will be applied depends on whether the [world simulation is enabled](#simulation-enabled) and how your [world clock](#clock) is configured.

## See Also


* [Game Objects](game-objects.md)
* [Components](components.md)
* [World Modules](world-modules.md)
* [Object Lifetime](object-lifetime.md)
* [Messaging](world-messaging.md)
