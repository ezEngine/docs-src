# TypeScript Component

The *TypeScript Component* represents a custom component that was written in TypeScript, rather than in C++.

The component itself is a C++ component. It mediates between C++ and TypeScript by forwarding C++ events and messages to the script code and back.

## Properties

`HandleGlobalEvents`: If enabled, this component acts as a [Global Event Message Handler](../../runtime/world/world-messaging.md#global-event-message-handlers). This is useful for scripts that should implement logic for an entire level.

`Script`: The [TypeScript asset](ts-asset.md) reference for which script to run.

`Parameters`: In case the referenced script has [exposed parameters](../../scenes/exposed-parameters.md), they are being listed here and can be modified. When the script gets instantiated, the values of these parameters are passed into the script. Modifying the values after the script was started currently has no effect.

## See Also


* [TypeScript Asset](ts-asset.md)
