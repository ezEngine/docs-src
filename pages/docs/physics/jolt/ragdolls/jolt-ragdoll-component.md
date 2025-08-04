# Jolt Ragdoll Component

The *Jolt ragdoll component* is used to physically simulate limp bodies.

<video src="media/ragdolls.webm" width="800" height="600" autoplay loop></video>

## Ragdoll Configuration

Ragdolls only work with [skeletons](../../../animation/skeletal-animation/skeleton-asset.md) that have a proper bone collider and joint setup. The most important bones need to have *collider shapes*. Additionally, bones that should be anatomically connected, need to have *joints* set up. Bones also must adhere to a physically plausible hierarchy, meaning that leg bones should be child bones of a hip bone, feet bones must be child bones of leg bones and so on. Unfortunately many assets don't strictly follow this rule, which often makes them unsuitable for use as a ragdoll.

The ragdoll component works with *uniform scaling*, so you can create differently sized characters or objects. It does *not* work with non-uniform scaling.

It is common to add a ragdoll component to a character, but set the component to *inactive*, and only activate the component when the character goes limp.  

## Breakable Objects

The ragdoll component can be used for a simple breaking effect. For this you need to build a mesh out of broken pieces and give each piece a bone. In the rest pose the mesh should look like one piece. Now you can use a [visual script](../../../custom-code/visual-script/visual-script-overview.md) to determine under what conditions the object should shatter and then activate the ragdoll component. In this case the skeleton only needs to define shapes for the bones, but no joints between them. Thus each fragment will fall individually and the object looks like it breaks apart.

Use the properties `CenterPosition`, `CenterVelocity` and `CenterAngularVelocity` to make the pieces fly away more convincingly.

> **Important**
>
> This feature is only experimental and very limited in functionality.

<video src="media/breakable.webm" width="800" height="600" autoplay loop></video>

## Ragdoll Simulation

Once a ragdoll component is switched to *active*, it takes over the *pose generation* for the [animated mesh](../../../animation/skeletal-animation/animated-mesh-component.md). It will also take over the positioning of the *owner game object*. That means that the owner position will be moved to the position of the top-most simulated joint of the ragdoll (the first one that has a collider). So the owner position might be at a character's feet before the ragdoll takes over, but then get moved to the hips once the ragdoll activates.

### Animated Ragdolls

If the `AnimMode` property is set to *Powered* or *Controlled* and an [animation graph](../../../animation/skeletal-animation/animation-graphs/animation-graph-overview.md) is active that provides a pose, the ragdoll will use that pose to influence the ragdoll simulation.

In the *powered* mode, the ragdoll is still physically simulated like normal, but the joints act like muscles, moving the ragdoll towards the desired pose. This is typically used to play a death animation, and have the character continue to move a little before it finally goes limp.

In the *controlled* mode, the ragdoll is fully moved by the animation, include position changes that can let the ragdoll walk around or jump. It isn't really physically simulated, only small overlaps with other geometry can be avoided, but they usually produce jittering.

This mode is mainly meant to control the ragdoll for a very short time (less than a second) and then switch to the powered or limp mode, so that a death animation can start off more dramatically. This will also give each bone some motion, which will then be continue by the physics simulation.

Use [animation events](../../../animation/skeletal-animation/animation-events.md) to mark up a death animation, where it should switch to *controlled*, *powered* or *limp* mode, and use a script to forward this setting to the ragdoll component.

In *powered* mode, you can also call `FadeJointMotorStrength()` to have the strength of the muscles fade over a short time. This does allow to also fade the strength back in, as the ragdoll stays in the powered mode, and the animation provider will stay active and will continue to provide animation poses. To fully switch of animation generation, switch the ragdoll to *limp* mode at the end of a death animation.

## Component Properties

* `SelfCollision`: Whether the individual bones of a ragdoll shall collide with each other. If disabled, they will pass through each other and only the joint constraints will prevent unnatural motion. Wether self collision works well or not on a given character highly depends on how the colliders for the bones are set up.
* `StartMode`: In which *pose* the ragdall should start:
  * `WithBindPose`: The ragdoll starts immediately and uses the default bind pose (or rest pose) of the skeleton.
  * `WithNextAnimPose`: The ragdoll waits for the next animation pose from and then starts from there. This requires a [simple animation component](../../../animation/skeletal-animation/simple-animation-component.md) or [animation graph](../../../animation/skeletal-animation/animation-graphs/animation-graph-overview.md) to be active.
  * `WithCurrentMeshPose`: The ragdoll starts immediately with the current pose. This does not require another component to regularly provide new poses and thus can also be used with a [skeleton pose component](../../../animation/skeletal-animation/skeleton-pose-component.md).
* `AnimMode`: What to do, in case an animation pose is provided during ragdoll simulation, by an [animation controller component](../../../animation/skeletal-animation/animation-graphs/animation-controller-component.md).
  * `Limp`: The ragdoll ignores the animation. It also instructs the animation provider to deactivate itself, to not waste performance.
  * `Powered`: The ragdoll joints attempt to rotate towards the desired animation target, however, the ragdoll is still fully physically simulated and will fall, push against objects and be limited by walls etc.
  * `Controlled`: The entire ragdoll is controlled by the animation, like a puppet. It will follow the animation nearly perfectly, including position changes (ie it can jump etc). Physical simulation does happen, but will only prevent minor penetration issues.
* `GravityFactor`: How much gravity to use.
* `WeightCategory`, `WeightScale`: How heavy the ragdoll should be. See [weights and forces](../concepts/weights-forces.md) for details.
* `StiffnessFactor`: The overall stiffness of the joints. Each joint has an individual stiffness as defined in the [skeleton asset](../../../animation/skeletal-animation/skeleton-asset.md), but when scaling characters up or down, it may be necessary to also scale the stiffness.
* `OwnerVelocityScale`: A ragdoll may get enabled while a character is moving, for example while it is running. The owner object velocity is then transferred to the ragdoll to have it continue falling into the direction, rather then suddenly stop and just fall down. This factor allows to tweak how much of that momentum to keep (or even exaggerate).
* `CenterPosition`: An experimental feature mainly meant for breakable objects (ragdolls with no joints). Specifies an offset where the *center* of the object should be, to apply an outwards force from. 
* `CenterVelocity`, `CenterAngularVelocity`: What linear and angular velocity to set at start outwards from the `CenterPosition` on each bone. This makes it possible to build *breakable* objects that break apart when the ragdall gets activated.

## Script Functions

* `SetInitialImpulse`, `AddInitialImpulse`: Should be called before activating the ragdoll component. Will apply an impulse to the ragdoll at the provided position, when it starts simulating.
* `SetJointTypeOverride`: Call this before activating the ragdoll. Makes it possible to override the type of a joint in ragdoll, so that it can be either stiff or break off.
* `SetJointMotorStrength`: Changes the overall strength of the joint motors ("muscles") in an animation powered ragdoll.
* `FadeJointMotorStrength`: Fades the motor ("muscle") strength of an animation powered ragdoll to a target value. Typically used to fade out the animation contribution.

## See Also

* [Skeletal Animations](../../../animation/skeletal-animation/skeletal-animation-overview.md)
* [Jolt Hitbox Component](jolt-hitbox-component.md)
* [Skeleton Asset](../../../animation/skeletal-animation/skeleton-asset.md)
* [Weights and Forces](../concepts/weights-forces.md)
