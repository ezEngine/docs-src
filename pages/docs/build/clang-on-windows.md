# Building with Clang on Windows

You can build ezEngine using Clang on Windows. This can be useful to find and fix compilation errors and warnings, that do not happen with MSVC. However, as Clang support on Windows is still experimental, you may not be able to build a working executable.

## Using Clang/LLVM with the CMake GUI

### Prerequisites

1. Install [CMake](https://cmake.org/) (or locate `cmake-gui.exe` in the ez repository).
1. Get a recent Clang Windows distribution: <https://releases.llvm.org/download.html> (the 64-bit version is recommended)
    * **Note:** The binary should be called something like `LLVM-<version>-win64.exe`
    * A Windows binary may not be available for the latest version, use an older version, if necessary.
1. Get **ninja** from <https://ninja-build.org> and put it in your `PATH` environment variable.
1. If you had to edit your `PATH` variable, restart your PC.

### Generate a Solution

1. Using `cmake-gui.exe`, create a new solution for a Clang build by pointing *Where to build the binaries* to a new location.
1. Press *Configure* once, a dialog will show up.
1. Choose **Ninja** as the generator.
1. Choose **Specify native compilers** then hit *Finish*.
1. Specify the *C* and *C++* compiler. When using the default paths they are located at:
    * C: `C:/Program Files/LLVM/bin/clang.exe`
    * C++: `C:/Program Files/LLVM/bin/clang++.exe`
1. Click *Finish*
1. If CMake can't find your `ninja.exe` even though it is in your `PATH` set the `CMAKE_MAKE_PROGRAM` manually to point to `ninja.exe` and click *Configure* again.
1. You will now get an error from CMake ```No CMAKE_RC_COMPILER could be found```.
    1. Check the **Advanced** checkbox to show additional options.
    1. Point `CMAKE_RC_COMPILER` to `C:\Program Files (x86)\Windows Kits\10\bin\<windows-sdk-version>\x64\rc.exe` (for example `C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\rc.exe`).
    1. Also set `CMAKE_RC_COMPILER_INIT` to `rc` (if it even shows up).
1. Click *Configure*
1. Click *Generate*
1. Open a Terminal and `cd` into the build location
1. Run `ninja` to build.

## Using the Clang frontend for Visual Studio with the CMake GUI

The clang frontend for the Visual Studio Compiler is no longer in development. Use official LLVM Clang as described above.

## See Also

* [Windows Builds](build-windows.md)
