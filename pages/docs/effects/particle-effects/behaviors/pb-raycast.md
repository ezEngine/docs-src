# Raycast Behavior

This behavior uses raycasts to detect collisions along the trajectory of a particle. If a particle would collide with geometry, the behavior can either adjust the its velocity, or terminate the particle early, potentially raising an [event](../particle-effects-overview.md#events-and-event-reactions), which could in turn lead to other effects or being spawned.

**Reaction:** Specifies how the particle should react to a collision.

* *Bounce:* The particle's velocity will be adjusted such that it bounces off the hit surface.
* *Die:* The particle will be killed early.
* *Stop:* The particle's current velocity will be set to zero, thus stopping it in its tracks. If other position affecting behaviors are active, for example the [gravity behavior](pb-gravity.md), it will start moving again, but without its previous momentum.

**BounceFactor:** How much of the current speed should be preserved after the bounce.

**CollisionLayer:** The physics collision layer to use. Affects with which geometry the particle will collide and which it will pass through.

**OnCollideEvent:** An optional name of an [event](../particle-effects-overview.md#events-and-event-reactions) to raise. If set, other effects or prefabs can be spawned at the location of impact.

<video src="../media/raycast.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
