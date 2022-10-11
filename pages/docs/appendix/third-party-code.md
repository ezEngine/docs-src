# ThirdParty Code and Data

This page lists which third party code and data is used by EZ.

> **Important:**
>
> Before you distribute any project, please check the licensing conditions for all used components. The list below tries to be exhaustive and up-to-date for components directly used by EZ, but this is only provided for your convenience and we give no guarantee for correctness. It is still your responsibility to make absolutely certain that your project doesn't violate any licensing conditions from third-party components used directly or indirectly in your project.

## Assimp

Link: [http://www.assimp.org](http://www.assimp.org)

Compile switch: None (hard dependency for the asset processing)

Open Asset Import Library, a portable Open Source library to import various well-known 3D model formats in a uniform manner.

## cc0Textures

Link: [https://cc0textures.com](https://cc0textures.com)

CC0 Textures offers a library containing hundreds of detailed PBR materials with displacement-, normal- and roughness maps for photorealistic rendering. All assets are available for free and without any restrictions.

## cgbookcase

Link: [https://cgbookcase.com](https://cgbookcase.com)

cgbookcase provides hundreds of high quality, PBR textures. All textures on cgbookcase.com are licensed as CC0.

## Dear Imgui

Link: [https://github.com/ocornut/imgui](https://github.com/ocornut/imgui)

Compile switch: **EZ_3RDPARTY_IMGUI_SUPPORT**

A nice library for easily creating ingame GUIs.

## DirectXTex

Link: [https://github.com/Microsoft/DirectXTex](https://github.com/Microsoft/DirectXTex)

Compile switch: Currently none

Used by ezImage and the ezTexConv tool for GPU-enabled block compression.

## Duktape

Link: [https://duktape.org](https://duktape.org)

Compile switch: **EZ_3RDPARTY_DUKTAPE_SUPPORT**

Duktape is an embeddable Javascript engine, with a focus on portability and compact footprint.
It can be used directly or through ezDuktapeWrapper. Non-essential for the engine, but scripting functionality (using [TypeScript](https://www.typescriptlang.org/)) is built on top of it.

## Enet

Link: [http://enet.bespin.org](http://enet.bespin.org)

Compile switch: **EZ_3RDPARTY_ENET_SUPPORT**

An efficient and easy to use networking library, built on top of the UDP protocol. It is used by ezTelemetry to interact with the ezInspector, and it is also used to implement the file serving functionality.

## FleetOps

Link: [https://www.fleetops.net](https://www.fleetops.net)

Some assets were kindly provided with permission to use and redistribute, by the awesome team behind the FleetOps project. Thanks so much guys!

## FMOD 2.x

Link: [https://www.fmod.com](https://www.fmod.com)

Compile switch: **EZ_BUILD_FMOD**

EZ has an [integration for the FMOD sound system](../sound/fmod-overview.md).

> **Important:**
>
> FMOD is a commercial product and you may need to buy a license to use it in your project.

## FreeSound

Link: [https://freesound.org](https://freesound.org/)

Freesound is a collaborative database of Creative Commons Licensed sounds.

## jc_voronoi

Link: [https://github.com/JCash/voronoi/blob/dev/src/jc_voronoi.h](https://github.com/JCash/voronoi/blob/dev/src/jc_voronoi.h)

Compile switch: None

A fast single file 2D voronoi diagram generator. Used by ezBreakableSheetComponent.

## Kenney.nl

Link: [kenney.nl](https://kenney.nl/)

Kenney provides thousands of textures, 3D models and sound effects under a generous public domain license. Some of them are used in our sample projects.

## Lua

Link: [(http://www.lua.org](http://www.lua.org)

Compile switch: **EZ_3RDPARTY_LUA_SUPPORT**

The Lua scripting language. Can be used directly or through ezLuaWrapper for easier access to common functionality. Non-essential for EZ, only the ingame console interpreter would stop working without it.

## Mikktspace

Link: [http://mmikkelsen3d.blogspot.ie](http://mmikkelsen3d.blogspot.ie)

Compile switch: None (hard dependency for the asset processing)

Tangent space generation code by Morten S. Mikkelsen. See [https://wiki.blender.org/index.php/Dev:Shading/Tangent_Space_Normal_Maps](https://wiki.blender.org/index.php/Dev:Shading/Tangent_Space_Normal_Maps) for more information. It is used by ezGeometry.

## Ozz

Link: [http://guillaumeblanc.github.io/ozz-animation](http://guillaumeblanc.github.io/ozz-animation)

Compile switch: None

Used as the basis for skeletal animations. Both during asset import (to build an optimized skeleton structure) and at runtime for animation playback.

## PhysX 4.1.1

Link: [https://github.com/NVIDIAGameWorks/PhysX](https://github.com/NVIDIAGameWorks/PhysX)

Compile switch: **EZ_BUILD_PHYSX**

NVIDIA PhysX is used to provide collision detection, physics simulation, character controllers and other interactions.

To build PhysX yourself:

1. Checkout **<https://github.com/NVIDIAGameWorks/PhysX.git>**
1. Goto **physx/buildtools/presets/public** and open all presets that you want to build and change or add\
\<cmakeSwitch name="NV_USE_STATIC_WINCRT" value="False" comment="Use the statically linked windows CRT" />\
\<cmakeSwitch name="NV_USE_DEBUG_WINCRT" value="True" comment="Use the debug version of the CRT" />
1. **Run physx/generate_projects.bat** for every configuration you want to build
1. Open **physx/compiler/.../PhysXSDK.sln** and compile **CMakePredefinedTargets/INSTALL** for both debug and release
1. Uwp installs are missing two include folders: **PhysX/include/cudamanager** and **PhysX/include/gpu** so copy those from **physx/include** to **physx/install/.../PhysX/include**
1. The content of the built configuration in **physx/install** is now ready to be consumed by ezEngine by pointing the advanced cmake var **EZ_PHYSX_SDK** to it.

> **Important:**
>
> Depending on how you use PhysX, you may need to acquire (buy) a license for it from NVIDIA.

## Qt 5

Link: [https://www.qt.io](https://www.qt.io)

Compile switch: **EZ_ENABLE_QT_SUPPORT**

Used for all desktop GUI code in the editor and tools.

> **Important:**
>
> Depending on how you use Qt, you may need to acquire (buy) a license for it. See <https://www.qt.io/terms-conditions/>.

## Qt Advanced Docking System

Link [https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System)

Compile switch **EZ_3RDPARTY_ADS_SUPPORT**

A docking system for Qt similiar to the one in visual studio. Used by the editor and inspector applications.

## Recast

Compile switch: **EZ_3RDPARTY_RECAST_SUPPORT**

Link: [https://github.com/recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation)

A library to generate navigation meshes from arbitrary 3D geometry.

## RenderDoc

Link: [https://renderdoc.org](https://renderdoc.org)

Compile switch: **EZ_3RDPARTY_RENDERDOC_SUPPORT**
  
RenderDoc is a free MIT licensed stand-alone graphics debugger. The ezRenderDocPlugin enables full control over taking RenderDoc snapshots from within the engine.

## RmlUi

Link: [https://mikke89.github.io/RmlUiDoc/](https://mikke89.github.io/RmlUiDoc/)

RmlUi is the C++ user interface package based on the HTML and CSS standards, designed as a complete solution for any project's interface needs. It is a fork of the libRocket project, introducing new features, bug fixes, and performance improvements.

## SFML

Link: [http://www.sfml-dev.org](http://www.sfml-dev.org)

Compile switch: **currently none (TODO)**

This library provides a simple and portable interface for window creation, input handling and more. Used by ezWindow and ezStandardInputDevice on non-Windows platforms (Mac, Linux).

## Silk Icons

Link: [http://www.famfamfam.com/lab/icons/silk](http://www.famfamfam.com/lab/icons/silk)

Icons from this set are used by the tools.

## Sonniss

Link: [https://sonniss.com](https://sonniss.com)

Sonniss is a premium distribution platform for high-quality sound effects libraries. Sounds distributed from Sonnis are taken from the GameAudioGDC bundles. See `Data\Content\Sound\FmodProject\Assets\Sonnis\Licensing.pdf` for details.

## stb

Link: [https://github.com/nothings/stb](https://github.com/nothings/stb)

Compile switch: None

Public domain licensed code by Sean Barrett. Used by ezImage to read and write some of the supported formats like PNG and JPEG.

## UTF8-CPP

Link: [https://github.com/nemtrif/utfcpp](https://github.com/nemtrif/utfcpp)

Compile switch: None

A library that provides Unicode related functionality. Integrated directly into ezFoundation.

## V-HACD

Link: [https://github.com/kmammou/v-hacd](https://github.com/kmammou/v-hacd)

Compile switch: **EZ_3RDPARTY_VHACD_SUPPORT**

The "Volumetric Hierarchical Approximate Convex Decomposition" library is used to decompose a concave triangle mesh into multiple convex pieces. This allows you to generate complex [collision meshes](../physics/physx/collision-shapes/physx-collision-meshes.md) which can be used as the shapes of [dynamic PhysX actors](../physics/physx/actors/physx-dynamic-actor-component.md).

## xxHash

Link: [https://github.com/Cyan4973/xxHash](https://github.com/Cyan4973/xxHash)

Compile switch: None

A very fast hash algorithm. Integrated directly into ezFoundation.

## zLib

Link: [http://www.zlib.net](http://www.zlib.net)

Compile switch: **EZ_3RDPARTY_ZLIB_SUPPORT**

Provides algorithms for zip compression and decompression. It is used by ezCompressedStreamReaderZlib and ezCompressedStreamWriterZlib in ezFoundation.

## zstd

Link: [https://facebook.github.io/zstd](https://facebook.github.io/zstd)

Compile switch: **EZ_3RDPARTY_ZSTD_SUPPORT**

A very fast lossless compression library. It is used by ezCompressedStreamReaderZstd and ezCompressedStreamWriterZstd and also by ezArchive.
