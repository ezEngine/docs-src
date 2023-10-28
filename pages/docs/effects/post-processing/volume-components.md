# Volume Components

Volume components are used to define custom environmental conditions in areas of a level.

By itself, volume components have no functionality and no noticeable effect. They only specify an area and what values to use there. Values are usually specified by referencing a [blackboard template asset](../../Miscellaneous/blackboard-template-asset.md). Other systems may use this information to implement behavior.

One such system is the [post-processing component](post-processing-component.md) which uses these volumes to modify parameters of the rendering pipeline, for example to have different color grading per area.

A custom system could for example also use these volumes to determine whether the player is inside water.

There are multiple volume components for different shapes:

* `ezVolumeBoxComponent`
* `ezVolumeSphereComponent`

They only add options to define their shape, such as extents or radius, but do not differ in functionality.

## Component Properties

All volume components share these properties:

* `Type`: A [spatial category](../../runtime/world/spatial-system.md) used for separating volumes that represent different things. This way one volume may be used to configure graphics settings, while other volumes may affect gameplay relevant functionality, and they don't accidentally interfere with each other, since the respective systems only get to see the volumes that are meant to affect them.

* `SortOrder`: In case two volumes overlap, the one with a higher sort order value has precedence.

* `Template`: A reference to a [blackboard template asset](../../Miscellaneous/blackboard-template-asset.md) to define the key/value pairs. It is usually more convenient to use a blackboard template as a preset for values, than to specify them directly on the volume component.

* `Values`: Individually added key/value pairs. Prefer to use a `Template`, but If the same key is also added here, it overrides the value from the template.

* `Falloff`: Volumes may have a *soft edge*, meaning that the boundary of the volume is not considered to be aprubt. This is used to smoothly fade values from one value to the one inside the volume. For example if a volume represents a foggy area, where the whole color grading is supposed to change, the colors are not supposed to change exactly the moment that the camera enters the volume, but rather the colors should become stronger the farther the camera is inside the volume. The *falloff* value is a value between `0` and `1` that configures how smooth the edge of the volume is. At `0` the edge is hard and change happens immediately. This is useful for example for water, where you are either inside or outside, but not in between. Any value above `0` is meant for smoother transitions. Be aware that additional to this, some systems may also transition to new values over time. To test the falloff value, it is best to deactivate any time delay.

## See Also

* [Post-Processing Component](post-processing-component.md)
