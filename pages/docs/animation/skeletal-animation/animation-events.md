# Animation Events

*Animation events* are markers that are placed in [animation clip assets](animation-clip-asset.md) to indicate that something of interest happens at a certain time during playback.

These events can be used for mundane things like *foot down* markers, in a walking animation, to vital gameplay information like *shot fired* in an attack animation. 

Whenver the EZ animation system plays back any animation clip, it also inspects the *event track*. For every event that it encounters, it broadcasts an `ezMsgGenericEvent` with `Message` set to the value of the event's name.

If you have a [TypeScript](../../custom-code/typescript/typescript-overview.md) or [Visual Script](../../custom-code/visual-script/visual-script-overview.md) (or [custom C++ components](../../custom-code/cpp/custom-cpp-component.md) that is also an event handler) attached to any parent node of the animated mesh, you can handle this type of event and react with the desired game logic.

<video src="../media/anim-point-shoot.webm" width="500" height="500" autoplay loop></video>

In the video above, the clip contains a marker for when a shot is fired. A script reacts to this by spawning a projectile. In this example one could also just spawn the projectile at the same time at which the shoot animation is triggered, however, if the animation was longer, the exact time at which to do this, would be more difficult to estimate and using an event makes it much easier.

<video src="../media/anim-clip.webm" width="800" height="600" autoplay loop></video>

The clip above shows the event track at the bottom of an [animation clip asset](animation-clip-asset.md). This is how you add event markers to a clip. 

## See Also


* [Skeletal Animations](skeletal-animation-overview.md)
* [Event Nodes](animation-graphs/anim-nodes-events.md)
* [Custom Code](../../custom-code/custom-code-overview.md)
* [Messaging](../../runtime/world/world-messaging.md)
