# Custom Components with TypeScript

To create a new component type, create a new [TypeScript asset](ts-asset.md). In that asset document, click the toolbar button to edit the script with Visual Studio Code. This will not only open the text editor, but also ensure that the `.ts` file exists and contains a basic template for your new component.

## Base Class

Your component class must extend one of these base classes:

1. `ez.TypescriptComponent`
1. `ez.TickedTypescriptComponent`

If it extends `ez.TypescriptComponent`, it can react to messages, startup/shutdown and activation/deactivation callbacks. However, it will not be updated regularly. Though this can be achieved through [messages](ts-messaging.md).

If it extends `ez.TickedTypescriptComponent`, the member function `Tick()` is executed regularly. The rate at which it shall be called can be modified using `SetTickInterval()`.

Often game components need to do regular checks and update their own state. Use the *ticked* base class when this is necessary. Choose a tick interval that is as long as possible to reduce their performance cost. You can also dynamically change the tick rate, to e.g. do more updates when the player is close, than when they are far away.

Whenever possible, though, prefer to use the non-ticked base class and have no regular update, at all. Such components rely on other machnisms, such as [triggers](../../physics/jolt/actors/jolt-trigger-component.md) to detect when they need to react, and they can use delayed messages (sent by others or by themselves) to trigger follow up work.

### Tick Function

When extending `ez.TickedTypescriptComponent`, the component code must contain a function with this signature:

```typescript
Tick(): void
{
}
```

It will be executed during the game update whenever enough time has passed. Use `SetTickInterval()` to adjust the frequency.

## Initialization

The template code contains examples for these functions:

1. `Initialize()`
1. `Deinitialize()`
1. `OnActivated()`
1. `OnDeactivated()`
1. `OnSimulationStarted()`

These functions are called in the same way as for C++ components. See [Component Activation](../../runtime/world/components.md#component-activation) for details.

## Message Handlers

TypeScript components can both send and receive messages. The article [Messaging in TypeScript Code](ts-messaging.md) explains this in more detail.

To handle messages, message handler functions must be registered first. This is done on a per-type basis, rather than per instance. Therefore you have to register message handlers from within the static function `RegisterMessageHandlers()`.

## Auto Generated Code

The editor may insert auto generated code into the `.ts` file. This is needed for example for variables that are supposed to show up as [exposed parameters](../../scenes/exposed-parameters.md). Special code comments are used to tag the are where the editor can insert the generated code:

```typescript
/* BEGIN AUTO-GENERATED: VARIABLES */
/* END AUTO-GENERATED: VARIABLES */
```

> **Important:**
>
> Don't remove these comments and don't put any of your code between these two lines.

## Writing Your Component

To initialize things, use the `OnSimulationStarted()` callback. For regular updates, put your code into the `Tick()` function. Use [messaging](ts-messaging.md) to communicate with unknown component types or when a delay is desired. For all known component types, you can call functions or read and write properties directly.

For an overview what functionality is available through TypeScript, check out the [TypeScript API](ts-api.md).

## See Also


* [TypeScript Asset](ts-asset.md)
* [Messaging in TypeScript Code](ts-messaging.md)
* [TypeScript API](ts-api.md)
* [Custom Code with TypeScript](typescript-overview.md)
