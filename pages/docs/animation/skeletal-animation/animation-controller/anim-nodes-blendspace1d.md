# Sample Blendspace 1D Node

The *Sample Blendspace 1D* node is used to linearly interpolate between a fixed set of animations.

<video src="../../media/anim-mix1d.webm" width="500" height="500" autoplay loop></video>

Every [animation clip](../animation-clip-asset.md) is assigned a *position* value in 1D space. The `Lerp` input pin value determines how to interpolate those clips. The output pose will be either exactly one of those clips, or a mix between two clips, but never more than that.

So if one clip is placed at position `0` and another at position `1`, you can fade from the first clip to the second by passing in a *lerp value* between `0` and `1`.

The length of each clip may be different, however, the lookup positions across all clips are synchronized. That means if two clips are being mixed, and the first clip is sampled right at its middle, then the second clip will also be sampled at its middle, even if this is a completely different time offset (say 1 second versus 1.5 seconds). At which speed to move the sample position forwards, is determined by the length of the two animation clips that the *lerp value* is closest to.

This node is useful if you have an action that can be done at different speeds and you want to cover all possible speeds with just a few different animation clips. The most intuitive example is a walk/run motion. You only need two animation clips, one for slow walking and one for fast running, and this node allows you to generate any speed in between through interpolation.

For this to work, all animation clips have to follow the rule that they do the same motion at the same relative time offset. So in the case of a walk/run motion, both clips have to start with the same foot forwards, then move the other foot and finally move the first foot again, such that the animation is looped. The clips can have different lengths, though, so the *run* clip might be shorter than the *walk* clip (and therefore faster).

In the video above you can see such a transition in action. The *lerp* input value is varyied to demonstrate how the resulting interpolated animation looks. Here the node also has an *idle* and a *walk backward* clip, so it can interpolate between even more states.

## Node Properties

* `Loop`: Whether to play the animation just once from start to finish, or loop it endlessly.

* `Playback Speed`: An additional factor for speeding up or slowing down playback.

* `Apply Root Motion`: Whether [root motion](../root-motion.md) should be sampled and passed through.

* `Clips`: A list of animation clips between which this animation node will interpolate. The node will only ever sample the two clips whose `Position` values are closest the the value provided through the `Lerp` input pin. Additionally, the playback speed for each clip may be tweaked. 

## Input Pins

* `Start`: When this pin gets triggered, the node starts playback. If it is already playing, playback is reset to the start. If this pin is *not connected* playback starts right away, which is useful for nodes that play in an endless loop anyway.

* `Loop`: If connected, overrides the `Loop` property. When playback reaches the end and loop is enabled, it restarts, otherwise it stops playing and the `On Finished` output pin gets triggered.

* `Speed`: If connected, overrides the `Playback Speed` property.

* `Lerp`: This value determines which animation clips get mixed together. If the *lerp* value is in between two `Position` values of two clips, the output pose will be the linear interpolation of those two clips. If the *lerp* value is lower than the lowest `Position` value or higher than the highest, the output will be exactly that animation clip (there will be no extrapolation).

## Output Pins

* `Pose`: The resulting interpolated pose. A valid pose is only produced during playback, once the node is inactive, there is no pose output.

* `On Started`: This output pin gets triggered every time playback is started or restarted, either because of user input or because playback reached the end and was looped.

* `On Finished`: This output pin gets triggered when playback reaches the end and looping is disabled.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
* [Sample Clip Node (TODO)](anim-nodes-sample-clip.md)
* [Sample Blendspace 2D Node (TODO)](anim-nodes-blendspace2d.md)
