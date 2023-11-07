# Blackboards

A blackboard is a simple data structure that holds data as *key/value* pairs. Each entry in a blackboard has a name (the *key*) and a basic value type, such as `int`, `float` or `string`. Entries can be added and modified at any time.

Blackboards are a convenient data structure to share information between different systems. Apart from pure data storage, the blackboard implementation in EZ may also send messages whenever a value of an entry changes. This way a system can react immediately to a change, without having to poll the blackboard regularly.

## Using Blackboards

In C++ code you can use the `ezBlackboard` data structure directly. In scenes and [prefabs](../prefabs/prefabs-overview.md) you can attach a [blackboard component](local-blackboard-component.md) to an object. Systems that require a blackboard to function, such as [animation controllers](../animation/skeletal-animation/animation-graphs/animation-controller-component.md), will traverse the object hierarchy upwards to find a blackboard component which they can use to read and write their state.

## Global Blackboards

Through the [local blackboard component](local-blackboard-component.md) you add a blackbard to a specific object. These typically store object specific data that's used within that object hierarchy.

However, you can also create *global blackboards*. These will exist as long as anyone references them. If, for instance, a [game state](../runtime/application/game-state.md) holds on to a global blackboard, it will be available throughout the application lifetime, even across worlds.

Global blackboards can be created from C++ using `ezBlackboard::GetOrCreateGlobal()` or with a [global blackboard component](global-blackboard-component.md). All global blackboards are identified by name, meaning that you can have many different ones, for different purposes, but if you use the same name in different components, they all end up using the same blackboard.

Similarly, if `ezBlackboardComponent::FindBlackboard()` is used, and a non-empty name is provided, a global blackboard may get created, if no other matching blackboard is available.

## See Also

* [Blackboard Template Asset](blackboard-template-asset.md)
* [Local Blackboard Component](local-blackboard-component.md)
* [Global Blackboard Component](global-blackboard-component.md)
