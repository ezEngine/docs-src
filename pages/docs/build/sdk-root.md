# SDK Root Folder

When the engine launches, one of the first things it usually does, is to detect the exact path of the *SDK root folder*. This folder is a so called *special directory* and is mostly used when mounting [data directories](../projects/data-directories.md).

*Special directories* are referenced with a ">" at the beginning, and are only allowed in few places, such as when adding data directories. For example, the 'base' data directory is mounted like this:

```cpp
ezFileSystem::AddDataDirectory(">sdk/Data/Base");
```

This adds the folder *"Data/Base"* that is located inside the folder where the SDK (ezEngine) is stored.

## Default Strategy for Locating SDK Root

The default strategy by which the engine detects the SDK root folder, is to start at the location of the application binary, and walk the file structure up, until it finds a folder, which contains the sub-folders "Data/Base".

So for instance, if the running application is located in `C:/ezEngine/Bin/MyGame.exe`, the search will start in `C:/ezEngine/Bin`, where no such folder is found. Then it will continue in `C:/ezEngine`. That folder does have the sub-structure `C:/ezEngine/Data/Base`, so the SDK root is determined to be `C:/ezEngine`.

This strategy works, as long as the application binary is located somewhere inside the ezEngine SDK.

## Redirecting to SDK Root

If you use a different file structure, the default strategy won't work. This is commonly the case when integrating [ezEngine as a Submodule](submodule.md). For example your file structure may look like this:

```cmd
C:/MyRepo
C:/MyRepo/ezEngine-module/ ...
C:/MyRepo/Bin/MyGame.exe
C:/MyRepo/OtherData/ ...
```

Here ezEngine is integrated into another repository. The 'Bin' folder is top level, just as the 'ezEngine-module' folder.

To enable such a pattern, you can place a 'redirection file', which points to the SDK root folder. The file has to be called **ezSdkRoot.txt** and it must be located somewhere along the path that the default strategy searches. In this case it would be put into `C:/MyRepo/ezSdkRoot.txt` and it would contain the string `ezEngine-module`. This way, when the engine searches for the folder that contains 'Data/Base', it will reach `C:/MyRepo`, see the `ezSdkRoot.txt` file, read its content, append the relative path inside to its current path (`C:/MyRepo/ezEngine-module`) and find `C:/MyRepo/ezEngine-module/Data/Base`, which means it determines `C:/MyRepo/ezEngine-module` to be the SDK root folder.

Using a redirection file is the least invasive method and it works for all EZ applications, e.g. the editor, samples and tools.

## Custom SDK Root

You can fully control where the SDK root should be and how it is found, if you write your own [application (TODO)](../runtime/application/application.md). During early startup you can simply set the path of the SDK root folder with `ezFileSystem::SetSdkRootDirectory()`.

This can be preferable when you use a very different structure.

Note that this method will only work for applications that you control. Tools such as [ezInspector](../tools/inspector.md) or the editor expect to find the SDK root through the default search strategy (or through a redirection file).

## When to Redirect At All

The SDK root folder doesn't need to point to the folder where ezEngine is stored. This is only necessary, when you really need the data that is stored in `Data/Base`. If you only use a fraction of EZ, for example only the Foundation library, or not the editor and rendering code, then you can also use a very different folder as your root (for example `C:/MyRepo` in the example above). In such cases your application would almost certainly specify its [custom SDK root](#custom-sdk-root) in its startup code directly.

## See Also

* [ezEngine as a Submodule](submodule.md)
* [CMake Setup](cmake-config.md)
* [Building ezEngine](building-ez.md)
