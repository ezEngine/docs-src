# Basic FPS Project Template

The **Basic FPS** template is available for [project creation](../docs/projects/projects-overview.md#creating-a-project). It acts both as a sample and as a starting point for your own game.

Click the image below for a playthrough video:

[![video](https://img.youtube.com/vi/VkgtSEl7j_I/0.jpg)](https://www.youtube.com/watch?v=VkgtSEl7j_I)

## Template Specifics

The template is meant for getting started on a first-person shooter game.

The following steps are already taken care of:

* A player [character controller](../docs/physics/jolt/special/jolt-character-controller.md) is fully set up.
* [Input](../docs/input/input-overview.md) is configured for mouse + keyboard controls.
* Physics [collision layers](../docs/physics/jolt/collision-shapes/jolt-collision-layers.md) are configured.
* [Tags](../docs/projects/tags.md) are set up, for the game code to find certain objects in the world.
* A few [surface assets](../docs/materials/surfaces.md) are set up to provide a sample for how to make surface specific footstep sounds and bullet impact effects.
* Two [scenes](../docs/scenes/scene-editing.md) are provided, when the player reaches the end of the *Main* scene, the game transitions to the second one.
* All game logic is written in [AngelScript (TODO)](../docs/custom-code/angelscript/angelscript-overview.md).
* The project comes with an enemy type that uses the [AI navigation component](../docs/ai/AiPlugin/navigation-component.md) for path finding and steering.
* And FMOD project is set up for making [sound](../docs/sound/sound-overview.md).
* The gameplay code shows how to make basic weapons, health pickiups and explosions.

## See Also

* [Projects](../docs/projects/projects-overview.md)
* [Samples](samples-overview.md)
* [Videos](../getting-started/videos.md)
