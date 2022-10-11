# Physics Joints

A *PhysX joint* is a component that links [PhysX actors](../actors/physx-actors.md) to constrain their movement. There are multiple types of joints that each constrain the actors in different ways.

Joints can be used for simple things like door hinges, up to complex configurations like rag dolls.

## Joining Actors

Joints can be used to link:

* Two [dynamic actors](../actors/physx-dynamic-actor-component.md). This will create a more complex dynamic object that can still freely move throughout the scene, but has multiple parts that can wiggle around.
* One [static actor](../actors/physx-static-actor-component.md) with one [dynamic actor](../actors/physx-dynamic-actor-component.md). In this case the dynamic actor is now constrained in its movement relative to the static actor. Since the static actor never moves, the dynamic actor's freedom is severely limited.
* One [dynamic actor](../actors/physx-dynamic-actor-component.md) with no second actor. This just affixes the dynamic actor with 'the world'. This is effectively the same as joining it with another static actor.
* One [dynamic actor](../actors/physx-dynamic-actor-component.md) with one [kinematic actor](../actors/physx-dynamic-actor-component.md#kinematic-vs-simulated). If the kinematic actor moves, the dynamic actor is forced to follow according to the constraint between them. The dynamic actor does not affect the kinematic actor in any way. This setup is common to have full control over the movement of one part (the kinematic actor) and still get physically plausible behavior from another part.

There are two ways that a joint component can link actors.

### Using Object References

You can use the [object references](../../../scenes/object-references.md) on the joint component to specify both the *parent actor* and the *child actor*:

![Linking Actors](media/link-joints.png)

With this method, the [game objects](../../../runtime/world/game-objects.md) for the actors and the joint don't need to have a specific hierarchy, they can be placed just next to each other. This also allows to create *loops* of linked actors. On the other hand, you always need to know exactly which actors shall be linked.

> **Note:**
>
> The `Child Actor` of a joint always has to be specified this way.

### Using the Object Hierarchy

To determine which `Parent Actor` to link the joint to, you can utilize the object hierarchy. If no parent actor is specified as an object reference, the joint will automatically traverse its object hierarchy upwards and search for the closest object with a static or dynamic actor. If it finds one, the joint will link to that object as the parent actor.

If it does not find any such actor on a parent node, the joint will attach to 'the world', meaning it will be fixed to its current world position.

This method can be useful especially when you want to put the joint into a [prefab](../../../prefabs/prefabs-overview.md). For example, if you have a prefab for a chandelier that can swing around, you can set up the joint to only reference the actor that represents the chandelier, but the prefab does not contain an actor for the anchor point. If this prefab is placed into a scene, the rule that a joint *without* a parent actor just gets linked to the world, means that you can easily place these prefabs in a scene, and they will swing around the location where they have been instantiated.

However, if your scene contains for example a moveable room, you can also place it there and make sure to attach the chandelier prefab as a child node of the moveable room actor. That means, the joint of the chandelier will now link the chandelier actor with the moveable room actor, and thus whenever the room moves, the chandelier will be physically dragged along as well.

> **Important:**
>
> This method of linking actors only works properly, if the parent actor is either **static** or **kinematic**. It doesn't work for simulated dynamic actors, as the transform update introduces jitter.

## Joint Position

The position and rotation of a joint object specifies the pivot point. For [revolute joints](physx-revolute-joint-component.md), [spherical joints](physx-spherical-joint-component.md) and [6DOF joints](physx-6dof-joint-component.md) the position of the joint determines around which point the linked actors rotate. For [fixed joints](physx-fixed-joint-component.md) the position still affects how strong forces may become due to lever effects.

For [distance joints](physx-distance-joint-component.md) the joint position determines from where the distance is computed. Only for [prismatic joints](physx-prismatic-joint-component.md) is the position of the joint less relevant, though for computational stability, it should still be somewhere in between the linked actors.

## Video: Basic Setup

[![video](https://img.youtube.com/vi/r3wVz3Xd8xU/0.jpg)](https://www.youtube.com/watch?v=r3wVz3Xd8xU)

## Using the ChildActorAnchor Property

Using the `ChildActorAnchor` property is entirely optional and often not needed. Basically this option is used to reference any object, and tell the joint that the position and orientation of that object should be the anchor point where the joint acts upon the child actor. For most joint types this is rarely needed. If you link two actors with a revolute joint, the position of the joint already defines where between the actors the hinge will be.

However, this setup always assumes that the two actors should start out in the 'default configuration' of the joint. For example, for a revolute joint with a stiff spring, the default configuration is when it is fully relaxed, meaning you could not put them into a start configuration where the joint is already under tension.

Similarly, for a distance joint, the child actor would always need to start out such that the joint position is exactly at the position of the actor, where it should link to the actor. This can be problematic especially when the distance joint uses a *minimum distance*, as the joint would immediately push away the actor, potentially with high speed.

Using a dedicated object to specify the anchor point, both situations can be fixed. The anchor point specifies the position at which the joint affects the child actor. For most joint types the rotation of the anchor point is important as well. If the anchor's transform is identical to the joint's transform, it is redundant and could be left out. However, if it is different from the joint's transform, this difference basically tells the joint how much its start state deviates from the 'default configuration'. For example for a revolute joint the position of the anchor should always be identical to the joint's position, otherwise the child actor will jerk towards the revolute joint at startup. However, the rotation may deviate from the joint's rotation, which specifies how much the joint is already rotated at startup.

### Video: How to use the Anchor Property

[![video](https://img.youtube.com/vi/xnQEaA8E0SM/0.jpg)](https://www.youtube.com/watch?v=xnQEaA8E0SM)

## Shared Joint Component Properties

These properties are shared among all joint types:

* `BreakForce`, `BreakTorque`: By specifying non-zero values here, the joint is turned into a *breakable* joint. If enough force is applied to the joint, it will break apart and the two actors are not linked any further. Unfortunately it can be tricky to choose a proper break threshold, especially for torques, as some interactions produce surprisingly large forces, whereas other actions don't.
* `PairCollision`: By default actors that are linked with a joint will not collide with each other, instead they will pass through each other. Some joints have options that won't allow such situations to happen, and those options are always more efficient and preferable. However, you can also enable this, to have the two actors still collide with each other.
* `ParentActor`, `ChildActor`: References to objects with [actor components](../actors/physx-actors.md) to link with this joint. If not set, the parent/child hierarchy is used instead. See [joining actors](#joining-actors) above.
* `ChildActorAnchor`: An optional reference to an object that tells the joint where it should attach to the child actor. See [using the ChildActorAnchor property](#using-the-childactoranchor-property) above.

## Joint Types

These types of constraints are currently available:

* [PhysX Revolute Joint Component](physx-revolute-joint-component.md)
* [PhysX Spherical Joint Component](physx-spherical-joint-component.md)
* [PhysX Fixed Joint Component](physx-fixed-joint-component.md)
* [PhysX Prismatic Joint Component](physx-prismatic-joint-component.md)
* [PhysX Distance Joint Component](physx-distance-joint-component.md)
* [PhysX 6DOF Joint Component](physx-6dof-joint-component.md)

## Joint Stability

Joining multiple actors in a chain can quickly result in really bad simulation results. Have a look at [dynamic actor simulation stability](../actors/physx-dynamic-actor-component.md#simulation-stability) for ways to improve this. When working with joints the following aspects help a lot:

* Make sure that the involved actors are not too light. For smaller objects they automatically computed mass is often too low for the joint to be stable.
* Drastically increase linear and especially angular damping on the actors (`0.1` to `0.8`).
* Reduce `MaxContactImpulse`, especially on smaller actors.
* Don't create very long chains, try to achieve the desired result with as few joints as possible.
* Don't use joint limits (revolute joint, spherical joint), they can add significant instability.

Also have a look at NVIDIA's recommendations: [Configuring Joints for Best Behavior (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html#configuring-joints-for-best-behavior)

## See Also

* [PhysX Actors](../actors/physx-actors.md)
* [Joints (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html)
