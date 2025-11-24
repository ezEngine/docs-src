# Spline Node Component

The *spline node component* is used in conjunction with a [spline component](spline-component.md) to build a spline shape.
It must be attached to a child object of the object where a spline component is present.

The spline node component has no runtime functionality and mainly exists for editing splines, as it provides a shape icon in the editor for node selection, and can be moved around with the standard editing tools. At runtime, the spline component stores all the important data in a more optimized data structure.

> **Important:**
>
> Objects that only contain a *spline node component* are removed from the scene during [scene export](../../editor/run-scene.md). They have no use at runtime and are solely used for editing purposes. Thus in an exported scene you will neither find any spline node components, nor the objects that they were attached to, unless you attach other components or child objects to them.

## Editing Tips

When editing a spline you often need to select the child path nodes and then go back to the spline object. `Ctrl+Q` selects the parent object of the currently selected object, which is very useful here. Also `Ctrl+B` changes to the previous selection, which can also be used to *undo* a selection change.

## Component Properties

* `Roll`: Sets the roll angle at this node, affecting how the up direction is oriented. This is used by components that sample the spline, such as the [follow path component](follow-path-component.md).

* `TangentModeIn`, `TangentModeOut`: The mode for the tangents of the incoming and outgoing spline segments:
  * `Auto`: The curvature at the node is automatically adjusted to be smooth.
  * `Linear`: The spline takes the shortest route in or out of the node. Used to create sharp corners without any curvature.
  * `Custom`: You can manually specify the tangent direction and length.

* `CustomTangentIn`, `CustomTangentOut`: When using *Custom* tangent mode, these specify the tangent vectors. The tangent direction and magnitude affect the curve shape.

* `LinkCustomTangents`: When enabled, the incoming and outgoing tangents are linked so that changing one automatically mirrors the other. This ensures a smooth transition through the node even with custom tangents.

## See Also

* [Spline Component](spline-component.md)
* [Follow Path Component](follow-path-component.md)
