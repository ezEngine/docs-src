# Mouse Cursor

The engine can display a custom mouse cursor, meaning a cursor that is drawn by the engine itself, rather than by the operating system. This is often called a *software cursor*. Since it is just an image that the engine renders, it can use the same artwork as the rest of the game, and it can be animated, tinted and rotated at runtime.

The mouse cursor is also affected by two related settings: whether the OS cursor is visible at all, and whether the mouse is confined to the application window.

## Displaying a Custom Cursor

`ezInputManager::SetMouseCursor()` takes an `ezMouseCursorDesc` that describes what the cursor should look like:

```cpp
ezMouseCursorDesc cursor;
cursor.m_sCursor = "{ d4aca571-6900-48aa-93c6-3d388f551f50 }"; // a texture asset

// the tip of the arrow is in the top-left corner of the image
cursor.m_vHotspot.Set(0.0f);

ezInputManager::SetMouseCursor(cursor);
```

Setting a custom cursor hides the OS cursor automatically. `ezInputManager::ClearMouseCursor()` (or an empty `m_sCursor`) switches back to the OS cursor.

The cursor is drawn on top of everything else, even while no [world](../runtime/world/worlds.md) is loaded. Calling `SetMouseCursor()` every frame, for example from your [game state](../runtime/application/game-state.md) update, is inexpensive, so the cursor can be animated, rotated or tinted freely.

### Cursor Description

| Member | Description |
|--------|-------------|
| `m_sCursor` | Which image to display. This is the GUID or the path of either a [texture](../graphics/textures-overview.md) or a [material](../materials/materials-overview.md) asset. An empty string means that no custom cursor is used. |
| `m_fSize` | Scales the size of the cursor image. |
| `m_vHotspot` | The point of the image that sits exactly on the mouse position, in normalized coordinates. `(0,0)` is the top-left corner, `(0.5,0.5)` the center. This is also the pivot around which the rotation is applied. |
| `m_vUvTopLeft` / `m_vUvBottomRight` | The sub-rectangle of the image to display. Use this for texture atlases and animated cursors. |
| `m_Rotation` | Rotation of the image around its hotspot. Positive angles rotate clockwise on screen. |
| `m_Color` | The image is multiplied with this color. Useful for state changes without extra artwork. |

### Cursor Size

By default (`m_fSize` at 1) the custom cursor is rendered at the size of the OS cursor, which takes both the DPI scaling of the display and the mouse pointer size from the user's system settings into account. The cursor therefore matches the size that the player expects on any monitor, resolution and window size. Only change `m_fSize` to deliberately deviate from that. `ezInputManager::GetHardwareCursorSize()` returns the size in pixels, if you need it yourself.

### Using a Material

If `m_sCursor` refers to a texture asset, the cursor is drawn with the built-in `Shaders/MouseCursor/MouseCursor.ezShader`. Pointing it at a [material](../materials/materials-overview.md) asset instead allows for arbitrary cursor effects.

A custom cursor material has to follow these rules:

* Its vertex shader has to `#include <Shaders/MouseCursor/MouseCursorCommon.h>` and return `ezMouseCursorVertex(VertexID)`, or do the equivalent math itself, using `ezMouseCursorConstants`.
* It has to set up its own render state (no depth test, no culling, alpha blending).
* It must not use constant buffer slot 3 in the `EZ_GAL_BIND_GROUP_FRAME` bind group, since that one holds `ezMouseCursorConstants`.
* It must not declare permutation variables and it must not read `ezGlobalConstants`, except for the time constants. Neither is in a defined state while the cursor is rendered.

## OS Cursor Visibility and Clipping

Two functions on `ezInputDeviceMouseKeyboard` control the OS cursor:

* `SetShowMouseCursor()` shows or hides it inside the application window.
* `SetClipMouseCursor()` confines the mouse to the window, using one of the `ezMouseCursorClipMode` values. Confining the mouse is usually wanted, to prevent accidental task switches, especially on multi-monitor systems. Don't use it when you have multiple windows and need absolute mouse positions.

Both of these express what the *application* wants. Overlays may temporarily override it, and once they stop doing so, the state requested here is restored automatically, so callers never have to save and restore it themselves. `GetShowMouseCursor()` and `GetClipMouseCursor()` return what the application requested, ignoring any overrides.

### Overrides

Overlay UI, such as the [in-game console](../debugging/console.md) or a debug UI, typically needs the OS cursor to be visible, even while the game hid it or displays a custom cursor. Such code registers an *override* instead of changing the application's request:

```cpp
// as a member of the overlay, requested and released as it is shown and hidden
ezMouseCursorOverrideRequest m_CursorOverride;

// ...
m_CursorOverride.Request(); // while the overlay is open
m_CursorOverride.Release(); // when it closes
```

`ezMouseCursorOverrideRequest` releases its override automatically when it is destroyed, so it can also be used as a scope guard by passing the desc to its constructor.

An `ezMouseCursorOverrideDesc` determines what the override does:

* `m_OSCursor` is one of `ezMouseCursorOverride::ForceOSCursor` (the OS cursor is forced to be visible and the custom cursor is not drawn), `ForceHidden` (the OS cursor is forced to be hidden, a custom cursor is still drawn) or `None` (no change).
* `m_bForceNoClip` forces `ezMouseCursorClipMode::NoClip`, so that the mouse can leave the window, no matter what the application requested.

The defaults are `ForceOSCursor` with `m_bForceNoClip` set to true, which is what overlay UI usually wants.

Multiple overrides can be active at the same time and the most recently requested one wins, so several overlays don't stomp each other. `ezInputManager::PushMouseCursorOverride()` and `PopMouseCursorOverride()` may be used directly, but `ezMouseCursorOverrideRequest` is preferred, since it cannot leak an override. Both may only be called from the main thread.

`ezInputManager::IsCustomMouseCursorActive()` returns whether a custom cursor is set and is not currently suppressed by an override.

## Rendering

The custom cursor is rendered by `ezMouseCursorRenderer` in the *GameEngine* library. A game that derives from `ezGameState` doesn't need to set this up, it is pointed at the main window automatically.

The cursor is not drawn as part of a [render pipeline](../graphics/render-pipeline/render-pipeline-overview.md), so it is not affected by post-processing, and it is visible even while a scene is still loading.

## See Also

* [Input System](input-overview.md)
* [Game States](../runtime/application/game-state.md)
* [Materials](../materials/materials-overview.md)
