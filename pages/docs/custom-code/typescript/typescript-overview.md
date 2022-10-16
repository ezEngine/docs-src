# Custom Code with TypeScript

[TypeScript](https://www.typescriptlang.org) (TS) is a language that is built on top of JavaScript. All JavaScript is valid TypeScript, but additionally TypeScript allows you to use strong typing to improve your coding experience. The TypeScript code itself is never executed, instead it is *transpiled* from TypeScript into pure JavaScript, and then interpreted by a regular JavaScript interpreter.

The benefit of using TypeScript is mostly in ease of use. You can edit TypeScript code with any text editor. However, ezEditor assumes that you have [Visual Studio Code](https://code.visualstudio.com/download) (VSC) installed. When you open a TS file from the editor, it will open an entire *workspace* in VSC, which contains references to all your project's [data directories](../../projects/data-directories.md). This enables VSC to give you full code-completion and type-checking functionality.

## Editing TypeScript Code

Providing a decent text editing experience for code is difficult. Therefore ezEditor doesn't even attempt to. All code editing has to be done in an external editor, usually meaning Visual Studio Code.

For details see the [TypeScript asset](ts-asset.md).

## Extending the Engine with TypeScript

The TypeScript integration allows you to create [custom components](custom-ts-components.md). TypeScript components can interact both with each other, as well as with C++ components. The APIs available to TypeScript code are deliberately very similar to their C++ counterparts, to make it easy to migrate a TypeScript component to C++, if the need arises.

At the moment you can't use TypeScript to write things like custom [game states](../../runtime/application/game-state.md).

## Instantiating TypeScript Components

TypeScript code is executed through the [TypeScript component](ts-component.md). This is effectively a C++ component which forwards everything of relevance to script code and back. Therefore you never add a script directly to a [game object](../../runtime/world/game-objects.md), instead you attach a TypeScript component, which then references the desired script.

## Compiling TypeScript Code

All functionality that TypeScript provides over JavaScript is technically possible to do with pure JavaScript, it is just very cumbersome. Therefore any piece of TypeScript can be transformed to (more complex) JavaScript code. This step is called *transpiling*.

All script code in a project has to be fully transpiled before a scene can be simulated. Therefore [running a scene](../../editor/run-scene.md) always triggers the transpilation step. Since the TypeScript transpiler is itself written in JavaScript and therefore executed in a JavaScript virtual machine, this step is unfortunately quite slow, especially for larger files. All results are cached, though, so only modified files ever need to be transpiled again.

Note that C++ reflection information is used to expose C++ components, enums, and messages to TypeScript, meaning that certain changes of C++ code can also trigger re-transpilation of some TypeScript files.

## Messaging

TypeScript code can use [messages](../../runtime/world/world-messaging.md) to communicate both with other TS components as well as with C++ components. TypeScript code can *handle* any message, and it can *send* (or *post*) any message. To communicate with another TS component, you can define custom message types directly in script code. To communicate with a C++ component, only C++ messages can be used, as the C++ code has no means to know and handle a TypeScript message. If necessary to do so, the custom message type has to be defined in C++.

See [Messaging in TypeScript Code](ts-messaging.md) for details.

## Functionality Available in TypeScript

The TypeScript binding is a mixture of auto-generated code and hand-crafted APIs specifically tailored to provide a smooth experience.

### Auto-Generated Code

Where possible [reflection information](../../runtime/reflection-system.md) is used to automatically generate the necessary TypeScript code to give Visual Studio Code the needed information for code-completion and error-checking. This is, for example, used to expose all C++ components, enums, flags, and messages. The generated TS code is stored in each project in the folder `TypeScript/ez` and you will notice that for instance the file `AllComponents.ts` is re-transpiled when a C++ component is added.

Consequently, for things like messages and components, only reflected parts can be available to TypeScript. For components this is obvious, as only reflected parts will show up in the editor UI as well, but for messages you may come across a C++ message for which members are missing in the TS version, as reflecting message properties is technically not necessary for the message to work. If you do need that message on the TypeScript side, you need to add the proper reflection information.

Additionally, not all kinds of reflected properties are currently supported for TypeScript. *Array*, *map* and *set* properties are not available, as well as *game object handles* and *component handles*. Such reflected properties are simply not included in the auto-generated TS code.

### Hand-Crafted Code

Although auto-generating code is the most convenient to keep large amounts of code in sync, there are limits what can be done. TypeScript and C++ are often very different and to not compromise the usability or performance of either side, the way some aspects are exposed to TypeScript has to be chosen carefully.

Basic types such as the math classes (Vec2, Vec3, Mat4, Quat, ...) have been designed to be very similar to their C++ counterparts. However, a big design goal was to minimize the amount of temporaries ('garbage') produced when using them, as this has a significant impact on performance. Therefore, using those classes you will notice that their functions often work 'in place', instead of returning a modified clone. Additionally, TypeScript doesn't support function overloading, which is why the TypeScript variants of `ez.Vec3`, etc use more explicit function names for disambiguation.

Finally, bindings for larger systems, such as [worlds](../../runtime/world/worlds.md) or [physics](../../physics/jolt/jolt-overview.md) are also built by hand. Here, exposing the C++ API 1:1 to TypeScript would simply not yield a good user experience. Instead, the TypeScript binding is fine tuned to expose useful functionality, and to hide pointless complexity. If you need full control over every aspect, there is no way around using C++ anyway. Consequently, if you decide that scripting is fine for your use case, the binding tries to make this as convenient as possible.

## Video

[![video](https://img.youtube.com/vi/T1eDenHWPKc/0.jpg)](https://www.youtube.com/watch?v=T1eDenHWPKc)

## See Also


* [TypeScript](https://www.typescriptlang.org)
* [Visual Studio Code](https://code.visualstudio.com)
* [Custom Code](../custom-code-overview.md)
* [TypeScript Asset](ts-asset.md)
* [Custom Components with TypeScript](custom-ts-components.md)
