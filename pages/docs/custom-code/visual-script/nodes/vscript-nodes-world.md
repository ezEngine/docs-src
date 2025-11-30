# Visual Script: World Nodes

## World

World nodes provide access to the [world](../../runtime/world/worlds.md) instance, which is the top-level container for all game objects, components, and systems in a scene. These nodes allow you to interact with world-level functionality from within visual scripts.

Use world nodes to:

* **Access the world instance** - Get a reference to the current world object
* **Query world state** - Check world properties and settings
* **World management** - Interact with world-level systems and services

The world is fundamental to the engine's object hierarchy. [Components](../../runtime/world/components.md) belong to [game objects](../../runtime/world/game-objects.md), which belong to the world. Most visual scripts get world access through component methods like `GetWorld()`, allowing scripts to access world-level functionality regardless of which object they're attached to.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Worlds](../../runtime/world/worlds.md)
* [Game Object Nodes](vscript-nodes-game-object.md)
* [Component Nodes](vscript-nodes-component.md)
