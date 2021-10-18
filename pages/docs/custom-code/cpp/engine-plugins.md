# Engine Plugins

Engine plugins are the best way to get your custom code into the engine, such that it is accessible by the editor and also [ezPlayer](../../tools/player.md).

Contrary to using a plugin, you could also build your own [application (TODO)](../../runtime/application/application.md), which may link to static libraries that contain your code. However, that approach means that your code cannot be loaded into the editor process and therefore you won't be able to leverage those tools to their full extent. We strongly advise against that.

## Creating a Plugin

The [Sample Game Plugin](../../../samples/sample-game-plugin.md) is a good reference for how to build a custom game plugin. To just create a plugin, at all, you only need very little setup.

The only files you need to look at are:

* `CMakeLists.txt`
* `SampleGamePluginDLL.h`
* `SampleGamePlugin.cpp`

### Build System Setup

The file `CMakeLists.txt` is only of interest here in case you want to reuse the EZ build infrastructure to generate your library. If you use [ezEngine as a Submodule](../../build/submodule.md) then you probably have your own CMake scripts. Either way, you need to add a project that generates a DLL.

### Plugin DLL Name

Make sure to call your plugin DLL `XyzPlugin.dll`. That means it should have the `Plugin` suffix in its name. Generally, plugins can have any name, but only DLLs with this naming convention will be listed by the editor in the [project settings](../../projects/project-settings.md) for you to activate.

### DLL Symbol Import/Export

The file `SampleGamePluginDLL.h` only contains `#define`s for DLL import/export macros.

<!-- BEGIN-DOCS-CODE-SNIPPET: dll-export-defines -->
```cpp
// Configure the DLL Import/Export Define
#if EZ_ENABLED(EZ_COMPILE_ENGINE_AS_DLL)
#  ifdef BUILDSYSTEM_BUILDING_SAMPLEGAMEPLUGIN_LIB
#    define EZ_SAMPLEGAMEPLUGIN_DLL __declspec(dllexport)
#  else
#    define EZ_SAMPLEGAMEPLUGIN_DLL __declspec(dllimport)
#  endif
#else
#  define EZ_SAMPLEGAMEPLUGIN_DLL
#endif
```
<!-- END-DOCS-CODE-SNIPPET -->

If your plugin will be entirely on its own, you don't even need this. However, if you want to use multiple plugins and some of them should contain shared code, then others need to be able to link against the shared libraries and access classes and functions from that library. By tagging classes with these macros you can *export* symbols from a DLL and thus make those things available to other code. For examples how to use this, just search the sample plugin.

### ezPlugin Instance

EZ provides additional hooks for initialization when a plugin gets loaded or unloaded. You can find these in `SampleGamePlugin.cpp`:

<!-- BEGIN-DOCS-CODE-SNIPPET: plugin-setup -->
```cpp
EZ_PLUGIN_ON_LOADED()
{
  // you could do something here, though this is rare
}

EZ_PLUGIN_ON_UNLOADED()
{
  // you could do something here, though this is rare
}
```
<!-- END-DOCS-CODE-SNIPPET -->

These callbacks are optional, though in some cases you may want to register and unregister things here. However, it is way more common to rather use the [startup system](../../runtime/configuration/startup.md) instead.

## Loading a Plugin

If you want to load a plugin from code, you would use `ezPlugin::LoadPlugin()` and provide only the name (no path) of your plugin. Make sure that the DLL is stored in the same directory as all other DLLs and EXEs.

The more convenient way to load your game plugin, though, is to enable it in the [project settings](../../projects/project-settings.md). Then it will be automatically loaded by every [application (TODO)](../../runtime/application/application.md).

## Add Custom Code

Once you have your basic plugin set up and can load it into your project, you can start adding custom code. The easiest way to get started is to write a [custom component](custom-cpp-component.md). Once you need control over higher level game logic, you can add your own [game state](../../runtime/application/game-state.md). And if you need to initialize and shut down certain systems, you should utilize the [startup system](../../runtime/configuration/startup.md).

## Utility Plugins

If you want to write a plugin that provides some functionality for shared access, like some integration of a third-party library, the process is exactly the same. The only difference is, that such libraries would never contain a [game state](../../runtime/application/game-state.md).

Also, have a look at [singletons](../../runtime/configuration/interfaces.md) if your plugin is supposed to provide an implementation of some abstract interface.

## See Also

* [Sample Game Plugin](../../../samples/sample-game-plugin.md)
* [Game States](../../runtime/application/game-state.md)
* [Custom Components with C++](custom-cpp-component.md)
* [Startup System](../../runtime/configuration/startup.md)
* [Singleton Interfaces](../../runtime/configuration/interfaces.md)
