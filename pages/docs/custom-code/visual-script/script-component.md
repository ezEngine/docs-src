# Script Component

The *Script Component* represents a custom component that was written using [visual scripting](visual-script-overview.md) or [AngelScript](../angelscript/angelscript-overview.md).

The component itself is a C++ component. It mediates between C++ and the script code by forwarding C++ events and messages to the script and back.

## Component Properties

* `HandleGlobalEvents`: If enabled, this component acts as a [Global Event Message Handler](../../runtime/world/world-messaging.md#global-event-message-handlers). This is useful for scripts that should implement logic for an entire level.

* `UpdateInterval`: How much time passes between script updates. Set this to zero, to have the script update every frame. Larger intervals are better for performance. Scripts can dynamically modify their update interval, such that they are called less often when idle, and more often, when they need to react in a timely manner to player input.

* `UpdateOnlyWhenSimulating`: By default, scripts are only updated when the scene is simulated, but not during regular editing. Enable this, to have a script also update during editing. This allows to use the script to display results at edit time, for example the script may place objects procedurally, and this should be live-editable.

* `ScriptClass`: The [visual script](visual-script-class-asset.md) or [AngelScript](../angelscript/as-asset.md)to execute.

* `Parameters`: In case the referenced script has [exposed parameters](../../concepts/exposed-parameters.md), they are listed here and can be modified. When the script gets instantiated, the values of these parameters are passed into the script.

## See Also

* [Custom Code](../custom-code-overview.md)
* [Custom Code with Visual Scripts](visual-script-overview.md)
* [Custom Code with AngelScript](../angelscript/angelscript-overview.md)
