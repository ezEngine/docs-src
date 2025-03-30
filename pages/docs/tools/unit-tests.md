# Unit Tests

ezEngine has a strong focus on reliability. Consequently, testing is taken very seriously. Due to the way game engines work, typical test frameworks are not a good fit, which is why EZ has its own test framework.

## Test Framework

The test framework can be built purely for console execution or to have a graphical user interface. If the [CMake](../build/cmake-config.md) variable `EZ_ENABLE_QT_SUPPORT` is set, the test applications will show a GUI (unless skipped via command line).

### Command Line Options

Run any test suite with the argument `-help` to get the full list of available options.

### Test Structure

The test framework works with *tests* and *subtests*. A *test* takes care of the slow initialization, like setting up the engine, the *subtests* then check various functionality, without rerunning the same initialization procedures. Tests and subtests can be disabled to focus on a specific issue.

All tests are derived from `ezTestBaseClass` and global instances in code are automatically picked up and shown in the UI. For trivial tests, as used in the FoundationTest application there are additional helper macros `EZ_CREATE_SIMPLE_TEST_GROUP` and `EZ_CREATE_SIMPLE_TEST` to add a new test with just two lines of code.

While running use the macros `EZ_TEST_INT/FLOAT/STRING/...` to check an assumption and make the test fail if it doesn't hold. There is also `EZ_TEST_IMAGE` and `EZ_SCHEDULE_IMAGE_TEST` to compare a screen capture against a stored reference image. You *create* reference images by running a succesful test once and then copying the result images to the proper folder. This can be done automatically for you through the *Test Data* menu in the GUI.

Writing tests is generally quite easy. All the test infrastructure is well documented. The best way to figure out how to write a test, is to run the different test suites to see which test is similar to what you want to do. Then look at that test, and jump to the C++ code comments of the test infrastructure to learn what it is for.

## Test Suites

The tests can be included or excluded from the build using the [CMake](../build/cmake-config.md) variable `EZ_BUILD_UNITTESTS`. If enabled, they show up in MSVC under the top level *UnitTests* folder.

The following test suites are available:

1. **FoundationTest**: These tests are for the absolute base functionality, that's found in the *Foundation* project and the *Texture* project.

2. **CoreTest**: These tests are for the core engine functionality, like the [scenegraph](../runtime/world/world-overview.md) and [resource management](../runtime/resource-management.md).

3. **RendererTest**: This tests the basic rendering functionality that's available with the rendering API abstraction. It doesn't test the high level rendering features.

4. **ToolsFoundationTest**: This is for testing editor and tools specific infrastructure.

5. **GameEngineTest**: These tests use the full engine functionality to test various high level features. Therefore they cover various rendering features as well as game features.

6. **EditorTest**: This test runs the editor and exercises things like creating all types of asset [documents](../editor/editor-documents.md), and so on.

7. **RemoteTestHarness**: This is a helper project to run tests on UWP. 

## See Also


