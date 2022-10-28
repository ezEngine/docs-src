# Blackboards

A blackboard is a simple data structure that holds data as *key/value* pairs. Each entry in a blackboard has a name (the *key*) and a basic value type, such as `int`, `float` or `string`. Entries can be added and modified at any time.

Blackboards are a convenient data structure to share information between different systems. Apart from pure data storage, the blackboard implementation in EZ may also send messages whenever a value of an entry changes. This way a system can react immediately to a change, without having to poll the blackboard regularly.

## Using Blackboards

In C++ code you can use the `ezBlackboard` data structure directly. In scenes and [prefabs](../prefabs/prefabs-overview.md) you can attach a [blackboard component](blackboard-component.md) to an object. Systems that require a blackboard to function, such as [animation controllers](../animation/skeletal-animation/animation-controller/animation-controller-component.md), will traverse the object hierarchy upwards to find a blackboard component which they can use to read and write their state.

## See Also

* [Blackboard Component](blackboard-component.md)
