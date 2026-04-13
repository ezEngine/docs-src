# Expressions

The expression system provides a small math language for evaluating per-element computations at runtime. It is used in places such as the [expression particle behavior](../effects/particle-effects/behaviors/pb-expression.md) or [visual scripts](visual-script/visual-script-overview.md).

## Syntax Overview

The language uses C-like syntax. A program consists of a sequence of statements, each terminated by a newline or semicolon. Comments are not supported.

```
outSize = inSize * 2.0
outColor.xyz = inColor.xyz * timeDiff
```

## Types

| Keyword | Aliases | Description |
|---------|---------|-------------|
| `bool` | — | Single boolean |
| `bool2`, `bool3`, `bool4` | — | Boolean vectors |
| `int` | — | Single integer |
| `int2`, `int3`, `int4` | `vec2i`, `vec3i`, `vec4i` | Integer vectors |
| `float` | — | Single float |
| `float2`, `float3`, `float4` | `vec2`, `vec3`, `vec4` | Float vectors |
| `var` | — | Type inferred from the right-hand side |

## Variables

Local variables must be declared before use:

```
float3 dir = normalize(inVel.xyz)
var speed = length(dir)
```

Input and output streams provided by the host (e.g. `inPos`, `outColor`) are pre-declared and do not need a declaration statement. Inputs are read-only; all outputs must be written before the program ends.

## Operators

**Arithmetic:** `+`, `-`, `*`, `/`, `%`

**Comparison:** `==`, `!=`, `<`, `<=`, `>`, `>=`

**Logical:** `&&`, `||`, `!`

**Bitwise:** `&`, `|`, `^`, `~`, `<<`, `>>`

**Ternary (select):** `condition ? valueIfTrue : valueIfFalse`

**Compound assignment:** `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`

## Swizzle

Vector components can be accessed and rearranged using swizzle notation with `xyzw` or `rgba`:

```
outColor.rgb = inColor.bgr   // swap red and blue
var d = inVel.w              // extract speed from velocity
```

Partial assignment is also supported:

```
outPos.y = 0.0               // zero out only the Y component
```

## Constructors

Vector values can be constructed by calling the type as a function:

```
var v = float3(1.0, 0.0, 0.0)
var c = float4(inColor.rgb, 1.0)
```

## Constants

| Name | Value |
|------|-------|
| `PI` | 3.14159… |
| `true` | Boolean true |
| `false` | Boolean false |

Integer literals may be written in hexadecimal (`0xFF`). Float literals require a decimal point or exponent.

## Built-in Functions

### Unary

| Function | Description |
|----------|-------------|
| `abs(x)` | Absolute value |
| `saturate(x)` | Clamps to `[0, 1]` |
| `sqrt(x)` | Square root |
| `exp(x)` | e raised to x |
| `ln(x)` | Natural logarithm |
| `log2(x)` | Base-2 logarithm |
| `log10(x)` | Base-10 logarithm |
| `pow2(x)` | 2 raised to x |
| `sin(x)` | Sine (radians) |
| `cos(x)` | Cosine (radians) |
| `tan(x)` | Tangent (radians) |
| `asin(x)` | Arc sine |
| `acos(x)` | Arc cosine |
| `atan(x)` | Arc tangent |
| `radToDeg(x)` / `rad_to_deg(x)` | Radians to degrees |
| `degToRad(x)` / `deg_to_rad(x)` | Degrees to radians |
| `round(x)` | Round to nearest integer |
| `floor(x)` | Round down |
| `ceil(x)` | Round up |
| `trunc(x)` | Truncate toward zero |
| `frac(x)` | Fractional part |
| `length(v)` | Vector length |
| `normalize(v)` | Unit vector |
| `all(b)` | True if all components are true |
| `any(b)` | True if any component is true |

### Binary

| Function | Description |
|----------|-------------|
| `min(a, b)` | Minimum |
| `max(a, b)` | Maximum |
| `pow(base, exp)` | Power |
| `log(x, base)` | Logarithm with given base |
| `mod(a, b)` | Modulo (also available as `%`) |
| `dot(a, b)` | Dot product |
| `cross(a, b)` | Cross product |
| `reflect(v, n)` | Reflect vector |

### Ternary

| Function | Description |
|----------|-------------|
| `clamp(x, min, max)` | Clamp to range |
| `lerp(a, b, t)` | Linear interpolation |
| `smoothstep(edge0, edge1, x)` | Hermite smooth interpolation |
| `smootherstep(edge0, edge1, x)` | Higher-order smooth interpolation |

## External Functions

The following functions may be registered by the host and available in specific contexts:

| Function | Description |
|----------|-------------|
| `random(seed)` | Pseudo-random float in `[0, 1)` |
| `perlinNoise(x, y, z)` | Perlin noise value |
| `sampleCurve(index, at)` | Sample a curve defined by the host at position `at` in `[0, 1]` |

Not all external functions are available in every context. See the documentation for the specific feature using expressions to find out which functions are provided.

## See Also

* [Expression Particle Behavior](../effects/particle-effects/behaviors/pb-expression.md)
