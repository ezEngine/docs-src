# Color Animation Component

The *color animation component* allows you to apply an animated [color gradient](../common/color-gradients.md) to other components, such as [meshes](../../graphics/meshes/mesh-component.md) or [light sources](../../graphics/lighting/lighting-overview.md) or any other component type that handles the message type `ezMsgSetColor`.

> **Important:**
>
> This component has no effect on its own. It tries to change the color of other attached components. If no other component has a main color or doesn't handle the message `ezMsgSetColor`, there will be no effect.

> **Note:**
>
> If an attached component does handle the `ezMsgSetColor`, but doesn't properly update its color dynamically when combined with this component, it may not invalidate its cached render data correctly. A temporary work around is to set the game object's mode to `Force Dynamic`.

## Component Properties

* `Gradient`: The [color gradient](../common/color-gradients.md) to use. The gradient will be sampled from left to right over `Duration` seconds. Each time the sampled color is put into an `ezMsgSetColor` and that [message is sent](../../runtime/world/world-messaging.md) to all other components that are attached to the same object.
* `Duration`: The duration that the color gradient should last before it is being repeated.
* `SetColorMode`: The mode with which to modify the color of the affect object. Although the color can be blended into the target object's color, for many components this quickly results in a fully black or fully white result, as the modifications accumulate with each change.
* `AnimationMode`: How to continue sampling the color gradient, once the end has been reached.
* `RandomStartOffset`: If enabled, the component starts with a random time offset. This way prevents synchronous playback, if multiple objects use the same animation.
* `ApplyToChildren`: Whether to send the `ezMsgSetColor` only to components on the same game object, or also to all components in the entire sub-graph. This can be used to modify the color of many objects in sync.

## See Also

* [Property Animation (TODO)](property-animation-overview.md)
* [Color Gradients](../common/color-gradients.md)
