# Jolt Point Constraint Component

The *Jolt point constraint component* is a [constraint](jolt-constraints.md) that links two actors with a *ball and socket constraint*, meaning the actors can rotate around the constraint's pivot point, but cannot move apart.

<video src="media/spherical-joint.webm" width="600" height="600" autoplay loop></video>

The point constraint is very simple and therefore also quite stable. If you can get away with its limited functionality, prefer to use it over more complex constraints.

If the maximum swing or twist angle shall be constrained, use a [cone constraint](jolt-cone-constraint-component.md) or a [swing-twist constraint](jolt-swing-twist-constraint-component.md).

## Component Properties

* [Shared Joint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Cone Constraint Component](jolt-cone-constraint-component.md)
* [Jolt Swing-Twist Constraint Component](jolt-swing-twist-constraint-component.md)
