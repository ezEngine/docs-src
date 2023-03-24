# Jolt Trigger Component

The *Jolt trigger component* is a special kind of [actor](jolt-actors.md) that determines whether other actors overlap with its volume. If so, it sends a trigger [event message](../../../runtime/world/world-messaging.md). Other components or script code can react to this message to implement their game logic.

Triggers are often used to open and close doors, to check whether a character walked over a pickup item and to detect when the player reached some location.

<video src="media/trigger.webm" width="600" height="600" autoplay loop></video>

A trigger is set up the same way as a [static actor](jolt-static-actor-component.md) or a [dynamic actor](jolt-dynamic-actor-component.md), by attaching [collision shapes](../collision-shapes/jolt-shapes.md) to it. Which other physics objects activate the trigger is determined through the [collision layers](../collision-shapes/jolt-collision-layers.md) on the attached shapes.

Since triggers are not simulated like rigid bodies, they don't require much configuration.

Triggers can be moved around at runtime and they will fire, when an object enters a trigger because the trigger moved into the object.

When a trigger fires, it sends the event message `ezMsgTriggerTriggered`. The message states which other object was involved, and whether it entered or left the trigger volume. It will also pass along the `TriggerMessage` string. This can be used to identify which (kind of) trigger was just triggered.

> **Note:**
>
> Physics triggers only detect overlaps with other physics objects. For such scenarios they are an efficient solution. If, however, you need to query overlaps with other kinds of objects, you should take a look at the [spatial system](../../../runtime/world/spatial-system.md).

To achieve more complex trigger behavior, for instance to only activate something after a delay, you can utilize the [trigger delay modifier component](../../../custom-code/game-logic/trigger-delay-modifier-component.md).

## Component Properties

* `CollisionLayer`: The [collision layer](../collision-shapes/jolt-collision-layers.md) to use.
* `TriggerMessage`: The string that should be sent along with the `ezMsgTriggerTriggered`.

## See Also

* [Trigger Delay Modifier Component](../../../custom-code/game-logic/trigger-delay-modifier-component.md)
* [Jolt Actors](jolt-actors.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
* [Spatial System](../../../runtime/world/spatial-system.md)
* [Marker Component](../../../gameplay/marker-component.md)
