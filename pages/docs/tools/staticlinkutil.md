# StaticLinkUtil

When **statically linking** libraries into an application the linker will only pull in all the functions and variables that are inside
translation units (CPP files) that somehow get referenced.

In EZ a lot of stuff happens automatically (e.g. types register themselves etc.), which is accomplished through global variables
that execute code in their constructor during the application's startup phase. This only works when those global variables are actually
put into the application by the linker. If the linker does not do that, functionality will not work as intended.

## Mitigation

Contrary to common believe, the linker is not allowed to optimize away global variables. The only reason for not including a global
variable into the final binary, is when the entire translation unit where a variable is defined in, is never referenced and thus never
even looked at by the linker.

To fix this, the StaticLinkUtil inserts macros into each and every file which reference each other. Afterwards every file in a library will
reference every other file in that same library and thus once a library is used in any way in some program, the entire library
will be pulled in and will then work as intended.

These references are accomplished through empty functions that are called in one central location (where `EZ_STATICLINK_LIBRARY` is defined),
though the code actually never really calls those functions, but it is enough to force the linker to look at all the other files.

## Usage

Call this tool with the path to the root folder of some library as the sole command line argument:

```cmd
StaticLinkUtil.exe "C:\ezEngine\Code\Engine\Foundation"
```

This will iterate over all files below that folder and insert the proper macros.
Also make sure that exactly one file in each library contains the text `EZ_STATICLINK_LIBRARY();`

The parameters and function bodies will be generated automatically and later updated, you do not need to provide more.

You only need to run this tool, if you intend to link statically, which is only needed on some platforms. Even then, most new code will work even without always keeping the static link macros up to date, as the issues that it fixes are not too common. If, however, you notice that some types are missing (such as new components) that were just added, you should rerun this tool on the affected libraries.

## See Also


