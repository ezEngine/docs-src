# Pull Along Behavior

Typically once a particle has been spawned, its position is unaffected by changes to the particle effect position. That means when an effect moves around quickly, it may leave a trail of particles behind it, but that trail will be very choppy, unless you have an extremely high particle spawn count and frequency. Thus making something like a rocket exhaust look convincing for a fast moving object can be difficult.

The *pull along behavior* helps to solve this problem by keeping track of any position changes of the particle effect node and applying a fraction of those movements to all the particles' positions as well. This way, if the effect moves a meter, all particles may move 0.8 meters as well. One typically only applies a fraction, such that when the effect moves fast, the particles will be stretched long behind it and not move in perfect unison with the effect node, yielding a more convincing effect.

**Strength:** How much of the effect node's movement should be carried over to the particle positions.

The video below shows two effects beside each other. The left one does not use the pull along behavior, the right one does. As can be seen, the particles on the right stay closer to the moving emitter position.

<video src="../media/pull-along-behavior.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
