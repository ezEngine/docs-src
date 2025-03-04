# Custom Code

There are currently three ways to write custom code:

1. [Custom Code with C++](cpp/cpp-overview.md)
1. [Custom Code with AngelScript](angelscript/angelscript-overview.md)
1. [Custom Code with Visual Scripts](visual-script/visual-script-overview.md)

## C++

Extending the engine with C++ is the most versatile and efficient. With C++ you have full access to the entire engine, giving you all the power you need. Any serious project will have to use C++ code for some parts. For things like game logic you can start with script code instead, and migrate critical parts to C++ on demand. Extending the renderer and access to third party integrations is mostly only possible from C++ code. Using the [C++ Project Generation](cpp/cpp-project-generation.md) feature, it is very quick and easy to set up a custom C++ plugin.

C++ obviously has the downsides of longer compilation times, and live updating code is not possible. There is a way for game plugins to be modifiable while the editor runs, and the editor can fully shut down and reload its engine process, which does enable a form of [live reloading of C++ code](cpp/cpp-code-reload.md).

## AngelScript

The AngelScript integration allows you to write custom components. The integration provides access to the most important aspects that are needed for game code. C++ components can be accessed, as long as they expose their functionality through [reflection](../runtime/reflection-system.md). AngelScript is very useful for game logic and allows to quickly create complex [prefabs](../prefabs/prefabs-overview.md). AngelScript is compiled to bytecode, which is interpreted in a VM. Its performance is decent, though, of course, slower than C++. However, migrating a critical component from AngelScript to C++ at a later stage is possible and usually straight-forward, due to the nearly identical syntax.

AngelScript code is updated every time you [run a scene](../editor/run-scene.md), which allows for quick iteration times.

## Visual Scripting

Visual script code is the most limited both in functionality and tooling, but it is quite convenient to use for small scripts that act as the glue code, for example between C++ and [state machines](game-logic/state-machine-asset.md), or for handling simple logic.
