# XR

> **NOTE:**
>
> XR support is still in development. You will need to enable *Show in Development Features* in the [editor settings](../editor/editor-settings.md) to use it.

*XR* stands for both *VR* (virtual reality) as well as *AR* (augmented reality) devices. Currently supported devices:

 1. **VR**: Windows desktop VR devices that support DX11 and OpenXR.

Currently there are three XR implementations:

1. **ezDummyXR**: If XR is requested and no other plugin is available the dummy XR implementation is used. This one allows for stereo rendering to be tested on a PC without needing to use an actual *HMD* (head mounted device).
2. **ezOpenXR**: This plugin uses *OpenXR* and supports both AR and VR devices, DX11 only for now.
3. **ezOpenVR**: WIP, currently not functional.

## Getting started

To get started with creating an XR application, please follow the [XR Project Setup](xr-project-setup.md) guide.

## See Also

* [XR Project Setup](xr-project-setup.md)
* [XR Graphics](xr-graphics.md)
* [XR Input](xr-input.md)
* [XR Components](xr-components.md)
