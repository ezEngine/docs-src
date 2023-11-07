# Root Motion

By default a skeletal animation has its origin at the position of the game object on which it is played. Relative to that location  animations will move the bones and the skinned mesh will move accordingly. The game object itself stays fixed at that location, though.

This is sufficient if either the game object shouldn't change its location anyway, or when any change in position is controlled through other means. For example a player character might be moved around the world through [custom code](../../custom-code/custom-code-overview.md) and a walking animation is only played to visualize the action. This approach can be the right solution, depending on the type of game.

Such a method is, however, very prone to *foot sliding*, meaning an artifact where the feet move, but don't *stick* to the ground. If the movement of a game object should generally be determined by the exact blend of animation clips, it is better to have the motion be part of each animation clip.

For example a *walk animation* would contain the information into which direction and at what speed a game object should be moved to fit the animation. When a *forward* and *walk right* animation get mixed together, their root motion information is equally mixed and the object would be moved diagonally.

## Defining Root Motion

There are multiple ways how root motion could be defined for a clip. It could come from a dedicated bone for overall motion, or it could be extracted from how the feet touch the ground, etc.

For the time being EZ only implements the most simple method. An [animation clip](animation-clip-asset.md) either has no root motion at all, or it has a *constant motion* that is used for the entire clip. This is sufficient to build basic locomotion animations.

Finally, for now only *positional* root motion is available. That means an animation can change the position of a game object, but not its rotation.

It is planned to add more sophisticated methods for root motion in the future.

## Applying Root Motion

The [simple animation component](simple-animation-component.md) and the [animation controller component](animation-graphs/animation-controller-component.md) get the root motion data from the played animation clips. There are these modes to apply it to their owner game object:

* `Ignore`: No root motion is applied, the game object will not be moved by the animation.

* `ApplyToOwner`: Any available root motion is directly applied to the game object and thus moves it without restriction. This mode is useful for objects that have to follow a fixed path. For example moving platforms (which are *kinematic* [physics actors](../../physics/jolt/actors/jolt-dynamic-actor-component.md)), or objects that don't physically interact with the player. This mode is not suited for characters that should obey physical restrictions.

* `SendMoveCharacterMsg`: If this mode is used, root motion is not applied to any object, instead the [message](../../runtime/world/world-messaging.md) `ezMsgMoveCharacterController` is sent to the *top most game object* in the hierarchy. This way, if there is also a [character controller](../../physics/jolt/special/jolt-character-controller.md) or other component that accepts this type of message, it can apply the root motion as it sees fit.

## See Also


* [Skeletal Animations](skeletal-animation-overview.md)
* [Simple Animation Component](simple-animation-component.md)
* [Animation Controller Component](animation-graphs/animation-controller-component.md)
