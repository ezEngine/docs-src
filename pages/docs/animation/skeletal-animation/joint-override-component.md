# Joint Override Component

The *joint override component* enables you to take control over the *local* transform of a specific bone. Any transform for that bone that comes from an animation is discarded and replaced with the local transform of the object on which this component is attached.

This component can be very useful if you have an object that is typically driven by animations, but a specific bone is meant to be controlled procedurally through game code. An example would be a turret which has a shoot animation for recoil etc, but you want to control the direction into which the barrel points from game code.

The joint override component works in the reverse way that the [joint attachment component](joint-attachment-component.md) works. Every time an animation pose becomes available, this component will overwrite the transform of the selected bone with its own local transform. Thus you can control the bone transform simply by moving and rotating the game object on which the joint override component is attached.

## Component Properties

* `JointName`: The *name* of the joint/bone whose transform you want to take control over. You can look up the bone names in the respective [skeleton asset](skeleton-asset.md).

* `OverridePosition`, `OverrideRotation`, `OverrideScale`: Whether the component shall override the bone *position*, *rotation* and/or *scale*.

## See Also


* [Skeletal Animations](skeletal-animation-overview.md)
* [Joint Attachment Component](joint-attachment-component.md)
