# Tracy Integration

EZ has an integration for [Tracy](https://github.com/wolfpld/tracy), a popular tool for doing performance measurements, logging and memory inspection.

To get the latest version of Tracy, see their [releases](https://github.com/wolfpld/tracy/releases).

## Building with Tracy Support

Unfortunately, when Tracy support is enabled, it hooks into the PDB files (debug symbols) in such a way, that it breaks [Hot Reloading C++ Game Plugins in the Editor](../custom-code/cpp/cpp-code-reload.md).

Therefore, Tracy support is currently disabled by default.

Use the [CMake GUI](https://cmake.org/) to adjust the [CMake configuration](../build/cmake-config.md). Enable `EZ_3RDPARTY_TRACY_SUPPORT` then click *Configure* and *Generate*.

If you want to use Tracy to inspect memory usage, you should also enable `EZ_3RDPARTY_TRACY_TRACK_ALLOCATIONS`. Note that this adds additional performance overhead.

## Using Tracy

Once Tracy support is enabled, you can run `Tracy.exe` and connect to any EZ process, such as `ezEditor`, `ezEditorEngineProcess` or `ezPlayer`. Be aware that the editor uses multiple processes.

For more information about how to use Tracy, please consult [their documentation](https://github.com/wolfpld/tracy).

## See Also

* [ezInspector](../tools/inspector.md)
* [Profiling](../performance/profiling.md)
* [Debugging C++ Code](debug-cpp.md)
