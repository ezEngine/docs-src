# Launching the Editor

The ezEditor can be launched simply by running `ezEditor.exe`. By default, it will restore the project that was open during the last session (see [Editor Preferences](editor-preferences.md)).

## Command Line Options

The editor supports the following command line arguments:

| Option | Description |
|--------|-------------|
| `-project <path>` | Opens the editor with the specified project. The path should point to the project's `ezProject` file. |
| `-noRecent` | Opens the editor without loading a recent project. Use this to start with a blank editor. |
| `-safe` | Starts the editor in *safe mode*, which disables automatic loading of projects and scenes. This is useful for troubleshooting startup issues. |

### Examples

```cmd
ezEditor.exe -project "C:/dev/MyGame/ezProject"
```

```cmd
ezEditor.exe -noRecent
```

```cmd
ezEditor.exe -safe
```

## Windows Taskbar Integration

On Windows, the editor integrates with the taskbar jumplist. Right-click the editor icon in the taskbar to access:

* **Recent Projects** - Quickly open one of your recently used projects.
* **New Window** - Launch a new editor instance without loading a project.
* **Start in Safe Mode** - Launch the editor in safe mode.

## See Also

* [Dashboard](dashboard.md)
* [Editor Preferences](editor-preferences.md)
* [Projects](../projects/projects-overview.md)
