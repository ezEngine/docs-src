# Editing Gizmos

This page describes the most common tools to interact with objects in a scene.

## Standard Gizmos

The standard gizmos are **Translate** (`W`), **Rotate** (`E`), **Scale** (`R`) and **Drag-To-Position** (`T`). They can be disabled using the `Q` key.

![Gizmos](media/gizmos.jpg)

Click and drag a gizmo to modify the selected objects. The *Drag-To-Position* gizmo moves the selected object to the position that you point at. If you select one of the six handles, instead of its center, it will additionally align the selected axis with the surface normal of what you point at.

The translate and the rotate gizmo may operate either in **local space** (*object space*) or in **global space** (*world space*). You can toggle the space either using the world icon from the toolbar, or by selecting the tool again. For instance, press `W` once to enable the translate gizmo, press `W` again to toggle the space.

### Modifiers

* Hold `SHIFT` while dragging a gizmo to disable snapping.

* Hold `CTRL` before clicking a gizmo to duplicate the object in place. This works for all but the scale gizmo.

### Gizmos in Orthographic Views

When the *Translate*, *Rotate* or *Scale* gizmo is active, holding `LMB` and moving the mouse will modify objects. The perspective of the selected [view](../editor/editor-views.md) (top-down, front, right) determines along which axis the object will be translated or rotated (always in global space). *Scale* will always be uniform.

> **Note:**
>
> The 3D gizmos are not displayed in orthographic views, just left-clicking anywhere in the view will perform the selected action.

## Snap Settings

In the toolbar there are three icons with numbers:

![Snap Toolbar](media/snap-toolbar.png)

These three dropdown menus allow you to quickly select the snap settings for position, rotation and scale. The icon displays the currently selected setting.

Alternatively, you can press `End` to open the snap settings dialog:

![Snap Settings](media/snap-settings.png)

These settings affect not only the gizmos, but also the positioning of [assets](../assets/assets-overview.md) dragged from the [asset browser](../assets/asset-browser.md) into the scene.

> **Tip!**
>
> Use the shortcut `Ctrl+End` to snap the position of the selected objects to the current pivot point. The pivot point is at the location of the last selected object.
>
> You can also snap the position of all selected objects  to the grid individually, using *Edit > Edit Mode > Snap Each Object To Grid*.

## Grid

The grid can be toggled with the `G` key or the grid icon from the toolbar. If enabled, the grid shows up for the *transform gizmo* and in [greyboxing mode](greyboxing.md). For the translate gizmo you can choose in which plane the grid is shown, by clicking one of its quads. Afterwards you can still move along the orthogonal axis by dragging the respective axis handle.

![Grid](media/grid.jpg)

The density of the grid shows the current position snap value. If position snap is disabled, the grid will not show.

## Manipulators

Manipulators are component and property specific gizmos. Properties of a component that can be changed with a manipulator, are highlighted in blue (off) or violet (on). You can click the property label to toggle the manipulator mode. Once a manipulator is enabled, all *Standard Gizmos* are disabled. You can now also use the `Q` key to toggle manipulator mode off and on.

![Manipulator](media/manipulator.jpg)

### Manipulators in Orthographic Views

Most manipulators will not be available in orthographic [views](../editor/editor-views.md).

## Visualizers

Some components use *visualizers* to make some of their aspects more obvious, such as the cone of the spotlight in the image below. These visualizers are only drawn for selected objects and can be toggled using the `V` key. When visualizers are enabled, the editor will also display a yellow [bounding box](selection.md#selection-bounding-box) around each selected object.

![Visualizer and Shape Icon](media/visualizer-shapeicon.jpg)

## Video

[![video](https://img.youtube.com/vi/ua70HBP93co/0.jpg)](https://www.youtube.com/watch?v=ua70HBP93co)

## See Also


* [Selecting Objects](selection.md)
* [Greyboxing](greyboxing.md)
* [Scene Editing](scene-editing.md)
