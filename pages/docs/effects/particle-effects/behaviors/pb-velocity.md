# Velocity Behavior

This behavior affects particle position and velocity. It can be used to gradually dampen the starting velocity through 'friction' and it may apply a constant upwards movement. If a scene contains [wind](../wind/wind.md), this behavior can also apply a fraction of the wind force to the particle's position.

**RiseSpeed:** If non-zero, the particles will move upwards with at least this constant speed. This is added to the particle position independent from its velocity, so if the current velocity points downward, the two may cancel each other out.

**Friction:** This value imitates air friction. If it is non-zero, the particle's velocity will be dampened over time. The value's range is `[0; infinity]`. To achieve an effect as in the animation below, the particles must have a very large starting velocity (here: 10). The *friction* here is set to 6. This way the particles will appear to be quite fast, but will also get slowed down almost to a standstill within a fraction of a second.

**WindInfluence:** If the scene has wind, this value specifies how much the wind should be able to push the particles around.

<video src="../media/velocity.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
