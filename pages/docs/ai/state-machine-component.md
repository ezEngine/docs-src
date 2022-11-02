# State Machine Component

The *state machine component* creates an instance of a [state machine asset](state-machine-asset.md) and updates that every frame. The *InitialState* property determines the starting state of the state machine.

This component also enables a state machine to send messages to [components](../runtime/world/components.md) attached to the same [game object](../runtime/world/game-objects.md). For example the `ezMsgStateMachineStateChanged` [event message](../runtime/world/world-messaging.md#event-messages) will be broadcast on this object, if the state machine contains a corresponding state.

## Component Properties

* `Resource`: The [state machine](state-machine-asset.md) to use.
* `InitialState`: In which state the state machine is supposed to start. If left empty, the [default initial state](state-machine-asset.md#default-initial-state) is used.

## See Also

* [State Machine Asset](state-machine-asset.md)
* [Custom Code](../custom-code/custom-code-overview.md)
