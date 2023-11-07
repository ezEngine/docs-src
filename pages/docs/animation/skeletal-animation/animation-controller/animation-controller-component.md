# Animation Controller Component

The *animation controller component* is used to apply complex animation playback and blending functionality to an [animated mesh](../animated-mesh-component.md). It is the big brother of the [simple animation component](../simple-animation-component.md). Instead of playing just a single animation clip, it uses an [animation graph asset](animation-graph-asset.md) to determine the animation pose.

The component itself doesn't do much, other than updating the animation pose and sending it to the animated mesh. For how to control the animation playback, please see the [Animation Graph (TODO)](animation-graph-overview.md) chapter.

## Component Properties

* `AnimGraph`: The [animation graph](animation-graph-asset.md) to use.

* `RootMotionMode`: Selects how [root motion](../root-motion.md) is applied to the owning game object.

* `InvisibleUpdateRate`: How often to update the animation when the object is not visible. For performance reasons the update rate should be very low or even paused when an object isn't visible. However, since animations may have an important impact on gameplay, it can be undesirable to have a lower update rate even when the object is not visible. Note that this affects the update rate of objects that are not visible by the main camera, but by a shadow casting light. Objects whose shadow can be seen generally get updated, but at a low rate, unless this setting forces a higher update rate.

## See Also

* [Skeletal Animations](../skeletal-animation-overview.md)
* [Simple Animation Component](../simple-animation-component.md)
* [Animation Graph (TODO)](animation-graph-overview.md)
