# ezEditorProcessor

*ezEditorProcessor.exe* is the editor without a UI. The editor starts it on its own to [transform assets](../assets/assets-overview.md#asset-transform) in the background - see [Editor Plugins](../editor/editor-plugins.md#ezeditorprocessorexe) for its role in the process structure.

This page is about launching it manually, to automate operations on a project: creating a project, transforming all assets, compiling the [C++ plugin](../custom-code/cpp/cpp-project-generation.md) or [exporting](../shipping/project-export.md) the project. The *GameEngineTests* and the *EditorTests* use it this way.

## Command Line Options

```cmd
ezEditorProcessor.exe -project "C:/dev/MyGame" -transform Default
```

| Option | Description |
|--------|-------------|
| `-project <path>` | The project folder, or the path to its `ezProject` file. |
| `-transform <profile>` | Transforms all assets for the given [asset profile](../assets/asset-profiles.md), e.g. `Default`. |
| `-resave` | Resaves all assets. |
| `-compile` | Generates and compiles the project's C++ plugin. |
| `-recompile` | Like `-compile`, but re-runs CMake and compiles unconditionally. Needed when source files were added, removed or renamed, which `-compile` does not notice. |
| `-export <path>` | [Exports](../shipping/project-export.md) the project into the given absolute directory. The directory is deleted first, an `ExportLog.txt` is written into it. |
| `-outputDir <path>` | Where logs, profiling data and crash dumps are written. |
| `-profiling` | Writes profiling information into the output directory. |

The options of the editor itself work as well. Most relevant are `-createProject`, `-projectTemplate`, `-pluginTemplate` and `-listTemplates`, see [Launching the Editor](../editor/editor-launch.md#creating-a-project).

`ezEditorProcessor.exe -help` prints all options.

Steps are executed in a fixed order within one run: create project, build C++ code, transform, export. So a single call can do everything:

```cmd
ezEditorProcessor.exe -createProject "C:/dev/MyGame" -projectTemplate "Basic FPS" -transform Default
```

If a [C++ plugin](../custom-code/cpp/cpp-project-generation.md) exists, it is always built before assets are transformed or the project is exported, since assets may depend on it. An export does not transform the assets again if `-transform` already did so in the same run.

## Exit Behavior

*ezEditorProcessor* always terminates on its own. Once the requested work is done - or has failed - it shuts the editor down and exits, so it can be waited on from a script without any further handshake.

The one exception is a call that specifies none of the above operations. That is the mode the editor uses for background processing: the process connects back to the host process that started it, waits for assets to transform, and exits when that host is gone. Started by hand, it will fail to connect and exit with code `200`.

The exit code says what happened:

| Code | Meaning |
|------|---------|
| 0 | Success. |
| 1 | The asset profile passed to `-transform` is unknown, or transforming an asset failed. |
| 2 | The project could not be opened. |
| 3 | Generating or compiling the C++ plugin failed. |
| 4 | The export failed. |
| 5 | Creating the project failed. |
| 200 | Started in background mode, but no host process was there to connect to. |

Failures are also written to the log. Since there is no UI, the log is the only place where the details of a failed transform or a compiler error can be found.

## See Also

* [Launching the Editor](../editor/editor-launch.md)
* [Editor Plugins](../editor/editor-plugins.md)
* [Asset Transform](../assets/assets-overview.md#asset-transform)
* [Project Export](../shipping/project-export.md)
