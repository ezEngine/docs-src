# World Modules

*World modules* are systems that are used to update certain aspects of a world. There can be only one instance of each world module for each [world](worlds.md).

A good example for a world module is the `ezPhysXWorldModule`. This module is responsible for updating the physics world every frame. To do so, it hooks into two *update phases* of the world, once early in the frame, where it kicks off the physics simulation in a parallel task, and once late in the frame, where it fetches the results of the simulation and applies them to the world.

Components represent individual pieces in the world. World modules represent large systems that provide the foundation for the components to work. World modules are frequently needed when integrating third party systems that require per frame updates to function.

## Creating and Instantiating World Modules

You create a new world module class by deriving from `ezWorldModule`.

You never instantiate world modules yourself. Instead, call `ezWorld::GetOrCreateModule()`. This will allocate the desired world module if necessary.

Consequently, if no code path ever calls `ezWorld::GetOrCreateModule()`, the respective world module will never be instantiated. Therefore, the lifetime and existence of a world module is often coupled to some component. Once a component is added to a world, its respective [component manager](component-managers.md) (which also is a world module) is automatically instantiated. If those components request access to another world module, that will be instantiated, as well.

Only few systems require a world module, without having some component type that would request its instantiation. For example, there is no need to instantiate a physics world module, if the scene doesn't contain any physics component.

If you do need a system that is always running, consider putting it into a [game state](../application/game-state.md). And if you determine it really does need to be a world module, a custom game state may be the right place to do the initial call to `ezWorld::GetOrCreateModule()` to instantiate the system.

The more common approach, though, is to have a custom component type, which ensures to set up a world module. You would then put a single component of this type into each world. This also allows you to have properties on the component, with which you can configure the world module.

### Example: Wind World Module

Code can query for the `ezWindWorldModuleInterface` using `ezWorld::GetWorldModule<ezWindWorldModuleInterface>()`. If a world module that implements this interface exists, the function will return a valid pointer. Things like [particle effects](../../effects/particle-effects/particle-effects-overview.md) can then ask the system for a wind value at their location, to apply wind to particles.

[Wind](../../effects/wind.md) can be implemented in different ways. From full 3D fluid simulations with turbulence, over simpler models, down to entirely basic models with just a randomly changing wind vector. What implementation you want may depend on your scene. Therefore, you choose the wind module by adding a corresponding component to the level. Out of the box you can have either no wind, or very simple wind. By adding an `ezSimpleWindComponent` to a scene, that component will make sure a wind module of type `ezSimpleWindWorldModule` is instantiated. Through the component's properties you can configure how the wind behaves.

If you want different wind behavior, you can add your own implementation of `ezWindWorldModuleInterface` through a [plugin](../../custom-code/cpp/engine-plugins.md). You would then add your own wind component, which instantiates and configures your custom wind module.

## Update Functions

The main feature of world modules is that they can hook into the world update and execute code at specific points. To do so, they need to register update functions using `ezWorldModule::RegisterUpdateFunction()`. This should be done during `ezWorldModule::Initialize()`.

To register an update function, you need to fill out an `UpdateFunctionDesc`. This takes a delegate to the actual function that should be called, and requires you to give a unique name to that function. This way, other world modules can refer to your update function by name. This is useful, when you have dependencies between world modules. Say you need to run one part of the physics update, then a specific animation update and finally another part of the physics update. You can do so, by registering three update functions and set up dependencies. The world will then execute the update functions in the required order.

### Update Phases

An important aspect of the update functions is in which *update phase* of the world they are executed. These are the steps in which the world is updated:

1. **Pre-async phase:** The corresponding update functions are called synchronously in the order of their dependencies.
1. **Async phase:** The update functions are called in batches, asynchronously on multiple threads.
   * There is no guarantee in which order they are called.
   * It is not allowed to access any data other than the components' own data during this phase.
1. **Post-async phase:** Another synchronous phase like the pre-async phase.
1. **Object deletion:** Dead objects and components are removed.
1. **Transform update:** The global transformation of all dynamic objects is updated.
1. **Post-transform phase:** Another synchronous phase like the pre-async phase, after the global transformation has been updated.

The choice in which phase to run an update function affects performance, how you can access other components, and how recent some data is that you read.

Many things must be updated in a single-threaded way. These would typically be done in the *pre-async* phase. Since everything runs single-threaded here, you can access other components, both to read and to modify them.

If you have something that operates solely on the data of a single component and would be safe to be executed for multiple components at the same time, you should put this into the *async* phase. Your update function will automatically be distributed across multiple threads to speed things up.

If you do have an async update, you may need to finalize or clean up some data afterwards, but in a single threaded way. Use the *post async* phase for that.

In all of these phases you can modify the owner game object's *local transform*, but when you read the *global transform* you will get the value from the previous frame. For most use cases this is sufficient, but in a few cases you must have the absolutely latest global transform, to prevent things from lagging a frame behind. For those cases you use the *post transform* phase. Here you can read the latest global transform value that will be used by the renderer. You can still modify the local transform here, but it won't have an effect until the next frame.

## See Also

* [Component Managers](component-managers.md)
* [The World / Scenegraph System](world-overview.md)
