# Welcome to ezEngine

ezEngine is a free, open source game engine written in C++. Its philosophy is to be modular and flexible, such that it can be adapted to many different use cases. EZ utilizes a plugin system to integrate features such as [FMOD](https://www.fmod.com) or [Jolt Physics](https://github.com/jrouwe/JoltPhysics). This makes it possible to only include those features that you need, or to replace systems with a custom solution that works better for your requirements.

[![video](https://img.youtube.com/vi/S342o8ZmPdA/0.jpg)](https://www.youtube.com/watch?v=S342o8ZmPdA)

Similarly, the EZ code base can be [built in multiple tiers](pages/docs/build/cmake-config.md#build-filter), where you either get the entire feature set, with a [fully functional editor](pages/getting-started/editor-overview.md), asset management and renderer, or you can strip it down to just the base libraries and core engine functionality. This can be extremely useful if you need to build a lot of custom technology, but require a high-performance, reliable foundation. EZ has a strong emphasis on providing robust, easy to use and well-tested base functionality. It is successfully being used in such a capacity in commercial products.

## When to use ezEngine

ezEngine is designed to be a great basis for complicated projects. It provides you with lots of functionality that is tedious and difficult to build, such as efficient STL like [container classes](pages/docs/appendix/container-usage.md), a [high-performance scenegraph](pages/docs/runtime/world/world-overview.md), resource streaming and much more. It can be used to build the tech for games, as well as for industry applications. In many code bases the lower level functionality is messy and buggy, because it is hard (and boring) to build these parts, and game developers rather spend time on making pretty pictures. In EZ the base functionality is clean, consistent, efficient and fully unit-tested. It [builds on Windows, Mac, Linux and Android](pages/docs/build/supported-platforms.md).

Out of the box EZ can be used to create games just with [scripting](pages/docs/custom-code/custom-code-overview.md). However, it is meant for people who need or want to build their own technology and are looking for a great foundation to build on top of. The ezEditor is a powerful and robust tool that enables quick iteration on ideas with fast startup-times and WYSIWYG real-time editing. It is also completely optional, in case you need a different kind of workflow.

EZ is also a very good fit for students interested in learning how modern game engines work. It is easy to setup, compiles fast, is well documented, and straight-forward to extend. We also welcome [contributions](pages/getting-started/how-to-contribute.md) in the form of code or art.

## When not to use ezEngine

ezEngine is mainly developed on Windows. The renderer currently uses DX11. A Vulkan port is in development and the tools are being ported to Linux as well, however this is still in the early phase and not yet productively usable.

It is also not comparable in feature completeness to commercial offerings such as Unreal or Unity. Although it does support scripting game logic both with TypeScript and Visual Scripting, it is not meant for low-code or no-code development. The scripting capabilities are limited, for many game ideas you need to be comfortable writing C++ code.

## Getting Started

* You can download [prebuilt binaries](pages/getting-started/binaries.md) or [clone the latest dev branch](https://github.com/ezEngine/ezEngine).
* See the [documentation](pages/docs/docs-overview.md) for [build instructions](pages/docs/build/building-ez.md) and available [samples](pages/samples/samples-overview.md).
* Check out the [FAQ](pages/getting-started/faq.md).
* There are [videos](pages/getting-started/videos.md) about various topics on our [YouTube channel](https://www.youtube.com/@ezEngine).
* If you need help, [contact us](pages/contact.md).
* Everyone is [welcome to contribute](pages/getting-started/how-to-contribute.md).
