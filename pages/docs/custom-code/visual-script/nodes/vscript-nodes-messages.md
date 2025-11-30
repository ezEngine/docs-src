# Visual Script: Message Nodes

## Messages

While [event handler nodes](vscript-nodes-events.md) react to incoming messages, message nodes allow scripts to *send messages* to other objects. This is the primary mechanism for communication between components and game objects.

Message delivery modes:

* **Direct to component** - Send a message to a specific component
* **Broadcast to object** - Deliver to all components on a game object
* **Recursive broadcast** - Send to an entire sub-tree of objects and components
* **Event mode** - Deliver *upwards* along the parent chain to the closest handler (see [event messages](../../runtime/world/world-messaging.md#event-messages))

The `Send Mode` property controls how messages propagate through the hierarchy. When set to *Event*, messages travel upward through parent objects until a component handles them, enabling event bubbling similar to UI event systems.

Message nodes are essential for decoupled communication. Instead of directly calling functions on other components, you send messages that any component can choose to handle. This keeps scripts flexible and reusable. See the [world messaging documentation](../../runtime/world/world-messaging.md) for a comprehensive guide to the messaging system.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [World Messaging](../../runtime/world/world-messaging.md)
* [Event Handler Nodes](vscript-nodes-events.md)
* [Game Object Nodes](vscript-nodes-game-object.md)
