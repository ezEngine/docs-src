# MCP Server

*MCP* (Model Context Protocol) is the protocol that AI coding agents use to talk to an application. ezEngine ships an MCP server in two places: in the [editor](../editor/editor-launch.md), and in a running game. An agent that connects to one of them can inspect and modify the live application, instead of only reading and writing the project's files on disk.

Agents can already do a lot without this, since the [document file formats](../editor/editor-documents.md) are text and can be read and modified directly. What they cannot do that way is anything that needs the editor's own logic. The MCP server closes that gap: connected to the editor, an agent can do the things you would otherwise do through the UI - import and transform assets, open documents and change them through the same undo/redo system, build the C++ plugin, export the project. Connected to a running game, it can send input, let frames pass and take a screenshot, which is what lets it verify a result rather than guess at one.

Both hosts also expose the [reflection](../runtime/reflection-system.md) information, the [CVars](../debugging/cvars.md) and the [log](../debugging/logging.md) of their process, so an agent can work with custom C++, script and plugin types that it has no other knowledge of.

None of this has to be described to the agent - MCP is self-describing, so it asks the server what it can do and gets the full list with descriptions and arguments.

Where this helps is investigating problems, answering questions about a project that the files alone do not answer, and checking that a change actually works. It is not meant for AI driven scene or asset creation - for most authoring work a human is faster.

MCP is a development-only feature. The server exists only in [development builds](../build/cmake-config.md), and the plugin that implements it is never part of a project's plugin configuration, so it is not packaged when a project is [exported](../shipping/project-export.md).

## Editor

The editor starts its server automatically as soon as a project is open, on port **7391**. Nothing has to be enabled.

To run several editors at the same time, give each one its own port, since only the first can bind the default:

```cmd
ezEditor.exe -project "C:/dev/MyGame" -editor-mcpport 7500
```

The engine process that the editor runs the game in serves on the editor's port **+ 1**.

## Games

A game process starts a server only when asked to, by port:

```cmd
ezPlayer.exe -project "C:/dev/MyGame" -scene "Scenes/Main.ezScene" -mcpport 7401
```

Without `-mcpport` no server is started. This works for any game application built on the [game application](../runtime/application/application.md) framework, not just [ezPlayer](player.md), because the plugin is loaded on demand when the option is present.

## Connecting

The server speaks the *streamable HTTP* transport at `http://127.0.0.1:<port>/mcp`. Registering it with an MCP client the way a permanently running service would be registered is of limited use, since neither the editor nor a game runs most of the time and the port may differ per run. Agents usually just talk to the URL directly and start an editor or a game themselves when they need one.

## Custom Tools

Any [plugin](../custom-code/cpp/engine-plugins.md) can add its own tools by deriving from `ezMcpToolProvider`. There is no registration call, the type is found through reflection, and it works on both sides: an editor plugin adds tools to the editor, a runtime plugin adds tools to the game process.

This is worth doing for game specific functionality that an agent otherwise has no handle on - putting the game into a particular state, spawning something, reading out whatever your game considers its current situation. The generic tools cover the engine, but the questions you actually want to ask about your game are usually specific to it, and an agent can only ask what some tool exposes. A provider is a small class: describe the tools it offers, and implement them. Everything runs on the main thread, so an implementation can touch the world and the game state directly.

## Things to Know

* Every call runs on the main thread of the host and blocks it. Calls happen one at a time, and some - transforming all assets, exporting, compiling C++ - run for minutes.
* The editor suppresses modal dialogs for the duration of a call, so an agent cannot leave the editor waiting on a dialog that nobody will answer, and reports afterwards what was suppressed. Dialogs during startup are not covered by this, which is why an editor that an agent launches itself should be started with `-unattended`, see [Unattended Mode](../editor/editor-launch.md#unattended-mode).
* Injected input is merged with real input rather than replacing it, so you are never locked out of a game that an agent is driving.
* Nothing is saved implicitly, and everything an agent changed in a document can be undone.
* The server is bound to `127.0.0.1` and is reachable only from the same machine.

## See Also

* [Launching the Editor](../editor/editor-launch.md)
* [ezPlayer](player.md)
* [ezEditorProcessor](editor-processor.md)
* [Editor Plugins](../editor/editor-plugins.md)
