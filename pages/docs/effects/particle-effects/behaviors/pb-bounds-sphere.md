# Bounds Sphere Behavior

<video src="../media/bounds-sphere.mp4" width="500" height="500" autoplay loop></video>

This behavior confines particles to a spherical volume. Particles that leave the sphere are either killed or pushed back to the sphere surface. This behavior can be used to prevent particles from straying too far from the center or to make it suddenly stop at a given distance.

**CenterOffset:** The center of the sphere relative to the particle system's origin.

**Radius:** The radius of the bounding sphere.

**OutOfBoundsMode:** Defines what happens when a particle leaves the sphere.

* **Kill:** Particles outside the sphere are destroyed immediately.
* **Constrain:** Particles outside the sphere are pushed back to the sphere's surface.

## See Also

* [Bounds Behavior](pb-bounds.md)
* [Particle Behaviors](../particle-behaviors.md)
* [Particle Effects](../particle-effects-overview.md)
* [Particle Initializers](../particle-initializers.md)
* [Particle Renderers](../particle-renderers.md)
