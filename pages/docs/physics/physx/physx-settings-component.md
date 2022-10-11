# PhysX Settings Component

The *PhysX settings component* is used to configure general PhysX simulation options. You can only have one such component in a scene, it is an error to have two or more. If no such component is present, all PhysX settings use default values.

## Component Properties

* `ObjectGravity`: The gravity that is applied to all [dynamic actors](actors/physx-dynamic-actor-component.md). This property sets both the direction and strength of the gravity.

* `CharacterGravity`: A separate gravity value that is used for [characters controllers](special/physx-character-controller.md). In many games the gravity for characters is higher than what's used for regular objects.

* `MaxDepenetrationVelocity`: The maximum speed with which PhysX may separate objects that managed to penetrate each other.

* `SteppingMode`: The stepping mode determines with what time steps PhysX is updated. This is most relevant when your game doesn't run at a fixed framerate:

  * `Variable`: PhysX will be stepped every frame with the time delta from the previous frame. This mode will forward any frame rate variations to PhysX unfiltered, which means the time step can vary drastically. This mode has the least overhead, but can also result in an unstable simulation when the framerate varies too much. If your game doesn't use dynamic actors much and you mainly use it for raycasts, character movement and overlap queries, this can be entirely sufficient.

  * `Fixed`: In this mode PhysX is always stepped with the time delta for the `FixedFrameRate`. If too little time has passed between frames, the PhysX update is skipped entirely, once the delta has been reached, PhysX is stepped. If the time between two frames is very long, up to `MaxSubSteps` are done to update PhysX. This mode is the most reliable, producing the most stable and deterministic results, since a variable framerate doesn't introduce any variation in how PhysX is updated.
  
    This mode is most suitable when your game runs at a locked framerate.

    This mode can be problematic, if you do have a variable framerate, especially when a frame can take a very long time. In that case the physics simulation will do up to `MaxSubSteps` simulation steps to catch up with the passed time. If that is not sufficient, the PhysX update will continue catching up during the next frame. As a result, the speed at which simulated objects move may appear erratic until the simulation has fully caught up with the passed time.

  * `SemiFixed`: This mode is a compromise between `Variable` and `Fixed`. It prefers to use fixed time steps, to achieve good simulation stability. At high framerates it will do shorter update steps, but may also skip the PhysX update until enough time has passed. At low framerates, it will do up to `MaxSubSteps` per frame, but it will use those to always fully catch up with the time that passed between the frames.

* `FixedFrameRate`: The framerate to use for the 'fixed' timesteps. A higher framerate means the simulation will be more stable, but also cost more update steps and therefore performance.

* `MaxSubSteps`: The maximum number of simulation steps to do between to frames. This is to introduce an upper bound on the performance cost of the PhysX update during one frame.

## See Also


* [PhysX Integration](physx-overview.md)
