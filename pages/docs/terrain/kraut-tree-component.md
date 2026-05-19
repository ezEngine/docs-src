# Kraut Tree Component

The *Kraut tree component* places a procedurally generated tree in a scene. It references a [Kraut tree asset](kraut-tree-asset.md) and selects a random seed to determine the tree's visual appearance. Different seeds produce different-looking trees from the same asset.

LOD meshes are generated on demand in background tasks and the component renders the appropriate LOD for the current camera distance.

## Component Properties

`Kraut Tree` — The [Kraut tree asset](kraut-tree-asset.md) from which the tree is generated.

`Variation Index` — Selects a seed from the asset's *Good Random Seeds* list. The list is defined in the tree asset. If the list is empty or the index is out of range, the component falls back to the owner object's stable random seed. Use this property to place trees that are known to look good while still having variation between instances.

`Custom Random Seed` — Overrides the seed with a fixed value. Trees using the same seed will look identical. Mutually exclusive with *Variation Index*.

## Seed Selection

The component determines which seed to use according to the following priority:

1. **Custom Random Seed** — if set, this seed is always used.
2. **Variation Index** — if set, selects from the asset's *Good Random Seeds* list.
3. **Owner object's stable random seed** — used when neither of the above is set. This ensures that identically configured tree components on different objects still look different from each other without any manual configuration.

## Collision

The component adds a cylinder mesh as a collision approximation when geometry extraction is requested (e.g. for static mesh baking or physics). The cylinder radius is taken from the *Static Collider Radius* property of the referenced tree asset.

## See Also

* [Kraut Overview](kraut-overview.md)
* [Kraut Tree Asset](kraut-tree-asset.md)
