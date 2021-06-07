# ezEngine as a Submodule

When using git and CMake for a project, ezEngine can be integrated as a submodule into the git repository and reference from CMake.

First ezEngine needs to be added as a submodule to git:

```cmd
git submodule add https://github.com/ezEngine/ezEngine.git
```

Additionally, if you want to use the precompiled tools and the sample content from EZ, you also need to pull in its submodules as well:

```cmd
cd ezEngine
git submodule init
git submodule update
```

Next, add the ezEngine folder in your root `CMakeLists.txt`:

```cmake
# Set the build filter, if you only want to integrate parts of EZ into your build.
# set(EZ_BUILD_FILTER "FoundationOnly")

add_subdirectory(ezEngine)
```

The ezEngine language detection can be reused by including the ezEngine submodule utility file:

```cmake
# include the EZ submodule utility CMake functions
include("ezEngine/Code/BuildSystem/CMake/ezUtilsSubmodule.cmake")

ez_detect_languages()

project("MyProject" LANGUAGES ${EZ_LANGUAGES})
```

For a full example see: [https://github.com/ezEngine/submodule-example](https://github.com/ezEngine/submodule-example)

> **Important:**
>
> This kind of integration is useful, if you want to integrate EZ *code* into your project, for instance, if you want to use ezFoundation as your base library. Since the EZ folder isn't top-level in this setup, using the full engine and all the data located in the [data directories](../projects/data-directories.md) won't work out of the box. For additional options, see the [CMake setup](cmake-config.md) page.

## Strip Unnecessary Code

When integrating EZ this way, you may only want a subset of the available functionality. For instance, you may only need the ezFoundation base library (and 3rd party dependencies). You can achieve this by configuring the [build filter](cmake-config.md#build-filter)

## SDK Root Folder

When integrating EZ as a submodule, it is common for the binaries to be located outside of the ezEngine sub-folder, which means the engine won't be able to find the SDK root folder anymore. See [this article](sdk-root.md) for ways to fix this.

## See Also


* [CMake Setup](cmake-config.md)
