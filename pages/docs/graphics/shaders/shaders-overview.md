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

Material shaders are special and require additional sections to expose parameters to the engine and editor. The three dedicated sections are `MATERIALCONSTANTS`, `MATERIALPARAMETER`, and `MATERIALCONFIG`.

See [Shader Material Sections](shader-material-sections.md) for full documentation.

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

* [Shader Material Sections](shader-material-sections.md)
* [Shader Render State](shader-render-state.md)
* [Shader Permutation Variables](shader-permutation-variables.md)
* [Shader Resources](shader-resources.md)
* [ShaderCompiler](../../tools/shadercompiler.md)
* [Render Pipeline](../render-pipeline/render-pipeline-overview.md)
