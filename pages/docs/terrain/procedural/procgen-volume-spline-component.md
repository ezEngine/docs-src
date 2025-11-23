# Procedural Volume Spline Component

The *procedural volume spline component* defines a tube-shaped volume along a [spline](../../animation/paths/path-component.md) in which the rules of [ProcGen graphs](procgen-graph-asset.md) are modified. Not every graph has to make use of this information, and what the exact effect is, is up to the ProcGen graph.

For more details see the chapter on [ProcGen graph modifier nodes](procgen-graph-modifiers.md).

![Spline Modifier](media/procgen-modifier-volume-spline.jpg)

Spline volumes are useful for creating paths, roads, rivers, or other linear features through procedurally generated terrain. The volume follows the spline curve with a configurable radius and falloff.

## Setup

The procedural volume spline component must be on the same game object as a [spline component](../../animation/paths/path-component.md). The spline defines the path that the volume follows, while this component controls the volume's radius, value, and blending properties.

1. Create a game object with a [spline component](../../animation/paths/path-component.md) and configure the spline shape.
2. Add a *Procedural Volume Spline Component* to the same game object.
3. Set the `Radius` to control how wide the influence area is around the spline.
4. Configure the `Value`, `BlendMode`, and other properties as needed.
5. Add the appropriate [tag](../../projects/tags.md) to the game object so that it can be picked up by [modifier nodes](procgen-graph-modifiers.md) in the ProcGen graph.

## Component Properties

* `Value`: A single number value. This is combined with the *InputValue* from the [modifier node](procgen-graph-modifiers.md) in the graph, using the `BlendMode` formula.
* `SortOrder`: If multiple modifier volumes overlap, the `SortOrder` can be used to control in which order the volumes are evaluated.
* `BlendMode`: How to combine `Value` with the *InputValue* from the [modifier node](procgen-graph-modifiers.md) in the graph. The *Set* mode just sets the result to `Value` and ignores the other operand.
* `Radius`: The radius around the spline centerline in which the modifier is active. Points within this distance from the spline curve are affected by the volume.
* `FadeOutStart`: The influence of the volume can fade out towards its edges, for smooth transitions. This value controls where the fade out starts relative to the radius. A value of zero means fade out starts immediately at the spline centerline, while a value of one means no fade out (influence stops abruptly at the radius boundary).

## See Also

* [Spline Component](../../animation/paths/path-component.md)
* [Procedural Object Placement](procedural-object-placement.md)
* [ProcGen Graph Modifier Nodes](procgen-graph-modifiers.md)
* [Procedural Volume Box Component](procgen-volume-box-component.md)
* [Procedural Volume Sphere Component](procgen-volume-sphere-component.md)
