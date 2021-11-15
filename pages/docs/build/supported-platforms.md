# Supported Platforms

ezEngine is developed primarily on Windows 10, using Visual Studio 2019, typically in 64 Bit builds. As such this is the best tested and therefore most stable platform. The code uses C++ 11, 14 and 17 features, but only where broad compiler and platform support is available.

## Windows

### Supported Versions

* Windows 10 (Desktop)
* Windows 10 [UWP builds](build-uwp.md)

### Compilers

* Visual Studio 2019 32 Bit
* Visual Studio 2019 64 Bit

## Windows Clang

It is possible to [build with Clang on Windows](clang-on-windows.md) through Visual Studio.

## MacOS

### Supported Versions

* OS X 10.9 (Mavericks)

### Compilers

* Makefiles 64 Bit
* XCode 5.1.1 or higher (GCC / Clang) 64 Bit

### Dependencies

* XQuartz 2.7.5 or higher
* SFML-2.5.1
* Qt 5.11 (optional)

See [MacOS Builds](build-macos.md) for details.

## Linux

### Versions

* Ubuntu 19.4

### Compilers

* GCC 7 64 Bit

### Dependencies

* uuid-dev
* SFML-2.5.1
* Qt 5.11 (optional)

See [Linux Builds](build-linux.md) for details.

## Android

Versions:

* Android 6.0 Marshmallow (API 23) or newer

See [Android Builds](build-android.md) for details.

## See Also

* [Building ezEngine](building-ez.md)
