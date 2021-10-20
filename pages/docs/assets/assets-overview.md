# Assets

*Assets* are the most common type of [documents](../editor/editor-documents.md) in the editor. Assets represent data that usually comes from some source file (like an image or a model) and must be processed into an optimized format for the engine to use at runtime.

This processing step is called **asset transformation**. A good example are [textures](../graphics/textures-overview.md). Textures come in many different source formats, such as TGA, JPG, PNG, and so on. Texture data in these formats is not suited to be loaded directly by the engine. Instead, it must be encoded and compressed in formats that GPUs can decode efficiently. This step can be very time consuming and should therefore be done up front. Additionally, textures should contain mipmaps and may need to be downscaled for different platforms. Exactly how a texture should be transformed is something that you may want to have full control over, so you need some way to configure this.

Therefore, instead of loading a texture directly into the engine, you need to create a texture asset in the editor. This document will reference one or multiple source files and allow you to configure the asset transform. When the asset gets *transformed* it will output an optimized file that the engine can then load and use efficiently.

## Types of Assets

One can distinguish between two types of assets: Assets that mostly exist to transform existing data from a source format into an optimized format, and assets that represent entirely new data, authored in the editor.

Examples for the former are [textures](../graphics/textures-overview.md), [meshes](../graphics/meshes/mesh-asset.md), [collision meshes](../physics/collision-shapes/collision-meshes.md), [sounds](../sound/sound-overview.md) and so on. Their purpose is to ensure that the engine does not need to handle all sorts of source formats, but only optimized runtime formats. Instead, the editor and other tools will deal with the source formats, and allow the user to configure this conversion step.

Examples for the latter are [scenes](../scenes/scene-editing.md), [prefabs](../prefabs/prefabs-overview.md), [materials](../materials/materials-overview.md), [property animations (TODO)](../animation/property-animation/property-animation-overview.md), [curves](../animation/common/curves.md) and so on. Their data does not come from some other file on disk, but is instead built entirely in the editor. However, they still need to be *transformed* to provide the engine with an optimized format.

## Creating Assets

The straight forward way to create an asset document is through the menu *Editor > Create Document...*. This gives you a blank asset and you can (and must) fill out all properties manually.

For common types of assets there is a more convenient way to quickly fill out the common properties. See the [asset import](import-assets.md) documentation for details.

## Asset GUID

The editor references assets not by file path, but by **GUID** (**G**lobally **U**nique **ID**entifier). Each asset is assigned a GUID upon creation and the GUID never changes. That means an asset document can be renamed and moved to a different location on disk, and the editor will continue to find it. Similarly, the engine runtime will also locate the transformed asset files through the asset GUID (the [file system](../runtime/filesystem.md) takes care of translating a GUID to an actual path). This makes reorganizing the file structure easy and resilient to errors.

For the rare case that you need to know the actual GUID of an asset, you can right click any asset document and select *Copy Asset GUID*.

The only caveat is, that you should never duplicate an asset by actually copy and pasting an asset file, as this would result in two assets with the same GUID. The editor will try to detect and fix such cases, but it may not work out the way you planned. Instead use the *File > Save as...* functionality to create a copy of an asset with a different name. This will assign a new asset GUID to the new asset document.

## Asset Browser

All assets are listed in the [asset browser](asset-browser.md).

## Asset Errors

An asset can be in an error state. The most common reason for this is, that it references files or other assets that don't exist (anymore). In this case the asset cannot be transformed correctly and will therefore not produce any new output.

All erroneous assets are listed in the [asset curator](asset-curator.md). The curator panel will also show error log output for those assets. A common problem is, when you moved an asset document to a new location, you may also need to adjust the path to input files, such as the source texture or model data. Another problem are deleted assets, or missing assets because of a different [data directory](../projects/data-directories.md) setup.

## Asset Profiles

Assets can produce different, platform specific output, depending on which platform they are being transformed for. That means a texture may, for example, generate a runtime file that contains full resolution 4K textures for PC, but only limited 1K resolution textures for mobile devices. Such platform specific options can be configured through [asset profiles (TODO)](asset-profiles.md). For some types of assets, such platform specific settings may also be handled externally, for example [FMOD](../sound/fmod-overview.md) already deals with platform specific audio encoding on its own.

## Assets and Resources

The term *asset* mostly refers to the editor side and the [editor documents](../editor/editor-documents.md). When an asset gets transformed, it generates the data representation for the runtime side. Inside the engine this data will be read into a *resource* by the [resource manager (TODO)](../runtime/resource-management.md).

Assets and resources are conceptually two different things. Assets always live on the editor side, resources always on the runtime side. Their code is strictly separate. Resources can be loaded from files or procedurally generated at runtime. The files that they load can come from anywhere and there is no requirement that those files are created through assets. However, assets are the most common and most convenient way to generate the runtime data. You could replace the entire asset management system with a custom system, though. The editor may be the most convenient way to transform assets from source format to runtime format for most scenarios, but if you have a special use case, you could built a completely custom asset processing pipeline and ignore the editor entirely, there is no 'secret sauce' in the editor that is required to make the runtime work.

Consequently, when the documentation mentions 'assets', it always refers the data and behavior in the editor, and when it mentions 'resources' it always refers to data that is used by the runtime side (the renderer, the physics engine, the game logic, etc). When you work with the editor, the two code paths are even separated into different processes: `Editor.exe` and `EditorEngineProcess.exe`

## Video

[![ezEngine Overview](https://img.youtube.com/vi/1OUJfB6ltWw/0.jpg)](https://www.youtube.com/watch?v=1OUJfB6ltWw)

## See Also

* [Editor Documents](../editor/editor-documents.md)
* [Asset Browser](asset-browser.md)
* [Asset Curator](asset-curator.md)
* [Asset Profiles (TODO)](asset-profiles.md)
* [Asset Import](import-assets.md)
