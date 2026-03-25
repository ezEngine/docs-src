# Attract Behavior

<video src="../media/attractors.mp4" width="500" height="500" autoplay loop></video>

This behavior pulls particles toward [Particle Attractor Components](../particle-attractor-component.md) placed in the scene.

The attractor's force falls off linearly from full strength at the attractor's minimum distance to zero at its outer radius. Particles that enter the attractor's kill zone are destroyed.

**Influence:** A scale factor applied on top of the attractor's own strength. Use this to tune how strongly the particle system reacts without changing the attractor component itself.

**AffectVelocity:** When enabled, the attract force modifies particle velocity, producing a physically plausible spiral or arc toward the attractor. When disabled, particle positions are moved directly, which creates a snapping effect that is stronger but less physically correct.

**MaxAttractors:** The maximum number of nearby attractors considered per update. Increasing this allows particles to respond to several attractors at once but costs more performance.

## See Also

* [Particle Attractor Component](../particle-attractor-component.md)
* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
