# Shaders Resources

Shader resources are things like textures, samplers constant buffers etc. that need to be separately bound in the renderer for the shader to function. Each resource must be bound to a bind group and slot. Depending on the [platform](shaders-overview.md#platforms) used, the requirements for this binding can be very different. E.g. in Vulkan slot assignments must be unique within a bind group (Vulkan descriptor set) across all stages while in DX11 most slots only need to be unique within a stage. Not following these rules will result in a runtime error. Manually assigning slots is an option but is very tedious. To make this easier, the shader system can automate this process provided some constraints are met how resourced are declared.

1. Currently, EZ does not support arrays of resources like `Texture2D Diffuse[3]` in its shaders.
2. Resources must have unique names across all shader stages. The same resource name can be used in multiple stages as long as the resource it maps to is exactly the same.
3. Only four bind groups are supported (DX12 register space, Vulkan descriptor set).

## Resource Binding

The shader system only supports the DX11 / DX12 [register syntax](https://learn.microsoft.com/windows/win32/direct3d12/resource-binding-in-hlsl) for binding resources to bind groups. Both the bind group and slot can be bound. If no bind group is given, it is implicitly set to 0.

EZ uses the following bind groups - resources should ideally be bound to these sets according to their update frequency:
* **BG_FRAME (0)**: Should only contain resources that are set only once per frame or once per view. 
* **BG_RENDER_PASS (1)**: Resources that are unqiue to a render pass. Also use it for small shaders that e.g. do some image processing within a render pass.
* **BG_MATERIAL (2)**: This group is normally occupied by the material resources. If a material exposes a resource like a texture, it must be put into this bind group.
* **BG_DRAW_CALL (3)**: Resources that change every few draw calls should go in here.

Here is a list of a few examples of how to bind resources properly:

```cpp
Texture2D Diffuse : register(t3, space1); // DX12 syntax, slot 3, bind group 1
SamplerState MySampler : register(s4); // DX11 syntax slot 4, bind group 0 (default)
ByteAddressBuffer MyBuffer BIND_RESOURCE(SLOT_AUTO, BG_RENDER_PASS); // Slot Auto, bind group 1
ByteAddressBuffer MyBuffer2 BIND_GROUP(BG_RENDER_PASS); // Slot Auto, bind group 1

CONSTANT_BUFFER(ezTestPositions, 1) // Slot 1, bind group 0 (default)
{
  ...
};

CONSTANT_BUFFER2(ezTestPositions, SLOT_AUTO, BG_MATERIAL) // Slot Auto, bind group 2
{
  ...
};
```

The HLSL `register` syntax is a bit impractical, so the macros `BIND_RESOURCE(Slot, BindGroup)` and `BIND_GROUP(BindGroup)` were introduced. These will generate invalid HLSL code which the shader compiler will eventually parse, organize and patch to do the correct thing on each platform. In most cases, you should only be concerned about deciding in which bind group a resource should reside in. Either use the macro `SLOT_AUTO` when setting a slot or just use the `BIND_GROUP` macro which omits the slot entirely.

### C++ resource binding

Before a shader can be used to render something, all the resources need to be bound to their respective bind groups. This is happening automatically for material resources but for custom shaders used in e.g. a custom render pass, this has to be done manually. To access the individual bind groups, use the following code:
```cpp
// By default, GetBindGroup uses `EZ_GAL_BIND_GROUP_FRAME`.
ezBindGroupBuilder& bindGroup = ezRenderContext::GetDefaultInstance()->GetBindGroup();
ezBindGroupBuilder& bindGroupRenderPass = ezRenderContext::GetDefaultInstance()->GetBindGroup(EZ_GAL_BIND_GROUP_RENDER_PASS);
ezBindGroupBuilder& bindGroupMaterial = ezRenderContext::GetDefaultInstance()->GetBindGroup(EZ_GAL_BIND_GROUP_MATERIAL);
ezBindGroupBuilder& bindGroupDraw = ezRenderContext::GetDefaultInstance()->GetBindGroup(EZ_GAL_BIND_GROUP_DRAW_CALL);
```

When binding a resource, it is sufficient to only provide the resource name and GAL handle to bind the entire resource. If you want to bind only a subset of the resource, you can use `ezGALTextureRange` or `ezGALBufferRange` like this:

```cpp
ezGALTextureRange textureRange;
textureRange.m_uiBaseMipLevel = uiMipMapIndex;
textureRange.m_uiBaseArraySlice = m_uiSpecularOutputIndex * 6;
textureRange.m_uiArraySlices = 6;
bindGroup.BindTexture("ReflectionOutput", pFilteredSpecularOutput->m_TextureHandle, textureRange);
// Or as a shorter form:
bindGroup.BindTexture("ReflectionOutput", pFilteredSpecularOutput->m_TextureHandle, {m_uiSpecularOutputIndex * 6, 6, uiMipMapIndex, EZ_GAL_ALL_MIP_LEVELS});
```

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
3. `ByteAddressBuffer` in just an array of bytes. A raw buffer needs to be bound to the resource. With HLSL 5.1, you can cast any offset of the buffer into a struct. Maps to `ezGALShaderResourceType::ByteAddressBuffer` in C++.

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

Read-write variants of these buffers are also supported and map to `ezGALShaderResourceType::TexelBufferRW`, `ezGALShaderResourceType::StructuredBufferRW` and `ezGALShaderResourceType::ByteAddressBufferRW` respectively.

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
