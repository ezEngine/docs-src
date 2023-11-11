# Building for Windows UWP

This page describes how to build EZ for the Universal Windows Platform (UWP). For desktop builds, see [this page](build-windows.md).

Note that only a subset of EZ's functionality is officially maintained and supported on UWP. In general UWP support is not a priority for us.

## Prerequisites

Install the [desktop Windows prerequisites](build-windows.md#prerequisites).

### Microsoft Visual Studio

In Visual Studio, install these additional workloads:

* *Universal Windows Platform Development*

### CMake

[CMake](https://cmake.org/) is used as the build system. For UWP you need to have a custom installation.

## Generate the Solution

To generate a solution for UWP, you need to pass a *toolchain file* to CMake. The file is located in the EZ repository under **Code/BuildSystem/CMake/toolchain-winstore.cmake**.

### Using the CMake GUI

1. Start the CMake GUI application.
1. Create a new solution by pointing *Where to build the binaries* to a new location.
1. Press **Configure** once, a dialog will show up to choose the generator.
1. Choose the desired Visual Studio generator at the top.
1. Depending on your target device, choose the platform. For instance, for HoloLens 1 select *Win32*.
1. At the bottom select **Specify toolchain file for cross-compiling**.
1. On the next screen set the toolchain file ***PathToEzRepository*/Code/BuildSystem/CMake/toolchain-winstore.cmake**

### Using the command line

Run CMake with this argument: **-DCMAKE_TOOLCHAIN_FILE=*PathToEzRepository*/Code/BuildSystem/CMake/toolchain-winstore.cmake**

## Building the Code

Open the generated solution with Visual Studio and build everything.

## See Also

* [Windows Builds](build-windows.md)
