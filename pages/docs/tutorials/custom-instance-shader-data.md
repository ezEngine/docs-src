# Tutorial: Custom Per-Instance Shader Data

When rendering objects ezEngine passes a `perInstanceData` buffer to shaders containing standard per-object information: transform, color, a `GameObjectID`, and a small `CustomData` vec4 (see [ObjectConstants.h](https://github.com/ezEngine/ezEngine/blob/dev/Data/Base/Shaders/Common/ObjectConstants.h)).

For cases where the 4-float `CustomData` channel is insufficient, the renderer supports an additional, fully custom structured buffer that can be attached to any mesh component. This tutorial walks you through the required steps to add such a buffer.

## How It Works

A component manager registers a typed GPU buffer once per world via `ezRenderDataManager`. Each component that needs the data allocates a slot in that buffer, writes its data (potentially every frame), and passes the buffer handle + slot offset to the mesh component it wants to apply it to. The renderer then binds the buffer to the `perInstanceDataCustom` shader resource slot and stores the slot index in `DataOffsets.y`, where shaders can read it.

Two in-engine examples that use this system:

- **`ezProcVertexColorComponent`** ([ProcVertexColorComponent.h](https://github.com/ezEngine/ezEngine/blob/dev/Code/EnginePlugins/ProcGenPlugin/Components/ProcVertexColorComponent.h)) — stores per-vertex color data for procedurally-painted meshes.
- **`ezMeshComponentBase::SetCustomInstanceData()`** ([MeshComponentBase.h](https://github.com/ezEngine/ezEngine/blob/dev/Code/Engine/RendererCore/Meshes/MeshComponentBase.h#L128)) — the API through which any component attaches a custom buffer to a mesh.

## Step 1: Define the Data Struct

Create a header that is usable from both C++ and HLSL using the `EZ_SHADER_STRUCT` / shader macro system:

```cpp
// MyInstanceData.h  (include from both C++ and .ezShader files)
#include <Shaders/Common/Platforms.h>
#include <Shaders/Common/ConstantBufferMacros.h>

struct EZ_SHADER_STRUCT MyCustomInstanceData
{
    TRANSFORM(WorldToObject);   // expands to ezShaderTransform (C++) / Transform (HLSL)
    FLOAT4(CustomParams);       // expands to ezVec4 (C++) / float4 (HLSL)
};
```

All available field macros are defined in [ConstantBufferMacros.h](https://github.com/ezEngine/ezEngine/blob/dev/Data/Base/Shaders/Common/ConstantBufferMacros.h).

## Step 2: Register the Buffer in the Component Manager

You need a custom component manager (not `ezComponentManagerSimple`) so you can override `Initialize()` and `Deinitialize()`. Call `RegisterCustomInstanceData()` once and store the returned index — it is your handle to this buffer for the lifetime of the world.

```cpp
// MyComponent.h
class MyComponentManager : public ezComponentManager<MyComponent, ezBlockStorageType::FreeList>
{
public:
    MyComponentManager(ezWorld* pWorld);
    virtual void Initialize() override;
    virtual void Deinitialize() override;

    ezUInt32 m_uiCustomDataIndex = ezInvalidIndex;
};
```

```cpp
// MyComponent.cpp
#include <RendererCore/Pipeline/RenderDataManager.h>
#include <RendererFoundation/Device/Device.h>

void MyComponentManager::Initialize()
{
    SUPER::Initialize();

    ezGALBufferCreationDescription desc;
    desc.m_uiStructSize = sizeof(MyCustomInstanceData);
    desc.m_uiTotalSize  = 256 * desc.m_uiStructSize;  // initial capacity; the buffer grows as needed
    desc.m_ResourceAccess.m_bImmutable = false;
    desc.m_BufferFlags = ezGALBufferUsageFlags::StructuredBuffer | ezGALBufferUsageFlags::ShaderResource;

    ezRenderDataManager* pRdm = GetWorld()->GetOrCreateModule<ezRenderDataManager>();
    m_uiCustomDataIndex = pRdm->RegisterCustomInstanceData(desc, "MyCustomInstanceData");
}

void MyComponentManager::Deinitialize()
{
    SUPER::Deinitialize();
}
```

> **Tip:** `RegisterCustomInstanceData()` accepts an optional `beforeUploadCallback` delegate. Use it if your data is produced asynchronously (e.g. by a task), so you can wait for the task to finish before the GPU upload happens. See `ezProcVertexColorComponentManager::Initialize()` in [ProcVertexColorComponent.cpp](https://github.com/ezEngine/ezEngine/blob/dev/Code/EnginePlugins/ProcGenPlugin/Components/Implementation/ProcVertexColorComponent.cpp) for an example.

## Step 3: Store a Slot Offset per Component Instance

Each component (or each mesh it controls) needs one `ezCustomInstanceDataOffset` to track its position within the shared buffer. It starts invalidated (`m_uiOffset == ezInvalidIndex`) and gets a real value on first write.

```cpp
// MyComponent.h  (inside the component class)
private:
    ezCustomInstanceDataOffset m_CustomDataOffset;
    ezComponentHandle m_hMeshComponent;   // the mesh this data applies to
```

## Step 4: Write Data Each Frame

Call `GetOrCreateCustomInstanceDataAndFill()` to allocate or update the slot, then hand the buffer handle and offset to the mesh component. Do this wherever you update your component's state — an `Update()` function or `OnMsgExtractRenderData` are both valid choices.

```cpp
#include <RendererCore/Meshes/MeshComponentBase.h>

void MyComponent::UpdateShaderData()
{
    auto* pManager = static_cast<MyComponentManager*>(GetOwningManager());
    ezRenderDataManager* pRdm = GetWorld()->GetOrCreateModule<ezRenderDataManager>();

    MyCustomInstanceData data;
    data.m_WorldToObject = GetOwner()->GetGlobalTransform().GetInverse();
    data.m_CustomParams  = ezVec4(1, 0, 0, 1);

    ezMeshComponentBase* pMesh = nullptr;
    if (!GetWorld()->TryGetComponent(m_hMeshComponent, pMesh))
        return;

    const ezGALDynamicBufferHandle hBuffer = pRdm->GetOrCreateCustomInstanceDataAndFill(
        pManager->m_uiCustomDataIndex, *pMesh, m_CustomDataOffset, data);

    pMesh->SetCustomInstanceData(m_CustomDataOffset, hBuffer);
}
```

`GetOrCreateCustomInstanceDataAndFill()` is declared in [RenderDataManager.h](https://github.com/ezEngine/ezEngine/blob/dev/Code/Engine/RendererCore/Pipeline/RenderDataManager.h#L74). If you need to write an array of structs (e.g. one entry per vertex), use `GetOrCreateCustomInstanceData()` instead, which returns an `ezArrayPtr<T>` you can fill manually.

## Step 5: Release the Slot on Deactivation

When a component is deactivated, release its slot so the memory can be reused:

```cpp
void MyComponent::OnDeactivated()
{
    auto* pManager = static_cast<MyComponentManager*>(GetOwningManager());
    ezRenderDataManager* pRdm = GetWorld()->GetModule<ezRenderDataManager>();
    if (pRdm)
        pRdm->DeleteCustomInstanceData(pManager->m_uiCustomDataIndex, m_CustomDataOffset);

    SUPER::OnDeactivated();
}
```

### Optional: Handle Buffer Compaction

Over time, if slots of varying sizes are allocated and freed, the buffer may become fragmented. Call `CompactCustomInstanceDataBuffer()` periodically (e.g. once per second) to defragment it. When the buffer is compacted, offsets change — any component that is *not* the owner of its mesh component must listen for `ezMsgCustomInstanceDataOffsetChanged` and update the mesh:

```cpp
// In component reflection block:
EZ_MESSAGE_HANDLER(ezMsgCustomInstanceDataOffsetChanged, OnCustomInstanceDataOffsetChanged)

// Handler implementation:
void MyComponent::OnCustomInstanceDataOffsetChanged(ezMsgCustomInstanceDataOffsetChanged& msg)
{
    m_CustomDataOffset = msg.m_NewOffset;

    ezMeshComponentBase* pMesh = nullptr;
    if (GetWorld()->TryGetComponent(m_hMeshComponent, pMesh))
        pMesh->SetCustomInstanceData(m_CustomDataOffset, pMesh->GetCustomInstanceDataBuffer());
}
```

`ezMsgCustomInstanceDataOffsetChanged` is declared in [RenderData.h](https://github.com/ezEngine/ezEngine/blob/dev/Code/Engine/RendererCore/Pipeline/RenderData.h#L228).

## Step 6: Declare the Buffer in Your Shader

In your `.ezShader` file, include your data struct header and declare the `perInstanceDataCustom` resource. The name and bind group are fixed — the renderer always binds the custom buffer to this slot.

```hlsl
#include "MyInstanceData.h"

StructuredBuffer<MyCustomInstanceData> perInstanceDataCustom BIND_GROUP(BG_DRAW_CALL);
```

Access the data using `DataOffsets.y` as the index. The `DataOffsets` semantic is available in the vertex shader input after calling `FillVertexData()`:

```hlsl
// In your vertex shader:
MyCustomInstanceData customData = perInstanceDataCustom[G.Input.DataOffsets.y];
float4x4 worldToObject = TransformToMatrix(customData.WorldToObject);
```

The four offset channels in `DataOffsets` are:

| Component | Contains |
| --- | --- |
| `.x` | Standard instance data index (`perInstanceData`) |
| `.y` | Custom instance data index (`perInstanceDataCustom`) |
| `.z` | Material data index |
| `.w` | Skinning data index |

The standard `perInstanceData` buffer (transform, color, `CustomData` vec4) is still accessible alongside the custom buffer via `GetInstanceData()` or `perInstanceData[G.Input.DataOffsets.x]`. See [ObjectConstants.h](https://github.com/ezEngine/ezEngine/blob/dev/Data/Base/Shaders/Common/ObjectConstants.h) for its layout.

## See Also

- [Custom C++ Components](../custom-code/cpp/custom-cpp-component.md)
- [Shader Render State](../graphics/shaders/shader-render-state.md)
- [Meshes](../graphics/meshes/meshes-overview.md)
