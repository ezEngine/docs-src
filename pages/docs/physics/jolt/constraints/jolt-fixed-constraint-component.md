# Jolt Fixed Constraint Component

The *Jolt fixed joint component* is the most simple [joint](jolt-constraints.md) type. It links two [actors](../actors/jolt-actors.md) together, such that they move in unison. If all you want is to merge two [shapes](../collision-shapes/jolt-shapes.md), you should just attach them to the same actor. The main use case for fixed joints is to make them *breakable*.

> **NOTE:**
>
> *Breakable* constraints are currently not implemented in Jolt.
> That means joints can't automatically break due to physical stress. At the moment you can only make
> joints break by deactivating a constraint programmatically.

<!-- 
<video src="media/fixed-joint.webm" width="600" height="600" autoplay loop></video>

Fixed joints can be used to set up very simple destructible objects.
-->

## Component Properties

* [Shared Constraint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
