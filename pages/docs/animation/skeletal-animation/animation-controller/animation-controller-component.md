# Animation Controller Component

The *animation controller component* is used to apply complex animation playback and blending functionality to an [animated mesh](../animated-mesh-component.md). It is the big brother of the [simple animation component](../simple-animation-component.md). Instead of playing just a single animation clip, it uses an [animation controller asset](animation-controller-asset.md) to determine the animation pose.

The component itself doesn't do much, other than updating the animation pose and sending it to the animated mesh. For how to control the animation playback, please see the [Animation Controller](animation-controller-overview.md) chapter.

## Component Properties

* `AnimController`: The [animation controller](animation-controller-asset.md) to use.

* `RootMotionMode`: Selects how [root motion](../root-motion.md) is applied to the owning game object.

## See Also


* [Skeletal Animations](../skeletal-animation-overview.md)
* [Simple Animation Component](../simple-animation-component.md)
* [Animation Controller](animation-controller-overview.md)
