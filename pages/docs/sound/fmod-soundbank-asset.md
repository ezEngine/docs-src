# FMOD Sound Bank Asset

The *sound bank asset* is used to import data from an FMOD sound bank into the engine, and expose FMOD events as [sound event assets](fmod-soundevent-asset.md).

FMOD Studio (the tool to edit FMOD projects) stores all sound data in so called *sound banks*. A sound bank contains all the necessary meta data about sounds (called 'events') as well as the sound data. The FMOD runtime loads these sound banks into memory and decodes sound data as needed. In an FMOD Studio project you can split up sound data into as many sound banks as you like, which allows you to organize sounds in such a way that not all sound banks need to be loaded at the same time.

To make use of FMOD events inside an FMOD sound bank, you first have to create a sound bank asset in the ezEditor and reference an exported FMOD sound bank file. When you *transform* the sound bank [asset](../assets/assets-overview.md) it will extract the meta information about all the events, and create [sound event assets](fmod-soundevent-asset.md), which appear in the [asset browser](../assets/asset-browser.md).

You can then add [sound events](fmod-event-component.md) to scenes via drag and drop of sound event assets from the asset browser.

## Asset Properties

* `SoundBankFile`: The relative path (from any [data directory](../projects/data-directories.md)) to the exported FMOD sound bank file.

## See Also

* [FMOD Integration](fmod-overview.md)
* [FMOD Sound Event Asset](fmod-soundevent-asset.md)
* [FMOD Event Component](fmod-event-component.md)
