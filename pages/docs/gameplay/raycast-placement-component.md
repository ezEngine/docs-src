# Raycast Placement Component

The *raycast placement component* does a ray cast and positions a target object there.

The image below shows raycast placement components being used together with a [beam components](../effects/beam-component.md) to create laser beams.

![Laser Beam](../effects/media/beam.jpg)

This component does a ray cast along the forward axis of the game object it is attached to. If this produces a hit, the target object is placed there. If no hit is found the target object is either placed at the maximum distance or deactivated depending on the component configuration.

## Component Properties

* `MaxDistance`: The maximum distance to do the raycast.

* `DisableTargetObjectOnNoHit`: If set, the `RaycastEndObject` is set to [inactive](../runtime/world/game-objects.md#active-flag) when the raycast hits nothing within `MaxDistance`. This can be used for things like laser pointers, where the target object represents the 'laser dot'. If the laser pointer hits nothing, the laser dot object should temporarily disappear. Once the raycast hits something again, the component will make sure to reactivate the target object again.

* `RaycastEndObject`: A [referenced object](../concepts/object-references.md) that this component should affect. Every time the placement component determines a different position for the raycast hit, it will move the referenced object there.

* `ForceTargetParentless`: If set, the placement component will make sure that the referenced `RaycastEndObject` will be detached from any parent object. The practical reason for this is, that to prevent multiple objects from modifying the position of the end object, it should have no parent game object, which may pass down its own transform changes. However, when the end object is part of a prefab, it will always have a parent, and that parent may need to move. For example when a weapon is attached to a character controller. Therefore the placement component can take care of detaching the end object at the appropriate time.

* `ShapeTypesToHit`: Which kind of physics objects to hit with the raycast.

* `CollisionLayerEndPoint`: The [collision layer](../physics/jolt/collision-shapes/jolt-collision-layers.md) to use for the raycast to detect where the `RaycastEndObject` should be placed.

* `ChangeNotificationMsg`: If this string is non-empty, the component will broadcast a `ezMsgGenericEvent` message every time that the raycast hit position changes. This can be used by game code to react, for example a laser trip mine could then determine whether it should explode.

## See Also

* [Beam Component](../effects/beam-component.md)
* [Trigger Component](../physics/jolt/actors/jolt-trigger-component.md)
