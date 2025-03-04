# AngelScript API

This page gives an overview over the functionality that EZ exposes through AngelScript.

While this chapter mentions *what* is available, for concrete examles *how* to use the code, please look at the [sample projects](../../../samples/samples-overview.md), such as the [Testing Chambers](../../../samples/testing-chambers.md). They use AngelScript for gameplay code and demonstrate how to do many different things.

## AngelScript Language

For an introduction to the AngelScript language please consult the [AngelScript documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script.html).

Additionally, the following EZ specific limitations apply:

* Global variables are not allowed in AngelScript code.
* Certain types, such as `ezStringBuilder`, `ezStringView`, `ezGameObject@` and `ezComponent@` are forbidden to be used as member variables (they can only be used as temporary variables). To store these, use `ezString`, `ezGameObjectHandle` and `ezComponentHandle` instead.
* Not all types can be used in `array`s.
* Dictionaries and other containers are currently not available.
* The `string` type does not exist in AS code in EZ. Use `ezString` and other EZ specific string classes instead.
* There is no access to the filesystem or other OS functionality.

## Code Editing

Make sure to use [Visual Studio Code](https://code.visualstudio.com/download) (VSC) together with the VSC extension [AngelScript Language Server (angel-lsp)](https://github.com/sashi0034/angel-lsp).

## API Documentation

There is currently no API documentation directly in AngelScript available. However, all functions map directly to their C++ counterparts, so you can look at the [API Docs](../../api-docs.md) for those.

## Full API Listing

Once you set up AngelScript in a project, the file **as.predefined** is written to the project folder. This file lists the entire available API and is thus the best source for what is available and what the function signatures look like. The *angel-lsp* plugin for VSC uses this file to provide features such as auto-completion.

## Including Files

To use code that is written in a different `.as` file, use the `#include` statement. This works the same as in regular C++.

Paths can either be relative to the current file location, or relative to the [data directories](../../projects/data-directories.md).

A file-relative #include uses quotes:

```cpp
#include "../Shared/Common.as"
```

A data-directory-relative #include uses angle brackets:

```cpp
#include <Shared/Common.as>
```

> **Note**
>
> The angel-lsp plugin for VSC only understands file-relative paths.

Data-directory-relative paths have to be used, if you want to #include a file from a different [data directory](../../projects/data-directories.md).

## API Overview

The following APIs are frequently used:

### Math

The `ezMath` namespace provides general math functions. `ezVec2`, `ezVec3` and `ezVec4` are vector classes, `ezQuat` is a quaternion implementation for representing rotations. `ezTransform` represents a full position / rotation / scale transform.

`ezAngle` is used for representing angles either in degree or Radians.

`ezColor` is used for HDR colors in linear color space (the default) and `ezColorGammaUB` can be used for 8-bit colors in Gamma space (see [Color Spaces (TODO)](../../appendix/color-spaces.md)).

### Time

The class `ezTime` is used for storing time values. `ezClock` can be retrieved from the `ezWorld` and gives you the current game time.

Note that the `Update()` function of components comes with a `deltaTime` argument, which gives you the time between calls to `Update()`, whereas `ezClock` gives you the time difference between frames, which often is not the same.

### Random

An instance of `ezRandom` can be retrieved through the `ezWorld`. It generates random numbers.

### Strings

As in C++, there are multiple string classes in EZ.

* `ezString` is the default type for *storing* strings.
* `ezStringBuilder` is used for working with strings, ie for concatenating, formatting and so on. Instances of `ezStringBuilder` can only be used as local variables, they are forbidden as member variables.
* `ezStringView` is a read-only view into another string object. This is the typical way for passing strings into functions (instead of using `const char*` which doesn't exist in AS anyway). Since `ezStringView` doesn't store the actual string data, this type may also only be used temporarily and not stored as a member variable.
* `ezHashedString` and `ezTempHashedString` are also exposed to AS for completeness. Both are used to optimize repeated usage of strings and are needed to bind all functions to AS. You usually don't need to use them directly in script code.

### GameObject

Most functionality of `ezGameObject` is accessible in AS code. For details, [see this chapter](../../runtime/world/game-objects.md).

Additionally, in AS you can create components on a game object through `ezGameObject::CreateComponent()`. This is different to how it would be done in C++.

### Component

`ezComponent` is the base class for all C++ components. All these component types are automatically exposed to AS code.

### World

The `ezWorld` object represents the entire scenegraph of the currently running level. You can always call `ezAngelScriptClass::GetWorld()` to get access to the world. Through it you can create new game objects, send and post messages to other objects, and access things like the `ezClock` and `ezRandom`.

### Logging

The `ezLog` namespace contains functions for [logging](../../debugging/logging.md).

### Debug Rendering

The `ezDebug` namespace exposes some functions for [debug rendering](../../debugging/debug-rendering.md). Note that not all functionality is available.

### Physics

In the `ezPhysics` namespace you'll find functions to do raycasts, overlap queries and some other common operations that are powered by the physics engine.

There are also functions to trigger [surface interactions](../../materials/surfaces.md), such as spawning effects for impacts or footsteps.

### Spatial

The `ezSpatial` namespace contains some functions to access the [spatial system](../../runtime/world/spatial-system.md). This allows you to search for nearby objects of certain types, such as [marker components](../../gameplay/marker-component.md), to identify objects to interact with.

### Sound

The `ezSound` namespace contains functions to play sounds.

### array

The `array` class is a template type that can be used with many (but not all) types. It is mainly useful for saving state within AngelScripts. The API functions to interact with C++ code currently do not support passing arrays back and forth.

## See Also

* [Custom Code with AngelScript](angelscript-overview.md)
