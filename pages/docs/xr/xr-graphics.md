# XR Graphics

XR needs to render two images, one for each eye. Therefore, special care needs to be taken when authoring shaders to make sure they support stereo rendering.

## Material Shaders

To make a material shader work with stereo rendering, it must contain the following sections:

```cpp
[PERMUTATIONS]
// Will be set to CAMERA_MODE_STEREO.
CAMERA_MODE

// Defined if the GPU supports setting the render target array index in the vertex shader. If not, a geometry shader will be used.
VERTEX_SHADER_RENDER_TARGET_ARRAY_INDEX

[VERTEXSHADER]
#include <Shaders/Materials/MaterialVertexShader.h>

VS_OUT main(VS_IN Input)
{
  // FillVertexData will set s_ActiveCameraEyeIndex to either 0 or 1. s_ActiveCameraEyeIndex is used in all camera related functions to pull in the correct eye projection / transform etc.
  VS_OUT Output = FillVertexData(Input);
  //...
  return Output;
}

[GEOMETRYSHADER]
// Will only be active if VERTEX_SHADER_RENDER_TARGET_ARRAY_INDEX is not supported.
#include <Shaders/Materials/MaterialStereoGeometryShader.h>

[PIXELSHADER]
// If you use the default MaterialPixelShader.h and just implement GetDiffuseColor() etc then all stereo rendering is done for you. If you write a custom pixel shader, you will need to add this at the start:
//  #if CAMERA_MODE == CAMERA_MODE_STEREO
//    s_ActiveCameraEyeIndex = Input.RenderTargetArrayIndex;
//  #endif
#include <Shaders/Materials/MaterialPixelShader.h>

```

## Postprocessing Shaders

Post-processing shaders are a bit more complicated than material shaders as they usually pull in data from a previous render pipeline pass which will now be an array texture as the input will be stereo as well. Here is a small example of a full-screen render pass and what it requires in order to work in stereo mode:

```cpp
[PERMUTATIONS]
// Will be set to CAMERA_MODE_STEREO.
CAMERA_MODE

// Defined if the GPU supports setting the render target array index in the vertex shader. If not, a geometry shader will be used.
VERTEX_SHADER_RENDER_TARGET_ARRAY_INDEX

[VERTEXSHADER]
#include <Shaders/Pipeline/FullscreenTriangleVertexShader.h>

[GEOMETRYSHADER]
// Will only be active if VERTEX_SHADER_RENDER_TARGET_ARRAY_INDEX is not supported.
#include <Shaders/Pipeline/FullscreenTriangleStereoGeometryShader.h>

[PIXELSHADER]
#include <Shaders/Pipeline/FullscreenTriangleInterpolator.h>

// Note that this will work fine in non-stereo rendering as well as 2D textures are just 2D-array texture with very few slices.
Texture2DArray Input;

float4 main(PS_IN input) : SV_Target
{
  // To make all camera related functions work correctly, this must be called at the very start to define the right eye.
  #if CAMERA_MODE == CAMERA_MODE_STEREO
    s_ActiveCameraEyeIndex = Input.RenderTargetArrayIndex;
  #endif

  float4 res = Input.Sample(LinearClampSampler, float3(input.TexCoord0, s_ActiveCameraEyeIndex));
  //...
  return res;
}
```