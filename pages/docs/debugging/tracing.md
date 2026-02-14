# Tracing

ezEngine provides a cross-platform tracing system that emits structured events to the operating system's tracing infrastructure. Tracing is different from [profiling](../performance/profiling.md) and [logging](../performance/logging.md) as it allows for different debugging aproaches:
1. Unlike [profiling](../performance/profiling.md), which stores data in an in-process ring buffer, tracing sends events to an external OS-level backend for capture by dedicated tools. This enables correlation with e.g.kernel events (scheduling, I/O).
1. Traces are system wide so you can capture events from multiple threads / processes, even those you don't own.
1. You can attach data fields to a trace event which are structured, allowing tools to aggregate or filter by them.
1. Each trace event stores process and thread information, allowing to filter by various dimensions unlike [logging](../performance/logging.md) which is always linear.

When you should not use tracing:
1. If you need instant feedback in the debugger, use [logging](../performance/logging.md) instead.
1. If you want to do performance profiling on CPU / GPU, use [profiling](../performance/profiling.md) for capturing or [tracy](../performance/profiling.md) for real-time observation instead.


The tracing system uses:

* **ETW** (Event Tracing for Windows) via TraceLogging on Windows.
* **LTTNG-UST** (Linux Trace Toolkit Next Generation) on Linux.
* **Perfetto SDK** on Android.
* No-op stubs on all other platforms

Tracing is controlled by the `EZ_USE_TRACING` compile-time toggle (see `UserConfig.h`). When disabled, all macros expand to nothing with zero overhead. It is enabled by default in non-shipping builds.

## Trace Providers

Each library or executable that emits trace events needs its own *provider*. Create two files in a `Tracing/` subfolder of your library:
1. `TraceProvider.h`:

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-provider-header -->
```cpp
EZ_DECLARE_TRACE_PROVIDER(g_ezTrace_FoundationTest);

/// All EZ_TRACE_* macros in FoundationTest source files use this provider.
#define EZ_TRACE_PROVIDER g_ezTrace_FoundationTest
```
<!-- END-DOCS-CODE-SNIPPET -->
2. `TraceProvider.cpp`:
<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-provider-cpp -->
```cpp
EZ_IMPLEMENT_TRACE_PROVIDER(g_ezTrace_FoundationTest, "ez_FoundationTest");
```
<!-- END-DOCS-CODE-SNIPPET -->

### Important Rules

* **Never include `Tracing.h` directly outside of the provider setup.** Source files that emit trace events should include the provider header `TraceProvider.h` of their respective library.
* **Only include the provider header in `.cpp` files.** Never include tracing headers from another header. Each trace macro instantiation must exist exactly once or linker errors will occur.
* **Events with different schemas must have different names.** If two events share a name but have different fields (different number or types of `EZ_TRACE_VALUE` arguments), Linux traces will be corrupted. The exception is begin/end macro pairs, which must share a name — the backend renames them internally when needed.
* **Do not include `TraceProvider.h` from other libraries.** If you need to emit events from the provider of a different library, wrap these events into functions and export them.

## Emitting Events

All events need a name and take an `ezTraceLevel::Enum` that maps to the platform's native severity levels:

* `ezTraceLevel::Error`: serious failure.
* `ezTraceLevel::Warning`: potential problem.
* `ezTraceLevel::Info`: informational.
* `ezTraceLevel::Verbose`: detailed diagnostic.

Events can store additional data besides the name and level via the use of the `EZ_TRACE_VALUE` macro. The following value types are supported:

| C++ Type | Description |
|---|---|
| `bool` | Boolean value. |
| `ezInt8`, `ezInt16`, `ezInt32`, `ezInt64` | Signed integers. |
| `ezUInt8`, `ezUInt16`, `ezUInt32`, `ezUInt64` | Unsigned integers. |
| `float` | 32-bit floating point. |
| `double` | 64-bit floating point. |
| `const char*` | Null-terminated UTF-8 string. |
| `const void*` | Pointer value (logs the address, not the data). |

The macro auto-detects the C++ type. Cast the value explicitly if the auto-detection picks the wrong type (e.g. `(ezInt32)42`).

### Instant Events

A single point-in-time event:

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-instant-event -->
```cpp
// Instant event demonstrating all supported value types.
const void* pDemoPtr = nullptr;
EZ_TRACE_EVENT("TestInstantEvent", ezTraceLevel::Info,
  EZ_TRACE_VALUE("BoolField", true),
  EZ_TRACE_VALUE("Int8Field", (ezInt8)-1),
  EZ_TRACE_VALUE("Int16Field", (ezInt16)-16),
  EZ_TRACE_VALUE("Int32Field", (ezInt32)42),
  EZ_TRACE_VALUE("Int64Field", (ezInt64)1234567890LL),
  EZ_TRACE_VALUE("UInt8Field", (ezUInt8)255),
  EZ_TRACE_VALUE("UInt16Field", (ezUInt16)65535),
  EZ_TRACE_VALUE("UInt32Field", (ezUInt32)100),
  EZ_TRACE_VALUE("UInt64Field", (ezUInt64)9876543210ULL),
  EZ_TRACE_VALUE("FloatField", 3.14f),
  EZ_TRACE_VALUE("DoubleField", 2.71828),
  EZ_TRACE_VALUE("StringField", "hello"),
  EZ_TRACE_VALUE("PointerField", pDemoPtr));
```
<!-- END-DOCS-CODE-SNIPPET -->

### Scoped Events

Automatically records begin and end timestamps via RAII. Fields are attached to the begin event:

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-scoped-event -->
```cpp
// Scoped event (RAII begin + end).
{
  EZ_TRACE_SCOPE("TestScopedWork", ezTraceLevel::Verbose,
    EZ_TRACE_VALUE("Detail", "scope-payload"));
  ezThreadUtils::Sleep(ezTime::MakeFromMilliseconds(5));
}
```
<!-- END-DOCS-CODE-SNIPPET -->

### Manual Scope Events

For situations where the begin and end do not fall within the same C++ scope (e.g. across callbacks):

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-manual-scope -->
```cpp
// Manual scope begin + end (for cases where RAII is not applicable).
EZ_TRACE_SCOPE_BEGIN("TestManualScope", ezTraceLevel::Info,
  EZ_TRACE_VALUE("Detail", "manual-scope-payload"));
ezThreadUtils::Sleep(ezTime::MakeFromMilliseconds(5));
EZ_TRACE_SCOPE_END("TestManualScope");
```
<!-- END-DOCS-CODE-SNIPPET -->

### Async Activities

Correlate events across threads using a unique `ezUInt64` ID:

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-async-activity-start -->
```cpp
// Async activity that spans across threads.
const ezUInt64 uiAsyncId = 123456789ULL;
EZ_TRACE_ASYNC_BEGIN("CrossThreadActivity", uiAsyncId, ezTraceLevel::Info,
  EZ_TRACE_VALUE("Resource", "test-resource.dat"));
```
<!-- END-DOCS-CODE-SNIPPET -->

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-async-activity-end -->
```cpp
// Complete the async activity that was started on the main thread.
EZ_TRACE_ASYNC_END("CrossThreadActivity", m_uiAsyncId);
```
<!-- END-DOCS-CODE-SNIPPET -->

### Flushing

Call `EZ_TRACE_FLUSH()` before stopping a trace session to ensure all buffered events are written out. Some backends buffer events internally and may lose the tail of a trace without an explicit flush.

<!-- BEGIN-DOCS-CODE-SNIPPET: tracing-flush -->
```cpp
// Flush buffered events to the tracing backend.
EZ_TRACE_FLUSH();
```
<!-- END-DOCS-CODE-SNIPPET -->

## Log Writer

`ezLogWriter::Tracing` is a log writer that forwards `ezLog` messages as trace events. It is automatically registered in `ezGameApplicationBase::BaseInit_ConfigureLogging` but you may have to register it manually if you are creating a custom application:

```cpp
ezGlobalLog::AddLogWriter(ezLogWriter::Tracing::LogMessageHandler);
// ... run application ...
ezGlobalLog::RemoveLogWriter(ezLogWriter::Tracing::LogMessageHandler);
```

This makes all engine log output (including `EZ_LOG_BLOCK` scopes) visible in the trace alongside your custom events.

## Capturing Traces

A cross-platform PowerShell 7 script is provided at `Utilities/Tracing/Capture-Trace.ps1`. It supports Windows, Linux, and Android.

### Interactive Mode

Start a trace, wait for a keypress, then stop and save:

```sh
pwsh Utilities/Tracing/Capture-Trace.ps1
```

### Non-Interactive Mode

For automation and CI:

```sh
pwsh Utilities/Tracing/Capture-Trace.ps1 -Start
# ... run application ...
pwsh Utilities/Tracing/Capture-Trace.ps1 -Stop -OutputPath my-trace.etl
```

### Android

Target a connected Android device via Perfetto:

```sh
pwsh Utilities/Tracing/Capture-Trace.ps1 -Android
```

When `-OutputPath` is not specified, traces are saved in the current working directory with an ISO-timestamped name (e.g. `ez-trace-2026-02-14T15-30-00.etl`).



### Platform Prerequisites

#### Windows (ETW)

* `wpr.exe` must be on PATH (ships with Windows 10+).
* Must run as Administrator.
* The WPR profile `Utilities/Tracing/ezTraceProvider.wprp` is used automatically.
* Open traces in [Windows Performance Analyzer](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-analyzer).

To capture manually without the script:

```bat
wpr -start Utilities\Tracing\ezTraceProvider.wprp
:: ... run your application ...
wpr -stop MyTrace.etl
wpa MyTrace.etl
```

#### Linux (LTTNG)

* Install LTTNG tools: `sudo apt install lttng-tools lttng-modules-dkms liblttng-ust-dev`
* Build with `EZ_3RDPARTY_TRACELOGGING_LTTNG_SUPPORT=ON` (default on Linux).
* Your user must be in the `tracing` group: `sudo usermod -aG tracing $USER` (log out and back in).
* Open traces in [Trace Compass](https://www.eclipse.org/tracecompass/).

To capture manually without the script:

```sh
lttng create ez-session
lttng enable-event -u 'ez_*:*'
lttng add-context -u -t vpid -t vtid -t procname
lttng start
# ... run your application ...
lttng stop
lttng destroy
```

To add kernel scheduling events (requires root):

```sh
sudo lttng enable-event -k sched_switch,sched_wakeup
```

#### Android (Perfetto)

* Build with `EZ_3RDPARTY_PERFETTO_SUPPORT=ON` (default on Android).
* The Perfetto config `Utilities/Tracing/ez-perfetto.pbtx` is used automatically.
* If traces are zero bytes, run `pwsh Utilities/Tracing/Capture-Trace.ps1 -Android -Cleanup` which restarts the perfetto daemon on the device. Note this requires root so your only alternative is to restart the device if your device isn't rooted.
* Open traces in the [Perfetto UI](https://ui.perfetto.dev). Events appear under the `ez` category.

To capture manually without the script:

```sh
adb push Utilities/Tracing/ez-perfetto.pbtx /data/local/tmp/
adb shell perfetto --txt -d \
  -c /data/local/tmp/ez-perfetto.pbtx \
  -o /data/misc/perfetto-traces/ez.perfetto-trace
# ... run your application ...
adb shell 'kill -INT $(cat /data/local/tmp/ez-perfetto.pid 2>/dev/null)'
adb pull /data/misc/perfetto-traces/ez.perfetto-trace .
```

## Viewing Traces

While you can use the most common trace viewer for you respective platform:
1. [Windows Performance Analyzer](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-analyzer) for Windows ETW traces.
1. [Trace Compass](https://www.eclipse.org/tracecompass/) for Linux LTTNG.
1. [Perfetto UI](https://ui.perfetto.dev) for Android perfetto traces.

You also have the option of converting to different trace formats to use different tools. No tool is perfect and each has its own strength and weaknesses. Some options to consider:
1. There are many tools that can read LTTNG traces.
1. You can use [ctf2ctf](https://github.com/KDABLabs/ctf2ctf) to convert LTTNG traces to Chrome Trace Format (json). Chrome trace format can be opened by [chrome://tracing/](chrome://tracing/) in chromium-based browser or in Qt's [Chrome Trace Format Visualizer](https://doc.qt.io/qtcreator/creator-ctf-visualizer.html).
1. You can install [Microsoft Performance Tools Linux / Android](https://github.com/microsoft/Microsoft-Performance-Tools-Linux-Android) plugins into WPA to be able to load perfetto and LTTNG (ctf format) traces. Note that you need to zip the LTTNG trace folder and rename it to `*.ctf` in order to open it in WPA.

## See Also

* [Tracy Integration](tracy.md)
* [Profiling](../performance/profiling.md)
* [Logging](logging.md)
* [Debugging C++ Code](debug-cpp.md)
