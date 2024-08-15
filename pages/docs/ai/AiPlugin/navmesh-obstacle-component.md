# Navmesh Obstacle Component

The *navmesh obstacle component* is used to inform the navmesh system, that a certain area has changed (blocked or unblocked) and needs to be regenerated.

This is mainly intended for large objects that either appear or disappear (for example when a player places a building) or that move only infrequently, such as a city gate opening after some quest got completed. It will not work for freely moving obstacles that would require *avoidance* by NPCs.

The obstacle must have a physical [collider](../../physics/jolt/collision-shapes/jolt-shapes.md) to represent its shape. The obstacle component automatically informs the navmesh that a *navmesh sector* is outdated when the component becomes active and inactive. If necessary, it can also be triggered externally to invalidate the sector again, for example when it moved.

## Exposed Functions

* `InvalidateSectors`: Triggers a rebuild of the navmesh sectors that the obstacle overlaps with.

## See Also

* [Runtime Navmesh](runtime-navmesh.md)
* [AI Navigation Component](navigation-component.md)
