# Particle Initializers

This page lists and describes all *particle initializers*.

## Box Position Initializer

Initializes a particle's position to a random point within a box shape.

**PositionOffset, Size:** These values define the size and position of the box, relative to the origin of the particle system. With a position offset of `(0, 0, 0)`, the box will be centered around the system's origin.

**ScaleXParam, ScaleYParam, ScaleZParam:** Optional names of [effect parameters](particle-effects-overview.md#effect-parameters). This allows to scale the volume in which particles spawn.

**Note:** Scaling the volume will change particle density. To compensate, the particle system will automatically spawn more or fewer particles. Thus you can author an effect as a 1x1x0 meter sized patch and then let the user decide how large a patch she needs by exposing these parameters. If your 1x1x0 patch requires roughly 100 particles at all times, then scaling it to a 10x5x0 patch will require 5000 particles.

<video src="media/box-position-init.webm" width="500" height="500" autoplay loop></video>

## Cylinder Position Initializer

Initializes a particle's position to a random point either within a cylinder or on its surface. A cylinder of height `0` initializes the position to a random point on a circle or its circumference.

**PositionOffset, Radius, Height:** These values define the size and position of the cylinder, relative to the origin of the particle system. With a position offset of `(0, 0, 0)`, the cylinder will be centered around the system's origin. A height of `0` turns the cylinder into a circle.

**OnSurface:** If enabled, particles will only spawn on the surface of the cylinder, not inside it. This also excludes the caps. For a cylinder of height `0` that means the particles will spawn on the circumference of a circle.

**SetVelocity, Speed:** If enabled, the initializer will additionally set the particle's starting velocity. The velocity is always outward from the cylinder's center line.

**ScaleRadiusParam, ScaleHeightParam:**

Optional names of [effect parameters](particle-effects-overview.md#effect-parameters). This allows to scale the volume in which particles spawn.

**Note:** Scaling the volume will change particle density. See the [box position initializer](#box-position-initializer) for details.

<video src="media/cylinder-position-init.webm" width="500" height="500" autoplay loop></video>

## Sphere Position Initializer

Initializes a particle's position to a random point within a sphere shape.

**PositionOffset, Radius:** These values define the size and position of the sphere, relative to the origin of the particle system. With a position offset of `(0, 0, 0)`, the sphere will be centered around the system's origin.

**OnSurface:** If enabled, particles will only spawn on the surface of the sphere, not inside it.

**SetVelocity, Speed:** If enabled, the initializer will additionally set the particle's starting velocity. The velocity is always outward from the sphere's center.

**ScaleRadiusParam:**

Optional name of an [effect parameter](particle-effects-overview.md#effect-parameters). This allows to scale the volume in which particles spawn.

**Note:** Scaling the volume will change particle density. See the [box position initializer](#box-position-initializer) for details.

<video src="media/sphere-position-init.webm" width="500" height="500" autoplay loop></video>

## Random Color Initializer

Initializes a particle's color to a random color.

**Gradient:** If specified, the random color will be picked from the given [color gradient](../../animation/common/color-gradients.md).

**Color1, Color2:** A random interpolated color between the two given colors is used. So if one color is white and the other is black, particles will get a random grey value as their color. If a *gradient* is set as well, the two colors are combined.

<video src="media/random-color-init.webm" width="500" height="500" autoplay loop></video>

## Random Size Initializer

Initializes a particle's size to a random value.

**Size:** The base size for the particles to start with. To initialize all particles to have a fixed size, set the variance to zero.

**SizeCurve:** If specified, the [curve](../../animation/common/curves.md) is sampled at a random location and the normalized value (always between `0` and `1`) is used to scale the randomly chosen base size. The shape of the curve has no meaning for this use case, it only provides a way to affect the distribution of the random sizes. For example, you could have a curve that sets exactly half of all particles to exactly a tenth of the base size. If you want exactly the same distribution as the curve has, you should set the variance of the *base size* to zero.

<video src="media/random-size-init.webm" width="500" height="500" autoplay loop></video>

## Rotation Speed Initializer

Initializes a particle's rotation and rotation speed to a random value.

**RandomStartAngle:** If enabled, the particle will start out with a random rotation. For particles with a distinct texture or shape, this can make the effect look significantly more natural.

**DegreesPerSecond:** If set to a non-zero value, particles will rotate with a constant speed. Each particle gets its own random speed assigned. With a low variance all particles will rotate similarly fast, with a high variance you will see some particles rotate very fast and some very slowly. Half of the particles rotate clockwise, the other half counter-clockwise.

<video src="media/rotation-speed-init.webm" width="500" height="500" autoplay loop></video>

## Velocity Cone Initializer

Initializes a particle's velocity to a random up vector.

**Angle:** The maximum opening angle of the upside down cone. With a small opening angle, particles will fly straight up. With a wide opening angle, particles will fly in all directions.

**Speed:** The initial speed for the particles.

<video src="media/velocity-cone-init.webm" width="500" height="500" autoplay loop></video>

## See Also


* [Particle Effects](particle-effects-overview.md)
* [Particle Behaviors](particle-behaviors.md)
* [Particle Renderers](particle-renderers.md)
