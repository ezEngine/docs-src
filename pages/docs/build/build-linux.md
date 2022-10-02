# Linux Builds

## Supported Compilers / Make Systems

The ezEngine CMake scripts support the following compilers when building for Linux:

* GCC
* Clang

C++17 support is required, so make sure that your respective compiler supports it.

The ezEngine CMake scripts support the following two generators when building for Linux:

* Unix Makefiles
* Ninja 

## Simple Setup

ezEngine provides a simple `Generate.sh` script which will install all required packages for you and call cmake so you can start building right away.

Currently supported distributions by this script are:
 * Ubuntu 22
 * Linux Mint 21

 PRs to add support for more Distributions to `Generate.sh` are welcome.

### GCC

When running the script the first time execute

`./Generate.sh --setup`

This will install all required packages for your distribution and then generate the make files required to build the `Dev` version of ezEngine.

To build the `Dev` build execute:

`ninja -C build-Dev`

This build command is also given by Generate.sh as the final output.

If you change any cmake files or add new source files it is sufficient to then run:

`./Generate.sh`

This will only invoke cmake without checking for missing packages.

To build a different build type then `Dev` pass the additional `--build-type` argument:

`./Generate.sh --build-type Debug`

### Clang

If you would like to use clang instead of gcc, simply add `--clang` to all invocations of `Generate.sh`

```
./Generate.sh --setup --clang
./Generate.sh --clang
./Generate.sh --build-type Debug --clang
```

## Manual Setup

If you want to setup things manually or your Distribution is not supported by the `Generate.sh` script, you will most likely need all of the following packages:

* C++17 compliant compiler (GCC or Clang)
* CMake 3.20 or newer
* uuid-dev
* Qt5
* ninja or gnu-make
* libxrandr
* libxinerama
* libxcursor
* libxi
* libfreetype

Then invoke cmake with the following arguments

| Option | Explanation |
| -------| ----------- |
| `-B build` | path to the build directory |
| `-S .` | path to the ezEngine root |
| `-G Ninja` | Choose to generate Ninja makefiles. Optional if not provided gnu-make will be used |
| `-DCMAKE_CXX_COMPILER=g++-12` | Specify the C++ compiler to use. Optional, if not provided the system 
default will be used |
| `-DCMAKE_C_COMPILER=gcc-12` | Specify the C compiler to use. Optional, if not provided the system default will be used |
| `-DEZ_EXPERIMENTAL_EDITOR_ON_LINUX=ON` | Build the ezEngine Editor on Linux. This is currently experimental and might contain significant Bugs |
| `-DEZ_BUILD_EXPERIMENTAL_VULKAN=ON` | Build the Vulkan Renderer. This is currently experimental and might contain significant Bugs |
| `-DCMAKE_BUILD_TYPE=Dev` | Specify the build type to use. `Debug`, `Dev` or `Release`. If not provided `Debug` will be used. |
| `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` | Generate a compile_commands.json file to be used for code completion in editors like Visual Studio Code |

Example usage:
```bash
mkdir build
cmake -B build -S . -G Ninja -DCMAKE_CXX_COMPILER=g++-12 -DCMAKE_C_COMPILER=gcc-12 -DEZ_EXPERIMENTAL_EDITOR_ON_LINUX=ON -DEZ_BUILD_EXPERIMENTAL_VULKAN=ON -DCMAKE_BUILD_TYPE=Dev -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

## Using Qt Creator

The root of the repository can also be opened in Qt Creator which will generally do a good job at finding the Qt location on its own.

## See Also

* [Building ezEngine](building-ez.md)
