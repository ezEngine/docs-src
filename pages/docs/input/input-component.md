# Input Component

The *input component* is used to forward input from a selected [input set](input-overview.md) to all components in the same sub-tree of game objects via the `ezMsgInputActionTriggered` [message](../runtime/world/world-messaging.md).

For the desired input set to show up in the editor, it has to be set up through the [project settings](input-config.md).

## Deactivating Input Notifications

You may have many objects in a scene that the player can take control of. Each object would have its own input component to route input into its scripts. However, every object is only interested to receive input notification messages, while it is actually controlled by the player. At other times it would be wasteful to still receive input notifications, only to ignore them.

Therefore an object should [deactivate](../runtime/world/components.md#component-activation) its input component when the player is not controlling it.

## Input Notification Message

The message `ezMsgInputActionTriggered` contains information about a single *input action*. It passes along the current state (up, down, pressed, released) and how much the input slot got activated (for instance how far the mouse was moved).

## Component Properties

* `InputSet`: The name of the *input set* to use. All *input actions* that are part of this input set will be forwarded as messages.
* `Granularity`: Configures whether the component sends messages only for certain state changes, or also continuously while a button is held down.
* `ForwardToBlackboard`: If enabled, the input component will attempt to store input states in a nearby [blackboard](../Miscellaneous/blackboards.md). If it can find a blackboard on the same owner game object, or a parent game object, it will set a value with the name of the action to a float value between `0` and `1`, depending on whether the action is fully triggered (`1`), not triggered (`0`) or partially triggered (e.g. for a thumb stick). This is an quick way to forward input data to an easily accessible data structure.

## See Also

* [Input](input-overview.md)
