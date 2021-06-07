# Local To Model Pose Node

The `Local To Model Pose` node is used to convert a pose from *local space* to *model space*.

Animation clips store animation data in so called *local space*. That means that every bone stores its transformation (rotation, position and scale) relative to its parent bone. Therefore the actual full position of any given bone is not readily available, but instead has to be computed by concatenating the transformations of all ancestor bones.

Having the data in this representation is advantageous for mixing multiple animations together, which is why this is done in local space. However, to apply a pose to a mesh, the final position and rotation has to be known for every bone. Additionally, operations like inverse kinematics (IK) also have to be done in model space.

Therefore this node is necessary to convert a pose from one representation to the other, before it can be passed to an [output node](anim-nodes-output.md).

## Input Pins

* **LocalPose**: A single pose in local space.

## Output Pins

* **ModelPose**: The converted pose in model space.

## See Also


* [Animation Controller](animation-controller-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
