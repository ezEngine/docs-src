# Blackboard Nodes

The animation graph provides nodes to read and write values from and to a [blackboard](../../../misc/blackboards.md). For this, the [game object](../../../runtime/world/game-objects.md) on which the [animation controller component](animation-controller-component.md) is attached, or one of its parent nodes, also needs to hold a [blackboard component](../../../misc/local-blackboard-component.md).

> **Note:**
>
> If no blackboad is available, these nodes will typically silently not do anything. If a blackboard is available, but the desired entry is not (yet) in the blackboard, they may add the entry or log a warning and assume a default value.

## Set Number Node / Set Bool Node

When activated, this node writes a given value to the blackboard. If the activation pin is not connected, at all, the node updates the blackboard with the incoming number every update.

### Node Properties

* `Blackboard Entry`: The name of the blackboard entry (variable) to write to.

* `Number` / `Bool`: The value to write in case the value input pin is connected.

### Input Pins

* `Activate`: When triggered, the node changes the blackboard value.

* `Number` / `Bool`: The value to write. If not connected, the value configured on the node is used.

## Get Number Node / Get Bool Node

Outputs the value of a specific blackboard entry.

### Node Properties

* `Blackboard Entry`: The name of the blackboard entry (variable) to read.

### Output Pins

* `Number` / `Bool`: The value of the entry. If the entry doesn't exist, the pin outputs zero.

## Check Number Node

This node monitors a blackboard value and compares it to a reference value. When the result of the comparison changes, the `On True` or `On False` output pin gets triggered for one frame. 

### Node Properties

* `Blackboard Entry`: The name of the blackboard entry (variable) to monitor.

* `Reference Value`: A reference value for the comparison.

* `Comparison`: The way the two values get compared.

### Output Pins

* `On True`: Gets triggered for one frame when the comparison result changes to `true`.
* `On False`: Gets triggered for one frame when the comparison result changes to `false`.
* `Is True`: Outputs the result of the comparison. This is a data pin that can always be read, contrary to the other two pins that are *event pins* and only get triggered when something changes.
* `Is False`: Outputs the opposite value of `Is True`.

## Check Bool Node

This node monitors a boolean blackboard value and compares it to `true`. When the result of the comparison changes, the `On True` or `On False` output pin gets triggered for one frame. 

### Node Properties

* `Blackboard Entry`: The name of the blackboard entry (variable) to monitor.

### Output Pins

* `On True`: Gets triggered for one frame when the value changes to `true`.
* `On False`: Gets triggered for one frame when the value changes to `false`.
* `Bool`: Outputs the blackboard value. This is a data pin that can always be read, contrary to the other two pins that are *event pins* and only get triggered when the value changes.

## OnChanged Node

This node monitors a blackboard value and triggers its output event node when the value changes. This should be used when *any* change to a variable is of interest.

### Node Properties

* `Blackboard Entry`: The name of the blackboard entry (variable) to monitor.

### Output Pins

* `On Value Changed`: Gets triggered for one frame when the value changes somehow.

## See Also

* [Animation Graph](animation-graph-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
