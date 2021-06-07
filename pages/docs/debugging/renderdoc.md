# RenderDoc Integration

[RenderDoc](https://renderdoc.org/) is a great tool to capture rendering commands for analysis and debugging. Commonly, to analyze a rendering issue, one would launch an application through RenderDoc, such that it can hook into the application and record rendering commands.

ezEngine has a dedicated *RenderDocPlugin*, to integrate RenderDoc support even better. When that plugin is active (see [Project Settings](../projects/project-settings.md)) you can trigger a RenderDoc capture at any time, even if your application was not launched through RenderDoc.

## Taking Captures

If you write your own [application (TODO)](../runtime/application/application.md) you can hook up RenderDoc in different ways, however, by default these methods are available:

* **Press F11:** The `F11` key will take a capture of the current frame.
* Type `CaptureFrame()` into the game [console](console.md).

All captures are written to a sub-folder of the `appdata` [data directory](../projects/data-directories.md). On Windows this refers to the `%appdata%` folder, which you can find by typing `%appdata%` into Windows Explorer. The exact sub-folder is printed into the [log](logging.md) (or see the in-game [console](console.md)).

You can then open the capture using RenderDoc.

## See Also


* [ezInspector](../tools/inspector.md)
* [Profiling](../performance/profiling.md)
* [Common Application Features](../runtime/application/common-application-features.md)
