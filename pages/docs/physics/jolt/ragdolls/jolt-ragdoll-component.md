# Jolt Ragdoll Component

> **Note**
>
> Ragdolls are a work-in-progress feature. They are working, but the exact functionality may change in the future.

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

## Component Properties

* `SelfCollision`: Whether the individual bones of a ragdoll shall collide with each other. If disabled, they will pass through each other and only the joint constraints will prevent unnatural motion. Wether self collision works well or not on a given character highly depends on how the colliders for the bones are set up.
* `StartMode`: In which *pose* the ragdall should start:
    * `WithBindPose`: The ragdoll starts immediately and uses the default bind pose (or rest pose) of the skeleton.
    * `WithNextAnimPose`: The ragdoll waits for the next animation pose from and then starts from there. This requires a [simple animation component](../../../animation/skeletal-animation/simple-animation-component.md) or [animation graph](../../../animation/skeletal-animation/animation-controller/animation-graph-overview.md) to be active.
    * `WithCurrentMeshPose`: The ragdoll starts immediately with the current pose. This does not require another component to regularly provide new poses and thus can also be used with a [skeleton pose component](../../../animation/skeletal-animation/skeleton-pose-component.md).
* `GravityFactor`: How much gravity to use.
* `Mass`: How heavy the ragdoll should be.
* `StiffnessFactor`: The overall stiffness of the joints. Each joint has an individual stiffness as defined in the [skeleton asset](../../../animation/skeletal-animation/skeleton-asset.md), but when scaling characters up or down, it may be necessary to also scale the stiffness.
* `OwnerVelocityScale`: A ragdoll may get enabled while a character is moving, for example while it is running. The owner object velocity is then transferred to the ragdoll to have it continue falling into the direction, rather then suddenly stop and just fall down. This factor allows to tweak how much of that momentum to keep (or even exaggerate).
* `CenterPosition`: An experimental feature mainly meant for breakable objects (ragdolls with no joints). Specifies an offset where the *center* of the object should be, to apply an outwards force from. 
* `CenterVelocity`, `CenterAngularVelocity`: What linear and angular velocity to set at start outwards from the `CenterPosition` on each bone. This makes it possible to build *breakable* objects that break apart when the ragdall gets activated.

## See Also

* [Skeletal Animations](../../../animation/skeletal-animation/skeletal-animation-overview.md)
* [Jolt Hitbox Component](jolt-hitbox-component.md)
* [Skeleton Asset](../../../animation/skeletal-animation/skeleton-asset.md)
