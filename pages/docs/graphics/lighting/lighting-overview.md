# Lighting

Lighting is the most important aspect of making a scene look good.

## Physically Based Rendering

There are many formulas for computing lighting on surfaces. The defacto industry standard, which is also used in ezEngine, is **P**hysically **B**ased **R**endering (PBR) which describes a surface in terms of *color*, the surface normals, its *roughness*, whether it is a *metal*. Using this data, very convincing lighting can be computed.

Therefore the standard type of [material](../../materials/materials-overview.md) requires you to provide such textures. Optionally an *occlusion texture* can pronounce the lighting for small crevices.

## Static vs. Dynamic Lighting

Many games differentiate between *static* or *baked* lighting, and *dynamic* lighting. Static lighting is precomputed and typically stored in *lightmaps* (dedicated textures) and other data structures. Dynamic lighting does not require any preprocessing or extra data. Baked lighting typically has the advantage that it can look much better because it can simulate light bounces and thus illuminate areas that are not directly lit.

Currently ezEngine **only supports dynamic lighting**. That means every light source that you add to the scene can be moved around and change its color or brightness. It also means that every light source has a performance cost. The renderer uses a clustered forward rendering approach which can handle a relatively large amount of light sources efficiently. The most important rule is to reduce the number of *overlapping* light sources. The editor [render modes](../../editor/editor-views.md#render-modes) allow you to look for hotspots.

## Shadows

Dynamic lights have the disadvantage that they don't provide shadows by default. Instead, casting shadows is a separate process, which costs a lot of performance for every light source involved. Therefore, each light source requires you to decide whether it should cast shadows or not. You can use many small fill lights, as long as they don't cast shadows, but you should keep the number of shadow casting lights as low as possible, and each light should only cover an area as small as possible.

For more details see the chapter about [dynamic shadows](dynamic-shadows.md).

## Light Component Types

There are different component types to provide different types of lighting:

* [Ambient Light Component](ambient-light-component.md): For lighting up a scene in general.
* [Directional Light Component](directional-light-component.md): For sun/moon light.
* [Point Light Component](point-light-component.md): For light bulbs and overall fill lights.
* [Spot Light Component](spot-light-component.md): For flashlights and directed lighting.
* [Sky Light Component](sky-light-component.md): For dynamic light contribution from the sky.

## See Also


* [Materials](../../materials/materials-overview.md)
* [Dynamic Shadows](dynamic-shadows.md)
* [Render Modes](../../editor/editor-views.md#render-modes)