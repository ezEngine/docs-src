# Logging

Log messages are often very helpful in finding problems.

## Logging Information

The log is accessible through the `ezLog` class. There are multiple functions to log information of different severity:

* `ezLog::Debug` - for verbose output, will be compiled out in non-debug builds
* `ezLog::Dev` - for output during development, will typically be silenced (but not compiled out) in non-development builds
* `ezLog::Info` - for regular information
* `ezLog::Warning` - for important information that may point at problems
* `ezLog::SeriousWarning` - for problems that should be fixed but won't crash the system just now
* `ezLog::Error` - for errors

Log messages can be *grouped* using the `EZ_LOG_BLOCK` macro.

## Inspecting the Log

There are multiple ways to see the content of the log:

* In the ezEditor you can open *Panels > Log*. Note that the editor consists of [multiple processes](../editor/editor-plugins.md) and the log panel shows the logs of two of those processes combined, which may result in unexpected output. If you want to see the logs separately, open the [preferences](../editor/editor-settings.md) and uncheck `Application: General > Combined Editor and Engine Logs`.
* [ezInspector](../tools/inspector.md) shows the log of the connected process.
* The in-game [console](console.md) outputs the log messages.
* By default all EZ [applications](../runtime/application/application.md) also write the log output to a `Log.htm` file in the application's *appdata* folder.

## Thread-local logging

The logging system uses a thread-local variable to store the *active* logging system, through which to route all messages that originate on that thread. This can be used to easily replace the entire logging backend on a thread and capture all log messages in a custom backend. See `ezLogSystemScope` and `ezLogInterface`, if you want to write a custom backend. This can be used to, for example, capture all output from some subsystem and prevent the messages from reaching the regular outputs.

## Custom Log Writers

`ezLog` is the central class for all messages to be logged. By default, it routes all messages through an instance of `ezGlobalLog`, though you can redirect this on the calling side if you want. On `ezGlobalLog` you can register multiple handlers that take the messages and either write them to some output or forward them to another system. This method is used to, for instance, forward log messages from one process to another. The [ezInspector](../tools/inspector.md) integration, for example, registers a custom log writer to gather all log messages, and send them over the network, for display in the external tool. ezEditor does something similar for the messages from the engine process.

For an in-depth explanation of how you can configure the system, see `ezLog` and `ezGlobalLog`.

## See Also


* [ezInspector](../tools/inspector.md)
* [Console](console.md)