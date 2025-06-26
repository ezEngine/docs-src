# Tracy Integration

EZ has an integration for [Tracy](https://github.com/wolfpld/tracy), a popular tool for doing performance measurements, logging and memory inspection.

The `tracy-profiler.exe` of the version with which EZ was compiled is checked into the folder `Data/Tools/Precompiled`.
To get the latest version of Tracy, see their [releases](https://github.com/wolfpld/tracy/releases).

## Building with Tracy Support

General support for Tracy is enabled by default, but can be disabled with the compile switch `EZ_3RDPARTY_TRACY_SUPPORT`.

If you want to use Tracy to also inspect memory usage, you need to enable `EZ_3RDPARTY_TRACY_TRACK_ALLOCATIONS` in the [CMake configuration](../build/cmake-config.md). Note that this adds additional performance overhead. By default, this option is disabled.

## Using Tracy

When Tracy support is enabled, you can run the Tracy profiler app either manually from `Data/Tools/Precompiled`, or you can launch it from the editor through *Tools > Launch Tracy...*. Connect to any EZ process, such as `ezEditor`, `ezEditorEngineProcess` or `ezPlayer`. Be aware that the editor uses multiple processes and you have to connect to the correct one, depending on what you want to profile.

For more information about how to use Tracy, please consult [its documentation](https://github.com/wolfpld/tracy).

## See Also

* [ezInspector](../tools/inspector.md)
* [Profiling](../performance/profiling.md)
* [Debugging C++ Code](debug-cpp.md)
