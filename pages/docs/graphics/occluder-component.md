# Occluder Component

The *occluder component* is used to add invisible geometry to a scene that is only used for [occlusion culling](../performance/occlusion-culling.md).

![Occlusion buffer](../performance/media/occlusion-view.jpg)

Currently the occluder component always uses a box shape.

Contrary to [greybox geometry](../scenes/greyboxing.md), the occluder component itself is invisible. Enable [occluder geometry visualization](../performance/occlusion-culling.md#visualizing-occluder-geometry) to see it in action.

Occluders can be moved around dynamically, so you can attach it to a door and it will properly occlude objects when the door closes. You can also (de-)activate the entire component programmatically. For example a breakable wall can use an occluder as long as it is intact, and deactivate it when the wall breaks.

## Component Properties

* `Extents`: The size of the box.

## See Also

* [Occlusion Culling](../performance/occlusion-culling.md)
* [Greyboxing](../scenes/greyboxing.md)
