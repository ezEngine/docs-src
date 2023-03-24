# Forward Events To Game State Component

This component forwards any message that it receives to the active [game state](../../runtime/application/game-state.md).

Game states can have [message handlers](../../runtime/world/world-messaging.md) just like any other reflected type.
However, since they are not part of the [world](../../runtime/world/worlds.md), messages are not delivered to them. By attaching this component to a game object, all event messages that arrive here are forwarded to the active game state.

This way, a game state can receive information, such as when a trigger gets activated. Multiple of these components can exist in a scene, gathering and forwarding messages from many different game objects, so that the game state can react to all of them.

## Properties

None.

## See Also

* [Game States](../../runtime/application/game-state.md)
* [Messaging](../../runtime/world/world-messaging.md)
