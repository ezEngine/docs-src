# Release Notes August 2020 (20.8)

See the [20.8 milestone](https://github.com/ezEngine/ezEngine/milestone/5?closed=1) for all closed tickets and pull requests.

## Highlights / Major new Features

* [#274](https://github.com/ezEngine/ezEngine/pull/274): Added support for [RmlUi](http://ezengine.net/ui/rmlui.html).
* Wrote over 100 new pages of [documentation](http://ezengine.net).

## Editor

* [#259](https://github.com/ezEngine/ezEngine/pull/259): The editor now uses a dashboard to open projects, and show which samples are available. It also contains links to all the available online resources.
* [#264](https://github.com/ezEngine/ezEngine/pull/264): Added feature to make editing certain component enum properties much easier. For example, [surface interactions](http://ezengine.net/materials/surfaces.html).
* [#253](https://github.com/ezEngine/ezEngine/issues/253): Improved user experience for exporting and running a scene. It's now one button, instead of two, and by default it will ensure all assets are transformed.
* [#228](https://github.com/ezEngine/ezEngine/issues/228): Fixed opening Visual Studio Code, when it was installed not to the user directory.
* [#269](https://github.com/ezEngine/ezEngine/issues/269): Changed asset buttons to not use right-click, but left-click for showing all the options.
* [#220](https://github.com/ezEngine/ezEngine/issues/220): A new release is now automatically detected and the user gets an information popup.
* [#233](https://github.com/ezEngine/ezEngine/issues/233): 'Create Prefab' is now possible even when having multiple objects selected. This restriction has been lifted a while ago, but was still imposed in this workflow.
* [#232](https://github.com/ezEngine/ezEngine/issues/232): 'Create Prefab' now centers the objects within the created prefab.
* [#294](https://github.com/ezEngine/ezEngine/pull/294): Added the ability to align certain visualizers (capsule, box, sphere, ...) at their edges, instead of their centers.
* [#203](https://github.com/ezEngine/ezEngine/issues/203): Fixed incorrect culling of objects after undoing a parenting operation.
* [#262](https://github.com/ezEngine/ezEngine/issues/262): Fixed that creating an asset from an asset button did not work anymore.
* [#263](https://github.com/ezEngine/ezEngine/issues/263): Fixed opening an asset document from the [asset curator](http://ezengine.net/assets/asset-curator.html).
* [#234](https://github.com/ezEngine/ezEngine/issues/234): Fixed 'Convert to Editor Prefab' to work again.
* [#217](https://github.com/ezEngine/ezEngine/issues/217): Fixed that closing an inactive document would change the active document.

## Runtime

* [#284](https://github.com/ezEngine/ezEngine/pull/284), [#279](https://github.com/ezEngine/ezEngine/pull/279): Hashes for strings are now also computed using xxHash instead of MurmurHash, including the ones computed at compile-time.
* [#261](https://github.com/ezEngine/ezEngine/pull/261): ezTasks are now reference counted.
* [#261](https://github.com/ezEngine/ezEngine/pull/261): Added `ezArgSensitive` to be able to censor sensitive user data in certain scenarios.
* [#261](https://github.com/ezEngine/ezEngine/pull/261): Added `ezHashStreamWriter` to compute a hash through for data serialized through a stream.
* [#261](https://github.com/ezEngine/ezEngine/pull/261): Improved quality and size of converted textures.
* [#272](https://github.com/ezEngine/ezEngine/pull/272): Added a rational data type.

## Rendering

* [#235](https://github.com/ezEngine/ezEngine/pull/235): The debug renderer can now be used to render textured triangles.

## Physics

* [#286](https://github.com/ezEngine/ezEngine/pull/286): Added component to grab physical objects.
* [#283](https://github.com/ezEngine/ezEngine/issues/283), [#280](https://github.com/ezEngine/ezEngine/issues/280): Added many features to physics joints, fixed several issues and improved how they can be anchored. Also wrote lots of [documentation](http://ezengine.net/physics/joints/physx-joints.html).
* [#295](https://github.com/ezEngine/ezEngine/pull/295): Refactored the character controllers. Added support for teleporting and move the CC's origin to the capsule bottom.
* [#182](https://github.com/ezEngine/ezEngine/issues/182): Fixed that character controllers would stick to the ceiling when they touched it.
* [#210](https://github.com/ezEngine/ezEngine/issues/210): Fixed that the PVD would crash upon connection, if any joint was in a scene.

## Particle Effects

* [#293](https://github.com/ezEngine/ezEngine/pull/293): Particles are now always aligned with the surface that they are dropped onto.

## Decals

* [#293](https://github.com/ezEngine/ezEngine/pull/293): Decals are now always aligned with the surface that they are dropped onto.

## TypeScript

* [#287](https://github.com/ezEngine/ezEngine/issues/287): Add `GameObject.SendEventMessage()`.

## VR / AR / XR

* [#265](https://github.com/ezEngine/ezEngine/pull/265), [#212](https://github.com/ezEngine/ezEngine/pull/212): Worked on OpenXR support.

## Components

* [#207](https://github.com/ezEngine/ezEngine/issues/207): The [SpawnComponent](http://ezengine.net/gameplay/spawn-component.html) now allows you to set values for the prefab's exposed parameters.

## Tools

* [#261](https://github.com/ezEngine/ezEngine/pull/261): The ArchiveTool can now extract ezArchives that use a non-default file extension.

## Third Party Integrations

* [#288](https://github.com/ezEngine/ezEngine/pull/288): Update Lua to version 5.4.0

## Samples

* Many additions to the [Sample Game Plugin](http://ezengine.net/samples/sample-game-plugin.html) to demonstrate various features.
* Various additions and fixes in the [Testing Chambers](http://ezengine.net/samples/testing-chambers.html) sample, such as an improved character controller and lots of new things in the *Physics* scene to show the various [joint types](http://ezengine.net/physics/joints/physx-joints.html).
* The [RTS Sample](http://ezengine.net/samples/rts.html) now uses the new [Rml UI](http://ezengine.net/ui/rmlui.html).

## Build System

* [#223](https://github.com/ezEngine/ezEngine/issues/223): Added support for detecting Visual Studio 2019 properly.

## Platforms

* [#266](https://github.com/ezEngine/ezEngine/pull/266), [#225](https://github.com/ezEngine/ezEngine/pull/225): Made it possible to build the editor with LLVM/Clang (on Windows).
* [#285](https://github.com/ezEngine/ezEngine/pull/285): Various fixes for building for Android.

## See Also


* [Releases](releases.md)
