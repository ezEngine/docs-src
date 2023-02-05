# Jolt Physics Integration

[Jolt Physics](https://github.com/jrouwe/JoltPhysics) is an open source physics engine. It computes the physical interactions between objects using [rigid body dynamics](https://en.wikipedia.org/wiki/Rigid_body_dynamics).

Physics engines are a vital part in most 3D games, to make objects collide and interact with each other convincingly. An important feature are also *raycasts* and *shape queries* which are used to detect objects and analyze the state of the world.

## Enable Jolt Support

Support for Jolt is enabled by default on all platforms. It can be disabled in the [CMake config](../../build/cmake-config.md).

## Working with Jolt

The most important Jolt functionality is exposed through components, as well as through [TypeScript](../../custom-code/typescript/typescript-overview.md).

When you write custom C++ code, you can access the most important functionality, like raycasts and shape queries, through the abstract `ezPhysicsWorldModuleInterface`, which is implementation independent. If you need to access Jolt features that are not exposed in EZ, you can cast that interface to `ezJoltWorldModule` and directly work with the `JPH::PhysicsSystem`. For Jolt details, refer to its [documentation](https://github.com/jrouwe/JoltPhysics).

## Feature Overview

You use components to tell Jolt which objects should be considered for its simulation, and how. In Jolt, objects participating in the simulation are called *bodies* but in EZ they are usually referred to as *actors*.

How to set up actors [is described here](actors/jolt-actors.md). Reading up on actors is the best starting point.

Actors are made up of shapes, such as spheres, boxes, capsules and meshes. Shapes are [described here](collision-shapes/jolt-shapes.md).

Actors can be physically linked, to constrain their movement. This is how you would set up a door hinge for example. Linking two actors is accomplished using [constraints](constraints/jolt-constraints.md).

To make a player or NPC walk through a physically simulated scene, you need something that computes how the character collides with walls, climbs stairs, slides down slopes, and so on. This functionality is provided by a so called [character controller](special/jolt-character-controller.md).

Often games have invisible areas that either need to be reached as a goal, or that activate something. Such areas are called [triggers](actors/jolt-trigger-component.md).

Several non-Jolt components either use the available physics engine, or even expose new functionality. For example the [raycast placement component](../../gameplay/raycast-placement-component.md) does a raycast (using the abstract physics interface) and exposes the hit position to the user by moving a linked object there. The [area damage component](../../gameplay/area-damage-component.md) does a shape query and both damages and pushes the found physical objects.

## Video: How to create a physics object

[![video](https://img.youtube.com/vi/hlEUdO5yVig/0.jpg)](https://www.youtube.com/watch?v=hlEUdO5yVig)

## See Also

* [Jolt Physics](https://github.com/jrouwe/JoltPhysics)
* [Jolt Architecture](https://jrouwe.github.io/JoltPhysics)
* [Jolt Actors](actors/jolt-actors.md)
