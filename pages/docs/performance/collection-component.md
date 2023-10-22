# Collection Component

A *collection component* references a [collection asset](asset-collections.md). When it is part of a scene and active, it makes sure to preload all resources that are referenced by the collection. Since the collection holds a reference to each resource, this also prevents those resources from being unloaded prematurely, which can prevent artifacts and performance hiccups.

Placing a collection component into a scene or even into a prefab can be useful when you know that some assets will be needed, but they are currently not referenced in such a way that the engine keeps them loaded. By referencing a collection that contains all the needed assets, you can be certain that those assets are loaded as soon as possible and will stay loaded at least as long as the collection component exists.

If a deactivated collection component is part of a scene, it will not trigger a resource preload until it gets activated. You can use this to control exactly when you need the preload to happen. For instance, when the player enters a certain area, a collection component can be activated to preload data that is needed for a cutscene.

## Component Properties

* `Collection`: The referenced [collection asset](asset-collections.md).
* `RegisterNames`: If enabled, the component will register the resources in the collection asset that have a dedicated *name* under that name, so that these resources can be loaded that way. See [Referencing Assets by Name](asset-collections.md#referencing-assets-by-name).

## See Also

* [Asset Collections](asset-collections.md)
* [Profiling](profiling.md)
