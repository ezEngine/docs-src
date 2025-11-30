# Visual Script: Clock and Time Nodes

## Clock

Clock nodes provide access to the engine's time systems. Understanding the difference between the two clocks is essential for proper script behavior:

* **Global Clock** - Advances in real-time, unaffected by game speed. Use this for:
  * UI animations
  * Real-time timers
  * Effects that should run at normal speed regardless of slow-motion
  * Frame-rate independent animations

* **World Clock** - Scales with game speed and can be paused or slowed down. Use this for:
  * Gameplay mechanics
  * AI behavior
  * Physics-driven animations
  * Anything that should respect slow-motion or game pauses

Choosing the correct clock is important: gameplay timers should use the world clock so they pause when the game pauses, while UI elements should typically use the global clock to remain responsive.

Clock nodes provide access to delta time (time since last frame), total elapsed time, and other timing information. Use these with [coroutine nodes](vscript-nodes-coroutine.md) to create time-based behaviors.

## Time

Time nodes operate on the *time* data type, allowing you to:

* **Convert time values** - Between different representations (seconds, milliseconds)
* **Compare times** - Check if enough time has passed
* **Calculate durations** - Measure elapsed time
* **Store timestamps** - Track when events occurred

Time values work together with clock nodes to create time-aware script logic.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Coroutine Nodes](vscript-nodes-coroutine.md)
