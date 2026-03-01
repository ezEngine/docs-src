# Render Pipeline Passes

This page lists all render pipeline *passes* and their functionality.

## AO Pass

Generates a screen-space ambient occlusion (SSAO) texture from the depth buffer. The effect darkens crevices and contact areas to simulate indirect lighting occlusion.

**Properties:**

* `Radius`: World-space sampling radius.
* `MaxScreenSpaceRadius`: Clamps the radius in screen space to avoid sampling too large an area on nearby geometry.
* `Contrast`: Sharpens or softens the occlusion effect.
* `Intensity`: Overall strength of the darkening.
* `FadeOutStart`, `FadeOutEnd`: World-space distances between which the effect is blended out. Beyond `FadeOutEnd` the occlusion is zero.
* `PositionBias`: Small offset along the normal to reduce self-occlusion artefacts.
* `MipLevelScale`: Controls which mip level is sampled at different distances.
* `DepthBlurThreshold`: Depth difference at which bilateral filtering stops blurring across edges.

**Required Extractor:** [Visible Objects Extractor](render-pipeline-extractors.md#visible-objects-extractor)

## Antialiasing Pass

Post-process anti-aliasing pass. Performs an advanced resolve of MSAA render targets using a two-pixel-wide B-spline filter. No configurable properties.

## Blend Pass

Linearly interpolates between two input textures and writes the result to the output.

**Properties:**

* `BlendFactor`: `0` outputs Input A unchanged, `1` outputs Input B, intermediate values blend between them.

## Bloom Pass

Extracts overbright pixels from the image, blurs them, and writes the result to a separate render target. The bloom image is usually fed into the [Tonemap Pass](#tonemap-pass) to be composited on top of the final image.

**Properties:**

* `Radius`: Blur spread of the bloom effect.
* `Threshold`: Luminance value above which pixels contribute to bloom.
* `Intensity`: Overall brightness of the bloom output.
* `InnerTintColor`, `MidTintColor`, `OuterTintColor`: Color tints applied to the inner, middle, and outer bloom regions, allowing colored glow effects.

## Blur Pass

Applies a separable Gaussian blur to the input texture.

**Properties:**

* `Radius`: Blur kernel radius in pixels.

## Copy Texture Pass

Copies a texture from input to output verbatim. Useful to preserve an intermediate result for later use in the pipeline.

## Custom Render Data Pass

A flexible pass that renders all [render data](render-pipeline-overview.md) belonging to a user-specified *render data category*. This allows rendering custom objects at a precise point in the pipeline, between standard passes, without creating an entirely new pass type.

This is used in the default pipelines to create three named hook points:

* **InitDepth** — runs before the depth pre-pass, using `ByDepthOffsetOnly` sorting. Use it to prime the depth or stencil buffer.
* **InitLit** — runs before the opaque forward pass, using `ByDepthOffsetOnly` sorting. Use it to write initial data into the lit render target.
* **LitScreenFX** — runs after all geometry forward passes but before post-processing and tonemapping, using `BackToFrontThenByRenderData` sorting. Use it for full-screen or world-space screen effects that must appear on top of geometry but below post-process.

**Properties:**

* `RenderDataCategoryName`: The name of the render data category to collect and render.
* `SortingFunction`: How render data is ordered before rendering. Options: `ByRenderDataThenFrontToBack`, `BackToFrontThenByRenderData`, `ByDepthOffsetOnly`. See [Sorting Functions](#sorting-functions) below.

## Depth Only Pass

Renders geometry into a depth buffer without producing any color output. Used for depth pre-passes and shadow map generation.

**Properties:**

* `RenderStaticObjects`: Whether static geometry is included.
* `RenderDynamicObjects`: Whether dynamic geometry is included.
* `RenderTransparentObjects`: Whether transparent geometry is included (off by default).

**Required Extractor:** [Visible Objects Extractor](render-pipeline-extractors.md#visible-objects-extractor)

## History Source Pass

Provides access to a render target from the *previous* frame. Always used in combination with a [History Target Pass](#history-target-pass). On the first frame the render target is cleared to `ClearColor`.

**Properties:**

* `Format`: Pixel format of the history buffer.
* `MsaaMode`: MSAA sample count.
* `ClearColor`: Color used to clear the buffer on the first frame.

## History Target Pass

Captures the current frame's input and stores it so the [History Source Pass](#history-source-pass) can expose it next frame.

**Properties:**

* `SourcePassName`: Name of the corresponding `HistorySourcePass` node in the graph.

## LSAO Pass

Implements *Line Sweep Ambient Occlusion* (LSAO), an alternative SSAO algorithm that sweeps line samples across the screen instead of sampling a hemisphere. Based on the technique from *Quantum Break*.

**Properties:**

* `LineToLinePixelOffset`: Pixel distance between adjacent sweep lines.
* `LineSamplePixelOffsetFactor`: Step size along each sweep line.
* `OcclusionFalloff`: Rate at which occlusion contribution falls off with distance.
* `DepthCutoffDistance`: World-space depth difference beyond which two points are considered unrelated.
* `DepthCompareFunction`: How depth is evaluated when gathering samples — `Depth` (hard cutoff), `Normal` (plane-weighted), or `NormalAndSampleDistance` (plane and sample-distance weighted).
* `DistributedGathering`: Spreads gather samples across multiple frames to reduce per-frame cost.

## MSAA Resolve Pass

Resolves a multi-sampled render target into a regular texture by averaging the samples. Required before passing MSAA output into passes that cannot process multi-sampled textures.

**Properties:**

* `IsDepth`: Set to `true` when resolving a depth-stencil texture rather than a color texture.

## MSAA Upscale Pass

Converts a regular texture into a multi-sampled render target by replicating each pixel across all samples. Used when transitioning back from non-MSAA post-processing to an MSAA render target.

**Properties:**

* `MsaaMode`: Target MSAA sample count.

## Opaque Forward Render Pass

Forward render pass for opaque geometry. Performs full lighting and shading. Accepts an optional ambient occlusion input from an [AO Pass](#ao-pass) or [LSAO Pass](#lsao-pass).

**Properties:**

* `ShadingQuality`: `Normal` applies full lighting; `Simplified` reduces shading cost for lower-end hardware.
* `WriteDepth`: Whether to write to the depth buffer during this pass (usually `true`).

**Required Extractor:** [Clustered Data Extractor](render-pipeline-extractors.md#clustered-data-extractor)

## Picking Render Pass

Renders object IDs into an off-screen buffer for editor picking functionality.

## Reflection Filter Pass

Pre-filters a cubemap for image-based lighting. Generates a mip chain of specular reflection cubemaps with increasing roughness and computes a diffuse irradiance cubemap, both used for physically-based rendering (PBR) environment lighting.

**Properties:**

* `DiffuseIntensity`: Scale factor for the diffuse irradiance contribution.
* `DiffuseSaturation`: Saturation of the diffuse irradiance colors.
* `SpecularIntensity`: Scale factor for the specular reflection contribution.
* `SpecularOutputIndex`, `IrradianceOutputIndex`: Which output slots the two cubemaps are written to.

## Selection Highlight Pass

Draws a colored outline and translucent overlay around selected objects. Used exclusively in editor pipelines.

**Properties:**

* `HighlightColor`: Outline and overlay color.
* `OverlayOpacity`: Opacity of the fill drawn over the selected object.

## Separated Bilateral Blur Pass

A depth-aware blur that preserves silhouette edges. Uses a two-pass separable bilateral filter that considers both spatial distance and depth difference, preventing blur from bleeding across object boundaries. Commonly used to smooth out SSAO or similar noisy per-pixel effects.

**Properties:**

* `Radius`: Kernel radius in pixels.
* `GaussianSigma`: Standard deviation of the Gaussian weight function.
* `Sharpness`: Higher values preserve edges more aggressively.

## Simple Render Pass

Renders unlit and debug geometry as well as all UI and editor overlays. Accepts an optional color input and renders on top of it, or renders directly into the view's current render target if no input is provided.

What the simple render pass renders depends on which extractors are active:

* [ImGui](../../ui/imgui.md) (via [ImGUI Extractor](render-pipeline-extractors.md#imgui-extractor))
* [RmlUi](../../ui/rmlui.md)
* The editor grid (via [Editor Grid Extractor](render-pipeline-extractors.md#editor-grid-extractor))
* [Sprites](../sprite-component.md) and [shape icons](../../misc/components/shape-icon-component.md)
* [Editing gizmos](../../scenes/gizmos.md)
* Unlit meshes

**Properties:**

* `Message`: Debug string shown in the render output during development.

## Sky Render Pass

Forward render pass for skybox and sky dome objects. Renders sky geometry at infinite depth, after opaque objects but before transparent geometry.

**Required Extractor:** [Clustered Data Extractor](render-pipeline-extractors.md#clustered-data-extractor)

## Source Pass

Allocates a new render target for downstream passes to render into. This is where the pipeline creates its working textures.

**Properties:**

* `Format`: Pixel format. Available options include 8-bit normalized sRGB/linear, 16-bit float, 32-bit float, 11/11/10-bit float, and depth formats (`Depth16Bit`, `Depth24BitStencil8Bit`, `Depth32BitFloat`).
* `MsaaMode`: MSAA sample count (`None`, `2`, `4`, `8`).
* `ClearColor`: Color the texture is cleared to when `Clear` is enabled.
* `Clear`: If `true`, the render target is cleared at the start of every frame.

## Stereo Test Pass

A test pass for verifying stereoscopic rendering. Not used in production pipelines.

## Target Pass

The terminal pass that forwards the final pipeline output to the screen (swap chain) or to externally specified render targets. Every render pipeline must end with a target pass.

## Tonemap Pass

Converts high dynamic range (HDR) color values to display output. Combines exposure, color grading, and optional bloom. Typically the last image-quality pass before the [Target Pass](#target-pass).

**Properties:**

* `MoodColor`, `MoodStrength`: Tints the entire image towards a mood color. Useful for time-of-day effects.
* `Saturation`: Multiplier on color saturation. `1` = unchanged, `0` = greyscale.
* `Contrast`: Adjusts the contrast of the final image.
* `LUT1`, `LUT1Strength`, `LUT2`, `LUT2Strength`: Up to two 3D color lookup tables for color grading, each with a blend weight.
* `VignettingTexture`: Multiplied onto the image to darken edges.
* `NoiseTexture`: Adds film-grain style noise to reduce color banding.

## Transparent Forward Render Pass

Forward render pass for transparent geometry. Objects are sorted back-to-front to produce correct alpha blending. Optionally accepts a resolved depth input for soft particle effects.

**Required Extractor:** [Clustered Data Extractor](render-pipeline-extractors.md#clustered-data-extractor)

## Sorting Functions

Render data sorting controls the order in which objects are submitted to the GPU within a single pass. The available functions are:

* `ByRenderDataThenFrontToBack`: Groups objects by render data type first (minimizing state changes), then sorts front-to-back within each group (maximising early-Z rejection). Best for opaque geometry.
* `BackToFrontThenByRenderData`: Sorts back-to-front first (required for correct alpha blending), then by render data type. Best for transparent geometry.
* `ByDepthOffsetOnly`: Sorts purely by the render data's depth offset value, back-to-front. Produces a fully deterministic draw order independent of scene depth, which is useful for full-screen effects and render hooks where relative order must be predictable.

## See Also

* [Render Pipeline](render-pipeline-overview.md)
* [Render Pipeline Extractors](render-pipeline-extractors.md)
