# Jolt Physics Settings Component

The *Jolt physics settings component* is used to configure general Jolt simulation options. You can only have one such component in a scene, it is an error to have two or more. If no such component is present, all Jolt settings use default values.

## Component Properties

* `ObjectGravity`: The gravity that is applied to all [dynamic actors](actors/jolt-dynamic-actor-component.md). This property sets both the direction and strength of the gravity.

* `CharacterGravity`: A separate gravity value that is used for [characters controllers](special/jolt-character-controller.md). In many games the gravity for characters is higher than what's used for regular objects.

* `SteppingMode`: The stepping mode determines with what time steps Jolt is updated. This is most relevant when your game doesn't run at a fixed framerate:

  * `Variable`: Jolt will be stepped every frame with the time delta from the previous frame. This mode will forward any frame rate variations to Jolt unfiltered, which means the time step can vary drastically. This mode has the least overhead, but can also result in an unstable simulation when the framerate varies too much. If your game doesn't use dynamic actors much and you mainly use it for raycasts, character movement and overlap queries, this can be entirely sufficient.

  * `Fixed`: In this mode Jolt is always stepped with the time delta for the `FixedFrameRate`. If too little time has passed between frames, the Jolt update is skipped entirely, once the delta has been reached, Jolt is stepped. If the time between two frames is very long, up to `MaxSubSteps` are done to update Jolt. This mode is the most reliable, producing the most stable and deterministic results, since a variable framerate doesn't introduce any variation in how Jolt is updated.
  
    This mode is most suitable when your game runs at a locked framerate.

    This mode can be problematic, if you do have a variable framerate, especially when a frame can take a very long time. In that case the physics simulation will do up to `MaxSubSteps` simulation steps to catch up with the passed time. If that is not sufficient, the Jolt update will continue catching up during the next frame. As a result, the speed at which simulated objects move may appear erratic until the simulation has fully caught up with the passed time.

  * `SemiFixed`: This mode is a compromise between `Variable` and `Fixed`. It prefers to use fixed time steps, to achieve good simulation stability. At high framerates it will do shorter update steps, but may also skip the Jolt update until enough time has passed. At low framerates, it will do up to `MaxSubSteps` per frame, but it will use those to always fully catch up with the time that passed between the frames.

* `FixedFrameRate`: The framerate to use for the 'fixed' timesteps. A higher framerate means the simulation will be more stable, but also cost more update steps and therefore performance.

* `MaxSubSteps`: The maximum number of simulation steps to do between two frames. This is to introduce an upper bound on the performance cost of the Jolt update during one frame.

* `MaxBodies`: For performance reasons, Jolt pre-allocates certain resources once at startup. Therefore you can't have more active bodies than this. The default value should be sufficient for the vast majority of use cases, but if necessary, you can increase the value here.

## See Also

* [Jolt Integration](jolt-overview.md)
