# AiPlugin Overview

The *AiPlugin* is an optional engine plugin that provides functionality for doing typical game AI tasks.

To enable the plugin, use the [plugin selection](../../projects/plugin-selection.md) dialog and enable the *AiPlugin*. Some functionality will show up in the form of *components*, other functionality may only be available through C++ code.

To get access to the C++ functionality, your code needs to additionally link against the AiPlugin library. For example the [Monster Attack Sample](../../../samples/monster-attack/monster-attack.md) does so through its `CMakeLists.txt` file. 

## Navigation

The plugin provides functionality to create navmeshes on-demand at runtime. See [this chapter](runtime-navmesh.md) for details.

Additionally there is C++ functionality available for searching paths and *steering* characters along the found path. See the [Monster Attack Sample](../../../samples/monster-attack/monster-attack.md), specifically the *monster component*, to see how this can be used.

The [Detour Crowd Agent Component](detour-crowd-agent-component.md) provides a ready-to-use component for multi-agent navigation with local obstacle avoidance between agents.

For objects that move freely through 3D space, such as flying creatures or spaceships, the plugin provides [3D voxel navigation](voxel-navigation.md) instead, which uses volumetric grids rather than a navmesh.

## See Also

* [Runtime Navmesh](runtime-navmesh.md)
* [AI Navigation Component](navigation-component.md)
* [Detour Crowd Agent Component](detour-crowd-agent-component.md)
* [3D Voxel Navigation](voxel-navigation.md)
