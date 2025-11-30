# Building ezEngine

To try out ezEngine, you can download a [precompiled binary package](../../getting-started/binaries.md). This article describes how you can build the engine yourself, which enables you to extend the engine with custom functionality.

## Getting the Code and Data

1. Clone a branch from [the GitHub repository](https://github.com/ezEngine/ezEngine).
    * If you need a good git GUI, have a look at [Fork](https://git-fork.com/).
    * Check out the 'dev' branch.
1. Unless your git client already checks out git sub-modules for you, also run `git submodule update --init`in your local clone. The EZ project uses submodules to deliver additional data such as [sample content](https://github.com/ezEngine/content) and [precompiled tools](https://github.com/ezEngine/precompiled-tools).

## Vulkan Rendering

The Vulkan renderer in ezEngine no longer requires installing the Vulkan SDK. All necessary Vulkan dependencies (VMA, SPIRV-Reflect, and Vulkan-Headers) are included in the third-party folder and will be automatically available when building.

The Vulkan SDK is now **optional** and only needed if you want to:

* Use Vulkan validation layers for debugging
* Access Vulkan development tools

The Vulkan loader is dynamically loaded at runtime, so ezEngine will work on systems with or without Vulkan installed.

> **Note for C++ Developers:**
>
> Direct Vulkan C function calls are no longer supported and will cause linker errors. You must use Vulkan-hpp (C++ wrapper) functions instead. The `vulkan.hpp` header is only included in `RendererVulkanDLL.h` with the appropriate defines configured.

## Platform Builds

* [Windows Builds](build-windows.md)
* [Linux Builds](build-linux.md)
* [MacOS Builds](build-macos.md)
* [Android Builds](build-android.md)
* [Building with Clang on Windows](clang-on-windows.md)

## Build Types

EZ sets up three build configuration types:

1. **Debug**
2. **Dev**
3. **Shipping**

While developing your game you should either use a **Debug** or a **Dev** build.

The **Debug** build is best when you want to use a C++ debugger to investigate problems. It includes the necessary *debug symbols* and has many optimizations disabled, which makes it much easier to step through the code. Debug builds are significantly slower than the other build types.

The **Dev** build has most of the optimizations enabled, yet still includes *debug symbols*. The *Dev* build is 3x to 10x faster than a *Debug* build in most cases and is very close to the speed of a *Shipping* build. Stepping through the C++ code with a debugger is possible, though it often behaves erratic due to the optimizations (inlining and such). For most developers the *Dev* build should be the main configuration to use.

The **Shipping** build has all optimizations enabled. It does not include *debug symbols* anymore and it also has all the developer features disabled. That means things like [ezInspector](../tools/inspector.md) won't work here. Similarly, features like *allocation tracking* (for detecting memory leaks) and [profiling features](../performance/profiling.md) are disabled as well.

## Static Linking

On some platforms, such as *Android*, all code needs to be statically linked. In this case some of the automatisms used to load and configure the engine may not work correctly, because the linker optimizes away code that it deems unreferenced.

See the [StaticLinkUtil](../tools/staticlinkutil.md) for how to fix this.

## See Also

* [Supported Platforms](supported-platforms.md)
* [ezEngine as a Submodule](submodule.md)
* [StaticLinkUtil](../tools/staticlinkutil.md)
