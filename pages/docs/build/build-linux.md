# Building for Linux

Linux support for ezEngine is currently in development and still to be considered experimental and incomplete. You can try it, but don't expect to be able to work productively with it.

For rendering the new Vulkan backend is used, which itself is also very much in development yet.

We welcome help finding and fixing issues.

## Supported Compilers / Make Systems

The ezEngine CMake scripts support the following compilers when building for Linux:

* GCC
* Clang

C++17 support is required, so make sure that your respective compiler supports it.

These generators are currently supported for Linux:

* Unix Makefiles
* Ninja

## Automatic Setup

The `RunCMake.sh` script in the root folder of ezEngine can be used to automatically install all required packages and run CMake, so that you can start building right away.

This script currently supports these distributions:

* Ubuntu 22
* Linux Mint 21

We welcome contributions to add support for more distributions.

> :warning: If the scripts prints a warning about Qt 6.3.0 or newer not being present in your package manager, you will have to install Qt 6.3.0 or newer manually. See [Installing Qt 6 Manually](#installing-qt-6-manually)

### GCC

When running the script the first time, execute:

`./RunCMake.sh --setup`

This will install all required packages for your distribution and then generate the make files required to build the `Dev` version of ezEngine.

To build the `Dev` build, execute:

`ninja -C build-Dev`

This build command is also given by `RunCMake.sh` as the final output.

If you change any CMake files or add new source files it is sufficient to run:

`./RunCMake.sh`

This only invokes CMake, without checking for missing packages.

To build a different [build type](building-ez.md#build-types) then `Dev`, pass the additional `--build-type` argument:

`./RunCMake.sh --build-type Debug`

### Clang

If you would like to use Clang instead of GCC, simply add `--clang` to all invocations of `RunCMake.sh`:

```bash
./RunCMake.sh --setup --clang
./RunCMake.sh --clang
./RunCMake.sh --build-type Debug --clang
```

### Installing Qt 6 Manually

Some distributions provide quite outdated versions of Qt 6 and the ezEngine Editor requires at least Qt 6.3.0 due to a bug that exists in previous versions of Qt and prevents the 3D viewport in the Editor from working correctly.

You have the following options:

  1. Install through [aqtinstall](https://github.com/miurahr/aqtinstall)
  2. Install Qt 6 through the [official installer](https://doc.qt.io/qt-6/get-and-install-qt.html#using-qt-online-installer)
  3. [Build from source](https://doc.qt.io/qt-6/linux-building.html)

 Once you have obtained a recent version of Qt, you have two options so that the ezEngine cmake scripts find it:

 1) Add the install location permantently to your `PATH` environment variable
 2) Specify the install location when calling `RunCMake.sh` like this:

    ```bash
    > PATH=/path/to/qt6/install:$PATH ./RunCMake.sh
    ```

## Manual Setup

If you want to setup things manually or your distribution is not supported by the `RunCMake.sh` script, you will most likely need all of the following packages:

* C++17 compliant compiler (GCC or Clang)
* CMake 3.20 or newer
* uuid-dev
* Qt6 (version 6.3 or newer)
* ninja or gnu-make
* libxrandr
* libxinerama
* libxcursor
* libxi
* libfreetype
* libtinfo5
* libomp

Then invoke CMake with the following arguments:

| Option                                 | Explanation                                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `-B build`                             | Path to the build directory.                                                                               |
| `-S .`                                 | Path to the ezEngine root.                                                                                 |
| `-G Ninja`                             | Choose to generate Ninja makefiles. Optional, if not provided gnu-make will be used.                       |
| `-DCMAKE_CXX_COMPILER=g++-12`          | Specify the C++ compiler to use. Optional, if not provided the system default will be used.                |
| `-DCMAKE_C_COMPILER=gcc-12`            | Specify the C compiler to use. Optional, if not provided the system default will be used.                  |
| `-DEZ_EXPERIMENTAL_EDITOR_ON_LINUX=ON` | Build the ezEngine editor on Linux. This is currently experimental and might have significant bugs.        |
| `-DEZ_BUILD_EXPERIMENTAL_VULKAN=ON`    | Build the Vulkan renderer. This is currently experimental and might have significant bugs.                 |
| `-DCMAKE_BUILD_TYPE=Dev`               | Specify the [build type](building-ez.md#build-types) to use.                                               |
| `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON`   | Generate a `compile_commands.json` file to be used for code completion in editors like Visual Studio Code. |
| `-DEZ_QT_DIR=/path/to/qt6` | Manually specify the path cmake should look for Qt 6 in. |
| `-DEZ_ENABLE_FOLDER_UNITY_FILES=OFF` | Disable unity builds. This increases compile times but might help certain editors to provide better code completion. |

Example usage:

```bash
mkdir build
cmake -B build -S . -G Ninja -DCMAKE_CXX_COMPILER=g++-12 -DCMAKE_C_COMPILER=gcc-12 -DEZ_EXPERIMENTAL_EDITOR_ON_LINUX=ON -DEZ_BUILD_EXPERIMENTAL_VULKAN=ON -DCMAKE_BUILD_TYPE=Dev -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

## Using Qt Creator

The root of the repository can also be opened in Qt Creator, which will generally do a good job at finding the Qt location on its own.

<!-- TODO: should add something about building and setting the precompiled binaries.
See https://github.com/ezEngine/ezEngine/pull/1152
 -->

## See Also

* [Building ezEngine](building-ez.md)
