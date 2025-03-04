# Messaging in AngelScript Code

AngelScript components can both send and receive messages. The way messages can be sent, posted and received, and how messages are routed is identical to the behavior on the C++ side. Please read the chapter about [messaging](../../runtime/world/world-messaging.md) to familiarize yourself with the general concepts.

The main difference in AngelScript is, that messages that have been declared in C++ can be sent and received in AngelScript, but messages that have been declared in AngelScript can only be sent and received by AngelScript code.

## Sending Messages

You can send a message directly to a specific component or game object, through these functions:

* `ezGameObject::SendMessage()`
* `ezGameObject::SendMessageRecursive()`
* `ezGameObject::PostMessage()`
* `ezGameObject::PostMessageRecursive()`
* `ezComponent::SendMessage()`
* `ezComponent::PostMessage()`

You can also send messages through `ezWorld` which is more convenient when you only have an `ezGameObjectHandle` or `ezComponentHandle`.

### Event Messages

You can send *event messages* on any game object with `ezGameObject::SendEventMessage()` or `ezGameObject::PostEventMessage()`.

## Handling Messages

To handle messages of a specific type, a component needs a function that takes that message type as a *handle* (using the '@' suffix) as its only parameter. Also the function name must start with **OnMsg**:

```cpp
void OnMsgSetColor(ezMsgSetColor@ msg)
{
    ezLog::Info("MsgSetColor: {}, {}, {}, {}", msg.Color.r, msg.Color.g, msg.Color.b, msg.Color.a);
}
```

## Declaring a Message in AngelScript

You declare a custom message in AngelScript by deriving from `ezAngelScriptMessage`:

```cpp
class MsgShowText : ezAngelScriptMessage
{    
    ezString text;
}
```

If you need to send a message from one component and handle it in another component type, you should put the message declaration into a separate `.as` file and [#include](as-api.md#including-files) that file from both component files.

### AngelScript Event Messages

At the moment it is not supported to send AngelScript messages as event messages.

## See Also

* [Messaging](../../runtime/world/world-messaging.md)
* [Custom Code with AngelScript](angelscript-overview.md)
