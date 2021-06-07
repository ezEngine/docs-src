# Input Component

The *input component* is used to forward input from a selected [input set](input-overview.md) to all components in the same sub-tree of game objects via the `ezMsgInputActionTriggered` [message](../runtime/world/world-messaging.md).

For the desired input set to show up in the editor, it has to be set up through the [project settings](input-config.md).

## Deactivating Input Notifications

You may have many objects in a scene that the player can take control of. Each object would have its own input component to route input into its scripts. However, every object is only interested to receive input notification messages, while it is actually controlled by the player. At other times it would be wasteful to still receive input notifications, only to ignore them.

Therefore an object should [deactivate](../runtime/world/components.md#component-activation) its input component when the player is not controlling it.

## Input Notification Message

The message `ezMsgInputActionTriggered` contains information about a single *input action*. It passes along the current state (up, down, pressed, released) and how much the input slot got activated (for instance how far the mouse was moved).

The name of the input slot is only sent as a hashed value, for performance reasons. To compare against a known input action name, compute the hash for your string and compare those values. In C++ use `ezTempHashedString::ComputeHash()` in TypeScript use `ez.Utils.StringToHash()`.

In both cases, prefer to precompute the hash once.

## Component Properties

* `InputSet`: The name of the *input set* to use. All *input actions* that are part of this input set will be forwarded as messages.
* `Granularity`: Configures whether the component sends messages only for certain state changes, or also continuously while a button is held down.

## See Also


* [Input](input-overview.md)
