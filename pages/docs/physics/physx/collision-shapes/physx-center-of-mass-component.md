# PhysX Center of Mass Component

The *center of mass component* is used to adjust the weight distribution of a [physics actor](../actors/physx-dynamic-actor-component.md). In general the mass of an physical object is computed from all the [shapes](physx-shapes.md) that it is made up of. Since all shapes are assumed to have constant density, the center of mass for many objects often ends up being different from where it would be for a real object.

By adding a [game object](../../../runtime/world/game-objects.md) and attaching a center of mass component, you can specify the exact location of the center of mass yourself.

In many cases the center of mass must be moved slightly downwards, to prevent objects from tipping over too easily. However, you can also use this to create an object that rights itself up. In reality this would be achieved through a heavy weight at its bottom, here all you need to do is shift the center of mass way down.

## See Also


* [Physics Actors](../actors/physx-actors.md)
* [Physics Shapes](physx-shapes.md)

