# RmlUI Canvas 3D Component

The *RmlUI Canvas 3D Component* renders [RmlUi](rmlui.md) user interfaces onto 3D meshes in world space. This allows you to create interactive UI elements that exist as part of the 3D scene, such as computer terminals, interactive screens, holographic displays, or any other in-world interface.

![RmlUI 3D Canvas](media/rmlui-canvas3d.jpg)

The 3D canvas component projects the UI onto a mesh surface in the game world where it can be interacted with through raycasts. This is ideal for any interface that should exist as a physical object in your scene rather than as a screen overlay.

## 3D vs 2D Canvas

The key differences between the 3D and 2D canvas components:

| Feature | 3D Canvas | [2D Canvas](rmlui-canvas2d-component.md) |
|---------|-----------|------------------------------------------|
| **Rendering** | On 3D mesh surfaces | Screen overlay |
| **Positioning** | World space | Screen coordinates |
| **Input** | Raycast-based | Direct mouse/keyboard |
| **Use Cases** | Terminals, displays, holograms | Menus, HUDs, dialogs |

Use the 3D canvas when you need UI that exists as part of the 3D scene. Use the [2D canvas](rmlui-canvas2d-component.md) when you want standard overlay UI elements that appear on top of your game view.

## How It Works

The 3D canvas component renders the RmlUi interface to a texture and applies it to a 3D mesh material. The component:

1. Creates a unique material based on the provided base material
2. Renders the UI to a texture at the specified resolution
3. Assigns the texture to the material's designated texture slot
4. Sends the material to the target game object's mesh renderer

## Setting Up a 3D UI

To create a 3D UI in your scene:

1. Add a game object with a mesh renderer component
2. Add the *RmlUI Canvas 3D Component* to the same object (or a parent object)
3. Assign an [RmlUi asset](rmlui.md) to the component's `Document` property
4. Set up the material properties:
   - `BaseMaterial`: A material that will be used as a template
   - `TextureSlotName`: The name of the texture parameter in the material (e.g., "BaseTexture")
   - `MaterialIndex`: Which material slot on the mesh to apply to (default: 0)
5. Configure the texture size and DPI scaling as needed

## Input and Interaction

The 3D canvas supports interactive elements through raycast input. To send input to the canvas:

- Use `RaycastInput()` from code with a ray origin and direction
- The component performs ray-triangle intersection testing to determine where the ray hits the mesh
- The hit location is converted to UV coordinates, which map to the UI canvas
- Mouse and keyboard input can then be processed at that location

### Hit Testing

The component uses the attached mesh for hit testing by default. You can optionally specify a separate `ProxyMesh` for hit detection:

- Useful for simplified collision geometry
- Falls back to basic geometric primitives if the mesh is simple
- Improves performance for complex meshes

## Component Properties

### UI Content

* `Document`: The [RmlUi document asset](rmlui.md) to display
* `TextureSize`: Resolution of the UI texture (e.g., 1024x1024). Higher resolutions provide sharper UI but use more memory
* `DpiScale`: Scales the UI elements. Values > 1.0 make elements larger, < 1.0 makes them smaller

### Material Settings

* `BaseMaterial`: The material asset used as a template. The component will create a unique instance of this material
* `TextureSlotName`: Name of the texture parameter in the material where the UI texture will be assigned
* `MaterialIndex`: Which material slot on the target mesh to apply to (usually 0)

### Input Settings

* `Interactive`: Whether the UI can receive input events. Disable for non-interactive displays
* `ClearStaleInput`: Automatically clears input that hasn't been updated recently, preventing stuck inputs

### Advanced

* `ProxyMesh`: Optional separate mesh used only for ray intersection testing. Use this to simplify hit detection on complex meshes

## Example Use Cases

- **Computer Terminals**: Interactive screens showing game information or controls
- **Holographic Displays**: Floating UI panels in sci-fi environments
- **Interactive Signs**: Information boards or kiosks in the game world
- **Vehicle Dashboards**: Cockpit displays with functional controls
- **Shop Interfaces**: In-world menus for purchasing or inventory management

## Code Example

To interact with a 3D RmlUi canvas from C++ code:

```cpp
ezRmlUiCanvas3DComponent* pCanvas;
// ... get component reference ...

// Send raycast input
ezVec3 vRayOrigin = ...; // Camera position
ezVec3 vRayDir = ...;    // Ray direction from camera
ezRmlUiInputSnapshot input; // Configure input state
pCanvas->RaycastInput(vRayOrigin, vRayDir, input);

// Access the RmlUi context
ezRmlUiContext* pContext = pCanvas->GetRmlContext();

// From here you can use standard RmlUi API
// See RmlUi documentation: https://mikke89.github.io/RmlUiDoc/
```

The Testing Chambers sample contains an example scene demonstrating 3D canvas usage.

## Live Preview and Editing

The ezEngine editor provides a live preview for RmlUi canvases. When you edit the `.rml` or `.rcss` files referenced by your UI document, the changes will be reflected immediately in the editor viewport. This makes it easy to iterate on your UI design.

Additionally, CSS files (`.rcss`) automatically trigger asset reloading when modified, so changes to stylesheets are instantly visible without manual refresh.

## Performance Considerations

- Higher `TextureSize` values provide better quality but use more GPU memory and rendering time
- The UI is rendered every frame by default
- Consider using a `ProxyMesh` for complex geometry to optimize hit testing
- Disable `Interactive` on purely visual displays to skip input processing

## See Also

* [RmlUi](rmlui.md)
* [RmlUI Canvas 2D Component](rmlui-canvas2d-component.md)
* [Ingame UI](ui.md)
