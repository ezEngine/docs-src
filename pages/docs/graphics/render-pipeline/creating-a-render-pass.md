# Creating a Render Pass

This page describes how to create a custom render pipeline pass by deriving from `ezRenderPipelinePass`. For background on how the render graph works, see the [Render Graph](../render-graph/render-graph.md) documentation.

## Overview

A render pipeline pass is a node in the [render pipeline](render-pipeline-overview.md) graph. Each pass has input and output **pins** that carry textures between nodes. When the pipeline runs, it calls `AddRenderPasses()` on each pass, which records one or more render graph passes that do the actual GPU work.

Creating a custom pass requires:

1. A **header** declaring the class, its pins, and any configurable properties.
2. An **implementation** with reflection metadata and the `AddRenderPasses()` override.
3. Optionally, `Serialize`/`Deserialize` overrides for persistence and `AddRenderPassesInactive` for inactive state handling.

## Pin Types

Pins define the inputs and outputs visible in the render pipeline editor. Declare them as `protected` members:

* `ezRenderPipelineNodeInputPin` — receives a texture from an upstream node.
* `ezRenderPipelineNodeOutputPin` — produces a new texture for downstream nodes.
* `ezRenderPipelineNodePassThroughPin` — receives a texture and passes it through. The pass renders into the texture without creating a new one. Has both an input and output index.

## Minimal Example: Copy Texture Pass

The simplest pass reads one texture and copies it to a new output. This example shows the complete structure.

### Header

Derive from `ezRenderPipelinePass` and add `EZ_ADD_DYNAMIC_REFLECTION`. Pass a default name and whether the pass supports stereoscopic rendering to the base constructor. Declare pins as `protected` members.

<!-- BEGIN-DOCS-CODE-SNIPPET: renderpass-header -->
```cpp
class EZ_RENDERERCORE_DLL ezCopyTexturePass : public ezRenderPipelinePass
{
  EZ_ADD_DYNAMIC_REFLECTION(ezCopyTexturePass, ezRenderPipelinePass);

public:
  ezCopyTexturePass();
  ~ezCopyTexturePass();

  virtual ezStatus AddRenderPasses(const ezViewData& viewData, const ezCamera& camera, ezRenderGraph& graph, const ezArrayPtr<const ezRenderPipelinePinConnection> inputs, ezArrayPtr<ezRenderPipelinePinConnection> outputs) override;

protected:
  ezRenderPipelineNodeInputPin m_PinInput;
  ezRenderPipelineNodeOutputPin m_PinOutput;
};
```
<!-- END-DOCS-CODE-SNIPPET -->

### Reflection

In the reflection block, register all pins as `EZ_MEMBER_PROPERTY` so they appear in the editor. Any configurable parameters should also be registered here. The `ezCategoryAttribute` determines which group the pass appears in within the render pipeline editor.

<!-- BEGIN-DOCS-CODE-SNIPPET: renderpass-reflection -->
```cpp
EZ_BEGIN_DYNAMIC_REFLECTED_TYPE(ezCopyTexturePass, 1, ezRTTIDefaultAllocator<ezCopyTexturePass>)
{
  EZ_BEGIN_PROPERTIES
  {
    EZ_MEMBER_PROPERTY("Input", m_PinInput),
    EZ_MEMBER_PROPERTY("Output", m_PinOutput)
  }
  EZ_END_PROPERTIES;
  EZ_BEGIN_ATTRIBUTES
  {
    new ezCategoryAttribute("Utilities")
  }
  EZ_END_ATTRIBUTES;
}
EZ_END_DYNAMIC_REFLECTED_TYPE;
```
<!-- END-DOCS-CODE-SNIPPET -->

### Render Passes

The function `AddRenderPasses` does all the actual rendering work. Here, you can declare render passes on the passed in [render graph](../render-graph/render-graph.md).

**Read inputs:** Access input textures via pin indices and validate they are connected. Return an error status if a required input is missing. Failing this function causes the rendering of the pipeline to be canceled.

**Create outputs or pass through:** For `ezRenderPipelineNodeOutputPin`, create a new transient texture with `graph.CreateTexture()`. For `ezRenderPipelineNodePassThroughPin`, forward the input handle directly as the output.

**Add render graph passes:** Create one or more render graph passes and declare their resource access. For graphics passes, also declare color and depth targets.

**Set the execution callback:** The actual rendering code needs to be placed in the execution callback. Use `ctx.ResolveTexture()` to convert graph handles to real GPU handles inside the callback.

If your pass can be toggled off in the editor but downstream passes depend on its output, override `AddRenderPassesInactive()`. This has the same interface as `AddRenderPasses` and must still create a valid output texture, typically cleared to a neutral value.



<!-- BEGIN-DOCS-CODE-SNIPPET: renderpass-add-render-passes -->
```cpp
ezStatus ezCopyTexturePass::AddRenderPasses(const ezViewData& viewData, const ezCamera& camera, ezRenderGraph& graph, const ezArrayPtr<const ezRenderPipelinePinConnection> inputs, ezArrayPtr<ezRenderPipelinePinConnection> outputs)
{
  ezRenderGraphTextureHandle hInput = inputs[m_PinInput.m_uiInputIndex].m_TextureHandle;
  if (hInput.IsInvalidated())
    return ezStatus(ezFmt("Input: Not connected"));

  const ezGALTextureCreationDescription inputDesc = graph.GetTextureDesc(hInput);
  ezRenderGraphTextureHandle hOutput = graph.CreateTexture(inputDesc);
  outputs[m_PinOutput.m_uiOutputIndex].m_TextureHandle = hOutput;

  auto pass = graph.AddTransferPass("CopyTexture");
  pass.ReadTexture(hInput, {}, ezGALResourceState::CopySource);
  pass.WriteTexture(hOutput, {}, ezGALResourceState::CopyDestination);
  pass.SetExecuteCallback([=](const ezRenderGraphContext& ctx)
  {
    ctx.GetCommandEncoder()->CopyTexture(ctx.ResolveTexture(hOutput), ctx.ResolveTexture(hInput));
  });

  return EZ_SUCCESS;
}
```
<!-- END-DOCS-CODE-SNIPPET -->

### Rendering Objects

More complex passes may need to access the `ezRenderViewContext` which can be accessed via `ctx.GetUserData<ezRenderViewContext>()` inside the execution callback. For graphics passes, you need to call `renderViewContext.UpdateViewport();` to apply the viewport to the global constant buffer and set the viewport up for rendering.

If your pass needs to render materials and have access to the data provided by data providers, you need to declare the dependencies by calling `ezRenderPipelinePass::SetupResourceDependencies` on the pass and inside the execution callback you need to run `ezRenderPipelinePass::BindDataProviderResources` to bind the resources to the bind groups.

If your pass renders scene geometry, use `RenderDataWithCategory()` inside the callback to draw objects from extractors.

<!-- BEGIN-DOCS-CODE-SNIPPET: renderpass-render-objects -->
```cpp
    ezRenderPipelinePass::SetupResourceDependencies(viewData, graph, pass, m_ShadingQuality);
    pass.SetExecuteCallback([=](const ezRenderGraphContext& ctx)
      {
        const ezRenderViewContext& renderViewContext = *ctx.GetUserData<ezRenderViewContext>();
        ezRenderPipelinePass::BindDataProviderResources(renderViewContext, m_ShadingQuality);
        ezBindGroupBuilder& bindGroupRenderPass = renderViewContext.m_pRenderContext->GetBindGroup(EZ_GAL_BIND_GROUP_RENDER_PASS);
        if (!hResolvedDepth.IsInvalidated())
        {
          bindGroupRenderPass.BindTexture("SceneDepth", ctx.ResolveTexture(hResolvedDepth));
        }
        RenderDataWithCategory(renderViewContext, ezDefaultRenderDataCategories::LitMeshDecal); //
      });
```
<!-- END-DOCS-CODE-SNIPPET -->

### Serialization

If your pass has configurable properties, override `Serialize` and `Deserialize` for persistence. Always call the base class first:

<!-- BEGIN-DOCS-CODE-SNIPPET: renderpass-serialization -->
```cpp
ezResult ezDepthOnlyPass::Serialize(ezStreamWriter& inout_stream) const
{
  EZ_SUCCEED_OR_RETURN(SUPER::Serialize(inout_stream));
  inout_stream << m_bRenderStaticObjects;
  inout_stream << m_bRenderDynamicObjects;
  inout_stream << m_bRenderTransparentObjects;
  return EZ_SUCCESS;
}

ezResult ezDepthOnlyPass::Deserialize(ezStreamReader& inout_stream)
{
  EZ_SUCCEED_OR_RETURN(SUPER::Deserialize(inout_stream));
  const ezUInt32 uiVersion = ezTypeVersionReadContext::GetContext()->GetTypeVersion(GetStaticRTTI());

  if (uiVersion >= 3)
  {
    inout_stream >> m_bRenderStaticObjects;
    inout_stream >> m_bRenderDynamicObjects;
  }

  if (uiVersion >= 2)
  {
    inout_stream >> m_bRenderTransparentObjects;
  }

  return EZ_SUCCESS;
}
```
<!-- END-DOCS-CODE-SNIPPET -->

## See Also

* [Render Graph](../render-graph/render-graph.md)
* [Render Pipeline](render-pipeline-overview.md)
* [Render Pipeline Passes](render-pipeline-passes.md)
