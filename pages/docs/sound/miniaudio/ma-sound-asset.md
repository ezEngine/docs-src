# MiniAudio Sound Asset

The *MiniAudio sound asset* represents one in-game sound. The asset references *WAV* or *MP3* files and it can randomize the playback by choosing from a list of sounds and also by applying random pitch and volume.

A sound asset may be set to be *positional*, which means that its location influences how audible it is, or it may be non-positional, in which case the sound is always audible in exactly the same way. Non-positional sounds are typically used for UI sounds or in games that do not need it. For instance, the [PacMan sample](../../../samples/pacman.md) uses only non-positional sounds, since everything is always on-screen anyway.

Sound assets are used by [MiniAudio sound components](ma-sound-component.md), which instantiate and play the sounds in the world.

You can instantiate sounds by dragging a sound asset from the asset browser into a scene. This will automatically create a [game object](../../runtime/world/game-objects.md) and attach a [sound component](ma-sound-component.md).

## Asset Properties

* `Files`: A list of sound files. Every time a sound gets played, a random sound file is chosen. Every sound asset has to have at least one such input file.

* `Group`: What sound group this sound belongs to. Sometimes also called a *bus* or *VCA* (*Voltage Controlled Amplifier*). Usually something like *music*, *effects*, *background* or *ui*. The game code can control the volume of groups through the `ezSoundInterface`.

* `Loop`: Whether to play the sound in a looping fashion. If there are multiple input files, one random file is chosen and then that one file is played in a loop. If instead you want to loop the playback and play random files each time, use the `Restart` option on the [MiniAudio sound component](ma-sound-component.md) instead.

* `MinRandomVolume`, `MaxRandomVolume`: Every time a sound gets played, the volume of the sound is randomized between these two values.

* `MinRandomPitch`, `MaxRandomPitch`: Every time a sound gets played, the pitch of the sound is randomized between these two values. Even just a small random pitch is enough to prevent a sound from sounding repetative, so it is a good idea to use this for the majority of effect sounds.

* `IsPositional`: If true, the sound will be attenuated according to the distance and direction towards the listener. If disabled, the sound will always sound identical, which is useful for UI sounds.

* `DopplerFactor`: How strong the [Doppler Effect](https://en.wikipedia.org/wiki/Doppler_effect) shall be for this sound. Be careful to only enable this for sounds that really need it, since it costs additional performance and often sounds broken, since game characters typically move way faster than possible in real life. This is only relevant for positional sounds.

* `SoundSize`: How large the sound source is in the world. Within this radius, sounds are always equally loud and appear to be coming from all directions. Be careful not to set this too large, as it also affects how far a sound can be audible, at all. This is only relevant for positional sounds.

* `Rolloff`: How quickly a sound drops in volume over distance. This is only relevant for positional sounds.

## See Also

* [MiniAudio Integration](ma-overview.md)
* [MiniAudio Sound Component](ma-sound-component.md)
* [Assets](../../assets/assets-overview.md)
