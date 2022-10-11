# Meshes

Meshes are the central feature of any 3D engine. Meshes can be separated into two kinds: the ones used for rendering, and the ones used for interactions ([physics](../../physics/physx/physx-overview.md)).

Mesh data is either [imported](../../assets/import-assets.md) from external files, such as FBX files, or procedurally generated. Generating meshes procedurally is mostly useful for very basic shapes either for special cases or as placeholders during early development.

Graphical meshes are handled by the [mesh asset](mesh-asset.md). Meshes that are used in physics simulations are called [collision meshes](../../physics/physx/collision-shapes/physx-collision-meshes.md).

Once a mesh is imported as an [asset](../../assets/assets-overview.md), it can be placed in a scene as often as you like. For the most common use case you would use a [mesh component](mesh-component.md) to do so, but there are other components for special cases, such as the [instanced mesh component](instanced-mesh-component.md). Meshes may also be used by other things, for example as a [type of particle](../../effects/particle-effects/particle-renderers.md#mesh-renderer). To instantiate collision meshes, you need to use the proper [shape component](../../physics/physx/collision-shapes/physx-shapes.md).

Graphical meshes reference [materials](../../materials/materials-overview.md) which define how the mesh gets rendered. Collision meshes may use [surfaces](../../materials/surfaces.md) to set their physical properties.

## See Also


* [Materials](../../materials/materials-overview.md)
* [Surfaces](../../materials/surfaces.md)
