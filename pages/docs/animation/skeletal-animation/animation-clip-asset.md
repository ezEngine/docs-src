# Animation Clip Asset

The *animation clip asset* is used to import a single animation for an [animated mesh](animated-mesh-asset.md).

<video src="../media/anim-clip.webm" width="800" height="600" autoplay loop></video>

An animation clip represents a single motion, such as a walk cycle, a jump or other action. Simple animations can be played on a mesh using a [simple animation component](simple-animation-component.md). For complex behavior you will need to use multiple clips and fade from one to the other at the right times. Use an [animation graph](animation-graphs/animation-graph-overview.md) for that.

> **Important:**
>
> In animation graph nodes animation clips are **not referenced directly** but rather through a name mapping. This mapping is configured in the [animation graph asset](animation-graphs/animation-graph-asset.md).

## Importing Many Animation Clips Quickly

In the [asset browser](../../assets/asset-browser.md) select to show `<Importable Files>` then find your source animation clip file. Right click on it, and from the *Import As* sub-menu select `Animation Clips (All)`. In the next step, you are asked to select an [animated mesh](animated-mesh-asset.md) as the preview model.

After this, the editor creates a new animation clip document for each animation that it finds in the file.

Animation clips can also be imported automatically when [importing an animated mesh](../../graphics/meshes/mesh-import.md).

## Asset Properties

* `File`: The file from which to import the animation clip.

* `PreviewMesh`: The [animated mesh](animated-mesh-asset.md) to use for previewing this animation clip. This has to be set to see any preview.

* `UseAnimationClip`: The (case sensitive) name of the animation clip to import from the file. *Transform* the asset once to populate the list of `AvailableClips`. Then type the name of the desired clip into this field and transform the asset again. If a clip doesn't show up in the list, make sure it is correctly exported. See the chapter [Authoring and Exporting Animations with Blender](blender-export.md) for known issues.

* `FirstFrame`, `NumFrames`: It is best to put every animation into a separate clip and export them that way. However, sometimes files contain only a single animation and each clip is found at another interval. By specifying the index of the first frame and the number of frames to use, you can extract individual clips from such data. Note that setting NumFrames to zero always means to use all the remaining frames after the first frame.

  **Note:** It can be difficult to know the exact indices. Sometimes the data is authored at 24 frames per second and also exported that way, then you can plug in the numbers straight away. However, GLTF/GLB files are always exported at 1000 FPS. That means if your animation clip was authored with 24 FPS and starts at the one second mark, in the GLB file this wouldn't be at keyframe 24, but instead at keyframe 1000.

* `Additive`, `AdditiveReference`: If enabled, the animation clip will be applied as an *additive* animation. See [this page](https://guillaumeblanc.github.io/ozz-animation/samples/additive) for an explanation of the concept.

  To calculate the difference, a reference pose is needed. You can select either the first or last keyframe as the reference.

  > **Important**
  >
  > Additive animations usually only work well, if they are applied to a skeleton that is in a similar pose as the reference pose of the additive animation. The animation clip window always displays the animation on top of the *rest pose*. This can look very broken, especially when the rest pose is a proper *T-pose* or *A-pose*.

* `RootMotion`: If the animation clip should be able to move the [game object](../../runtime/world/game-objects.md), this can be achieved through [root motion](root-motion.md). This option allows you to select how root motion should be incorporated into the animation clip.

  For the time being the only mode available is *constant motion*, which means that when this clip is played, the parent object will be moved at a constant speed into a single direction. This can be used for walking animations, but it might be tricky to avoid *foot sliding*.

  * `ConstantRootMotion`, `RootMotionDistance`: The constant motion is separated into a direction and distance value. If the distance is non-zero, the direction value is rescaled to this length. This makes it easier to define diagonal directions. E.g. you can use the value `(1, 1, 0)` as direction and `1` as length, and don't need to *normalize* the direction yourself to `(0.7, 0.7, 0)`.

    > **Automatic Extraction:**
    >
    > Constant root motion can be estimated automatically by the editor for you. Click the button *Extract Root Motion From Feet* in the toolbar, or from the *Asset* main menu. The editor then samples the animation clip and estimates how the feet would move the character to determine an average direction and speed. For this to work, the [skeleton](skeleton-asset.md) must specify which bones are the left and right foot bones. Upon success, it fills out the root motion direction value. You can then adjust the value, for example, it is often necessary to remove unwanted motion along the Z axis.

* `AdjustScale`: Allows you to scale the position data of the animation clip during import. This is useful if the animation was authored or exported at a different scale than the mesh. The default value is `1.0` (no scaling).

* `AvailableClips`: When you manually *transform* the asset, this list shows all the animation clips that have been found in the given file. Use this information to fill out the `UseAnimationClip` property.

## Playback

The toolbar buttons allow you to play/pause/reset and slow-down the animation playback. Additionally you can use the **time scrubber** right below the 3D viewport to manually play the animation. It is best to pause the automatic playback then.

## Event Track

Below the time scrubber there is an additional strip to edit [animation events](animation-events.md). Here you can add events that shall occur at specific times during the animation clip playback, such as *foot-down* or *fire-weapon*. Use the time scrubber above to play the clip and inspect at which time the event shall occur. Then *right click* into the event track and select **Add Event**. Which type of event will be added is specified with the combo box at the bottom right.

## See Also

* [Skeletal Animations](skeletal-animation-overview.md)