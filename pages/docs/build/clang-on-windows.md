# Building with Clang on Windows

You can build ezEngine using the Clang on Windows. This can be useful to find and fix compilation errors and warnings, that do not happen with MSVC. However, as Clang support on Windows is still experimental, you may not be able to build a working executable.

## Using Clang/LLVM with the CMake GUI

1. Get the latest clang windows distribution: <https://releases.llvm.org/download.html> (the 64-bit version is recommended)
1. Create a new solution for the Clang build by pointing *Where to build the binaries* to a new location.
1. Press **Configure** once, a dialog will show up.
1. Choose **Ninja** as the generator. (Note: Get ninja from https://ninja-build.org and put it in your **PATH**)
1. Choose *Specify native compilers* then hit **Finish**.
1. Specify the *C* and *C++* compiler. When using the default paths they are located at:
    * C: C:/Program Files/LLVM/bin/clang.exe
    * C++: C:/Program Files/LLVM/bin/clang++.exe
1. Hit **Finish**
1. You will now get an error from cmake ```No CMAKE_RC_COMPILER could be found```. Check the **Advanced** checkbox to show additional options and point ```CMAKE_RC_COMPILER``` to ```C:\Program Files (x86)\Windows Kits\10\bin\<windows-sdk-version>\x64\rc.exe``` (for example ```C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\rc.exe```).
1. Hit **Configure**
1. Hit **Generate**
1. ```cd``` into the build location and run ```ninja``` to build.

## Using the Clang frontend for Visual Studio with the CMake GUI

The clang frontend for the Visual Studio Compiler is no longer in development. Using the official LLVM clang is recommended.

1. Create a new solution for the Clang build by pointing *Where to build the binaries* to a new location.
1. Press **Configure** once, a dialog will show up.
1. Choose the desired Visual Studio generator at the top.
1. In the field **Optional toolset to use (argument to -T)** type **v140_clang_c2**
1. Finish the dialog and run 'Configure'.
1. Check the **Advanced** checkbox to show additional options.
1. **Disable EZ_USE_PCH**, as the Clang build will not work with precompiled headers.
1. You may also want to **disable EZ_ENABLE_FOLDER_UNITY_FILES** as that makes it easier to see from which file a compilation error originated.
1. Finish the [CMake configuration](cmake-config.md), open the solution in Visual Studio and start compiling.

## See Also


* [Building ezEngine](building-ez.md)
