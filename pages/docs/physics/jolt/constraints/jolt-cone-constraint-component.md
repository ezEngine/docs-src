# Jolt Cone Constraint Component

The *Jolt cone constraint component* is a [constraint](jolt-constraints.md) that links two actors in a similar way to a [point constraint](jolt-point-constraint-component.md) but additionally constrains the maximum angle that the actors can swing.

<video src="media/6dof-joint.webm" width="600" height="600" autoplay loop></video>

If additionally the maximum twist around the rotational axis shall be constrained, use a [swing-twist constraint](jolt-swing-twist-constraint-component.md).

## Component Properties

* [Shared Constraint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

* `ConeAngle`: The maximum angle how for the child actor may tilt or swing relative to the parent actor. This sets up a cone shape within which the child actor may be. This can be used to prevent unrealistic rotations for stiff objects.

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Point Constraint Component](jolt-point-constraint-component.md)
* [Jolt Swing-Twist Constraint Component](jolt-swing-twist-constraint-component.md)
