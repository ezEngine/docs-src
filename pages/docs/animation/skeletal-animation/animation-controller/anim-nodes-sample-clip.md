# Sample Clip Node

The *sample clip node* is the most basic node to play an animation. It is used for typical playback of a single animation either once or in a loop.

<video src="../../media/skeletal-anim.webm" width="500" height="500" autoplay loop></video>

## Node Properties

* `Loop`: Whether to play the animation just once from start to finish, or loop it endlessly.

* `Playback Speed`: Adjusts the speed with which the animation is sampled.

* `Apply Root Motion`: Whether [root motion](../root-motion.md) should be sampled and passed through.

* `Clip`: The [animation clip](../animation-clip-asset.md) to play.

## Input Pins

* `Start`: When this pin gets triggered, the node starts playback. If it is already playing, playback is reset to the start. If this pin is not connected playback starts right away, which is useful for nodes that play in an endless loop anyway.

* `Loop`: If connected, overrides the `Loop` property. When playback reaches the end and loop is enabled, it restarts, otherwise it stops playing and the `On Finished` output pin gets triggered.

* `Speed`: If connected, overrides the `Playback Speed` property.

## Output Pins

* `Pose`: The sampled pose. A valid pose is only produced during playback, once the node is inactive, there is no pose output.

* `On Started`: This output pin gets triggered every time playback is started or restarted, either because of user input or because playback reached the end and was looped.

* `On Finished`: This output pin gets triggered when playback reaches the end and looping is disabled.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
* [Sample Sequence Node](anim-nodes-sample-sequence.md)
* [Sample Blendspace 2D Node](anim-nodes-blendspace2d.md)
