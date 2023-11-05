# Output Nodes

<!-- PAGE IS TODO -->
<!-- TODO THIS PAGE IS OUTDATED -->

Every [animation graph (TODO)](animation-graph-overview.md) must have exactly one `output` node. Only animation poses that are ultimately connected to an output node will affect the [animated mesh](../animated-mesh-asset.md).

This allows you to quickly deactivate an entire part of the graph simply by removing the connection to the output node. Nodes that are not connected to the output are not evaluated at runtime and therefore don't cost any performance.

## Model Pose Output Node

The `Model Pose Output` node is currently the only available type of output node.

### Input Pins

* **ModelPose**: The one pose to use as the output. This pose has to be in model space. It is thefore quite common that the input is directly connected to a Local To Model Pose node.

* **RotationZ**: This *number value* adds angular [root motion](../root-motion.md) to the final pose. This enables the animation to change the rotation of the [game object](../../../runtime/world/game-objects.md) on which it is played. This is mainly convenient for simpler use cases and for prototyping. In more complex scenarios you may prefer control the object's orientation with [custom code](../../../custom-code/custom-code-overview.md).

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
