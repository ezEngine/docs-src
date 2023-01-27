# Slider Component

The *slider component* is a very useful utility component to move an object back and forth along a single axis. This can be used for simple animations, such as having a pickup item bounce up and down, or for simple buttons or sliding doors.

## Video: How to make objects rotate and bounce

[![video](https://img.youtube.com/vi/skzDv7IUk2M/0.jpg)](https://www.youtube.com/watch?v=skzDv7IUk2M)

## Component Properties

* `Speed`: The maximum speed at which the slider will move.
* `Running`: Whether the slider will move right from the start. If this is disabled, external code needs to switch the state to on, for the slider to do anything.
* `ReverseAtEnd, ReverseAtStart`: Whether the slider should automatically reverse its direction when it reaches the end, and when it reaches the start point again. If both are enabled, the slider will go back and forth indefinitely. Otherwise it will stop either at the end, or at the start point. In both cases the `Running` state is reset to `false`, and the slider can be restarted by setting the `Running` state to `true` again.
* `Axis`: The local axis along which the slider should move.
* `Distance`: The distance that the slider should travel before stopping or returning.
* `Acceleration, Deceleration`: How fast to speed up and slow down. Use zero if the slider should reverse course instantly.
* `RandomStart`: If set to zero, the slider will always start from the beginning. Otherwise a random time offset between zero and `RandomStart` is used to pre-simulate the slider position. This is useful if you have multiple moving objects next to each other and you don't want them all to move in perfect unison. If you just want any random start position, just pick a very large `RandomStart` value.

## Scripting

* `SetDirectionForwards`: Allows to force the direction of the slider to either forwards or backwards along its axis.
* `IsDirectionForwards`: Queries whether the slider is currently moving forwards or backwards.
* `ToggleDirection`: Toggles the current direction of the slider.

## See Also

* [Rotor Component](rotor-component.md)
* [Property Animation (TODO)](property-animation-overview.md)
* [MoveTo Component (TODO)](move-to-component.md)
