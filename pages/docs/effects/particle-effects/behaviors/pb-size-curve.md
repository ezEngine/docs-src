# Size Curve Behavior

This behavior changes a particle's size over the course of its lifetime.

**SizeCurve:** A [curve](../../../animation/common/curves.md) which is used to look up the size of the particle. The current fraction of the particle's lifespan is used for the lookup along the X axis. The absolute X and Y values in the curve don't matter, the curve is normalized to `[0; 1]` range.

**BaseSize:** The particles will always have at least this size, the rest is added on top.

**CurveScale:** Specifies what value the largest value in the curve maps to. That means at the peak of a curve, the particle's size will be `BaseSize + CurveScale`.

<video src="../media/size-curve.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
