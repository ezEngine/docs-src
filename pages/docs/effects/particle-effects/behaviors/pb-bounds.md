# Bounds Behavior

This behavior can be used for atmospheric effects that should be centered around the player, such as rain, snow or mist. The bounds behavior specifies an area in which particles are allowed. When the player moves, and thus the particle effect is moved to a new location, particles would usually stay behind although not being needed anymore. The bounds behavior can make sure to delete those particles. For some effects it is also vital to fill up the new space quickly. This can be achieved with a very high rate of spawning new particles, though this is often not feasible for atmospheric effects. Instead, the bounds behavior can also just teleport the particles that were left behind, to the new area.

**PositionOffset, Extents:** These values define the size and position of the box, relative to the origin of the particle system. With a position offset of `(0, 0, 0)`, the box will be centered around the system's origin.

**OutOfBoundsMode:** Defines what happens for particles that leave the bounding area.

* **Die:** Particles outside the area will be killed right away.
* **Teleport:** Particles leaving one side of the bounding box will be teleported to the other end of the box. This allows the effect to keep a constant density of particles and is therefore useful for effects that should happen around a player, without being simulated completely in the local space of the player, which would prevent things like using the [raycast behavior](pb-raycast.md). Instead, particles can simulate in global space, and only be teleported on demand. Be aware that this teleportation can still break the effect in various ways, because only the *position* and *last position* of each particle is relocated. Behaviors and [particle renderers](../particle-renderers.md) that use additional positional data may not work well with this. For example, the [trail renderer's](../particle-renderers.md#trail-renderer) position history is not relocated and therefore trails will suddenly stretch through the entire bounding area after a relocation.
Similarly, an effect that uses the [raycast behavior](pb-raycast.md) to prevent tunneling through geometry, may be able to tunnel through walls, if it is being relocated from an unobstructed area to a position where it should not have been able to get to without the teleportation.

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
