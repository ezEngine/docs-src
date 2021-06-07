# Frequently Asked Questions

## Platforms

The ezEngine base libraries (Foundation, Core) have been built to be fully cross platform. The corresponding unit tests are run on Windows, Linux, Mac and Android every day. There are some stubs for functions that are currently only needed on Windows, but implementing them is easy to do, when needed.

Everything higher level (editor, tools, rendering) is **only implemented for Windows 10**. There is **no Linux**, **no Mac** and also **no Windows 8 or lower** support.

The editor uses Qt, so that is generally portable, and it wouldn't even be too crazy, but also not entirely trivial. There is some Windows specific code for inter process communication (pipes), which would need to be implemented differently on other systems.

## Render API

At the moment we only provide a **DX11 renderer**. We would like to switch to Vulkan at some point, but some non-trivial refactoring is needed first. This currently doesn't have a high priority for us.

Obviously, this would also be a prerequisite to porting the editor to other platforms.

## Networking & Multiplayer

The engine ships with the [Enet](../docs/appendix/third-party-code.md#enet) networking library included. This is a great, easy to use library that was developed for an FPS game.

There is **no multiplayer support** in EZ, whatsoever. For the foreseeable future we have no plans to add something. Multiplayer is a very complicated topic and the solutions vary drastically between genres, so providing something that "just works" isn't really possible.

If you want to do multiplayer, you have to implement that aspect yourself. This is possible, of course, and for games with simpler networking logic (turn based, slow or simply not competitive) it may not be too hard (still lots of work, though, as all game development is).

## Visual Scripting

Yes, EZ has [visual scripting](../docs/custom-code/visual-script/visual-script-overview.md). It's not really great, though. You can do simple level logic, like "if that lever is pulled, open that door". You shouldn't really use it for anything else. We are generally not convinced that visual scripting is a great way to program (in no engine, no matter how good their tools are). Therefore we have no plans on improving our implementation at the moment, we rather improve the [TypeScript](../docs/custom-code/typescript/typescript-overview.md) binding. Though, if you are a fan of visual scripting and want to improve it, feel free to look into it.

## Scripting with TypeScript

We have a [TypeScript](../docs/custom-code/typescript/typescript-overview.md) binding which is pretty decent. The entire game logic in the [Testing Chambers](../samples/testing-chambers.md) project is done with this.

Future work for the TypeScript binding is [gathered here](https://github.com/ezEngine/ezEngine/projects/2). If you have some experience working with the TypeScript compiler tools, we could use your help.

## Rendering

We don't have occlusion culling at the moment (through a CPU rasterizer), though would like to add that at some point.

## Terrain

We currently have **no terrain system**. We have several ideas how we would like to do this, but this is very low priority at the moment. If you want to do terrain, you should just import static meshes. Of course that also means you need to do terrain sculpting in a separate tool. What we do have, is a simple [heightfield component](../docs/terrain/heightfield-component.md). For basic scenarios this may already be sufficient.

## Skeletal Animation

We started implementing a skeletal animation system and got the basics up an running. It's still very, very limited, though. However, a skeletal animation system does have **high priority** for us.

## AI

We have an integration for building **nav-meshes with [Recast](../docs/appendix/third-party-code.md#recast)**. We also have some really crappy components to do simple steering. Those are awful and need to be rewritten. If you have experience with AI and would like to contribute something in this regard, we would be happy to get some help. AI has low priority for us at the moment, but since this is a very isolated problem domain, you could probably improve the status quo significantly, without having to know the engine too much in detail.

## Streaming

All our resources (textures, materials, shaders, ...) always use streaming. However, we have **no level streaming**. Since we also don't have a terrain system, this is currently not really needed. However, we do have [asset collections](../docs/performance/asset-collections.md), which can be used to load data in the background. So you could build a system that instantiates e.g. a part of a level only once the background loading is finished. The building blocks are there, but it's not working out of the box.

## Roadmap

We don't plan very far ahead. Here are the things we intend to work on in the near term.

1. High level documentation.
1. Small code samples, where needed for the documentation.
1. Automated tests for some features, especially where the documentation can benefit as well.
1. Bug fixing for issues discovered by the documentation efforts.
1. Polish user experience, especially for first time users, where possible with little effort.
1. Skeletal Animation System.

"Intend to work" **doesn't mean complete**, though. We can't give estimates on that.

## History & Team

The core team is about 5 people, who work on this project in their spare time. Time is our most precious resource, which is why we focus it on aspects where the project benefits the most. Good infrastructure has always been a focus for us, as this will save so much time in the long run. The team consists of engineers who previously worked on the [Vision Engine](https://en.wikipedia.org/wiki/Vision_(game_engine)).

We started working on ezEngine with an empty folder and a first blank .h file in November 2012. Every line of code was written from the ground up. The first project was a unit test framework. For source control we started with Mercurial. In 2013 we switched to Subversion. The history from SVN was migrated to git in 2018 (f86ff53686f839a5f729ff70b9ec09e110cbef94 is the first commit). Since then all development is done in the open through GitHub.

From the start our intention was to create something that is free to use with no restrictions. An important aspect was always to not create a monolithic engine that can only be used for certain types of games, but something that is flexible and can be adapted to many different use cases. Therefore, most functionality is plugin based and it is easy to strip out things that you don't need or replace them with a custom implementation. This design philosophy is for example why things like our texture processing are stand-alone tools, instead of being integrated into the editor, so that you can utilize these tools, even when you don't want to use the editor.

Consequently, good documentation both directly inside code, as well as external, is very dear to us. The best technology is worthless, if only few people know how to use it.

We would love to see EZ being used by other people. We try to fix issues and help out as well as possible, but there is only so much we can do with our time. We understand that for many people other engines are a better fit. If EZ does fit your needs, that's great. And if you are able to help out make it better, that's really awesome.

## See Also


* [How to Contribute](how-to-contribute.md)
* [Contact](../contact.md)
