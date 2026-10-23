# Trigger Delay Modifier Component

Handles `ezMsgTriggerTriggered` events and sends new messages after a delay. This is typically used to activate something not right away, but when something is present inside a trigger volume for a minimum duration. Similarly, it can also be used from deactivating something too early.

The *enter* and *leave* messages are sent only when an empty trigger is entered or when the last object leaves the trigger. While any object is already inside the trigger, no change event is sent. Therefore this component can't be used to keep track of all the objects inside a trigger.

The *enter* and *leave* events can be sent with a delay. The *enter* event is only sent, if the trigger had at least one object inside it for the full duration of the delay. Which exact object may change, but once the trigger contains no object, the timer is reset.

The sent `ezMsgTriggerTriggered` does not contain a reference to the *triggering* object, since there may be multiple and they may change randomly.

## Setup

The trigger delay modifier has to sit between the trigger and the component that reacts to the trigger, in the object hierarchy:

* Put the trigger delay modifier on the **same object** as the trigger component (for example the [Jolt Trigger Component](../../physics/jolt/actors/jolt-trigger-component.md) and its shape).
* Put the component that handles the trigger message (for example a [script component](../visual-script/visual-script-overview.md)) on the **parent** of that object.

```text
Parent object          <- Script Component (receives the delayed message)
  └─ Trigger object    <- Jolt Trigger, Shape, Trigger Delay Modifier
```

The trigger sends its event message to the components on its own object first. The trigger delay modifier handles it there and, after the delay, sends a new message to the parent object.

If the script component is on the same object as the trigger, it receives the original, undelayed message directly, and the delayed message goes to the parent, where nothing handles it. The trigger then appears to have no delay at all.

The *Testing Chambers* sample uses this setup in the `Main` scene: the rotating ship is activated one second after the player enters its trigger and deactivated two seconds after the player left.

## Component Properties

* `ActivationDelay`, `DeactivationDelay`: The time that an object needs to be present inside the trigger, or have fully left the trigger area, before the trigger is considered to be activated or deactivated. Only after this delay is the `ezMsgTriggerTriggered` event sent to the parent object.  

## See Also

* [Jolt Trigger Component](../../physics/jolt/actors/jolt-trigger-component.md)
* [Messaging](../../runtime/world/world-messaging.md)
