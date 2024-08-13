# Wind Volume Components

Wind volume components are used to define areas in a scene where wind should blow in a certain way.

> **Note:**
>
> On their own these components won't have any effect in a scene. A [wind system](wind.md) additionally has to be set up. Placing a [simple wind component](simple-wind-component.md) in a scene creates a basic wind system.

## Shared Component Properties

All wind volume components have these properties:

* `Strength`: The strength with which the wind shall blow.
* `StrengthFactor`: An additional multiplier for the wind strength. Can be adjusted dynamically and may be set to a negative value to reverse the wind direction. This can be used to pull things inwards, instead of pushing them away.
* `BurstDuration`: If this is set to zero, the wind blows continuously. Otherwise it blows for the specified amount of time and then stops.
* `OnFinishedAction`: If `BurstDuration` is non-zero, the component will deactivate itself once the burst is done. Additionally, the component may delete itself or the entire object. Note that if *None* is selected, the wind burst can be restarted, simply by reactivating the component.

## Sphere Wind Volume Properties

* `Radius`: The radius of the wind volume.

<video src="../media/wind-sphere.webm" width="600" height="600" autoplay loop></video>

## Cylinder Wind Volume Properties

* `Length`, `Radius`: The size of the cylinder.
* `RadiusFalloff`, `PositiveFalloff`, `NegativeFalloff`: An optional falloff for the wind strength, such that it smoothly ramps up when getting close to the cylinder. The *radius falloff* is used along the radial directions, the other two falloff values are used along the main axis of the cylinder either in the *positive* or *negative* direction from the center.
* `Mode`: How the wind force is computed.
  * `Directional`: The wind force is along the main cylinder axis.
  * `Vortex`: The wind whirls around the cylinder's axis. See the video below.

<video src="../media/wind-vortex.webm" width="600" height="600" autoplay loop></video>

## Cone Wind Volume Properties

* `Angle`, `Length`: Angle and length of the cone shape.

<video src="../media/wind-cone.webm" width="600" height="600" autoplay loop></video>

## See Also

* [Wind](wind.md)
* [Simple Wind Component](simple-wind-component.md)
