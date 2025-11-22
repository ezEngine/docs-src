# RTS Sample

The **RTS Game Plugin** is a more complex example of how to write a plugin that adds custom components and game logic. It also demonstrates how to build a complete user interface using [RmlUi](../docs/ui/rmlui.md).

![RTS1](media/rts1.jpg)

## Project

The editor project belonging to this sample can be found under *Data/Samples/RTS*.

Open the *Main* scene document. Make sure to transform all assets (in the *AssetBrowser* panel the box with the red arrow). Then press 'Play the Game' in the scene. Use the mouse to create, select and send ships around.
Further usage instructions are listed by the game UI.

## User Interface

The sample features a complete UI implementation using RmlUi:

* **In-game HUD**: Shows game information and instructions.
* **Main Menu**: Press `ESC` to open the main menu with settings and example UI components.
* **Settings Panel**: Includes UI scaling options to demonstrate dynamic UI resizing.
* **Resizable Window**: The game window can be resized to see how the UI adapts to different resolutions.

![RTS3](media/rts3.jpg)

The sample also includes a default RmlUi stylesheet that can serve as a starting point for other projects.

## Code

The code shows how to use a custom ezGameState for high-level game logic, as well as a number of custom ezComponent classes for various different game elements. It also demonstrates how to communicate with RML UI elements.

## See Also

* [Samples](samples-overview.md)
* [RmlUi](../docs/ui/rmlui.md)
* [Videos](../getting-started/videos.md)