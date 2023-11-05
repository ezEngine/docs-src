# Event Nodes

Event nodes are used to broadcast [event messages](../../../runtime/world/world-messaging.md#event-messages) on the [game object](../../../runtime/world/game-objects.md) on which the animation graph is running. This allows other code to react at the right moment to things like an animation being finished.

Event nodes allow you to broadcast custom events under exactly defined conditions. Additionally, every time an [animation clip](../animation-clip-asset.md) is played, and actively contributes to the final pose, events that are defined on that clip will automatically be broadcast on the associated game object.

Note that the animation graph itself cannot *react* to events. For that purpose use [custom code](../../../custom-code/custom-code-overview.md).

## Send Event Node

When this node is triggered, it broadcasts an `ezMsgGenericEvent` with `Message` set to the value of `Event Name`.

### Node Properties

* `Event Name`: The string that is used as the `Message` property of the `ezMsgGenericEvent` that is broadcast.

### Input Pins

* `Activate`: When this pin gets triggered, the message is sent.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
