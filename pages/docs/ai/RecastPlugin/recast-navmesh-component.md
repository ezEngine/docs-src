# Recast Navmesh Component

The Recast Navmesh component is used to add a navigation mesh to a scene. See the chapter about the [Recast Navmesh](recast-navmesh.md) for details.

## Component Properties

* `ShowNavMesh`: If enabled, a debug visualization of the navmesh is rendered. **Note:** The same can be achieved through the [CVar](../../debugging/cvars.md) `ai_ShowNavMesh` which can be dynamically toggled at runtime.
* `AgentHeight`, `AgentRadius`: The height and radius of the average agent for which the navmesh will be generated.
* `AgentClimbHeight`: How high obstacles can be before they prevent the agent from stepping over.
* `WalkableSlope`: The slope angle that the agent is able to walk up.
* `CellSize`, `CellHeight`: The size of the cells used for voxelizing the level geometry, from which the navmesh is computed. Smaller cell sizes are better for correctness and precision, but also cost much longer to compute. Note that the cell height must be small enough to properly detect obstacle heights, otherwise the `AgentClimbHeight` won't work as expected. If necessary, prefer a finer grained cell height over a smaller cell size.
* `MinRegionSize`: The minimum area (in square meters) for every navmesh section. Islands that are smaller than this will be discarded.
* For all the remaining options refer to the Recast documentation.

## See Also

* [Recast Navmesh](recast-navmesh.md)
* [Recast Integration](recast.md)
