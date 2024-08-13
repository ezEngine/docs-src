# Asset Import

All [assets](assets-overview.md) are represented by [documents](../editor/editor-documents.md). That means to get a texture into the engine, you need a [texture document](../graphics/textures-overview.md) which describes which source files (png, jpg, etc) are used to create the texture and how they shall be imported. This is where you configure such things as, whether to use compression, whether an alpha channel should be present and so on.

Other asset types of course have other options for importing.

To create these documents you have two options: Manual or automatic import.

## Create Documents Manually

You can manually create documents by right clicking into the [asset browser](asset-browser.md) and selecting *New > Asset Type*. If you right clicked free space, the asset document will be created in the folder that is selected on the left. If you right clicked another document, the new document will be created in the same folder as the selected asset.

The new document will be in a blank state. You need to fill out all the properties, including where the source files are located.

This method always works for all asset types and for some types it is the only way. Since this method always involves multiple, mostly simple steps, it can become tedious. Therefore, some asset types provide a way to automate much of this process.

## Create Documents Automatically

For asset types that are mostly defined by a single source file (e.g. [textures](../graphics/textures-overview.md) and [meshes](../graphics/meshes/mesh-asset.md)), the editor often provides an importing method that automates most of the trivial setup.

### Quick Import

The **most convenient** way is to find the source asset file in the [asset browser](asset-browser.md) (ensure it shows *importable files*), right-click on it and select **Import As**. This sub-menu makes it possible to quickly import one or multiple assets as a specific asset type. It does so fully automatically. For some file types this method also allows to import assets quickly multiple times. For example, [animation clips](../animation/skeletal-animation/animation-clip-asset.md) are often packed into a single file, which requires them to be imported many times.

### Controlled Import

If you want to have a few more options, select **Import...** instead.

Another method is to select **Project > Import Assets...** or press **CTRL+I** to open a file browse dialog. Navigate to the file(s) that you want to import and select them. If you want to know which asset types are currently supported for automatic import, you can open the dropdown with the allowed file extensions here.

Afterwards, you will be presented with a table of options how to import the selected files:

![Asset Import Table](media/asset-import.png)

Here we selected four files for import. One .obj file and three .jpg files. The automatic import uses heuristics to make an educated guess how to import certain source files. Here it already suggests to import the "_col.jpg" file as a diffuse texture, the "_nrm.jpg" file as a normal map and so on. If the heuristic is incorrect, you can use the dropdown on the left to fix it.

Some source files can be imported in multiple ways. For example the .obj file could be imported as a mesh for rendering or as a mesh for physics. Often you want to import the same mesh for both, so you want two asset documents (a *Mesh* and a *Collision Mesh*) which reference the same input file. Therefore this table lists the .obj file twice but with different import options in the dropdown box. If, for example, you do not want a mesh to be imported as collision mesh, at all, you can just select *No Import* from the respective dropdown.

Once you click *Import* the asset documents are generated and you can then open them. If background asset processing is enabled, the editor will already start [transforming](assets-overview.md#asset-transform) the asset data.

The automatic import creates the documents using a set of rules to fill out its properties, depending on the template that you selected for it. So for example an image imported as a "diffuse texture" and one imported as a "normal map" are mostly the same, except that a few options are already configured in a certain way for you. You should review all options for correctness afterwards.

### Import Via Drag And Drop

The methods above assume that the source asset is already present inside one of the project's [data directories](../projects/data-directories.md). If that is not the case, you can drag and drop a file into the [asset browser](asset-browser.md) to copy the file into the selected directory. This also automatically launches the asset import dialog mentioned above.

## Video: How to import textures

[![video](https://img.youtube.com/vi/x4qUFga-Jis/0.jpg)](https://www.youtube.com/watch?v=x4qUFga-Jis)

## Video: How to import meshes

[![video](https://img.youtube.com/vi/XBO4OPcF2bs/0.jpg)](https://www.youtube.com/watch?v=XBO4OPcF2bs)

## See Also

* [Assets](assets-overview.md)
* [Asset Browser](asset-browser.md)
