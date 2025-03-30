# MiniAudio Sound Component

The *MiniAudio sound component* plays an instance of a [MiniAudio sound asset](ma-sound-asset.md) at its location.

It will randomize the sound playback according to the sound asset properties.

If the sound is positional, the location of the object is important to determine attenuation and direction in relation to the [listener](ma-listener-component.md). If it is non-positional, the location of the game object is irrelevant.

If the sound asset is configured to be looping, the playback can only be stopped by either deleting the component or object, or by programmatically calling `Stop()` or `FadeOut()` on the component (for instance through a [visual script](../../custom-code/visual-script/visual-script-overview.md)).

## Component Properties

* `Sound`: The [sound asset](ma-sound-asset.md) that will be played by this component.
* `Paused`: If set, the referenced sound won't start playing at start. Toggling this value programmatically will pause/resume a playing sound.
* `Volume`: Adjusts the volume for this sound.
* `Pitch`: Higher pitch means the sound plays faster, a lower pitch makes it play slower (and at lower frequency).
* `NoGlobalPitch`: If disabled, changing the [world](../../runtime/world/worlds.md) clock speed (game speed) also affects the playback of sounds. For instance, slowing down time will make sounds play back slower and at lower frequency. For sounds where this is not desired, enable this option.
* `OnFinishedAction`: For sounds that end by themselves, this option allows you to specify whether the component should delete itself or its entire object afterwards, or restart the sound playback to create a looping effect that includes randomization.

## Component Script Functions

* `Play()`: Starts or resumes playing the sound, if it isn't already playing.
* `Pause()`: Pauses a currently playing sound.
* `Stop()`: Stops (and rewinds) playback of a sound. If followed by `Play()` the sound will be played from the beginning.
* `FadeOut(duration)`: Similar to `Stop()` but fades the sound out over the given duration for a less jarring stop.
* `StartOneShot()`: Plays an instance of the sound at the current location and with the current properties of the component, but detatches it from the component. Only allowed for non-looping sounds. When this is used, the component is typically not used for playback itself.

## See Also

* [MiniAudio Integration](ma-overview.md)
* [MiniAudio Sound Asset](ma-sound-asset.md)
* [MiniAudio Listener Component](ma-listener-component.md)
