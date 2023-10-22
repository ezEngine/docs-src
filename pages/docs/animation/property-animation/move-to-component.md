# MoveTo Component

A light-weight component that moves the owner object towards a single position.

The functionality of this component can only be controlled through (script) code.
The component is given a single point in global space. When it is set to *running* it will move
the owning object towards this point. Optionally it may use acceleration or deceleration and a maximum speed
to reach that point.

Since the target position is given through code and can be modified at any time, this component can be used
for moving objects to a point that is decided dynamically. For example an elevator can be moved to a
specific height, depending on which floor was selected. Or an object could follow a character,
by updating the target position regularly.

The component sends the event `ezMsgAnimationReachedEnd` and resets its running state when it reaches the target position.

## Component Properties

* `Running`: Whether the component is currently moving the owner. Has to be set to `true` to start moving towards the target position. Setting this to `false` before the target was reached will interrupt the movement immediately.
* `TranslationSpeed`: The maximum speed at which to move towards the target.
* `TranslationAcceleration`: The acceleration to use to reach the translation speed.
* `TranslationDeceleration`: The deceleration to use to slow down when the target destination is being reached.

## Component Script Functions

* `SetTargetPosition(pos)`: Call this to change the target position. Nothing will happen, though, unless `Running` is also set to `true`.

## See Also

* [Follow Path Component](../paths/follow-path-component.md)
* [Slider Component](slider-component.md)
