# Procedural Placement Component

The *procedural placement component* is used to apply the rules that are defined by a [ProcGen graph asset](procgen-graph-asset.md) within a defined volume of space. The most common use case is to procedurally place vegetation.

The main purpose of the component is to define the region where the procedural rules are to be evaluated. It is not intended to move the volume around at runtime. Rather, the system already automatically takes care of only placing objects in the vicinity of the camera, and delete objects that have are too far away.

## Component Properties

* `Resource`: The [ProcGen graph asset](procgen-graph-asset.md) to use for deciding where to place which type of object.
* `Extents`: The size of the volume in which to evaluate the placement rules. This has to overlap with the terrain geometry where objects shall be placed.

## See Also

* [Procedural Object Placement](procedural-object-placement.md)
* [ProcGen Graph Placement Output](procgen-graph-output-placement.md)
