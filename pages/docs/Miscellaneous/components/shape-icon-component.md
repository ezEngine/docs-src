# Shape Icon Component

The *shape icon component* is automatically attached to new game objects. Its sole purpose is to give empty objects an icon in the 3D viewport, such that it is possible to select them easily.

In some cases you may need an empty game object as an anchor, for example when setting up a [rope](../../effects/ropes/fake-rope-component.md). In such instances, it can be useful to keep the shape icon component. In most other cases it is preferable to remove it, once you attached the desired components to the game object.

> **Note:**
>
> Shape icon components are automatically removed from a scene or prefab during export. In an exported scene, none of these components exist and therefore never take up space of performance in any way.

## See Also

* [Comment Component](comment-component.md)
