# Terrain Materials

Terrain components require materials whose shaders understand the terrain's vertex format. The engine ships sample shader implementations that can be used directly or as a reference for custom shaders. The necessary setup code is provided in headers that can be easily reused in custom shaders.

## Sample Shaders

Two ready-to-use sample shaders are provided:

* `Shaders/Terrain/Rendering/HeightfieldTerrainMaterial.ezShader` — for [terrain patches](terrain-patch-component.md).
* `Shaders/Terrain/Rendering/VoxelMeshMaterial.ezShader` — for [terrain volumes](terrain-volume-component.md).

Example material assets that use these shaders can be found in the *Testing Chambers* sample project under `Data/Samples/Testing Chambers/Materials/`.

## Texture Setup

Both sample shaders use three texture arrays (type `Texture2DArray`):

* `LayerBaseTexture` — diffuse/albedo color.
* `LayerNormalTexture` — normal maps.
* `LayerRoughnessTexture` — roughness, read from the R channel. The sample shaders take metallic from a material-wide `MetallicValue` constant instead of a texture channel, and disable ambient occlusion on terrain geometry entirely.

The sample material supports up to 8 layers and there is a mapping to reuse the same texture layer across different material layers. The shader uses different textures to project onto the ground and walls. This is just one way to do this, when you write your own terrain shaders, you can use entirely different methods to organize your data and you can support much more layers, as well.

## Height Blending

By default, the transition between two material layers is a linear cross-fade. With *height blending*, each layer additionally provides a height map, and in the transition area the layer that is locally higher is shown. For example, where rocks transition into sand, the stones of the rock texture stay visible further into the sand, while the sand fills the crevices between the stones. This makes transitions sharper and more detailed. Height blending requires additional texture samples in the pixel shader for every layer that contributes to a pixel.

To use height blending, enable the `TERRAIN_HEIGHT_BLEND` permutation on the material and set up these additional properties:

* `LayerHeightTexture` — texture array with the height map of each layer, read from the R channel. 
* `HeightBlendDepth` — the width of the transition between layers. Small values result in hard edges around individual features, large values approach the linear blend.
* `HeightBlendStrength` — how strongly the height maps affect the transition. A value of `0` results in the linear blend.

## Writing a Custom Heightfield Shader

The engine exposes the heightfield's vertex data through include-able header files. A custom heightfield shader must do the following:

**Vertex shader:**

1. Before including any material interpolator header, declare the custom interpolator that carries the upper two blend weights to the pixel shader:
   ```hlsl
   #define CUSTOM_INTERPOLATOR float2 MatWeightsHi : TEXCOORD2;
   ```
2. Include `<Shaders/Terrain/Rendering/HeightfieldTerrainVS.h>`. This provides the `FillHeightfieldTerrainVertexOutput(uint vertexID)` function and declares the GPU buffers for heights, normals, cell materials, and per-vertex blend weights.
3. Call `FillHeightfieldTerrainVertexOutput(input.VertexID)` from the main vertex shader function and return its result.

The vertex output carries:
* `TexCoord0.x/y` — blend weights w0 and w1 for the top two material layers.
* `MatWeightsHi.x/y` — blend weights w2 and w3 for the third and fourth material layers.
* `DataOffsets.y` — four packed 8-bit cell material indices (mat0 in bits 0–7, mat1 in bits 8–15, mat2 in bits 16–23, mat3 in bits 24–31).

A fifth implicit weight for the fallback material slot (given by the `FallbackMaterialSlot` push constant) is reconstructed as `max(0, 1 - w0 - w1 - w2 - w3)`.

**Pixel shader:**

Include `<Shaders/Terrain/Rendering/TerrainLayerSampling.h>` after `MaterialPixelShader.h`. This provides:
* `TriplanarWeights(float3 worldNormal)` — computes blend weights for triplanar projection.
* `TriplanarSampleColorArray(tex, samp, worldPos, worldNormal, weights, scale, matIndex)` — samples one layer from a color texture array using triplanar projection.
* `TriplanarSampleNormalArray(tex, samp, worldPos, worldNormal, weights, scale, matIndex)` — same for normal map arrays; returns a world-space normal.

## Writing a Custom Voxel Shader

**Vertex shader:**

Include `<Shaders/Terrain/Rendering/VoxelTerrainVS.h>` in the vertex shader section. This provides `FillVoxelTerrainVertexOutput(uint vertexID)` and declares the GPU vertex and index buffers.

The vertex output carries:
* `TexCoord0.x` — material blend weight (`MaterialStrength`), in [0, 1]. This is the brush-painted override blend weight; 0 means only the base material is visible.
* `DataOffsets.y` — dominant material index for this vertex, or `0xFFFFFFFF` if the vertex is inactive.

**Pixel shader:**

Use the same `<Shaders/Terrain/Rendering/TerrainLayerSampling.h>` helpers as for heightfield shaders.

## See Also

* [Terrain Patch Component](terrain-patch-component.md)
* [Terrain Volume Component](terrain-volume-component.md)
* [Materials](../materials/materials-overview.md)
* [Visual Shaders](../materials/visual-shaders.md)
