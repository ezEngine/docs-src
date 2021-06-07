# Rotor Component

The *rotor component* is a very useful utility component to rotate an object around an axis. This can be used for simple animations, such as having an itme in the world spin around itself.

## Component Properties

* `Speed`: The maximum speed at which the rotor will turn.
* `Running`: Whether the rotor will move right from the start. If this is disabled, external code needs to switch the state to on, for the rotor to do anything.
* `ReverseAtEnd, ReverseAtStart`: Whether the rotor should automatically reverse its direction when it reaches the end, and when it reaches the start point again. If both are enabled, the rotor will turn back and forth indefinitely. Otherwise it will stop either at the end, or at the start. In both cases the `Running` state is reset to `false`, and the rotor can be restarted by setting the `Running` state to `true` again.
* `Axis`: The local axis around which the rotor should turn.
* `AxisDeviation`: A random deviation to apply to the `Axis`. This allows you to place multiple copies of the same object next to each other, and have them all rotate slightly differently.
* `DegreesToRotate`: How far to turn before the rotor needs to stop or reverse direction. This is not limited to 360 degrees, it may represent multiple revolutions. Use `0`, if the rotor should just rotate continuously in one direction. In that case acceleration and decelaration have no effect.
* `Acceleration, Deceleration`: How fast to speed up and slow down. Use zero if the rotor should reverse course instantly.

## See Also


* [Slider Component](slider-component.md)
* [Property Animation (TODO)](property-animation-overview.md)
