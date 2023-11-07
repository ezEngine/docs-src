# Sample Sequence Node

The *sample sequence node* plays multiple clips in a row. One clip is used to enter the animation sequence, then there can be one or multiple different clips that may be played in a loop, and once the loop is exited, another clip can be played to finish the sequence. 

Such sequences are common for actions such as jumping or climbing a ladder. The start clip transitions the character from a start state, such as idle or walking into the new state, such as *jumping*. The middle clip is then played as long as the jumping state needs to continue, and once the character hits the ground again, the end clip is played to transition back.

<video src="../../media/anim-point-shoot.webm" width="500" height="500" autoplay loop></video>

The video above shows such a sequence. Here the node uses a *point gun* and a *shoot gun* clip for the middle part of the sequence, but it doesn't use a start or end clip at all (they are optional). Using the `Clip Index` input pin, the game code can switch at any time whether the gun is pointed or shot. One of the two clips is played in a loop as long as the game code decides to keep this state active. Here raising and lowering the arm is simply a result from fading the animation in and out over a short duration, but if desired these could also be dedicated animation clips.

## Node Properties

Most node properties are the same as on the [sample clip node](anim-nodes-sample-clip.md#node-properties).

* `Start Clip`: The [animation clip](../animation-clip-asset.md) to start with. This clip should end on a keyframe from where the `Middle Clips` can continue seemlessly.

* `Middle Clips`: One or multiple animation clips to play after the `Start Clip`. These get looped as long as the `Loop` property is enabled. If more than one clip is added, which one to play can be selected using the `Clip Index` pin. Otherwise a random one will be selected on every iteration.

* `End Clip`: The clip to play when the *looped* property is disabled after the start and middle clip are finished.

## Input Pins

Most input pin properties are the same as on the [sample clip node](anim-nodes-sample-clip.md#input-pins).

* `Clip Index`: This pin can be used to select which of the `Middle Clips` to play next. In the video above this is used to select whether the gun should get fired or not.

## Output Pins

Most output pin properties are the same as on the [sample clip node](anim-nodes-sample-clip.md#output-pins).

* `On Middle Started`: This event pin is triggered every time a middle clip starts playing.
  
* `On End Started`: This event pin is triggered when *looping* is disabled and the `End Clip` starts playing.

## See Also

* [Animation Graph](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
