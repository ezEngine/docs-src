# Visual Script: Logging Nodes

## Log

Logging nodes output messages to the [engine's log system](../../debugging/logging.md), allowing you to track script execution, debug issues, and monitor runtime behavior. These nodes are essential for understanding what your scripts are doing and troubleshooting problems.

Logging features:

* **Formatted messages** - Create log messages with variable substitution using format strings
* **Multiple inputs** - Add any number of input values to include in the log message
* **Format syntax** - Reference input values using `{0}`, `{1}`, `{2}` and so on in your format string
* **Log levels** - Output at different severity levels (info, warning, error)

Example: A log message with format string `"Player health: {0}, position: {1}"` with two inputs will substitute the values into the message.

## See Also

* [Visual Script Class Asset](../visual-script-class-asset.md)
* [Visual Script Overview](../visual-script-overview.md)
* [Script Component](../script-component.md)
* [Logging](../../debugging/logging.md)
* [Debug Nodes](vscript-nodes-debug.md)
* [String Nodes](vscript-nodes-string.md)
