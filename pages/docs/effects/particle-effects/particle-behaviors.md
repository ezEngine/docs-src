# Particle Behaviors

This page lists and describes all *particle behaviors*.

## Bounds Behavior

This behavior can be used for atmospheric effects that should be centered around the player, such as rain, snow or mist. The bounds behavior specifies an area in which particles are allowed. When the player moves, and thus the particle effect is moved to a new location, particles would usually stay behind although not being needed anymore. The bounds behavior can make sure to delete those particles. For some effects it is also vital to fill up the new space quickly. This can be achieved with a very high rate of spawning new particles, though this is often not feasible for atmospheric effects. Instead, the bounds behavior can also just teleport the particles that were left behind, to the new area.

**PositionOffset, Extents:** These values define the size and position of the box, relative to the origin of the particle system. With a position offset of `(0, 0, 0)`, the box will be centered around the system's origin.

**OutOfBoundsMode:** Defines what happens for particles that leave the bounding area.

* **Die:** Particles outside the area will be killed right away.
* **Teleport:** Particles leaving one side of the bounding box will be teleported to the other end of the box. This allows the effect to keep a constant density of particles and is therefore useful for effects that should happen around a player, without being simulated completely in the local space of the player, which would prevent things like using the [raycast behavior](#raycast-behavior). Instead, particles can simulate in global space, and only be teleported on demand. Be aware that this teleportation can still break the effect in various ways, because only the *position* and *last position* of each particle is relocated. Behaviors and [particle renderers](particle-renderers.md) that use additional positional data may not work well with this. For example, the [trail renderer's](particle-renderers.md#trail-renderer) position history is not relocated and therefore trails will suddenly stretch through the entire bounding area after a relocation.
Similarly, an effect that uses the [raycast behavior](#raycast-behavior) to prevent tunneling through geometry, may be able to tunnel through walls, if it is being relocated from an unobstructed area to a position where it should not have been able to get to without the teleportation.

## Color Gradient Behavior

This behavior changes a particle's color during the update step. A [color gradient](../../animation/common/color-gradients.md) is used as the color source, and a mode specifies how to look up the color from the gradient.

**Gradient:** The [color gradient](../../animation/common/color-gradients.md) to use as the source.

**TintColor:** An additional color to be multiplied into the gradient, for tweaking the final result.

**ColorFrom:** This mode specifies how the color is looked up from the gradient:

* `Age` - In this mode the particle's color depends on its age and remaining lifetime. That means it starts out with the leftmost color from the gradient and transitions towards the rightmost color. Optimally, the color gradient should include alpha values, such that the particles can fade out towards the end.
* `Speed` - In this mode the particle's color is determined from its current speed. Slow particles are assigned colors from the left side of the gradient, fast particles that from the right side. This mode only makes sense when either every particle gets a random speed assigned, or when its speed is able to change over time, due to friction, gravity or other factors.

**MaxSpeed:** When using *ColorFrom = Speed*, this value specifies the maximum expected speed of any particle. That speed is then mapped to the rightmost side of the color gradient.

<video src="media/color-gradient.webm" width="500" height="500" autoplay loop></video>

## Fade Out Behavior

This behavior changes a particle's alpha value to gradually fade out over its lifetime. This behavior can also be achieved using a [color gradient behavior](#color-gradient-behavior), however, the fade out behavior is easier to set up and more efficient at runtime.

**StartAlpha:** The alpha value to begin with when the particle has just spawned.

**Exponent:** How quickly to fade the alpha value from `StartAlpha` towards `0` over the particle's lifespan. An exponent of `1` results in a linear fade. An exponent of `2` will make it fade out much earlier, a value of `0.5` will make it fade out very slowly at first and then quite abruptly at the end.

## Flies Behavior

This behavior moves particles around the emitter center in erratic patterns, similar to a swarm of flies circling something.

**FlySpeed:** The speed with which the particles move.

**PathLength:** The distance that the particles move into some direction before making another turn. The shorter this is, the more often the particles can change direction and thus the smoother the motion becomes. They will also clump up more and stay within the *MaxEmitterDistance*, if the particles can correct their course more often. With a long *PathLength* they may spread out more.

**MaxEmitterDistance:** The maximum distance that the particles will fly away from the effect's center before turning back. If they travel further, they will always steer back towards the emitter. How quickly that is possible though, depends on *PathLength* and *MaxSteeringAngle*.

**MaxSteeringAngle:** Every time a particle has traveled a distance of *PathLength*, it will make a random turn. This value specifies how large that turn may be. A small value results in very slow and wide turns, whereas a large value results in quick and erratic behavior.

<video src="media/flies.webm" width="500" height="500" autoplay loop></video>

## Gravity Behavior

This behavior lets particles fall downwards.

**GravityFactor:** Scales gravity before applying it to the particles' velocity.

<video src="media/gravity.webm" width="500" height="500" autoplay loop></video>

## Pull Along Behavior

Typically once a particle has been spawned, its position is unaffected by changes to the particle effect position. That means when an effect moves around quickly, it may leave a trail of particles behind it, but that trail will be very choppy, unless you have an extremely high particle spawn count and frequency. Thus making something like a rocket exhaust look convincing for a fast moving object can be difficult.

The *pull along behavior* helps to solve this problem by keeping track of any position changes of the particle effect node and applying a fraction of those movements to all the particles' positions as well. This way, if the effect moves a meter, all particles may move 0.8 meters as well. One typically only applies a fraction, such that when the effect moves fast, the particles will be stretched long behind it and not move in perfect unison with the effect node, yielding a more convincing effect.

**Strength:** How much of the effect node's movement should be carried over to the particle positions.

The video below shows two effects beside each other. The left one does not use the pull along behavior, the right one does. As can be seen, the particles on the right stay closer to the moving emitter position.

<video src="media/pull-along-behavior.webm" width="500" height="500" autoplay loop></video>

## Raycast Behavior

This behavior uses raycasts to detect collisions along the trajectory of a particle. If a particle would collide with geometry, the behavior can either adjust the its velocity, or terminate the particle early, potentially raising an [event](particle-effects-overview.md#events-and-event-reactions), which could in turn lead to other effects or being spawned.

**Reaction:** Specifies how the particle should react to a collision.

* *Bounce:* The particle's velocity will be adjusted such that it bounces off the hit surface.
* *Die:* The particle will be killed early.
* *Stop:* The particle's current velocity will be set to zero, thus stopping it in its tracks. If other position affecting behaviors are active, for example the [gravity behavior](#gravity-behavior), it will start moving again, but without its previous momentum.

**BounceFactor:** How much of the current speed should be preserved after the bounce.

**CollisionLayer:** The physics collision layer to use. Affects with which geometry the particle will collide and which it will pass through.

**OnCollideEvent:** An optional name of an [event](particle-effects-overview.md#events-and-event-reactions) to raise. If set, other effects or prefabs can be spawned at the location of impact.

<video src="media/raycast.webm" width="500" height="500" autoplay loop></video>

## Size Curve Behavior

This behavior changes a particle's size over the course of its lifetime.

**SizeCurve:** A [curve](../../animation/common/curves.md) which is used to look up the size of the particle. The current fraction of the particle's lifespan is used for the lookup along the X axis. The absolute X and Y values in the curve don't matter, the curve is normalized to `[0; 1]` range.

**BaseSize:** The particles will always have at least this size, the rest is added on top.

**CurveScale:** Specifies what value the largest value in the curve maps to. That means at the peak of a curve, the particle's size will be `BaseSize + CurveScale`.

<video src="media/size-curve.webm" width="500" height="500" autoplay loop></video>

## Velocity Behavior

This behavior affects particle position and velocity. It can be used to gradually dampen the starting velocity through 'friction' and it may apply a constant upwards movement. If a scene contains [wind](../wind/wind.md), this behavior can also apply a fraction of the wind force to the particle's position.

**RiseSpeed:** If non-zero, the particles will move upwards with at least this constant speed. This is added to the particle position independent from its velocity, so if the current velocity points downward, the two may cancel each other out.

**Friction:** This value imitates air friction. If it is non-zero, the particle's velocity will be dampened over time. The value's range is `[0; infinity]`. To achieve an effect as in the animation below, the particles must have a very large starting velocity (here: 10). The *friction* here is set to 6. This way the particles will appear to be quite fast, but will also get slowed down almost to a standstill within a fraction of a second.

**WindInfluence:** If the scene has wind, this value specifies how much the wind should be able to push the particles around.

<video src="media/velocity.webm" width="500" height="500" autoplay loop></video>

## See Also


* [Particle Effects](particle-effects-overview.md)
* [Particle Initializers](particle-initializers.md)
* [Particle Renderers](particle-renderers.md)
