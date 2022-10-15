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

1. `ezJoltCharacterControllerComponent`: A base class for Jolt character controllers. It gives access to the most important functionality and also adds some convenience functionality.
1. `ezJoltDefaultCharacterComponent`: An implementation of `ezJoltCharacterControllerComponent` that is provided as an example and as a decent starting point. It implements behavior similar to old-school first-person shooter games, such as Half-Life 2. Depending on how significantly different behavior you want, you can either derive from this class and override some parts, or copy the entire code and rewrite everything as desired.

## Example

The player object is often the most complicated object in a game. The character controller only provides the locomotion aspect, but this is often coupled tightly to the overall game logic. For example, the player may move slower or be disallowed to jump while [carrying an object](jolt-grab-object-component.md). Many of these aspects can be handled by an overall player logic script. Other aspects, like the details of the characters velocity while sliding down a slope or jumping through the air, have to be implemented directly inside a character controller component.

The [Testing Chambers sample](../../../../samples/testing-chambers.md) contains a [prefab](../../../prefabs/prefabs-overview.md) called **Player.ezPrefab**, which demonstrates how to build your own player object. The top level node contains a *Default Character Controller* component. You could replace this with a custom character controller component, to test out entirely different movement behavior.

Note that the player object also uses an [input component](../../../input/input-component.md) to funnel input into a [script](../../../custom-code/typescript/typescript-overview.md), which implements high level game logic, like weapon selection.

## See Also

* [PhysX Character Controller](../../physx/special/physx-character-controller.md)