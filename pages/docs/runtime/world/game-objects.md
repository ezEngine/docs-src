# Game Objects

For an introduction what a game object is and how it fits into the overall picture, see [The World / Scenegraph System](world-overview.md).

This documentation focuses on the C++ `ezGameObject` class. The functionality exposed through other mechanisms, such as [Visual Scripts](../../custom-code/visual-script/visual-script-overview.md), may be more limited in scope, but ultimately maps to the C++ implementation.

## Creating Game Objects

You create new game objects by calling `ezWorld::CreateObject()`. This function takes a `ezGameObjectDesc`. This is used to initialize the game object, all options can be changed later on, however things like changing the 'dynamic' state can be expensive to switch.

## Deleting Game Objects

Use `ezWorld::DeleteObjectDelayed()` to remove an object from the world. This will also delete all child nodes and attached components. This function puts the object into a deletion queue and only deallocates it at the end of the frame, so code that still tries to access the object in the same frame will not be affected.

The chapter about [object lifetime](object-lifetime.md) explains this in more detail.

## Object Transforms

Game objects have a position, rotation and scaling. These values are separated into *local* and *global*. The local transform represents the offset to the *parent*. If a game object has no parent, the local and global transform are identical.

You can query or modify either, though in the editor the property grid only allows you to set the local transform.

The global transform is computed from the local transform and the global transform of the parent (recursively). For *dynamic* objects (see below) the global transform is recomputed regularly. *Static* objects will not be updated after their initial placement.

### Video: How to parent objects

[![video](https://img.youtube.com/vi/7wPy3g75weY/0.jpg)](https://www.youtube.com/watch?v=7wPy3g75weY)

## Static vs. Dynamic Objects

*Static* game objects are objects that are considered to never move. *Dynamic* objects, however, can move around the scene arbitrarily. Internally the engine separates these two types of objects into different memory regions. The object transform for dynamic objects is updated *every frame*. That means from a performance perspective it makes no difference whether a dynamic object was moved in a frame or not. The transforms for static objects, however, are only updated when it is needed (after creation). If you try to move a static object, you will see warnings in the [log](../../debugging/logging.md) in development builds, and the object will not move.

When you build a scene in the editor, you generally don't need to worry about this. Each [component type](components.md) is flagged to either be *dynamic* (meaning it may modify its owner's position) or static. From the attached components, the editor will automatically detect whether a game object must be created as static or dynamic.

However, in some cases you may know that an object will end up having dynamic components later. So to prevent a costly switch from static to dynamic, you can force a game object to be dynamic, by selecting this mode from the properties.

The renderer also caches rendering state for static objects. This does not mean that a static object cannot change rendering state dynamically, but when it does, the code must ensure to properly invalidate the render caches. If switching from static to dynamic fixes a rendering issue, some attached component doesn't handle this cache invalidation correctly.

### Performance Considerations

For performance reasons it is always best to keep all objects static that don't need to be moved. Due to the render data caching, this can save even more CPU time. However, the code paths to update dynamic objects are still quite heavily optimized. A current CPU can easily handle updating 100.000+ dynamic objects at interactive framerates.

## Active Flag

Game objects have an 'active flag'. By default all objects are marked active. If the active flag is removed, all components on that object get deactivated. That means they will not get updated further and in general the object is treated as if it is not part of the world anymore.

The active flag propagates down to child objects. Using `ezGameObject::GetActiveFlag()` you can check the state of the active flag on a given game object. However, even if the flag is set, the game object can still be deactivated, if any one of its parents has been deactivated. You can check this with `ezGameObject::IsActive()`.

The active flag is useful to hide an entire object hierarchy. For example the player object in the [Testing Chambers](../../../samples/testing-chambers.md) project has multiple weapons attached. Only one of them is active at a time, and therefore visible.

## Lifetime and Referencing Game Objects

When deleting a game object, it typically stays alive till the end of the frame, to make writing robust code easier. You should, however, never store pointers to game objects across frames, as objects can be relocated in memory. Instead, always use **handles** (`ezGameObjectHandle`) to store references to game objects.

The chapter about [object lifetime](object-lifetime.md) explains this in more detail.

Components can also [reference objects](../../scenes/object-references.md) from their properties. These references are also based on handles.

## Tags

Game objects can have [tags](../../projects/tags.md). These are used to control things like whether the object will cast shadows. However, they are mostly at your disposal to tag objects with game play relevant information.

## Iterating over Game Objects

You can iterate over *all* objects in a world using `ezWorld::GetObjects()`. This will return the objects in an arbitrary order, but is the more efficient way.

You can also traverse the object *hierarchy* with `ezWorld::Traverse()`. This allows you to list the objects either in a depth-first or a breadth-first order.

When you have a specific game object, you can also iterate over its children with `ezGameObject::GetChildren()`.

## Finding Objects

There are multiple ways to find specific objects, or objects relative to some parent node.

### Global Keys

You can assign a game object a *global key*. This is a string that should be unique across all objects within the world. That includes all game objects from all [prefab](../../prefabs/prefabs-overview.md) instances, so you must be very careful with this. If the same global key is used twice, one of them will be ignored.

You can query for a game object by global key using `ezWorld::TryGetObjectWithGlobalKey()`.

Global keys can be useful to find unique objects, like the one player object (in a single player game), or level specific items.

### Finding Child Objects

Within an object hierarchy, you can use the *name* of objects to search for certain child nodes. These functions are available:

* `ezGameObject::FindChildByName()`
* `ezGameObject::FindChildByPath()`
* `ezGameObject::SearchForChildByNameSequence()`
* `ezGameObject::SearchForChildrenByNameSequence()`

For details please consult the [API Docs](../../api-docs.md) on those functions.

## Coordinate System

The [coordinate system of the world](worlds.md#coordinate-system) is configurable. To make it easier to not hard code assumptions about which axis represents what direction, the game objects provide functions to query the local axis:

* `ezGameObject::GetGlobalDirForwards()`
* `ezGameObject::GetGlobalDirRight()`
* `ezGameObject::GetGlobalDirUp()`

These functions return the respective directions in global space considering the worlds coordinate system and the objects own global rotation.

## Messaging

You can send messages to all components attached to an object, or the entire hierarchy below an object. You can also send *event messages*, which will 'bubble up' the hierarchy until they find a component to handle it.

See the chapter about [messaging](world-messaging.md) for details.

## Team ID

All game objects store a 16 bit *team ID*. This value can be used to identify which team or faction an object belongs to. The team ID has no functionality by itself, you can use it or ignore it.

The one feature that the team ID has, is that it is automatically propagated for you when components create objects or instantiate [prefabs](../../prefabs/prefabs-overview.md). This way, when a player with team ID `3` shoots, the bullet prefab that gets instantiated by the [spawn component](../../gameplay/spawn-component.md) will automatically be assigned team ID `3` as well. Thus when that bullet hits another player, your code can easily attribute a kill to a team, or filter out friendly fire.

Although it would be possible to implement something similar entirely with custom components, only by having this in the basic game object, is it possible to trace this information even through built in components, meaning you don't need to reimplement basic functionality like the spawn component or the [projectile component](../../gameplay/projectile-component.md).

## See Also


* [The World / Scenegraph System](world-overview.md)
* [Components](components.md)
* [Object Lifetime](object-lifetime.md)
* [Messaging](world-messaging.md)
