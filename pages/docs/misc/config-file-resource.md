# Config File Resource

The `ezConfigFileResource` is used to load files which contain lists of variable value assignments ("key/value pairs"). These variables are strictly typed (`int`, `float`, `bool` or `string`) and it is very efficient to look up these values at runtime.

You can use this kind of configuration files for anything in your code. From general game settings, to defining the properties of different game elements.

Since all resources can be hot reloaded at runtime, using `ezConfigFileResource`s allows you to tweak values while playing to immediately see the effect.

> **Important:**
>
> Currently, interacting with resources is only possible from C++ code.

An alternative to *config file resources* is [custom data](custom-data.md).

## File Structure

The layout of config files is similar to C/C++ code, including the support for the [C preprocessor](https://en.wikipedia.org/wiki/C_preprocessor).

### Declaring Variables

To add a *new* variable, write its type, name and initial value:

```cpp
int i = 1
float f = 2.3
bool b = false
string s = "hello"
```

### Overriding Existing Variables

Once a variable has been declared the first time, it is an error to redeclare it the same way. Instead you need to add the `override` keyword:

```cpp
override int i = 11
override float f = 21.3
override bool b = true
override string s = "world"
```

It is also an error to declare a variable for the first time *with* the override keyword. This is to ensure that you have one place where the variable name is defined clearly, and to be able to point out where variables have been misspelled later on.

### Defining Value Names

You can use `#define` to define a fixed name for a certain value:

```cpp
#define SmallValue 3
#define BigValue 5
int MyValue = BigValue
```

This is more convenient to read and makes it easier to define and tweak values in one place.

### Hierarchical File Structure

You can `#include` other config files to pull in their variable definitions:

```cpp
#include "BaseConfig.ezConfig"
override int SomeValue = 7
```

Here the variable `SomeValue` must have been declared in *BaseConfig.ezConfig* (or another file included by that file). The code then overrides the existing variable with a custom value. If *BaseConfig.ezConfig* did not declare that variable, you will see an error in the [log](../debugging/logging.md).

Using this feature, it is very convenient to define variables (and their default values) for things like units in a game (players, enemies, etc) and then override variables where needed for specific unit types.

### Conditional Evaluation

You can use all C preprocessor features, such as `#ifdef` to conditionally evaluate the config files:

```cpp
#define TESTING 1

#ifdef TESTING
int PlayerHealth = 1000000
#else
int PlayerHealth = 100
#endif
```

## See Also

* [Resource Management](../runtime/resource-management.md)
* [C preprocessor (Wikipedia)](https://en.wikipedia.org/wiki/C_preprocessor)
* [Custom Data](custom-data.md)
