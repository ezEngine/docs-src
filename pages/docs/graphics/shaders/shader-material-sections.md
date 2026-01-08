# Material Sections

Material shaders are special and require further sections expose parameters to the engine and editor.

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

## `MATERIALCONSTANTS`: This sections defines per-material constants
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

## `MATERIALPARAMETER`: What parameters to expose on a material in the editor
There are three categories:
  * **Permutation variables**: Add the name of a permutation variable to expose it to the user in the editor. This is explained in detail in [exposing permutation variables to materials](shader-permutation-variables.md#exposing-permutations-to-materials).
  * **Material constants**: To expose, these need to match exactly the name that was used in the `MATERIALCONSTANTS` section described above. Note that the type changes from the macro name to the HLSL name, e.g. `FLOAT1(MaskThreshold);` becomes `float MaskThreshold @Default(0.25);`.
  * **Textures**: Both `Texture2D` and `TextureCube` are supported. Use the same syntax as you would for declaring a texture in HLSL.

Parameters can have attributes that define default value and other meta data for the editor:
* `@Default(<VALUE_TYPE>)`: Can be used on constants and textures to define the default value.
* `@Clamp(0.0, 1.0)`: Usable on float and int parameters, this can be used to clamp the value the user can set in the editor to a fixed range.


## `MATERIALCONFIG`: This section controls when a material is rendered during a frame
This is done by changing the *RenderDataCategory* with a line like this: `RenderDataCategory = LitOpaque`. You can use the preprocessor to change the value depending on some permutation variable, if neccessary. The valid values for `RenderDataCategory` are defined in code via `ezRenderData::RegisterCategory`. Commonly used values are `LitOpaque` for opaque materials, `LitMasked` for alpha-tested materials and `LitTransparent` for alpha blended materials.

## See Also

* [Shaders](shaders-overview.md)
* [Shader Permutation Variables](shader-permutation-variables.md)
