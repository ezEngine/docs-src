# Head Bone Component

The *head bone component* is a very simple component that applies a vertical rotation, ie around the *right* axis (`+Y`). It clamps the maximum rotation, so that it only applies a limited relative rotation to the parent object.

This is mainly used for vertical rotation of a camera attached to a [character controller](../../physics/jolt/special/jolt-character-controller.md). The character controller already defines the horizontal rotation, ie the direction into which it moves.

Usually custom code would take some [input](../../input/input-overview.md) and forward it to the head bone component to allow the player to look up and down.

This component is for very simple use cases. In a proper game one would often want to have more advanced camera behavior, which should be done through a [custom C++ components](../../custom-code/cpp/custom-cpp-component.md).

## Component Properties

* `VerticalRotation`: The maximum relative rotation away from the parent.

## Scriptable Functions

* `SetVerticalRotation(angle)`: Sets the vertical rotation to a known value.
* `ChangeVerticalRotation(angle)`: Adds to the rotation. The final rotation is always clamped to the valid range.

## See Also

* [Camera Component](../../graphics/camera-component.md)
* [Character Controller](../../physics/jolt/special/jolt-character-controller.md)
* [Custom Code with Visual Scripts](../../custom-code/visual-script/visual-script-overview.md)
* [Thirdperson View Component](thirdpersonview-component.md)
