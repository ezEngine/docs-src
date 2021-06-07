# String Formatting

For formatting strings there are a couple of different options:

* `ezConversionUtils` provides various `ToString` functions. These are useful for generic cases, where only individual variables need to be converted to a string representation and no control over the exact formatting is needed. `ezConversionUtils` also provides functions to parse strings for numbers.
* `ezStringUtils::snprintf` is a custom implementation of the infamous C `printf` function, with better security against buffer overruns and consistent behavior across platforms. It is available, but should generally be avoided, as it cannot provide any type safety.
* `ezFormatString` is the preferred way to do string formatting. It is easy to use, fully type safe, extensible with custom formatters and optimized for performance by doing only very few allocation and delaying the formatting until it is needed, which enables functions to not pay the price for formatting an incoming string, if the function doesn't actually use the result.

## Using ezFormatString as an Argument

`ezFormatString` is a class that can be easily used as a function parameter to accept formatted strings:

```cpp
void Print(const ezFormatString& text);
```

A function that takes just an `ezFormatString` has to be called with the `ezFmt` wrapper:

```cpp
Print(ezFmt("Hello {}", "World"));
```

The `ezFmt` function is a variadic template, that can take up to 10 arguments and wraps them all up into an `ezFormatString` object.

If you want your `Print` function to be a little bit more convenient, and not require the use of `ezFmt`, you can add an overload that provides the variadic template functionality directly.

```cpp
template <typename... ARGS>
void Print(const char* szFormat, ARGS&&... args)
{
    Print(ezFormatStringImpl<ARGS...>(szFormat, std::forward<ARGS>(args)...));
}
```

Now `Print` can be called like this:

```cpp
Print("Hello {}", "World");
```

Inside `Print`, all you need to do to get the formatted string is to call `ezFormatString::GetText()`:

```cpp
void Print(const ezFormatString& text)
{
    ezStringBuilder tmp;
    const char* szResult = text.GetText(tmp);

    // do something with szResult, do not use tmp, as it is not guaranteed to hold the result (meaning, it may not have been needed)
}
```

## Using ezFormatString

Once a function takes an `ezFormatString` (see above), you can use `{}` notation to indicate where an argument shall be inserted.

### Positional Arguments

If a formatting string contains `{}`, every instance will use the *next* argument, as given to the function. You can also use `{n}` with n being `0` to `9` to insert the n-th argument. This allows you to skip, rearrange, or repeat arguments:

```cpp
Print("Arg1: {1}, Arg2: {2}, Arg1: {1}", "zero", "one", "two");
```

### Formatting Options

Most types that can be formatted, can be passed in directly:

```cpp
Print("int value is {}", 23);
```

However, often you may want to specify exactly how to display the value. To do so, you need to wrap the incoming argument in an option struct. Each option struct can have arbitrary parameters to configure how it works.

```cpp
Print("HEX: 0x{}", ezArgU(value, 8, true, 16, true));
```

`ezArgU` is an option struct for unsigned int values. Here we specify that the output should have a fixed *width* of 8 characters, should pad the output with zeros if necessary, use base 16 (hex) and upper case letters.

There are many such option structs available, each with their own parameters. By convention, all formatting option structs are named `ezArgXYZ`.

### Available Option Structs

This is a not necessarily complete list of available option structs:

* `ezArgC` - for single characters
* `ezArgF` - for floating point values
* `ezArgI` - for int values
* `ezArgU` - for unsigned int values
* `ezArgP` - for pointers
* `ezArgErrorCode` - for Windows error codes
* `ezArgDateTime` - for ezDateTime
* `ezArgHumanReadable` - for shortening numbers with suffixes (such as `K` (kilo) and `M` (mega))
* `ezArgFileSize` - for shortening file sizes and use suffixes (such as `KB` and `MB`)

### Custom Argument Formatters

You can easily write your own formatter. The formatting work is done by a free function called `BuildString`, overloaded for the type that it shall format. If you search for `BuildString` functions, you will find many overloads, each handling a different type. Please look at those functions to see how to write your own formatter.

For it to work, all that is necessary, is that your code is `#include`'d when it is used in a format string. If you try to use a type (such as `MyType`) in a format string and your custom formatter is not known (`#include`'d) in that cpp file, you will get a compile time error with a *very long* message telling you that no overload of of `BuildString` is available to handle this type.

The `ezArgXYZ` structs are just used to wrap a type and store additional options. This is not required, for `BuildString` to work, but it does allow you to wrap the same type multiple times to select different formatters. For example, unsigned int is wrapped by `ezArgU` for regular int formatting options, by `ezArgFileSize` to print a value with `B`, `KB`, `MB` or `GB` suffixes and by `ezArgErrorCode` to interpret it as a Windows error code and translate it to a readable string. If you have a custom type `MyType` and you do not need any formatting options, you can write a `BuildString` overload, that takes a `MyType` directly.

## See Also


* [String Usage Guidelines](string-usage.md)
