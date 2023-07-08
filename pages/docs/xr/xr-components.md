# XR Components

## Stage Space Component

The stage space defines the position, rotation and scale relative to which the user is placed in the virtual world. The `ezStageSpaceComponent` should be placed on the [game object](../runtime/world/game-objects.md) that best represents the characters position in the world.
By scaling the stage space, you can change the scale of the virtual user relative to the world. Turning you into a giant or a small ant. This can be very useful for physics precision for example which might not work well with very small object scales. You can compensate this by scaling the world up and the stage space down. 

### Component Properties
* `Stage Space`: Can be either `Standing` or `Seated`. This defines the offset of the HMD to the stage space. In `Standing` mode, the stage space should be placed on the floor as the HMD will be placed relative to it matching the physical height of the user's head over the physical floor. In `Seated` mode, the HMD position relative to the stage space will match the users' head position relative to their head position when the app was started.


## Device Tracking Component

To automatically make a game object follow the HMD or one of the controllers, you can attach a `ezDeviceTrackingComponent` to a game object.

### Component Properties
* `Device Type`: Which device we want to track. E.g. the HMD (a.k.a. your head) or one of the controllers.
* `Pose Location`: Some input devices have different poses for `Grip` and `Aim`. E.g. your hand's grip position is in the middle of your fist pointing upwards, while the aim position is at your index finger pointing forward.
* `Transform Space`: Whether the local or global transform should be set to the input device's transform.
* `Rotation`: Whether to apply rotation to the game object. Translation is always applied but in some cases it might be useful to not apply rotation. E.g. for helper nodes in the scene.
* `Scale`: Whether to apply scale to the game object. All input devices usually have an identity scale. If you don't want this to be overwritten while tracking, disable this option.


## Spatial Anchor Component

Many AR scenarios require virtual objects to be anchored in the real world. The simplest way to achieve this is to add an `ezSpatialAnchorComponent` to the game object in question.

This component does not have any properties. Persistance of anchors across sessions is not yet supported.

Once the component is added, it will use `ezXRSpatialAnchorsInterface` to stabilize the objects transform in hte real world.


## Visualize Hand Component

For debugging, it can be useful to visualize tracked hands. Create a `ezVisualizeHandComponent` and attach it to a random game object to achieve this. No properties exist for this component.

## See Also

* [XR Overview](xr-overview.md)
* [XR Input](xr-input.md)
