# Building for MacOS

## Prerequisites

### Supported Compilers

You can compile EZ through one of these methods:

* XCode 5.1.1 or higher (GCC / Clang) 64 Bit
* Makefiles 64 Bit

### Dependencies

You need to install these libraries:

* XQuartz 2.7.5
* SFML-2.5.1
* Qt 5.11 (optional)

A good way to do so is via [homebrew](https://brew.sh/):

``` cmd
brew update
brew install Caskroom/cask/xquartz
brew install qt6
brew install sfml
```

## Using the command line

Run CMake with `CMAKE_PREFIX_PATH` pointing to the dependencies listed above. In this example, a `build` folder is created under the root of the repo and cmake is executed in it:

``` cmd
cmake -DCMAKE_PREFIX_PATH=/usr/local/Cellar/qt/5.13.1/;/usr/local/Cellar/sfml/2.5.1/ -DEZ_ENABLE_QT_SUPPORT=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DEZ_ENABLE_FOLDER_UNITY_FILES=$(unityfiles) -G "Xcode" ../
```

Afterwards the generated solution can be opened in XCode.

## See Also

* [Building ezEngine](building-ez.md)
