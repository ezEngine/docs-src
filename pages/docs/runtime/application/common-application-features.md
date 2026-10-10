# Common Application Features

All applications that are built on top of `ezGameApplication` provide a number of useful features for developers.

The shortcuts below are also listed in the *Engine* menu of the in-game [console](../../debugging/console.md) and can be triggered from there.

## In-game console

**Press F1** to toggle the in-game [console](../../debugging/console.md). See its documentation for further details.

## Reload Resources

**Press F4** to instruct the engine to reload all [resources](../resource-management.md). This can be useful, if for example, you are working on a [shader](../../graphics/shaders/shaders-overview.md) and want to see the result of your changes inside the game, without having to restart the game.

Reloading resources works for all assets that are used directly by the engine (e.g. [Shaders](../../graphics/shaders/shaders-overview.md)). For some assets it will work, after the editor processed the input [assets](../../assets/assets-overview.md). For example for [textures](../../graphics/textures-overview.md) and [materials](../../materials/materials-overview.md) and many others. Some resources, though, are not reloadable, e.g. things that get instantiated at runtime, such as [prefabs](../../prefabs/prefabs-overview.md).

## Show Frames Per Second

**Press F5** to toggle the display of the FPS counter.

## Take a Profiling Capture

**Press F8** to take a capture of the profiling data. See the [profiling](../../performance/profiling.md) documentation for details.

## Open ezInspector

**Press F10** to launch the [ezInspector](../../tools/inspector.md) tool. It is started from the directory of the running application, so it is only available if `ezInspector` was built and deployed next to it.

## Take a RenderDoc Capture

**Press F11** to take a RenderDoc capture. See the [RenderDoc integration](../../debugging/renderdoc.md) documentation for details.

## Take a Screenshot

**Press F12** to take a screenshot. Screenshots are stored in the `appdata` [data directory](../../projects/data-directories.md) (see the [log output](../../debugging/logging.md)). On Windows this can be found by typing `%appdata%` into the Windows Explorer.

## Unattended Runs

All applications built on `ezGameApplication` understand a set of command line options for running them from a script or by an agent, for example as a smoke test, to render reference screenshots, or while being driven through the [MCP server](../../tools/mcp-server.md). These options are only available in development builds, not in shipping builds.

| Option | Description |
|---|---|
| `-unattended` | Runs the application in unattended mode, see below. |
| `-runframes <N>` | Quits after `N` rendered frames. Used to check that a project starts up and renders at all. Implies `-unattended`. |
| `-timeout <seconds>` | Quits after this many seconds, no matter what. A safety net in case startup hangs. Sets the return code to `2` when it triggers. Implies `-unattended`. |
| `-failonerror` | Sets the return code to `1` if any error was logged during the run. Implies `-unattended`. |
| `-screenshot <path>` | Absolute path to a PNG file that a screenshot is written to, right before quitting. Only useful together with `-runframes` or `-timeout`. |
| `-logfile <path>` | Absolute path to a text file that the full log is written to. |
| `-fixedtimestep <N>` | Advances the clock by a fixed `1/N` seconds per frame, instead of the time that really elapsed. The application then no longer runs in real time. |
| `-seed <N>` | Seeds the random number generator of every world that exists at startup. Together with `-fixedtimestep` this makes consecutive runs produce identical frames, which is needed to compare screenshots against reference images. |

In unattended mode:

* A failed assert is logged as an error and ends the process, instead of showing a message box that waits for someone to close it. With a debugger attached, the debugger stops at the assert. Applications that install their own assert handler keep it.
* Input from real hardware, such as mouse, keyboard and controllers, is ignored. Only input devices that generate their input programmatically have an effect, for example the input device of the [MCP server](../../tools/mcp-server.md), as well as values injected through `ezInputManager::InjectInputSlotValue()`.
* The window doesn't take the focus when it opens, and the mouse cursor is neither hidden nor clipped to the window, regardless of what the game requests.

This allows someone to keep working on the same machine while a script or an agent runs the game, without their input interfering with it.

## See Also


* [Application](application.md)
* [ezPlayer](../../tools/player.md)
* [Profiling](../../performance/profiling.md)
* [RenderDoc Integration](../../debugging/renderdoc.md)
