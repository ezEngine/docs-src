# Area Damage Component

The *area damage component* posts an `ezMsgDamage` to all objects in its vicinity every time it is triggered. It may also send an `ezMsgPhysicsAddImpulse` to push objects away from its location. This is used to implement the effect of explosions and other things that should damage close-by objects.

## Component Properties

* `OnCreation`: If enabled, the component will apply damage the moment it gets activated.
* `Radius`: The radius in which objects will receive damage.
* `CollisionLayer`: The physics [collision layer](../physics/jolt/collision-shapes/jolt-collision-layers.md) to use to find objects to which to apply damage.
* `Damage`: The maximum amount of damage to apply. Damage is scaled down linearly by distance, so an object further away will receive less damage.
* `Impulse`: An optional physical impulse to apply to damaged objects. This will push objects away from this object. The applied impulse is also scaled down linearly by distance.

## Scripting

* `ApplyAreaDamage()`: This function can be called manually to control when and how often this component applies damage. For example a 'dangerous' area can be implemented by repeatedly triggering a component of this type.

## See Also

* [Spawn Component](spawn-component.md)
* [Timed Death Component](timed-death-component.md)
