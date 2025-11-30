# Visual Script: Component and Property Nodes

## Component

Component nodes provide access to functionality shared by all [components](../../runtime/world/components.md). These are essential nodes for interacting with the component system and navigating the object hierarchy.

Common component operations:

* `GetOwner`: Returns the component's owner [game object](../../runtime/world/game-objects.md)
* `GetWorld`: Returns the [world](../../runtime/world/worlds.md) that the component belongs to

Additionally, each component type has its own specialized nodes available in the sub-menus, providing access to component-specific functionality. Use these together with [property nodes](vscript-nodes-property.md) to read and modify component state.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Components](../../runtime/world/components.md)
* [Game Object Nodes](vscript-nodes-game-object.md)
* [World Nodes](vscript-nodes-world.md)
* [Property Nodes](vscript-nodes-property.md)
