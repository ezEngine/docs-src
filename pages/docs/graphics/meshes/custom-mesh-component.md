# Custom Mesh Component

The `ezCustomMeshComponent` can be used in place of a [mesh component](mesh-component.md), but rather than loading a [mesh asset](mesh-asset.md), the mesh geometry is provided through (C++) code dynamically at runtime.

This component is useful when you need to build geometry dynamically, for example to create visualizers that show what a player can do at a specific point in your game world. These things may not be possible to build up from fixed pieces, and therefore need custom geometry.

## Mesh Buffer Resource

Each custom mesh component references a `ezDynamicMeshBufferResource`. Either its very own one, or a shared resource. At runtime, you would modify the geometry in that resource, and the `ezCustomMeshComponent` takes care of rendering it.

## Instancing

If you want to render multiple instances of the same geometry, create multiple `ezCustomMeshComponent`s and set all of them to reference the same mesh buffer resource.

## Materials

Each component only uses a single [material](../../materials/materials-overview.md) for rendering, but if you want to use multiple materials to render different pieces of the geometry, you can use multiple custom mesh components, and have each one render a different part of the geometry by giving it a limited *primitive range*.

## Vertex Colors

Custom mesh components use *vertex colors*, meaning every vertex stores its own color information. This is different to typical mesh data in EZ, where per-vertex colors are usually not used. If you do not require vertex colors, this is fine and you can use any default [material](../../materials/materials-overview.md) (and thus shader). The extra information will simply be ignored.

However, if you do need the vertex color information, for instance to precisely control transparency, then you also need to set a material, which uses a [shader (TODO)](../shaders/shaders-overview.md) that actually reads the vertex color value and uses it in the way that you desire. You may need to write a custom shader for that.

## See Also

* [Meshes](meshes-overview.md)
* [Shaders](../shaders/shaders-overview.md)
