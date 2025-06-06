# Sample Clip Node

The *sample clip node* is the most basic node to play an animation. It is used for typical playback of a single animation either once or in a loop.

<video src="../../media/skeletal-anim.webm" width="500" height="500" autoplay loop></video>

## Node Properties

* `Loop`: Whether to play the animation just once from start to finish, or loop it endlessly.

* `Playback Speed`: Adjusts the speed with which the animation is sampled.

* `Root Motion Amount`: How much [root motion](../root-motion.md) should be applied. A value of zero deactivates root motion, a value of 1 passes the motion from the clip through. Smaller or higher values can be used to tweak the movement speed.

* `Clip`: The [animation clip](../animation-clip-asset.md) to play.

## Input Pins

* `Start`: When this pin gets triggered, the node starts playback. If it is already playing, playback is reset to the start. If this pin is not connected playback starts right away, which is useful for nodes that play in an endless loop anyway.

* `Loop`: If connected, overrides the `Loop` property. When playback reaches the end and loop is enabled, it restarts, otherwise it stops playing and the `On Finished` output pin gets triggered.

* `Speed`: If connected, overrides the `Playback Speed` property.

## Output Pins

* `Pose`: The sampled pose. Once playback reaches the end of the clip and is not set to loop, the last frame is output indefinitely.

* `On Started`: This output pin gets triggered every time playback is started or restarted, either because of user input or because playback reached the end and was looped.

* `On Finished`: This output pin gets triggered when playback reaches the end and looping is disabled.

## See Also

* [Animation Graph](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
* [Sample Sequence Node](anim-nodes-sample-sequence.md)
* [Sample Blendspace 2D Node](anim-nodes-blendspace2d.md)
