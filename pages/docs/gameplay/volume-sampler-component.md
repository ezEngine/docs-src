# Volume Sampler Component

The *Volume Sampler Component* samples arbitrary values from [volume components](../effects/post-processing/volume-components.md) at the owner game object's position (or the main camera's position). The sampled values can be read back via script or C++ code and used for gameplay logic, graphics effects, or any other purpose.

Values fade towards the volume borders according to the volume's [falloff](../effects/post-processing/volume-components.md) setting, and interpolate smoothly over a configurable duration when the owner moves from one volume into another.

## Setup

1. Add an `ezVolumeSamplerComponent` to a game object.
1. Set `VolumeType` to the [spatial category](../runtime/world/spatial-system.md) that matches the volumes you want to sample (e.g. `GenericVolume`).
1. Add one entry per value to the `Values` list. For each entry set:
   * `Name`: The key to look up in the volumes (must match a key stored in the volume's [blackboard template](../misc/blackboard-template-asset.md) or `Values` list).
   * `DefaultValue`: The value to use when no volume is active.
   * `InterpolationDuration`: How long to interpolate between values when transitioning between volumes. Set to zero for instant changes.
1. Read the current values at runtime using the scriptable functions `GetFloatValue`, `GetColorValue`, or the generic `GetValue`.

Alternatively, values can be registered at runtime via `RegisterValue` instead of the component's `Values` list. This is useful when the set of values is determined dynamically.

## Component Properties

* `VolumeType`: The [spatial category](../runtime/world/spatial-system.md) identifying which volumes to sample. Default is `GenericVolume`. This must match the `Type` property of the target [volume components](../effects/post-processing/volume-components.md).

* `Values`: A list of values to sample. Each entry has:
  * `Name`: The key name to look up inside volumes.
  * `DefaultValue`: Returned when the owner is outside all volumes.
  * `InterpolationDuration`: The time over which the value transitions when moving into or out of a volume.

* `AttachToMainCamera`: If enabled, the sampling position is taken from the main camera instead of the owner game object's position. Use this for effects that should follow what the player sees rather than a specific object's location.

## Scriptable Functions

* `RegisterValue(Name, DefaultValue, InterpolationDuration)`: Registers a new value to be sampled at runtime. This is an alternative to the `Values` list that is not serialized.
* `GetValue(Name)`: Returns the current sampled value for the given name as a generic variant.
* `GetFloatValue(Name, FallbackValue)`: Returns the current value as a float, or `FallbackValue` if the value cannot be converted.
* `GetColorValue(Name, FallbackValue)`: Returns the current value as a color, or `FallbackValue` if the value cannot be converted.

## Example Use Case

The [Post-Processing Component](../effects/post-processing/post-processing-component.md) already uses volumes internally to adjust rendering parameters per area. The Volume Sampler Component extends this pattern for generic use cases.

For example, to change fog settings based on area, attach a Volume Sampler Component to the camera's game object and use a visual script to read the sampled fog values each frame and apply them to the [fog component](../effects/fog.md) or render pipeline. The [Testing Chambers](../../samples/testing-chambers.md) project contains a sample scene that demonstrates this. It modifies the fog settings when moving between two rooms.

## See Also

* [Volume Components](../effects/post-processing/volume-components.md)
* [Post-Processing Component](../effects/post-processing/post-processing-component.md)
* [Blackboard Template Asset](../misc/blackboard-template-asset.md)
* [Spatial System](../runtime/world/spatial-system.md)
