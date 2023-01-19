# Camera Shake Volume Components

*Camera shake volumes* are used to place regions in a scene where a player's camera should vibrate. This is used in conjunction with [camera shake components](camera-shake-component.md). The volumes have no effect on their own, instead the camera shake component will check whether it is inside such a volume, and apply its shake effect accordingly.

## Shared Component Properties

All camera shake volumes share these properties:

* `Strength`: How much shake to apply when the camera is at the strongest point inside the volume (for a sphere that would be right at the center). This is a factor between 0 and 1, scaling the camera shake between the `MinShake` and `MaxShake` value of the camera shake component.

* `BurstDuration`: If zero, the shake is indefinite. Otherwise it is active for only a limited duration. This would be used for effects like explosions that should only last a short time.

* `OnFinishedAction`: If used as a burst, the component or entire object may get deleted afterwards.

## Camera Shake Volume Sphere Component

This camera shake volume defines a spherical volume. The shake is strongest at its center and gradually fades out towards its edge.

### Sphere Component Properties

* `Radius`: The radius of the sphere volume. 

## See Also

* [Camera Shake Component](camera-shake-component.md)
