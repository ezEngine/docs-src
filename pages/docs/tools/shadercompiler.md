# ShaderCompiler

The *ShaderCompiler* is a command-line application to precompile shader permutations.

This tool can be used to prepare shaders and shader permutations before they are needed at runtime. On platforms where runtime shader compilation is possible, EZ will compile shader permutations on demand. This leads to a small delay when a new permutation is encountered, but is very convenient during development.

By precompiling all necessary permutations, it is possible to prevent this delay. On platforms that do not allow runtime shader compilation this is even necessary for the shaders to be available, at all.

## Command Line Options

For the full list of available command line options, run

```cmd
ShaderCompiler.exe -help
```

* `-project <path>`: The compiler takes a path to a [project](../projects/projects-overview.md) to resolve paths relative to the project directory.

* `-platform <name>`: The name of the target platform for which to compile the shaders. For example `DX11_SM50`. See the command line help for all options.

* `-shader <path1;path2>`: Semicolon separated list of paths to shader files or folders containing shaders. Paths may be absolute or relative to the *-project* directory. If a path to a folder is specified, all .ezShader files in that folder are compiled.

* `-perm <PERM1=TRUE PERM2=11>`: List of permutation variables to set to fixed values. For all other permutation variables, all possible combinations are used to compile the shaders. Spaces are used to separate multiple arguments.

## Example

```cmd
ShaderCompiler.exe -project "C:\ez\Data\Base" -platform DX11_SM50 -shader "Shaders\Debug" -perm TOPOLOGY=TOPOLOGY_LINES CAMERA_MODE=CAMERA_MODE_PERSPECTIVE
```

## See Also


* [Shaders (TODO)](../graphics/shaders/shaders-overview.md)