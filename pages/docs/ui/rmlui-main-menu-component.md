# RmlUI Main Menu Component

The *RmlUi Main Menu* component (`ezRmlUiMainMenuComponent`) provides a main menu with a settings page, without any code or UI authoring. Add it to any object in a scene, and pressing *ESC* opens a menu with *Resume*, *Settings* and *Exit*.

This exists so that samples and new projects have a way to leave the application and to change the most common settings. A finished game will usually want its own menu, either by replacing the documents that this component displays, or by building the UI from scratch, as the [RTS sample](../../samples/rts.md) does.

## How it is opened

[ezFallbackGameState](../runtime/application/game-state.md) searches the world for a main menu component. If it finds one, pressing *ESC* opens the menu instead of quitting the application. *ESC* then goes back one page at a time, and closes the menu from the top level page.

`Ctrl+Q` always quits, no matter whether the menu is open. Inside ezEditor both the *Exit* button and `Ctrl+Q` stop the play-the-game mode, rather than the editor.

Note that `Ctrl+Q` is only registered in development builds. In an exported game the menu's *Exit* button is the way out.

A custom game state can drive the menu through the `ezMainMenuComponent` interface:

```cpp
#include <GameEngine/UI/MainMenuComponent.h>

ezComponentHandle hMenu = ezMainMenuComponent::FindInWorld(*pWorld);

ezMainMenuComponent* pMenu = nullptr;
if (pWorld->TryGetComponent(hMenu, pMenu))
{
  pMenu->SetMenuPage(ezMainMenuComponent::Page::Menu);
}
```

`ezMainMenuComponent` is declared in the *GameEngine* library and knows nothing about RmlUi, so game code that only opens and closes a menu does not have to depend on the [RmlUi](rmlui.md) plugin.

## Component Properties

**Menu File:** The document to display for the top level menu. Defaults to the built-in `rmlui-menu/ez-main-menu.ezRmlUiAsset`.

**Settings File:** The document to display for the settings page. Defaults to the built-in `rmlui-menu/ez-app-settings.ezRmlUiAsset`. Clearing this leaves the menu without a settings page.

**Sound Groups:** One volume slider is added to the *Audio* tab for each entry. *Label* is what the menu shows, *Sound Group* is what is passed to `ezSoundInterface::SetSoundGroupVolume()`. What a group name means depends on the sound plugin: [MiniAudio](../sound/miniaudio/ma-overview.md) uses the names from its sound group configuration, FMOD expects the GUID of a VCA. The list is empty by default, so the *Audio* tab only offers the master volume until groups are added. `Music` and `Effects` are what the sample projects configure. Without a sound plugin the sliders are disabled.

**Input Sets:** The input sets whose actions the *Controls* tab offers for rebinding. When this is empty, every input set is listed, except the ones that the engine registers for itself (the console, the debug keys of `ezGameApplication`, the scene switching of *ezPlayer*, the menu itself). Set this to the input set that the game's own actions use (`Player` in the sample projects) to keep the actions of other systems out of the menu.

**Pause World:** Whether the world's clock is paused while the menu is open (enabled by default). The world keeps updating, it just does not advance in time, so the UI stays responsive while the game is frozen. A world that was already paused when the menu opened stays paused when it closes.

## Build information

The lower right corner of the menu shows the engine version, the build configuration, the platform and the date on which the engine was built. This is meant for bug reports from testers, who otherwise have no way to tell which build they are running.

## Saved settings

What the user picks is stored in CVars whose names start with `Options.`, for example `Options.Graphics.ShadowQuality` or `Options.Audio.MasterVolume`. These carry the `Save` flag, so they end up in `:appdata/CVars` and are read back at startup.

They are deliberately separate from the engine's own CVars: a quality selection is a single number that means 'Medium', while the engine is configured through several unrelated values (shadow atlas size, mip drop, ...). Only the selection is worth saving and showing, the mapping to the engine's CVars is what `ezRmlUiMainMenuComponent::ApplySettings()` does. A game that offers its own menu would do the same.

The component applies these settings when it is activated, which is how the settings of a previous run take effect. *Restore Defaults* resets the settings of the tab that is open to the value they were declared with. Which ones those are is decided by which widgets are visible, so it also works in a document with a different tab layout.

The volumes of the sound groups are an exception: how many groups there are is only known once a scene is loaded, whereas CVars have to exist before the settings file is read, so they all go into `Options.Audio.SoundGroupVolumes` as a list of `group=volume` pairs.

## Settings

The settings page has four tabs, and writes to [CVars](../debugging/cvars.md), to the sound system and to the window configuration:

* *General*: *Player Name* is stored in `Options.Game.PlayerName` and read by nothing - it is there as an example of a text field. *Show FPS* maps to the `App.ShowFPS` CVar, *UI Scale* scales the menu's own canvases.
* *Graphics*: The window mode is a pair of radio buttons, the rest of the display settings are drop downs. *V-Sync* maps to `App.VSync`, *Texture Filtering* to `Rendering.TextureQuality`, *Texture Quality* to `Rendering.Textures.DropMips` and `Rendering.Textures.MaxResolution`, *Shadow Quality* to the shadow atlas CVars. Quality settings are presets, rather than individual values, so that they can be presented as a single choice. The same tab holds the window mode, the monitor and the resolution. *Apply* writes those to `:appdata/RuntimeConfigs/Window.ddl`, which the next start of the application prefers over the project's own `Window.ddl`.
* *Audio*: *Master Volume* goes through `ezSoundInterface::SetMasterChannelVolume()`, *Music* and *Effects* through `ezSoundInterface::SetSoundGroupVolume()` with the group names from the component's properties. Without a sound plugin the sliders are disabled and the tab says so.
* *Controls*: One row per input action, see below.

Exclusive fullscreen is deliberately not offered, because it changes the resolution of the display itself, which cannot be applied to a window that already exists. Applying the display settings without a restart requires `ezWindowPlatformShared::Reconfigure()`, which is currently only implemented on Windows. Elsewhere the settings are saved and take effect after a restart, which the page states.

## Key bindings

The *Controls* tab lists the input actions of the game, taken from the [input manager](../input/input-overview.md) at the moment the component is activated, with one column per alternative trigger of an action.

Clicking a binding makes it wait for a key, mouse button or controller button; the next one that is pressed is bound to that action, and *ESC* cancels the change without closing the page. Only inputs that can be *pressed* can be picked up this way - an axis such as the mouse movement or a thumb-stick can be bound to an action, but there is no moment at which the user presses it, so the menu can only show such a binding, not create one. *X* removes all bindings of an action.

Binding a slot removes it from the other actions of the same input set, since otherwise both would be triggered at once. Binding a slot that the same action is already bound to moves it, rather than having it twice: the alternative triggers of an action are alternatives, so the same slot in two of them would do nothing twice.

Changed bindings are written to `:appdata/RuntimeConfigs/InputConfig.ddl`, in the same format as the project's own `RuntimeConfigs/InputConfig.ddl`. `ezGameApplication` reads that file after the project's, so the bindings are in effect from the next start, and the component applies it again when it is activated, because a game state configures its input actions after the application does.

*Restore Defaults* on this tab deletes that file and reads the project's configuration back from disk, so the player ends up with what the project ships with - including changes that were made in the editor while the game was running. Actions that are registered in code (as `ezFallbackGameState` does for its `Game` actions) do not appear in that file, so for those the component restores the bindings that they had when it was activated.

## Keyboard navigation

The pages can be used without a mouse: the component focuses the first button when a page opens, and RmlUi moves the focus with the arrow keys from there (see the `nav` property in the RCSS files). *Enter* and *Space* activate the focused element.

## Using the documents as an RmlUi example

Besides being a working menu, the two documents show most of what a settings UI needs from [RmlUi](rmlui.md): a tab set, tables, buttons, check boxes, sliders, drop downs, radio buttons, a text field, both image types, and rows that are generated from C++ at runtime (the sound groups and the key bindings). The component's implementation next to them shows the other half: how each widget is read and written, and which of that may happen on the world update's worker thread.

The two image types are separate elements: the logo on the menu page is a vector image (`<svg src="ez.svg"/>`), which is rasterized at the size that the layout gives it and therefore stays sharp at any UI scale, while the icon above the tabs of the settings page is a raster image (`<img src="ez.png"/>`). A raster image is loaded through the ez resource system, so its `src` takes a texture asset just as well as the file that ships next to the document.

## Replacing the documents

The built-in documents live in `Data/Plugins/RmlUiPlugin/rmlui-menu/`, next to the default RmlUi styles, so they are available in every project that has the RmlUi plugin enabled. To change how the menu looks, copy them into your project, adjust them, and point the *Menu File* and *Settings File* properties at your copies.

The component addresses the widgets by their element IDs, and the buttons by the identifiers in their `onclick` and `onchange` attributes, so those have to be kept. A widget that a document does not contain is simply skipped, which is how a stripped down settings page can be built: remove the rows that should not be offered and leave the rest alone.

