# Pose Generation Nodes

These nodes are responsible for generating poses. They may create them procedurally, by sampling [animation clips](../animation-clip-asset.md) or a combination of the two.

## Rest Pose Node

This node always outputs the *rest pose* of a skeleton. It has no configuration options or input pins. It is mainly used to provide a fallback pose when nothing else is available, especially during testing.

## Sample Blendspace 1D Node

This node uses a 1D coordinate to select two clips for synchronized sampling and blending between them.

See [Sample Blendspace 1D Node](anim-nodes-blendspace1d.md) for details.

## Sample Blendspace 2D Node

This node uses a 2D coordinate to select from a range of clips which ones to sample in a synchronized fashion and blend between them.

See [Sample Blendspace 2D Node](anim-nodes-blendspace2d.md) for details.

## Sample Clip Node

This node plays back a single animation clip.

See [Sample Clip Node](anim-nodes-sample-clip.md) for details.

## Sample Clip Sequence Node

This node plays back multiple clips in sequence, optionally using one clip for start (fade in), one or multiple clips for the middle section (which may loop) and optionally one clip for the end (fade out).

See [Sample Sequence Node](anim-nodes-sample-sequence.md) for details.

## Sample Frame Node

This node samples an animation clip at a specific, constant time and outputs that pose. There is no automatic playback. You can pass in the sample position to dynamically select which frame to sample, but often this is used to just sample the first or last frame of an animation clip to hold a specific pose.

### Node Properties

* `Clip`: The [animation clip](../animation-clip-asset.md) to sample.

* `Norm Pos`: The *normalized* sample position. This is a value between `0` and `1` where zero maps to the start of the clip, `0.5` to the exact middle and one to the very last frame of the clip.

### Input Pins

* `Norm Pos`: If connected, overrides the `Norm Pos` property.

* `Abs Pos`: If connected, overrides the `Norm Pos` value with an absolute playback position, which means you can pass in the actual time value where to sample a clip. Note that you could use this for proper playback of a clip, but it lacks features such as getting informed when the clip finishes, [animation events](../animation-events.md) and so on. Prefer to use a [Sample Clip node](anim-nodes-sample-clip.md) instead.

### Output Pins

* `Pose`: The pose of the animation clip at the given position.

## See Also

* [Animation Graphs](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
