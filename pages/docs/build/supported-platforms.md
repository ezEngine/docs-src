# Supported Platforms

ezEngine is developed primarily on Windows 11, using Visual Studio 2022 and 2026 in 64 Bit builds. Therefore this platform has the largest feature set and is the best tested one.

The code uses C++ 11, 14 and 17 features, but only where broad compiler support is available.

On Windows, both the D3D11 and Vulkan renderers are built by default, with D3D11 used by default. Pass `-renderer Vulkan` on the command line to use the Vulkan renderer instead. The editor is currently available on Windows, and being ported to Linux.

On Mac, Android and Linux only the base libraries are fully functional. Once the Vulkan renderer is more mature, the goal is to have most features available everywhere.

## Hardware Requirements

* A 64 Bit CPU. There are no 32 Bit builds.
* A GPU with support for either Direct3D 11 or Vulkan 1.1. The Direct3D renderer falls back to lower feature levels if necessary, but not all rendering features work then.

To build C++ code, whether the engine itself or just a [game plugin](../custom-code/cpp/cpp-overview.md), a supported compiler has to be installed. See the platform specific pages below for details.

## List of Officially Supported Platforms

* Windows 10/11 ([details](build-windows.md))
* Linux ([details](build-linux.md))
* Android 10 (API level 29) or newer ([details](build-android.md))
* macOS 11 (Big Sur) or newer, on Intel and Apple Silicon ([details](build-macos.md))

## Consoles (Unofficial Ports)

The ezEngine team does not have access to console developer kits and thus cannot provide support for those platforms.

[WDStudios](https://wdstudios.tech) has ported ezEngine to various consoles. If you are a registered developer with Sony, Microsoft or Nintendo, you can contact them to get access to their ports.

Send an e-mail to <contact@wdstudios.tech> with the title `[XBox / PlayStation / Nintendo] Platform Access for ezEngine` to inquire for details. Be aware that this service may not be provided for free.

> **Important:**
>
> The ezEngine project is in no way associated with WDStudios. If you become a paying customer of WDStudios, all contractual obligations are only between you and WDStudios. ezEngine itself is a free and open-source project built by people in their spare-time and the software is provided as-is.

## See Also

* [Building ezEngine](building-ez.md)
