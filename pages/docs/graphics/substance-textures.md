# Substance Textures

EZ has support for [Substance Designer](https://www.adobe.com/products/substance3d-designer.html) textures. This is provided through the *Substance* plugin. Once you [enable the plugin](../projects/plugin-selection.md), the *Substance Package* asset type is available.

This asset type allows you to reference a `*.sbs` file. Then you can define which *graphs* to import from the SBS file.

The outputs of the substance material are made available as *Substance Texture* assets. These can be referenced anywhere, where any other [2D texture](textures-overview.md) could be used.

> **Note:**
>
> The Substance integration is only an editor feature. At runtime there is no procedural texture generation. Thus, there is also no memory saving for using SBS files over regular textures. This is purely a convenience feature for people who use Substance Designer, so that they don't need to manually export the textures. Instead the EZ editor takes care of updating the outputs for you. 

> **Important:**
>
> This feature requires you to have Substance Designer installed and a valid license for its usage. If you want to use this workflow in a team, **every user of the editor** must have Substance Designer on their machine, otherwise asset transform will fail for them.

## See Also

* [Textures](textures-overview.md)
* [Substance Designer](https://www.adobe.com/products/substance3d-designer.html)
