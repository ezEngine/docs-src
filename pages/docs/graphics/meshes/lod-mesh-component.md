# LOD Mesh Component

This component is functionally identical to the [LOD component](../lod-component.md), except that it switches only between [meshes](mesh-asset.md) rather than entire objects. It is thus both easier to set up and more efficient in these more limited use cases. For details how to use this component, please consult the [LOD component](../lod-component.md) documentation.

## Component Properties

* `Color`, `CustomData`, `SortingDepthOffset`: See the [mesh component](mesh-component.md) for details.

* `BoundsOffset`, `BoundsRadius`, `ShowDebugInfo`, `OverlapRanges`: See the [LOD component](../lod-component.md) for details.

* `Meshes`: An array that lists the different level-of-detail meshes to switch between. Each entry names one `Mesh` and a `Threshold`. The first mesh is used for coverage values from 1 down to the given threshold. Then the next mesh is used from that coverage value down to the next threshold and so on. If the last mesh uses a threshold larger than 0, then nothing gets rendered when the coverage value is lower than that.

## See Also

* [Mesh Component](mesh-component.md)
* [LOD Component](../lod-component.md)
