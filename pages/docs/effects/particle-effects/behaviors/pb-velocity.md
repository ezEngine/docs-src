# Velocity Behavior

This behavior affects particle velocity over time. It can be used to gradually dampen the starting velocity through friction or to control the particle speed using a curve.

**Friction:** This value imitates air friction. If it is non-zero, the particle's velocity will be dampened over time. The value's range is `[0; infinity]`. To achieve an effect as in the animation below, the particles must have a very large starting velocity (here: 10). The *friction* here is set to 6. This way the particles will appear to be quite fast, but will also get slowed down almost to a standstill within a fraction of a second.

**SpeedCurve:** A [curve](../../../animation/common/curves.md) that controls the particle speed over its lifetime. This allows for more precise control over how fast particles move at different stages of their life.

<video src="../media/velocity.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
