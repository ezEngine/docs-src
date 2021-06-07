# Fmod Sound Event Asset

The *sound event asset* represents a single Fmod sound event. An event typically represents an actual sound, but may also be something like a reverb effect. Sound events are very versatile, for details refer to the Fmod documentation.

You don't create sound event assets. Instead, when you transform a [sound bank asset](fmod-soundbank-asset.md), for every event in the Fmod sound bank, one sound event asset appears in the [asset browser](../assets/asset-browser.md).

Sound event assets are *virtual assets*, they don't have a representation on disk. They mainly exist as a UI element, such that you can browse for and select them in the [sound event component](fmod-event-component.md).

You can also instantiate sound events by dragging a sound event asset from the asset browser into a scene. This will automatically create a [game object](../runtime/world/game-objects.md) and attach an [Fmod event component](fmod-event-component.md).

## See Also


* [Fmod Integration](fmod-overview.md)
* [Fmod Sound Bank Asset](fmod-soundbank-asset.md)
* [Assets](../assets/assets-overview.md)
