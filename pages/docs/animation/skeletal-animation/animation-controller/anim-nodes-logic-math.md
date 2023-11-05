# Logic and Math Nodes

The animation graph provides nodes to evaluate basic arithmatic and logic. This is meant for very simple use cases and for quick prototyping. Often animation logic requires much more complex rules than what would be feasible to express in the animation graph. Instead use [custom code](../../../custom-code/custom-code-overview.md) to decide which animation should run under which circumstances, and pass the result to the animation graph via a [blackboard](../../../Miscellaneous/blackboards.md). The animation graph can then simply read the state for each animation using the [blackboard nodes](anim-nodes-blackboard.md).

## AND Node

This node checks whether **all** boolean input values are `true` and sets its own `Is True` and `Is False` output pins accordingly.

### Node Properties

* `Bool Count`: How many input pins the node should have.

## OR Node

This node checks whether **any** boolean input value is `true` and sets its own `Is True` and `Is False` output pins accordingly.

### Node Properties

* `Bool Count`: How many input pins the node should have.

## NOT Node

Outputs the oppositve value of its input.

## Compare Number Node

This node can be used to check whether a number value compares in a certain way against a reference value. For example whether some input value is larger than 0.5.

### Node Properties

* `Reference Value`: The reference value to compare the incoming value against.
* `Comparison`: The mathematical operation with which to compare the two values.

### Input Pins

* `Number`: The number to compare against the reference value.
* `Reference`: If connected, this acts as the reference value.

### Output Pins

* `Is True`: A boolean output for the result of the comparison.


## Bool To Number Node

Converts a boolean value (`true` or `false`) to a number. By default this node converts `false` to `0` and `true` to `1`, but you can select other numerical values to use.

### Node Properties

* `False Value`, `True Value`: The *number value* to output for when the input is `false` or `true`.

## Event AND Node

Used to filter an event pin to only activate the next node, if additionally to the event another condition is met at the same time.

Event pins are triggered only infrequently. For example a button press may result in an event pin being triggered. However, you often don't want that event to immediately have an effect, because often the currently playing animations don't allow this. So you may have additional state keeping track of whether some reaction would be possible.

The *Event AND* node makes it easy to listen to an event pin and forward the event only if another condition is also true.

### Input Pins

* `Activate`: An event pin that will trigger the evaluation.
* `Bool`: A condition that must be true for the output pin to get triggered. As long as this is `false` all activations are ignored.

### Output Pins

* `On Activated`: If both the `Activate` and `Bool` input pins are true at the same time, this pin gets activated for one frame.

## Expression Node

The expression node takes up to four different numbers as its input, plugs them into a user provided expression and outputs the result.

The expression must be syntactically correct, otherwise the node prints an error to the [log](../../../debugging/logging.md).

### Node Properties

`Expression`: The expression can use the following:

* Numbers in floating point format (e.g. `1`, `2.3`, `-78`)
* `+`, `-`, `*`, `/`, `%` (modulo)
* Parenthesis `(` and `)` to specify precedence
* The variables `a`, `b`, `c` and `d` representing the input pin values
* The functions `abs` and `sqrt`

**Examples:**

* `a * 0.5 - b`
* `abs(a) + abs(b)`
* `(a + 1) % 2`

### Input Pins

* `a`, `b`, `c` and `d`: Input values to the mathematical expression. Unconnected pins are treated as having the value zero.

### Output Pins

* `Result`: Outputs the result of the evaluated expression.

## See Also

* [Animation Graph (TODO)](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
