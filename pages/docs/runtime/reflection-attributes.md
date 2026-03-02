# Reflection Attributes

Reflection attributes decorate [reflected](reflection-system.md) types and properties to control how they appear and behave in the editor. Attributes are attached either to a **type** (inside `EZ_BEGIN_ATTRIBUTES` / `EZ_END_ATTRIBUTES`) or to an individual **property** (via `->AddAttributes(...)`).

```cpp
EZ_BEGIN_COMPONENT_TYPE(MyComponent, 1, ezComponentMode::Static)
{
  EZ_BEGIN_PROPERTIES
  {
    EZ_MEMBER_PROPERTY("Radius", m_fRadius)
      ->AddAttributes(new ezDefaultValueAttribute(1.0f), new ezClampValueAttribute(0.0f, ezVariant())),
  }
  EZ_END_PROPERTIES;

  EZ_BEGIN_ATTRIBUTES
  {
    new ezCategoryAttribute("MyPlugin"),
  }
  EZ_END_ATTRIBUTES;
}
EZ_END_COMPONENT_TYPE
```

## Basic Editor Behavior

### `ezReadOnlyAttribute`

The property is displayed in the editor but cannot be modified by the user. Use this for values that are set only by code.

```cpp
EZ_MEMBER_PROPERTY("ComputedValue", m_fComputed)->AddAttributes(new ezReadOnlyAttribute()),
```

### `ezHiddenAttribute`

The property is not shown in the editor at all. It is still serialized and exists in the reflected data, but the user has no way to see or change it.

```cpp
EZ_MEMBER_PROPERTY("InternalState", m_iState)->AddAttributes(new ezHiddenAttribute()),
```

### `ezTemporaryAttribute`

The property is neither shown in the editor nor serialized. It exists only at runtime or during editing. Use this for runtime-only cached data that should not be saved.

```cpp
EZ_MEMBER_PROPERTY("CachedHandle", m_hCached)->AddAttributes(new ezTemporaryAttribute()),
```

## Type-Level Attributes

These are placed on the **type** in an `EZ_BEGIN_ATTRIBUTES` block, not on individual properties.

### `ezCategoryAttribute`

Places the type in a named category in the editor's add-component menu. Use `/` to create sub-categories.

```cpp
EZ_BEGIN_ATTRIBUTES
{
  new ezCategoryAttribute("Effects/Particles"),
}
EZ_END_ATTRIBUTES;
```

### `ezInDevelopmentAttribute`

Marks a component as still in development. The editor typically hides these objects, unless explicitly enabled in the [editor preferences](../editor/editor-preferences.md).

```cpp
EZ_BEGIN_ATTRIBUTES
{
  new ezInDevelopmentAttribute(ezInDevelopmentAttribute::Alpha),
}
EZ_END_ATTRIBUTES;
```

### `ezColorAttribute`

Sets a color used to visually distinguish this type in the editor (e.g. for visual script node headers).

```cpp
EZ_BEGIN_ATTRIBUTES
{
  new ezColorAttribute(ezColorScheme::LightUI(ezColorScheme::Teal)),
}
EZ_END_ATTRIBUTES;
```

### `ezTitleAttribute`

Sets a dynamic title string for a visual script node or embedded struct. Use `{PropertyName}` placeholders to insert the current value of a property into the title.

```cpp
EZ_BEGIN_ATTRIBUTES
{
  new ezTitleAttribute("Set Property '{Name}'"),
}
EZ_END_ATTRIBUTES;
```

## Value and Display Attributes

### `ezDefaultValueAttribute`

Sets the default value for a property. This is what the property is initialized to when a new component is created.

```cpp
EZ_MEMBER_PROPERTY("Speed", m_fSpeed)->AddAttributes(new ezDefaultValueAttribute(5.0f)),
EZ_MEMBER_PROPERTY("Color", m_Color)->AddAttributes(new ezDefaultValueAttribute(ezColor::White)),
```

### `ezClampValueAttribute`

Restricts the range of a numeric property in the editor. Pass `ezVariant()` for no bound in one direction.

```cpp
// Clamp between 0 and 100
EZ_MEMBER_PROPERTY("Percent", m_f)->AddAttributes(new ezClampValueAttribute(0.0f, 100.0f)),
// Clamp to minimum 0, no upper limit
EZ_MEMBER_PROPERTY("Range", m_fRange)->AddAttributes(new ezClampValueAttribute(0.0f, ezVariant())),
```

### `ezSuffixAttribute`

Appends a suffix string to the property value in the editor's display. Useful for making units explicit.

```cpp
EZ_MEMBER_PROPERTY("Distance", m_fDist)->AddAttributes(new ezSuffixAttribute(" m")),
EZ_MEMBER_PROPERTY("Angle", m_fDeg)->AddAttributes(new ezSuffixAttribute(" °")),
```

### `ezMinValueTextAttribute`

Replaces the display of the minimum value with a text label. Commonly used to show "Auto" instead of `0` when zero means automatic computation.

```cpp
EZ_ACCESSOR_PROPERTY("Range", GetRange, SetRange)
  ->AddAttributes(new ezClampValueAttribute(0.0f, ezVariant()), new ezMinValueTextAttribute("Auto")),
```

### `ezExposeColorAlphaAttribute`

For `ezColor` or `ezColorGammaUB` properties, exposes the alpha channel in the color picker. Without this attribute, the alpha channel is hidden.

```cpp
EZ_ACCESSOR_PROPERTY("Color", GetColor, SetColor)->AddAttributes(new ezExposeColorAlphaAttribute()),
```

### `ezGroupAttribute`

Visually groups properties in the editor under a collapsible header. The optional `fOrder` parameter controls the order of groups relative to each other.

```cpp
EZ_BEGIN_PROPERTIES
{
  EZ_MEMBER_PROPERTY("Color", m_Color)->AddAttributes(new ezGroupAttribute("Appearance")),
  EZ_MEMBER_PROPERTY("Size", m_fSize),
  EZ_MEMBER_PROPERTY("Mass", m_fMass)->AddAttributes(new ezGroupAttribute("Physics")),
}
```

## Widget and Picker Attributes

### `ezAssetBrowserAttribute`

Marks a string (or resource handle) property as an asset reference, replacing the text field with an asset browser picker. The type filter specifies which asset types are accepted.

```cpp
EZ_RESOURCE_MEMBER_PROPERTY("Texture", m_hTexture)
  ->AddAttributes(new ezAssetBrowserAttribute("CompatibleAsset_Texture_2D")),
EZ_RESOURCE_MEMBER_PROPERTY("Mesh", m_hMesh)
  ->AddAttributes(new ezAssetBrowserAttribute("CompatibleAsset_Mesh_Static")),
```

The second constructor overload accepts a required asset tag to further filter which assets appear:

```cpp
->AddAttributes(new ezAssetBrowserAttribute("CompatibleAsset_CustomData", "MyTag")),
```

### `ezFileBrowserAttribute`

For string properties that hold a file path (not an asset). Opens a native file dialog with the given title and file type filter. The `ezDependencyFlags` parameter controls how the reference is treated for asset transforms and packaging.

```cpp
EZ_MEMBER_PROPERTY("InputFile", m_sFile)
  ->AddAttributes(new ezFileBrowserAttribute("Choose Input File", "*.fbx;*.gltf")),
```

Predefined type filters are available as static constants: `ezFileBrowserAttribute::Meshes`, `ezFileBrowserAttribute::ImagesLdrOnly`, `ezFileBrowserAttribute::ImagesHdrOnly`, `ezFileBrowserAttribute::ImagesLdrAndHdr`.

### `ezExternalFileBrowserAttribute`

Like `ezFileBrowserAttribute`, but allows browsing outside the project directory. Useful for referencing external executables or system files.

```cpp
EZ_MEMBER_PROPERTY("ExternalTool", m_sPath)
  ->AddAttributes(new ezExternalFileBrowserAttribute("Select Tool", "*.exe")),
```

### `ezDynamicEnumAttribute`

For integer properties, displays a dropdown populated from a named `ezDynamicEnum`. The enum values can change at runtime.

```cpp
EZ_MEMBER_PROPERTY("Layer", m_iLayer)->AddAttributes(new ezDynamicEnumAttribute("PhysicsLayers")),
```

### `ezDynamicStringEnumAttribute`

Like `ezDynamicEnumAttribute`, but for string properties, backed by a named `ezDynamicStringEnum`.

```cpp
EZ_MEMBER_PROPERTY("Preset", m_sPreset)->AddAttributes(new ezDynamicStringEnumAttribute("QualityPresets")),
```

### `ezDynamicBitflagsAttribute`

For integer properties, displays a multi-select checklist populated from a named dynamic bitflags set.

```cpp
EZ_MEMBER_PROPERTY("Flags", m_uiFlags)->AddAttributes(new ezDynamicBitflagsAttribute("CollisionLayers")),
```

### `ezTagSetWidgetAttribute`

For tag set member properties (`EZ_SET_MEMBER_PROPERTY`), displays the tag set editor. The argument is a semicolon-separated list of tag category names to filter the available tags.

```cpp
EZ_SET_MEMBER_PROPERTY("Tags", m_Tags)->AddAttributes(new ezTagSetWidgetAttribute("Default")),
```

### `ezGameObjectReferenceAttribute`

Marks a property as a reference to a game object. The editor shows a game object picker instead of a plain text field.

This attribute requires an **accessor property** (`EZ_ACCESSOR_PROPERTY`). Because the value is stored internally as an `ezGameObjectHandle`, the getter is a dummy that always returns `nullptr`. The setter receives a string reference and resolves it via the world's reference resolver.

```cpp
// Header
const char* DummyGetter() const { return nullptr; }
void SetTargetReference(const char* szReference); // [ property ]

// Cpp - reflection block
EZ_ACCESSOR_PROPERTY("Target", DummyGetter, SetTargetReference)
  ->AddAttributes(new ezGameObjectReferenceAttribute()),

// Cpp - setter implementation
void MyComponent::SetTargetReference(const char* szReference)
{
  auto resolver = GetWorld()->GetGameObjectReferenceResolver();
  if (resolver.IsValid())
    m_hTarget = resolver(szReference, GetHandle(), "Target");
}
```

### `ezRttiTypeStringAttribute`

Turns a string property into a dropdown that lists all reflected types derived from a given base type.

```cpp
EZ_MEMBER_PROPERTY("ComponentType", m_sType)->AddAttributes(new ezRttiTypeStringAttribute("ezComponent")),
```

### `ezImageSliderUiAttribute`

Displays a numeric property as an image-based slider (the image background is generated by a named image generator). Must be combined with `ezClampValueAttribute`.

```cpp
EZ_ACCESSOR_PROPERTY("Temperature", GetTemperature, SetTemperature)
  ->AddAttributes(new ezImageSliderUiAttribute("LightTemperature"),
                  new ezClampValueAttribute(1000, 15000)),
```

## Container Attributes

### `ezContainerAttribute`

Controls which operations (add, delete, reorder) are allowed on an array or set property in the editor.

```cpp
// Allow adding and deleting but not reordering
EZ_ARRAY_MEMBER_PROPERTY("Items", m_Items)
  ->AddAttributes(new ezContainerAttribute(true, true, false)),
```

### `ezMaxArraySizeAttribute`

Limits the maximum number of elements an array property can hold in the editor.

```cpp
EZ_ARRAY_MEMBER_PROPERTY("Slots", m_Slots)->AddAttributes(new ezMaxArraySizeAttribute(8)),
```

### `ezPreventDuplicatesAttribute`

Prevents the user from adding duplicate entries to an array or set. For arrays of objects, this means that multiple objects of the same type are not allowed.

```cpp
EZ_ARRAY_MEMBER_PROPERTY("Behaviors", m_Behaviors)->AddAttributes(new ezPreventDuplicatesAttribute()),
```

### `ezExposedParametersAttribute`

Used on a variant map property to expose the parameters of an asset referenced by another property. The argument is the name of the property that holds the asset reference.

```cpp
EZ_ACCESSOR_PROPERTY("Effect", GetEffectFile, SetEffectFile)
  ->AddAttributes(new ezAssetBrowserAttribute("CompatibleAsset_Particle_Effect")),
EZ_MAP_ACCESSOR_PROPERTY("Parameters", ...)
  ->AddAttributes(new ezExposedParametersAttribute("Effect")),
```

### `ezDynamicDefaultValueAttribute`

Retrieves default values for an embedded class or container property from the asset meta data of an asset referenced by another property. Useful for exposing skeleton bone data or similar asset-driven defaults.

```cpp
EZ_MEMBER_PROPERTY("Skeleton", m_sSkeleton)
  ->AddAttributes(new ezAssetBrowserAttribute("CompatibleAsset_Skeleton")),
EZ_MAP_MEMBER_PROPERTY("BoneTransforms", m_Bones)
  ->AddAttributes(new ezDynamicDefaultValueAttribute("Skeleton", "ezSkeletonMetaData", "Bones")),
```

### `ezNoTemporaryTransactionsAttribute`

Prevents the editor from creating an undo step for every incremental change to a property (such as each keystroke or slider tick). The change is only committed as a single undo step when editing is complete.

```cpp
EZ_MEMBER_PROPERTY("Name", m_sName)->AddAttributes(new ezNoTemporaryTransactionsAttribute()),
```

## Scripting Attributes

### `ezScriptableFunctionAttribute`

Marks a function (declared via `EZ_SCRIPT_FUNCTION_PROPERTY`) as callable from script. The variadic arguments define each parameter's direction (`In`, `Out`, or `Inout`) and display name. This attribute is applied automatically by the `EZ_SCRIPT_FUNCTION_PROPERTY` macro.

```cpp
EZ_BEGIN_FUNCTIONS
{
  EZ_SCRIPT_FUNCTION_PROPERTY(FireProjectile, In, "Direction", In, "Speed"),
  EZ_SCRIPT_FUNCTION_PROPERTY(GetHealth, Out, "Health"),
}
EZ_END_FUNCTIONS;
```

### `ezExcludeFromScript`

Prevents a function or property from being exposed to the scripting system even if it would otherwise qualify.

```cpp
EZ_BEGIN_FUNCTIONS
{
  EZ_FUNCTION_PROPERTY(InternalUpdate)->AddAttributes(new ezExcludeFromScript()),
}
EZ_END_FUNCTIONS;
```

### `ezDynamicPinAttribute`

Marks an array or integer property as the source for dynamically generated pins on a visual script node. The argument is the name of the property that determines the number of pins.

```cpp
EZ_ARRAY_MEMBER_PROPERTY("Inputs", m_Inputs)->AddAttributes(new ezDynamicPinAttribute()),
```

## Miscellaneous

### `ezLongOpAttribute`

Applied to a **type** to register a long-running editor operation (derived from `ezLongOpProxy`) that is triggered by the presence of this component in a scene. The editor will display a button to execute the operation with a progress dialog.

```cpp
EZ_BEGIN_ATTRIBUTES
{
  new ezLongOpAttribute("ezBakingLongOp"),
}
EZ_END_ATTRIBUTES;
```

## Manipulator Attributes

Manipulators add **interactive 3D handles** to the editor viewport for a component's properties. They are placed on the **type** in the `EZ_BEGIN_ATTRIBUTES` block. Property names are passed as strings referring to existing reflected properties.

### `ezSphereManipulatorAttribute`

Displays a draggable sphere handle to edit a radius property. An optional inner radius property can be provided for a double-sphere (e.g. inner/outer radius).

```cpp
new ezSphereManipulatorAttribute("OuterRadius", "InnerRadius"),
```

### `ezCapsuleManipulatorAttribute`

Displays a capsule handle to edit height and radius properties.

```cpp
new ezCapsuleManipulatorAttribute("Height", "Radius"),
```

### `ezBoxManipulatorAttribute`

Displays a box handle to edit a size (vec3) property. `fSizeScale` multiplies the stored value for display. `bRecenterParent` repositions the owner object when the box is resized. Optional offset and rotation properties shift the displayed box.

```cpp
new ezBoxManipulatorAttribute("Extents", 1.0f, false),
new ezBoxManipulatorAttribute("Extents", 1.0f, false, "Offset", "Rotation"),
```

### `ezNonUniformBoxManipulatorAttribute`

Like `ezBoxManipulatorAttribute`, but each of the six faces is driven by a separate property, allowing asymmetric extents. Can be constructed either with six separate properties (`NegX`, `PosX`, `NegY`, `PosY`, `NegZ`, `PosZ`) or with three uniform size properties (`SizeX`, `SizeY`, `SizeZ`).

```cpp
new ezNonUniformBoxManipulatorAttribute("NegX", "PosX", "NegY", "PosY", "NegZ", "PosZ"),
```

### `ezConeLengthManipulatorAttribute`

Displays a draggable cone to edit a length/radius property.

```cpp
new ezConeLengthManipulatorAttribute("ConeRadius"),
```

### `ezConeAngleManipulatorAttribute`

Displays a draggable cone to edit an angle property. `fScale` multiplies the cone length. An optional radius property drives the cone length instead.

```cpp
new ezConeAngleManipulatorAttribute("OuterAngle", 1.0f, "Range"),
```

### `ezTransformManipulatorAttribute`

Displays standard translate/rotate/scale gizmos for separate transform component properties.

```cpp
new ezTransformManipulatorAttribute("LocalPosition", "LocalRotation", "LocalScale"),
```

### `ezBoneManipulatorAttribute`

Displays a bone transform manipulator for skeletal editing. The second argument names the property to bind to.

```cpp
new ezBoneManipulatorAttribute("Transform", "BoneName"),
```

### `ezSplineManipulatorAttribute`

Displays the spline editing handles (control points and tangent handles). References properties for the node array, a closed flag, and a binding target.

```cpp
new ezSplineManipulatorAttribute("Nodes", "IsClosed", ""),
```

### `ezSplineTangentManipulatorAttribute`

Displays tangent editing handles for individual spline nodes. Used on the node struct type.

```cpp
new ezSplineTangentManipulatorAttribute("TangentMode", "CustomTangent"),
```

## Visualizer Attributes

Visualizers draw **non-interactive overlays** in the viewport to show the bounds or shape of a component. Like manipulators, they are placed on the **type** in `EZ_BEGIN_ATTRIBUTES`. An optional `ezVisualizerAnchor` flag can anchor the shape to a face of the component's bounding box instead of its center.

### `ezBoxVisualizerAttribute`

Draws a wireframe box. References a vec3 size property and optionally a color property, an offset property, and a rotation property.

```cpp
new ezBoxVisualizerAttribute("Extents", 1.0f, ezColor::MediumAquamarine),
new ezBoxVisualizerAttribute("Extents", 1.0f, ezColor::White, "BoxColor", ezVisualizerAnchor::Center, ezVec3::MakeZero(), "Offset"),
```

### `ezSphereVisualizerAttribute`

Draws a wireframe sphere. References a radius property and optionally a color property and offset.

```cpp
new ezSphereVisualizerAttribute("Radius", ezColor::MediumAquamarine),
```

### `ezCapsuleVisualizerAttribute`

Draws a wireframe capsule. References height and radius properties.

```cpp
new ezCapsuleVisualizerAttribute("Height", "Radius", ezColor::MediumAquamarine),
```

### `ezCylinderVisualizerAttribute`

Draws a wireframe cylinder. References height and radius properties and a fixed or property-driven axis.

```cpp
new ezCylinderVisualizerAttribute(ezBasisAxis::PositiveX, "Height", "Radius", ezColor::MediumAquamarine),
```

### `ezDirectionVisualizerAttribute`

Draws an arrow along a fixed or property-driven axis. `fScale` controls the arrow length, which can also be driven by a length property.

```cpp
new ezDirectionVisualizerAttribute(ezBasisAxis::PositiveX, 0.5f, ezColor::MediumAquamarine),
new ezDirectionVisualizerAttribute(ezBasisAxis::PositiveX, 1.0f, ezColor::White, "Color", "Length"),
```

### `ezConeVisualizerAttribute`

Draws a wireframe cone along a given axis. References an angle property and optionally a radius property and color property.

```cpp
new ezConeVisualizerAttribute(ezBasisAxis::PositiveX, "OuterAngle", 1.0f, "Range", ezColor::MediumAquamarine),
```

### `ezCameraVisualizerAttribute`

Draws a camera frustum wireframe driven by mode, FOV, ortho dimension, and near/far plane properties.

```cpp
new ezCameraVisualizerAttribute("Mode", "FOV", "OrthoDim", "NearPlane", "FarPlane"),
```

## See Also

* [Reflection System](reflection-system.md)
* [Components](world/components.md)
* [Custom Components with C++](../custom-code/cpp/custom-cpp-component.md)
