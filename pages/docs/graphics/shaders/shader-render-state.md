# Shader Render State

The state of the [rendering pipeline](../render-pipeline/render-pipeline-overview.md) can only be set through [shaders](shaders-overview.md). There is no way to change its state other than to select a shader which includes that specific state.

Use [shader permutations](shader-permutation-variables.md) to create variants of a shader. Each variant may incorporate a different render state. By setting shader permutation variables at runtime, you select the specific shader variant (permutation) and thus also get its render state.

This design follows what rendering APIs such as DirectX 12 and Vulkan require.

## The Shader Render State Section

Each shader is made up of several [sections](shaders-overview.md#shader-sections):

```cpp
[PLATFORMS]

ALL
DEBUG

[PERMUTATIONS]

ALPHATEST
WIREFRAME

[RENDERSTATE]

#if WIREFRAME == 1
  WireFrame = true
#endif

[VERTEXSHADER]

VS_OUT main(VS_IN Input)
{
  ...
}

[PIXELSHADER]

...
```

The render pipeline state associated with the shader is defined in the **[RENDERSTATE]** section. It may use permutation variables just like the shader code. To have different state for different permutations, use standard C preprocessor syntax.

## Render States

The following variables are available in the **[RENDERSTATE]** section. Simply overwrite them with the desired value.

### Rasterizer States

* bool **FrontCounterClockwise** = false

  When `false`, triangles with clockwise winding order are considered front-facing. When `true`, counter-clockwise triangles are front-facing. This affects culling and two-sided stencil operations.

* bool **ScissorTest** = false

  When `true`, fragments outside the scissor rectangle are discarded. The scissor rectangle is set by the rendering code, not the shader.

* bool **WireFrame** = false

  When `true`, renders only the edges of triangles instead of filled polygons. Useful for debugging geometry.

* bool **ConservativeRasterization** = false

  When `true`, a pixel is considered covered if the triangle touches any part of the pixel. This is useful for voxelization and collision detection algorithms.

* enum **CullMode** = CullMode_Back

  ```cpp
  CullMode = CullMode_None   // Render both front and back faces
  CullMode = CullMode_Back   // Don't render back faces (default)
  CullMode = CullMode_Front  // Don't render front faces
  ```

* float **DepthBiasClamp** = 0.0

  Maximum depth bias value. Clamps the computed depth bias to prevent excessive offset.

* float **SlopeScaledDepthBias** = 0.0

  Depth bias that scales with the polygon's slope. Useful for shadow mapping to reduce shadow acne on angled surfaces.

* int **DepthBias** = 0

  Constant depth bias added to each fragment's depth value. Used together with `SlopeScaledDepthBias` for techniques like shadow mapping.

### Depth-Stencil State

#### Depth Testing

* bool **DepthEnable** = true

  When `true`, depth testing is performed. Fragments are compared against the depth buffer using `DepthTestFunc`. For backwards compatibility, `DepthTest` is also supported but deprecated.

* bool **DepthWrite** = true

  When `true`, fragments that pass the depth test write their depth value to the depth buffer. Typically disabled for transparent objects rendered after opaque geometry.

* enum **DepthTestFunc** = CompareFunc_Less

  Comparison function used for depth testing. The fragment passes if this comparison succeeds.

  ```cpp
  DepthTestFunc = CompareFunc_Never         // Never pass (no fragments rendered)
  DepthTestFunc = CompareFunc_Less          // Pass if closer than depth buffer (default)
  DepthTestFunc = CompareFunc_Equal         // Pass if equal to depth buffer
  DepthTestFunc = CompareFunc_LessEqual     // Pass if closer or equal
  DepthTestFunc = CompareFunc_Greater       // Pass if farther than depth buffer
  DepthTestFunc = CompareFunc_NotEqual      // Pass if not equal
  DepthTestFunc = CompareFunc_GreaterEqual  // Pass if farther or equal
  DepthTestFunc = CompareFunc_Always        // Always pass (ignores depth buffer)
  ```

#### Stencil Testing

* bool **StencilEnable** = false

  When `true`, stencil testing is performed. Fragments are compared against the stencil buffer, and operations can modify the stencil buffer based on test results.

* int **StencilReadMask** = 255

  Bitmask applied when reading from the stencil buffer during comparison. Use `255` (all bits) to compare the full stencil value.

* int **StencilWriteMask** = 255

  Bitmask applied when writing to the stencil buffer. Use `255` (all bits) to write the full stencil value.

* int **StencilRefValue** = 0

  The reference value used for stencil comparisons and operations. When comparing, this value (masked by `StencilReadMask`) is compared against the stencil buffer value. When using `StencilOp_Replace`, this value (masked by `StencilWriteMask`) is written to the stencil buffer.

  Set this to `-1` to use a dynamic stencil reference value provided by the rendering code at runtime, rather than the fixed value from the shader.

* bool **UseUserStencilRef** = false

  When `true`, the stencil reference value is provided dynamically by the rendering code at runtime. When `false`, the shader's `StencilRefValue` is used. Setting `StencilRefValue` to `-1` implicitly enables this option.

#### Front-Face Stencil Operations

These operations apply to front-facing polygons (see `FrontCounterClockwise` to configure winding order).

* enum **StencilCompareFunc** = CompareFunc_Always

  Comparison function for stencil testing on front faces.

  ```cpp
  StencilCompareFunc = CompareFunc_Never         // Never pass
  StencilCompareFunc = CompareFunc_Less          // Pass if (ref & mask) < (stencil & mask)
  StencilCompareFunc = CompareFunc_Equal         // Pass if (ref & mask) == (stencil & mask)
  StencilCompareFunc = CompareFunc_LessEqual     // Pass if (ref & mask) <= (stencil & mask)
  StencilCompareFunc = CompareFunc_Greater       // Pass if (ref & mask) > (stencil & mask)
  StencilCompareFunc = CompareFunc_NotEqual      // Pass if (ref & mask) != (stencil & mask)
  StencilCompareFunc = CompareFunc_GreaterEqual  // Pass if (ref & mask) >= (stencil & mask)
  StencilCompareFunc = CompareFunc_Always        // Always pass (default)
  ```

* enum **StencilFailOp** = StencilOp_Keep

  Operation performed when the stencil test fails.

  ```cpp
  StencilFailOp = StencilOp_Keep               // Keep current value (default)
  StencilFailOp = StencilOp_Zero               // Set to 0
  StencilFailOp = StencilOp_Replace            // Replace with reference value
  StencilFailOp = StencilOp_IncrementSaturated // Increment, clamp to max
  StencilFailOp = StencilOp_DecrementSaturated // Decrement, clamp to 0
  StencilFailOp = StencilOp_Invert             // Bitwise invert
  StencilFailOp = StencilOp_Increment          // Increment, wrap to 0
  StencilFailOp = StencilOp_Decrement          // Decrement, wrap to max
  ```

* enum **StencilDepthFailOp** = StencilOp_Keep

  Operation performed when the stencil test passes but the depth test fails.

  ```cpp
  StencilDepthFailOp = StencilOp_Keep
  StencilDepthFailOp = StencilOp_Zero
  StencilDepthFailOp = StencilOp_Replace
  StencilDepthFailOp = StencilOp_IncrementSaturated
  StencilDepthFailOp = StencilOp_DecrementSaturated
  StencilDepthFailOp = StencilOp_Invert
  StencilDepthFailOp = StencilOp_Increment
  StencilDepthFailOp = StencilOp_Decrement
  ```

* enum **StencilPassOp** = StencilOp_Keep

  Operation performed when both stencil and depth tests pass.

  ```cpp
  StencilPassOp = StencilOp_Keep
  StencilPassOp = StencilOp_Zero
  StencilPassOp = StencilOp_Replace
  StencilPassOp = StencilOp_IncrementSaturated
  StencilPassOp = StencilOp_DecrementSaturated
  StencilPassOp = StencilOp_Invert
  StencilPassOp = StencilOp_Increment
  StencilPassOp = StencilOp_Decrement
  ```

#### Back-Face Stencil Operations

These operations apply to back-facing polygons. If not explicitly set, they default to the front-face values, allowing separate stencil operations for two-sided geometry.

* enum **StencilBackFaceCompareFunc** = CompareFunc_Always

  Comparison function for stencil testing on back faces. Falls back to `StencilCompareFunc` if not set.

  ```cpp
  StencilBackFaceCompareFunc = CompareFunc_Never
  StencilBackFaceCompareFunc = CompareFunc_Less
  StencilBackFaceCompareFunc = CompareFunc_Equal
  StencilBackFaceCompareFunc = CompareFunc_LessEqual
  StencilBackFaceCompareFunc = CompareFunc_Greater
  StencilBackFaceCompareFunc = CompareFunc_NotEqual
  StencilBackFaceCompareFunc = CompareFunc_GreaterEqual
  StencilBackFaceCompareFunc = CompareFunc_Always
  ```

* enum **StencilBackFaceFailOp** = StencilOp_Keep

  Operation when stencil test fails on back faces. Falls back to `StencilFailOp` if not set.

  ```cpp
  StencilBackFaceFailOp = StencilOp_Keep
  StencilBackFaceFailOp = StencilOp_Zero
  StencilBackFaceFailOp = StencilOp_Replace
  StencilBackFaceFailOp = StencilOp_IncrementSaturated
  StencilBackFaceFailOp = StencilOp_DecrementSaturated
  StencilBackFaceFailOp = StencilOp_Invert
  StencilBackFaceFailOp = StencilOp_Increment
  StencilBackFaceFailOp = StencilOp_Decrement
  ```

* enum **StencilBackFaceDepthFailOp** = StencilOp_Keep

  Operation when stencil passes but depth fails on back faces. Falls back to `StencilDepthFailOp` if not set.

  ```cpp
  StencilBackFaceDepthFailOp = StencilOp_Keep
  StencilBackFaceDepthFailOp = StencilOp_Zero
  StencilBackFaceDepthFailOp = StencilOp_Replace
  StencilBackFaceDepthFailOp = StencilOp_IncrementSaturated
  StencilBackFaceDepthFailOp = StencilOp_DecrementSaturated
  StencilBackFaceDepthFailOp = StencilOp_Invert
  StencilBackFaceDepthFailOp = StencilOp_Increment
  StencilBackFaceDepthFailOp = StencilOp_Decrement
  ```

* enum **StencilBackFacePassOp** = StencilOp_Keep

  Operation when both tests pass on back faces. Falls back to `StencilPassOp` if not set.

  ```cpp
  StencilBackFacePassOp = StencilOp_Keep
  StencilBackFacePassOp = StencilOp_Zero
  StencilBackFacePassOp = StencilOp_Replace
  StencilBackFacePassOp = StencilOp_IncrementSaturated
  StencilBackFacePassOp = StencilOp_DecrementSaturated
  StencilBackFacePassOp = StencilOp_Invert
  StencilBackFacePassOp = StencilOp_Increment
  StencilBackFacePassOp = StencilOp_Decrement
  ```

### Blend State

* bool **AlphaToCoverage** = false

  When `true`, uses the alpha channel to determine per-pixel coverage in MSAA rendering. Useful for rendering foliage and other alpha-tested geometry with smoother edges.

* bool **IndependentBlend** = false

  When `true`, each render target (0-7) can have independent blend settings. When `false`, all render targets use the settings from render target 0.

#### Per-Render-Target Blend Settings

The following variables configure blending for individual render targets. You can specify them without a suffix (e.g., `BlendingEnabled`) to configure render target 0, or with a suffix 0-7 (e.g., `BlendingEnabled0`, `BlendingEnabled1`) to configure specific targets.

When **IndependentBlend** is `false`, all render targets use the settings from target 0.

* bool **BlendingEnabled** = false

  When `true`, enables blending for this render target. The source color from the pixel shader is combined with the destination color in the render target using the blend operation and factors.

* enum **BlendOp** = BlendOp_Add

  The operation used to combine source and destination RGB values.

  ```cpp
  BlendOp = BlendOp_Add         // result = src + dest (default)
  BlendOp = BlendOp_Subtract    // result = src - dest
  BlendOp = BlendOp_RevSubtract // result = dest - src
  BlendOp = BlendOp_Min         // result = min(src, dest)
  BlendOp = BlendOp_Max         // result = max(src, dest)
  ```

* enum **BlendOpAlpha** = BlendOp_Add

  The operation used to combine source and destination alpha values. Often the same as `BlendOp`.

  ```cpp
  BlendOpAlpha = BlendOp_Add
  BlendOpAlpha = BlendOp_Subtract
  BlendOpAlpha = BlendOp_RevSubtract
  BlendOpAlpha = BlendOp_Min
  BlendOpAlpha = BlendOp_Max
  ```

* enum **SourceBlend** = Blend_One

  Factor applied to the source RGB color before blending.

  ```cpp
  SourceBlend = Blend_Zero              // (0, 0, 0)
  SourceBlend = Blend_One               // (1, 1, 1) - use source color as-is (default)
  SourceBlend = Blend_SrcColor          // (Rs, Gs, Bs)
  SourceBlend = Blend_InvSrcColor       // (1-Rs, 1-Gs, 1-Bs)
  SourceBlend = Blend_SrcAlpha          // (As, As, As) - common for transparency
  SourceBlend = Blend_InvSrcAlpha       // (1-As, 1-As, 1-As)
  SourceBlend = Blend_DestAlpha         // (Ad, Ad, Ad)
  SourceBlend = Blend_InvDestAlpha      // (1-Ad, 1-Ad, 1-Ad)
  SourceBlend = Blend_DestColor         // (Rd, Gd, Bd)
  SourceBlend = Blend_InvDestColor      // (1-Rd, 1-Gd, 1-Bd)
  SourceBlend = Blend_SrcAlphaSaturated // (f, f, f) where f = min(As, 1-Ad)
  SourceBlend = Blend_BlendFactor       // Constant blend factor
  SourceBlend = Blend_InvBlendFactor    // 1 - constant blend factor
  ```

* enum **DestBlend** = Blend_One

  Factor applied to the destination RGB color (current render target value) before blending.

  ```cpp
  DestBlend = Blend_Zero              // (0, 0, 0) - ignore destination
  DestBlend = Blend_One               // (1, 1, 1) - use destination as-is (default)
  DestBlend = Blend_SrcColor          // (Rs, Gs, Bs)
  DestBlend = Blend_InvSrcColor       // (1-Rs, 1-Gs, 1-Bs) - common for transparency
  DestBlend = Blend_SrcAlpha          // (As, As, As)
  DestBlend = Blend_InvSrcAlpha       // (1-As, 1-As, 1-As)
  DestBlend = Blend_DestAlpha         // (Ad, Ad, Ad)
  DestBlend = Blend_InvDestAlpha      // (1-Ad, 1-Ad, 1-Ad)
  DestBlend = Blend_DestColor         // (Rd, Gd, Bd)
  DestBlend = Blend_InvDestColor      // (1-Rd, 1-Gd, 1-Bd)
  DestBlend = Blend_SrcAlphaSaturated // (f, f, f) where f = min(As, 1-Ad)
  DestBlend = Blend_BlendFactor       // Constant blend factor
  DestBlend = Blend_InvBlendFactor    // 1 - constant blend factor
  ```

* enum **SourceBlendAlpha** = Blend_One

  Factor applied to the source alpha value before blending.

  ```cpp
  SourceBlendAlpha = Blend_Zero
  SourceBlendAlpha = Blend_One
  SourceBlendAlpha = Blend_SrcColor
  SourceBlendAlpha = Blend_InvSrcColor
  SourceBlendAlpha = Blend_SrcAlpha
  SourceBlendAlpha = Blend_InvSrcAlpha
  SourceBlendAlpha = Blend_DestAlpha
  SourceBlendAlpha = Blend_InvDestAlpha
  SourceBlendAlpha = Blend_DestColor
  SourceBlendAlpha = Blend_InvDestColor
  SourceBlendAlpha = Blend_SrcAlphaSaturated
  SourceBlendAlpha = Blend_BlendFactor
  SourceBlendAlpha = Blend_InvBlendFactor
  ```

* enum **DestBlendAlpha** = Blend_One

  Factor applied to the destination alpha value before blending.

  ```cpp
  DestBlendAlpha = Blend_Zero
  DestBlendAlpha = Blend_One
  DestBlendAlpha = Blend_SrcColor
  DestBlendAlpha = Blend_InvSrcColor
  DestBlendAlpha = Blend_SrcAlpha
  DestBlendAlpha = Blend_InvSrcAlpha
  DestBlendAlpha = Blend_DestAlpha
  DestBlendAlpha = Blend_InvDestAlpha
  DestBlendAlpha = Blend_DestColor
  DestBlendAlpha = Blend_InvDestColor
  DestBlendAlpha = Blend_SrcAlphaSaturated
  DestBlendAlpha = Blend_BlendFactor
  DestBlendAlpha = Blend_InvBlendFactor
  ```

* int **ColorWriteMask** = 255

  Bitmask controlling which color channels are written to the render target. Use `255` to write all channels (RGBA), or combine bits: R=1, G=2, B=4, A=8. For example, use `7` to write only RGB (1+2+4). The deprecated name `WriteMask` is also supported.

## Common Configuration Examples

### Standard Alpha Blending (Transparency)

For typical transparent objects:

```cpp
[RENDERSTATE]

BlendingEnabled = true
SourceBlend = Blend_SrcAlpha
DestBlend = Blend_InvSrcAlpha
DepthWrite = false  // Don't write to depth buffer for transparent objects
```

### Additive Blending (Particles, Effects)

For light-emitting particles and effects:

```cpp
[RENDERSTATE]

BlendingEnabled = true
SourceBlend = Blend_One
DestBlend = Blend_One
BlendOp = BlendOp_Add
DepthWrite = false
```

### Wireframe Rendering

For debugging mesh geometry:

```cpp
[RENDERSTATE]

WireFrame = true
CullMode = CullMode_None  // Show both front and back faces
```

### Depth Pre-Pass

For early depth rejection optimization:

```cpp
[RENDERSTATE]

DepthEnable = true
DepthWrite = true
ColorWriteMask = 0  // Only write depth, no color output
```

## See Also

* [Shaders](shaders-overview.md)
* [Shader Permutation Variables](shader-permutation-variables.md)
* [Shader Templates](shader-templates.md)
* [Render Pipeline](../render-pipeline/render-pipeline-overview.md)
