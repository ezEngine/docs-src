# Input System

All input devices, such as mouse, keyboard, controllers and other periphery are managed by the central `ezInputManager`. New devices are exposed to the system by implementing a custom `ezInputDevice`. For details, please see the [API Docs](../api-docs.md) for those classes.

## Video: How to do Input

[![video](https://img.youtube.com/vi/G16mBOH1I6A/0.jpg)](https://www.youtube.com/watch?v=G16mBOH1I6A)

## Abstract State

All input state is abstracted away. There are two layers of abstraction: **input slots** and **input actions**. *Slots* are the lower level hardware representation, *actions* are a higher level semantic representation of what the player can do. Actions are bound to one or multiple slots and if possible the game should allow the player to change those bindings.

### Input Slots

Input slots represent the state of actual device features, such as the buttons on a controller or the keys on a keyboard. Slots are already an abstraction, though. For instance for a mouse there are input slots for both the last relative movement, as well as the current absolute cursor position. Input devices are free to define arbitrary input slots, which may represent actual physical features or virtual functionality.

Each input slot is a single `float` value that is typically in the range `[0; 1]` or `[0; inf]`. If a device feature has both a positive and a negative value, such as the X and Y axis of a stick, these are typically exposed as two input slots, one for the positive part of the axis, one for the negative part, and each uses an absolute value. This generalized concept makes it easier to map input slots to actions in various ways. For example, each stick on a controller is represented as four input slots (+X, -X, +Y, -Y). The same would be true for a DPad. That allows to map either the stick or the DPad to, e.g. steering a vehicle. The only difference is that the stick can report values between zero and one, whereas the DPad would only report values that are exactly zero or one.

If you want to allow the player to map input slots themselves, you can query `ezInputSlotFlags` for each slot, which describe how a slot can be used, to only let them map keys that make sense for a given action.

In practice though, you rarely work directly with input slots. Typically the only situation where one works directly with input slots, is during the initial setup of the slot to action key binding.

### Input Actions

Input actions represent the features that the game exposes to the player. Actions are typically things like *walk forwards/backwards*, *jump*, *shoot* and so on. In actual game code you typically only work with input actions. Actions are bound to input slots, meaning one or multiple slots will trigger the action. This binding can be modified at any time. It is common to bind both keyboard/mouse slots to an action, as well as controller slots, such that a game can be played with either device.

### Input Sets

An *input set* represents a specific use case in a game. For example you might have a dedicated input set for being on foot and one for driving a vehicle. Each *input action* is associated with one *input set*. That means you can have an action for 'drive forwards' in one input set and an action for 'walk forwards' in another input set. Each input action may be triggered by any input slot, meaning that the same input slot, e.g. the `W` key, can trigger both 'walk forwards' and 'drive forwards' at the same time. The game would either query the one action or the other, depending on whether the player is currently on foot or in a vehicle.

When you have multiple input sets, you can reuse the same names for actions (e.g. 'shoot') and still allow the player to bind the keys differently.

In practice you may only need a single input set, and you shouldn't use more than three.

### Key Value

Each input slot and therefore also each action has an *amount* how much it is being triggered. This is mostly of interest for analog signals such as from a stick, since buttons only report the values `0` and `1` with nothing in between. You can query these values, if an actions grants fine grained control over something.

For many actions, though, you only require the *key state*.

### Key State

Both slots and actions have a current `ezKeyState`, which describes whether the action is currently active or not, and whether the stated changed just now (between the last frame and this frame) or has been persisting. If you want to react only once to a button press, you would check for the state `ezKeyState::Pressed`, whereas if you want to do something as long as a button is held, you would react to `ezKeyState::Down`.

The key state is derived from the *key value*. Once a button gets pressed, the key value jumps from `0` to `1`. As a consequence the *key state* transitions from `ezKeyState::Up` to `ezKeyState::Pressed` for this frame, and continues to `ezKeyState::Down` in the next frame. Once a button is depressed, the key value goes back to `0` and the key state transitions first to `ezKeyState::Released` for one frame, and finally back to `ezKeyState::Up` in the next frame.

## Accessing Input State

Through `ezInputManager` all input state (both for slots and actions) is accessible by all code at all times. However, depending on the type of game you build, you may prefer to use the [input component](input-component.md) to get a specific *input set* routed to a specific component through `ezMsgInputActionTriggered`.

### Direct Input Access

In some games the player doesn't have a physical presence, but is rather an outside observer. Examples would be an RTS or Tetris. Here you don't have a [character controller](../physics/jolt/special/jolt-character-controller.md) inside the world. Implementing the control scheme for such game logic through game objects and components can be tedious. Instead, it is much easier to write a custom [game state](../runtime/application/game-state.md) and handle all the interaction, the camera movement and the general game logic there.

In such a scenario, the game state would call `ezInputManager::GetInputActionState()` directly to retrieve the state of an action. This is also what the `ezFallbackGameState` uses to provide the most basic functionality (such as quitting when `ESC` is pressed).

Therefore, if you write a custom game state to show a main menu, you would use this direct access to hook up the input system to the UI navigation.

### Component Based Input Access

In games where the player does have a physical presence, such as creatures or vehicles, and they may swap between those, it might be difficult to retrieve the input in a [game state](../runtime/application/game-state.md) and then use it to control any one of the many vehicles.

Instead, it is easier to have each vehicle fully handle its own state and therefore also retrieve the input locally. In this case each vehicle would know whether is currently 'possessed' by the player, and as long as it's not, it would just ignore all input (or generally disable receiving input notifications).

If you write a [custom component](../custom-code/cpp/custom-cpp-component.md) for your vehicle, that component could access the input state directly, during its update.

Another option, though, is to use an [input component](input-component.md). All that this component does, is to check for state changes of input actions from a selected *input set* and send those state changes as [messages](../runtime/world/world-messaging.md) to its sub-tree of game objects and components. Any component that handles this message type, can react to the input.

This message based approach is how [script components](../custom-code/visual-script/script-component.md) are able to handle input. Since the input messages are delivered to all child objects, you can have multiple scripts or other components which each react to different input. For example one script can forward movement related input to a [character controller](../physics/jolt/special/jolt-character-controller.md) and another script can handle input for weapons.

## Setting Up Input Sets

Input sets can be configured either from code, or through the editor [project settings](../projects/project-settings.md). For details, see [this page](input-config.md).

## See Also

* [Input Set Configuration](input-config.md)
* [Input Component](input-component.md)
