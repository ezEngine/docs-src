# Custom Code with AngelScript

[AngelScript](https://www.angelcode.com/angelscript) (AS) is a script language that was designed specifically to be used in games. Its syntax is very close to C++ which makes it easy to move code from C++ to AS and vice versa. Its runtime performance is also much better than many other script languages.

AngelScript code uses strong typing and is compiled up front, which makes it easy to detect coding errors. You can write short AS scripts directly in [AngelScript assets](as-asset.md), but it is more convenient to have code in separate files, which can be opened with [Visual Studio Code](https://code.visualstudio.com/download) (VSC).

There is a great extension for VSC, called [AngelScript Language Server](https://github.com/sashi0034/angel-lsp) (short: angel-lsp), which is supported by EZ, and which adds syntax highlighting, error detection, jump-to-definition and several other features to VSC, which makes editing AngelScript code for EZ very convenient.

AngelScript code compiles nearly instantly, and is automatically reloaded, which means you can edit a script, switch to the editor and press play, and have the latest code running without any delay.

## Video: Introduction to AngelScript

[![video](https://img.youtube.com/vi/3iWVQyZAp6k/0.jpg)](https://www.youtube.com/watch?v=3iWVQyZAp6k)

## The AngelScript Language

For a description of the AngelScript language, please consult the [AngelScript documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script.html).

## Extending the Engine with AngelScript

The AngelScript integration allows you to create [custom components](as-components.md). AngelScript components can interact both with each other, as well as with C++ components. The [APIs](as-api.md) available to AngelScript code are nearly identical to their C++ counterparts, to make it easy to migrate an AS component to C++.

## Instantiating AngelScript Components

AngelScript code is executed through the [script component](../visual-script/script-component.md). This is a C++ component which forwards everything of relevance to script code and back.
The same component is also used to execute [Visual Scripts](../visual-script/visual-script-overview.md).

## Compiling AngelScript Code

AngelScript code is compiled by [AngelScript assets](as-asset.md). If there is an error, the asset transform will fail (you can see all failing assets in the [Asset Curator](../../assets/asset-curator.md)). More error details can be found in the asset document.

Each script is compiled in isolation. Scripts can [#include](as-api.md#including-files) other files to share code. If a shared file gets modified, EZ automatically recompiles all scripts that depend on it.

## Messaging

AngelScript code can use [messages](../../runtime/world/world-messaging.md) to communicate both with other AS components, as well as with C++ components. AngelScript code can *handle* any message, and it can *send* (or *post*) any message. To communicate with another AS component, you can define custom message types directly in script code. To communicate with a C++ component, only C++ messages can be used, as the C++ code has no means to know and handle an AngelScript message. If necessary to do so, the custom message type has to be defined in C++.

See [Messaging in AngelScript Code](as-messaging.md) for details.

## Functionality Available in AngelScript

The AngelScript binding is a mixture of auto-generated code and hand-crafted APIs specifically tailored to provide a smooth experience.

### Manual Bindings

All the base functionality, such as the math code, has been manually bound to AngelScript, since this allows for the most efficient execution.

There are also a hand full of functions that require features (such as callbacks) which are not covered by the reflection system, and thus were added by hand.

### Auto-Generated Bindings

Where possible [reflection information](../../runtime/reflection-system.md) is used to expose EZ functionality to AngelScript. This is, for example, used to expose all C++ components, enums, flags, and messages.

However, only reflected parts are available to AngelScript. For components this is obvious, as only reflected parts will show up in the editor UI as well, but for messages you may come across a C++ message for which members are missing in the AS version, as reflecting message properties is technically not necessary for the message to work. If you do need that message on the AngelScript side, you need to add the proper reflection information.

Additionally, not all kinds of reflected properties are currently supported in AngelScript. *Array*, *map* and *set* properties are not available. Such reflected properties are simply not included in the auto-generated AS code.

### Auto-Generated Syntax File

EZ automatically generates the file `as.predefined` in the project root folder. This file is used by the VSC extension *angel-lsp* for code-completion and error-checking. But it is also a good source to see which functionality is generally available.

## See Also

* [Visual Studio Code](https://code.visualstudio.com)
* [Custom Code](../custom-code-overview.md)
