# Mix Clips 2D Node

<!-- PAGE IS TODO -->
<!-- TODO THIS PAGE IS OUTDATED -->

The *Mix Clips 2D* animation controller node is used to interpolate between a set of animations which are positioned in 2D space. You give it a 2D coordinate, and it will determine which animation clips are relevant and mix them together with proper weights depending on how close the coordinate is to each clip.

The purpose of this node is to generate a continuous animation space from just a few discrete clips. This is often used for locomotion, where you only have animation clips for walking into a fixed number of directions and at certain speeds, but you'd like to be able to move a character into any direction and at any speed in between.  

<video src="../../media/anim-mix2d.webm" width="500" height="500" autoplay loop></video>

This node can generally be used to combine animations that can be thought of as having a position on a 2D plane. For example if you have animations for aiming forwards, to the left, right, up and down, you can use the mix 2D node to generate any pose in between.

Be aware that the poses will be combined linearly, though. If the poses from two clips are too different, the result may not look very good. In this case it is best to create additional clips with in-between poses.

## How To Use

You add multiple animation clips and give each clip a position (`X` and `Y`). As with the [mix clips 1D node (TODO)](anim-nodes-mix1d.md), the playback of all clips is synchronized, meaning that the length of each clip may differ, but they will be played back such that they start and end in unison. That means your clips must be authored accordingly, so for example for locomotion all clips should start with the left foot forwards, then move the right foot forwards, then the left again. From that point on the clips will be looped.

What the coordinates represent is up to you. For locomotion you could say that `X` represents left/right movement and `Y` forwards/backwards. You would then position a *walk left* clip at `(-1, 0)` a *walk right* clip at `(+1, 0)` a *walk forward* clip at `(0, +1)` and a *run forward* clip at `(0, +2)`.

Through the `X` and `Y` input pins you provide a 2D coordinate. During testing you may hook this up directly to an [input node (TODO)](anim-nodes-input.md), though later you'll probably need more control.

The node will then take that input coordinate to decide which clips should be used with what influence, and mix them together to a single output pose.

## Node Properties

See [common properties](anim-nodes-playclip.md#common-properties).

* `InputResponse`: A time duration over which changes to the `X` and `Y` input values are applied. This prevents sudden extreme changes. For example when `X` and `Y` are connected to physical buttons, which are just turned *on* or *off*, the final animation would jerk between those extremes. In a finished game you may want to smooth out the input yourself, but for starters this node can do a basic smoothing of the input values for you. Thus, if an input value switches from `1` to `0`, an `InputResponse` of 50ms means that the used value will transition smoothly towards `0` over that amount of time and thus the output pose will also transition smoothly.  

* `CenterClip`: An optional clip for the position `(0, 0)`. This clip is always played at its own speed and not synchronized to the other clips. It is meant for *idle state* animations. It may be much longer and contain many subtle motions for variation. If such behavior is not desired and instead you want the center clip to be synchronized with the rest, you can instead place a clip at position `(0, 0)` as well.

* `Clips`: The various clips. Each clip must have a unique 2D `position` assigned.

## Input Pins

See [common input pins](anim-nodes-playclip.md#common-input-pins).

* `X`, `Y`: The input coordinate to select how to blend the `Clips`. It directly relates to the clips` positions.

## Output Pins

See [common output pins](anim-nodes-playclip.md#common-output-pins).
  
## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
* [Mix Clips 1D Node (TODO)](anim-nodes-mix1d.md)
* [Play Single Clip Nodes (TODO)](anim-nodes-playclip.md)
