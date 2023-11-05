# Play Single Clip Nodes

<!-- PAGE IS TODO -->
<!-- TODO THIS PAGE IS OUTDATED -->

Animation controller graphs provide multiple node types that are used for sampling animation clips. The *play single clip node* is the most basic one. This node samples an animation clip and outputs the respective animation pose. It is thus used for typical playback of a single animation either once or in a loop. For added variety you may reference multiple animation clips, in which case the node will randomly pick one of them for playback.

<video src="../../media/skeletal-anim.webm" width="500" height="500" autoplay loop></video>

## Common Properties

All animation controller nodes that sample animation clips share these properties:

* `Loop`: If enabled the node will loop playback while its `Active` pin is triggered. Which clip exactly gets looped depends on the node. The *play single clip node* for example just loops playback in general, but randomly picks a different clip in every iteration. The [play clip sequence node (TODO)](anim-nodes-sequence.md) on the other hand will loop its middle clip instead.

* `ApplyRootMotion`: If enabled, the node will compute the [root motion](../root-motion.md) from the sampled clips and forward this to the [animation controller component](animation-controller-component.md), which may apply this to the game object's position.

* `PlaybackSpeed`: Adjusts the speed with which the animations are sampled.

* `FadeIn`, `FadeOut`: The time (in seconds) that it should take to fade an animation in and out. If this is set to `0`, the animation will immediately switch on or off when the node gets (de-)activated. If the time is non-zero, the animation will gradually fade in or out over this duration. These values are very important to cross-fade from one animation to another. For example, if a character is playing an *idle* animation and then should transition to *walk*, the walk animation should have a short *fade in* duration and the idle animation should have a *fade out* duration. The shorter of the two durations determines how long the two animations are being cross-faded to transition smoothly from one state to the other.

  Additionally, if the fade in and out values are longer than the animation itself, the animation will be forced to play back for that amount of time, typically by extending the use of the last keyframe. This can be very useful if you use an animation that only contains a static pose, for example a pose for aiming. With a `FadeIn` of 200ms this single pose will be held for 200ms but gradually faded in. That leads to a character slowly raising their hand, instead of immediately having the hand raised. The same is true for the `FadeOut` property, which again can be used to slowly lower the hand by fading out the aim pose over a longer duration.

* `ImmediateFadeIn`, `ImmediateFadeOut`: The playback starts when the `Active` pin is triggered. If `ImmediateFadeOut` is off, the clip will be played back to its very end before it is allowed to fade out. If `ImmediateFadeOut` is on, however, the animation will be faded out right away when the `Active` pin stops being triggered. If `ImmediateFadeIn` is off, once a node starts fading out, it will continue fading out until it is fully off, no matter what the `Active` pin state is. If `ImmediateFadeIn` is on, a node that has started fading out may immediately fade in again if the `Active` pin gets triggered again.

  These values determine how responsive animation playback is in regards to input changes. Immediately fading in and out can drastically reduce delay between input and a visual reaction, but may also only work well with certain animations.

## Node Properties

* `Clips`: One or multiple [animation clips](../animation-clip-asset.md) to play. If more than one is added, the node will pick one at random in every loop iteration.

## Common Input Pins

Many animation controller nodes have some or all of these input pins:

* `Active`: This pin determines whether the node samples its animation clips *at all*. Once it gets triggered in a frame, the node starts to sample its animation clips, fades them in etc. If `Loop` is enabled, the playback will repeat as long as the `Active` pin is triggered. Once the pin is not triggered anymore, the node will start to fade out its animations. Either right away (`ImmediateFadeOut` on) or when it reaches the end of the currently playing clip (`ImmediateFadeOut` off).

* `Weights`: If this pin is connected to a [bone weight node](anim-nodes-bone-weights.md), then the sampled animation clip is only applied to that part of the character. This is used to limit playback of an animation to selected body parts.

* `Speed`: This pin adjusts the overall playback speed.

## Input Pins

* `ClipIndex`: If the node has multiple `Clips` set, exactly which one will be played back can be controlled through this pin. With `ClipIndex` set to `0` the first clip is used exclusively, with `ClipIndex` set to `1` only the second clip is used, and so on. If `ClipIndex` is not connected or set to a negative value, a random clip is used.

## Common Output Pins

Many animation controller nodes have some or all of these output pins:

* `LocalPose`: The final pose from the sampled animation clips is output through this pin. This has to be passed to a [combine poses node (TODO)](anim-nodes-combine-poses.md) or a local to model pose node.

* `OnFadeOut`: This pin gets triggered for a single frame once the node changes its internal state to fade out the animation (affected by `ImmediateFadeOut` and `FadeOut`). This is typically a good time to start fading in another animation to take over. This pin is guaranteed to get triggered, even if the `FadeOut` time is zero.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
* [Bone Weight Nodes](anim-nodes-bone-weights.md)
* [Play Clip Sequence Node (TODO)](anim-nodes-sequence.md)
* [Mix Clips 2D Node (TODO)](anim-nodes-mix2d.md)
