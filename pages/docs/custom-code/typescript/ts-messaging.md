# Messaging in TypeScript Code

TypeScript components can both send and receive messages. The way messages can be sent, posted and received, and how messages are routed is identical to the behavior on the C++ side. Please read the chapter about [messaging](../../runtime/world/world-messaging.md) to familiarize yourself with the general concepts.

The main difference in TypeScript is, that messages that have been declared in C++ can be sent and received in TypeScript, but messages that have been declared in TypeScript can only be sent and received by TypeScript code.

## Sending Messages

You can either send a message directly to a specific component (through `ez.Component`) or to a game object hierarchy (through `ez.GameObject`). Contrary to the C++ API, there are no functions on `ez.World` to send messages.

The `SendMessage()` functions on `ez.Component` and `ez.GameObject` take an additional boolean parameter `expectResultData`. If this is set to true, that means that the sender of the message expects the receiver(s) to write back result data into the sent message, and intends to read those results afterwards. If it is set to false, the message sender does either not expect result data in the message, or doesn't intend to read it. This is an optimization, if you need any result data, set the parameter to true, which means additional work is necessary to synchronize the message back to the caller. Otherwise keep this set to the default value (false).

### Sending Event Messages

TypeScript components can raise *event messages* on themselves through `ez.TypescriptComponent.BroadcastEvent()`.

> **Note:**
>
> At the moment TypeScript components can't raise event messages on other components or game objects.

## Handling Messages

To handle messages of a specific type, a component needs a function that takes that message type as its only parameter, and it must register that function as a message handler:

```typescript
static RegisterMessageHandlers()
{
    ez.TypescriptComponent.RegisterMessageHandler(ez.MsgSetColor, "OnMsgSetColor");
}

OnMsgSetColor(msg: ez.MsgSetColor): void
{
    ez.Log.Info("MsgSetColor: " + msg.Color.r + ", " + msg.Color.g + ", " + msg.Color.b + ", " + msg.Color.a);
}
```

The static function `RegisterMessageHandlers()` is the only place where your code may call `ez.TypescriptComponent.RegisterMessageHandler()`. It is an error to call this from anywhere else.

## Declaring a Message in TypeScript

You declare a custom message in TypeScript by extending `ez.Message`:

```typescript
export class MsgShowText extends ez.Message {

    EZ_DECLARE_MESSAGE_TYPE;
    
    text: string;
}
```

> **Important:**
>
> It is vital to insert `EZ_DECLARE_MESSAGE_TYPE;` into the body of the message to make it work.

If you need to send a message from one component and handle it in other component types, you should put the message declaration into a separate `.ts` file and `import` that file from both component files. See [Importing Files (`require`)](ts-api.md#importing-files-require) for details.

### Declaring Event Messages

> **Note:**
>
> At the moment it is **not supported to declare event messages**.

## See Also


* [TypeScript API](ts-api.md)
* [Custom Components with TypeScript](custom-ts-components.md)
