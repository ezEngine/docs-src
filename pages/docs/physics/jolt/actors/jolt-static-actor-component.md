# Jolt Static Actor Component

The *Jolt static actor component* is used to represent static collision geomtry. Most geometry in a scene should be *static*, meaning that it never moves, rotates, scales or is animated in any way. Static geometry is generally faster to process, and in the case of physics simulations, only static actors may use **concave** collision geometry.

All [Jolt shapes](../collision-shapes/jolt-shapes.md) that can be found in the hierarchy below the static actor are combined to form the compound shape of the actor. However, if any other actor (static or dynamic) is part of the hierarchy below the static actor, the shapes below that object are ignored for this actor. Additionally, if the static actor itself references a [collision mesh](../collision-shapes/jolt-collision-meshes.md), it will also become part of the actor compound shape. Only static actors are able to reference concave triangle collision meshes.

If you need your geometry to be able to move, use a [dynamic actor](jolt-dynamic-actor-component.md) instead.

## Component Properties

* `CollisionLayer`: The [collision layer](../collision-shapes/jolt-collision-layers.md) defines which objects will collide with this actor.
* `CollisionMesh`: An optional convex or concave [collision mesh](../collision-shapes/jolt-collision-meshes.md) representing the static actor geometry. This will be combined with all [shapes](../collision-shapes/jolt-shapes.md) found in the hierarchy below the owner object.
* `IncludeInNavmesh`: If set, this object will be considered an obstacle for AI and [navmeshes](../../../ai/recast-navmesh.md) are generated around it.
* `PullSurfacesFromGraphicsMesh`: If this is enabled, at startup the actor will check whether there is a [graphics mesh component](../../../graphics/meshes/mesh-component.md) attached to the same owner, which has the same amount of materials, as the collision mesh. If so, it will query those materials for their [surfaces](../../../materials/surfaces.md) and use them to override the surfaces that are stored in the collision mesh. This can be very convenient, especially for complex meshes, because you only need to set up the materials for the graphics mesh, and don't need to mirror the same setup on the collision mesh. Also modifications to the graphics mesh (or its materials) will then apply to the collision mesh as well. Enabling this option forces the graphics mesh to be loaded at startup and therefore reduces potential for streaming data in the background.
* `Surface`: The [surface](../../../materials/surfaces.md) to use for this actor's shapes. The surface determines the friction and restitution during simulation, but also determines what effects are spawned when you interact with the object. Note that [collision meshes](../collision-shapes/jolt-collision-meshes.md) already specify the surface to use. If a surface is selected on the actor, it overrides the mesh's surface.

## See Also

* [Jolt Dynamic Actor Component](jolt-dynamic-actor-component.md)
* [Jolt Shapes](../collision-shapes/jolt-shapes.md)
* [Jolt Collision Meshes](../collision-shapes/jolt-collision-meshes.md)
