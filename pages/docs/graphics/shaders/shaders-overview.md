# Shaders

Shaders are files with the `.ezShader` extension. These files not only provide the HLSL code for each shader stage used, but also the complete render state used when drawing with this shader. Several permutations of the same shader can exist. Permutations can impact the render state or affect the HLSL source code. Thus, one shader file can produce several outputs.

## Getting Started

This page describes the structure of a shader file in ezEngine. If you want to write your own shader, we highly suggest to start from a [shader template](shader-templates.md), as it makes setting up a basic shader significantly easier.

## Shader Sections

Each shader is made up of several **sections**. Not all sections need to be defined as most have a default state. Here is a very simple shader:

```cpp
[PLATFORMS]
ALL

[PERMUTATIONS]

[RENDERSTATE]

[SHADER]

cbuffer PerObject : register(b1)
{
  float4x4 mvp : packoffset(c0);
};

struct VS_IN
{
  float3 pos : POSITION;
  float2 texcoord0 : TEXCOORD0;
};

struct VS_OUT
{
  float4 pos : SV_Position;
  float2 texcoord0 : TEXCOORD0;
};

typedef VS_OUT PS_IN;

[VERTEXSHADER]
VS_OUT main(VS_IN Input)
{
  VS_OUT RetVal;
  RetVal.pos = mul(mvp, float4(Input.pos, 1.0));
  RetVal.texcoord0 = Input.texcoord0;
  return RetVal;
}

[PIXELSHADER]
Texture2D DiffuseTexture;
SamplerState PointClampSampler;

float4 main(PS_IN Input) : SV_Target
{
  return DiffuseTexture.Sample(PointClampSampler, Input.texcoord0);
}
```

The following sections are supported:

### PLATFORMS

The `PLATFORMS` section lists the shader platforms that are supported by this shader and for which the shader should be compiled. Currently, these values are supported:

* `ALL`: The shader is supported on all platforms.
* `DEBUG`: If set, the shader is not optimized and contains debug information to allow stepping through it in tools like RenderDoc.
* `VULKAN`: The shader will be compiled as SPIRV code for the Vulkan renderer.
* `DX11_SM50`: DX11 feature set. Default platform used by the DX11 renderer.

```cpp
[PLATFORMS]
ALL
DEBUG
```

### PERMUTATIONS

The `PERMUTATIONS` section defines permutation variables which allow for modification of the shader code. Each variable is exposed as a preprocessor variable, allowing for various sections of the shader to be modified via preprocessor blocks. 

The values of these permutation variables are defined by the engine / material and the entire system is explained in detail in the dedicated [shader permutation variables](shader-permutation-variables.md) page.

```cpp
[PERMUTATIONS]
ALPHATEST
CAMERA_MODE = CAMERA_MODE_PERSPECTIVE
```

### Material Sections

Material shaders are special and require further sections to expose parameters to the engine and editor.

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

#### MATERIALCONSTANTS

This sections defines per-material constants.

The material constants are what eventually maps to constant buffer or structured buffer in the engine, depending on the renderer feature set. These can be changed at runtime for each material and also exposed to the editor.

These need to be constant macros defined in `Data/Base/Shaders/Common/ConstantBufferMacros.h`, e.g. `FLOAT1(ConstantName);`. Only these macros are supported:

* `FLOAT1`, `FLOAT2`, `FLOAT3`, `FLOAT4`: Maps to HLSL `float`, `float2` etc.
* `INT1`, `INT2`, `INT3`, `INT4`: Maps to HLSL `int`, `int2` etc.
* `UINT1`, `UINT2`, `UINT3`, `UINT4`: Maps to HLSL `uint`, `uint2` etc.
* `MAT3`, `MAT4`: Maps to HLSL `float3x3` and `float4x4`.
* `TRANSFORM`: Note, that there is no HLSL type for this, instead this maps to a struct with three rows `r0`, `r1` and `r2`.
* `COLOR4F`: Note, that there is no color type in HLSL, so this maps to `float4` instead.
* `BOOL1`: Note, that the HLSL `bool` is always 4 bytes wide. Consider using flags inside an `UINT1` instead to safe space if you have multiple bool variables in your constants.

To access these in the shader, use the macro `GetMaterialData(ConstantName)` to access the constant's value.

#### MATERIALPARAMETER

This section defines which parameters to expose on a material in the editor.

There are three categories:

* **Permutation variables**: Add the name of a permutation variable to expose it in the editor. This is explained in detail in [exposing permutation variables to materials](shader-permutation-variables.md#exposing-permutations-to-materials).

* **Material constants**: To expose, these need to match exactly the name that was used in the `MATERIALCONSTANTS` section described above. Note that the type changes from the macro name to the HLSL name, e.g. `FLOAT1(MaskThreshold);` becomes `float MaskThreshold @Default(0.25);`.

* **Textures**: Both `Texture2D` and `TextureCube` are supported. Use the same syntax as you would for declaring a texture in HLSL.

Parameters can have attributes that define default value and other meta data for the editor:

* `@Default(<VALUE_TYPE>)`: Can be used on constants and textures to define the default value.
* `@Clamp(0.0, 1.0)`: Usable on float and int parameters, this can be used to clamp the value the user can set in the editor to a fixed range.

#### MATERIALCONFIG

The MATERIALCONFIG section controls when a material is rendered during a frame by assigning a *RenderDataCategory*. This category determines which render passes process the material, the sorting order of objects using this material, and how the material integrates into the rendering pipeline.

##### Understanding RenderDataCategory

During rendering, components extract render data and tag it with a specific category. Render passes then process only the categories they need in a specific order. For example, opaque geometry (LitOpaque category) is rendered before transparent geometry (LitTransparent category), and objects within each category are sorted differently: opaque geometry front-to-back for depth rejection optimization, transparent geometry back-to-front for correct alpha blending.

##### Default Category Assignment

Most materials use the default category assignment provided by `MaterialConfig.h`. Include it in your MATERIALCONFIG section to automatically map BLEND_MODE permutation values to appropriate categories:

```cpp
[MATERIALCONFIG]
#include <Shaders/Materials/MaterialConfig.h>
```

This automatically assigns categories based on BLEND_MODE:

* `BLEND_MODE_OPAQUE` → `LitOpaque`
* `BLEND_MODE_MASKED` or `BLEND_MODE_DITHERED` → `LitMasked`
* All others (TRANSPARENT, ADDITIVE, MODULATE) → `LitTransparent`

You can override this by explicitly setting the category:

```cpp
[MATERIALCONFIG]
RenderDataCategory = SimpleForeground
```

##### Available Render Data Categories

###### Lit Categories (Full PBR Lighting)

These categories render with complete lighting calculations including direct lights, shadows, and image-based lighting.

* **LitOpaque** - Use for solid, opaque materials. Renders in the depth pre-pass (optional) and opaque forward pass. Sorted front-to-back for optimal depth rejection. Automatically resolves to LitOpaqueStatic or LitOpaqueDynamic based on whether the object is static or moves.

* **LitMasked** - Use for materials with binary alpha cutout like foliage, chain-link fences, or grates. Similar to LitOpaque but uses alpha testing to discard pixels. Writes to the depth buffer. Renders in depth pre-pass and opaque forward pass. Resolves to LitMaskedStatic or LitMaskedDynamic.

* **LitTransparent** - Use for alpha-blended transparent materials like glass, water, or particles. Renders in the transparent forward pass after opaque geometry. Sorted back-to-front for correct blending. Does not write to the depth buffer. Reads lighting information.

* **LitForeground** - Use for transparent materials that should render after other transparent objects. Renders after the LitTransparent pass. Useful for effects that need to appear in front of regular transparent geometry.

* **LitScreenFX** - Use for screen-space effects with lighting. Renders in the transparent forward pass with special handling for screen-aligned effects.

###### Simple Categories (Unlit Rendering)

These categories use unlit rendering without lighting calculations. Useful for debug visualization, editor tools, and effects that should not be affected by scene lighting.

* **SimpleOpaque** - Use for unlit opaque geometry like debug visualizations or editor gizmos. Renders after lit passes. No lighting calculations. Sorted front-to-back.

* **SimpleTransparent** - Use for unlit transparent geometry. Renders after SimpleOpaque. Sorted back-to-front. No lighting calculations.

* **SimpleForeground** - Use for debug overlays and UI elements in 3D space. Renders last among simple categories to ensure debug visualization appears on top of other geometry.

###### Special Categories

* **Sky** - Use for skybox and sky dome materials. Renders after the depth pre-pass but before the opaque forward pass to provide the scene background.

* **Light** - Use for light source visualization geometry. Renders with special handling for light volumes and debug rendering.

* **Decal** - Use for projected decals on surfaces. Renders after the opaque forward pass and projects onto opaque geometry.

* **ReflectionProbe** - Use for reflection probe visualization. Primarily used for editor and debug rendering of reflection capture volumes.

* **Selection** - Use for editor selection highlighting. Editor-only category for visualizing selected objects.

* **GUI** - Use for UI rendering. Special category with specific handling for GUI elements.

##### Static vs Dynamic Resolution

LitOpaque and LitMasked are "redirected categories" that automatically resolve to Static or Dynamic variants at runtime:

* **LitOpaque** resolves to **LitOpaqueStatic** or **LitOpaqueDynamic**
* **LitMasked** resolves to **LitMaskedStatic** or **LitMaskedDynamic**

This resolution happens during render data extraction based on component flags (whether the object's transform changes or is animated). The rendering pipeline can then optimize static geometry separately from dynamic geometry, enabling better batching and caching strategies.

**Important:** Shader authors should use LitOpaque and LitMasked in the MATERIALCONFIG section, not the Static/Dynamic variants directly. The engine handles the resolution automatically.

##### Rendering Pipeline Order

Materials are rendered in this order during a frame:

1. **Depth Pre-Pass** (optional): LitOpaqueStatic, LitOpaqueDynamic, LitMaskedStatic, LitMaskedDynamic - Renders depth-only for early-z rejection optimization
2. **Sky Rendering**: Sky - Renders the background skybox or sky dome
3. **Opaque Forward**: LitOpaqueStatic, LitOpaqueDynamic, LitMaskedStatic, LitMaskedDynamic - Renders opaque geometry with full lighting
4. **Decals**: Decal - Projects decals onto opaque surfaces
5. **Transparent Forward**: LitTransparent, LitForeground, LitScreenFX - Renders transparent geometry with lighting
6. **Simple Rendering**: SimpleOpaque, SimpleTransparent, SimpleForeground - Renders unlit geometry and debug visualization
7. **Special**: Light, ReflectionProbe, Selection, GUI - Renders specialized visualization and UI

### RENDERSTATE

Each shader defines the complete state of the renderer. This includes, but is not limited to blending, rasterizer, depth stencil etc. You can use permutation variables and preprocessor macros to change the render state of shader permutations.
This is explained in more detail on the [shader render state](shader-render-state.md) page.

```cpp
[RENDERSTATE]
#if WIREFRAME == 1
  WireFrame = true
#endif
```

### SHADER

The `SHADER` section contains code that is shared among all shader stages. The content is simply prepended to all used stages before compiling.

### SHADER stages

Each shader stage has its own section. The following stages are supported: `VERTEXSHADER`, `HULLSHADER`, `DOMAINSHADER`, `GEOMETRYSHADER`, `PIXELSHADER` and `COMPUTESHADER`. Even if you define a shader section, you can use the preprocessor to remove its content via permutation variables, allowing you to remove stages from certain permutations.

The entry point into each stage must be called `main`. The shader code supports preprocessor macros that are defined by [permutation variables](shader-permutation-variables.md) as well as include directives.
Beyond that, any HLSL code is fine as long as it compiles on the [platforms](#platforms) the shader defines. However, when defining resources, special care must be taken to ensure no conflicting resource mappings are created between the stages. Please refer to the [shader resource](shader-resources.md) page for further details and on how to facilitate interop with the C++ code.

### TEMPLATE_VARS

This section is only used when [creating a shader template](shader-templates.md#adding-a-shader-template).

## See Also

* [Shader Templates](shader-templates.md)
* [Shader Render State](shader-render-state.md)
* [Shader Permutation Variables](shader-permutation-variables.md)
* [Shader Resources](shader-resources.md)
* [ShaderCompiler](../../tools/shadercompiler.md)
* [Render Pipeline](../render-pipeline/render-pipeline-overview.md)
