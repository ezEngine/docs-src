# Pose Blending Nodes

An animation graph typically samples more than one animation. Sometimes these animations should be combined and sometimes you just wish to smoothly switch from one animation to another.

## Lerp Poses Node

The *lerp poses node* linearly interpolates between two poses. It is typically used to fade over from one pose to another and potentially to a third. Note that the node only controls the mix of the two animation poses, it is not used for synchronizing playback across clips. See the [Sample Blendspace 1D Node (TODO)](anim-nodes-blendspace1d.md) for that.

### Node Properties

* `Lerp`: The *linear interpolation* value that determines which clips get combined. For values between `0` and `1` the input poses `0` and `1` get combined. For example at `0.5` the two poses get combined half and half, whereas at `0.9` clip `0` is used with 10% strength and clip `1` is used with 90% strength. For *lerp values* between `1` and `2` the poses `1` and `2` get combined, for example at `1.5` the two are combined half and half.

* `Poses Count`: How many input pose pins to show.

### Input Pins

* `Lerp`: A pin to dynamically pass in the *linear interpolation* value. See the node properties above.

* `Poses[]`: The array of input poses.

### Output Pins

* `Pose`: The combined output pose.

## Pose Switch Node

The *Pose Switch Node* is used to quickly but smoothly transition from one pose to another. The incoming poses are typically different animations. Note that the pose switch has no influence over the playback position of an incoming pose, so you may need to make sure that the target animation to switch to, gets restarted from the beginning.

### Node Properties

* `Transition Duration`: The time to take for transitioning from the previously active pose to the now active pose.

* `Poses Count`: How many input pose pins to show.

### Input Pins

* `Index`: Which input pose to use. If the index changes, the node will transition from the previously active pose to the new pose using linear blending. The index may switch from any value to any other value in range, it doesn't need to change only up or down.

* `Poses[]`: The array of available poses.

### Output Pins

* `Pose`: The combined output pose.

## See Also

* [Animation Graphs (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
