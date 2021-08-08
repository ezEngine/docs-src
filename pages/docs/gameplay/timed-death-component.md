# Timed Death Component

The *timed death component* is used to automatically delete the object that it is attached to, after a timeout. Additionally, it may spawn a [prefab](../prefabs/prefabs-overview.md) when its timeout has been reached.

## Component Properties

* `MinDelay`: The minimum time to wait before deleting the parent object.
* `DelayRange`: An optional random range to wait. If this is set to zero, the component will execute exactly after a delay of `MinDelay`.
* `TimeoutPrefab`: If the component is triggered to delete the object, it may additionally spawn an instance of the selected prefab, at the location of the object.

## See Also

* [Spawn Component](spawn-component.md)
