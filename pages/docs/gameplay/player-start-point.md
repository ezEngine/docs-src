# Player Start Point

The *Player Start Point* component is used to indicate a position in a level from where the game should start playing.

The component references a [prefab](../prefabs/prefabs-overview.md) which represents the player object. This prefab must be built such that it handles [input](../input/input-overview.md) and implements the desired player movement and interactions.

When the game is run either using [Play-the-Game mode](../editor/run-scene.md#play-the-game-mode) or [stand-alone](../editor/run-scene.md#export-and-run), it will execute its [game state](../runtime/application/game-state.md). The default game state implementation will look for a player start component and instantiate the referenced prefab. This is most useful for games where a specific object represents the player. For games that do not have a player presence, such as RTS games, the custom game state should ignore this type of component and instead implement the player interaction logic itself.

When a scene contains a player start point component, you can use the [Play From Here](../editor/run-scene.md#play-from-here) feature.

## See Also


* [Running a Scene](../editor/run-scene.md)
* [ezPlayer](../tools/player.md)
