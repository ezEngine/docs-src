# Launching the Editor

The ezEditor can be launched simply by running `ezEditor.exe`. By default, it will restore the project that was open during the last session (see [Editor Preferences](editor-preferences.md)).

## Command Line Options

The editor supports the following command line arguments:

| Option | Description |
|--------|-------------|
| `-project <path>` | Opens the editor with the specified project. The path should point to the project's `ezProject` file, or to the folder containing it. |
| `-documents <path> ...` | Documents to open after the project. The paths are relative to a [data directory](../projects/data-directories.md). Only used together with `-project`. |
| `-dashboard` | Opens the editor into the [dashboard](dashboard.md), rather than restoring the last project. |
| `-safe` | Starts the editor in *safe mode*, which disables automatic loading of projects and scenes. This is useful for troubleshooting startup issues. |
| `-unattended` | Tells the editor that no user is present, see [below](#unattended-mode). |
| `-NoSplash` | Disables the splash screen. Can also be disabled permanently in the [editor preferences](editor-preferences.md). |
| `-createProject <path>` | Creates a new project and opens it, see [below](#creating-a-project). |
| `-projectTemplate <name>` | Which project template `-createProject` should use. |
| `-pluginTemplate <name>` | Which plugin template `-createProject` should use. |
| `-listTemplates` | Logs the names that `-projectTemplate` and `-pluginTemplate` accept, then continues. |
| `-editor-mcpport <port>` | The port for the editor's [MCP server](../tools/mcp-server.md), by default `7391`. Only needed to run several editors at once. |

Running `ezEditor.exe -help` prints the full list and then exits.

### Examples

```cmd
ezEditor.exe -project "C:/dev/MyGame/ezProject"
```

```cmd
ezEditor.exe -dashboard
```

```cmd
ezEditor.exe -safe
```

## Creating a Project

A project can also be created from the command line, which is useful in scripts and for automated tests:

```cmd
ezEditor.exe -createProject "C:/dev/MyGame" -projectTemplate "Basic FPS"
```

The path has to be absolute, and the directory must either not exist yet, or be empty. The new project is opened right afterwards.

Without `-projectTemplate`, a blank project is created. In that case `-pluginTemplate` determines which [plugins](../projects/plugin-selection.md) it starts with (`General3D` if not specified). A project template brings its own plugin selection, so the two options are not combined.

`-listTemplates` logs which names are available:

```cmd
ezEditor.exe -listTemplates
```

The same options are understood by *ezEditorProcessor.exe*, which creates the project without opening a UI and then exits. See [ezEditorProcessor](../tools/editor-processor.md).

## Unattended Mode

`-unattended` is meant for editors that are driven by a script or another tool. Modal dialogs are suppressed and the questions they would ask are answered with the option that lets the operation continue, rather than the safest one - a half-started editor is of no use to an automated caller. Notably, the offer to start in safe mode after a crash is declined, since accepting it would prevent the project from being loaded.

Without this option, a dialog that nobody closes blocks the editor indefinitely.

## Windows Taskbar Integration

On Windows, the editor integrates with the taskbar jumplist. Right-click the editor icon in the taskbar to access:

* **Recent Projects** - Quickly open one of your recently used projects.
* **New Window** - Launch a new editor instance without loading a project, showing the dashboard.
* **Start in Safe Mode** - Launch the editor in safe mode.

## See Also

* [Dashboard](dashboard.md)
* [Editor Preferences](editor-preferences.md)
* [Projects](../projects/projects-overview.md)
* [ezEditorProcessor](../tools/editor-processor.md)
* [MCP Server](../tools/mcp-server.md)
