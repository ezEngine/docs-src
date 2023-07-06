# XR Project Setup

## XR Project Config

As an example, we will use the [Testing Chambers](../../samples/testing-chambers.md) project and its **Surfaces** scene to set up XR rendering for desktop VR use. Start by opening the project and scene.

Enable *Show in Development Features* in the [editor settings](..\editor\editor-settings.md) and restart it to see XR features in the editor.

To use XR in your project you must first load a plugin to supports XR devices. In the [plugin selection](../projects/plugin-selection.md) dialog, select your custom XR plugin. In this case, we select the *Open XR* plugin and close the dialog.

Next is to enable XR rendering under [asset profiles (TODO)](asset-profiles.md). Select the profile you want to enable XR in and then check the *Enable XR* checkbox. You also need to select the *XR Render Pipeline* here. Currently, both the `MainRenderPipeline` and the `HololensRenderPipeline` fully support XR rendering. Let's select the `MainRenderPipeline` for this example and close the dialog.

Pressing 'Play the Game' in the scene should now already start rendering on the HMD and you can look around but it will not be very interactive.

## Character Rig Setup

To be able to move around and use our controllers, we need to modify our character rig to support XR input scenarios. As an example, we will modify the **Player** prefab found in the testing chambers project.

### Stage Space

Once a XR plugin is active it takes control of the rendering camera. This means that the transform and projection of the [camera component](../graphics/camera-component.md) is no longer taken into account when rendering. To move the user in XR, we need to instead move the *stage space* that the XR system is using as a reference point to place the user into the scene. 

The `ezStageSpaceComponent` does just that. It should be placed on the [game object](../runtime/world/game-objects.md) that best represents the characters position in the world. In our example, add the component to the root `Player` object of the prefab.

The component only has one property:
* `Stage Space`: Can be either `Standing` or `Seated`. This defines the offset of the HMD to the stage space. In `Standing` mode, the stage space should be placed on the floor as the HMD will be placed relative to it matching the physical height of the user's head over the physical floor. In `Seated` mode, the HMD position relative to the stage space will match the users' head position relative to their head position when the app was started.

### Device Tracking

As mentioned above, the XR plugin takes ownership of the rendering camera. However, in many cases you will want to reflect the HMD position and controller positions in the scene as well. To do so, attach the `ezDeviceTrackingComponent` to a game object that you like to follow one of the XR input devices.

* `Device Type`: Which device we want to track. E.g. the HMD (a.k.a. your head) or one of the controllers.
* `Pose Location`: Some input devices have different poses for `Grip` and `Aim`. E.g. your hand's grip position is in the middle of your fist pointing upwards, while the aim position is at your index finger pointing forward.
* `Transform Space`: Whether the local or global transform should be set to the input device's transform.
* `Rotation`: Whether to apply rotation to the game object. Translation is always applied but in some cases it might be useful to not apply rotation. E.g. for helper nodes in the scene.
* `Scale`: Whether to apply scale to the game object. All input devices usually have an identity scale. If you don't want this to be overwritten while tracking, disable this option.

Add one component to the `Camera` game object with default settings and one to the `Gun` game object with device type `Right Controller`, pose location `Aim` and `Global` transform.

Safe the prefab and play the scene again. You should now be able to move the controller via a gamepad and poin the gun at things using your right controller.

## See Also

* [XR Graphics](xr-graphics.md)
* [XR Input](xr-input.md)
