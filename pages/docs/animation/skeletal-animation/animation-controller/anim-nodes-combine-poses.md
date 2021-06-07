# Combine Poses Nodes

An animation controller typically samples more than one animation. For example you may want to play a walking animation on the lower part of a character, and an aim weapon animation on the upper part. These animations are generally independent of each other, but have to be combined at some point, to form the final single animation pose.

Certain nodes in the animation controller graph allow you to accomplish this.

## Combine Poses Node

Currently the `Combine Poses` node is the only available node to combine multiple poses in *local space* into one.

### Properties

* **MaxPoses**: The maximum number of *active* poses to blend. You can have more input pins connected to this node. This number just says how many of them will be blended, if more poses than this are actually active at any given time. If more poses are active, the ones with the lowest *weight* will be ignored.

Example: Let's say this value is set to 2. You have three input poses connected. One for walking, one for aiming a gun and one as a general breathing / idle animation. If all three poses are active at the same time, one of them will be ignored. For example, if walking and aiming both have a weight of 1, but breathing has a weight of 0.5, the breathing animation will not be mixed into the final result.

This is used to clamp the maximum performance cost of the animation blending.

### Input Pins

* **LocalPoses**: This is a single input pin that allows an unlimited number of connections. Each incoming pose carries not only the bone transformations, but also the *bone weights*. These are typically determined by the animation clip sampling nodes and the [bone weight nodes](anim-nodes-bone-weights.md). All poses are mixed together according to their overall weight.

In practice that means that two animations that don't use custom [bone weights](anim-nodes-bone-weights.md) will be blended 50:50.

### Output Pins

* **LocalPose**: The single combined pose in *local space*. It is common to pass this directly on to a [Local To Model Pose node](anim-nodes-modelspace.md).

### Performance Considerations

You can use multiple nodes to combine many poses in several steps. However, for best performance prefer to use only a single node to combine many poses and make use of [bone weights](anim-nodes-bone-weights.md) to control each ones overall influence.


## See Also


* [Animation Controller](animation-controller-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
