# Blackboard Nodes

The animation controller provides nodes to read and write values from and to a [blackboard](../../../Miscellaneous/blackboards.md). For this, the [game object](../../../runtime/world/game-objects.md) on which the [animation controller component](animation-controller-component.md) is attached, also needs to hold a blackboard component.

> **Note:**
> If no blackboad is available, these nodes will output a warning to the [log](../../../debugging/logging.md). If a blackboard is available, but the desired entry is not (yet) in the blackboard, they may add the entry or assume a default value of zero.

## Set Blackboard Value Node

When activated or deactivated, this node writes a given value to the blackboard.

### Node Properties

* **BlackboardEntry**: The name of the blackboard entry (variable) to write to.

* **SetOnActivation**: If true, `ActivationValue` will be written to the blackboard whenever the `Active` input pin changes from disabled to enabled.

* **ActivationValue**: The value that shall be written to the blackboard, when the `Active` pin becomes enabled.

* **SetOnDeactivation**: If true, `DeactivationValue` will be written to the blackboard whenever the `Active` input pin changes from enabled to disabled.

* **DeactivationValue**: The value that shall be written to the blackboard, when the `Active` pin becomes disabled.

### Input Pins

* **Active**: The *active* state determines when either the `ActivationValue` or `DeactivationValue` shall be written to the blackbard. As long as this pin's state doesn't change, no value is written.

## Check Blackboard Value Node

This node constantly monitors a blackboard value and compares it to a reference value. Whenever the comparison yields `true`, the `Active` output pin is enabled, otherwise disabled.

### Node Properties

* **BlackboardEntry**: The name of the blackboard entry (variable) to monitor.

* **ReferenceValue**: A reference value for the comparison.

* **Comparison**: The way the two values get compared.

### Output Pins

* **Active**: This output pin will be triggered whenever the comparison was successful.

## Get Blackboard Value Node

This node outputs the value of a specific blackboard entry. The number value can then be forwarded to other nodes.

### Node Properties

* **BlackboardEntry**: The name of the blackboard entry (variable) to read.

### Output Pins

* **Number**: The value of the blackboard entry. If the entry doesn't exist, the pin outputs zero.

## See Also

* [Animation Controller](animation-controller-overview.md)
* [Skeletal Animations](../skeletal-animation-overview.md)
