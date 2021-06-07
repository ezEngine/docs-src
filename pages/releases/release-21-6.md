# Release Notes June 2021 (21.6)

The release notes mention the more notable closed tickets and pull requests. See the [21.6 milestone](https://github.com/ezEngine/ezEngine/milestone/6?closed=1) for all closed tickets and pull requests.

## Highlights / Major new Features

This release contains many improvements to existing features, such as the [RmlUi](../docs/ui/rmlui.md) integration. Additionally, with this release EZ finally has a proper [skeletal animation system](../docs/animation/skeletal-animation/skeletal-animation-overview.md). This is just the first version and will be expanded upon in the future.

## Editor

* [#402](https://github.com/ezEngine/ezEngine/pull/402): Added a splashscreen with our new logo.
* [#404](https://github.com/ezEngine/ezEngine/pull/404): The [asset browser](../docs/assets/asset-browser.md) can now show in which other assets an asset is referenced.
* [#401](https://github.com/ezEngine/ezEngine/pull/401): Generalized sky light options across asset documents.
* [#303](https://github.com/ezEngine/ezEngine/issues/303): Improved mesh material assignment workflow.
* [#304](https://github.com/ezEngine/ezEngine/issues/304): Reduced screen space required by asset type filter list.

## Runtime

* [#378](https://github.com/ezEngine/ezEngine/pull/378): Resources can now be created asynchroneously.
* [#373](https://github.com/ezEngine/ezEngine/pull/373), [#315](https://github.com/ezEngine/ezEngine/pull/315): Added support for blackboards.
* [#372](https://github.com/ezEngine/ezEngine/pull/372): Added image data resource + asset
* [#370](https://github.com/ezEngine/ezEngine/pull/370): Added a 'random seed' value to every game object.
* Added support for tracking which input device is in use (controller vs. mouse/keyboard).

## Infrastructure

* [#356](https://github.com/ezEngine/ezEngine/pull/356): Added infrastructure to self-document available command line options.
* [#345](https://github.com/ezEngine/ezEngine/pull/345): Added support for custom variant types.
* [#338](https://github.com/ezEngine/ezEngine/pull/338): Allow using an 'ezSdkRoot.txt' redirection file to point to the SDK dir.
* [#316](https://github.com/ezEngine/ezEngine/pull/316): Added new small array container class.
    
## Rendering

* [#407](https://github.com/ezEngine/ezEngine/pull/407): Added option to modulate fog with sky color.
* [#401](https://github.com/ezEngine/ezEngine/pull/401): Metallic materials can now reflect the skybox.
* [#374](https://github.com/ezEngine/ezEngine/pull/374): Added a basic heightmap terrain component.
* [#358](https://github.com/ezEngine/ezEngine/pull/358): Refactored RendererFoundation to make a Vulkan port easier.
* [#350](https://github.com/ezEngine/ezEngine/pull/350): SPIR-V shader compiler support.
* [#348](https://github.com/ezEngine/ezEngine/pull/348): Early draft of vulkan implementation.

## Physics

* [#330](https://github.com/ezEngine/ezEngine/pull/330): Added option to decompose collision mesh into convex pieces.
* [#301](https://github.com/ezEngine/ezEngine/issues/301): Static collision meshes can now use surfaces from the render mesh.

## VR / AR / XR

* [#365](https://github.com/ezEngine/ezEngine/pull/365): OpenXR Remoting support.
* [#332](https://github.com/ezEngine/ezEngine/pull/332): OpenXR upgrade.

## Tools

* [#389](https://github.com/ezEngine/ezEngine/pull/389): Add support for .vox MagicaVoxel models.
* [#322](https://github.com/ezEngine/ezEngine/pull/322): Rewrote the ModelImporter.

## Third Party Integrations

* [#398](https://github.com/ezEngine/ezEngine/pull/398): Update ZStd to latest, includes the 1.5.0 release which brings speed improvements.
* [#396](https://github.com/ezEngine/ezEngine/pull/396): Updated ads (Advanced Docking System) to version 3.7.1.
* [#394](https://github.com/ezEngine/ezEngine/pull/394): Updated to RmlUi 4.0.
* [#371](https://github.com/ezEngine/ezEngine/pull/371): Significant improvements to the [Kraut](https://github.com/jankrassnigg/Kraut) integration.
* [#362](https://github.com/ezEngine/ezEngine/pull/362): Added RmlUI blackboard binding.
* [#320](https://github.com/ezEngine/ezEngine/pull/320): Updated assimp to latest (5.0.1+).
  
## Samples

* [#403](https://github.com/ezEngine/ezEngine/pull/403): Added demo scene for animations.
* Added a sample scene for terrain and vegetation to the [Testing Chambers](../samples/testing-chambers.md) project.

## See Also


* [Releases](releases.md)
