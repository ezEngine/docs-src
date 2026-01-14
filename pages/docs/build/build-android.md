# Building for Android

## Prerequisites

You need the following to build for Android:

* Android SDK Platform 10.0 ("Q") API-Level 29
* Android NDK 26.1 or higher (older should work as well, but untested)
* Android SDK Build Tools
* Android SDK Platform-Tools
* Android Emulator (optional)
* Java (JRE)
* Cmake
* Vulkan SDK 1.3.275 or newer
* [Ninja](https://ninja-build.org)
* Powershell 7 (for debugging in VSCode or running convenience scripts)
* Visual Studio 2022 or Linux

[Ninja](https://ninja-build.org/) is a build generator used by CMake and needs to be added to the `PATH` environment variable.

The easiest way to install the Android components is to use the provided installation script from the root of the EZ checkout:

```pwsh
./Utilities/Android/InstallAndroidDependencies.ps1
```

This script downloads and installs the Android SDK, NDK and required tools to a shared workspace directory. Use the `-InstallEmulator` parameter to also install the emulator, or `-AcceptLicenses` to automatically accept licenses (useful for CI environments).

Alternatively, you can download [Android Studio](https://developer.android.com/studio) and select the required components from the **SDK Manager**.

You can also install these via the command line tool located in `C:\Users\[USER]\AppData\Local\Android\Sdk\cmdline-tools\latest\bin`:

```pwsh
# From the root of the EZ checkout, run:
.\Utilities\Android\AndroidEmulator.ps1 -installBuildDependencies
# Or run these manually from the ...\cmdline-tools\latest\bin folder:
./sdkmanager "build-tools;34.0.0"
./sdkmanager "cmdline-tools;latest"
./sdkmanager "ndk;26.1.10909125"
./sdkmanager "platform-tools"
./sdkmanager "platforms;android-29"
# Optional for emulator:
./sdkmanager "emulator"
./sdkmanager "extras;google;Android_Emulator_Hypervisor_Driver"
./sdkmanager "system-images;android-29;google_apis;x86_64"
# Accept licenses for the above
./sdkmanager --licenses
```

Once installed, the following environment variables need to be set:
Change the version to reflect the one you are using.
  
* **ANDROID_NDK_HOME** needs to point to your installed version, by default this is: `C:\Users\[USERNAME]\AppData\Local\Android\Sdk\ndk\[VERSION]`
* **ANDROID_HOME** needs to point to your installed version, by default this is: `C:\Users\[USERNAME]\AppData\Local\Android\Sdk`
* **JAVA_HOME** needs to point to a java runtime. Android Studio has its own version so there is no need to download it separately: `C:\Program Files\Android\Android Studio\jbr`
* **ANDROID_STUDIO** (Optional for debugging). Needs to point to the root of Android Studio, e.g. `C:\Program Files\Android\Android Studio`. We currently rely on the `lldb-server` that ships with Android Studio. Alternatively, you can also debug any app with Android Studio once at which point the required files are on the device and this env var is no longer needed.

## Building with RunCMake.ps1

The simplest way to configure and build for Android is using the `RunCMake.ps1` script in the root of the repository:

```pwsh
# Configure for Android arm64 debug build
./RunCMake.ps1 -target android-arm64-debug

# Configure for Android arm64 release build
./RunCMake.ps1 -target android-arm64-release
```

The script uses CMake presets and handles the configuration automatically. After running the script, you can build with:

```pwsh
cmake --build --preset android-arm64-debug
```

## Compiling Shaders

To compile shaders for Android, use the `CompileShaders.ps1` script:

```pwsh
# On Windows (uses precompiled tools by default)
./Utilities/Android/CompileShaders.ps1

# On Linux (specify the binary directory)
./Utilities/Android/CompileShaders.ps1 -BinDir /path/to/ezEngine/Output/Bin/LinuxClangDev64
```

## Visual Studio / VSCode / CLion

Alternatively, you can use an IDE. CMake's `CMakePresets.json` is already configured for Android arm64 and x64 builds.
* **Visual Studio**: Use Visual Studio's open folder functionality. Go to `File > Open > Folder...` and select the root of the repository. If all environment variables were set correctly VS should automatically configure CMake. Once done, a drop down appears in the VS toolbar, allowing you to select the configuration, e.g. `android-arm64-debug`. Once changed, VS will start to configure CMake again for the new configuration. Next, select a build target, e.g. `libFoundationTest.so` which are the foundation unit tests. Note that you can only select applications, not all libraries here.
* **VSCode**: Make sure you have the `C/C++`, `C/C++ Extension Pack`, `CMake` and `CMake Tools` plugins installed. Select `File > Open Folder...` and select the root of the repository. Execute `CMake: Select Configure Preset` to select the config you wish to use. Make sure CMake runs through without errors. On failure fix any errors and execute  `CMake: Configure` until successful. Finally, execute `CMake: Build Target` to build the project you want.
* **CLion**: Open settings, go to `Build, Execution, Deployment > CMake`, select the profile you wish to use and enable it. Make sure CMake configure runs through without errors. Finally, select the build target of choice in the toolbar and press the build button next to it.

## Setting up an Emulator AVD

You can either use the Android Studio GUI or the command line to setup the emulator. For the command line option, the `avdmanager` is usually located in the `C:\[USERNAME]\admin\AppData\Local\Android\Sdk\cmdline-tools\latest\bin` folder. The following powershell command will create a device that can run EZ generated apks:

```pwsh
# From the root of the EZ checkout, run:
./Utilities/Android/AndroidEmulator.ps1 -installEmulator
# Or run this manually from the ...\cmdline-tools\latest\bin folder:
./avdmanager create avd --force --name "Pixel7" --abi "google_apis/x86_64" --package "system-images;android-29;google_apis;x86_64" --device "pixel_7"
```

## Starting the Emulator

The emulator can be comfortably started from within Android Studio or via the `emulator` application located in `C:\[USERNAME]\admin\AppData\Local\Android\Sdk\emulator` via these powershell commands:

```pwsh
# From the root of the EZ checkout, run:
./Utilities/Android/AndroidEmulator.ps1 -startEmulator
# Or run this manually from the ...\Sdk\emulator folder:
./emulator -avd "Pixel7" -wipe-data -no-snapshot -no-audio -port 5555 -gpu swiftshader_indirect
```

For better performance, the `-gpu host` option can be used but it may cause crashes or graphical artifacts. For more information on the available options, see [the official emulator hardware acceleration](https://developer.android.com/studio/run/emulator-acceleration) page.
The options `-wipe-data -no-snapshot -no-audio` are not strictly necessary but will provide the same environment our unit tests are run under.

To use the GUI instead, open Android Studio, go to `Configure>AVD Manager` and select `Create Virtual Device`. Select the `Pixel 7` hardware profile. Next, select `x86 Images`, then select `Q (API 29), x86_64`. 

> **NOTE:**
> If the emulator hangs on start, go to the AVD's `Advanced Settings` -> `Emulated Performance` and select **Cold boot** or reset the image to factory defaults.

## Debugging Code

You can use Android Studio by using the `Profile or Debug APK` option and selecting your APK. Before you can start debugging, open the `Project Structure...` dialog and make the following changes:
1. Project -> SDK: Select one of the installed Android SDKs.
2. Modules -> Dependencies Tab -> Module SDK: Select one of the installed Android SDKs.
Afterwards, just select your target device and press `Debug`.

If you want to use VSCode instead, you can follow the rest of the guide. Otherwise this section can be skipped.

Before debugging it should be ensured that you have an emulator set up or a device connected. There should only be one device or emulator. Otherwise debugging is going to fail because it's unknown which target to use.

```pwsh
$ adb devices
List of devices attached
ce11171b5298cc120c      device
```

If adb is not available in the command line, `%ANDROID_HOME%\platform-tools` needs to be added to the `PATH` environment variable.

You will need to install the `CodeLLDB` VSCode extension and then create or modify the `.vscode/launch.json` file in your checkout and add a launch config. There are a few examples in the `launch.json` file in the root of the repo.
What you need to change is the following:
1. **PackageName**: This is the package name of the app you want to run, e.g. `com.ezengine.RendererTest`.
1. **apk (optional)**: If set, the app will be installed first before starting. This should point to the output directory of your configuration. E.g. `${workspaceFolder}/Output/Bin/[BUILD_CONFIG]/RendererTest.apk`.
```VSCode
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Android RendererTest",
            "type": "lldb",
            "request": "custom",
            "targetCreateCommands": [
                "shell pwsh \"${workspaceFolder}/Utilities/DbgAndroidLldb.ps1\" -PackageName \"com.ezengine.RendererTest\" -debugTemp \"${workspaceFolder}/debugtemp\" -apk \"${workspaceFolder}/Output/Bin/AndroidNinjaClangDebug64/RendererTest.apk\" -MessageBoxOnError",
                "command source ${workspaceFolder}/debugtemp/lldb.setup"
            ],
            "processCreateCommands": [
                "shell pwsh \"${workspaceFolder}/Utilities/DbgAndroidJdb.ps1\" &",
                "continue"
            ]
        }
    ]
}
```

In VSCode you can now select the debug config from the `Run and Debug` menu and start debugging. Note, if something goes wrong on Windows, a message box will pop up which might not be in the foreground. On Linux, inspect the LLDB log. You can also follow the detailed debugging guide in the FAQ section below.

## See ezEngine log output

To see the ezEngine log output the following logcat filter can be used.

``` cmd
adb logcat ezEngine:D *:S
```

## FAQ

### No debugging visualizers loaded

You need to ensure that the `.lldbinit` in the root of the repo can be loaded. Under Linux, add or change the following line in the home `~/.lldbinit` file:
```sh
settings set target.load-cwd-lldbinit true
```

### VSCode Debugger does not start / command line debugging

If debugging doesn't work or debugging from the command line is preferred, the command line debugger can be started. It gives detailed output.

**Step 1**: The debugging script is located in `Utilities/DbgAndroidLldb.ps1`. To run it manually you will need to run the following in powershell:
```pwsh
./home/[USERNAME]/Code/ezEngine/Utilities/DbgAndroidLldb.ps1 -PackageName "com.ezengine.ShaderExplorer" -debugTemp "/home/[USERNAME]/Code/ezEngine/debugtemp" -apk "/home/[USERNAME]/Code/ezEngine/Output/Bin/AndroidNinjaClangDebugArm64/ShaderExplorer.apk"
```
Of course, adjust the paths so they match your local ezEngine checkout location and Android build config. This will either fail with an error message or should start the apk on your device, showing the wait for debugger prompt.

**Step 2**: Start the `lldb` shell from any LLDB installation of your choosing and run the following commands in the shell:
```sh
command source /home/[USERNAME]/Code/ezEngine/debugtemp/lldb.setup
shell pwsh "/home/[USERNAME]/Code/ezEngine/Utilities/DbgAndroidJdb.ps1" &
continue
```
Run each line at a time. No errors should show up. `command source` is written by `DbgAndroidLldb.ps1` and contains the commands to connect to the device and running process. `DbgAndroidJdb.ps1` connects the java debugger in a fire and forget fashion to close the *Waiting for debugger* prompt on the device. Finally `continue` will start running the paused application.

## See Also

* [Building ezEngine](building-ez.md)
