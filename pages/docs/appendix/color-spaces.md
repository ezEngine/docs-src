# Color Spaces

Color spaces are a fundamental concept in computer graphics. Understanding the difference between linear and gamma (sRGB) color spaces is crucial for achieving correct color representation and lighting in your projects.

This page gives a very brief introduction, for more in-depth explanations, please consult online resources.

## What is Linear Space

Linear color space is the representation of colors how people would *expect* colors to work. Here a value of `0.5` is half as bright as a value of `1.0`. Or if encoded as bytes, a value of 128 is half as bright as a value of 256.

Consequently, doing mathematical operations with them make sense. For instance, multiplying an RGB value of `(64, 64, 64)` (a dark grey) by `2` results in the RGB value `(128, 128, 128)`. If these values are in linear space, the perceived brightness is then also doubled.

## What is Gamma Space (sRGB)

Gamma (or sRGB) color space is the representation of colors that nobody expects, but that is used in practice nearly everywhere where colors are saved with one byte per channel.

Gamma space is *only relevant for 8-bit-per-channel* colors. Once a color is stored with 16 or 32 bits per channel, it is always in linear space. The reason is, that Gamma space is basically a compression method and when more storage space is available, this compression is not necessary anymore.

Basically, human vision is pretty good at distinguishing dark color shades, whereas it is pretty bad at distinguishing bright colors. The reason is simply, that humans need to be able to see as much as possible in the dark, so our eyes are more sensitive to darker shades.

8 bits per channel is not enough to represent the many shades of colors that the human eye can distinguish and this is especially true for the darker color shades. To still be able to store colors reasonably well with just 8 bits per channel (24 bits per RGB pixel), the sRGB color space uses more bits to represent darker colors and only few bits to represent bright colors.

As a consequence, the RGB color value `(64, 64, 64)` in Gamma space appears much darker than the same value when interpreted in linear space. Also multiplying it by `2`, while still resulting in the same mathematical value of `(128, 128, 128)` results in a grey value that is not perceived as *twice as bright*. Consequently, although doing mathematical operations with sRGB values works and gives believable results, they are mathematically incorrect.

However, all the lighting, blending and filtering operations that are done in 3D graphics rely on mathematical correctness and break when they are done in sRGB space.

*Fun fact:* The vast majority of programs do their color calculations in Gamma space. Outside of the realm of 3D graphics, most programmers are not aware of this problem and even many professional programs do this incorrectly.

## Practical Uses

In practice nearly all photos and textures that represent visual images are stored in Gamma space (except HDR images).

However, artificial textures like *normal maps*, *roughness textures* and pretty much all other textures that store calculated data, treat the pixel values as linear values.

The GPU is capable of automatically converting sRGB values to linear space, as long as it knows that a texture holds such data. That's the reason why [textures](../graphics/textures-overview.md) have a *usage* parameter, where you need to select wether the texture contains *real colors* (e.g. a photo) or just *data* (e.g. roughness). This way, the GPU can take care of the conversion, and the shader code can then work with all values in linear space.

## Color Classes in ezEngine

ezEngine provides several color classes to help you work correctly with different color spaces:

- **ezColor**: Represents an RGBA color in linear space, using floating-point values. This is the main class for color computations. Colors don't have to be store this way, but when you need to manipulate a color, always assign it to an `ezColor` instance first, then do the calculations, and afterwards assign it back to the desired storage format.
- **ezColorGammaUB**: Stores colors in gamma (sRGB) space using 8 bits per channel. This is the format typically used for images and textures intended for display. This is also the format that all 8-bit color values are displayed in in paint programs or CSS files.
- **ezColorLinearUB**: Stores colors in linear space using 8 bits per channel (unsigned byte). This should only be used when it is absolutely crucial to store a color with 8 bits per channel and the value has to already be converted to linear space. This is nearly only the case for vertex color streams.

### Example: Converting Between Spaces

When you hardcode a color from a paint program (which gives you sRGB values), you can convert it to linear space like so:

```cpp
// Convert from sRGB (gamma) to linear
// Cornflower Blue: sRGB(100, 149, 237)
ezColor linear = ezColorGammaUB(100, 149, 237);
```

When you want to display a color in the UI, convert it back to gamma space:

```cpp
// Convert from linear to sRGB (gamma)
ezColorGammaUB gamma = ezColor(0.39f, 0.58f, 0.93f);
```

## See Also

- Code documentation of `ezColor`.
* [Gamma and Linear Space: What They Are & How They Differ](https://kinematicsoup.com/news/2016/6/15/gamma-and-linear-space-what-they-are-how-they-differ)
* [Unity Manual: Differences between linear and gamma color space](https://docs.unity3d.com/6000.1/Documentation/Manual/differences-linear-gamma-color-space.html)
* [Linear, Gamma, and sRGB Color Spaces (Matt77hias Blog)](https://matt77hias.github.io/blog/2018/07/01/linear-gamma-and-sRGB-color-spaces.html)
