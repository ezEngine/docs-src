# Shader Debugging

To debug a shader, one can configure it such that the shader compiler includes debugging information. To do so, include **DEBUG** as a platform in the **[PLATFORMS]** section of the shader:

```cpp
[PLATFORMS]

ALL
DEBUG

[PERMUTATIONS]

ALPHATEST
WIREFRAME

[RENDERSTATE]

#if WIREFRAME == 1
  WireFrame = true
#endif

[VERTEXSHADER]

VS_OUT main(VS_IN Input)
{
  ...
}

[PIXELSHADER]

...
```

## See Also

* [Shaders (TODO)](shaders-overview.md)
* [Shader Templates](shader-templates.md)
* [ShaderCompiler](../../tools/shadercompiler.md)
