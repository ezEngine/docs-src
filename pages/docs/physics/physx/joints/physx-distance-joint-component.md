# PhysX Distance Joint Component

The *PhysX distance joint component* is a [joint](physx-joints.md) that links two actors such that they will keep a minimum and maximum distance. If the actors come closer than the minimum distance, they will repell each other, if they get farther apart than the maximum distance, they will attract each other. The distance constraint can be either hard, meaning it can never be violated, or soft, meaning when it is violated, a spring with a certain stiffness becomes active to try to push or pull the involved actors back to the desired distance.

<video src="media/distance-joint.webm" width="600" height="600" autoplay loop></video>

The distance joint can be used to fake the behavior of chains and ropes, if no proper simulation and visualization of those is needed.

## Component Properties

* [Shared Joint Component Properties](physx-joints.md#shared-joint-component-properties)

* `MinDistance`: The minimum distance that the two joined actors should keep from each other. If the joint has no parent actor, the child actor will keep this distance from the joint position. Note that if the distance joint does not use the `ChildActorAnchor` option, a non-zero minimum distance will make the child actor be pushed away right after startup.
* `MaxDistance`: The maximum distance between the two joined actors. Without a spring, the two joined actors are unable to get farther apart than this. With a spring, the two actors will be pulled back together with the spring force, when they become farther apart than this.
* `SpringStiffness`: If zero, the distance constraint is *hard*, meaning the joined actors are unable to violate the distances. If this is non-zero, the constraint is *soft* and if violated, a spring force will start to push or pull the actors.
* `SpringDamping`: A damping factor for the spring to prevent oscilation.
* `SpringTolerance`: An optional distance tolerance, that prevents the spring from becoming active. Note that this effectively increases the `MaxDistance` and decreases the `MinDistance`.

## See Also


* [Physics Joints](physx-joints.md)
* [PhysX Actors](../actors/physx-actors.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Distance Joint (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/Joints.html#fixed-joint)
