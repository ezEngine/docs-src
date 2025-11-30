# Fade Out Behavior

This behavior changes a particle's alpha value to gradually fade out over its lifetime. This behavior can also be achieved using a [color gradient behavior](pb-color-gradient.md), however, the fade out behavior is easier to set up and more efficient at runtime.

**StartAlpha:** The alpha value to begin with when the particle has just spawned.

**Exponent:** How quickly to fade the alpha value from `StartAlpha` towards `0` over the particle's lifespan. An exponent of `1` results in a linear fade. An exponent of `2` will make it fade out much earlier, a value of `0.5` will make it fade out very slowly at first and then quite abruptly at the end.

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
