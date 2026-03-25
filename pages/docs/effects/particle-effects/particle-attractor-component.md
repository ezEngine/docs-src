# Particle Attractor Component

The *Particle Attractor Component* defines a point in the world that attracts or repels nearby particles. Particle systems that use the [attract behavior](behaviors/pb-attract.md) discover attractor components automatically and apply their forces to their particles.

A single attractor can be used to suck particles into a hole or have them orbit something. Multiple attractors in the same area can be used to create complex patterns, especially if the attractors themselves are also moving. Attractors exhibit a constant force, they are not meant for burst, such as explosions. If that is desired, custom logic to control their behavior is needed. For explosion effects, prefer to use [wind volumes](../wind/wind-volume-components.md) and the [wind behavior](behaviors/pb-wind.md), as wind will have an effect on many more things in the world.

<video src="media/attractors.mp4" width="500" height="500" autoplay loop></video>

## Component Properties

**Radius:** The sphere of influence. Particles further away than this distance are not affected.

**Strength:** The attraction force that gets applied. The force falls off linearly from full strength at `MinDistance` to zero at `Radius`. Set this to a negative value to repel particles instead of attracting them.

**MinDistance:** The inner radius below which the force no longer increases. This prevents a singularity at the attractor's center and keeps particles from accelerating uncontrollably when they get very close. If set to larger values, it can also be used to push or pull only particles that touch the sphere, but then let them continue normally once they are inside.

**KillDistance:** Particles that come closer than this distance are destroyed. Set to zero to disable the kill zone. The kill zone can be used, for example, to simulate particles being consumed by a vortex.

## See Also

* [Attract Behavior](behaviors/pb-attract.md)
* [Particle Effects](particle-effects-overview.md)
* [Particle Behaviors](particle-behaviors.md)
