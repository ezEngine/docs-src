# Render Pipeline Extractors

Extractors run every frame before any rendering takes place. Their job is to inspect the scene and record *render data* — the information that render passes then use to draw objects. Which extractors are present in a pipeline determines what can be rendered.

## Clustered Data Extractor

Collects all visible lights, [decals](../../effects/decals/decals-overview.md), [reflection probes](../lighting/reflection-probe-components.md), and [fog](../../effects/fog.md), then assigns them to a 3D grid of spatial clusters that covers the camera frustum. During shading each pixel looks up which lights and decals affect it from the cluster it falls into, making per-pixel lighting cost proportional to local density rather than scene totals.

This extractor is required by all forward rendering passes (Opaque, Sky, Transparent) for lighting and decals to work.

**Properties:** *none*

## Editor Grid Extractor

Extracts render data for the editor's construction grid. Only meaningful inside editor pipelines.

**Properties:** *none*

**Required Render Pass:** [Simple Render Pass](render-pipeline-passes.md#simple-render-pass)

## Editor Selected Objects Extractor

Extracts render data for objects that are currently selected in the editor, feeding the [Selection Highlight Pass](render-pipeline-passes.md#selection-highlight-pass) with the geometry it needs to draw the outline. Only meaningful inside editor pipelines.

**Properties:** *none*

## Editor Shape Icons Extractor

Extracts the 3D icon sprites that the editor draws at the position of objects whose component type has a registered shape icon (e.g. light sources, cameras, sound sources). Only meaningful inside editor pipelines.

**Properties:**

* `Size`: World-space radius of the icons in metres (default 1 m).
* `MaxScreenSize`: Maximum rendered size of an icon in pixels (default 64 px). Prevents icons from becoming too large when the camera is very close.

**Required Render Pass:** [Simple Render Pass](render-pipeline-passes.md#simple-render-pass)

## ImGUI Extractor

Collects the geometry produced by [Dear ImGui](../../ui/imgui.md) each frame and prepares it for rendering.

**Properties:** *none*

**Required Render Pass:** [Simple Render Pass](render-pipeline-passes.md#simple-render-pass)

## Selected Objects Extractor

A runtime equivalent of the *Editor Selected Objects Extractor* that can be used in game pipelines. A `SelectionContext` object is supplied at runtime via `ezView::SetExtractorProperty()`, listing the game objects that should receive the selection highlight outline.

**Properties:** *none*

**Required Render Pass:** [Selection Highlight Pass](render-pipeline-passes.md#selection-highlight-pass)

## Simplified Data Extractor

A lightweight alternative to the *Clustered Data Extractor*. Gathers only basic sky irradiance data, without the full spatial clustering of lights and decals. Used by pipelines that do not need dynamic per-pixel lighting, such as the reflection capture pipeline.

**Properties:** *none*

## Visible Objects Extractor

The main extractor for scene geometry. Iterates over all visible game objects and calls `ezMsgExtractRenderData` on their components, allowing each component to record the render data it needs. This is what makes meshes, particles, sprites, and other visual components appear in the world.

**Properties:** *none*

## See Also

* [Render Pipeline](render-pipeline-overview.md)
* [Render Pipeline Passes](render-pipeline-passes.md)
