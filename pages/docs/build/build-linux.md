# Building for Linux

Linux support for ezEngine is currently in development and still to be considered experimental and incomplete. You can try it, but don't expect to be able to work productively with it.

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

* Ubuntu 22, 24, 25, 26
* Linux Mint 21, 22
* Debian 13
* Arch Linux

We welcome contributions to add support for more distributions.

> :warning: If the scripts prints a warning about Qt 6.3.0 or newer not being present in your package manager, you will have to install Qt 6.3.0 or newer manually. See [Installing Qt 6 Manually](#installing-qt-6-manually)

### First-Time Setup

When running the script for the first time, execute:

`./RunCMake.sh --setup`

This detects your distribution and installs all required packages (compiler, Ninja, Qt6, X11/graphics dev headers, etc.) through your package manager, and runs `git submodule update --init` to make sure all submodules are checked out. Add `--force` to auto-confirm any package manager prompts, which is useful for unattended/CI setups.

`--setup` only installs dependencies, it does not configure CMake. Once it finishes, run the script again without `--setup` to actually configure the project.

### Configuring and Building

Which compiler and [build type](building-ez.md#build-types) to use is selected together via the `--target` argument, which picks one of the CMake presets defined in the repository's `CMakePresets.json`:

* `linux-gcc-debug`, `linux-gcc-dev`, `linux-gcc-shipping`
* `linux-clang-debug`, `linux-clang-dev`, `linux-clang-shipping`
* `linux-steam-clang-debug`, `linux-steam-clang-dev`, `linux-steam-clang-shipping` (see [Building with SteamRT Sniper](#building-with-steamrt-sniper-steam-linux-runtime-3))

If `--target` is omitted, `linux-gcc-debug` is used.

```bash
./RunCMake.sh --target linux-clang-dev
```

This configures CMake into `Workspace/<target>`, e.g. `Workspace/linux-clang-dev`. To build, run:

`ninja -C Workspace/linux-clang-dev`

This build command is also given by `RunCMake.sh` as the final output.

If you change any CMake files or add new source files, it is sufficient to run the script again with the same `--target` to reconfigure. This does not check for missing packages again.

`RunCMake.sh` also supports these additional options:

| Option | Explanation |
| --- | --- |
| `--no-unity` | Disables unity builds. This increases compile times but might help certain editors provide better code completion. |
| `--solution-name <name>` | Sets a custom solution name via `EZ_SOLUTION_NAME`. |
| `--workspace-dir <dir>` | Configures into `Workspace/<dir>` instead of `Workspace/<target>`, with matching output directories `Workspace/<dir>-output/{Bin,Lib}`. Useful for keeping several build trees side by side. |

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
* CMake 3.22 or newer
* uuid-dev
* Qt6 (version 6.3 or newer)
* ninja or gnu-make
* libxrandr
* libxinerama
* libxcursor
* libxi
* libfreetype
* libxkbcommon
* mold (or another linker such as lld)
* lttng-ust / lttng-tools
* libtinfo5 (older distributions) or libtinfo6 (newer distributions)
* libomp (only required for Clang)

Once these are installed, configure the project using one of the presets from `CMakePresets.json` directly:

```bash
cmake --preset linux-gcc-dev
ninja -C Workspace/linux-gcc-dev
```

If you need to override individual settings, pass additional `-D` arguments alongside `--preset`:

| Option | Explanation |
| --- | --- |
| `-DEZ_QT_DIR=/path/to/qt6` | Manually specify the path cmake should look for Qt 6 in. |
| `-DEZ_ENABLE_FOLDER_UNITY_FILES=OFF` | Disable unity builds. This increases compile times but might help certain editors to provide better code completion. |
| `-DEZ_SOLUTION_NAME=MyName` | Set a custom solution name. |
| `-DCMAKE_CXX_COMPILER=g++-12` / `-DCMAKE_C_COMPILER=gcc-12` | Override the compiler used by the preset. |

Example usage:

```bash
cmake --preset linux-gcc-dev -DEZ_QT_DIR=/path/to/qt6 -DEZ_ENABLE_FOLDER_UNITY_FILES=OFF
```

## Using Qt Creator

The root of the repository can also be opened in Qt Creator, which will generally do a good job at finding the Qt location on its own.

<!-- TODO: should add something about building and setting the precompiled binaries.
See https://github.com/ezEngine/ezEngine/pull/1152
 -->

## Using CLion

The repository's `CMakePresets.json` already defines all Linux presets, so CLion can configure and build the project directly without going through `RunCMake.sh`.

Before opening the project, make sure the machine actually has the required dependencies available, since CLion does not install them for you:

* The system packages listed under [Manual Setup](#manual-setup) (compiler, Qt6, Ninja, X11/graphics dev headers, ...). The easiest way to get these is to run `./RunCMake.sh --setup` once from a terminal; it installs everything and exits without configuring CMake.
* The git submodules must be checked out, e.g. via `git submodule update --init` (also done by `--setup`).

With those in place, open the repository root in CLion, go to `Build, Execution, Deployment > CMake`, and enable the preset you want to use (e.g. `linux-gcc-debug`). Make sure CMake configure runs through without errors, then select the desired build target in the toolbar and press build.

## Building with SteamRT Sniper (Steam Linux Runtime 3)

SteamRT Sniper (Steam Linux Runtime 3) is Valve's official containerized runtime for building and running Linux games on Steam. Building ezEngine inside the SteamRT Sniper SDK/container ensures maximum compatibility with the Steam client and other games using this environment.

**Why use SteamRT Sniper?**

* Provides a consistent, predictable build and runtime environment for Linux games on Steam.
* Matches the environment used by modern native Linux games and Proton.
* Reduces issues caused by differences between Linux distributions.
* Allows you to build once and run on all Steam-supported Linux distributions, making it ideal for shipping games on Steam.

**How to use:**

1. Download and set up the SteamRT Sniper SDK/container. See the [Steam Runtime 3 'sniper' SDK documentation](https://gitlab.steamos.cloud/steamrt/sniper/sdk/-/blob/steamrt/sniper/README.md) for details.
2. You can also install the runtime via Steam: `steam steam://install/1628350`.
3. Inside the container, configure using the `linux-steam-clang-debug`, `linux-steam-clang-dev`, or `linux-steam-clang-shipping` preset, e.g. `./RunCMake.sh --target linux-steam-clang-dev` or `cmake --preset linux-steam-clang-dev`.
4. If you need to customize SDK paths (e.g. a custom `EZ_STEAMRT_SDK_ROOT`), copy `CMakeUserPresets.json.template` in the repository root to `CMakeUserPresets.json` and adjust it as needed; it defines presets that inherit from the `linux-steam-clang-*` presets above.
5. Build ezEngine inside the container using the usual CMake/Ninja commands. The container provides all required dependencies.

For more information, see the [Valve Steam Runtime repository](https://github.com/ValveSoftware/steam-runtime) and the [SteamRT Sniper SDK documentation](https://gitlab.steamos.cloud/steamrt/sniper/sdk/-/blob/steamrt/sniper/README.md).

## See Also

* [Building ezEngine](building-ez.md)
