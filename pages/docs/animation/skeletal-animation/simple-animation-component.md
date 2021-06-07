# Simple Animation Component

The *simple animation component* is used to play a single [animation clip](animation-clip-asset.md) on an [animated mesh](animated-mesh-component.md).

<video src="../media/skeletal-anim.webm" width="500" height="500" autoplay loop></video>

The component has to be attached on a [game object](../../runtime/world/game-objects.md) that also has an [animated mesh component](animated-mesh-component.md). The selected animation clip has to be compatible with the mesh's [skeleton](skeleton-asset.md).

For more complex scenarios use an [animation controller](animation-controller/animation-controller-overview.md) instead.

## Component Properties

* `AnimationClip`: The [animation clip](animation-clip-asset.md) to play.

* `AnimationMode`: How to play the animation:

  * `Once`: The animation is played exactly once and then stops.
  * `Loop`: The animation is played in an endless loop.
  * `BackAndForth`: The animation is played to its end, then it reverses and plays back to the start. Then the cycle repeats.

* `Speed`: The playback speed. A speed of zero pauses playback. A negative speed makes the animation play backwards. The speed can be changed at any time.

* `RootMotionMode`: Selects how [root motion](root-motion.md) is applied to the owning game object.

## Events

The component will broadcast the event `ezMsgGenericEvent` every time it encounters an [animation event](animation-events.md) in the animation clip. [Custom code](../../custom-code/custom-code-overview.md) can listen for these events and trigger relevant game mechanics.

## See Also


* [Skeletal Animations](skeletal-animation-overview.md)
* [Animation Clip Asset](animation-clip-asset.md)
* [Animated Mesh Component](animated-mesh-component.md)
* [Animation Controller](animation-controller/animation-controller-overview.md)
