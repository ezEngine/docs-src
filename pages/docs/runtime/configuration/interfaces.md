# Singleton Interfaces

*Singletons* are classes of which there should only be a single instance throughout the lifetime of the process. Although EZ uses the *singleton pattern* quite extensively for built-in classes, such as `ezTaskSystem` and `ezResourceManager`, those classes don't use dedicated singleton infrastructure. Instead, they only expose static functions, and there is no need for any instance.

Accessing such singletons is trivial, as you can always call their functions directly. However, there is another type of singleton, which does require special handling.

There are cases where you want to define an *interface* to make certain functionality available, but you may have different implementations. Only one implementation should ever be active, though. Concrete examples are the integrations of third party libraries. For example there is an `ezFrameCaptureInterface`. This class defines an interface through which `ezGameApplicationBase` can do a capture of the rendered frame, which can be used for debugging graphics issues. However, *how* such a frame capture could be taken, depends on the platform, the installed tools, the used graphics API and so on. This functionality may be available or not and the exact implementation that is needed can differ drastically.

Therefore, we want to be able to dynamically load the necessary implementation and make it available through the abstract interface. For the `ezFrameCaptureInterface` we have an implementation by our [RenderDoc integration](../../debugging/renderdoc.md). In the future we might have a second implementation for PIX or some other platform specific tool.

Using the singleton infrastructure, we can simply load an [engine plugin](../../custom-code/cpp/engine-plugins.md) that contains an implementation, and from that plugin register our implementation for that interface. Other code can then query for an instance of this interface and, if available, use it without knowing anything about the implementation, and without the need to link against that library.

## Implementing Singletons

This section shows all the pieces needed for a singleton. You can find the sample code in the [Sample Game Plugin](../../../samples/sample-game-plugin.md).

### Interface Base Class

First, you need to have a virtual base class that declares the actual interface.

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-interface -->
```cpp
/// \brief Pure virtual interface for demonstrating the singleton work flow
///
/// This declaration would typically be in a shared location, that all code can #include
class PrintInterface
{
public:
  virtual ~PrintInterface() = default;

  virtual void Print(const ezFormatString& text) = 0;
};
```
<!-- END-DOCS-CODE-SNIPPET -->

This is the class through which other code will later access the functionality, so it must be in a shared location.

### Interface Implementation

Next, you need one or more *implementations* of your interface. You can, of course, have zero implementations, if all you want to provide is the option for future extensibility, and your code should generally be able to handle the fact that no implementation is currently loaded.

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-impl-declaration -->
```cpp
/// \brief Implementation of the PrintInterface, just forwards the text to ezLog::Info()
///
/// This would typically be in a different plugin than the interface and would be allocated by that plugin on startup.
class PrintImplementation : public PrintInterface
{
  EZ_DECLARE_SINGLETON_OF_INTERFACE(PrintImplementation, PrintInterface);

public:
  PrintImplementation();

  virtual void Print(const ezFormatString& text) override;

private:
  // needed for the startup system to be able to call the private function below
  EZ_MAKE_SUBSYSTEM_STARTUP_FRIEND(SampleGamePluginStartupGroup, SampleGamePluginMainStartup);

  void OnCoreSystemsStartup()
  {
    /* we could do something important here */
  }
};
```
<!-- END-DOCS-CODE-SNIPPET -->

Note the `EZ_DECLARE_SINGLETON_OF_INTERFACE` macro. This adds one part of the required functionality. For one, this class adds a function to query the one and only instance of your class (`GetSingleton()`). Also, it prevents you from creating two instances of this class, as that would violate the singleton contract.

Finally, you need to add this to you cpp file:

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-impl-definition -->
```cpp
EZ_IMPLEMENT_SINGLETON(PrintImplementation);

PrintImplementation::PrintImplementation()
  : m_SingletonRegistrar(this) // needed for automatic registration
{
}
```
<!-- END-DOCS-CODE-SNIPPET -->

The macro again inserts vital code for your singleton to work. The constructor also has to follow the pattern shown above.

You can now implement the desired behavior for the overridden functions.

## Instantiating Singletons

The EZ singleton infrastructure does not automatically create an instance of singleton classes. It is up to you whether, when and how you create your instance. The most common way to do this, is to leverage the [startup system](startup.md) to hook into the engine startup process at the right time.

For details, read that chapter, but here is what you would typically do. At startup you instantiate your singleton implementation:

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-allocate -->
```cpp
ON_CORESYSTEMS_STARTUP
{
  // allocate an implementation of PrintInterface
  s_PrintInterface = EZ_DEFAULT_NEW(PrintImplementation);

  s_PrintInterface->OnCoreSystemsStartup();
  s_PrintInterface->Print("Called ON_CORESYSTEMS_STARTUP");
}
```
<!-- END-DOCS-CODE-SNIPPET -->

And at shutdown you make sure to clean it up again:

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-deallocate -->
```cpp
ON_CORESYSTEMS_SHUTDOWN
{
  s_PrintInterface->Print("Called ON_CORESYSTEMS_SHUTDOWN");

  // clean up the s_PrintInterface, otherwise we would get asserts about memory leaks at shutdown
  s_PrintInterface.Clear();
}
```
<!-- END-DOCS-CODE-SNIPPET -->

## Accessing Singletons

There are two ways that you can access your singleton instance. In a piece of code that knows for certain that it will only run in conjunction with a specific singleton implementation, you can access it directly:

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-query-instance -->
```cpp
PrintImplementation::GetSingleton()->Print("Called ON_HIGHLEVELSYSTEMS_SHUTDOWN");
```
<!-- END-DOCS-CODE-SNIPPET -->

This is the most efficient way. However, use cases for this should be relatively rare. The more common situation is, when you want to get the implementation for an interface. To do so, you need to go through `ezSingletonRegistry`:

<!-- BEGIN-DOCS-CODE-SNIPPET: singleton-query-interface -->
```cpp
ezSingletonRegistry::GetSingletonInstance<PrintInterface>()->Print("Called ON_HIGHLEVELSYSTEMS_STARTUP");
```
<!-- END-DOCS-CODE-SNIPPET -->

Here we don't need to know anything about the implementation and therefore have no link dependency on the library that provides it. This is how most code would access a singleton implementation. Be aware that this requires a more expensive lookup, so locally cache the result, if you want to do multiple function calls on it.

## See Also


* [Startup System](startup.md)
* [Engine Plugins](../../custom-code/cpp/engine-plugins.md)
