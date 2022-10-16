# Supported Platforms

ezEngine is developed primarily on Windows 10/11, using Visual Studio 2022 in 64 Bit builds. As such platform has the largest feature set and is the best tested one.

The code uses C++ 11, 14 and 17 features, but only where broad compiler support is available.

The renderer currently uses DX11 on Windows and a Vulkan implementation is in progress. The editor is currently available on Windows, and being ported to Linux.

On Mac, Android and Linux currently only the base libraries are fully functional. Once the Vulkan renderer is more mature, the goal is to have most features available everywhere.

## List of Supported Platforms

* Windows 10/11 desktop ([details](build-windows.md))
* Windows 10/11 UWP ([details](build-uwp.md))
* OS X 10.9 (Mavericks) ([details](build-macos.md))
* Linux ([details](build-linux.md))
* Android 6.0 Marshmallow (API 23) or newer ([details](build-android.md))

## See Also

* [Building ezEngine](building-ez.md)
