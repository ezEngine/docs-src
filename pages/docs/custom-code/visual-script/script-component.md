# Script Component

The *Script Component* represents a custom component that was written using [visual scripting](visual-script-class-asset.md).

The component itself is a C++ component. It mediates between C++ and the visual script by forwarding C++ events and messages to the script and back.

## Component Properties

* `HandleGlobalEvents`: If enabled, this component acts as a [Global Event Message Handler](../../runtime/world/world-messaging.md#global-event-message-handlers). This is useful for scripts that should implement logic for an entire level.

* `Script`: The [visual script](visual-script-class-asset.md) to execute.

* `Parameters`: In case the referenced script has [exposed parameters](../../scenes/exposed-parameters.md), they are listed here and can be modified. When the script gets instantiated, the values of these parameters are passed into the script.

## See Also

* [Custom Code with Visual Scripts](visual-script-overview.md)
* [Visual Script Class Asset](visual-script-class-asset.md)
* [Custom Code](../custom-code-overview.md)
