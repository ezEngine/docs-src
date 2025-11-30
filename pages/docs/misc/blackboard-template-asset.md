# Blackboard Template Asset

A *blackboard template asset* is used to set up a configuration of a [blackboard](blackboards.md). Components, such as the [local blackboard component](local-blackboard-component.md) or the [global blackboard component](global-blackboard-component.md) can reference these templates to configure their blackboards with the same configuration. This is prefereable to setting up the configuration directly on the component.

## Asset Properties

* `BaseTemplates`: If any other templates are referenced here, their entries are first be added to the blackboard. This template may add further entries or overwrite the previously added ones.

* `Entries`: When a template is used by a [blackboard component](local-blackboard-component.md) these entries will be added to its blackboard. Some systems that use a blackboard may add their own entries, others expect an entry to already exist. For example the [input component](../input/input-component.md) may write input state into a blackboard, but it will only do so for entries that already exist.

## See Also

* [Blackboards](blackboards.md)
* [Local Blackboard Component](local-blackboard-component.md)
* [Global Blackboard Component](global-blackboard-component.md)
