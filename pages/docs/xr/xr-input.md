# XR Input

XR input is not much different from regular [input](../input/input-overview.md). XR controllers are normal input devices that are provided by the `ezXRInputDevice` and work just like any other input device with the added feature set that the controllers can be tracked in space.

## XR Feature Flags

There are various kinds of XR controllers which varying feature sets. At runtime, you can query the existance of a type of device via the `ezXRInputDevice::GetDeviceIDByType` function and its supported features by using the `ezXRInputDevice::GetDeviceFeatures` function.

```cpp
ezXRInterface* pXRInterface = ezSingletonRegistry::GetSingletonInstance<ezXRInterface>();
ezXRInputDevice& xrInput = pXRInterface->GetXRInput();
ezXRDeviceID deviceID = pXRInterface->GetXRInput().GetDeviceIDByType(ezXRDeviceType::LeftController);
if (deviceID != -1)
{
    ezBitflags<ezXRDeviceFeatures> features = pXRInterface->GetXRInput().GetDeviceFeatures(deviceID);
    if (features.IsSet(ezXRDeviceFeatures::GripPose))
    {
```

Besides using the feature flags, you can also query the name of the controller via the `ezXRInputDevice::GetDeviceName` call. This will return e.g. **Mixed Reality Motion Controller** or **Hand Interaction**.

## XR Device Presence

The `ezXRDeviceType::HMD` represents your head and is always present. This is not true for other controller. You can either poll their state via the `ezXRInputDevice::GetDeviceIDByType` function or you can subscribe to `ezXRInputDevice::GetInputEvent` which will inform you whenever input devices are added or removed.

## XR Input Mapping

XR input slots are defined in `Code\Engine\GameEngine\XR\XRInputDevice.h` and all start with **xr_**. Use the same machanism as for other input controllers to create an [input set configuration](../input/input-config.md).

## Pose Tracking

XR controllers also provide positional data. You can either use the [ezDeviceTrackingComponent](xr-components.md#device-tracking-component) to automatically make a game object follow a controller or you can manually query the controller transform using the `ezXRInputDevice::GetDeviceState` function.

Many devices support two poses `Grip` and `Aim`. The difference between the two is nicely explained [here](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#semantic-path-standard-pose-identifiers). 

```cpp
ezXRInterface* pXRInterface = ezSingletonRegistry::GetSingletonInstance<ezXRInterface>();
ezXRInputDevice& xrInput = pXRInterface->GetXRInput();
ezXRDeviceID deviceID = pXRInterface->GetXRInput().GetDeviceIDByType(ezXRDeviceType::LeftController);
if (deviceID != -1)
{
    const ezXRDeviceState& state = pXRInterface->GetXRInput().GetDeviceState(deviceID);
    if (state.m_bDeviceIsConnected && state.m_bGripPoseIsValid)
    {
        ezVec3 vPosition = state.m_vGripPosition;
        ezQuat qRotation = state.m_qGripRotation;
```
You should check for `m_bDeviceIsConnected` and either `m_bGripPoseIsValid` or `m_bAimPoseIsValid` before accessing the transform. Due to e.g. tracking loss, the controller can provide invalid poses at any point. 

## Hand Tracking

Hands (if supported by the platform) are exposed as input controllers via the input system as well as via raw hand-tracked data. If basic click interaction and pose tracking is not enough, you can use the `ezXRHandTrackingInterface` if present, to query the bone positions of your hands:

```cpp
ezXRHandTrackingInterface* pXRHand = ezSingletonRegistry::GetSingletonInstance<ezXRHandTrackingInterface>();
if (!pXRHand)
    return;

ezHybridArray<ezXRHandBone, 6> bones;
for (ezXRHand::Enum hand : {ezXRHand::Left, ezXRHand::Right})
{
    for (ezUInt32 uiPart = 0; uiPart < ezXRHandPart::COUNT; ++uiPart)
    {
        ezXRHandPart::Enum part = static_cast<ezXRHandPart::Enum>(uiPart);
        if (pXRHand->TryGetBoneTransforms(hand, part, ezXRTransformSpace::Global, bones) == ezXRHandTrackingInterface::HandPartTrackingState::Tracked)
        {
```

## See Also

* [Input](../input/input-overview.md)
* [XR Overview](xr-overview.md)
* [XR Components](xr-components.md)