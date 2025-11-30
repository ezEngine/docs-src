# Visual Script: Logic Nodes

## Logic

Logic nodes provide flow control and conditional execution in visual scripts. This group contains boolean operators, conditions, loops, and comparison operations that form the foundation of script logic.

Essential logic nodes:

* `Branch`: An `if` condition node with two execution paths based on a boolean value
* `Switch`: Several variants to map one value to multiple possible execution paths
* `Compare`: Checks whether two values are equal, returning a boolean result
* `Is Valid`: Checks whether a value (such as a game object or component reference) is still valid and can be used

Additional logic operations include:

* **Boolean operators** - AND, OR, NOT for combining conditions
* **Loops** - For, while, and foreach loops for iteration (see [loops and arrays](../visual-script-class-asset.md#loops-and-arrays))
* **Numeric comparisons** - Greater than, less than, etc.
* **Null checks** - Verify references before use

Logic nodes control the flow of script execution and are used in nearly every visual script. Combine them with [math nodes](vscript-nodes-math.md) for numerical logic and [string nodes](vscript-nodes-string.md) for text comparisons.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Loops and Arrays](../visual-script-class-asset.md#loops-and-arrays)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Math Nodes](vscript-nodes-math.md)
* [Enum Nodes](vscript-nodes-enum.md)
