# Spatial Anchor Component

Many AR scenarios require virtual objects to be anchored in the real world. The simplest way to achieve this is to add an `ezSpatialAnchorComponent` to the game object in question.

This component does not have any properties. Persistance of anchors across sessions is not yet supported.

Once the component is added, it will use `ezXRSpatialAnchorsInterface` to stabilize the object's transform in the real world.

## See Also

* [XR Overview](xr-overview.md)
* [XR Input](xr-input.md)
* [Stage Space Component](stage-space-component.md)
* [Device Tracking Component](device-tracking-component.md)
