# Sky

By default the background of a rendered scene is black. To change this, you need to create a game object in the scene and attach a sky component.

## SkyBox component

The *SkyBox component* implements a simply sky, which displays a cubemap texture as a static background. The position and scale of the game object has no effect on the sky, it will always appear behind all other geometry. The rotation, however, can be used to orient the sky as desired.

* **CubeMap**: The cubemap [texture asset](../graphics/textures-overview.md) to use.

* **ExposureBias**: This specifies how bright the sky will appear. A higher value results in a brighter sky.

* **InverseTonemap**: Switches the tonemapping mode. For HDR skyboxes this should stay off. For skyboxes that do not have high-dynamic range values, enabling this mode will improve brightness and contrast of the colors.

* **UseFog, VirtualDistance**: If enabled, [fog](fog.md) will be applied to the sky. In that case *VirtualDistance* is being used to compute how foggy the sky should appear.

## See Also


* [Fog](fog.md)
* [Textures](../graphics/textures-overview.md)
* [Lighting](../graphics/lighting/lighting-overview.md)
