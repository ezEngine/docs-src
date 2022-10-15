# Build Prerequisites

We try to keep the number of prerequisites to build ezEngine as small as possible. However, the following software must be obtained and installed separately:

## C++ Compiler

To build the source, you have to have a supported C++ compiler installed. See the [supported platforms](supported-platforms.md) page for which compilers are supported on which platform.

## C# Compiler (optional)

If you want to build everything (including the unit tests) on Windows, you also need to have C# installed as a workload in Visual Studio.

## CMake (optional)

[CMake](https://cmake.org/) is used as the build system. Version 3.20 or newer is required.

On Windows, if you run the generate scripts from the root level, it will use a `cmake.exe` that comes with the EZ repository. If you want more control over this step, you can run CMake manually, in which case the CMake GUI is very handy. You will have to install that yourself.

## See Also

* [CMake Configuration](cmake-config.md)
