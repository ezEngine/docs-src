# RmlUi

[RmlUi](https://github.com/mikke89/RmlUi) is a third-party GUI library that uses an HTML-like syntax to describe UI elements, and CSS to style them. RmlUi is lightweight, yet flexible.

![RmlUi](media/rmlui.jpg)

Support for RmlUi is provided through a dedicated [engine plugin](../custom-code/cpp/engine-plugins.md). To enable it in your project, activate the plugin in the [project settings](../projects/project-settings.md).

## Rml Documentation

The documentation for RmlUi [can be found here](https://mikke89.github.io/RmlUiDoc/index.html).

Please refer to that documenation for any questions around how to use RmlUi.

## Sample

The [RTS Sample](../../samples/rts.md) shows how to use RmlUi. Have a look at it the project in the editor, it contains Rml assets. The editor shows a live preview for Rml canvases, and you can edit the respective `.rml` files to see the effect:

![Edit RmlUi](media/rml-edit.jpg)

The sample uses multiple *RmlUi Canvas 2D* components in its scene to place the UI elements. At runtime the RTS sample's game code accesses the RmlUi functionality through the `ezRmlUiCanvas2DComponent`. Search the sample's code for those places to see how to interact with the GUI.

Using `ezRmlUiCanvas2DComponent::GetRmlContext()` you get access to the `ezRmlUiContext`. This class implements `Rml::Core::Context`. This gives you access to all the RmlUi features. See the RmlUi [documentation](https://mikke89.github.io/RmlUiDoc/index.html) for details.

## Canvas Components

ezEngine provides two canvas components for placing RmlUi documents in a scene:

* The [RmlUI Canvas 2D Component](rmlui-canvas2d-component.md) (`ezRmlUiCanvas2DComponent`) renders the UI as a screen-space overlay. This is the standard choice for HUDs and menus.
* The [RmlUI Canvas 3D Component](rmlui-canvas3d-component.md) (`ezRmlUiCanvas3DComponent`) renders the UI into a texture applied to a mesh in the scene, allowing UI panels to exist as physical objects in the 3D world.

Both components support blackboard data binding, event messages, and on-demand rendering. See the individual component pages for their full property reference.

## Localization

All text content in RmlUi documents is automatically passed through ezEngine's localization system (`ezTranslate`). That means you can set up translation tables for different languages.

## See Also

* [RmlUI Canvas 2D Component](rmlui-canvas2d-component.md)
* [RmlUI Canvas 3D Component](rmlui-canvas3d-component.md)
* [Ingame UI](ui.md)
* [ImGui](imgui.md)
* [Blackboards](../misc/blackboards.md)
