# Polishing an Exported Project

A freshly [exported project](project-export.md) runs, but it still behaves like a development build: it launches through [ezPlayer](../tools/player.md), it reacts to all the developer shortcuts, and it shows the default loading screen. This page lists the steps to turn that into something that can be given to players.

## Use a Shipping Build

Most of the development features are compiled out in a *Shipping* build (see [Build Configurations](../build/building-ez.md)). Since the export copies the binaries that the editor itself is running with, you need an editor built in the *Shipping* configuration to export *Shipping* binaries.

Using a *Shipping* build takes care of several things at once:

* The developer keyboard shortcuts are not registered (see below).
* [ezInspector](../tools/inspector.md) support is disabled, so the game doesn't open a network port for it.
* [Tracy](../debugging/tracy.md) is compiled out, so the game doesn't open a network port for that either.

The last two points are the reason why a *Dev* build makes the OS firewall report that the game tried to access the network. In a *Shipping* build no such connection is set up at all.

## Ship Your Own Executable

By default a project is launched with [ezPlayer](../tools/player.md), which is a generic application for running any ez project. To ship a game with its own executable and its own name, use the [C++ project generation](../custom-code/cpp/cpp-project-generation.md). Besides the plugin for your game code, it also sets up an application target named `<PluginName>Game`.

If that executable has been built, project export picks it up automatically:

* The executable is added to the exported binaries, even though the default export filters exclude all EXE files.
* `ezPlayer` is not exported anymore.
* A single launch script for your executable is written, instead of one script per scene.

Most of the startup logic lives in [ezGameState](../runtime/application/game-state.md), so the executable itself stays minimal. Which scene is loaded at startup is decided by `ezGameState::GetStartupOptions()`. The default implementation takes the scene from the `-scene` command line option, which is what ezPlayer is used with. In a game you typically override it to return your main menu scene.

## Write Your Own Game State

`ezFallbackGameState` is meant for development and for tools like ezPlayer, not for a finished game. Among other things it displays a menu for selecting which scene to load, which is opened with the *Windows* key. To be able to use that key, it also disables the OS hotkeys through `ezInputDeviceMouseKeyboard::SetDisableOSHotkeys()`, which means that all *Windows* key shortcuts stop working while the game has focus.

For a game, derive your [game state](../runtime/application/game-state.md) directly from `ezGameState` and implement the functionality that you need. Looking at what `ezFallbackGameState` does is a good starting point.

If you want to keep using `ezFallbackGameState` for the time being, set its `m_bAllowOpenMenu` member to false to disable the scene selection menu.

## Developer Shortcuts

`ezGameState::ConfigureInputActions()` registers the input actions that the application itself handles. In a development build these are all the developer shortcuts, such as *F1* for the [console](../debugging/console.md), *F5* for the [stats](../debugging/stats.md) display and *ESC* to close the application. In a *Shipping* build only the project's own [input configuration](../input/input-config.md) is loaded and none of the developer shortcuts are registered.

If you need a different split than that, override `ezGameState::ConfigureInputActions()` in your game state and call `ezGameApplication::RegisterGameApplicationInputActions()` with exactly the `ezGameApplicationInputFlags` that you want. `ezGameApplicationInputFlags::Regular` is the set without any developer functionality.

Note that the developer shortcuts and the actions of your game are registered in the same input set, so a game that uses, for example, the *ESC* key needs to make sure that the `Dev_EscapeToClose` action isn't registered.

## Customize the Loading Screen

While a scene is loaded in the background, the game displays a loading screen, which by default is an empty world, so all you see is the clear color of the render pipeline.

To replace it, override `ezGameState::CreateLoadingScreenWorld()`. A loading screen is a regular [world](../runtime/world/worlds.md), so it can be loaded from a scene file, but since it has to be ready quickly, it is better to set it up procedurally in code. For a simple full screen image, place a quad mesh in front of the camera and set the desired color and texture on its mesh instance.

## Reduce Stalls at Startup

Two things make the world visibly appear piece by piece after the loading screen:

**Shaders are compiled at runtime.** The first time a shader permutation is used, it is compiled and written to `Output/ShaderCache` next to the exported package. Since the export doesn't include a shader cache, this happens on the machine of every player, during the first launch. As a workaround, run the exported game yourself, play through the parts that you want to be smooth, and then ship the resulting `Output/ShaderCache` folder with your package.

**Assets are loaded on demand.** To load the assets of a scene up front, create an [asset collection](../performance/asset-collections.md) with the same name as the scene. It is then used as the preload collection for that scene and all its assets are loaded while the loading screen is displayed.

## Export Options

The [project export dialog](project-export.md) has options that matter for a final package:

* **Create Launch Scripts** writes the `.bat` files for starting the game. For a package that is distributed to players, these are usually not wanted, since the executable can be started directly.
* The `ProjectBinaries.ezExportFilter` and `ProjectData.ezExportFilter` files in your project folder control which files end up in the package. All DLLs of the SDK are currently exported, whether the project uses them or not, so this is the place to remove the ones that you don't need.

## See Also

* [Project Export](project-export.md)
* [Build Configurations](../build/building-ez.md)
* [Game States](../runtime/application/game-state.md)
* [C++ Project Generation](../custom-code/cpp/cpp-project-generation.md)
* [Asset Collections](../performance/asset-collections.md)
