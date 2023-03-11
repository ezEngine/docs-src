# Path Node Component

The *path node component* is used in conjunction with a [path component](path-component.md) to build a path shape.
It must be attached to a child object of the object where a path component is present.

The path node component has no runtime functionality and mainly exists for editing paths, as it provides a shape icon in the editor for node selection, and can be moved around with the standard editing tools. At runtime, the path component stores all the important data in a more optimized data structure.

> **Important:**
>
> Objects that only contain a *path node component* are removed from the scene during [scene export](../../editor/run-scene.md). They have no use at runtime and are solely used for editing purposed. Thus in an exported scene you will neither find any path node components, nor the objects that they were attached to, unless you attach other components or child objects to them.

## Component Properties

* `Roll`: Sets the roll angle at this node, ie. how much the path curls around its own forward direction here. This doesn't affect the path shape itself, however, components that use the path, such as the [follow path component](follow-path-component.md), may use this information for rotation.
* `Tangent1`, `Tangent2`: The mode for the tangents of the incoming and outgoing path segments:
  * `Auto`: The curvature at the node is automatically adjusted to be smooth.
  * `Linear`: The path takes the shortest route in or out of the node. Used to create sharp corners without any curvature.

## See Also

* [Path Component](path-component.md)
* [Follow Path Component](follow-path-component.md)
