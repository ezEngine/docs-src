# Turbulence Behavior

This behavior applies a turbulent force to particles. It is useful to make smoke, fire and magical effects look more varied and interesting.

<video src="../media/turbulence.mp4" width="500" height="500" autoplay loop></video>

**Strength:** How much force is applied to particles. Higher values cause more chaotic motion.

**Frequency:** The frequency of the noise pattern. Lower values create large, slow-rolling turbulence; higher values create tighter, more rapid swirls.

**ScrollSpeed:** How fast the noise pattern moves through world space along each axis. Scrolling the noise creates the impression that the flow field is changing over time, which is useful for simulating rising smoke or drifting fog.

**Octaves:** The number of noise octaves used to generate the turbulence field. More octaves add finer detail on top of the base pattern at increased CPU cost. Valid range is 1 to 4. Usually a single octave is sufficient, the difference with multiple octaves is often very hard to make out.

**AffectVelocity:** When enabled, the turbulence force modifies the particles' velocity while preserving their speed, resulting in a physically plausible deflection. When disabled, the force directly offsets particle positions, which produces a stronger visual effect but is less physically correct.

> **Tip:**
>
> To get a better understanding of the impact of each setting, disable `Affect Velocity`. Now you can see the raw impact of the noise values. If you are unsure, keep the `Scroll Speed` at the default level, set `Octaves` to 1, and only play around with high and low values for `Strength` and `Frequency`. Those are the most important values to get you close to the desired result.

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
