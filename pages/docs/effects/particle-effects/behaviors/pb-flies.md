# Flies Behavior

This behavior moves particles around the emitter center in erratic patterns, similar to a swarm of flies circling something.

**FlySpeed:** The speed with which the particles move.

**PathLength:** The distance that the particles move into some direction before making another turn. The shorter this is, the more often the particles can change direction and thus the smoother the motion becomes. They will also clump up more and stay within the *MaxEmitterDistance*, if the particles can correct their course more often. With a long *PathLength* they may spread out more.

**MaxEmitterDistance:** The maximum distance that the particles will fly away from the effect's center before turning back. If they travel further, they will always steer back towards the emitter. How quickly that is possible though, depends on *PathLength* and *MaxSteeringAngle*.

**MaxSteeringAngle:** Every time a particle has traveled a distance of *PathLength*, it will make a random turn. This value specifies how large that turn may be. A small value results in very slow and wide turns, whereas a large value results in quick and erratic behavior.

<video src="../media/flies.webm" width="500" height="500" autoplay loop></video>

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
