# Marker Component

The marker component can be used to markup objects and locations with gameplay relevant semantical information.

To implement game mechanics, especially some form of AI, your code must be able to reason about objects in the game. An AI for an NPC must be able to scan its nearby environment to detect objects that it can interact with, other NPCs, the player and locations that may be of interest.

The [spatial system](../runtime/world/spatial-system.md) is there to provide efficient means to do such queries. Using spatial queries, you can find all objects within an area that belong to some group. For this to work, you obviously need to insert objects into the spatial system. The marker component is a simple and convenient way to do so.

All that the marker component does, is to insert a sphere of a given size and [category](../runtime/world/spatial-system.md#spatial-data-categories) into the spatial system, so that the object that the component is attached to, can be found with spatial queries.

> **Note:**
>
> Keep in mind that the number of categories available for use is limited to about 25. You should therefore prefer generic categories where possible.

## Properties

`Marker`: Which [spatial data category](../runtime/world/spatial-system.md#spatial-data-categories) to use for this marker.

`Radius`: The size of the marker.

## Examples

The marker component can be used for many purposes. Here are a couple of examples:

* Tag NPCs and players.
* Tag objects that can be picked up. The position and rotation of the marker node can be used to orient the object when it is picked up.
* Set up points for visibility checks and for targeting when determining whether an NPC sees another NPC. Each character may have a 'target' node at its head, its torso, each elbow and knee. The AI can then do raycasts against all these points to determine whether a character is visible, and if so, shoot at one of the visible markers.
* Identify usable objects, such as buttons. The marker should be used to mark up that something is usable at that location, other mechanisms should be used to narrow down what the function is and how an AI could interact with it.
* Mark useful locations, for example good hiding spots, or sniper positions.
* Warn of dangerous locations. A grenade may have a large 'danger' marker attached, which informs NPCs to run away. The same can be used in front and behind vehicles, where they are enabled when a car starts driving, such that NPCs will get out of its way.

For an example how marker components and spatial queries can be used to find nearby objects, have a look at the [Sample Game Plugin](../../samples/sample-game-plugin.md).

## See Also


* [Spatial System](../runtime/world/spatial-system.md)
* [Sample Game Plugin](../../samples/sample-game-plugin.md)
* [Tags](../projects/tags.md)