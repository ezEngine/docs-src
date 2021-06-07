# Particle Emitters

This page lists and describes all *particle emitters*.

## Burst Emitter

This emitter type spawns particles either in one instantaneous burst or over a limited amount of time. It is mainly used for one-off effects like explosions, impacts, etc, which have a short lifespan. Once the burst emitter is finished, the particle effect will only continue to live until all spawned particles have reached the end of their life. For such effects the [particle effect components](particle-effect-component.md) are typically set to auto-delete themselves after the effect is finished.

**Duration:** The timespan over which the emitter will distribute the spawning of the particles. If this is set to zero, all particles spawn at the same instant.

**StartDelay:** An optional delay from when the particle effect is created, until the emitter starts spawning particles. Useful in effects with multiple particle systems, to tweak when one type of particles becomes visible, relative to other types of particles.

**MinSpawnCount, SpawnCountRange:** A random number of particles between `MinSpawnCount` and `MinSpawnCount + SpawnCountRange` is emitted over the emitter's *duration*.

**SpawnCountScaleParam:** An optional name of an [effect parameter](particle-effects-overview.md#effect-parameters) that can be used to scale the number of emitted particles up or down. *Note:* At the moment this mostly allows to reduce the number of emitted particles. Increasing the amount of particles may have no visible effect.

<video src="media/burst-emitter.webm" width="500" height="500" autoplay loop></video>

## Continuous Emitter

This emitter type continuously spawns new particles. Effects which have at least one such emitter type will never stop, unless custom code specifically switches the effect off, or the owning [particle effect component](particle-effect-component.md) is deleted. In both cases all spawned particles will continue to be simulated and rendered, until they reach the end of their life. This emitter type is commonly used for ambient effects such as smoke and fire. By exposing [effect parameters](particle-effects-overview.md#effect-parameters), continuous particle effects can be adjusted dynamically to visualize game mechanics, such as how hot something burns or how active some machine is.

**StartDelay:** See the [burst emitter](#burst-emitter).

**SpawnCountPerSec, SpawnCountPerSecRange:**  A random number of particles between `SpawnCountPerSec` and `SpawnCountPerSec + SpawnCountPerSecRange` is emitted every second.

**SpawnCountScaleParam:** See the [burst emitter](#burst-emitter).

**CountCurve, CurveDuration:** If no *CountCurve* is specified, particles are spawned in regular intervals. Only a large value for *SpawnCountPerSecRange* may introduce irregularities. Using a count curve, the distribution of how many particles are spawned at what time can be controlled. If a curve is given, *CurveDuration* specifies its timespan. For instance, a curve duration of two seconds means, that the count curve is sampled from left to right over a duration of two seconds, before it repeats again. The value of the curve at a given time determines how many particles will get spawned. The curve is only used as a scale factor between zero and one, though (its absolute values don't matter, it is normalized internally). Every time the emitter attempts to spawn particles, *SpawnCountPerSec* and *SpawnCountPerSecRange* determine the *maximum* amount of particles to spawn. Then the curve is sampled and the current value is used to scale the number of particles down. Thus count curves can be used to introduce more elaborate spawn patterns.

<video src="media/continuous-emitter.webm" width="500" height="500" autoplay loop></video>

## Distance Emitter

This emitter type only spawns new particles when the particle effect is moved for a distance of at least *DistanceThreshold* units. This can be used when an effect should have a relatively uniform particle density when in motion, without constantly spawning large amounts of particles. When the effect stands still, this emitter will not spawn any particles, so you may want to combine this with another [continuous emitter](#continuous-emitter).

**DistanceThreshold:** The distance that the effect has to be moved for the emitter to spawn another set of particles.

**MinSpawnCount, SpawnCountRange:** See the [burst emitter](#burst-emitter).

**SpawnCountScaleParam:** See the [burst emitter](#burst-emitter).

<video src="media/distance-emitter.webm" width="500" height="500" autoplay loop></video>

## OnEvent Emitter

This emitter type spawns new particles whenever a specific [event](particle-effects-overview.md#events-and-event-reactions) happens. It does *not* create the new particles at the position of the event. If that is desired, use an [event reaction](particle-effects-overview.md#event-reactions) instead.

**EventName:** The name of the [event](particle-effects-overview.md#events-and-event-reactions) which shall trigger spawning particles.

**MinSpawnCount, SpawnCountRange:** See the [burst emitter](#burst-emitter).

**SpawnCountScaleParam:** See the [burst emitter](#burst-emitter).

In the animation below, the blue particles use a [raycast behavior](particle-behaviors.md#raycast-behavior) to get removed when a collision is detected. The behavior also sends an *event*. This is picked up by a second particle system, which then spawns a number of red particles.

<video src="media/onevent-emitter.webm" width="500" height="500" autoplay loop></video>

## See Also


* [Particle Effects](particle-effects-overview.md)
