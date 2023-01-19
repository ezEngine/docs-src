# Wind

Some components can be animated by wind. For instance [particle effects](../particle-effects/particle-effects-overview.md), [ropes](../ropes/fake-rope-component.md) and [Kraut trees](../../terrain/kraut-overview.md) will react to wind. Usually these animations are for decorative purposes.

<video src="../media/wind-cone.webm" width="600" height="600" autoplay loop></video>

Wind is implemented as a [world module](../../runtime/world/world-modules.md). Thus, it is possible to have different wind system implementations, and choose the most suitable for each scene. For example, one system may do a full volumetric fluid simulation, whereas another does not.

You instantiate a specific wind system by adding the respective component to a scene. At this time, EZ only ships with a basic implementation. You instantiate it with the [simple wind component](simple-wind-component.md). As long as there is no such component in a scene, there won't be any wind.

## Querying Wind Values

At runtime you query the wind value by location. First you need to retrieve the wind world module:

```cpp
const ezWindWorldModuleInterface* pWindInterface = GetWorld()->GetModuleReadOnly<ezWindWorldModuleInterface>();
```

Make sure to check the pointer for `nullptr`, which happens when there is no wind system set up for a scene.

Then the wind can be queried by location:

```cpp
ezVec3 wind = pWindInterface->GetWindAt(position);
```

This returns a vector with the direction and strength of the wind at the queried position.

To react properly to wind, this value must be polled every frame. However, be careful to query only few values. Depending on the active system, this can be a very fast or a rather slow operation. However, usually wind doesn't change drastically within short distances. For example the [Kraut](../../terrain/kraut-overview.md) trees only query the wind once per tree instance, there is no need for finer detail.

> **Note:**
> 
> The wind system returns a vector of wind direction and strength. This alone often does not yield a convincing wind effect though. For example a tree or a piece of cloth would only be pushed to one side, but that looks very unnatural. Instead objects should *flutter* in the wind, e.g. wildly swing up and down or sideways. Such behavior is very object specific and must be implemented on top of the general wind value. The utility function `ezWindWorldModuleInterface::ComputeWindFlutter()` might be sufficient to get you started.

## Controlling Wind

To add wind locally, have a look at the [wind volume components](wind-volume-components.md). These can be used both for static wind fields, for example to make a flag blow in the wind nicely, as well as for short lived dynamic effects, such as the shockwave of an explosion.

## Affecting Physics Objects

Be aware that **wind does not affect** any [physics objects](../../physics/jolt/actors/jolt-dynamic-actor-component.md). Such behavior could be implemented, but it would be difficult to not have a serious performance impact, since it would keep the physics engine constantly busy (usually objects *go to sleep* when no forces act upon them, but wind would be a constantly active force).

Instead, explosions and such rather use a physics shape query to determine objects in range, and then apply a short impulse to only those objects once. See the [area damage component](../../gameplay/area-damage-component.md) as an example.

## Custom Wind Systems

It is possible to write your own wind system. Just implement a new [world module](../../runtime/world/world-modules.md), derive it from `ezWindWorldModuleInterface` and override the `GetWindAt()` function. Put your code into a custom [engine plugin](../../custom-code/cpp/engine-plugins.md) and also add a [custom component type](../../custom-code/cpp/custom-cpp-component.md) to instantiate your wind world module, and make it configurable.

For inspiration, just have a look at `ezSimpleWindWorldModule` and `ezSimpleWindComponent`.

## See Also

* [Wind Volume Components](wind-volume-components.md)
* [Simple Wind Component](simple-wind-component.md)
