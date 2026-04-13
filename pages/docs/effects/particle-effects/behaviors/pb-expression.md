# Expression Behavior

This behavior evaluates a math expression once per frame for each particle. The expression can read from and write to particle attributes, enabling custom per-particle logic that is not covered by other behaviors.

## Expression

The expression is a text field supporting the [expression language](../../../custom-code/expressions.md). It is evaluated in a SIMD-batched manner, operating on multiple particles at once.

### Input Streams

The following streams can be read by name in the expression:

| Name | Type | Description |
|------|------|-------------|
| `inPos` | vec3 | World-space position |
| `inVel` | vec4 | Velocity: xyz = direction, w = speed |
| `inColor` | vec4 | RGBA color and transparency |
| `inSize` | float | Particle size |
| `inRotSpeed` | float | Rotation speed |
| `inLifeTime` | vec2 | x = remaining lifetime in seconds, y = inverse of maximum lifetime |

### Output Streams

Write the following names to modify the corresponding particle attribute:

| Name | Type | Description |
|------|------|-------------|
| `outPos` | vec3 | World-space position |
| `outVel` | vec4 | Velocity: xyz = direction, w = speed |
| `outColor` | vec4 | RGBA color and transparency |
| `outSize` | float | Particle size |
| `outRotSpeed` | float | Rotation speed |
| `outDiscard` | bool | Set to `true` to remove the particle immediately |

### Global Variables

| Name | Type | Description |
|------|------|-------------|
| `timeDiff` | float | Elapsed time in seconds since the last frame |

Effect [input parameters](../../../concepts/exposed-parameters.md) (both float and color) are accessible by their parameter name directly.

### Curve Sampling

Curves defined in the **Inputs** array can be sampled with:

```
sampleCurve(index, at)
```

`index` is the zero-based position in the Inputs array. `at` is the lookup position in the `[0; 1]` range.

## Inputs

An array of curve inputs that the expression can sample at runtime. Each entry specifies either an inline curve or a shared [curve asset](../../../animation/common/curves.md).

## See Also

* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
