# Navmesh Path Test Component

This component is for testing the [runtime navmesh](runtime-navmesh.md).

Place an object with this component in you scene, then specify another object as the `PathEnd`. 
Make sure you have a [navmesh config](runtime-navmesh.md#navmesh-types) and a [path search config](runtime-navmesh.md#path-search-types) set up and chosen for this component to use.

Path searches are only possible while [simulating a scene](../../editor/run-scene.md), so press the *play* button to test it.

Now the plugin will automatically generate the navmesh and display the found path. If it doesn't show anything, check the *Visualize* options. `VisualizePathState` can help figuring out what went wrong. For instance the start and end points might not be in a location where the navmesh is reachable, at all, or they might be too high above the ground.

Also use the [navmesh visualization](runtime-navmesh.md#navmesh-visualization) functionality to make sure any mesh was generated successfully, at all.

## Component Properties

* `VisualizePathCorridor`: If enabled, the polygons that form the *corridor* of the path search result are visualized.
* `VisualizePathLine`: If enabled, the shortest line through the corridor is visualized.
* `VisualizePathState`: If enabled, the current state of the path search is printed as text at the location of this object.

* `PathEnd`: A [references](../../scenes/object-references.md) to another object that acts as the path's destination.
* `NavmeshConfig`: Which [navmesh type](runtime-navmesh.md#navmesh-types) to do the search on. 
* `PathSearchConfig`: Which [path search type](runtime-navmesh.md#path-search-types) to use for the path search.

## See Also

* [Runtime Navmesh](runtime-navmesh.md)
* [AiPlugin Overview](ai-plugin-overview.md)
