# Custom Components with C++

To write a custom C++ component, the first thing you need is a custom [engine plugin](engine-plugins.md). Once you have that, and have it enabled in your [project settings](../../projects/project-settings.md), any custom component that you define in that plugin will show up in the editor and can be attached to [game objects](../../runtime/world/game-objects.md).

The [Sample Game Plugin](../../../samples/sample-game-plugin.md) shows all the pieces that you need, including multiple components to get inspiration from. This article describes the steps to create a simple custom component.

Before you continue, please read the [components chapter](../../runtime/world/components.md), as it already covers most things that you need to know.

## Component Manager Declaration

For every type of C++ component there is a corresponding [component manager](../../runtime/world/component-managers.md). The component manager is responsible for allocating and deallocating components and for updating them. Each component manager is tied to a single [world](../../runtime/world/worlds.md), so if you have multiple worlds, each world will hold its own instance of each component manager.

A component manager is a [world module](../../runtime/world/world-modules.md), so it can register functions to be called during specific [update phases](../../runtime/world/world-modules.md#update-phases) of the world.

For the vast majority of components we only need a component manager that calls `Update()` on our component type once a frame. We can declare such a simple manager like this in the header file for our component:

<!-- BEGIN-DOCS-CODE-SNIPPET: customcomp-manager -->
```cpp
using DemoComponentManager = ezComponentManagerSimple<class DemoComponent, ezComponentUpdateType::WhenSimulating>;
```
<!-- END-DOCS-CODE-SNIPPET -->

## Component Class Declaration

Next, we declare our component class. All components must derive (at least indirectly) from `ezComponent`. Also vital is to insert the `EZ_DECLARE_COMPONENT_TYPE` macro, where you pass in the own component class name, the base class, and the component manager class.

<!-- BEGIN-DOCS-CODE-SNIPPET: customcomp-class -->
```cpp
class DemoComponent : public ezComponent
{
  EZ_DECLARE_COMPONENT_TYPE(DemoComponent, ezComponent, DemoComponentManager);

  //////////////////////////////////////////////////////////////////////////
  // ezComponent

public:
  virtual void SerializeComponent(ezWorldWriter& stream) const override;
  virtual void DeserializeComponent(ezWorldReader& stream) override;

protected:
  virtual void OnSimulationStarted() override;

  //////////////////////////////////////////////////////////////////////////
  // DemoComponent

public:
  DemoComponent();
  ~DemoComponent();

private:
  void Update();

  float m_fAmplitude = 1.0f;             // [ property ]
  ezAngle m_Speed = ezAngle::Degree(90); // [ property ]
};
```
<!-- END-DOCS-CODE-SNIPPET -->

Here we override a couple of functions from `ezComponent`. For the binary serialization we must implement `ezComponent::SerializeComponent()`. As long as you test your component only inside the editor, you don't yet need to implement these functions, as the editor stores reflected properties automatically. However, once you want to export your scene, these functions are used, and if you forgot to properly serialize something, the exported scene will not work correctly.

Note that our sample component has a (non-virtual) function called `Update()`. This is necessary because we use the `ezComponentManagerSimple` here, which expects to find such a function. If you write your own component manager, you can do this differently.

## Reflection Block

In our cpp file we need to insert a [reflection](../../runtime/reflection-system.md) block for our component type. This tells the engine all the details about our component, for instance which properties it has.

<!-- BEGIN-DOCS-CODE-SNIPPET: customcomp-reflection -->
```cpp
// clang-format off
EZ_BEGIN_COMPONENT_TYPE(DemoComponent, 3 /* version */, ezComponentMode::Dynamic)
{
  EZ_BEGIN_PROPERTIES
  {
    EZ_MEMBER_PROPERTY("Amplitude", m_fAmplitude)->AddAttributes(new ezDefaultValueAttribute(1), new ezClampValueAttribute(0, 10)),
    EZ_MEMBER_PROPERTY("Speed", m_Speed)->AddAttributes(new ezDefaultValueAttribute(ezAngle::Degree(90))),
  }
  EZ_END_PROPERTIES;

  EZ_BEGIN_ATTRIBUTES
  {
    new ezCategoryAttribute("SampleGamePlugin"),
  }
  EZ_END_ATTRIBUTES;
}
EZ_END_COMPONENT_TYPE
// clang-format on
```
<!-- END-DOCS-CODE-SNIPPET -->

This information is used in various ways. The editor uses it for the UI. Attributes on each property allow you to configure what default values the editor should use, and whether it should clamp the range for values, etc. Bindings to other languages also use this information to generate the necessary code. Everything that is not mentioned in this block, is internal to the C++ code and hidden from the tools.

## Initialization and Update

Next up, we implement our basic component code:

<!-- BEGIN-DOCS-CODE-SNIPPET: customcomp-basics -->
```cpp
DemoComponent::DemoComponent() = default;
DemoComponent::~DemoComponent() = default;

void DemoComponent::OnSimulationStarted()
{
  SUPER::OnSimulationStarted();

  // this component doesn't need to anything for initialization
}

void DemoComponent::Update()
{
  const ezTime curTime = GetWorld()->GetClock().GetAccumulatedTime();
  const ezAngle curAngle = curTime.GetSeconds() * m_Speed;
  const float curHeight = ezMath::Sin(curAngle) * m_fAmplitude;

  GetOwner()->SetLocalPosition(ezVec3(0, 0, curHeight));
}

```
<!-- END-DOCS-CODE-SNIPPET -->

Components rarely need to do much in their constructor and destructor. Most setup should be done in `ezComponent::OnSimulationStarted()`. For components that should already have functionality in the editor, while the simulation is not yet running, you should do your setup in `ezComponent::OnActivated()` instead. There is no `OnSimulationStopped()`, as this would always be the same as `ezComponent::OnDeactivated()`.

As you can see, this component modifies the position of its owner object during its update. This is why we had to use `ezComponentMode::Dynamic` in the reflection block, to tell the engine that objects with this component attached may change their position.

## Serialization

Finally, to make our component also work in exported scenes, we need to implement serialization:

<!-- BEGIN-DOCS-CODE-SNIPPET: component-serialize -->
```cpp
void DemoComponent::SerializeComponent(ezWorldWriter& stream) const
{
  SUPER::SerializeComponent(stream);

  auto& s = stream.GetStream();

  s << m_fAmplitude;
  s << m_Speed;
}
```
<!-- END-DOCS-CODE-SNIPPET -->

This writes out the data in the latest format. If you change the format, you should increase the version number of your component in the reflection block at the very top.

Obviously, at runtime we also need to deserialize our component. This is where we implement backwards compatibility for older exported scenes:

<!-- BEGIN-DOCS-CODE-SNIPPET: component-deserialize -->
```cpp
void DemoComponent::DeserializeComponent(ezWorldReader& stream)
{
  SUPER::DeserializeComponent(stream);
  const ezUInt32 uiVersion = stream.GetComponentTypeVersion(GetStaticRTTI());

  auto& s = stream.GetStream();

  s >> m_fAmplitude;

  if (uiVersion <= 2)
  {
    // up to version 2 the angle was stored as a float in degree
    // convert this to ezAngle
    float fDegree;
    s >> fDegree;
    m_Speed = ezAngle::Degree(fDegree);
  }
  else
  {
    s >> m_Speed;
  }
}
```
<!-- END-DOCS-CODE-SNIPPET -->

## Conclusion

Adding a custom component in C++ is not hard. Use the [Sample Game Plugin](../../../samples/sample-game-plugin.md) as a playground to get started. Of course with C++ you have the typical restriction that you can't hot reload code, you have to close the editor, compile your plugin and reopen the editor. [Hot Reloading C++ Game Plugins in the Editor](cpp-code-reload.md) describes a mechanism that can basically do all that for you with a single button press, though.

Armed with these basics, you should have a look at existing components to see how to solve specific issues.

## See Also


* [Components](../../runtime/world/components.md)
* [Custom Code](../custom-code-overview.md)
* [Sample Game Plugin](../../../samples/sample-game-plugin.md)
* [Hot Reloading C++ Game Plugins in the Editor](cpp-code-reload.md)
