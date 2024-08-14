# AI Navigation Component

The *AI navigation component* is used to make an NPC move towards a destination, using the [navmesh](runtime-navmesh.md) to move around obstacles.

The component has to be instructed via [code](../../custom-code/custom-code-overview.md) what to do. The `SetDestination()` function is used to make it move the parent game object along a path towards the goal. `GetState()` can be called to query whether it is moving and how.

The component uses physics queries to place the NPC on solid ground. It uses the navmesh information only for the general direction. The *foot radius* determines the width for this query. It should be wide enough, so that the NPC cannot fall through small holes in the ground, but narrow enough, so that it can't stand far away in the air on a ledge. As long as the "feet" touch any solid ground, the NPC will hang there, it will not slide down.

<video src="media/crawl.mp4" width="800" height="600" autoplay controls></video>

This component demonstrates how navigation for an NPC can be implemented. It is not meant to be a solution for every game, though. In many cases you may want to implement your own, so that you can handle your game specific needs as desired. Don't hesitate to copy the implementation of this component and just use it as a starting point.

> **Note:**
>
> So far this component does not implement any dynamic *obstacle avoidance*. It is also not very robust, in case external influences push the character off the navmesh. These issues may be addressed in the future.

## Component Properties

* `Navmesh Config`: Which [navmesh type](runtime-navmesh.md#navmesh-types) to do the search on. 
* `Path Search Config`: Which [path search type](runtime-navmesh.md#path-search-types) to use for the path search.
* `Speed`: The target speed to reach.
* `Acceleration`, `Deceleration`: How quickly to accelerate and decelerate.
* `Foot Radius`: The footprint to determine whether the character is standing on solid ground.
* `Reached Distance`: The distance at which the destination is considered to be reached.
* `Collision Layer`: The physics collision layer for determining what ground one can stand on.
* `Fall Height`: If there is more distance below the character than this, it is considered to be falling.
* `Debug Flags`: What aspects of the navigation to visualize.

## See Also

* [Runtime Navmesh](runtime-navmesh.md)
* [Navmesh Path Test Component](navmesh-path-test-component.md)
