# Follow Path Component

The *follow path component* is used to move an object along a spline.

<video src="media/path-component.webm" width="800" height="600" autoplay loop></video>

See the [spline component](spline-component.md) for how to create the spline shape.

This component is mainly meant for mechanical movement, such as objects moving on a rail. Movement is with constant speed and strictly along the path. It can be used for moving effects (lights, particles) around, where the mechanical behavior may not be too obvious, but for things like camera paths or anything else that should have natural acceleration, it won't be sufficient.

## Component Properties

* `Path`: The object on which the [spline](spline-component.md) to use is attached. If none is provided, the parent objects are searched for an object that contains a spline component. That means you can put an object into a [prefab](../../prefabs/prefabs-overview.md) and then place it onto different splines by adding the prefab instance as a child of the spline shape.
* `StartDistance`: At what distance along the path to start traversing it. If the `Path` reference is set, changing this value will properly preview where the object would start.
* `Running`: Whether the component is currently running or paused. This can be used at runtime from scripts, to start and stop traversal. It is also automatically set to false, when the end of the path is reached and no looping behavior is active.
* `Mode`: Whether to traverse the path in a loop or only once.
* `Speed`: How fast to move along the path.
* `LookAhead`: The component will rotate the object according to the path direction. For this it samples the path some distance ahead. The farther the look-ahead the earlier the object will rotate into upcoming curves. At a very low look-ahead, it will rotate very rigidly.
* `Smoothing`: With zero smoothing the position of the object will be exactly that of the path. With some smoothing, the position doesn't change as abruptly. For mechanical objects attached to a rail, this should be zero, for more organic movement, increase the value towards one.
* `FollowMode`: How the transform of the owner object gets modified:
    * `OnlyPosition`: Only the position gets moved along the path. The orientation of the object stays unaffected.
    * `AlignUpZ`: While moving along the path, the object rotates only around the up axis (Z) to look into the direction of the path. This is useful for moving platforms that should always stay perfectly flat.
    * `FullRotation`: The object is both moved and oriented accoring to the path.
* `TiltAmount`, `MaxTilt`: If `FollowMode` is `AlignUpZ`, *MaxTilt* defines whether the object may tilt a little when turning. *TiltAmount* specifies how much tilting will occur.

<video src="media/follow-path-mode.mp4" width="800" height="600" autoplay controls></video>

## See Also

* [Spline Component](spline-component.md)
* [Spline Node Component](spline-node-component.md)
