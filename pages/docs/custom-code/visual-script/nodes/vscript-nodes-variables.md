# Visual Script: Type Conversion and Variable Nodes

## Type Conversion

Type conversion nodes allow you to convert data between different types in visual scripts. These conversions are essential when working with different data types and connecting nodes with mismatched pin types.

The most important conversion node is `ConvertTo`, which converts a *Variant* to a specific type. A *Variant* is a special variable type that can hold data of many different types. When a node returns a variant, you typically know what type it should contain and use the `ConvertTo` node to extract the typed value.

Common type conversions include:

* **Number conversions** - Converting between integers, floats, and doubles
* **String conversions** - Converting any value to text for display or logging
* **Variant conversions** - Extracting typed values from variant containers
* **Boolean conversions** - Converting values to true/false

## Variable Nodes

Variable nodes operate on [visual script variables](../visual-script-class-asset.md#visual-script-variables). Variables must be declared on the script first through the script properties panel. Use variable nodes to:

* **Read variables** - Get the current value of a script variable
* **Write variables** - Update a variable's value during script execution
* **Track state** - Maintain internal state across multiple script executions
* **Access parameters** - Read values passed in through [exposed parameters](../../concepts/exposed-parameters.md)

### Temp Variable Node

The **Temp Variable** node is a special node for storing intermediate computation results. Unlike regular variables, temp variables have execution pins, allowing you to control exactly when their input is evaluated.

This is useful for two reasons:

1. **Performance** - Reuse computed values multiple times without reevaluating expensive expressions
2. **Consistency** - Guarantee the same value even if underlying data changes. For example, if an expression reads variable `A`, but the script later writes to `A`, the temp variable preserves the original value from when it was first evaluated.

The temp variable's output can be read as often as needed and won't change until the node is executed again.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Variables](../visual-script-class-asset.md#visual-script-variables)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Exposed Parameters](../../concepts/exposed-parameters.md)
* [String Nodes](vscript-nodes-string.md)
