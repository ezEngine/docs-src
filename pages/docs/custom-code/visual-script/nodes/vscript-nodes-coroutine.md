# Visual Script: Coroutine Nodes

## Coroutine

[Coroutines](../visual-script-class-asset.md#coroutines) allow you to pause script execution at any point and resume it later, enabling complex temporal behaviors without blocking the entire script. This is particularly useful for sequencing AI tasks, quest objectives, or any operations that need to wait for conditions or time to pass.

Common coroutine operations include:

* **Starting and stopping coroutines** - Launch new execution threads or cancel existing ones
* **Waiting** - Pause execution for a specified duration
* **Yielding** - Pause until the next frame
* **Coroutine management** - Track and control multiple concurrent execution paths

Each [entry point node](vscript-nodes-events.md) can be configured with a coroutine mode (Stop Other, Don't Create New, or Allow Overlap) to control how multiple coroutines interact. See the [coroutines documentation](../visual-script-class-asset.md#coroutines) for detailed information on coroutine modes and advanced features.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Event Handler Nodes](vscript-nodes-events.md)
