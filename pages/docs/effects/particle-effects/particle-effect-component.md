# Particle Effect Component

The *particle effect component* is used to instantiate and control particle effects in a scene. Each component handles one effect. When the owner game object is moved, the particle effect will move accordingly. Particles are emitted along the up axis (positive Z) of the game object.

**Effect:** The particle effect to spawn.

**SpawnAtStart:** If true, the effect will be spawned once the component becomes active. Otherwise, nothing will happen, and the component must be triggered manually via custom code.

**OnFinishedAction:** Specifies what happens when a non-continuous effect finishes:

* `None` - The effect stays off, and the particle effect component and its owner object stay as they are.
* `Delete Component` - The particle effect component gets automatically deleted to clean up unused components.
* `Delete Object` - The game object that the component is attached to is deleted including all attached components and child objects. This can be very useful to clean up entire effect objects, once the effect is finished. **Note:** This mode can be combined with other components that also have an *OnFinishedAction*. If multiple such components are set to delete themselves or the owning object, the *last one* that finishes will delete the object hierarchy. All components that finish earlier will only delete themselves (as if `Delete Component` was selected on them). This way you can attach for example a particle effect, a decal and a sound source to the same game object, select an *OnFinishedAction* on all of them, and get the correct behavior, no matter which one finishes first.
* `Restart` - The effect will be restarted after an optional *restart delay*.

**MinRestartDelay, RestartDelayRange:** If *OnFinishedAction* is set to `Restart`, a random time between `MinRestartDelay` and `MinRestartDelay + RestartDelayRange` has to pass before the effect will be restarted.

**RandomSeed:** If set to zero, the effect will use random values and look slightly different every time. If set to any other value, the effect will look identical every time it is restarted.

**SpawnDirection:** The direction along which the effect should be spawned (in local space). The default is 'positive Z' which means 'up', but to align this with other things, such as [decals](../decals/decals.md) or [lights](../../graphics/lighting/lighting-overview.md), it can be useful to use a different axis. Note that interactions with [surfaces](../../materials/surfaces.md) (e.g. an impact effect that is spawned when a bullet hits a wall) are always spawned such that the spawned prefab's positive X axis aligns with the surface interaction axis (e.g. it's normal). For such cases it therefore makes sense to spawn a particle effect along 'positive X'.

**IgnoreOwnerRotation:** By default the *SpawnDirection* is local to the owning game object, meaning when the owning object is tipped over, the effect will also spawn sideways. For some effects it can be desireable to ignore the rotation of the owner, and always spawn in *global space*, though. For instance, when an effect has a strong directionality, such as debris flying away in a cone, it may look best when it is always spawned upwards.

**SharedInstanceName:** If non-empty, this instance will use a [shared effect](particle-effects-overview.md#shared-effects).

**Parameters:** If the chosen effect exposed [effect parameters](particle-effects-overview.md#effect-parameters), they will be listed here and can be modified.

## See Also


* [Particle Effects](particle-effects-overview.md)
