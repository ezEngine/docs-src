# Common Application Features

All applications that are built on top of `ezGameApplication` provide a number of useful features for developers.

## In-game console

**Press F1** to toggle the in-game [console](../../debugging/console.md). See its documentation for further details.

## Reload Resources

**Press F4** to instruct the engine to reload all [resources (TODO)](../resource-management.md). This can be useful, if for example, you are working on a [shader](../../graphics/shaders/shaders-overview.md) and want to see the result of your changes inside the game, without having to restart the game.

Reloading resources works for all assets that are used directly by the engine (e.g. [Shaders](../../graphics/shaders/shaders-overview.md)). For some assets it will work, after the editor processed the input [assets](../../assets/assets-overview.md). For example for [textures](../../graphics/textures-overview.md) and [materials](../../materials/materials-overview.md) and many others. Some resources, though, are not reloadable, e.g. things that get instantiated at runtime, such as [prefabs](../../prefabs/prefabs-overview.md).

## Show Frames Per Second

**Press F5** to toggle the display of the FPS counter.

## Take a Profiling Capture

**Press F8** to take a capture of the profiling data. See the [profiling](../../performance/profiling.md) documentation for details.

## Take a RenderDoc Capture

**Press F11** to take a RenderDoc capture. See the [RenderDoc integration](../../debugging/renderdoc.md) documentation for details.

## Take a Screenshot

**Press F12** to take a screenshot. Screenshots are stored in the `appdata` [data directory](../../projects/data-directories.md) (see the [log output](../../debugging/logging.md)). On Windows this can be found by typing `%appdata%` into the Windows Explorer.

## See Also


* [Application](application.md)
* [ezPlayer](../../tools/player.md)
* [Profiling](../../performance/profiling.md)
* [RenderDoc Integration](../../debugging/renderdoc.md)
