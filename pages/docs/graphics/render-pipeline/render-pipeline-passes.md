# Render Pipeline Passes

This page lists all render pipeline *passes* and their functionality.

## AO Pass

## Antialiasing Pass

## Blend Pass

## Bloom Pass

## Blur Pass

## Copy Texture Pass

## Depth Only Pass

## History Source Pass

## History Target Pass

## LSAO Pass

## MSAA Resolve Pass

## MSAA Upscale Pass

## Opaque Forward Render Pass

**Required Extractor:** [Clustered Data Extractor](render-pipeline-extractors.md#clustered-data-extractor)

## Picking Render Pass

## Reflection Filter Pass

## Selection Highlight Pass

## Separated Bilateral Blur Pass

## Simple Render Pass

Takes care of rendering simple data, for example:

* [ImGui](../../ui/imgui.md)
* [RmlUi](../../ui/rmlui.md)
* The editor grid.
* [Sprites](../sprite-component.md) and [editor shape icons](../../misc/components/shape-icon-component.md).
* [Editing Gizmos](../../scenes/gizmos.md).
* Unlit meshes.

Different extractors generate data for the simple render pass.

## Sky Render Pass

**Required Extractor:** [Clustered Data Extractor](render-pipeline-extractors.md#clustered-data-extractor)

## Source Pass

## Stereo Test Pass

## Target Pass

## Tonemap Pass

## Transparent Forward Render Pass

**Required Extractor:** [Clustered Data Extractor](render-pipeline-extractors.md#clustered-data-extractor)

## See Also

* [Render Pipeline](render-pipeline-overview.md)
* [Render Pipeline Extractors](render-pipeline-extractors.md)
