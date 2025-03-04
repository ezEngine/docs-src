# Custom Components with AngelScript

To create a new component type, create a new [AngelScript asset](as-asset.md). In that asset document, select the `Source` mode to edit the script either inline or in an external editor.

Choose a name for your component class and make sure the name is also specified in the asset `Class Name` property.

## Base Class

Your component class must derive from the base class `ezAngelScriptClass` either directly or indirectly.

## Entry Points

If any of these functions is present, the [script component](../visual-script/script-component.md) will execute them in the same way as for C++ components. See [Component Activation](../../runtime/world/components.md#component-activation) for details.

* `void OnActivated()`: If present, this is executed every time the component *active state* changes to *active*. This is usually shortly after component creation. In an editor this happens right after scene loading or when a new object is added. It is rare to use this entry point, except when your component supports being deactivated and re-actived multiple times.

* `void OnDeactivated()`: If present, this is executed when the component *active state* changes to *inactive*. This happens shortly before destruction, and when the component is deliberately deactivated.

* `void OnSimulationStarted()`: If present, this function gets executed when the game simulation starts. In an editor this happens when you [run the scene](../../editor/run-scene.md) in any way. This is where you should execute first time setup code, for example to detect which child objects exist to store handles to them.

* `void Update(ezTime deltaTime)`: If present, this function gets executed in regular intervals. The interval can be configured on the script component, but the script can also dynamically adjust it through the function `ezAngelScriptClass::SetUpdateInterval()`.
The `deltaTime` argument gives you the time between calls to `Update()`, which is typically what you should use to update game logic.

If none of these entry points is present, the class must have at least one [message handler](as-messaging.md#handling-messages).

## Message Handlers

AngelScript components can both send and receive messages. The article [Messaging in AngelScript Code](as-messaging.md) explains this in more detail.

## Writing Your Component

To initialize things, use the `OnSimulationStarted()` callback. For regular updates, put your code into the `Update()` function. Use [messaging](as-messaging.md) to communicate with unknown component types or when a delay is desired.

For an overview what functionality is available through AngelScript, check out the [AngelScript API](as-api.md).

## See Also

* [AngelScript Asset](as-asset.md)
* [Messaging in AngelScript Code](as-messaging.md)
* [AngelScript API](as-api.md)