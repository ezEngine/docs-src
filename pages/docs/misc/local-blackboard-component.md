# Local Blackboard Component

The *local blackboard component* contains a [blackboard](blackboards.md). The component itself doesn't have any notable functionality. Instead it is used as the central storage, through which other systems can share their data and communicate.

If a system requires a blackboard, it will typically search for a blackboard component by traversing its own object structure upwards (in C++ you can use `ezBlackboardComponent::FindBlackboard()` to do so).

For example the [animation graph](../animation/skeletal-animation/animation-graphs/animation-graph-overview.md) is controlled by modifying blackboard entries, which the controller reads. You can modify the entries through [custom code](../custom-code/custom-code-overview.md). For this, the blackboard component has to be attached either to the same object, or a parent object.

## Component Properties

* `Template`: The [blackboard template](blackboard-template-asset.md) to use for configuring the blackboard. This is often much more convenient, than to add a all the entries one by one on each component. It also makes changing a configuration later easier. 

* `BlackboardName`: The *name* for the blackboard. This could be used to search for a specific blackboard, if multiple are available in the same hierarchy.

* `ShowDebugInfo`: If enabled, the component will [draw a debug text overlay](../debugging/debug-rendering.md) with the current entries and their values at the position of the game object.

* `SendEntryChangedMessage`: If enabled, all changes to blackboard entries will be broadcast as an [event message](../runtime/world/world-messaging.md#event-messages) of type `ezMsgBlackboardEntryChanged`. This allows other systems to react to every change, but also has a small performance cost.

* `Entries`: Entries that will be added at start with their initial values. Some systems will add their own entries, others expect an entry to already exist. For example the [input component](../input/input-component.md) may write input state into a blackboard, but it will only do so for entries that already exist. Therefore, you need to add all entries that you want to receive from the input system here.

## See Also

* [Blackboards](blackboards.md)
* [Blackboard Template Asset](blackboard-template-asset.md)
* [Global Blackboard Component](global-blackboard-component.md)
* [Animation Graph](../animation/skeletal-animation/animation-graphs/animation-graph-overview.md)
