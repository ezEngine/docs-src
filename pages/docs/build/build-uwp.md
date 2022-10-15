# UWP Builds

To generate a solution for building for the Universal Windows Platform (UWP), you need to pass a *toolchain file* to CMake. The file is located in the EZ repository under **Code/BuildSystem/CMake/toolchain-winstore.cmake**.

## Using the CMake GUI

1. Create a new solution for the UWP build by pointing *Where to build the binaries* to a new location.
1. Press **Configure** once, a dialog will show up to choose the generator.
1. Choose the desired Visual Studio generator at the top.
1. Depending on your target device, choose the platform. For instance, for HoloLens 1 select *Win32*.
1. At the bottom select **Specify toolchain file for cross-compiling**.
1. On the next screen set the toolchain file **_PathToEzRepository_/Code/BuildSystem/CMake/toolchain-winstore.cmake**

## Using the command line

Run CMake with this argument: **-DCMAKE_TOOLCHAIN_FILE=_PathToEzRepository_/Code/BuildSystem/CMake/toolchain-winstore.cmake**

## See Also

* [Building ezEngine](building-ez.md)
