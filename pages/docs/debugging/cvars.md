# CVars

CVars are global variables used for configuring the runtime. They are used for development to enable or modify hidden features.

## Types of CVars

Only a strictly limited set of CVar types is supported:

* `ezCVarBool`
* `ezCVarFloat`
* `ezCVarInt`
* `ezCVarString`

## Accessing and Modifying CVars

CVars are exposed in multiple ways.

### ezEditor

In [ezEditor](../../getting-started/editor-overview.md) you can open *Panels > CVars* to show a panel that allows you to modify CVars. Be aware that some CVars only have an effect when simulating the scene, and some even only when using Play-the-Game mode. The latter mostly happens when the effect of a CVar is implemented by a [Game State](../runtime/application/game-state.md).

### ezInspector

[ezInspector](../tools/inspector.md) allows you to modify CVars of the connected process using the same UI as the editor.

### In-Game Console

In-game a convenient way to modify CVars is the [console](console.md).

* Press **TAB** to list all CVars
* Type the beginning of a CVar name and press **TAB** to list CVars with just that prefix name.
* Type `CVarName = value` to modify the CVar's value.

  ```cmd
  cvar_bool = true
  cvar_bool =
  cvar_int = 3
  cvar_string = "test"
  ```

  For boolean CVars, typing 'var =' will toggle the variables value, which can be very handy, especially combined with using F2 to repeat the previous console command.

  You can also do basic arithmetic like so:

  ```cmd
  cvar_bool = not cvar_bool
  cvar_int = cvar_int + 1
  ```

### TypeScript

CVars can also be accessed through the [TypeScript API](../custom-code/typescript/ts-api.md#ezdebug).

## Command Line

CVars can be set through command line arguments using this syntax:

```cmd
MyGame.exe -CvarName Value
```

For example:

```cmd
MyGame.exe -Game.DebugDisplay true -fmod_MasterVolume 0.1
```

Values specified through the command line take precedence over stored values.

## Saving State

The value of a CVar is typically discarded when the program closes, however, if the CVar uses `ezCVarFlags::Save`, it will be saved and restored in the next run. Be careful with this flag, as it can be very confusing when it is used to toggle subtle behavior. Be especially careful keeping this flag in for production code.

There is also `ezCVarFlags::RequiresRestart` which means that modifying that variable will take no effect unless you restart the application. This can be used for things like screen resolutions and other initial values.

## Callbacks

You can subscribe to events for either all CVars or specific ones, to be informed when a CVar is modified.

## Example Code

You create a CVar simply by instantiating it as a global variable somewhere in a cpp file:

<!-- BEGIN-DOCS-CODE-SNIPPET: cvar-1 -->
```cpp
#include <Foundation/Configuration/CVar.h>

ezCVarBool cvar_DebugDisplay("Game.DebugDisplay", false, ezCVarFlags::Default, "Whether the game should display debug geometry.");
```
<!-- END-DOCS-CODE-SNIPPET -->

Then you can just treat it like a regular variable to read or write its value:

<!-- BEGIN-DOCS-CODE-SNIPPET: cvar-2 -->
```cpp
if (cvar_DebugDisplay)
{
  ezDebugRenderer::DrawLineSphere(m_pMainWorld, ezBoundingSphere(ezVec3::ZeroVector(), 1.0f), ezColor::Orange);
}
```
<!-- END-DOCS-CODE-SNIPPET -->

## See Also


* [Console](console.md)
* [ezInspector](../tools/inspector.md)