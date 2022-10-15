# Jolt Distance Constraint Component

The *Jolt distance constraint component* is a [constraint](jolt-constraints.md) that links two actors such that they will keep a minimum and maximum distance. If the actors come closer than the minimum distance, they will repel each other, if they get farther apart than the maximum distance, they will attract each other.

<video src="media/distance-joint.webm" width="600" height="600" autoplay loop></video>

The distance joint can be used to fake the behavior of chains and ropes, if no proper simulation and visualization of individual chain links is needed.

## Component Properties

* [Shared Constraint Component Properties](jolt-constraints.md#shared-constraint-component-properties)

* `MinDistance`: The minimum distance that the two joined actors should keep from each other. If the constraint has no parent actor, the child actor will keep this distance from the constraint position. Note that if the distance constraint does not use the `ChildActorAnchor` option, a non-zero minimum distance will make the child actor be pushed away right after startup.
* `MaxDistance`: The maximum distance between the two joined actors. Without a spring, the two joined actors are unable to get farther apart than this. With a spring, the two actors will be pulled back together with the spring force, when they become farther apart than this.
* `Frequency`: Determines how often (per second) the constraint is enforced. Higher values make the constraint stiffer, but can also lead to oscillation. Good values are in range 0.1 to 20.
* `Damping`: How much to dampen actors when they overshoot the target position. Lower values make the objects bounce back harder, higher values make them just stop.

## See Also

* [Jolt Constraints](jolt-constraints.md)
* [Jolt Actors](../actors/jolt-actors.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
