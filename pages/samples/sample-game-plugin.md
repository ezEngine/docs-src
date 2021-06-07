# Sample Game Plugin

The **SampleGamePlugin** demonstrates the basics of how to build a [custom plugin](../docs/custom-code/custom-code-overview.md) for game code that can run both in a stand-alone application (such as [ezPlayer](../docs/tools/player.md)) as well as inside the editor.

## Prerequisites

> **Note:**
>
> The project is only available when the solution is built with **EZ_BUILD_SAMPLES** activated.

## GameState

The *SampleGameState* class shows how to implement a simple [game state](../docs/runtime/application/game-state.md) that adds high-level game logic, such as handling a game UI. See `ezGameState` and `ezGameApplication` for further details.

## Components

* The `DemoComponent` shows how to modify the transform of an object dynamically.

* The `DebugRenderComponent` shows how to use [debug rendering](../docs/debugging/debug-rendering.md).

For further details also see `ezComponent`.

## Project

Under *Data/Samples/SampleGame* you will find an [editor project](../docs/projects/projects-overview.md) which uses the `SampleGamePlugin`. Note that the project references the plugin as a [runtime plugin](../docs/custom-code/cpp/engine-plugins.md) (under *Editor > [Project Settings](../docs/projects/project-settings.md) > Engine Plugins*). This makes the custom components available to the editor.

When you press 'Play' in the editor, the scene will be simulated and the custom components, such as the `DemoComponent`, will take effect.

When you press 'Play the Game' a full game window is launched and now even the custom [game state](../docs/runtime/application/game-state.md) is instantiated and executed. Consequently, the UI will appear and you can interact with it. Note that this still runs inside the editor process.

You can also [export and run the scene](../docs/editor/run-scene.md) externally in the stand-alone [ezPlayer](../docs/tools/player.md) application.

## See Also

* [Samples](samples-overview.md)
* [Running a Scene](../docs/editor/run-scene.md)
* [Game States](../docs/runtime/application/game-state.md)
* [Custom Code](../docs/custom-code/custom-code-overview.md)
* [Videos](../getting-started/videos.md)
