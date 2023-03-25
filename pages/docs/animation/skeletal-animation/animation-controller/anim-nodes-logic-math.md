# Logic and Math Nodes

The animation controller provides a couple of nodes to evaluate basic arithmatic and logic. This is meant for very simple use cases and for quick prototyping. Often animation logic requires much more complex rules than what would be feasible to express in the animation controller graph. Instead use [custom code](../../../custom-code/custom-code-overview.md) to decide which animation should run under which circumstances, and pass the result to the animation controller via a [blackboard](../../../Miscellaneous/blackboards.md). The animation controller can then simply read the state for each animation using the [blackboard nodes](anim-nodes-blackboard.md).

## Logic AND Node

This node sets its output pin to *triggered* when **all** incoming connections on the input pin are triggered at the same time. Note that even though there is only a single input pin, it can be connected to multiple sources.

### Node Properties

* **NegateResult**: If set, the output value will be negated. This effectively turns it into a `NAND` logic node.

## Logic OR Node

This node sets its output pin to *triggered* when **any** incoming connections on the input pin are triggered. Note that even though there is only a single input pin, it can be connected to multiple sources.

### Node Properties

* **NegateResult**: If set, the output value will be negated. This effectively turns it into a `NOR` logic node.

## Logic NOT Node

This node sets its output pin to *triggered* when the input pin is not triggered and vice versa.

As with the other nodes, you can connect multiple sources to this input pin. In this case, if any of those connections is triggered, the entire input pin is considered to be in the triggered state, and the output will be the opposite.

## Compare Value Node

This node can be used to check whether a number value compares in a certain way against a reference value. For example whether some input value is larger than 0.5. If this is the case, the output pin will be triggered.

### Node Properties

* **ReferenceValue**: The reference value to compare the incoming value against.
* **Comparison**: The mathematical operation with which to compare the two values.

### Input Pins

* **Number**: The number to compare against the reference value.

### Output Pins

* **Active**: The output pin is triggered whenever the comparison is successful.

## Math Expression Node

The math expression node takes up to four different numbers as its input, plugs them into a user provided expression and outputs the result.

The expression must be syntactically correct, otherwise the node prints an error to the [log](../../../debugging/logging.md).

### Node Properties

**Expression**: The expression can use the following:

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

* **a**, **b**, **c** and **d**: Input values to the mathematical expression. Unconnected pins are treated as having the value zero.

### Output Pins

* **Result**: Outputs the result of the evaluated expression.

## See Also


* [Animation Controller](animation-controller-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
