# ProcGen Graph Input Nodes

These node types are available as *inputs* for [ProcGen graph assets](procgen-graph-asset.md).

## Slope Input Node

When an object gets placed at a specific location, the *Slope* node calculates the slope of the terrain at that position and determines whether it is within a desired range. The better it is within the range, the closer the output value is to `1`, and if the slope is outside the desired range, the output value is `0`.

The output value of this node can be passed unchanged as `Density` into the [placement output node](procgen-graph-output-placement.md). In this case the slope directly decides whether an object gets placed or not. It may, however, also be passed into other values, for instance to affect the color of an object.

On the node you select a `MinSlope` and a `MaxSlope` which define the desired range. For example, if the `MinSlope` is set to `0` (flat ground) and the `MaxSlope` is set to `20` (slightly uphill), then objects will only be placed on nearly flat terrain.
If, however, `MinSlope` is set to `30` (steep) and `MaxSlope` is set to `70` (nearly vertical), then objects will only be placed along strong slopes, for example the sides of mountains.

The `LowerFade` and `UpperFade` values determine how quickly the output value fades towards zero when the slope approaches `MinSlope` or `MaxSlope` respectively. With a fade value of zero, the cut off is very abrupt, with a fade value of one, the output value declines earlier, but also more gradually.

### Node Properties

* `MinSlope`, `MaxSlope`: The slope range (in degree) between which the output value is non-zero.
* `LowerFade`, `UpperFade`: How quickly to fade the output value from one towards zero, when the slope approaches the min (lower) or max (upper) value. Fade values of zero mean an abrupt change from one to zero at the boundaries, a value of one means there is always some fade out, except right at the center of the value range.

## Height Input Node

The *Height* node works mostly the same way as the *Slope* node, except that it uses the height (z value) of the potential object position.

The *Height* node determines the z value of the location where an object shall be placed. It then checks whether the value is between `MinHeight` and `MaxHeight`. If not, it outputs the value `0`. Otherwise, it outputs a non-zero value. `LowerFade` and `UpperFade` are used to decide whether, and how much, to fade the output value from `1` towards `0`.

This node can be used to place objects only at specific altitudes, or to change object sizes or colors at higher elevations.

### Node Properties

* `MinHeight`, `MaxHeight`: The height range between which the output value is non-zero.
* `LowerFade`, `UpperFade`:  How quickly to fade the output value from one towards zero, when the height approaches the min (lower) or max (upper) value. Fade values of zero mean an abrupt change from one to zero at the boundaries, a value of one means there is always some fade out, except right at the center of the value range.

## Mesh Vertex Color Input Node

TODO

<!-- PAGE IS TODO -->

## See Also

* [Procedural Object Placement](procedural-object-placement.md)
* [ProcGen Graph Math Nodes](procgen-graph-math.md)
