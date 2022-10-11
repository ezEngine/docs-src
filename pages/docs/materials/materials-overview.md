# Materials

*Materials* are used to define the visual properties of rendered objects. Materials specify what [shader (TODO)](../graphics/shaders/shaders-overview.md) to use to render an object and they allow you to configure that shader. Most commonly you select which [textures](../graphics/textures-overview.md) to use. The most common use case for materials is through [meshes](../graphics/meshes/meshes-overview.md). Each sub-mesh can have its own material.

![Material editor](media/material-editor.jpg)

The image above shows the material asset editor. Material assets are often automatically created when you [import a mesh asset](../assets/import-assets.md). For example importing an `FBX` or `OBJ` file will not only create a mesh asset, but can additionally create the necessary material and texture assets for you. Unfortunately, this process is not always perfect, so you should always review which assets were created and how.

## Physical Properties

Although materials are mainly used to configure the rendering, they can optionally reference a [surface](surfaces.md), which is used to define physical properties (e.g. friction) and gameplay relevant interactions. Whether the referenced surface is actually used depends on where the material is applied. For instance, on a [greyboxing component](../scenes/greyboxing.md) the material sets up both the graphics and the physics properties, on a [mesh component](../graphics/meshes/mesh-component.md) it only sets up the rendering and you would need to additionally select a surface for the corresponding [collision mesh](../physics/physx/collision-shapes/physx-collision-meshes.md).

## Selecting a Shader

Through the `ShaderMode` property there are three ways a material can select which shader to use:

* **From Base Material:** This is the most convenient and most commonly used method. In this mode, you need to select a `BaseMaterial`, which is just another material. All the properties of that base material are copied over to your material, including the shader selection. You can then override each property as you like. This makes it easy to set up a few common base materials and then "derive" all other materials from this common base.

* **From File:** In this mode the material actually references a proper shader file. This allows you to select a custom [shader (TODO)](../graphics/shaders/shaders-overview.md). By default, EZ doesn't have many different shader files, as all important variations are provided by the same shader file. However, if you do decide to write a custom one, this is the way to select it for your material. The engine parses the shader file for configurable properties and displays those as UI elements in the material editor. So things like which texture you can select and what other lighting properties the material will have, are all defined by the selected shader.

  You can easily create a custom shader from a [shader template](../graphics/shaders/shader-templates.md).

* **Visual Shader:** In this mode the material editor will show an additional editing area beneath the 3D view, where you can create your own shader through a visual graph system. This enables you to create custom shader effects like animated textures. There is a dedicated chapter about [visual shaders (TODO)](visual-shaders.md) that explains how to do so.

If you change the selected shader, you need to *transform* (`Ctrl+E`) the material [asset](../assets/assets-overview.md) for the change to take full effect.

## Shader Properties

The `Shader Properties` section lists all the properties that the selected shader exposes. The 3D viewport will live update for any change you make here.

### DefaultMaterial Properties

The `DefaultMaterial` shader that comes with EZ implements a **P**hysically **B**ased **R**endering model (PBR), which is the de facto industry standard these days. The details of PBR rendering are beyond the scope of this documentation, if you want to get an understanding of how *roughness* and *metalness* are use (see below), please search the internet.

The `DefaultMaterial` provides these options:

**Blend Mode:** Defines whether the object will appear opaque or transparent.

* **Opaque:** The object appears solid.
* **Masked:** In this mode the object can have fully transparent (invisible) areas and fully opaque ones. *Blending* is not possible. This is commonly used for vegetation or things like chain-link fences to cut out part of the object. *Masked* geometry does not require any sorting during rendering and is therefore the most efficient and reliable mode of transparency. Which areas appear transparent are defined by the *alpha channel* of the *base texture* and the `MaskThreshold` property. Every pixel whose alpha value is above the threshold (e.g. white) will be visible (opaque) and every pixel whose value is below the threshold (e.g. black) will be invisible.
* **Transparent:** In this mode geometry will appear see-through, ie. it will be blended with the geometry behind it. This mode is commonly used for things like glass or water. Again, the *alpha channel* of the *base texture* determines which areas appear more or less transparent.
* **Additive:** In this mode the geometry will not be blended with the background but simply added on top of it. The *alpha channel* affects how strongly it is added.
* **Modulate:** This mode allows you to darken or brighten the background. A pure white material (base texture and base color) will brighten everything that is behind the object. A pure black material will darken the background. A material that is mid grey will let the background through unmodified. This mode can be used for various special effects, especially when writing a [visual shader (TODO)](visual-shaders.md) that animates the texture and the alpha channel with noise.

For testing transparent materials it may be useful to create an object in a scene and observe it there, where you can place it in front of different backgrounds.

**Shading Mode:** This mode allows you to select whether objects with this material should receive realistic *lighting* or should always appear *fullly bright*. The latter is useful for 2D sprites and UI elements.

**Two Sided:** If enabled, polygons with this material can be seen from both sides. This is useful for fences, vegetation and other *masked* geometry that is often represented only by a single polygon but can be looked at from both sides.

**MaskThreshold:** Used for the *Masked* blend mode (see above).

**UseBaseTexture:** If enabled, the *Base Texture* is used to color the object. This requires proper UV coordinates on the mesh.

**Base Color:** The base color of the material. When no *base texture* is used, this is its only color, otherwise it is multiplied into the base texture color.

**UseNormalAndRoughnessTexture:** If enabled, the shader uses the *Normal Texture* to apply *normal mapping* and the *Roughness Texture* to determine how rough the surface is. These affect the quality of lighting on the objects.

**Roughness Value:** If no *Roughness Texture* is given, this is the fallback roughness value to use for lighting. The rougher a material is (value closer to one), the more *diffuse* the lighting will be (stone, cloth, etc). The smoother the material is (value closer to zero), the more pronounced specular highlights it will have (glass, ceramic).

**UseMetallicTexture:** If enabled, a dedicated *Metallic Texture* is used to specify per pixel whether it is a metal or not. In physics, a material is either a metal or not, in computer graphics values in between are allowed and used to blend between the two results.

**Metallic Value:** If no *Metallic Texture* is provided, this is the fallback value. Typically this should be `1` for metals and `0` for all other material types.

**UseEmissiveTexture:** If enabled, the *Emissive Texture* is used to define per pixel where the material will *glow*. This is multiplied with the *EmissiveColor*, so make sure that is not set to black (its default).

**EmissiveColor:** An additional overall emissive color. If an *Emissive Texture* is activated, these two colors are multiplied, so you need to set this to *white* for the texture to have an effect. This is an HDR color, so you can scale up its *intensity* and thus pronounce the glow even further.

**UseOcclusionTexture:** If enabled, an *OcclusionTexture* is used to affect lighting and to pronounce crevices. The effect of this can be very subtle.

## Render Modes

The 3D viewport of the material editor allows you to switch [render modes](../editor/editor-views.md#render-modes) to inspect only specific aspects of the material.

## See Also


* [Visual Shaders (TODO)](visual-shaders.md)
* [Textures](../graphics/textures-overview.md)
* [Meshes](../graphics/meshes/meshes-overview.md)
