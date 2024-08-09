# Scene Transition Component

The *Scene Transition Component* is used to load another level. It can be triggered via script code or through a [Trigger Component](../physics/jolt/actors/jolt-trigger-component.md).

## Seamless Transitions

To make a transition from one level to another as seamless as possible, two things need to happen:

1. There should be no visual difference between the exit and entrance of two consecutive levels.
1. There should be as little delay when transitioning.

For the first criterium you mainly need to build the exit and entrance of two levels identically. The easiest way to achieve this, is to make a prefab for a piece of corridor, which you then reuse in both levels. Typically such connecting pieces have a zig-zag shape, such that the visible distance is severly limited into both directions.

Additionally, for such scenarios you should enable `RelativeSpawnPosition`, such that the player object in the target scene appears in the same spot as it was in the previous scene.

For the second criterium you need to make sure that the scene is already loaded when the transition happens. To achieve this, you should first place one trigger that starts the scene preload, and a bit further away you place the trigger that does the transition. Make sure that the distance is large enough such that the target scene is likely loaded before the player can reach the second trigger. If everything goes well, the transition will be nearly instant.

If the player is able to enter a preload area, but then leave it again, put another trigger in front of the preload trigger, which cancels the preloading, such that when the player turns around and does not proceed to the next level, the preloaded data gets freed.

## Component Properties

* `Mode`: What the component should do, if it gets triggered through a [Trigger Component](../physics/jolt/actors/jolt-trigger-component.md).
    * `None`: Do nothing.
    * `Load And Switch`: Immediately transition to the target scene. If necessary, show a loading screen until the target scene is finished loading.
    * `Preload`: Start loading the target scene in the background. The active level stays active.
    * `Cancel Preload`: Cancel any background preloads and free up the memory.   
* `TargetScene`: The scene that this component should load or preload.
* `PreloadCollection`: An optional [asset collection](../performance/asset-collections.md) that should be used for preloading data before switching to the target scene. This is necessary for proper progress calculation and helps to make scene transitions smoother.
* `SpawnPoint`: An optional name for the spawn point in the target scene. If the scene has multiple [player start points](player-start-point.md), the one with this name will be used to spawn the player.
* `RelativeSpawnPosition`: If enabled, the relative position to this object is calculated and used to spawn the player with the same offset in the target scene. This is useful when one scene is supposed to continue a level seamlessly. You can build the exit of one level identical to the entrance of the next level, such that the transition looks natural. By applying the relative position to the spawn position, a player that is walking on the left or right side of a corridor will then also spawn in the next level on the left or right side, instead of at a fixed center position.

## See Also

* [Game States](../runtime/application/game-state.md)
