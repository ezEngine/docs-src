# Visual Script: State Machine Nodes

## StateMachineInstance and StateMachineState

State machine nodes allow visual scripts to interact with [state machines](../../game-logic/state-machine-asset.md), enabling complex state-based behavior. These nodes are primarily used when a visual script itself serves as a state within a state machine (see [script states](../../game-logic/state-machine-asset.md#script-state)).

Key concepts:

* **State Machine Instance** - The runtime instance of a state machine that the script is running within. This is passed into the script through the `OnEnter`, `OnExit`, and `Update` event handler nodes.
* **State Transitions** - Nodes to query available transitions and trigger state changes
* **State Information** - Query the current state, previous state, and state duration
* **Blackboard Integration** - Access state machine blackboards for data sharing

When a visual script is used as a state machine state, it receives special entry point events (`OnEnter`, `OnExit`, `Update`) that provide the state machine instance as a parameter. Use state machine nodes to control transitions, access shared data, and coordinate with other states in the machine.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [State Machine Asset](../../game-logic/state-machine-asset.md)
* [Event Handler Nodes](vscript-nodes-events.md)
* [Blackboard Nodes](vscript-nodes-blackboard.md)
