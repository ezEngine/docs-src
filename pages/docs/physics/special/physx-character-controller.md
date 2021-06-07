# Character Controller

A *character controller* is a special object in the physics engine that is used to move a character throughout a scene and make it collide with other geometry. A character controller is typically an upright capsule that abstractly represents the space that a character occupies.

<video src="media/cc.webm" width="600" height="600" autoplay loop></video>

The character controller provides the following functionality:

* Move throughout a scene, collide with and slide along walls
* Fall to the ground, slide down steep slopes
* Climb up shallow slopes
* Step over small obstacles
* Climb stairs
* Jump
* Stand and crouch with different capsule sizes
* Push dynamic objects
* Get pushed by kinematic objects
* Ride on kinematic platforms

On top of these basic features, the character controller implements many details of movement. For example, while jumping or falling, a game may allow the player some degree of control. Such details are very game specific, though, and there is no one-size-fits-all solution.

Consequently, the character controller functionality is split up into multiple classes, and you are encouraged to implement your own logic:

1. `ezCharacterControllerComponent`: An abstract base class for all character controllers, with a minimal interface. Other (script) code typically uses this interface to instruct the character to move, according to the player's input or the decision of an AI controlled character. This class is not actually specific to the PhysX plugin.
1. `ezPxCharacterShapeComponent`: A base class for exposing the raw functionality of the PhysX [character controllers](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/CharacterControllers.html#climbing-mode). Specifically `ezPxCharacterCapsuleShapeComponent` provides an implementation for the most commonly used capsule controller. If you implement a custom character controller, you can still save some work by reusing this, instead of calling the PhysX code yourself. On the other hand, you may want to write a custom implementation for this, if you need to adjust the very low level PhysX behavior for colliding and interacting with other bodies.
1. `ezPxCharacterControllerComponent`: An implementation of `ezCharacterControllerComponent` that is provided as an example and as a decent starting point. It implements behavior similar to old-school first-person shooter games, such as Half-Life 2. Depending on how significantly different behavior you want, you can either derive from this class and override some parts, or copy the entire code and rewrite everything as desired. The latter approach may be the better solution, as `ezPxCharacterControllerComponent` may get changes over time that you don't desire for your game.

## Example

The player object is often the most complicated object in a game. The character controller only provides the locomotion aspect, but this is often coupled tightly to the overall game logic. For example, the player may move slower or be disallowed to jump while [carrying an object](physx-grab-object-component.md). Many of these aspects can be handled by an overall player logic script. Other aspects, like the details of the characters velocity while sliding down a slope or jumping through the air, have to be implemented directly inside a character controller component.

The [Testing Chambers sample](../../../samples/testing-chambers.md) contains a [prefab](../../prefabs/prefabs-overview.md) called **Player.ezPrefab**, which demonstrates how to build your own player object. The top level node contains both a *PhysX Character Capsule Shape* component (for the raw movement functionality), as well as a *PhysX Character Controller* component. You could replace the latter with a custom character controller component, to test out entirely different movement behavior.

Note that the player object also uses an [input component](../../input/input-component.md) to funnel input into a [script](../../custom-code/typescript/typescript-overview.md), which implements high level game logic, like weapon selection.

## ezPxCharacterShapeComponent Component Properties

* `CollisionLayer`: The [collision layer](../collision-shapes/collision-layers.md) to use for colliding with other geometry.
* `Mass`: The mass of the character affects how much force it applies to objects it is standing on.
* `MaxStepHeight`: The maximum height of obstacles that the CC will step over automatically. Unless `ConstrainedClimbMode` is enabled, the CC may step over higher objects, though, because of the rounded bottom of the capsule controller.
* `MaxSlopeAngle`: The maximum angle of slopes that the character controller may walk up.
* `ForceSlopeSliding`: Determines whether the CC can stand on slopes steeper than `MaxSlopeAngle`. If this is enabled, it will be forced to slide down the slope.
* `ConstrainedClimbMode`: Tries to prevent a capsule shaped CC from stepping over obstacles taller than `MaxStepHeight`. Costs extra performance.

## ezPxCharacterCapsuleShapeComponent Component Properties

This component inherits the properties of `ezPxCharacterShapeComponent` and adds these properties:

* `CapsuleHeight`, `CapsuleRadius`: The height and radius of the capsule shape. Note that the total height of the capsule character shape is `2 * radius + height`.

## ezPxCharacterControllerComponent Component Properties

The `ezPxCharacterControllerComponent` expects to find a `ezPxCharacterShapeComponent` attached to the very same game object. Note that this class is mainly intended for demonstration purposes and may not have all the features and behavior that you need in your game.

* `RotateSpeed`: How fast the CC rotates around the up axis due to mouse or keyboard input.
* `WalkSpeed`, `RunSpeed`, `CrouchSpeed`, `AirSpeed`: The speed at which the CC will walk, run, move while crouching, or be able to navigate while not touching the ground.
* `AirFriction`: How much the CC will slow down when not touching the ground.
* `CrouchHeight`: How tall the CC is during crouching. Note that the total height of the capsule character shape is `2 * radius + height`.
* `JumpImpulse`: With how much force the CC will jump, and consequently how high it will jump.
* `PushingForce`: With how much force the CC will push [dynamic actors](../actors/physx-dynamic-actor-component.md) when walking into them.
* `WalkSurfaceInteraction`: The [surface interaction](../../materials/surfaces.md#surface-interactions) to trigger on the [surfaces](../../materials/surfaces.md) that the CC walks over. This is typically used to create footstep sounds.
* `WalkInteractionDistance`, `RunInteractionDistance`: The distance that the CC has to walk or run, until another surface interaction is triggered.
* `FallbackWalkSurface`: The [surface](../../materials/surfaces.md) to use for triggering footstep interactions, if the ground has no surface of its own.
* `HeadObject`: An [object reference](../../scenes/object-references.md) to a child object of the CC, which is considered the 'head'. If such a reference is set, the CC will move this object up and down when the CC crouches or stands up. The [main camera component](../../graphics/camera-component.md) should be attached to this head object, such that the player sees the difference. This property is only useful for first-person player characters.

## See Also


* [Character Controllers (nvidia.com)](https://gameworksdocs.nvidia.com/PhysX/4.0/documentation/PhysXGuide/Manual/CharacterControllers.html)
