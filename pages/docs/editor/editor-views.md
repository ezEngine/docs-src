# Editing Views

Most documents come with at least one 3D view. The scene documents allow you to switch between single-view and quad-view mode, using the *Toggle Views* button in each view toolbar.

![Quad View](media/quad-view.jpg)

Using the *Perspective* menu in the toolbar (the *eye* icon) you can switch each view to either orthographic or perspective mode.

[Camera controls](../scenes/editor-camera.md) and [editing gizmos](../scenes/gizmos.md) act differently in orthographic and perspective mode.

## Render Modes

Render modes are used to visualize different aspects of the scene. They can be useful for debugging rendering issues, see potential performance hotspots, or easier edit a dark scene.

Most 3D viewports allow you to switch the rendering mode through a drop down menu.

### Default

This mode renders the scene as it would appear in the final game.

![Render Mode](media/render-mode-default.jpg)

### Wireframe

In this mode the scene is rendered only as wireframe. Either monochrome or colored.

![Render Mode](media/render-mode-wireframe-color.jpg)
<!-- ![Render Mode](media/render-mode-wireframe-mono.jpg) -->

### Diffuse Lit Only

This mode visualizes only the diffuse lighting contributions.

![Render Mode](media/render-mode-lit.jpg)

### Specular Lit Only

This mode visualizes only the specular lighting contributions, including reflections.

![Render Mode](media/render-mode-specular-lit.jpg)

### Decal Count

Visualizes how many decals affect each pixel. Yellow and red areas indicate high decal overdraw and will affect performance negatively.

![Render Mode](media/render-mode-decals.jpg)

### Light Count

Visualizes how many lights affect each pixel. Yellow and red areas have many contributing lights and will affect performance negatively.

![Render Mode](media/render-mode-lights.jpg)

### Static vs Dynamic

This mode visualizes which objects in the scene are `static` (green) and which ones are `dynamic` (red). Dynamic objects have a per-frame performance cost, even if they don't move. This mode allows you to find objects that are unnecessarily set to be dynamic.

![Render Mode](media/render-mode-static-dynamic.jpg)

### Texture Coordinates

There are two modes to visualize the UV0 and UV1 texture coordinates.

![Render Mode](media/render-mode-uv0.jpg)

### Normals and Tangents

There are multiple modes to visualize normals and tangents, per-vertex and per-pixel.

![Render Mode](media/render-mode-pixelnormal.jpg)
<!-- ![Render Mode](media/render-mode-vertexnormal.jpg) -->
<!-- ![Render Mode](media/render-mode-vertextangent.jpg) -->

### Diffuse Color

This mode only shows the diffuse color. It can be very handy for editing a scene that is otherwise very dark.

![Render Mode](media/render-mode-color.jpg)

### Diffuse Color Range Check

In `Physically Based Rendering` (PBR) the diffuse color values should never be too dark or too bright, as both will not give the best possible results. This mode visualizes which areas may have non-optimal diffuse colors.

![Render Mode](media/render-mode-colorcheck.jpg)

### Emissive Color

This mode visualizes which objects use emissive colors.

![Render Mode](media/render-mode-emissive.jpg)

### Specular Color

Visualizes the specular color.

![Render Mode](media/render-mode-specular.jpg)

### Ambient Occlusion

This mode shows ambient occlusion values. These come both from dedicated AO maps, as well as screen space ambient occlusion (SSAO).

![Render Mode](media/render-mode-ao.jpg)

### Depth

Visualizes the depth of all objects. Note that depending on the near and far plane settings and the camera distance to the closest object, this mode may appear nearly entirely black or white. For this screenshot the far plane had to be adjusted.

![Render Mode](media/render-mode-depth.jpg)

### Roughness

Visualizes the roughness of objects.

![Render Mode](media/render-mode-roughness.jpg)

## Video

[![video](https://img.youtube.com/vi/2erB3AfSAJ0/0.jpg)](https://www.youtube.com/watch?v=2erB3AfSAJ0)

## See Also


* [Editor Camera](../scenes/editor-camera.md)
* [Scene Editing](../scenes/scene-editing.md)
