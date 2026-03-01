# Jolt Generate Collision Component

The *Jolt generate collision component* automatically creates a static collision mesh from the render meshes produced by a [spline mesh component](../../../animation/paths/spline-mesh-component.md) on the same game object.

Because spline meshes are procedurally generated from a set of render mesh pieces, there is no single pre-authored collision asset that can be assigned by hand. This component solves that by mapping each render mesh piece to a corresponding Jolt collision mesh asset, then assembling the collision geometry to match the generated spline mesh exactly.

## Setup

1. Add a [spline mesh component](../../../animation/paths/spline-mesh-component.md) to a game object.
1. Add a *Jolt generate collision component* to the same object.
1. For each render mesh piece used by the spline mesh component, add an entry to the **Mesh Mappings** list:
   * **Render Mesh**: The render mesh asset used in the spline mesh component.
   * **Collision Mesh**: The corresponding [Jolt collision mesh](../collision-shapes/jolt-collision-meshes.md) asset (triangle mesh).
1. Set the **Collision Layer** to the appropriate [collision layer](../collision-shapes/jolt-collision-layers.md).

Render mesh pieces that have no mapping entry will not produce any collision geometry.

## Component Properties

* **Mesh Mappings**: List of render-mesh-to-collision-mesh pairs. Each entry maps one render mesh to one Jolt triangle collision mesh.
* **Collision Layer**: The [collision layer](../collision-shapes/jolt-collision-layers.md) assigned to the generated static actor.

## See Also

* [Spline Mesh Component](../../../animation/paths/spline-mesh-component.md)
* [Jolt Collision Meshes](../collision-shapes/jolt-collision-meshes.md)
* [Jolt Static Actor Component](../actors/jolt-static-actor-component.md)
* [Jolt Collision Layers](../collision-shapes/jolt-collision-layers.md)
