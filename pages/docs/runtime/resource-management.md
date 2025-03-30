# Resource Management

In the majoriy of cases, resources are binary representations of [assets](../assets/assets-overview.md) that are stored on disk. Resources can also be dynamically created at runtime based on a *resource descriptor*. All resources derive from the [ezResource](https://ezengine.github.io/api-docs/d3/d0a/classez_resource.htm) base class. You cannot create or access these directly. Instead, they are managed by the [ezResourceManager](https://ezengine.github.io/api-docs/dc/d99/classez_resource_manager.htm), which is a global singleton. In the chapters below, the following concepts will be used:

* **Resource ID**: This is a globally unique identifier, in the form of a case-sensitive string. It can be an asset GUID or a relative path into a data directory or a completely arbitrary string in case of runtime-generated resources. The resource ID must be provided when loading or creating a resource.  
* **Resource Handle**: User code should never store a pointer to a resource. Instead, a handle to a resource should be stored which is like a shared pointer (e.g. it increases the reference count of the resource). Handles come in two flavors: `ezTypelessResourceHandle` and `ezTypedResourceHandle`. The typeless variant allows you to store a handle to any resource of any type while the typed version only allows you to store a reference to one specific resource type. Typically there is a typed resource handle declaration for each resource type, see for example `ezParticleEffectResourceHandle` for particle resources. Note that storing a resource handle marks it as *in use* which prevents unloading of the resource. It is important to keep handles to resourcees around, that will be used soon, but if a handle isn't cleaned up properly, it will keep data loaded unnecessarily. So be careful where you store resource handles.
* **Resource Descriptor**: When creating a resource, you can't just call the constructor. Instead, you need to fill out a *resource descriptor* that defines the resource and tells the *resource manager* to create the resource for you via e.g. `ezResourceManager::CreateResource`.
* **Resource Pointer**: At some point you will want to access the content of a resource. As resource management is heavily multi-threaded, these accesses must happen by acquiring a lock to the resource. This is usually done via the `ezResourceLock`, which is explained later. The pointer must only be accessed under the lock and not stored after the lock is released.
* **Resource State**: A resource is always in one of the following states:
  * **Invalid**: The resource no longer exists.
  * **Unloaded**: The resource is not loaded yet. Each resource that gets loaded by the resource manager starts in this state.
  * **LoadedResourceMissing**: The resource failed to load. Most likely it is missing on disk.
  * **Loaded**: The resource is loaded at some level of quality and can be used.
* **Fallback Resource**: If a resource isn't loaded yet, a fallback resource can be returned by the *resource manager*. For this to work, either the resource type or the individual resource must provide a fallback resource and the user must acquire the resource with `ezResourceAcquireMode::AllowLoadingFallback`.
* **Quality Levels**: Some resources can exist at multiple quality levels. E.g. textures can have some of their mip levels missing. The texture is considered loaded as long as a single mip level was loaded so that the texture can be used. 

## Loading Resources

To load a resource, you will usually provide the [asset guid](../assets/assets-overview.md#asset-guid) or a relative path to a file. Note that this does not load the resource immediately. The resource manager is lazy and will only load resources that are actively being [acquired](#acquiring-resources). Similiarly, the resource manager might actually unload resources again to save memory if they haven't been acquiring in a while and no handles remain to them.
```cpp
ezShaderResourceHandle hShader = ezResourceManager::LoadResource<ezShaderResource>("ResourceID");
```

## Creating Runtime Resources

To create a resource at runtime, you need to fill out the resource type specific resource descriptor. Below is an example of an `ezMeshBufferResource` created from an `ezGeometry` instance:
```cpp
ezGeometry& inout_geom;
...
ezGALPrimitiveTopology::Enum topology;
ezMeshBufferResourceDescriptor desc;
  desc.AddStream(ezGALVertexAttributeSemantic::Position, ezGALResourceFormat::XYZFloat);
  desc.AddStream(ezGALVertexAttributeSemantic::Color0, ezGALResourceFormat::RGBAUByteNormalized);
  desc.AddStream(ezGALVertexAttributeSemantic::Normal, ezGALResourceFormat::XYZFloat);
  desc.AllocateStreamsFromGeometry(inout_geom, topology);
  desc.ComputeBounds();
ezResourceManager::CreateResource<ezMeshBufferResource>("MyUniqueResourceID", std::move(desc), szDescription);
```
Use `GetOrCreateResource` instead if you expect your resource to be created by multiple threads at the same time. E.g. your code runs inside a task or other multi-threaded environment. Unlike resources that are loaded via `ezResourceManager::LoadResource`, creating resources will block until the resource is fully created (i.e. in *Loaded* state) before returning to the caller. Therefore, complex resources should ideally be created inside tasks and not inside the runtime loop.

## Acquiring Resources

To access a resource, it needs to be acquired first. This is done by creating a scoped `ezResourceLock` on the handle. There are multiple modes in which a resource can be acquired defined by `ezResourceAcquireMode`:
* **PointerOnly**: This will only acquire the pointer to the resource. It will not trigger the resource manager to actually load this resource from disk. Use this if you merely want to e.g. register to [resource changes](#listening-for-resource-changes).
* **BlockTillLoaded**: As the name suggests, this blocks the current thread until the resource has switched to the *Loaded* state. This does NOT mean that all quality levels are loaded.
* **AllowLoadingFallback**: If the resource is loaded, it is immediately returned. If not, a fallback resouce is returned instead. If no fallback exists, this will assert. Prefer this version as is does not block.

For additional modes and further information, please refer to the `ezResourceAcquireMode` declaration.
The resource manager keeps track if and when resources are attempted to be acquired to decide which resources to load from disk. Thus, it is important that you try to acquire a resource you want to load via one of the `AllowLoadingFallback` variants at least once or the resource will never switch into a *loaded* state. 


```cpp
ezShaderResourceHandle hShader = ezResourceManager::LoadResource<ezShaderResource>("ResourceID");
{
  ezResourceLock<ezShaderResource> pShader(hShader, ezResourceAcquireMode::PointerOnly);
  ezResourceAcquireResult result = pShader.GetAcquireResult();
  if (result == ezResourceAcquireResult::LoadingFallback)
  {
    // A fallback was returned as the resource was not loaded yet.
    // In many cases the fallback resource can be used directly as a replacement for the actual resource.
    // Should the final result really be required, it is best to skip the operation until a later frame.
  }
  else if (result == ezResourceAcquireResult::Final)
  {
    // The resource is loaded and can now be accesed under the lock.
    pShader->...
  }
}
```

## Listening for Resource Changes

You can either listen to a single resource's state changes or you can listen to the same for all resource via the resource manager. Note that if you add an event handler to a single resource's event, you need to also hold a handle to that resource as you can't unsubscribe inside the event handler callback when the resource gets destroyed.

```cpp
// All resources
ezResourceManager::GetResourceEvents().AddEventHandler(ezMakeDelegate(...));

// Single resource
ezResourceLock<ezShaderResource> pShader(hShader, ezResourceAcquireMode::PointerOnly);
pShader->m_ResourceEvents.AddEventHandler(ezMakeDelegate(...));
```

## Unloading of Resources

There are two ways a resource can be unloaded: due to lack of handles pointing to the resource and due to forced resource unloading (tooling only).
The resource manager will enumerate resources with no handles on them and will start unloading them after a certain time of inactivity.

Forced resource unloading can be triggered via `ezResourceManager::ReloadAllResources`, `ezResourceManager::ReloadResource` and related functions on the resource manager. Calling these functions will immediately lock and unload the resource, switching it into the *Unloaded* state. The next resource acquisition will trigger loading the resource again. This means that resource unload and reload can potentially happen at any time during the frame. Some resources will have custom logic to e.g. double buffer its state to make sure resource switching happens at fixed times in the frame.

## See Also

* [Asset Overview](../assets/assets-overview.md)
