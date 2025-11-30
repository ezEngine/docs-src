# Stage Space Component

The stage space defines the position, rotation and scale relative to which the user is placed in the virtual world. The `ezStageSpaceComponent` should be placed on the [game object](../runtime/world/game-objects.md) that best represents the character's position in the world.

By scaling the stage space, you can change the scale of the virtual user relative to the world. Turning you into a giant or a small ant. This can be very useful for physics precision for example which might not work well with very small object scales. You can compensate this by building a larger world and scaling the stage space down.

## Component Properties

* `Stage Space`: Can be either `Standing` or `Seated`. This defines the offset of the HMD to the stage space. In `Standing` mode, the stage space should be placed on the floor as the HMD will be placed relative to it matching the physical height of the user's head over the physical floor. In `Seated` mode, the HMD position relative to the stage space will match the users' head position relative to their head position when the app was started.

## See Also

* [XR Overview](xr-overview.md)
* [XR Input](xr-input.md)
* [Device Tracking Component](device-tracking-component.md)
* [Spatial Anchor Component](spatial-anchor-component.md)
