# Shaders Resources

Shader resources are things like textures, samplers constant buffers etc. that need to be separately bound in the renderer for the shader to function. Each resource must be bound to a set and slot. Depending on the [platform](./shaders-overview.md#platforms) used, the requirements for this binding can be very different. E.g. in Vulkan slot assignments must be unique within a set across all stages while in DX11 most slots only need to be unique within a stage. Not following these rules will result in a runtime error. Manually assigning slots is an option but is very tedious. To make this easier, the shader system can automate this process provided some constraints are met how resourced are declared.

1. Currently, EZ does not support arrays of resources like `Texture2D Diffuse[3]` in its shaders.
2. Resources must have unique names across all shader stages. The same resource name can be used in multiple stages as long as the resource it maps to is exactly the same.

## Resource Binding

The shader system only supports the DX11 / DX12 [register syntax](https://learn.microsoft.com/windows/win32/direct3d12/resource-binding-in-hlsl) for resource binding. Both the set and slot can be bound. If no set is given, it is implicitly set 0. Here is a list of a few examples of how to bind resources properly:

```cpp
Texture2D Diffuse : register(t3, space1); // DX12 syntax, slot 3, set 1
SamplerState MySampler : register(s4); // DX11 syntax slot 4, set 0 (default)
ByteAddressBuffer MyBuffer BIND_RESOURCE(SLOT_AUTO, SET_RENDER_PASS); // Slot Auto, set 1
ByteAddressBuffer MyBuffer2 BIND_SET(SET_RENDER_PASS); // Slot Auto, set 1

CONSTANT_BUFFER(ezTestPositions, 1) // Slot 1, set 0 (default)
{
  ...
};

CONSTANT_BUFFER2(ezTestPositions, SLOT_AUTO, SET_MATERIAL) // Slot Auto, set 2
{
  ...
};
```

The HLSL `register` syntax is a bit impractical, so the macros `BIND_RESOURCE(Slot, Set)` and `BIND_SET(Set)` were introduced. These will generate invalid HLSL code which the shader compiler will eventually parse, organize and patch to do the correct thing on each platform. In most cases, you should only be concerned about deciding in which set a resource should reside in. Either use the macro `SLOT_AUTO` when setting a slot or just use the `BIND_SET` macro which omits the slot entirely. While you can set any integer for the set, some platforms like Vulkan have a limit on how many sets can be managed at the same time with a minimum of four. EZ defines macros for these four sets: `SET_FRAME`, `SET_RENDER_PASS`, `SET_MATERIAL` and `SET_DRAW_CALL`. Resources should ideally be bound to these sets according to their update frequency.


## Constant Buffers

Constant buffers map to `ezGALShaderResourceType::ConstantBuffer` in C++.
To facilitate C++ interop, constant buffers should be placed into a separate header file that looks like this:

```cpp
#pragma once
#include <Shaders/Common/ConstantBufferMacros.h>

CONSTANT_BUFFER(ezTestPositions, 3)
{
  FLOAT4(Vertex0);
  FLOAT4(Vertex1);
  FLOAT4(Vertex2);
};
```
By using the macros defined in **ConstantBufferMacros.h** like `CONSTANT_BUFFER` and the data types like `FLOAT4`, the file can be included in both shader and C++ code. This makes it easy to create an instance of the constant buffer as a C++ struct in code to update it. Care must be taken to ensure that the constant buffer has the same layout in C++ and HLSL though:
1. Make sure that the size of your struct is a multiple of 16 bytes. Fill out any missing bytes with dummy `FLOAT1` entries.
2. A `FLOAT3` can't be followed by another `FLOAT3`. It should be followed by a `FLOAT1` first or some other types of the same byte counts to ensure the next `FLOAT3` starts at a 16 byte boundary. This is necessary as the layout rules are different between HLSL and C++.

## Push Constants

Push constants map to `ezGALShaderResourceType::PushConstants` in C++. Push constants allow for fast updates of a small set of bytes. Usually at least 128 bytes. You can check `ezGALDeviceCapabilities::m_uiMaxPushConstantsSize` for the max push constant buffer size. On platforms that don't support push constants like DX11, this is emulated via a constant buffer. Only one push constants block is supported across all shader stages of a shader. Like with constant buffers, special macros have to be used and the declaration should be put into a separate header so it can be included in both shader and C++ code:

```cpp
// Header:
#pragma once
#include <Shaders/Common/ConstantBufferMacros.h>

BEGIN_PUSH_CONSTANTS(ezTestData)
{
  FLOAT4(VertexColor);
  FLOAT4(Vertex0);
  FLOAT4(Vertex1);
  FLOAT4(Vertex2);
}
END_PUSH_CONSTANTS(ezTestData)

// Shader:
float4 main(VS_OUT a) : SV_Target
{
  return GET_PUSH_CONSTANT(ezTestData, VertexColor);
}

// C++:
ezTestData constants;
constants.VertexColor = ...;
pContext->SetPushConstants("ezTestData", constants);
```

The `BEGIN_PUSH_CONSTANTS` and `END_PUSH_CONSTANTS` macros define the struct. Unlike with constant buffers, you can't simply access the values inside a shader by just the name of the variable, e.g. `VertexColor`. This is because depending on the platform, a different syntax needs to be used to access the content. To make the same shader compile on all platforms, you need to use the `GET_PUSH_CONSTANT(Name, Constant)` macro to access a member of the push constant buffer.

## Samplers

Samplers map to `ezGALShaderResourceType::Sampler` or `ezGALShaderResourceType::TextureAndSampler` in C++. Two types of samplers are supported: `SamplerState` and `SamplerComparisonState`. The naming of the samplers is important, as it can be used to optimize your workflow. ezEngine has a concept of immutable Samplers, these samplers are automatically bound so you can use them in the shader without needing to define them in C++. Immutable samplers are registered in code via `ezGALImmutableSamplers::RegisterImmutableSampler`. Currently, these samplers are registered: `LinearSampler`, `LinearClampSampler`, `PointSampler` and `PointClampSampler`.

ezEngine does not allow for two different resources to have the same name, the only exception is textures and samplers which can have the same name by calling the sampler *NAME_AutoSampler*. The compiler will rename the sampler to *NAME* and on platforms that support combined image samplers both will be combined into a single resource of type `ezGALShaderResourceType::TextureAndSampler`. The benefit of this approach is that when binding a texture resource to a material for example, the texture resource can define both the texture as well as the sampler state, binding both to the same name.

```cpp
SamplerState DiffuseSampler;
SamplerComparisonState ShadowSampler;
// Auto sampler combines with texture of the same name: 
Texture2D BaseTexture;
SamplerState BaseTexture_AutoSampler;
```

## Textures

Textures map to `ezGALShaderResourceType::Texture` or `ezGALShaderResourceType::TextureAndSampler` in C++ (see samplers above). ezEngine supports all HLSL texture types except for 1D textures. You can work around this by creating 1xN 2DTextures.

```cpp
Texture1D texture1D; // 1D textures currently not supported.
Texture1DArray texture1DArray; // 1D textures currently not supported.
Texture2D texture2D;
Texture2DArray texture2DArray;
Texture2DMS<float4> texture2DMS;
Texture2DMSArray<float4> texture2DMSArray;
Texture3D texture3D;
TextureCube textureCube;
TextureCubeArray textureCubeArray;
```

Read-write variants are also supported and map to `ezGALShaderResourceType::TextureRW` in C++.

```cpp
RWTexture1D<float> rwTexture1D; // 1D textures currently not supported.
RWTexture1DArray<float2> rwTexture1DArray; // 1D textures currently not supported.
RWTexture2D<float3> rwTexture2D;
RWTexture2DArray<float4> rwTexture2DArray;
RWTexture3D<uint> rwTexture3D;
```

## Buffers

There are three types of buffers supported by EZ:
1. HLSL's `Buffer<T>` type is very similar to a 1D texture. A buffer of the same type T needs to be bound to the resource. Maps to `ezGALShaderResourceType::TexelBuffer` in C++.
2. `StructuredBuffer<T>` should follow the same rules as for constant buffers: Put the declaration in a separate header file to allow access to it from C++ and ensure each struct is 16 bytes aligned. Maps to `ezGALShaderResourceType::StructuredBuffer` in C++.
3. `ByteAddressBuffer` in just an array of bytes. A raw buffer needs to be bound to the resource. With HLSL 5.1, you can cast any offset of the buffer into a struct. Maps to `ezGALShaderResourceType::StructuredBuffer` in C++.

```cpp
// Header:
#pragma once
#include <Shaders/Common/ConstantBufferMacros.h>

struct EZ_SHADER_STRUCT PerInstanceData
{
  TRANSFORM(ObjectToWorld);
};

// Shader:
Buffer<uint> buffer;
StructuredBuffer<PerInstanceData> structuredBuffer;
ByteAddressBuffer byteAddressBuffer;
```

Read-write variants of these buffers are also supported and map to `ezGALShaderResourceType::TexelBufferRW` and `ezGALShaderResourceType::StructuredBufferRW` respectively.

```cpp
RWBuffer<uint> rwBuffer;
RWStructuredBuffer<ezPerInstanceData> rwStructuredBuffer;
RWByteAddressBuffer rwByteAddressBuffer;
```

## Append / Consume Buffers

TODO: Future work: Append / consume buffers can be defined in shaders and are correctly reflected, but EZ does not support binding resources to them right now.

```cpp
// Header:
#pragma once
#include <Shaders/Common/ConstantBufferMacros.h>

struct EZ_SHADER_STRUCT ezAppendData
{
  FLOAT2(Value);
};

// Shader:
AppendStructuredBuffer<ezAppendData> appendStructuredBuffer;
ConsumeStructuredBuffer<ezAppendData> consumeStructuredBuffer;
```

## See Also

* [Shaders](shaders-overview.md)
* [ShaderCompiler](../../tools/shadercompiler.md)
