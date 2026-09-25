# Terrain Brush 2D Component

The *Terrain Brush 2D Component* modifies [terrain patches](terrain-patch-component.md) and [terrain volumes](terrain-volume-component.md) by raising or lowering it or painting a material onto it. Multiple brushes can overlap to form complex geometry.

<video src="media/terrain-brush-2d.mp4" autoplay controls></video>

For an overview of the terrain system, see [Terrain System](terrain-plugin-overview.md).

## Modify Modes

The `ModifyMode` property selects how the brush affects the terrain. **Raise** pulls the terrain up towards the brush, **Lower** pushes terrain down towards the brush. Vertices that are already above (when raising) or below (when lowering) the brush, are unaffected. **Set**, however, raises *and* lowers the terrain.

*Raise* is used to create mountains, *Lower* can be used to flatten an area, *Set* is useful for roads and riverbeds that are always at a fixed height.

**Paint Only** does not affect height, and only assigns a material. For material painting to work, `Material Strength` must be set to a non-zero value (usually `1`) and `Material Index` can then be used to select the material layer to paint.

**Displace** adds a signed noise offset to whatever height the terrain already has, rather than blending it towards the brush. The brush Z position is not used at all, and the brush does nothing unless `NoiseStrength` is non-zero. Use it as a detail overlay: a large brush with a soft falloff and ridged or warped noise adds erosion-like structure across an existing mountain without flattening its silhouette. *Displace* only works on terrain patches, terrain volumes ignore it.

## Footprint

The brush footprint is a rounded rectangle oriented by the owner object's rotation in the XY plane. The yellow line represents the inner shape, the green line the outer shape. The 2D brushes affect all terrain *below and above* them (depending on the *modify mode* they lower or raise the terrain).

`HalfSizeX`,`HalfSizeY` — Half-length of the straight edge along the local X and Y axis. Setting both to `0` produces a circle (top left image). Setting one to `0` produces a line (top right image).

`InnerRadius` — Corner rounding of the full-weight region. Setting this to zero produces a point or rectangle (bottom left image). Positive values give a circle (top left) or rounded rectangle (bottom right image)

![Brush Shapes](media/brushes-2d.jpg)

`OuterRadius` — Corner rounding of the falloff zone. The outer edge of the brush is at *InnerRadius + OuterRadius*. Vertices between the inner and outer edge are blended across that zone, shaped by *Sharpness*. Setting this to 0 gives a hard edge.

`Sharpness` — How abruptly the brush transitions from full strength to nothing, between `0` and `1`. `0` is a smooth, natural falloff across the whole zone between the inner and outer radius. Higher values compress the transition towards the middle of that zone, flattening the brush centre and the outer edge while steepening what is between them, until at `1` the change happens across roughly a seventh of the zone.

`Sharpness` deliberately does not move the point at which the brush reaches half strength, nor how wide the falloff zone is — those are what `InnerRadius` and `OuterRadius` are for. Use the radii to say *where* the edge is and how far it reaches, and `Sharpness` to say how hard it is.

| `Sharpness` | transition occupies | |
|---|---|---|
| 0 | 73% of the falloff zone | a natural hill |
| 0.25 | 29% | a firm edge |
| 0.5 | 18% | a steep bank |
| 1 | 10% | close to a cliff |

## Material Painting

Material painting let's you change the material layer that is used in some area. Material painting is activated by setting `MaterialStrength` to a non-zero value. If `ModifyMode` is set to *Paint Only*, the brush doesn't affect the geometry. In the example below, *noise* is also used, to make the pattern more natural.

`MaterialIndex` — The material layer index (0–31) to paint within the brush footprint.

`MaterialStrength` — Blend weight applied to *MaterialIndex* at the brush center. 0 disables painting; 1 fully assigns the material within the inner zone.

![Material Painting](media/brushes-paint.jpg)

## Noise

Noise affects both geometry and material painting. Noise is used to introduce random patterns to make the result more natural. See the image below for an example where the same brush settings are used, only with varying noise strength and frequency.

`NoiseType` — The shape of the noise.

| Type | Description |
|------|-------------|
| `None` | No noise. All other noise properties are hidden. |
| `FBM` | Sum of octaves. Rolling, evenly distributed hills. |
| `Ridged` | Sharp ridge lines running between smooth valleys. Mountain ranges. Detail concentrates along the ridges, so the valleys between them stay clean. |
| `Billow` | Rounded humps with rounded hollows between them and no sharp edges anywhere. Dunes and boulder fields. |
| `Terraced` | Quantized into flat steps with a sharp riser. Mesas and plateaus. |

*Ridged* and *Billow* are biased upwards, so in *Displace* mode a negative `NoiseStrength` flips them into carved channels and canyons.

Each type sits on its own part of the noise lattice, so switching between them gives a genuinely different pattern rather than the same features with a different profile.

`NoiseStrength` — Vertical noise amplitude in world units. 0 disables the vertical displacement. This has no effect on 3D brushes, which have no height axis.

Which *side of the brush plane* the noise displaces towards follows from the modify mode, so that by default it can never push the surface past the boundary the mode promises. *Raise* cuts downwards from the plane, keeping the result below it; *Lower* builds upwards from the plane, keeping the result above it. *Set* has no such boundary and displaces both ways. *Displace* has no plane at all.

A negative `NoiseStrength` moves the band to the other side of the plane. That deliberately gives up the mode's boundary — a *Raise* brush with negative noise strength reaches above its own height — so it only happens when you ask for it.

| Mode | `NoiseStrength` > 0 | `NoiseStrength` < 0 |
|------|---------------------|---------------------|
| `Raise` | brush height − amplitude … brush height | brush height … brush height + amplitude |
| `Lower` | brush height … brush height + amplitude | brush height − amplitude … brush height |
| `Set` | ± amplitude around the brush height | ± amplitude around the brush height |
| `Displace` | adds up to the amplitude | subtracts up to the amplitude |

Throughout, a higher noise value means higher terrain. Neither the mode nor the sign ever flips which end of the noise ends up on top, so the crests of `Ridged` stay crests in every combination instead of turning into grooves in some of them.

The noise is normalized so that its peaks reach the full amplitude. A *Raise* brush's highest points therefore touch the brush plane exactly, rather than stopping short of it and sinking further the more amplitude is used.

`NoiseFrequency` — World-space size of one noise cell. Small values make the effect very local, producing high-frequency noise, higher values are useful for larger terrain features, like mountains.

`NoiseEdge` — Perturbs the brush outline sideways, relative to `OuterRadius`, without changing heights. Use it to break up the regular rounded-rectangle silhouette, particularly for material painting. It is separate from `NoiseStrength` so that an irregular outline doesn't force a bumpy surface, and vice versa. The perturbation fades out towards the brush edge so that the footprint stays contained.

`NoiseWarp` — Displaces the noise lookup by a second, coarser noise before sampling. This stretches and swirls the pattern into flowing bands instead of evenly spread blobs, which reads as strata or water-carved channels. 0 disables it, values around 1 give a strong effect.

`NoiseSeed` — Two brushes with the same frequency, placement and rotation produce identical noise. Change the seed to make them differ.

The noise pattern is rotated by the brush, so turning the brush around its up axis turns the pattern with it. It is not otherwise attached to the brush: moving the brush slides it over the noise rather than carrying the pattern along. That is what lets the many stamps a spline brush generates share one continuous noise field instead of each repeating the same pattern.

![Noise](media/brush-noise.jpg)

## Shared Properties

`Priority` — Brush evaluation order. Brushes with higher priority are applied later and win over lower-priority brushes in the same region. It is very rarely necessary to adjust this, but if you have multiple brushes in the same area and one brush doesn't have the effect that you expect it to have, increase its priority, to make it more dominant.

`AffectPatches`, `AffectVolumes` — Whether the brush applies to [terrain patches](terrain-patch-component.md) or [terrain volumes](terrain-volume-component.md). By default 2D brushes only affect terrain patches, and 3D brushes only affect volumes.

`Tags` — When non-empty, the brush only affects terrain objects whose *TerrainTags* contain at least one matching tag. Empty tags match all terrain objects. This can be used on complex scenarios, to control precisely which brush affects which piece of terrain. For instance, you could place two heightfields above each other and now need to separate between brushes that affect the top or bottom one.

## Spline Brushes

When a [Spline Component](../animation/paths/spline-component.md) is attached to the same game object, the brush stamps along the full length of the spline. This is useful for mountain chains, roads, rivers and tunnels. The brush settings are the same everywhere along the spline, so to make a path wider at some point, you would either add another brush on top there, or stop the spline and start a new one, with different brush settings.

![Brush Path](media/brush-path.jpg)

## See Also

* [Terrain System](terrain-plugin-overview.md)
* [Terrain Patch Component](terrain-patch-component.md)
* [Terrain Brush 3D Component](terrain-brush-3d-component.md)
