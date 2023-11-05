# Global Blackboard Component

A *global blackboard component* is used to ensure that a [global blackboard](blackboards.md#global-blackboards) exists and contains all the expected entries.

A global blackboard is often added by a [game state](../runtime/application/game-state.md), but when only [simulating a scene](../editor/run-scene.md), no game state is active. Thus, code that relies on a global blackboard will not work as desired.

By adding a global blackboard component to a scene or prefab, you can ensure that the blackboard is always set up.

## Component Properties

* `Template`: The [blackboard template](blackboard-template-asset.md) to use for configuring the global blackboard. For global blackboards this is the only way to configure the entries.

* `ShowDebugInfo`: If enabled, the component will [draw a debug text overlay](../debugging/debug-rendering.md) with the current entries and their values at the position of the game object.

* `BlackboardName`: The *name* for the blackboard. For global blackboards this is important to set.

* `InitMode`: What to do when the global blackboard component gets activated.
    * `Ensure Entries Exist`: Only makes sure that all entries mentioned in the template exist in the global blackboard. The values are not changed for entries that already exist.
    * `Reset Entry Values`: Overwrites all entry values to the initial value from the template. If additional entries exist, they are not modified.
    * `Clear Entire Blackboard`: Clears the entire blackboard and then sets up the ones mentioned in the template. This means that additional (temporary) entries that have been stored in the global blackboard get removed.

## See Also

* [Blackboards](blackboards.md)
* [Blackboard Template Asset](blackboard-template-asset.md)
* [Local Blackboard Component](local-blackboard-component.md)
* [Animation Graph (TODO)](../animation/skeletal-animation/animation-controller/animation-graph-overview.md)
