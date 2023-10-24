# PhysX Static Actor Component

The *PhysX static actor component* is used to represent static collision geomtry. Most geometry in a scene should be *static*, meaning that it never moves, rotates, scales or is animated in any way. Static geometry is generally faster to process, and in the case of physics simulations, only static actors may use **concave** collision geometry.

All [PhysX shapes](../collision-shapes/physx-shapes.md) that can be found in the hierarchy below the static actor are combined to form the compound shape of the actor. However, if any other actor (static or dynamic) is part of the hierarchy below the static actor, the shapes below that object are ignored for this actor. Additionally, if the static actor itself references a [collision mesh](../collision-shapes/physx-collision-meshes.md), it will also become part of the actor compound shape. Only static actors are able to reference concave triangle collision meshes.

If you need your geometry to be able to move, use a [dynamic actor](physx-dynamic-actor-component.md) instead.

## Component Properties

* `CollisionMesh`: An optional convex or concave [collision mesh](../collision-shapes/physx-collision-meshes.md) representing the static actor geometry. This will be combined with all [shapes](../collision-shapes/physx-shapes.md) found in the hierarchy below the owner object.
* `CollisionLayer`: The [collision layer](../collision-shapes/physx-collision-layers.md) defines which objects will collide with this actor.
* `IncludeInNavmesh`: If set, this object will be considered an obstacle for AI and [navmeshes](../../../ai/RecastPlugin/recast-navmesh.md) are generated around it.
* `PullSurfacesFromGraphicsMesh`: If this is enabled, at startup the actor will check whether there is a [graphics mesh component](../../../graphics/meshes/mesh-component.md) attached to the same owner, which has the same amount of materials, as the collision mesh. If so, it will query those materials for their [surfaces](../../../materials/surfaces.md) and use them to override the surfaces that are stored in the collision mesh. This can be very convenient, especially for complex meshes, because you only need to set up the materials for the graphics mesh, and don't need to mirror the same setup on the collision mesh. Also modifications to the graphics mesh (or its materials) will then apply to the collision mesh as well. Enabling this option forces the graphics mesh to be loaded at startup and therefore reduces potential for streaming data in the background.

## See Also


* [PhysX Dynamic Actor Component](physx-dynamic-actor-component.md)
* [PhysX Shapes](../collision-shapes/physx-shapes.md)
* [Collision Meshes](../collision-shapes/physx-collision-meshes.md)
* [Collision Layers](../collision-shapes/physx-collision-layers.md)
