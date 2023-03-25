# Power Connector Component

This component is for propagating the flow of power in cables or fluid in pipes and determine whether it arrives at a receiver.

It is meant for building puzzles where you have to connect the right objects to power something. It uses physics constraints to physically connect two pieces and have them snap together.

The component also reacts to being grabbed (`ezMsgObjectGrabbed`) to disconnect.
On its own this component doesn't do anything. However, it can be set to be *connected* to another object with a power connector component, in which case it would propagate its own *output* as the *input* on that component.

If its output is non-zero and thus the input on the connected component is also non-zero, the other component will post `ezEventMsgSetPowerInput`, to which a script can react and for example switch a light on.

Connectors are bi-directional ("full duplex"), so they can have both an input and an output and the two values are independent of each other. That means power can flow in both or just one direction and therefore it is not important with which end a cable gets connected to something.

To enable building things like cables, each power connector component can also have a *buddy*, which is an object on which another power connector component exists. If a connector gets input, that input value is propagated to the buddy as its output value. Thus when a cable gets input on one end, the other end (if it is properly set as the buddy) will output that value. So if that end is also *connected* to something, the output will be further propagated as the *input* on that object. This can go through many hops until the value reaches the final connector (if you build a circular chain it will stop when it reaches the starting point).

The component automatically connects to another object when it receives a `ezMsgSensorDetectedObjectsChanged`, so it should have a child object with a [sensor](../ai/sensor-components.md). The sensor should use a dedicated [spatial category](../runtime/world/spatial-system.md) to search for [markers](marker-component.md) where it can connect.

To have a sensor (or other effects) only active when the connector is grabbed, put them in a child object with the name *ActiveWhenGrabbed* and disable the object by default. The parent power connector component will toggle the active flag of that object when it gets grabbed or let go.

To build a cable, don't forget to set each end as the *buddy* of the other end.

## Properties

* `Output`: Sets how much output (of whatever kind) this connector produces.

  If this is zero, it is either a receiver, or a pass-through connector, e.g. a cable, or just currently inactive.

  If this is non-zero, it acts like a source, and when another connector gets connected to it, that output will be propagated through the connection/buddy chain.

* `Buddy`: If this is intended to act like a cable with two ends, specify the [object references](../scenes/object-references.md) to the other end of the cable here. This way, if this end gets power, the other end will output that power, and vice versa.

* `ConnectedTo`: If this object is supposed to start in a state connected to something else, e.g. a power socket or another cable, use this [object references](../scenes/object-references.md) to configure it connected. Note that this will create a physics joint with between this object and the target object. If they aren't aligned already, this will make the two objects snap together during the first simulation steps.

## Message Handlers

* `ezMsgSensorDetectedObjectsChanged`: Tells the connector that it is close to another connector that it should attach to. If a [sensor components](../ai/sensor-components.md) is active on the same object, this can automatically make the connector connect to other things that it comes close to.

* `ezMsgObjectGrabbed`: Tells the connector that it was just grabbed, e.g. by a [grab object component](../physics/jolt/special/jolt-grab-object-component.md). Will make it disconnect, if it is currently attached to anything.

## Events

* `ezEventMsgSetPowerInput`: This event is sent every time the available power input changes. This is the power that 'arrives' at the connector. Note that power is never 'used up'. It should just be seen as a threshold value to decide whether something receives enough power to be active.

## See Also

* [Jolt Rope Component](../physics/jolt/special/jolt-rope-component.md)
* [Jolt Fixed Constraint Component](../physics/jolt/constraints/jolt-fixed-constraint-component.md)
* [Sensor Components](../ai/sensor-components.md)
* [Spatial System](../runtime/world/spatial-system.md)
