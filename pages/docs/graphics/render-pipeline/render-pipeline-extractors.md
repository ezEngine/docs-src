# Render Pipeline Extractors

This page lists all render pipeline *extractors* and their functionality.

## Clustered Data Extractor

Gathers information about
* light sources
* decals
* reflection probes
* fog

Required by the forward rendering passes, for lighting and other things to work.

**Properties:** *none*



## Editor Grid Extractor

Used in the editor to extract render data for the editor grid.

**Properties:** *none*

**Required Renderpass:** [Simple Render Pass](render-pipeline-passes.md#simple-render-pass)



## Editor Selected Objects Extractor

**Properties:** *none*



## Editor Shape Icons Extractor

Used in the editor to extract render data for all 3D icons used for selecting objects.

**Properties:**
* `Size`:
* `Max Screen Size`:

**Required Renderpass:** [Simple Render Pass](render-pipeline-passes.md#simple-render-pass)



## ImGUI Extractor

Prepares rendering of [ImGui](../../ui/imgui.md) UI. The *simple render pass* must be part of the render pipeline to render the data.

**Properties:** *none*

**Required Renderpass:** [Simple Render Pass](render-pipeline-passes.md#simple-render-pass)



## Selected Objects Extractor

**Properties:** *none*



## Simplified Data Extractor

**Properties:** *none*



## Visible Objects Extractor

**Properties:** *none*



## See Also

* [Render Pipeline](render-pipeline-overview.md)
* [Render Pipeline Passes](render-pipeline-passes.md)
