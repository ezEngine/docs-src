# Cloth Sheet Component

The *cloth sheet component* simulates a square patch of cloth as it hangs and swings in the wind. It is meant for decorative purposes such as flags.

<video src="media/wind-cone.webm" width="600" height="600" autoplay loop></video>

Cloth sheets are affected by [wind](wind/wind-overview.md) and movement of the owner object. They do not interact with physics objects and they don't collide with scene geometry.

## Component Properties

* `Size`: The physical size of the cloth sheet in the world.

* `Slack`: How much slack the cloth has along the X and Y axis. A value of zero means it is hung perfectly straight between its anchors. Positive values make it sag downwards.

* `Segments`: How detailed to simulate the cloth. Use as low values as possible, the simulation quickly becomes prohibitively expensive with higher tesselations.

* `Damping`: How quickly the cloth loses energy while swinging. Higher values make it come to rest more quickly, low values make it swing for a longer time. Once it comes to rest, it takes significantly less processing power.

* `WindInfluence`: How strongly [wind](wind/wind-overview.md) should make the cloth swing.

* `Flags`: These define at which corners and edges the sheet of cloth is attached to the world.

* `Material`: The [material](../materials/materials-overview.md) used for rendering the cloth. Make sure to set it to *two-sided* for cloth that can be seen from both sides.

* `Color`: An additional tint-color for rendering.

## See Also

* [Fake Rope Component](ropes/fake-rope-component.md)
* [Wind](wind/wind-overview.md)
