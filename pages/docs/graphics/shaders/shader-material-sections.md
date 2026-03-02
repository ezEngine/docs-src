# Shader Material Sections

Material shaders are special and require additional sections to expose parameters to the engine and editor. A material shader typically includes all three sections shown below:

```cpp
[MATERIALCONSTANTS]
COLOR4F(BaseColor);

[MATERIALPARAMETER]
Permutation BLEND_MODE;
Color BaseColor @Default(Color(1.0, 1.0, 1.0));
Texture2D BaseTexture @Default("{ ac614d7c-2b31-4a7b-aa0c-c5d8200b7b89 }");

[MATERIALCONFIG]
#if (BLEND_MODE == BLEND_MODE_OPAQUE)
    RenderDataCategory = LitOpaque
#elif (BLEND_MODE == BLEND_MODE_MASKED)
    RenderDataCategory = LitMasked
#else
    RenderDataCategory = LitTransparent
#endif

[PIXELSHADER]

Texture2D BaseTexture;
SamplerState BaseTexture_AutoSampler;

float4 main(VS_OUT a) : SV_Target
{
  float4 color = BaseTexture.Sample(BaseTexture_AutoSampler, ...).rgba;
  return color * GetMaterialData(BaseColor).rgba;
}
```

## MATERIALCONSTANTS

This section defines per-material constants. The constants map to a constant buffer or structured buffer in the engine, depending on the renderer feature set. They can be changed at runtime for each material instance and exposed to the editor.

Constants must be declared using the macros defined in `Data/Base/Shaders/Common/ConstantBufferMacros.h`, e.g. `FLOAT1(ConstantName);`. Only these macros are supported:

* `FLOAT1`, `FLOAT2`, `FLOAT3`, `FLOAT4`: Maps to HLSL `float`, `float2` etc.
* `INT1`, `INT2`, `INT3`, `INT4`: Maps to HLSL `int`, `int2` etc.
* `UINT1`, `UINT2`, `UINT3`, `UINT4`: Maps to HLSL `uint`, `uint2` etc.
* `MAT3`, `MAT4`: Maps to HLSL `float3x3` and `float4x4`.
* `TRANSFORM`: Maps to a struct with three rows `r0`, `r1` and `r2` (no direct HLSL equivalent).
* `COLOR4F`: Maps to `float4` (no color type exists in HLSL).
* `BOOL1`: The HLSL `bool` is always 4 bytes wide. Consider packing multiple flags into a `UINT1` to save space.

To access a constant in the shader, use `GetMaterialData(ConstantName)`.

## MATERIALPARAMETER

This section defines which parameters are exposed on a material in the editor. There are three categories:

* **Permutation variables**: Add the name of a permutation variable to expose it in the editor. See [Shader Permutation Variables](shader-permutation-variables.md#exposing-permutations-to-materials) for details.

* **Material constants**: These must match the name used in `MATERIALCONSTANTS` exactly. The type changes from the macro name to the HLSL name, e.g. `FLOAT1(MaskThreshold);` becomes `float MaskThreshold @Default(0.25);`.

* **Textures**: Both `Texture2D` and `TextureCube` are supported, using the same syntax as HLSL texture declarations.

Parameters support the following attributes:

* `@Default(<VALUE>)`: Sets the default value shown in the editor. Usable on constants and textures.
* `@Clamp(min, max)`: Restricts the range of float and int parameters in the editor.

## MATERIALCONFIG

This section controls when a material is rendered during a frame by assigning a *RenderDataCategory*. The category determines which render passes process the material, how objects using it are sorted, and how it integrates into the rendering pipeline.

### Default Category Assignment

Most materials use the default mapping provided by `MaterialConfig.h`:

```cpp
[MATERIALCONFIG]
#include <Shaders/Materials/MaterialConfig.h>
```

This automatically assigns categories based on `BLEND_MODE`:

* `BLEND_MODE_OPAQUE` → `LitOpaque`
* `BLEND_MODE_MASKED` or `BLEND_MODE_DITHERED` → `LitMasked`
* All others (TRANSPARENT, ADDITIVE, MODULATE) → `LitTransparent`

You can override this by setting the category explicitly:

```cpp
[MATERIALCONFIG]
RenderDataCategory = SimpleForeground
```

### Available Render Data Categories

#### Lit Categories (Full PBR Lighting)

These categories render with complete lighting calculations including direct lights, shadows, and image-based lighting.

* **LitOpaque** — Use for solid, opaque materials. Renders in the depth pre-pass and opaque forward pass. Sorted front-to-back for optimal depth rejection. Automatically redirected to `LitOpaqueStatic` or `LitOpaqueDynamic` based on whether the object is static or dynamic.

* **LitMasked** — Use for materials with binary alpha cutout, such as foliage, chain-link fences, or grates. Similar to `LitOpaque` but uses alpha testing to discard pixels. Writes to the depth buffer. Redirected to `LitMaskedStatic` or `LitMaskedDynamic`.

* **LitTransparent** — Use for alpha-blended transparent materials like glass, water, or particles. Renders after opaque geometry. Sorted back-to-front for correct blending. Does not write to the depth buffer.

* **LitForeground** — Use for transparent materials that must appear in front of regular transparent geometry. Renders after `LitTransparent`.

* **LitScreenFX** — Use for screen-space effects with lighting.

#### Simple Categories (Unlit Rendering)

These categories skip lighting calculations. Useful for debug visualization, editor tools, and effects that should not be affected by scene lighting or tonemapping.

* **SimpleOpaque** — Unlit opaque geometry. Renders after lit passes. Sorted front-to-back.
* **SimpleTransparent** — Unlit transparent geometry. Renders after `SimpleOpaque`. Sorted back-to-front.
* **SimpleForeground** — Debug overlays and 3D UI elements. Renders last among simple categories to appear on top of other geometry.

#### Special Categories

* **Sky** — For skybox and sky dome materials. Renders after the opaque forward pass to fill the background.
* **GUI** — For UI rendering.

### Static vs Dynamic Redirection

`LitOpaque` and `LitMasked` are *redirected categories*: at runtime, the engine automatically redirects them to their static or dynamic variants based on object flags.

* **LitOpaque** → **LitOpaqueStatic** or **LitOpaqueDynamic**
* **LitMasked** → **LitMaskedStatic** or **LitMaskedDynamic**

Shader authors should always use `LitOpaque` and `LitMasked` in the `MATERIALCONFIG` section. Do not use the Static/Dynamic variants directly.

### Rendering Pipeline Order

Materials are rendered in the following order each frame:

1. **Depth Pre-Pass** (optional): `LitOpaqueStatic`, `LitOpaqueDynamic`, `LitMaskedStatic`, `LitMaskedDynamic`
2. **Opaque Forward**: `LitOpaqueStatic`, `LitOpaqueDynamic`, `LitMaskedStatic`, `LitMaskedDynamic`
3. **Sky**: `Sky`
4. **Transparent Forward**: `LitTransparent`, `LitForeground`, `LitScreenFX`
5. **Simple**: `SimpleOpaque`, `SimpleTransparent`, `SimpleForeground`
6. **GUI**: `GUI`

## See Also

* [Shaders](shaders-overview.md)
* [Shader Permutation Variables](shader-permutation-variables.md)
* [Shader Render State](shader-render-state.md)
