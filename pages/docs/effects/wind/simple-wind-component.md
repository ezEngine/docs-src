# Simple Wind Component

The *simple wind component* implements a very basic [wind system](wind-overview.md). By placing a component of this type in a scene, the *simple wind [world module](../../runtime/world/world-modules.md)* is created. Things that can react to wind are then able to retrieve a wind value at any location. The simple wind system provides one global wind value, which changes randomly.

Additionally, it supports [wind volume components](wind-volume-components.md). If any such shape is in a scene, its contribution is added to the global wind value, for objects that are inside such a volume.

## Component Properties

* `MinWindStrength`, `MaxWindStrength`: The minimum and maximum strength with which the wind shall blow. A random value in between will be chosen every couple of seconds. To make it easier to get different things working well with each other, the wind values are hard-coded. They are inspired by the [Beaufort scale](https://en.wikipedia.org/wiki/Beaufort_scale). Most things that can react to wind (for example [particle effects](../particle-effects/particle-effects-overview.md) or [ropes](../ropes/fake-rope-component.md)) also have a *wind influence* parameter for tweaking how strongly they react to wind. The Beaufort scale enables you to get an idea what reaction to expect, e.g. you know how an effect should look under a light breeze or under storm conditions, and can then tweak the wind influence value accordingly.

* `MaxDeviation`: How much the wind direction may deviate from the local x-axis. Set this to the maximum value, if the wind is allowed to come from anywhere.

## See Also

* [Wind](wind-overview.md)
* [Wind Volume Components](wind-volume-components.md)
