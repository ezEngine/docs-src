# Spawn Component

The *SpawnComponent* is frequently used to spawn instances of [prefabs](../prefabs/prefabs-overview.md) at runtime. The component references a prefab. It can then either spawn this prefab continuously in intervals, or at will by triggering the spawn command from (script) code.

## Properties

`Prefab:` The [prefab](../prefabs/prefabs-overview.md) that will be spawned by this component.

`AttachAsChild:` If true, the spawned object will be attached to the owner of the SpawnComponent. In most cases this should be disabled.

`SpawnAtStart:` If true, the SpawnComponent will spawn the prefab immediately when it gets activated.

`SpawnContinuously:` If true, the component will continue to spawn more and more prefab instances. This can only be stopped either through custom (script) code or by deleting the spawn component.

`MinDelay, DelayRange:` The minimum time that has to pass before the component will spawn another instance, plus some random delay. This not only applies to the *SpawnContinuously* case, but also to cases where the spawn may be triggered from code. Meaning, this can be used to limit how often an action is allowed. For example, a gun can use a SpawnComponent to launch projectiles, and the gun code can simply trigger the SpawnComponent every time the user clicks. However, due to the *MinDelay*, the gun will only fire every once in a while, without having to write that logic in the gun code.

`Deviation:` When a new prefab instance is created, it will be positioned at the location of the SpawnComponent. The *Deviation* allows you to add a random rotation away from the X axis. In EZ most components use the +X axis as their main axis of operation. For instance, projectiles fly along +X, spot lights point into +X direction, etc. Therefore the SpawnComponent tilts the new instances away from the +X axis and all prefabs should be authored to work with this accordingly.

## Details

See the [API Docs](../../getting-started/api-docs.md) for `ezSpawnComponent` for the component's interface.

## See Also


* [Prefabs](../prefabs/prefabs-overview.md)
