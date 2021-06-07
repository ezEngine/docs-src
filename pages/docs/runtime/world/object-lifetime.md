# Object Lifetime

The lifetime of [game objects](game-objects.md) and [components](components.md) is tightly controlled by the [world](worlds.md) that they belong to. Neither are objects reference counted, nor garbage collected. You have full control over the destruction of objects, but by default 'deleted' objects are not destroyed before the end of the frame, to make writing robust code easy.

The lifetime of objects is directly linked to the object hierarchy. If a game object gets deleted, that also deletes all child nodes and all attached components.

## Referencing Objects

In C++ you can of course always hold pointers to anything. Within a single frame, it is fine to reference game objects and components by pointers. However, once the next frame starts, you have to assume that those pointers are invalid. Not only can objects be deleted, but even live objects can be moved around in memory. This 'compacting' is an optimization and can happen to any object between frames.

Therefore, instead of keeping pointers to objects, you should always use *handles*. Specifically `ezGameObjectHandle` for `ezGameObject` references, and `ezComponentHandle` for `ezComponent` (and derived) types.

Handles act like [weak pointers](https://en.wikipedia.org/wiki/Weak_reference). Once you have a handle to an object, you can keep it around forever. When you need to access the actual object, you call `ezWorld::TryGetObject()` or `ezWorld::TryGetComponent()`. If the object is still alive at that time, you get back a pointer. That pointer is guaranteed to stay valid until the end of the frame, so you don't need to call the `TryGet...` function again.

As a rule of thumb, you should *never* have `ezGameObject*` or `ezComponent*` types as class members. Pointers to these types should be limited to local function variables.

## Deleting Game Objects

To delete a game object, call `ezWorld::DeleteObjectDelayed()`. This will put the object into a deletion queue, and will remove the object at the end of the frame. This guarantees that all code that tries to access the object within this frame will work correctly.

You can also call `ezWorld::DeleteObjectNow()`. This will indeed delete the object right at that instant. The only situation where it is ok to call this, is in tools where you modify a world in a single threaded way and you know that no other code can ever access objects. Here, having an object not destroyed immediately may be undesirable.

## Deleting Components

To delete a component, get its [component manager](component-managers.md) and call `DeleteComponent()` on it. The component won't be deallocated right away, that is deferred till the end of the frame. However, it will be *deactivated* and *deinitialized* immediately. Therefore, if other code tries to access such a component, it will get valid memory, but it may see a deinitialized component. Such a situation can be detected by calling `ezComponent::IsActiveAndInitialized()` on the target. If you delete individual components during a frame (and not entire objects), code that accesses those components should be prepared to deal with deinitialized components.

## See Also


* [Game Objects](game-objects.md)
* [Components](components.md)
