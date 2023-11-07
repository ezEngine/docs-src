# Debug Nodes

These animation graph nodes are used to find problems.

## Log Nodes

The `Log Info` and `Log Error` nodes print a string to the [log](../../../debugging/logging.md) whenever they get activated.

### Node Properties

* `Text`: The text to print. This may include placeholders for the input values. Use `{0}`, `{1}`, `{2}`, etc to embed the value from the respective `Numbers[]` pin.

* `Number Count`: Specifies how many number input pins the node should have.

### Input Pins

* `Activate`: Every frame in which this pin gets triggered, the node will log `Text` to the [log](../../../debugging/logging.md).

* `Numbers[]`: These pins allow you to pass in number values for embedding in the output text.

## See Also

* [Animation Graph](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
