# Supported Platforms

ezEngine is developed primarily on Windows 11, using Visual Studio 2022 in 64 Bit builds. Therefore this platform has the largest feature set and is the best tested one.

The code uses C++ 11, 14 and 17 features, but only where broad compiler support is available.

The renderer currently uses DX11 on Windows and a Vulkan implementation is in progress. The editor is currently available on Windows, and being ported to Linux.

On Mac, Android and Linux only the base libraries are fully functional. Once the Vulkan renderer is more mature, the goal is to have most features available everywhere.

## List of Officially Supported Platforms

* Windows 10/11 desktop ([details](build-windows.md))
* Windows 10/11 UWP ([details](build-uwp.md))
* OS X 10.9 (Mavericks) ([details](build-macos.md))
* Linux ([details](build-linux.md))
* Android 6.0 Marshmallow (API 23) or newer ([details](build-android.md))

## Consoles (Unofficial Ports)

The ezEngine team does not have access to console developer kits and thus cannot provide support for those platforms.

[WDStudios](https://wdstudios.tech) has ported ezEngine to various consoles. If you are a registered developer with Sony, Microsoft or Nintendo, you can contact them to get access to their ports.

Send an e-mail to <contact@wdstudios.tech> with the title `[XBox / PlayStation / Nintendo] Platform Access for ezEngine` to inquire for details. Be aware that this service may not be provided for free.

> **Important:**
>
> The ezEngine project is in no way associated with WDStudios. If you become a paying customer of WDStudios, all contractual obligations are only between you and WDStudios. ezEngine itself is a free and open-source project built by people in their spare-time and the software is provided as-is.

## See Also

* [Building ezEngine](building-ez.md)
