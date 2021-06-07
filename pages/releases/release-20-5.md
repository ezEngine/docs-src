# Release Notes May 2020 (20.5)

## Editor

* Logged errors and warnings are now displayed in the status bar for a few seconds. A button shows the number of new errors and warnings.
* Added live resource update to color gradient and curve assets
* Action tooltips now show the action shortcut
* Snap object position when pasting
* Marquee selection does not select top-level objects anymore
* Allow to cancel marquee selection with ESC
* Added preference to always enable background asset processing
* Asset processing and background transform is now much more reliable and faster
* Editor objects are not rendered in camera previews anymore
* [#144](https://github.com/ezEngine/ezEngine/issues/144): The editor can now open projects provided by the command line
* [e6b3ecb](https://github.com/ezEngine/ezEngine/commit/e6b3ecb3454ee1deed4ae5f5e239d1d007d4458d): Added Group attribute to allow grouping properties

## Runtime

* Performance improvement for posted messages
* [#173](https://github.com/ezEngine/ezEngine/pull/173): Refactored the task system to fix some issues
* [#163](https://github.com/ezEngine/ezEngine/pull/163): Added `ezSimdVec4u`
* [b3c2507](https://github.com/ezEngine/ezEngine/commit/b3c25075610df3792e6207b3a30312adb9098385): Fixed various issues pointed out by the static code analyzer 'Semmle'
* [658e7c9](https://github.com/ezEngine/ezEngine/commit/658e7c9a42adc3db86980d42ba88d0fca6c3fc8b): ezWorld performance improvements
* [d667255](https://github.com/ezEngine/ezEngine/commit/d66725539d4c389eed235f18b6fb6d1d46ee0e0a): Added support for long file paths on Windows

## Rendering

* [#193](https://github.com/ezEngine/ezEngine/pull/193): Added support for color grading
* Optimized vertex data by using smaller formats for normals, tangents and texcoords

## Particle Effects

* [#188](https://github.com/ezEngine/ezEngine/pull/188) Several fixes for particle effects
* [#189](https://github.com/ezEngine/ezEngine/pull/189) Added particle 'bounds' behavior

## Decals

* [#158](https://github.com/ezEngine/ezEngine/pull/158): Added support for roughness, metallic and occlusion maps

## Components

* PlayerStartPointComponent now exposes the prefab parameters
* The main direction for decals and particle effects is now configurable

## Tools

* [7dcc0c6](https://github.com/ezEngine/ezEngine/commit/7dcc0c6e96c52cc851f4a3818b284e5cc523149a): Added search to the ingame console
* [7c71b8a](https://github.com/ezEngine/ezEngine/commit/7c71b8a5ad29ace802598a4aae4cbf14dd47405c): Added support for ETW profiling

## Third Party Integrations

* Upgraded PhysX to version 4.1.
* [#185](https://github.com/ezEngine/ezEngine/pull/185): Fixed PhysX crashes with high frame rates

## Documentation

* Added [high-level documentation](https://ezengine.github.io/docs/)

## Build System

* [#165](https://github.com/ezEngine/ezEngine/pull/165): ezEngine can now be integrated into other projects as a CMake sub-module

## Platforms

* [ac77380](https://github.com/ezEngine/ezEngine/commit/ac773803db0e9231b99a6fa2e2f756c55bc155e5): Added ability to compile for arm64 from Visual Studio open folder workflow
* [a8f3f4a](https://github.com/ezEngine/ezEngine/commit/a8f3f4acef592f1d0834da5897b2b018316027e5): Added basic support for Android debugging. Note: Android support is limited to low level libraries.
* [34ec12d](https://github.com/ezEngine/ezEngine/commit/34ec12dfbe556c07adf4bfd95aa6820811dae365): Added Android JNI wrappers

## See Also


* [Releases](releases.md)
