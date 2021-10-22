# Procedural Volume Box Component

The *procedural volume box component* defines a box shaped volume in which the rules of [ProcGen graphs](procgen-graph-asset.md) are modified. Not every graph has to make use of this information, and what the exact effect is, is up to the ProcGen graph.

For more details see the chapter on [ProcGen graph modifier nodes (TODO)](procgen-graph-modifiers.md).

## Component Properties

* `Value`: A single number value. This is combined with the *InputValue* from the [modifier node (TODO)](procgen-graph-modifiers.md) in the graph, using the `BlendMode` formula.
* `SortOrder`: If multiple modifier volumes overlap, the `SortOrder` can be used to control in which order the volumes are evaluated.
* `BlendMode`: How to combine `Value` with the *InputValue* from the [modifier node (TODO)](procgen-graph-modifiers.md) in the graph. The *Set* mode just sets the result to `Value` and ignores the other operand.
* `Extents`: The size of the box volume in which the modifier is active.
* `FadeOutStart`: The influence of the volume can fade out towards its edges, for smooth transitions. This value controls for every axis, at what distance from the center point the fade out starts. So if this is set to zero, the fade out starts immediately at the middle (towards the closest edge), whereas if it is set to one, there will be no fade out, at all, and rather the influence of the volume stops abruptly at its border.

## See Also

* [Procedural Object Placement](procedural-object-placement.md)
* [ProcGen Graph Modifier Nodes (TODO)](procgen-graph-modifiers.md)
