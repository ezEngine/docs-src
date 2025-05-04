# ezPlayer

The ezPlayer is a stand-alone application that can run any ezEngine game that is properly embedded in its own DLL. The ezEditor can [launch a scene](../editor/run-scene.md) directly in the ezPlayer application. The ezPlayer is meant for testing and as a very slim example of how to write a custom game application.

## Arguments

The Player takes these command line arguments:

```cmd
Player.exe -project "ProjectPath" -scene "ScenePath" [-wnd "optional/path/to/Window.ddl"] [-profile "OptionalAssetProfileName"]
```

With:

* `ProjectPath`: The absolute path to the project directory.
* `ScenePath`: A relative path to a scene file. It is relative to the [data directory](../projects/data-directories.md) that it resides in. If it is a path to an `.ezScene` or `.ezPrefab` file, ezPlayer automatically redirects the path to the corresponding exported `.ezObjectGraph` file in the *AssetCache*.

Typically you only need to pass the path to the project and scene (or prefab) file. The other options are used by the ezEditor to select different configurations.

## Execution

The Player will automatically detect the [projects](../projects/projects-overview.md) directory by searching the file system for an ezProject file. It then executes the core ezEngine functionality, meaning it reads the configuration for the [data directories](../projects/data-directories.md) as well as the [engine plugins](../custom-code/cpp/engine-plugins.md) from the project config files. If the scene requires custom (game) plugins, they must be referenced in those config files.

Then it will execute the regular game loop. Thus, if the scene contains game objects to spawn a character controller or otherwise handle input and move the camera, you will be able to interact with it. If a custom [plugin](../custom-code/cpp/engine-plugins.md) implements a custom [game state](../runtime/application/game-state.md) that will be instantiated and can take full control over the application logic. If no such functionality is available, the Player will instantiate the `ezFallbackGameState` which will spawn a player object, if a `ezPlayerStartPointComponent` is part of the scene. Otherwise it will provide a simple WASD camera movement scheme. If `ezCameraComponent`s are placed in the scene, you can cycle through them using `Page Up` and `Page Down`.

Pressing **Escape** will close the Player application (unless overridden by a custom game state).

## Common Application Features

Since ezPlayer is built on the [application](../runtime/application/application.md) framework, it provides a set of useful features common to all EZ applications.

See [this page](../runtime/application/common-application-features.md) for details.

## See Also

* [Game States](../runtime/application/game-state.md)
* [Engine Plugins](../custom-code/cpp/engine-plugins.md)
* [Projects](../projects/projects-overview.md)
