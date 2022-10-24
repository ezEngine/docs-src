# Windows Builds

This page describes how to build EZ for desktop Windows. For UWP builds, see [this page](build-uwp.md).

## Prerequisites

This software has to be installed manually.

### Microsoft Visual Studio

[Visual Studio](https://visualstudio.microsoft.com/downloads) is the only supported IDE on Windows. It is sufficient to install the free *Community* edition.

These versions are currently supported:

* Visual Studio 2019 64 Bit
* Visual Studio 2022 64 Bit

These *workloads* have to be installed:

* *Desktop Development with C++*
* *Game Development with C++*
* *.Net Desktop Development*

### CMake (optional)

[CMake](https://cmake.org/) is used as the build system. On Windows you only need to install CMake if you want to use the CMake GUI to choose custom [CMake configurations](cmake-config.md). If you only use the provided `GenerateXYZ.bat` scripts, those will use a `cmake.exe` that comes with the EZ repository.

## Generate the Solution

### Using the Generate Scripts

In the root folder of the EZ repository you will find a couple of `.bat` files, such as:

* `GenerateWin64vs2019.bat`
* `GenerateWin64vs2022.bat`

Run one of them to generate a Visual Studio solution for your preferred compiler. If these scripts fail, you most likely don't have all the [prerequisites](#prerequisites) installed. They also sometimes fail, if Visual Studio recently installed an update and you haven't rebooted your PC since. Usually when this script fails it is due to common issues with CMake or the MSVC installation. Read the error messages carefully and search the internet, you'll usually find a solution quickly.

Once the script finished successfully, there will be a **Workspace** folder in the EZ root folder. You fill find a `ezEngine_***.sln` file in the respective folder for the Visual Studio version that you chose.

### Manually Running CMake

This step requires that you install [CMake](#cmake-optional) yourself.

Run the CMake GUI and [configure the build options](cmake-config.md).

## Building the Code

Open the generated solution with Visual Studio and build everything.

## See Also

* [Building ezEngine](building-ez.md)
* [Building with Clang on Windows](clang-on-windows.md)
