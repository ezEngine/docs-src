# Bone Weight Nodes

<!-- PAGE IS TODO -->
<!-- TODO THIS PAGE IS OUTDATED -->

Bone weight nodes are used to generate a weight mask. The mask defines how strongly an animation clip will influence different parts of the skeleton. This is frequently used to apply an animation only to certain parts of a character, for example only the upper or lower body, or even only the left or right arm.

For example it is common to play a walking animation only on the bones below the hip, whereas on the spine and upwards one would want to play an attack animation.

Since animations are often authored for the entire skeleton, it is therefore necessary to mask out unwanted parts.

Bone weights are often in the range of zero to one, with zero meaning that that bone is entirely unaffected by an animation and one means it is fully affected. However, for convenience, weights above one are allowed as well. The system simply normalizes the weights on every bone at the very end. This way, if one animation affects a bone with a weight of one, and another animation affects the same bone with a weight of nine, the first one will only have 10% influence and the second has 90% influence. That makes it easier to layer an important animation on top of a base animation. By simply setting a very large weight (10 or more) an animation can easily override a part of the body, without having to use an inverse mask to filter out the base animation.

> **Important:**
>
> Not all animations will work correctly when they are layered on top of each other. If one animation rotates a bone into one direction, and another animation rotates the same bone very differently, it is possible for the interpolation of the rotations to result in an invalid value. This will manifest as jerking or jumping bones at specific points in the animation. If that happens, you have to use an inverse bone mask to fully filter out the base animation, such that in the end only one of the animations really influences those bones. 

Bone weights are typically connected directly to an animation clip sampling node, and the information that this animation clip shall only influence a part of the skeleton is passed along until it reaches a [combine poses node (TODO)](anim-nodes-combine-poses.md) where the result is baked into one pose. Without such a node in the graph, the bone weights won't have an effect.

## Bone Weight Config Node

This node creates a mask for every bone in the skeleton. By default, the mask is zero for every bone. You then add bones by name to the `RootBones` array. Every bone that is reachable from any of the root bones, will get a weight of one. You can specify multiple root bones, in case that an animation should for example affect both arms, but not the spine and head.

### Node Properties

* **Weight**: The overall weight for the mask. A higher weight means that animation clips that use this weight mask will have stronger influence on the final pose.

* **RootBones**: An array of bone names from where the weight mask should be set to one. Typically this only holds a single entry, for example the hip bone (to affect both legs) or a spine or shoulder bone (to affect the arms and head).
  
### Output Pins

* **Weights**: This represents the full bone mask and can be passed into animation clip sampling nodes, to make them only affect the desired bones.

* **InverseWeights**: If this pin is connected, the node generates the inverse mask as well. So for example, if the node would generate a mask that only affects the head, then the inverse mask will affect everything but the head.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
