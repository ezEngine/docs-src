# MiniDump Tool

The MiniDumpTool writes a mini-dump (memory, call-stacks) of an application. The mini dump can be used for diagnosing why an application crashed. The tool is used by the [unit tests](unit-tests.md).

## Arguments

The tool takes exactly two arguments:

```cmd
MiniDumpTool -PID 1234 -f "C:/crashdumps/justnow.dmp"
```

The first argument is the *Process ID* of the process for which the memory shall be dumped, the second argument specifies the file where the dump should be written to.

## Automatic Execution

You can integrate writing crash dumps into your application by setting the `ezCrashHandler_WriteMiniDump` through `ezCrashHandler::SetCrashHandler()`.

`ezCrashHandler_WriteMiniDump` has options to generate the filename automatically using the current date and time.

## See Also


* [Unit Tests](unit-tests.md)
