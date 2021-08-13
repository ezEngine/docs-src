# PhysX Dynamic Actor Component

The *PhysX dynamic actor component* is used to add physical behavior to an object. Dynamic actors are also referred to as *rigid bodies*. They are simulated by the physics engine.

<video src="media/dynamic-actor.webm" width="600" height="600" autoplay loop></video>

## Kinematic vs. Simulated

Dynamic actors can be in one of two modes: *fully simulated* or *kinematic*. For a kinematic body, the game code dictates its position and rotation, and the physics engine uses this information to push simulated objects out of their way. Kinematic actors are typically used for elevators, doors and other large pieces that are supposed to push other objects away and strictly follow an animation without any physical simulation of their movement.

Non-kinematic, or fully simulated objects on the other hand, are fully controlled by the physics engine. Their position and rotation is determined by forces, such as gravity, acting on them, as well as what other static and dynamic objects they collide with. Setting the position of such an actor has no effect, the physics engine will override the value with its own result. To affect a simulated object, you can apply external **forces** and **impulses**. For example the [area damage component](../../gameplay/area-damage-component.md) applies an outward impulse to all rigid bodies in its vicinity to push them away.

Whether a dynamic actor is kinematic or not is simply a flag and it is possible to toggle that state back and forth at runtime. This for example allows to animate an object along a predetermined path by making it kinematic at first, and then switch it to simulated at the end of its animation, to make it fall and collide realistically from there on. In the video below a [property animation (TODO)](../../animation/property-animation/property-animation-overview.md) was used to do exactly that:

<video src="media/kinematic-switch.webm" width="600" height="600" autoplay loop></video>

## Mass vs. Density

Dynamic actors have a weight. The weight determines how much force it takes to push them and how much they push other rigid bodies. There are two ways to adjust an actor's weight. If you set the `Mass` property, this is the bodies absolute weight no matter its size and shape. Thus a small stone with mass 10 (kilogram) will appear heavy whereas a huge boulder also with mass 10 will appear light.

The other way is to set its `Density` property instead. In this case the volume of all the attached [shapes](../collision-shapes/physx-shapes.md) is computed and scaled by the density. That means the object's final mass will depend on its scale, so a small stone would get a weight of 0.5 (kilogram) whereas a huge boulder would get a weight of 1000 kg.

Using densities is more convenient to get started. The default density often already produces believable results. If you create a [prefab](../../prefabs/prefabs-overview.md) that is supposed to be instantiated at various sizes, it is best to use density.

> **Important:**
>
> Physics engines are notoriously bad at dealing with large mass differences. Objects should never be too light or too heavy in general. Objects with a mass below 1 tend to be flung away at ridiculous speeds when they are pushed by heavy objects. Objects with a mass above 100 should be avoided as well.

Due to these limitations, it is not advisable to use realistic weights for objects, as many objects would become too light and their simulation would suffer from erratic behavior. Instead, choose a weight somewhere in the 0.5 to 100 range that looks good enough.

Consequently, it can often be easier to specify their value as an absolute `Mass`, instead of trying to achieve the same through the indirect `Density`.

## Center of Mass

The center of mass is automatically computed from the attached shapes. If the result does not match your expectation, you can adjust the center of mass by adding a [center of mass component](../collision-shapes/physx-center-of-mass-component.md).

## Simulation Stability

Simulated rigid bodies may not act as desired. Some bodies jitter and don't come to rest, others fly off at high speeds after collisions. Some objects may even *tunnel* through walls, meaning that instead of colliding properly with a wall, they manage to get to the other side.

These are all known issues with real-time physics engines. With the limited available computational power they have to do many approximations to achieve the desired real-time performance.

Consequently, you have to be careful how you set up your rigid-bodies, to improve simulation stability:

* **Avoid small and thin objects:** Thin objects are always problematic. For small objects, consider making their collision shape as large as possible, potentially larger than the graphical representation.
* **Avoid very heavy and very light objects:** See [Mass vs. Density](#mass-vs-density) above for details.
* **Reduce the maximum contact impulse:** When two objects collide, they apply *impulses* to each other. Small or thin objects can act erratic, with large impulses. If this is a problem for an object, you can reduce the `MaxContactImpulse` that shall be applied to it, to prevent it being flung away at high speeds. Be careful though, tweaking this parameter can have unintended side effects as well.
* **Use Continuous Collision Detection (CCD) for important small objects:** Continuous collision detection is mainly used to prevent objects from *tunneling* through other objects. For example a physically simulated grenade may be thrown at a high speed, which means it is prone to get through walls. This is less likely to happen for larger objects. CCD costs extra performance for every object on which it is used, but significantly reduces the likelihood for tunneling to happen.
* **Increase angular damping:** Some objects tend to spin too fast after collisions. By increasing angular damping, you can make them come to rest more quickly.
* **Reduce the complexity of the shape:** Especially [convex meshes](../collision-shapes/collision-meshes.md) are prone to *jittering* when the mesh has long thin triangles. Build convex meshes by hand to control their complexity, if an automatically created convex mesh results in unstable behavior.

## Component Properties

* `Kinematic`: See [Kinematic vs. Simulated](#kinematic-vs-simulated) above.
* `Mass`, `Density`: See [Mass vs. Density](#mass-vs-density) above.
* `DisableGravity`: If set, no gravity is applied to this actor, and it will float in space.
* `LinearDamping`, `AngularDamping`: The damping properties affect how quickly an actor loses momentum and comes to rest. This can be adjusted separately for positional (linear) movement and rotational (angular) movement.
* `MaxContactImpulse`: See [Simulation Stability](#simulation-stability) above.
* `ContinuousCollisionDetection`: See [Simulation Stability](#simulation-stability) above.
* `LockingFlags`: These flags can be used to prevent movement or rotation along one or multiple axis (in global space). This can be useful to make 2D games where objects shall only move in a plane. It can also be used to create objects that can't be tipped over, or to immitate basic constraints. Be aware that forces acting on such locked objects may be partially lost. It is therefore much harder to push a locked object along the floor, when friction would introduce a motion that is not allowed on this object. Reduce the objects mass to compensate.

## See Also


* [PhysX Static Actor Component](physx-static-actor-component.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Physics Joints](../joints/physx-joints.md)
