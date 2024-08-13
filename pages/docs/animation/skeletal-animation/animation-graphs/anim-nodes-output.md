# Output Nodes

Every [animation graph](animation-graph-overview.md) must have at least one output node. All nodes that shall affect the result must ultimately be connected to an output node.

The *pose result* nodes do not define the final result, though. Rather the final result is a mix of all poses that reach a *pose result* node. This makes it easier to set up many different animations and also split work up into several animation graphs. 

You can quickly deactivate an entire part of the graph by removing the connection to the output node. Nodes that are not connected to the output are not evaluated at runtime and therefore don't cost any performance.

## Pose Result Node

The *pose result* node is used to output *one* animation result. A more complex animation graph will contain many pose result nodes. All poses from *active* pose result nodes (the ones that have a non-zero `Target Weight`) will be combined according to their weight.

Usually you would set up the graph such, that all actions that could overlap flow into their own pose result nodes. For example you may have one sub graph that is responsible for walk animations and another one for jump animations. When jumping, the system should fade over from walking into jumping and thus there is a short duration of overlap. To achieve this, both sub graphs would have their own *pose result* node and when the jump starts, the jump sub graph fades its output in (by setting its `Target Weight` to `1`) and the walk sub graph fades its pose out respectively. The animation system takes care of combining the output poses accoring to their current weight.

Now consider that you may have two different jump animations, one for when the character is standing and one while it is walking. These cases are mutually exclusive, and thus there is no need for separate output nodes for the two jump styles. In this case one would rather use one of the [pose blending nodes](anim-nodes-pose-blending.md) to select the desired jump animation and feed it into one output node.

However, you *could* use different pose result nodes, regardless, if it is easier to set up the animation this way, there is no performance penalty for using additional nodes as long as the number of simultaneously active nodes is low.

### Node Properties

* `Fade Duration`: How long to fade the result pose in or out when the `Target Weight` changes. 

### Input Pins

* `Pose`: The pose to combine with all other active pose results.

* `Target Weight`: How strongly to apply the pose to the output. This should be used to signal whether the output is active, at all. Pass in `0` once an animation should be deactivated. Pass in `1` while it is active. The `Fade Duration` is used to ramp up or down the overall weight. If this pin is not connected, the node is considered to be always active and thus always combined with the other outputs, which may result in undesirable behavior, if this sub-graph sometimes doesn't actually provide a real pose.
 
* `Fade Duration`: When connected, overrides the `Fade Duration` property.

* `Weights`: The [bone weights](anim-nodes-bone-weights.md) to use to apply this pose only to a subset of bones. If the pin is not connected, the pose applies to the full skeleton.

### Output Pins

* `On Faded Out`: This event pin is triggered when the output node has finished fading out.

* `On Faded In`: This event pin is triggered when the output node has finished fading in.

* `Current Weight`: A data pin that outputs the currently used target weight, which changes over the fade duration.

> **Careful!**
>
> Using the output pins it is easily possible to build a **circular graph**, which is not allowed. Make sure that the output of this node is not fed into the input of itself. Use [blackboard nodes](anim-nodes-blackboard.md) or [event nodes](anim-nodes-events.md) to forward information and, if necessary, feed it back as input during the next graph update.

## Root Rotation Node

This node is used to add angular [root motion](../root-motion.md) to the final pose. It enables the animation to change the rotation of the [game object](../../../runtime/world/game-objects.md) on which it is played. This is mainly convenient for simpler use cases and for prototyping. In more complex scenarios you may prefer to control the object's orientation with [custom code](../../../custom-code/custom-code-overview.md).

### Input Pins

* `Rotate X/Y/Z`: The angular rotation to add on the selected axis.

## See Also

* [Animation Graph](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
