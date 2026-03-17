# ezTexConv

TexConv is a command-line tool to process textures from typical input formats like PNG, TGA, JPEG and DDS into optimized formats for runtime consumption.
The most common scenario is to convert a single input file `A.xxx` into an optimized format `B.yyy`. However, the tool has many additional options for advanced uses.

TexConv operates in one of three modes, selected with `-mode`:

* `-mode Convert` (default): Full texture conversion with channel mapping, compression, mipmap generation, etc.
* `-mode Compare`: Compare two images and produce difference images and an HTML report.
* `-mode Reduce`: Convert DDS or TGA files to JPG or PNG to reduce file size, without any texture processing.

## Command-line Help

Run TexConv.exe with the `--help` parameter to list all available options. Additionally, TexConv prints the used options when it is executed, to help understand what it is doing. Consult this output for details.

## General Usage

TexConv typically produces **one output** file. It may use **multiple input** files to assemble the output from. For the assembly, it also needs a **channel mapping**, which tells it which channel (*Red, Green, Blue* or *Alpha*) to take from which input file and move it into which channel of the output image.

The most straight forward command line is this:

```cmd
TexConv.exe -out D:/result.dds -in0 D:/img.jpg -rgba in0
```

* `-out` specifies the output file and format
* `-in0` specifies the first input image
* `-rgba` tells it that the output image should use all four channels and that they should be taken 1:1 from the input image

## Multiple Input Files

To assemble the output from multiple input files, specify each input file using the `-in` option with an increasing number:

```cmd
-in0 D:/img0.jpg -in1 D:/img1.jpg -in2 D:/img2.jpg ...
```

When assembling a cubemap from 2D textures, one can also use `-right`, `-left`, `-top`, `-bottom`, `-front`, `-back` or `-px`, `-nx`, `-py`, `-ny`, `-pz`, `-nz`.

To map these inputs to the output file, a proper channel mapping is needed.

## Channel Mappings

The channel-mapping options specify from which input to fill the given output channels. You can specify the input for each channel individually like this:

```cmd
-r in0.b -g in0.g -b in0.r -a in1.r
```

Here the RGB channels of the output would be filled using the first input image, but red and blue will get swapped. The alpha channel of the output would be filled with the values from the red channel of the second input image.

Specifying the mapping for each channel separately gives the greatest flexibility. For convenience the same can be written using "swizzling" operators:

```cmd
-rgb in0.bgr -a in1.r
```

### Output Channels

The following channel-mapping options are available:

* `-r`, `-g`, `-b`, `-a` : These specify single channel assignments.
* `-rg` : Specify the red and green channel assignments.
* `-rgb` : Specify the red, green and blue channel assignments.
* `-rgba` : Specifies all four channel assignments.

Mentioning only the R, RG or RGB channel, instructs TexConv to create an output file with only 1, 2 or 3 channels respectively.

### Input Swizzling

When stating which input texture should fill which output channel, one can swizzle the input:

* `-rgba in0` is equivalent to `-rgba in0.rgba`
* `-rgba in0.bgra` will swizzle the input channels
* `-rgb in0.rrr` will duplicate the red channel into all channels

One may also fill channels with either black or white:

* `-rgb in0 -a white` will create a 4 channel output texture but set alpha to fully opaque
* `-rg black -b white` will create an entirely blue texture

## Common Options

The most interesting options are listed below. More options are listed by `TexConv --help`.

### Output Type

* `-type 2D` : The output will be a regular 2D image.
* `-type Cubemap` : The output will be a cubemap image. Only supported for DDS output files. When this is specified, one can assemble the cubemap from 6 regular 2D input images.

### Image Compression

* `-compression none` : The output image will be uncompressed.
* `-compression medium` : If supported, the output image will use compression without sacrificing too much quality.
* `-compression high` : If supported, the output image will use compression and sacrifice quality in favor of a smaller file.

### Mipmaps

By default, TexConv generates mipmaps when the output format supports it.

* `-mipmaps none` : Mipmaps will not be generated.
* `-mipmaps Linear` : If supported, mipmaps will be generated using a box filter.

### Usage (sRGB / Gamma Correction)

The `-usage` option specifies the purpose of the output and thus tells TexConv whether to apply gamma correction to the input and output files. The usage only affects the RGB channels. The alpha channel is always considered to contain 'linear' values. If usage is not specified, the 'auto' mode will try to detect the usage from the format and file-name of the first input image. For instance, single and dual channel output formats are always linear. Check the output to see what decision TexConv made.

* `-usage Linear` : The output image contains values that do not represent colors. This is typically the case for metallic and roughness textures, as well as all kinds of masks.

* `-usage Color` : The output image represents color, such as diffuse/albedo maps. The sRGB flag will be set in the output DDS header.

* `-usage HDR` : The output file should use more than 8 bits per pixel for encoding. Consequently all values are stored in linear space. For HDR textures it does not matter whether the data represents color or other data.

* `-usage NormalMap` : The output image represents a tangent-space normal map. Values will be normalized and mipmap computation will be optimized slightly.

* `-usage NormalMap_Inverted` : The output is a tangent-space normal map with Y pointing in the opposite direction than the input.

### Image Rescaling

* `-minRes 64` : Specifies the minimum resolution of the output. If the input image is smaller, it will get upscaled.
* `-maxRes 1024` : Specifies the maximum resolution of the output. If the input image is larger, it will get downscaled.
* `-downscale 1` : If this is larger than 0, the input images will be halved in resolution N times. Use this to apply an overall quality reduction.

### Image Comparison

TexConv can also compare two images and generate difference images and an HTML page with embedded images for easy inspection.

Use `-mode Compare` to enable comparison mode, and the `-cmpXYZ` options to configure which images to compare and what outputs to generate. Consult the `--help` output for details.

## Reduce Mode

Reduce mode converts DDS and TGA files to JPG or PNG without applying any texture processing such as compression or mipmap generation. It is intended to reduce the on-disk size of imported source assets.

The output format is chosen automatically based on the alpha channel:

* If the image has no meaningful alpha (all pixels fully opaque), it is saved as **JPG**.
* If the image contains any non-trivial alpha values, it is saved as **PNG**.

If an output file with the target name already exists, the file is skipped.

### Reduce Mode Options

* `-in` : Path to the input file, or a folder path. Append `*` to the folder path to process subdirectories recursively (e.g. `-in "D:/textures/*"`).
* `-out` : Optional output path. Can be an existing directory, a direct output file path, or a directory path with a trailing `*` to mirror the input subfolder structure in the output.
* `-deleteSource` : If set to `true`, the source file is deleted after a successful conversion.

### Reduce Mode Examples

Convert a single file:

```cmd
TexConv.exe -mode Reduce -in D:/texture.dds
```

Convert all DDS and TGA files in a folder recursively, deleting the originals:

```cmd
TexConv.exe -mode Reduce -in "D:/textures/*" -deleteSource true
```

Convert files in a folder and place outputs in a separate directory, mirroring the folder structure:

```cmd
TexConv.exe -mode Reduce -in "D:/textures/*" -out "D:/output/*"
```

## Utility Scripts for Reducing Texture Sizes

The repository provides PowerShell scripts in `Utilities/Scripts/` to automate texture size reduction on a folder of assets.

### reduce-texture-sizes.ps1

Orchestrates DDS/TGA conversion and optional post-processing of the resulting JPG and PNG files.

```powershell
./reduce-texture-sizes.ps1 "C:/path/to/folder" [-Convert] [-OptimizeJpeg] [-OptimizePng]
```

* `-Convert`: Runs TexConv in reduce mode on all DDS and TGA files in the folder (recursively). Source files are deleted after successful conversion.
* `-OptimizeJpeg`: Runs `optimize-jpeg.ps1` on all JPG files afterwards.
* `-OptimizePng`: Runs `optimize-png.ps1` on all PNG files afterwards.

### optimize-jpeg.ps1

Recompresses all JPG files in a folder using [mozjpeg](https://github.com/imagemin/mozjpeg-bin). Requires Node.js and mozjpeg installed globally (`npm install --global mozjpeg`). Files inside `AssetCache` directories are skipped.

```powershell
./optimize-jpeg.ps1 "C:/path/to/folder"
```

### optimize-png.ps1

Recompresses all PNG files in a folder using `optipng`, which ships with the repository at `Data/Tools/Precompiled/optipng/optipng.exe`. Files inside `AssetCache` directories are skipped.

```powershell
./optimize-png.ps1 "C:/path/to/folder"
```

## Examples

### Convert a Color Texture

```cmd
TexConv.exe -out D:/diffuse.dds -in0 D:/diffuse.jpg -rgba in0 -usage color
```

### Convert a Normal Map

```cmd
TexConv.exe -out D:/normalmap.dds -in0 D:/normalmap.png -rgb in0 -usage normalmap
```

### Create an HDR Cubemap

```cmd
TexConv.exe -out "D:/skybox.dds" -in0 "D:/skymap.hdr" -rgba in0 -type cubemap -usage hdr
```

A great source for HDR cubemaps is [hdrihaven.com](https://hdrihaven.com/hdris/).

### Bake Multiple Images into One

```cmd
TexConv.exe -out "D:/Baked.dds" -in0 "D:/metal.tga" -in1 "D:/roughness.png" -in2 "D:/DiffuseAlpha.dds" -r in1.r -g in0.r -b black -a in2.a -usage linear
```

### Extract a Single Channel

```cmd
TexConv.exe -out D:/alpha-mask-only.dds -in0 D:/DiffuseAlpha.dds -r in0.a
```

## See Also

* [Textures](../graphics/textures-overview.md)
