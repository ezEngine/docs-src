# Debug Nodes

These animation controller nodes can be used to find problems.

## Log Node

The *log node* simply prints a *dev* string to the [log](../../../debugging/logging.md) whenever it gets activated.

### Properties

* `Text`: The text to print. This may include placeholders for the input values. Use `{0}` to `{3}` to embed the values from `Input0` to `Input3` respectively. 

### Input Pins

* `Active`: Every frame in which this pin is triggered, the node will log `Text` as a *Dev* message to the [log](../../../debugging/logging.md).

* `Input0` to `Input3`: These pins allow you to pass in values that can be printed to the log.

## See Also


* [Animation Controller](animation-controller-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
