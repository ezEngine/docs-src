# Linux Builds

## Supported Compilers / Make Systems

The ezEngine CMake scripts support the following compilers when building for Linux:

* GCC
* Clang

C++17 support is required, so make sure that your respective compiler supports it.

The ezEngine CMake scripts support the following two generators when building for Linux:

* Unix Makefiles
* Ninja 

## Prerequisites

You need to install the following libraries:

* CMake 3.20 or newer
* uuid-dev
* SFML-2.5.1
* Qt 5.11 (optional)

A good way to do so is via apt-get on supported distros:

``` cmd
sudo apt-get install -y cmake uuid-dev libx11-dev qtbase5-dev libqt5svg5-dev build-essential
```

If SFML is too old in your distro you can use the following steps to install the required version:

``` cmd
wget https://www.sfml-dev.org/files/SFML-2.5.1-linux-gcc-64-bit.tar.gz
sudo mkdir /usr/SFML
sudo tar xf SFML-2.5.1-linux-gcc-64-bit.tar.gz -C /usr/SFML/
```

If the same is true for your distro's Qt version, you can either use Qt's web installer or use one of the many pre-built Qt package sources, e.g. <https://launchpad.net/~beineri>.

``` cmd
sudo add-apt-repository ppa:beineri/opt-qt-5.11.1-xenial
sudo apt update
sudo apt install qt511-meta-full
```

## Using the command line

If your distribution comes with packages for SFML 2.5 and QT 5 you can directly invoke CMake.
In this example, a `build` folder is created under the root of the repo and CMake is executed in it:

``` cmd
mkdir build
cmake -B build -S .
```

If your package versions are incompatible you have to manually specify them with `CMAKE_PREFIX_PATH`. Pointing it to the dependencies listed above.

``` cmd
mkdir build
cmake -B build -S . -DCMAKE_PREFIX_PATH=/opt/qt511/;/usr/SFML/SFML-2.5.1/lib/cmake/SFML
```

To use a different compiler (like Clang or different versions of GCC) specify `CMAKE_CXX_COMPILER` and `CMAKE_C_COMPILER`.
``` cmd
cmake -B build -S . -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang
```

To disable Qt support (removing the need for Qt completely) use `-DEZ_ENABLE_QT_SUPPORT=OFF`.

To generate Ninja make files use `-G Ninja`.

ezEngine currently builds fully statically linked by default. If you want to build shared libraries instead and make use of ezEngine's dynamic plugin system pass `-DEZ_COMPILE_ENGINE_AS_DLL=ON`

## Using Qt Creator

The root of the repository can also be opened in Qt Creator which will generally do a good job at finding the Qt location on its own but the path to SFML will probably still have to be provided manually.

## See Also

* [Building ezEngine](building-ez.md)
