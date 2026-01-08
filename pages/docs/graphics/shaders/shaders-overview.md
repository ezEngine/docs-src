# Shaders

Shaders are files with the `.ezShader` extension. These files not only provide the HLSL code for each shader stage used, but also the complete render state used when drawing with this shader. Several permutations of the same shader can exist. Permutations can impact the render state or affect the HLSL source code. Thus, one shader file can produce several outputs.

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
* `DX11_SM40_93`: DX9 feature set. Used by the DX11 renderer when using downlevel hardware support.
* `DX11_SM40`: DX10 feature set. Used by the DX11 renderer when using downlevel hardware support.
* `DX11_SM41`: DX10.1 feature set. Used by the DX11 renderer when using downlevel hardware support.
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

Material shaders are special and require further sections expose parameters to the engine and editor.

> **NOTE:**
>
> These sections have changed with a recent refactor. If you need to migrate from the old system, please follow the steps here: [Material Refactor](https://github.com/ezEngine/ezEngine/pull/1516).

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

#### `MATERIALCONSTANTS`: This sections defines per-material constants
The material constants are what eventually maps to constant buffer (hence the name of the section) or structured buffer in the engine, depending on the renderer feature set. These can be changed at runtime for each material and also exposed to the editor. 
These need to be constant macros defined in `Data/Base/Shaders/Common/ConstantBufferMacros.h`, e.g. `FLOAT1(ConstantName);`. Only these macros are supported:
* `FLOAT1`, `FLOAT2`, `FLOAT3`, `FLOAT4`: Maps to HLSL `float`, `float2` etc.
* `INT1`, `INT2`, `INT3`, `INT4`: Maps to HLSL `int`, `int2` etc.
* `UINT1`, `UINT2`, `UINT3`, `UINT4`: Maps to HLSL `uint`, `uint2` etc.
* `MAT3`, `MAT4`: Maps to HLSL `float3x3` and `float4x4`.
* `TRANSFORM`: Note, that there is no HLSL type for this, instead this maps to a struct with three rows `r0`, `r1` and `r2`.
* `COLOR4F`: Note, that there is no color type in HLSL, so this maps to `float4` instead.
* `BOOL1`: Note, that the HLSL `bool` is always 4 bytes wide. Consider using flags inside an `UINT1` instead to safe space if you have multiple bool variables in your constants.

To access these in the shader, use the macro `GetMaterialData(ConstantName)` to access the constant's value.

#### `MATERIALPARAMETER`: What parameters to expose on a material in the editor
There are three categories:
  * **Permutation variables**: Add the name of a permutation variable to expose it to the user in the editor. This is explained in detail in [exposing permutation variables to materials](shader-permutation-variables.md#exposing-permutations-to-materials).
  * **Material constants**: To expose, these need to match exactly the name that was used in the `MATERIALCONSTANTS` section described above. Note that the type changes from the macro name to the HLSL name, e.g. `FLOAT1(MaskThreshold);` becomes `float MaskThreshold @Default(0.25);`.
  * **Textures**: Both `Texture2D` and `TextureCube` are supported. Use the same syntax as you would for declaring a texture in HLSL.

Parameters can have attributes that define default value and other meta data for the editor:
* `@Default(<VALUE_TYPE>)`: Can be used on constants and textures to define the default value.
* `@Clamp(0.0, 1.0)`: Usable on float and int parameters, this can be used to clamp the value the user can set in the editor to a fixed range. 


#### `MATERIALCONFIG`: This section controls when a material is rendered during a frame
This is done by changing the *RenderDataCategory* with a line like this: `RenderDataCategory = LitOpaque`. You can use the preprocessor to change the value depending on some permutation variable, if neccessary. The valid values for `RenderDataCategory` are defined in code via `ezRenderData::RegisterCategory`. Commonly used values are `LitOpaque` for opaque materials, `LitMasked` for alpha-tested materials and `LitTransparent` for alpha blended materials.



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

### *SHADER stages

Each shader stage has its own section. The following stages are supported: `VERTEXSHADER`, `HULLSHADER`, `DOMAINSHADER`, `GEOMETRYSHADER`, `PIXELSHADER` and `COMPUTESHADER`. Even if you define a shader section, you can use the preprocessor to remove its content via permutation variables, allowing you to remove stages from certain permutations.

The entry point into each stage must be called `main`. The shader code supports preprocessor macros that are defined by [permutation variables](shader-permutation-variables.md) as well as include directives.
Beyond that, any HLSL code is fine as long as it compiles on the [platforms](#platforms) the shader defines. However, when defining resources, special care must be taken to ensure no conflicting resource mappings are created between the stages. Please refer to the [shader resource](shader-resources.md) page for further details and on how to facilitate interop with the C++ code.

### TEMPLATE_VARS

This section is only used when [creating a shader template](shader-templates.md#adding-a-shader-template).

## See Also

* [Shader Render State](shader-render-state.md)
* [Shader Permutation Variables](shader-permutation-variables.md)
* [Shader Resources](shader-resources.md)
* [Shader Templates](shader-templates.md)
* [ShaderCompiler](../../tools/shadercompiler.md)
* [Render Pipeline](../render-pipeline/render-pipeline-overview.md)
