# Building for Android

## Prerequisites

You need the following to build for Android:

* Android SDK Platform 6.0 (Marshmallow) API-Level 23
* Android NDK 21 or higher
* Android SDK Tools
* Android SDK Platform-Tools
* Java (JRE)
* [Ninja](https://ninja-build.org)
* Android Emulator (optional)
* Visual Studio 2019

[Ninja](https://ninja-build.org/) is a build generator used by CMake and needs to be added to the `PATH` environment variable.\
The easiest way to install the Android components is to download [Android Studio](https://developer.android.com/studio) and then to select these from the **SDK Manager**.
Once installed, the following environment variables need to be set:
Change the version to reflect the one you are using.
  
* **ANDROID_NDK_HOME** needs to point to your installed version, by default this is: `C:\Users\[USERNAME]\AppData\Local\Android\Sdk\ndk\[VERSION]`
* **ANDROID_HOME** needs to point to your installed version, by default this is: `C:\Users\[USERNAME]\AppData\Local\Android\Sdk`
* **JAVA_HOME** needs to point to a java runtime. Android Studio has its own version so there is no need to download it separately: `C:\Program Files\Android\Android Studio\jre`

## Visual Studio Open Folder

While you can manually run CMake to use the ninja generator, a more convenient solution is to use Visual Studio's open folder functionality. Go to `File>Open>Folder...` and select the root of the repository. The CMake settings used by this feature are stored inside the `CMakeSettings.json` file in the root folder (`CppProperties.json` contains additional information for VS). Note that if a different API level is used, the **ANDROID_PLATFORM** parameter in the `CMakeSettings.json` has to be changed for all configurations.

If all environment variables were set correctly VS should automatically configure CMake. Once done, a drop down appears in the VS toolbar, allowing you to select the configuration, e.g. `Android-x86-Debug`. Once changed, VS will start to configure CMake again for the new configuration.

Next, select a build target, e.g. `libFoundationTest.so` which are the foundation unit tests. Note that you can only select applications, not all libraries here.

## Setting up an Emulator

Open Android Studio, go to `Configure>AVD Manager` and select `Create Virtual Device`. Download the **Pixel 2 x86** image (or any other compatible one). Next, select **Pie (API 28)** (29 is broken as of writing). In `Advanced Settings` go to `Emulated Performance` and select **Cold boot** as the other options tend to hang and the only option then is to reset the image to factory defaults.

## Debugging Code

Before debugging it should be ensured that you have a emulator setup or a device connected. There should only be one device or emulator. Otherwise debugging is going to fail because it's unknown which target to use.

``` cmd
$ adb devices
List of devices attached
ce11171b5298cc120c      device
```

If adb is not available in the command line `%ANDROID_HOME%\platform-tools` needs to be added to the `PATH` environment variable.

To debug & deploy select one of the launch targets which are prefixed with '>'. These have been configured in the `launch.vs.json` file for debugging. By hitting the "start debugging" button in visual studio, as usual, the app will be installed on the connected device / emulator, started and the debugger will be attached. The app can then be debugged by using the Visual Studio UI the same way as for an windows based C++ project.

## Troubleshooting Debugging / Command Line Debugging

If debugging doesn't work or debugging from the command line is preferred, the command line debugger can be started. It gives detailed output.

The debugging script is located in `Utilities\DbgAndroid.ps1`

The following parameters are present:

| parameter | meaning |
|-----------|---------|
|PrintCmds|Prints all commands that are run. Useful for debugging issues.|
|packageName|The name of the android package. For example "com.ezengine.FoundationTest". All ezEngine package names start with "com.ezengine.". If the package name is not known the .apk file can be opened with a zip tool. Then inspect the AndroidManifest.xml.|
|originalSoDir|The location where the shared object (.so) that contains all the binary code is located: Output\Lib\AndroidNinjaClang(Debug\|RelWithDebInfo\|Release)(arm32\|arm64\|x86\|x64)|
|arch|The architecture of the app you want to debug usually "arm","arm64","x86" or "x86_64"|
|apk|The apk to install on the device before starting debugging. This parameter is optional. If not given no apk will be installed and it is assumed that the apk was already installed on the device|

For example command line debugging the FoundationTest:

``` cmd
Utilities\DbgAndroid.ps1 -packageName "com.ezengine.FoundationTest" -arch arm -apk "Output\Lib\AndroidNinjaClangDebugArm32\FoundationTest.apk" -originalSoDir "Output\Lib\AndroidNinjaClangDebugArm32"
```

## See ezEngine log output

To see the ezEngine log output the following logcat filter can be used.

``` cmd
adb logcat ezEngine:D *:S
```

## See Also

* [Building ezEngine](building-ez.md)
