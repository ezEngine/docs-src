# XR Project Setup

## XR Project Config

As an example, we will use the [Testing Chambers](../../samples/testing-chambers.md) project and its **Surfaces** scene to set up XR rendering for desktop VR use. Start by opening the project and scene.

Enable *Show in Development Features* in the [editor settings](../editor/editor-settings.md) and restart it to see XR features in the editor.

To use XR in your project you must first load a plugin to support XR devices. In the [plugin selection](../projects/plugin-selection.md) dialog, select your custom XR plugin. In this case, we select the *Open XR* plugin and close the dialog.

Next is to enable XR rendering under [asset profiles](../assets/asset-profiles.md). Select the profile you want to enable XR in and then check the *Enable XR* checkbox. You also need to select the *XR Render Pipeline* here. Currently, both the `MainRenderPipeline` and the `HololensRenderPipeline` fully support XR rendering. Let's select the `MainRenderPipeline` for this example and close the dialog.

Pressing 'Play the Game' in the scene should now already start rendering on the HMD and you can look around but it will not be very interactive.

## Character Rig Setup

To be able to move around and use our controllers, we need to modify our character rig to support XR input scenarios. As an example, we will modify the **Player** prefab found in the testing chambers project.

### Stage Space

Once a XR plugin is active it takes control of the rendering camera. This means that the transform and projection of the [camera component](../graphics/camera-component.md) is no longer taken into account when rendering. To move the user in XR, we need to instead move the *stage space* that the XR system is using as a reference point to place the user into the scene.

The [ezStageSpaceComponent](stage-space-component.md) does just that. In our example, add the component to the root `Player` object of the prefab as it best represents the players position in the world. If the player moves, it will also move the XR camera and controllers relative to it.

### Device Tracking

As mentioned above, the XR plugin takes ownership of the rendering camera. However, in many cases you will want to reflect the HMD position and controller positions in the scene as well. A Simple way of achieving this is to add a [ezDeviceTrackingComponent](device-tracking-component.md) to a game object that you like to follow one of the XR input devices.

Add one component to the `Camera` game object with default settings and one to the `Gun` game object with device type `Right Controller`, pose location `Aim` and `Global` transform.

Safe the prefab and play the scene again. You should now be able to move the controller via a gamepad and point the gun at things using your right controller.

### Input Mapping

Next, you will need to map XR controller input to input actions. Go to the [Input Set Configuration](../input/input-config.md) dialog and change `Shoot` to `xr_hand_right_select_click`. If you play the scene again, you should be able to shoot with your right controller. More details can be found in the [XR Input](xr-input.md) chapter.

### Rendering Multithreading

By default, the engine renders multithreaded. This means that one frame of delay is introduced. This will worsen the stability of the XR experience. If enough CPU headroom is available, consider disabling the cvar `Rendering.Multithreading` using the methods outlined [here](../debugging/cvars.md).

## See Also

* [XR Graphics](xr-graphics.md)
* [XR Input](xr-input.md)
