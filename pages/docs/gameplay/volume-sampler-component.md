# Volume Sampler Component

The *Volume Sampler Component* samples arbitrary values from [volume components](../effects/post-processing/volume-components.md) at the owner game object's position (or the main camera's position). The sampled values can be read back via script or C++ code and used for gameplay logic, graphics effects, or any other purpose.

Values fade towards the volume borders according to the volume's [falloff](../effects/post-processing/volume-components.md) setting, and interpolate smoothly over a configurable duration when the owner moves from one volume into another.

## Setup

1. Add an `ezVolumeSamplerComponent` to a game object.
1. Set `VolumeType` to the [spatial category](../runtime/world/spatial-system.md) that matches the volumes you want to sample (e.g. `GenericVolume`).
1. Add one entry per value to the `Values` list. For each entry set:
   * `Name`: The key to look up in the volumes (must match a key stored in the volume's [blackboard template](../misc/blackboard-template-asset.md) or `Values` list).
   * `DefaultValue`: The value to use when no volume is active. May be left empty, see [Default Value](#default-value).
   * `InterpolationDuration`: How long to interpolate between values when transitioning between volumes. Set to zero for instant changes.
1. Read the current values at runtime using the scriptable functions `GetFloatValue`, `GetColorValue`, or the generic `GetValue`.

Alternatively, values can be registered at runtime via `RegisterValue` instead of the component's `Values` list. This is useful when the set of values is determined dynamically.

Enable `WriteToBlackboard` to also write every sampled value into a [blackboard](../misc/blackboards.md), using the same keys as configured in `Values`. This is the standard way to feed [render pipeline properties](../graphics/render-pipeline/render-pipeline-properties.md) dynamically, for example to change fog or color grading settings depending on which area of a level the camera is in.

## Component Properties

* `VolumeType`: The [spatial category](../runtime/world/spatial-system.md) identifying which volumes to sample. Default is `GenericVolume`. This must match the `Type` property of the target [volume components](../effects/post-processing/volume-components.md).

* `Values`: A list of values to sample. Each entry has:
  * `Name`: The key name to look up inside volumes. If `WriteToBlackboard` is enabled, this is also the key that the value is written to in the blackboard.
  * `DefaultValue`: The value outside of all volumes. Empty by default, see [Default Value](#default-value).
  * `InterpolationDuration`: The time over which the value transitions when moving into or out of a volume.

* `AttachToMainCamera`: If enabled, the sampling position is taken from the main camera instead of the owner game object's position. Use this for effects that should follow what the player sees rather than a specific object's location.

* `WriteToBlackboard`: If enabled, sampled values are written into a [blackboard](../misc/blackboards.md) every time they change, using the names from `Values` as keys.

* `BlackboardName`: The name of the [blackboard](../misc/blackboards.md) to write to, looked up the same way as [`ezBlackboardComponent::FindBlackboard`](../misc/blackboards.md). Leave empty to write to the world's blackboard.

## Default Value

`DefaultValue` decides what happens outside of all volumes:

* **Set:** The value moves to the default value. Near a volume's border, it is a mix of the default and the volume's value. Values from volumes are converted to the type of the default value.
* **Empty:** The value doesn't change, it keeps the last value that came from a volume. Until the first volume is entered, it has no value at all.

Leave it empty when whoever reads the value already has its own setting for the outside. For example, the [fog component](../effects/fog.md) has its own fog density. With a default value of `1` for `Fog.Density`, the fog near a volume's border would blend towards a density of `1`, instead of towards the fog component's own density.

## Strength

When `WriteToBlackboard` is enabled, every value gets a second blackboard entry with `_Strength` appended to its name, for example `Fog.Density_Strength`. It tells how much volumes affect the value at the current position: `0` outside of all volumes, `1` fully inside one, and in between in a volume's falloff region. It changes over the same `InterpolationDuration` as the value.

The [fog component](../effects/fog.md) uses the strength to blend from its own settings to the blackboard value. [Render pipeline properties](../graphics/render-pipeline/render-pipeline-properties.md) ignore it and use the value directly.

## Scriptable Functions

* `RegisterValue(Name, DefaultValue, InterpolationDuration)`: Registers a new value to be sampled at runtime. This is an alternative to the `Values` list that is not serialized.
* `GetValue(Name)`: Returns the current sampled value for the given name as a generic variant.
* `GetFloatValue(Name, FallbackValue)`: Returns the current value as a float, or `FallbackValue` if the value cannot be converted.
* `GetColorValue(Name, FallbackValue)`: Returns the current value as a color, or `FallbackValue` if the value cannot be converted.

## Example Use Case

To change fog settings based on area, attach a Volume Sampler Component to the camera's game object (or enable `AttachToMainCamera`), enable `WriteToBlackboard`, and add entries named `Fog.Color`, `Fog.Density`, etc. The [fog component](../effects/fog.md) automatically picks up matching keys from the world's blackboard. The [Testing Chambers](../../samples/testing-chambers.md) project contains a sample scene that demonstrates this, modifying the fog settings when moving between two rooms.

## See Also

* [Volume Components](../effects/post-processing/volume-components.md)
* [Render Pipeline Properties](../graphics/render-pipeline/render-pipeline-properties.md)
* [Blackboards](../misc/blackboards.md)
* [Blackboard Template Asset](../misc/blackboard-template-asset.md)
* [Spatial System](../runtime/world/spatial-system.md)
