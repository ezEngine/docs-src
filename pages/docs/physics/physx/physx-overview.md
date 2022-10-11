# PhysX Integration

[NVIDIA PhysX](https://github.com/NVIDIAGameWorks/PhysX) is an open source physics engine. It computes the physical interactions between objects using [rigid body dynamics](https://en.wikipedia.org/wiki/Rigid_body_dynamics).

Physics engines are a vital part in most 3D games, to make objects collide and interact with each other convincingly. An important feature are also *raycasts* and *shape queries* which are used to detect objects and analyze the state of the world.

## Enable PhysX Support

See [CMake Setup](../../build/cmake-config.md) on how to enable PhysX support in your build. In pre-compiled release packages, PhysX support is enabled.

## Working with PhysX

The most important PhysX functionality is exposed through components, as well as through [TypeScript](../../custom-code/typescript/typescript-overview.md).

When you write custom C++ code, you can access the most important functionality, like raycasts and shape queries, through the abstract `ezPhysicsWorldModuleInterface`, which is implementation independent. If you need to access PhysX features that are not exposed in EZ, you can cast that interface to `ezPhysXWorldModule` and directly work with `PxScene`. For PhysX details, refer to its [documentation](https://gameworksdocs.nvidia.com/simulation.html).

## Feature Overview

You use components to tell PhysX which objects should be considered for its simulation, and how. In PhysX objects participating in the simulation are called *actors* but they are often also referred to as *bodies*.

How to set up actors [is described here](actors/physx-actors.md). Reading up on actors is the best starting point.

Actors are made up of shapes, such as spheres, boxes, capsules and meshes. Shapes are [described here](collision-shapes/physx-shapes.md).

Actors can be physically linked, to constrain their movement. This is how you would set up a door hinge for example. Linking two actors is accomplished using [joints](joints/physx-joints.md).

To make a player or NPC walk through a physically simulated scene, you need something that computes how the character collides with walls, climbs stairs, slides down slopes, and so on. This functionality is provided by a so called [character controller](special/physx-character-controller.md).

Often games have invisible areas that either need to be reached as a goal, or that activate something. Such areas are called [triggers](actors/physx-trigger-component.md).

Several non-PhysX components either use the available physics engine, or even expose new functionality. For example the [raycast placement component](../../gameplay/raycast-placement-component.md) does a raycast (using the abstract physics interface) and exposes the hit position to the user by moving a linked object there. The [area damage component](../../gameplay/area-damage-component.md) does a shape query and both damages and pushes the found physical objects.

## See Also


* [NVIDIA PhysX](https://github.com/NVIDIAGameWorks/PhysX)
* [PhysX Actors](actors/physx-actors.md)
