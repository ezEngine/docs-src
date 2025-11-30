# Color Gradient Behavior

This behavior changes a particle's color during the update step. A [color gradient](../../../animation/common/color-gradients.md) is used as the color source, and a mode specifies how to look up the color from the gradient.

**Gradient:** The [color gradient](../../../animation/common/color-gradients.md) to use as the source.

**TintColor:** An additional color to be multiplied into the gradient, for tweaking the final result.

**ColorFrom:** This mode specifies how the color is looked up from the gradient:

* `Age` - In this mode the particle's color depends on its age and remaining lifetime. That means it starts out with the leftmost color from the gradient and transitions towards the rightmost color. Optimally, the color gradient should include alpha values, such that the particles can fade out towards the end.
* `Speed` - In this mode the particle's color is determined from its current speed. Slow particles are assigned colors from the left side of the gradient, fast particles that from the right side. This mode only makes sense when either every particle gets a random speed assigned, or when its speed is able to change over time, due to friction, gravity or other factors.

**MaxSpeed:** When using *ColorFrom = Speed*, this value specifies the maximum expected speed of any particle. That speed is then mapped to the rightmost side of the color gradient.

<video src="../media/color-gradient.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
