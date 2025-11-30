# Visual Script: Spatial Nodes

## Spatial

The [spatial system](../../../runtime/world/spatial-system.md) allows you to find nearby objects. Unlike using the [physics engine](vscript-nodes-physics.md) for this, the spatial system is typically used to find tagged objects (see [Marker Component](../../../gameplay/marker-component.md)). This is often useful for game logic.

For example, an NPC may want to find the closest health-pack, so it would use the spatial system to search for objects that use a health-pack marker. Other use cases include:

* **Proximity queries** - Find objects within a certain radius
* **Nearest object search** - Locate the closest object with a specific tag
* **Category filtering** - Query objects by marker categories
* **AI perception** - Allow AI to discover objects of interest in their vicinity

Spatial queries are more efficient than physics queries when you only need to find tagged objects, as they use a specialized spatial index optimized for this purpose.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Marker Component](../../../gameplay/marker-component.md)
* [Spatial System](../../../runtime/world/spatial-system.md)
* [Physics Nodes](vscript-nodes-physics.md)
* [Math Nodes](vscript-nodes-math.md)
