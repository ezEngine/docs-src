# Texture Sample

The **TextureSample** demonstrates the streaming functionality of the resource manager. It does so by creating a custom resource loader, which provides the engine with a sheer endless amount of textures.

Click and move the mouse around to scroll over the grid and thus move the camera to 'unexplored' areas. The resource manager will then stream in the required resources.

![TextureSample](media/texture-sample.jpg)

## Prerequisites

**Note:** The sample is only available when the solution is built with **EZ_BUILD_SAMPLES** activated in CMake.

## Code

The code creates a custom resource loader, which virtualizes reads to a large amount of textures (placed on a grid), by redirecting all reads to the same file on disk.

## See Also

* [Samples](samples-overview.md)
* [Videos](../getting-started/videos.md)