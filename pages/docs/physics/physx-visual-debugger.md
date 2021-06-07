# PhysX Visual Debugger

The *PhysX Visual Debugger* (PVD) is a stand-alone tool to inspect the state of the physics scene. It can be a very valuable tool when debugging physics related issues.

## Download

The tool can be downloaded here: [PhysX Visual Debugger](https://developer.nvidia.com/physx-visual-debugger) (NVIDIA account required)

## Usage

Just launch the PVD, then launch your game, either via [ezPlayer](../tools/player.md) or by [running a scene](../editor/run-scene.md). The PVD should then display the physics scene setup of your game. The PVD will not display anything when you only have a scene open in the editor for editing, as the engine will only create the PhysX objects once the simulation starts.

You may need to adjust the camera up axis in the PVD to align with the EZ coordinate system (+Z up, left-handed).

## See Also


* [PhysX Integration](physx-overview.md)
