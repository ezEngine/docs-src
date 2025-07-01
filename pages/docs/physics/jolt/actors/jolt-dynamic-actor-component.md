# Jolt Dynamic Actor Component

The *Jolt dynamic actor component* is used to add physical behavior to an object. Dynamic actors are also referred to as *rigid bodies*. They are simulated by the physics engine.

<video src="media/dynamic-actor.webm" width="600" height="600" autoplay loop></video>

## Kinematic vs. Simulated

Dynamic actors can be in one of two modes: *fully simulated* or *kinematic*. For a kinematic body, the game code dictates its position and rotation, and the physics engine uses this information to push simulated objects out of their way. Kinematic actors are typically used for elevators, doors and other large pieces that are supposed to push other objects away and strictly follow an animation without any physical simulation of their movement.

Non-kinematic, or fully simulated objects on the other hand, are fully controlled by the physics engine. Their position and rotation is determined by forces, such as gravity, acting on them, as well as what other static and dynamic objects they collide with. Setting the position of such an actor has no effect, the physics engine will override the value with its own result. To affect a simulated object, you can apply external **forces** and **impulses**. For example the [area damage component](../../../gameplay/area-damage-component.md) applies an outward impulse to all rigid bodies in its vicinity to push them away.

Whether a dynamic actor is kinematic or not is simply a flag and it is possible to toggle that state back and forth at runtime. This for example allows to animate an object along a predetermined path by making it kinematic at first, and then switch it to simulated at the end of its animation, to make it fall and collide realistically from there on. In the video below a [property animation (TODO)](../../../animation/property-animation/property-animation-overview.md) was used to do exactly that:

<video src="media/kinematic-switch.webm" width="600" height="600" autoplay loop></video>

## Actor Mass

Every dynamic actor needs to have a mass, to simulate how it behaves when it interacts with other rigid bodies.

However, physics engines don't work well with real-world masses, which makes tweaking mass values difficult. Therefore EZ adds a layer of indirection to let you configure masses in one central place, the so-called *weight categories*.

For more details, please see the chapter about [weights and forces](../concepts/weights-forces.md).

## Center Of Mass

The *center of mass* (COM) is the point in space around which an actor spins when a force is applied to it. The COM is computed automatically from the shapes and their masses. It sometimes ends up too high and makes objects tip over too easily. To adjust the center of mass, enable the property `CustomCenterOfMass` and edit the `CenterOfMass` property value.

## OnContact Reactions

TODO

## Simulation Stability

Simulated rigid bodies may not act as desired. Some bodies jitter and don't come to rest, others fly off at high speeds after collisions. Some objects may even *tunnel* through walls, meaning that instead of colliding properly with a wall, they manage to get to the other side.

These are all known issues with real-time physics engines. With the limited available computational power they have to do many approximations to achieve the desired real-time performance.

Consequently, you have to be careful how you set up your rigid-bodies, to improve simulation stability:

* **Avoid small and thin objects:** Thin objects are always problematic. For small objects, consider making their collision shape as large as possible, potentially larger than the graphical representation.
* **Avoid very heavy and very light objects:** See [actor mass](#actor-mass) above for details.
* **Use Continuous Collision Detection (CCD) for important small objects:** Continuous collision detection is mainly used to prevent objects from *tunneling* through other objects. For example a physically simulated grenade may be thrown at a high speed, which means it is prone to get through walls. This is less likely to happen for larger objects. CCD costs extra performance for every object on which it is used, but significantly reduces the likelihood for tunneling to happen.
* **Increase angular damping:** Some objects tend to spin too fast after collisions. By increasing angular damping, you can make them come to rest more quickly.
* **Reduce the complexity of the shape:** Especially [convex meshes](../collision-shapes/jolt-collision-meshes.md) are prone to *jittering* when the mesh has long thin triangles. Build convex meshes by hand to control their complexity, if an automatically created convex mesh results in unstable behavior.

## Component Properties

* `CollisionLayer`: The [collision layer](../collision-shapes/jolt-collision-layers.md) to use.
* `Kinematic`: See [Kinematic vs. Simulated](#kinematic-vs-simulated) above.
* `StartAsleep`: If enabled, the actor starts in the 'sleeping' state and will not be physically simulated until it gets into contact with another active actor. This is a performance optimization to prevent performance spikes after loading a level. If used badly, an object can float in air and not fall down until something else touches it. Make sure to only use this on objects that are [convincingly placed](../../../editor/run-scene.md#keep-simulation-changes) to begin with.
* `WeightCategory`, `WeightScale`: See [actor mass](#actor-mass) above.
* `Surface`: The [surface](../../../materials/surfaces.md) to use for this actor's shapes. The surface determines the friction and restitution during simulation, but also determines what effects are spawned when you interact with the object. Note that [collision meshes](../collision-shapes/jolt-collision-meshes.md) already specify the surface to use. If a surface is selected on the actor, it overrides the mesh's surface.
* `GravityFactor`: Adjusts the influence of gravity on this object. If set to zero, it will float in space.
* `LinearDamping`, `AngularDamping`: The damping properties affect how quickly an actor loses momentum and comes to rest. This can be adjusted separately for positional (linear) movement and rotational (angular) movement.
* `ContinuousCollisionDetection`: See [Simulation Stability](#simulation-stability) above.
* `OnContact`: See [OnContact Reactions](#oncontact-reactions) above.
* `CustomCenterOfMass`, `CenterOfMass`: See [Center Of Mass](#center-of-mass) above.

## See Also

* [Jolt Static Actor Component](jolt-static-actor-component.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
* [Jolt Constraints](../constraints/jolt-constraints.md)
* [Weights and Forces](../concepts/weights-forces.md)
