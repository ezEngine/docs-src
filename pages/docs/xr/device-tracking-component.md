# Device Tracking Component

To automatically make a game object follow the HMD or one of the controllers, you can attach a `ezDeviceTrackingComponent` to a game object.

## Component Properties

* `Device Type`: Which device we want to track. E.g. the HMD (a.k.a. your head) or one of the controllers.
* `Pose Location`: Some input devices have different poses for `Grip` and `Aim`. E.g. your hand's grip position is in the middle of your fist pointing upwards, while the aim position is at your index finger pointing forward.
* `Transform Space`: Whether the local or global transform should be set to the input device's transform.
* `Rotation`: Whether to apply rotation to the game object. Translation is always applied but in some cases it might be useful to not apply rotation. E.g. for helper nodes in the scene.
* `Scale`: Whether to apply scale to the game object. This has no affect in `local` space as no device type has scale. If `Transform Space` is set to `global`, the scale of the object will will match the scale of the stage space.

## See Also

* [XR Overview](xr-overview.md)
* [XR Input](xr-input.md)
* [Stage Space Component](stage-space-component.md)
* [Spatial Anchor Component](spatial-anchor-component.md)
