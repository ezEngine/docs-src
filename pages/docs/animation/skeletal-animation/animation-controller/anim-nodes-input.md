# Input Nodes

Input nodes expose the state of input devices to the animation graph. Input nodes are mainly provided for convenience during prototyping, as they may circumvent key mappings and general game state (e.g. whether the player is even allowed to move a character at all, at the moment).

For a proper game, it is better to use an [input component](../../../input/input-component.md) to forward input state to [custom code](../../../custom-code/custom-code-overview.md) and then decide there which animation shall get played. Then you can forward that state to the animation graph, through a [blackboard](../../../Miscellaneous/blackboards.md). The animation graph itself would retrieve what it should do through the [blackboard nodes](anim-nodes-blackboard.md).

## Controller Node

This node reads the raw state of the connected controller **1**. It outputs the button states as data pins.

This node completely ignores any kind of button mapping. It is purely meant for prototyping scenarios, where it can be very convenient.

### Output Pins

* This node has number output pins for the sticks and triggers and bool output pins for the buttons.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
