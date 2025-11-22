# Console

The in-game console is a utility for inspecting the [log](logging.md), modifying [CVars](cvars.md) and calling [console functions](#console-functions).

![Ingame Console](media/debug-console.jpg)

## Console Windows

The console provides multiple windows that can be shown, hidden, and rearranged:

* **Command Window:** Text input for entering commands with auto-completion. Shows command output separately from log messages.
* **Log Window:** Displays engine [log messages](logging.md). Supports text filtering and severity level filtering.
* **CVar Window:** Hierarchical tree view of all [CVars](cvars.md). CVars are organized by their dot-separated names (e.g., `r.Bloom` appears under "r" > "Bloom").
* **Stats Window:** Shows FPS, frame time graph, and memory usage.

### Pinnable Overlays

The Stats and Log windows can be *pinned* using the "Pin Window" checkbox. Pinned windows remain visible as overlays even when the console is closed. This is useful for monitoring performance or watching for specific log messages during gameplay.

## Key Bindings

The default key bindings for the console are:

* **F1** - Opens/closes the console.
* **Up / Down** - Select a previously entered command from the history. The history is saved to disk so that commands persist after restarting.
* **F2** and **F3** - Repeat last and second-to-last commands. This works even when the console is closed.
* **TAB** - Auto-completes the current input. Also displays all available input options in the output.
* **Enter** - Executes the typed command. If the typed text is only the name of a CVar without an assignment, this will print the current value and description of the CVar.

When the console is open, the mouse cursor is shown and not clipped to the window, allowing interaction with elements outside the console.

## Modify CVars

You can modify CVars by typing:

```cmd
CVarName = value
```

See the [CVars](cvars.md) chapter for details.

## Binding Keys

To bind commands to certain keys you can call:

```cmd
bind f App.ShowFPS=
```

This would bind the command 'App.ShowFPS=' (which toggles the display of the FPS counter) to the f-key. You can only bind commands to printable characters (a-z, 0-9) and the casing matters. So you can also bind another command to SHIFT+f by using `bind F ...`.

To unbind a key call:

```cmd
unbind f
```

## Log Filtering

The Log window provides filtering options to help find specific messages:

* **Text Filter:** Type in the filter field to show only log messages containing that text (case-insensitive).
* **Severity Filter:** Use the dropdown to filter messages by severity.
* **Clear Log:** Remove all current log messages from the display.

## Console Functions

Console functions are an easy way to expose C++ utility functions through the console. The class `ezConsoleFunction` is used to wrap any function (static or method function) in a delegate and enable the console to call it. Of course, since the user can only input certain types of variables in the console, the argument types that you can use are very limited: strings, numbers (int / float) and boolean.

This code snippet shows how to declare a console function in a class, for example inside a custom [game state](../runtime/application/game-state.md).

<!-- BEGIN-DOCS-CODE-SNIPPET: confunc-decl -->
```cpp
void ConFunc_Print(ezString sText);
ezConsoleFunction<void(ezString)> m_ConFunc_Print;
```
<!-- END-DOCS-CODE-SNIPPET -->

In the implementation the binding has to be completed. You need to provide a name under which to expose the function, a description (this should include the parameter list) and the actual function to forward the call to. For member functions this has to be an `ezDelegate` to also bind to the class instance (`this`).

<!-- BEGIN-DOCS-CODE-SNIPPET: confunc-impl -->
```cpp
SampleGameState::SampleGameState()
  : m_ConFunc_Print("Print", "(string arg1): Prints 'arg1' to the log", ezMakeDelegate(&SampleGameState::ConFunc_Print, this))
{
}

void SampleGameState::ConFunc_Print(ezString sText)
{
  ezLog::Info("Text: '{}'", sText);
}
```
<!-- END-DOCS-CODE-SNIPPET -->

When you now open the console (F1) in-game and press TAB, the 'Print' function will be among the listed functions. You can then execute it:

```cmd
Print("Hello Console")
```

If you need to call a certain function repeatedly, you can [bind the call to a key](#binding-keys) or use F2 and F3 to repeat it, as long as it is the last or second-to-last command in your history.

## See Also

* [CVars](cvars.md)
* [Logging](logging.md)
