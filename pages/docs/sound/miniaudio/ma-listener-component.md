# MiniAudio Listener Component

The *MiniAudio listener component* represents the position and direction from where the player perceives sound. Games that require *positional audio* must have exactly one listener component in the scene, to instruct MiniAudio how to compute the spatial sound.

For first-person and third-person games the listener component would usually be attached to the player character, typically the same node where the main [camera component](../../graphics/camera-component.md) is located.

For other kinds of games positioning the listener component can be more tricky. For example, in a top-down strategy game, or a 2D side scroller, you may move the camera very far out (to achieve the desired perspective). Though, if you were to place the listener component at the same position, you would either not hear anything (too far away), or if you adjust the sounds such that you hear something, you may hear a lot of sounds that are very far off-screen.

In such situations it is better to move the listener component much closer to the action. The image below shows such a setup, where the listener is much closer to the action than the camera:

![Listener](../media/listener.png)

The red cone represents what the camera sees. The green circle visualizes the area in which sounds are audible.

## Component Properties

This component currently has no properties, only it's position and orientation matter.

## See Also

* [MiniAudio Integration](ma-overview.md)
* [MiniAudio Sound Component](ma-sound-component.md)
