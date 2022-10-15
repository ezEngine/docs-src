# Jolt Swing-Twist Constraint Component

The *Jolt swing-twist constraint component* is a [constraint](jolt-constraints.md) that links two actors in a similar way to a [cone constraint](jolt-cone-constraint-component.md) but additionally constrains how much the actors may twist around their rotational axis.

<video src="media/6dof-joint.webm" width="600" height="600" autoplay loop></video>

The swing-twist constraint is more complex and thus also less stable than other constraints. If possible prefer to use a [cone constraint](jolt-cone-constraint-component.md) or a [point constraint](jolt-point-constraint-component.md).

## Component Properties

* [Shared Constraint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

* `SwingLimitY`, `SwingLimitZ`: These two angles make the constraint limit how far the child actor may tilt relative to the parent actor. This sets up a cone shape within which the child actor may be. This can be used to prevent unrealistic rotations for stiff objects.
* `Friction`: How easily the constraint rotates. Higher values make the constraint stiffer.
* `LowerTwistLimit`, `UpperTwistLimit`: How much the child actor may rotate around the main axis.

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Cone Constraint Component](jolt-cone-constraint-component.md)
* [Jolt Point Constraint Component](jolt-point-constraint-component.md)
