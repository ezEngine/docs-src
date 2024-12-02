# Editor Camera

This article describes how to use the editor camera.

## Camera Controls

In the following `LMB` refers to the *left mouse button*, `RMB` to the *right mouse button* and `MMB` to the *middle mouse button*.

### Perspective Views

* `MMB`: Move in the ground plane

* `CTRL + MMB`: Move forwards/backwards and sideways

* `Wheel`: Move forwards/backwards

* `RMB`: Activate fly camera and look around
  * `WASD`: Fly around
  * `Q` and `E`: Fly straight up or down
  * `SHIFT`: Move faster

* `LMB + RMB`: Pan

* `CTRL + Wheel`: Change the camera's movement speed. This can also be changed using the *Camera Speed* slider in the toolbar.

* `C`: Move the camera to the pointed at position

* `F`: *Frame* the currently selected objects
  * Pressing `F` once will only *pan* the camera towards the selected objects
  * Pressing `F` a second time will additionally zoom in on them

* `SHIFT + F`: Same as `F` but frames the object in all [views](../editor/editor-views.md) simultaneously
  * This can also be triggered by double-clicking an item in the *Scenegraph*

* `ALT + LMB`: Orbit around the last *framed* object

* `ALT + RMB`: Dolly (same as move forwards/backwards just with inverted mouse)

* `ALT + MMB`: Pan (inverted)

* Context menu > *Align Camera with Object*: Orients the camera with the selected object

### Orthographic Views

* `RMB`: Pan the selected view

* `Wheel`: Zoom

* `F` and `SHIFT + F`: *Frame object*, same as in perspective view

## Show/Hide Objects

To temporarily focus on certain objects, it is possible to make objects invisible.

* `H`: Hide the selected objects
* `CTRL + H`: Show all hidden objects
* `SHIFT + H`: Hide all objects that are not selected

Note that 'hide unselected' may hide lighting nodes, which can turn your level very dark. You can either activate [ambient lighting](../graphics/lighting/lighting-overview.md) in your scene, or switch the [render mode](../editor/editor-views.md#render-modes) to 'Diffuse Color', if necessary.

The hidden state of objects is not saved in the scene. Also [Play-the-Game](../editor/run-scene.md) mode and [ezPlayer](../tools/player.md) always show all objects. Similarly, the hidden state only excludes objects from rendering, not from simulation.

## Favorite Cameras

You can store up to ten favorite editor camera positions using `CTRL + 0-9`. You can then jump back to that position by pressing the respective number key.

These camera positions are saved per user, per scene. If you open the editor on the same computer at a later time, the camera positions are available again. They are not saved with the project, though, so you cannot share these positions with others. Use [level cameras](#level-cameras) for that.

The favorite camera actions can also be found in the menu *Scene > Favorite Cameras > ...*

## Level Cameras

If you have a *camera component* in your scene, you can assign it a shortcut number in its properties. You can then jump to that location using `ALT + 0-9`. If multiple camera components use the same number, it is undefined to which one the editor camera will move. Moving the editor camera to a camera component does not change the selected object.

You can also create a camera component in the scene at the current editor camera location and assign it a shortcut, by pressing `CTRL + ALT + 0-9`.

Since level cameras are simply objects in the scene, they will be saved in the scene and therefore are shared with others. This can be used both for game play relevant cameras, as well as to just save some useful locations. Camera components that are not actively used for rendering, have no performance impact.

The level camera actions can also be found in the menu *Scene > Favorite Cameras > ...*

## Field of View

The editor camera uses a fixed *field of view* (FOV). The FOV can be changed in the [preferences](../editor/editor-settings.md#preferences).

## Video

[![video](https://img.youtube.com/vi/qDiqRlzafLs/0.jpg)](https://www.youtube.com/watch?v=qDiqRlzafLs)

## See Also


* [Editor Settings](../editor/editor-settings.md)
* [Editing Views](../editor/editor-views.md)
