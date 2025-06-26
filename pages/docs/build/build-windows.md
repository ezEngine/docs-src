# Building for Windows

This page describes how to build EZ for desktop Windows.

## Prerequisites

This software has to be installed manually.

### Microsoft Visual Studio

[Visual Studio](https://visualstudio.microsoft.com/downloads) is the only supported IDE on Windows. It is sufficient to install the free *Community* edition.

These versions are currently supported:

* Visual Studio 2022 64 Bit

These *workloads* have to be installed:

* *Desktop Development with C++*
* *Game Development with C++*
* *.Net Desktop Development*

You can also use the file [Utilities/VS2022-ezEngine.vsconfig](https://github.com/ezEngine/ezEngine/tree/dev/Utilities/VS2022-ezEngine.vsconfig) to import the necessary configuration into the Visual Studio installer.

## Generate the Solution

### Using the Generate Scripts

In the root folder of the EZ repository you will find a couple of `.bat` files, such as:

* `GenerateWin64vs2022.bat`

Run one of them to generate a Visual Studio solution for your preferred compiler. Afterwards, there will be a **Workspace** folder in the EZ root folder, where you find a `ezEngine_***.sln` file in the respective folder for the Visual Studio version that you chose.

If the script fails, you most likely don't have all the [prerequisites](#prerequisites) installed. They also sometimes fail, if Visual Studio recently installed an update and you haven't rebooted your PC since. Usually when this script fails it is due to common issues with CMake or the MSVC installation. **Read the full error messages carefully** and search the internet, you'll usually find a solution quickly.

### Manually Running CMake (advanced)

This step requires you to install [CMake](https://cmake.org/) yourself.

Run the CMake GUI and [configure the build options](cmake-config.md).

> **Important**
>
> If you are new to EZ, you should **use the generate script**, since it also takes care of some potential pitfalls (e.g. forgetting to update the submodules).

## Building the Code

Open the generated solution with Visual Studio and build everything. Run the **Editor** project afterwards.

## See Also

* [Building ezEngine](building-ez.md)
* [Building with Clang on Windows](clang-on-windows.md)
