# Path Component

The *path component* is used to set up path shapes. Other components, such as the [follow path component](follow-path-component.md) can then use the path shape to animate objects or to build geometry.

<video src="media/path-component.webm" width="800" height="600" autoplay loop></video>

## How to Configure a Path

1. Add a [game object](../../runtime/world/game-objects.md) and attach a *path component* to it.
1. Add several game objects as child objects (at least three)
1. Attach a [path node component](path-node-component.md) to each child object.
1. Give each child object a different name. It is easiest to just give them numbers in the order in which you want them to be used in the path.

   ![Path hierarchy config](media/path-hierarchy.png)

1. Add those names in the desired order to the **Nodes** property of the path component.

   ![Path property config](media/path-properties.png)

1. Position the child objects in the world to form a path. Make sure the `Visualize Path` flag is enabled on the path component, so that you can see a preview of the shape.
1. Additionally to the options on the path component itself, you can also edit each node's properties, to adjust the curvature, and whether the path should curl around itself.

## What to do with a Path

A path component by itself has no functionality other than to define a shape. Currently these component types can utilize path shapes:

* [Follow Path Component](follow-path-component.md)

## Component Properties

* `Flags`: Preview flags for the path shape. The *visualize path* flag is enabled by default, once you are done setting up the path, you should disable it.
* `Closed`: Whether the path should loop in on itself or not.
* `Detail`: How detailed the path will be. A finer detail (low value) means there are fewer sharp turns along the curves, but also takes up more memory and time to compute. Unless you notice obvious problems with the path tesselation, this value should stay at its default value.
* `Nodes`: This array needs to reference all nodes by name. If a non-existing name is used, it is ignored.

## See Also

* [Path Node Component](path-node-component.md)
* [Follow Path Component](follow-path-component.md)
