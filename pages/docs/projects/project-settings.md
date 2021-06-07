# Project Settings

Project settings are options that are configured once and affect the entire application. Most project settings can be configured from the editor, though some (currently) can only be configured by writing certain configuration files manually.

In the editor you will find the project settings under *Editor > Project Settings > ...*.

## Data Directories

*Editor > Project Settings > Data Directories...* opens a dialog to set up the [data directories](data-directories.md).

## Engine Plugins

*Editor > Project Settings > Engine Plugins...* opens a dialog to configure the active [engine plugins](../custom-code/cpp/engine-plugins.md):

![Engine Plugins](media/editor-engine-plugins.png)

This dialog shows all available engine plugins. These are DLLs that are located in the same directory as `Editor.exe`. Note that EZ uses a specific name schema to differentiate which DLLs are considered engine plugins:

* All DLLs named `ezEnginePluginXYZ.dll` are considered to be plugins for the engine, but typically only used in conjunction with another plugin called `ezEditorPluginXYZ.dll`. These are only needed by `EditorEngineProcess.exe` to implement editor specific functionality such as 3D previews of assets. These plugins are **not needed** by the final game application and are not loaded by [ezPlayer](../tools/player.md) when [running an exported scene](../editor/run-scene.md#export-and-run).

* All DLLs named `ezXYZPlugin.dll` are considered to be proper plugins for the engine and implement runtime functionality. When your game uses a feature from one of these plugins, you need to make sure that the corresponding DLL is checked in this list, such that stand-alone applications will load the DLL.

In the list above a number of plugins have a **checkmark**. Also, most plugins are tagged with **(active)**, even if they are not checked:

* **Checked** plugins are the ones that are selected to be loaded by stand-alone applications such as [ezPlayer](../tools/player.md) or your own [application (TODO)](../runtime/application/application.md). These are the plugins that you consciously decided to use in your final game. Consequently you need to ship those DLLs and you can use all the features that they provide.

* **Active** plugins are DLLs that are currently loaded by the engine process. Their functionality is therefore available to you in the editor. As you can see, there are many *active* plugins, although they are not *checked*. This is because plugins can have dependencies on other plugins. The editor automatically loads most [editor plugins (TODO)](../editor/editor-plugins.md), which provide most of the editing functionality, and those will automatically include the necessary engine plugins. Therefore, even though you may not want to use the [Recast integration (TODO)](../ai/recast.md) in your game, the `ezRecastPlugin` is still *active* in the editor, because the `ezEditorPluginRecast` is loaded. This allows you to use the Recast functionality (to generate navmeshes), but if you were to export your game and run it stand-alone, all Recast specific components would be ignored.

If you want to fully remove a certain integration, even in the editor, you need to edit the list of [editor plugins (TODO)](../editor/editor-plugins.md). Then plugin specific asset types will not show up in the [asset browser](../assets/asset-browser.md) and its dedicated [components](../runtime/world/components.md) won't show up in the component list. However, this is a machine wide setting, that applies to all projects and should only be done when a plugin interacts badly with some other functionality.

### Loading Plugins from Code

A custom [application (TODO)](../runtime/application/application.md) or [game state](../runtime/application/game-state.md) can load plugins directly from code if necessary. For example the `ezInspectorPlugin` is automatically loaded for you by stock EZ applications, when building the code for development.

## Input Configuration

*Editor > Project Settings > Input Configuration...* opens a dialog to [configure input actions](../input/input-config.md).

## Tags

*Editor > Project Settings > Tags...* opens a dialog to configure which [tags](tags.md) are available in the project.

## Window Configuration

*Editor > Project Settings > Window Configuration...* opens a dialog to configure the default window configuration when [running a scene](../editor/run-scene.md).

![Window Configuration](media/editor-window-config.png)

These settings allow you to configure basic window settings for Play-the-Game mode and when running an exported scene in [ezPlayer](../tools/player.md). A proper game would typically implement this logic in a custom [application (TODO)](../runtime/application/application.md) and should allow the user to choose settings such as the resolution. The window configuration dialog is mainly for use during development.

There are two separately stored configurations:

**Project Default:** This configuration will be stored in the project folder and thus should be checked into source control to be shared with others.

**User Specific:** This configuration is only stored locally for the active user and not in the project directory. Therefore it cannot be checked into source control. It is meant for users who want to use settings different from the project default. For instance, when you have multiple monitors, you may want the exported scene to always appear on a specific one. This configuration must be enabled to override the default one.

Apart from the window position and size, the window configuration also controls the behavior of the mouse. If **Clip Mouse Cursor** is enabled, the mouse won't be able to leave the window area. This should be preferred for games that hide the mouse and only use relative mouse movement.

## Asset Profiles

*Editor > Project Settings > Asset Profiles...* opens a dialog to edit [asset profiles (TODO)](../assets/asset-profiles.md).

## FMOD

If the [FMOD Integration](../sound/fmod-overview.md) is enabled, *Editor > Project Settings > Fmod Project Settings...* will be available to configure the speaker mode and which master sound bank to use.

## PhysX

If the [PhysX Integration](../physics/physx-overview.md) is enabled, *Editor > Project Settings > PhysX Project Settings...* will be available to configure the [collision layers](../physics/collision-shapes/collision-layers.md).

## Video

[![video](https://img.youtube.com/vi/ivkAIlbK5f0/0.jpg)](https://www.youtube.com/watch?v=ivkAIlbK5f0)

## See Also


* [Projects](projects-overview.md)
