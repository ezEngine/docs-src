# Reset Transform Component

This component sets the local transform of its owner to known values when the simulation starts.

It is meant for use cases where an object may be activated and deactivated over and over.
For example due to a state machine switching between different object states by (de-)activating a sub-tree of objects.

Every time an object becomes active, it may want to start moving again from a fixed location.
This component helps with that, by reseting the local transform of its owner to such a fixed location once.

After that, it does nothing else, until it gets deactivated and reactivated again.

## Component Properties

* `ResetPositionX`, `ResetPositionY`, `ResetPositionZ`: Whether to reset the x, y and z component of the local position.
* `LocalPosition`: The local position value to reset the owner's transform to.
* `ResetRotation`: Whether to reset the local rotation. 
* `LocalRotation`: The local rotation value to reset the owner's transform to.
* `ResetScaling`: Whether to reset the local scaling.
* `LocalScaling`, `LocalUniformScaling`: The uniform and non-uniform local scaling value to reset the owner's transform to.

## See Also

* [Property Animations (TODO)](property-animation-overview.md)
* [Follow Path Component](../paths/follow-path-component.md)
