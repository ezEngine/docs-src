# RmlUI Canvas 2D Component

The *RmlUi Canvas 2D* component (`ezRmlUiCanvas2DComponent`) renders an [RmlUi](rmlui.md) document as a screen-space overlay. This is the standard choice for HUDs and menus.

## Component Properties

### Base Properties

These properties are shared with the [RmlUI Canvas 3D Component](rmlui-canvas3d-component.md).

**Rml Resource:** The `.rml` document file to load and render.

**Autobind Blackboards:** When enabled, the component searches the owner object's hierarchy for a [blackboard](../misc/blackboards.md) component and binds it automatically. The blackboard's name is used as the RmlUi model name, making its entries accessible as RmlUi data model variables. You can also bind blackboards manually from C++ using `ezRmlUiCanvasComponentBase::AddBlackboardBinding()`. Both scalar values and [variant arrays](https://mikke89.github.io/RmlUiDoc/pages/data_bindings.html) stored in the blackboard are supported.

**Send Event Message:** When enabled, every RmlUi event (such as a button click) fires an `ezMsgRmlUiEvent` message on the component's owner object. The message carries:

* `m_sIdentifier` — the identifier string configured on the RmlUi element (e.g. via the `data-event-id` attribute or the event listener identifier).
* `m_sType` — the RmlUi event type (e.g. `click`, `change`).

This message can be handled in [visual scripts](../custom-code/visual-script/visual-script-overview.md) or C++ components attached to the same object, enabling script-driven UI logic without writing a custom C++ event handler. As an alternative, you can register C++ event handlers directly via `ezRmlUiContext::RegisterEventHandler()`.

**On Demand Update:** When enabled (the default), the canvas texture is only re-rendered when something has changed. Disable this to force a re-render every frame.

### 2D-Specific Properties

**Offset:** A 2D pixel offset (in screen pixels) applied to the canvas position. Combined with **Anchor Point**, this determines where on screen the canvas appears.

**Size:** The resolution of the RmlUi canvas in pixels. This also determines the canvas's logical coordinate space for RmlUi layout.

**Anchor Point:** A normalized (0–1) 2D value that controls which corner or point of the canvas is placed at the screen anchor. `(0, 0)` anchors the top-left corner; `(1, 1)` anchors the bottom-right corner.

**Pass Input:** When enabled, mouse and keyboard input is forwarded to the RmlUi context for interaction. Disable this to make the canvas non-interactive (display only).

**Custom Scale:** A scaling factor applied to the canvas. Useful for adapting to different screen densities or for visual effects. Defaults to `1.0`.

## Interaction

Input is forwarded automatically when **Pass Input** is enabled. For programmatic interaction, call `ReceiveInput()` with a canvas-space mouse position and an `ezRmlUiInputSnapshot`.

## See Also

* [RmlUi](rmlui.md)
* [RmlUI Canvas 3D Component](rmlui-canvas3d-component.md)
* [Ingame UI](ui.md)
* [Blackboards](../misc/blackboards.md)
