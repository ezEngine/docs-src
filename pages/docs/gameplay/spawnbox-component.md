# Spawnbox Component

This component spawns [prefabs](../prefabs/prefabs-overview.md) inside a box.

The prefabs are spawned over a fixed duration. The number of prefabs to spawn over the time duration is randomly chosen between a minimum and maximum value.
Each prefab may get rotated around the Z axis and tilted away from the Z axis.
If desired, the component can start spawning automatically, or it can be (re-)started from code.
If *spawn continuously* is enabled, the component restarts itself after the spawn duration is over,
thus for every spawn duration the number of prefabs to spawn gets reevaluated.

## Component Properties

* `HalfExtents`: The dimensions of the box in which the prefabs are spawned.

* `Prefab:` The [prefab](../prefabs/prefabs-overview.md) that will be spawned by this component.

* `SpawnAtStart:` If true, the component will spawn the prefab immediately when it gets activated.

* `SpawnContinuously:` If true, the component will restart itself after a round. How many prefabs to spawn is reevaluated for each round.

* `MinSpawnCount`, `SpawnCountRange`: How many prefabs to spawn during one round.

* `Duration`: The lenght of one spawn round. The randomly chosen amount of prefabs to spawn is distributed over this time.

* `MaxRotationZ`: How much the spawned objects may be rotated away from the forward axis, around the Z (up) axis.

* `MaxTiltZ`: How much to tilt objects away from the Z axis.

## See Also

* [Prefabs](../prefabs/prefabs-overview.md)
* [Spawn Component](spawn-component.md)
