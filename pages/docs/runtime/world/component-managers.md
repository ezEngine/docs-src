# Component Managers

A component manager is a [world module](world-modules.md) whose purpose it is to create, store and update [components](components.md) of a single type. For every component type, there is exactly one component manager to handle that type.

## Simple Component Managers

There are two types of simple component managers:

1. Ones that don't update their components, at all.
1. Ones that call a simple `Update()` function once per frame on their components.

### No Update Component Manager

A component manager that doesn't update its components is declared like this:

<!-- BEGIN-DOCS-CODE-SNIPPET: component-manager-trivial -->
```cpp
using SendMsgComponentManager = ezComponentManager<class SendMsgComponent, ezBlockStorageType::Compact>;
```
<!-- END-DOCS-CODE-SNIPPET -->

We can simply instantiate the `ezComponentManager` template and not override anything. Therefore this component manager doesn't have any update function and so the component type that it manages is never updated. That doesn't mean that the component type in question can't do things periodically. In fact the `SendMsgComponent` does update its state regularly, but it triggers its own update through [messaging](world-messaging.md), which is more efficient for components that only need to wake up every once in a while.

### Simple Update Component Manager

Many component types need to be updated every frame, but it is sufficient if the component manager just calls a simple `Update()` function. Creating a component manager for this scenario looks like this:

<!-- BEGIN-DOCS-CODE-SNIPPET: component-manager-simple -->
```cpp
using DisplayMsgComponentManager = ezComponentManagerSimple<class DisplayMsgComponent, ezComponentUpdateType::WhenSimulating, ezBlockStorageType::FreeList>;
```
<!-- END-DOCS-CODE-SNIPPET -->

That is literally all. The template `ezComponentManagerSimple` will take care of the required update function setup. All you need to do then, is to add a (non-virtual) `Update()` function to the component type, which the component manager will call for all active components each frame.

The `ezComponentUpdateType` option determines whether the component manager will call the `Update()` function only while the world simulation is running (during a game) or also when it is not running, meaning when editing a scene. For things that should show up even while looking at a paused scene in the editor, you need to use `ezComponentUpdateType::Always`.

## Non-Simple Component Managers

The vast majority of component managers are very simple, but they can also be much more complex. This is mostly the case when the manager needs to synchronize state between components and other systems. Another reason to write a more complex component manager is efficiency. If the manager can track which components need updating and which ones can be ignored, it can skip the update for many components. Or it can update only a number of components each frame to amortize costs.

To write a more complex component manager you basically just register your own update functions and then do whatever needs to be done there. See the chapter about [world modules](world-modules.md) for how to do that.

> **Note:**
>
> When you write your own update function, don't forget to skip *inactive* components. Otherwise deactivating a component or object hierarchy has no effect on your component type. See `ezComponentManagerSimple::SimpleUpdate()` for an example.

## Component Storage

Both component managers above were configured with a `ezBlockStorageType` option. This determines what happens when a component gets deleted from the world.

If the component manager is set to `ezBlockStorageType::FreeList`, the unused memory block will be put into a free-list and reused when a new component is allocated. In the mean time, the component manager needs to skip these unused memory blocks, every time it iterates over all components. For components that have very short lifespans or are frequently created and destroyed, this can be more efficient. The main reason to use this, though, is for components that can't be relocated in memory. If a component would crash when it is copied to a different memory location, then using the free-list option prevents this.

If the component manager is set to `ezBlockStorageType::Compact`, then an unused memory block will be filled right away by relocating the last valid component to that freed up slot. This prevents memory fragmentation, which wastes performance when iterating over large arrays of components, of which many elements are unused. For components which are mostly long lived, this option gives better performance.

If in doubt, both options are fine. The `ezComponentManagerSimple` defaults to `ezBlockStorageType::FreeList` as this mode has fewer restrictions.

## See Also


* [World Modules](world-modules.md)
* [Components](components.md)
