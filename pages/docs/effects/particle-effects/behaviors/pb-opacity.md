# Opacity Behavior

This behavior changes a particle's opacity over the course of its lifetime using a curve.

**OpacityCurve:** A [curve](../../../animation/common/curves.md) which controls the opacity of the particle over its lifetime. The current fraction of the particle's lifespan is used for the lookup along the X axis. A value of 1 means fully opaque, 0 means fully transparent.

This behavior provides more control over particle transparency than the simpler [Fade Out Behavior](pb-fade-out.md), allowing for effects like particles that fade in, stay visible, and then fade out.

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Fade Out Behavior](pb-fade-out.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
