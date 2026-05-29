# Render Graph

The render graph is the underlying system that manages GPU resource allocation, synchronization and execution. Instead of manually creating render targets, inserting resource barriers and managing resource lifetimes, passes declare which resources they read and write and the render graph takes care of the rest during execution.

The render graph provides:

* **Automatic resource barriers** between passes based on declared resource access states.
* **Automatic ezGALRenderingSetup creation** based on the user pass description.
* **Transient resource pooling and aliasing** so that GPU memory is reused across passes with non-overlapping lifetimes.
* **Dead pass culling** to skip passes whose outputs are never consumed.

## Lifecycle

After creating a render graph once via `ezRenderGraphManager::CreateRenderGraph`, you can start recording passes into it. Each graph has:

* A **graph name** (immutable, set at creation) and an optional **user name** (mutable, per-frame label).
* A **phase** (immutable, set at creation) that controls execution order relative to other graphs: `PreRender`, `Render` (default), or `PostRender`. Within a phase, graphs run in FIFO order of their `ezRenderGraphManager::EnqueueRenderGraph` calls.
* A **user data** pointer (`void*`) that is forwarded to all execution callbacks.

A typical frame follows these steps:

1. Each Frame if you need to re-record the graph, follow this pattern:
  1. Reset the graph via `Reset()`.
  1. **Import** external resources (e.g. the swapchain image) with `ImportTexture()`. On subsequent frames, you can use `ReplaceImportedTexture()` to swap in the new swapchain image without rebuilding the graph again.
  1. **Create** transient resources with `CreateTexture()` / `CreateBuffer()`.
  1. **Add passes**, declare resource access and set execution callbacks.
1. **Enqueue** the graph with `ezRenderGraphManager::EnqueueRenderGraph()`. After this call, no new passes can be added to the graph anymore.
1. The **ezRenderGraphManager** compiles all enqueued graphs (building dependencies, culling dead passes, allocating transient resources), computes barriers across all graphs using a shared state tracker, and executes them.

## Creating resources

There are two kinds of resources in a render graph:

* **Transient resources** are created with `CreateTexture()` or `CreateBuffer()`. The render graph allocates them from a pool and automatically releases them when no longer needed. Two transient resources with non-overlapping lifetimes may share the same GPU memory.
* **Imported resources** are existing GPU resources brought into the graph with `ImportTexture()` or `ImportBuffer()`. The graph tracks their state but does not manage their lifetime. You can also use `ReplaceImportedTexture()` to swap in a compatible GAL handle (e.g. a new swapchain image) after recording without rebuilding the graph. When importing, you can optionally also provide a `ezGALResourceState` into which the resource should be barriered at the start of the graph execution. If you leave it to the default of `ezGALResourceState::Unknown`, no barriers will be added at the start of the graph.
 
Resources inside the render graph are referenced by `ezRenderGraphTextureHandle` and `ezRenderGraphBufferHandle` returned by the above functions. These are opaque, lightweight handles that are only valid inside the graph they were created on until the graph is reset.

> **Note:**
>
> There is no need to set any flags on the resources created via `CreateTexture()` or `CreateBuffer()`. Whenever a pass operates on a resources its flags are extended to support that operation.

For the code snippets from here on we will use the example of a transient MSAA texture that is to be resolved into an imported non-MSAA texture: 

<!-- BEGIN-DOCS-CODE-SNIPPET: rendergraph-msaa-create-resources -->
```cpp
  // Create transient MSAA texture
  ezGALTextureCreationDescription descMsaa;
  descMsaa.SetAsRenderTarget(64, 64, ezGALResourceFormat::RGBAHalf, ezGALMSAASampleCount::FourSamples);
  ezRenderGraphTextureHandle hMsaaColor = graph.CreateTexture(descMsaa);

  // Import persistent non-MSAA resolve target
  ezGALTextureCreationDescription descResolved;
  descResolved.SetAsRenderTarget(64, 64, ezGALResourceFormat::RGBAHalf);
  ezGALTextureHandle hResolvedGAL = m_pDevice->CreateTexture(descResolved);
  ezRenderGraphTextureHandle hResolved = graph.ImportTexture(hResolvedGAL);
```
<!-- END-DOCS-CODE-SNIPPET -->

## Creating Passes

A pass represents a unit of GPU work. Besides its parameters the user also sets a **callback** that is called when the pass is executed. There are three types of passes:

* **Graphics pass** (`AddGraphicsPass`) - rasterization work. Based on the description, the backend will create the `ezGALRenderingSetup` and call `BeginRendering` / `EndRendering`.
* **Compute pass** (`AddComputePass`) - compute shader dispatches. Backend calls `BeginCompute`/`EndCompute`.
* **Transfer pass** (`AddTransferPass`) - used for copy and resolve operations.

Passes execute in the order they were recorded into the graph. The above functions return a `ezRenderGraphPassBuilder`. This class is used to define the pass.

> **Important:**
>
> Only one instance on `ezRenderGraphPassBuilder` can be alive per scope / graph, so multiple `Add*Pass` calls must be in separate scopes.

## Resource States

The most crucial part of the recording is to set correct states for the resources each pass accesses. For this, you need to call `ReadTexture`, `WriteTexture`, `ReadBuffer` or `WriteBuffer`. As we want to resolve a texture, we need to set the states accordingly.

In general, if your shader uses an SRV `ezGALShaderResourceType`, you need to call `Read*` with `ezGALResourceState::ShaderResource`. If your shader uses an UAV `ezGALShaderResourceType`, you need to call `Write*` with `ezGALResourceState::UnorderedAccess`. For buffers, the `ezGALBufferUsageFlags` match the names of the corresponding states you need to use from `ezGALResourceState`. These states will be used by the graph to place proper barriers during execution.

You can also optionally set a shader stage via `ezGALShaderStageFlags`. Only use these for graphics passes when you know exactly in which stage a resource is accessed.

> **Note:**
>
> For depth textures, the correct SRV state is `ezGALResourceState::DepthStencilRead` instead of `ezGALResourceState::ShaderResource`, but the render graph automatically switches this for your convenience.

<!-- BEGIN-DOCS-CODE-SNIPPET: rendergraph-msaa-barriers -->
```cpp
    auto pass = graph.AddTransferPass("MsaaColorResolve");
    pass.ReadTexture(hMsaaColor, {}, ezGALResourceState::ResolveSource);
    pass.WriteTexture(hResolved, {}, ezGALResourceState::ResolveDestination);
```
<!-- END-DOCS-CODE-SNIPPET -->

## Execute Callback

You can set an execute callback that is run when the graph is executed later in the frame once all graphs have been enqueued. Not setting a callback can make sense for graphics passes that only need to clear something or if you just want to set some barriers. Inside the callback, you have access to the `ezRenderGraphContext`:

* `ResolveTexture(handle)` / `ResolveBuffer(handle)` - resolve graph handles to real GPU handles so they can be used in the command encoder.
* `GetCommandEncoder()` - the underlying command encoder.
* `GetRenderContext()` - the high-level render context (shader binding, draw calls).
* `GetDevice()` - the GAL device.
* `GetUserData<T>()` - access to the user data pointer set on the graph.

> **Important:**
>
> As the execute callback is called at a later date, make sure to capture variables by value if using a lambda.

<!-- BEGIN-DOCS-CODE-SNIPPET: rendergraph-msaa-execute-callback -->
```cpp
    pass.SetExecuteCallback([=](const ezRenderGraphContext& ctx)
    {
      ezGALTextureSubresource subresource;
      subresource.m_uiMipLevel = 0;
      subresource.m_uiArraySlice = 0;
      ctx.GetCommandEncoder()->ResolveTexture(ctx.ResolveTexture(hResolved), subresource, ctx.ResolveTexture(hMsaaColor), subresource);
    });
```
<!-- END-DOCS-CODE-SNIPPET -->


## Graphics Pass

In addition to the previous steps, in a graphics pass, you also need to declare the same color and depth targets you would have previously set on a `ezGALRenderingSetup` and the interface is roughly the same. Calling any of the clear functions will switch the corresponding `ezGALRenderTargetLoadOp` to `Clear`.

Setting render targets implicitly defines barriers via `WriteTexture` so there is no need to call these functions yourself. If your shader supports stereoscopic rendering, you need to call `SetStereoscopic` as well.

<!-- BEGIN-DOCS-CODE-SNIPPET: rendergraph-graphics-pass -->
```cpp
    auto pass = graph.AddGraphicsPass("RenderMSAA");
    pass.AddColorTarget(hMsaaColor, {}, ezGALRenderTargetLoadOp::Clear, ezGALRenderTargetStoreOp::Store);
    pass.SetClearColor(0, ezColor::CornflowerBlue);
    pass.AddDepthStencilTarget(hMsaaDepth, {}, ezGALRenderTargetLoadOp::Clear, ezGALRenderTargetStoreOp::Store, ezGALRenderTargetLoadOp::Clear, ezGALRenderTargetStoreOp::Store);
    pass.SetClearDepth(1.0f);
    pass.SetClearStencil(0);
    pass.SetStereoscopic(false);
    pass.HasSideEffects();
```
<!-- END-DOCS-CODE-SNIPPET -->

## Pass Culling

The render graph automatically removes passes whose outputs are never consumed. A pass is kept alive if:

* It was marked with `HasSideEffects()` during pass recording.
* It writes to an imported resource.
* Any of its outputs are read by another alive pass.

All transitive dependencies of alive passes are also kept alive. This means that if you toggle a feature off, the passes that fed into it are automatically skipped without any manual intervention.

## Compilation and Execution

Once recorded and enqueued, the `ezRenderGraphManager` drives the full pipeline during `ExecuteRenderGraphs`. Compilation consists of the following steps:

1. **ValidateGraph** - checks for dead or invalid GAL handles.
3. **CullDeadPasses** - removes passes whose outputs are never consumed (unless they have side effects or write to imported resources).
4. **BuildSortedPassList** - creates a linear list of remaining passes in declaration order.
5. **ComputeResourceLifetimes** - determines the first and last pass each transient resource is used in.
6. **AllocateTransientResources** - acquires concrete GPU resources from the pool via the `ezRenderGraphResourceAllocator`, sharing GAL handles between graph handles with non-overlapping lifetimes.
7. **BuildRenderingSetups** - creates the `ezGALRenderingSetup` for each graphics pass from its declared color and depth targets.

After compilation, the `ezRenderGraphManager` uses the `ezGALResourceStateTracker` to compute barriers for the entire frame by calling `ComputeBarriers` on each graph in execution order. Finally, all graphs are executed and all modified resources are barriered back into their default state.

## Integration with Render Pipeline

Within the [render pipeline](../render-pipeline/render-pipeline-overview.md), each `ezRenderPipelinePass` implements `AddRenderPasses()` to add one or more render graph passes. The pipeline calls this method during graph construction, passing the pin connections that link passes together.

For details on how to create a custom render pass using the render graph system, see [Creating a Render Pass](../render-pipeline/creating-a-render-pass.md).

## See Also

* [Render Pipeline](../render-pipeline/render-pipeline-overview.md)
* [Render Pipeline Passes](../render-pipeline/render-pipeline-passes.md)
* [Creating a Render Pass](graphics/render-pipeline/creating-a-render-pass.md)
