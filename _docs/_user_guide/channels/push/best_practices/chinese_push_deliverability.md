---
nav_title: Deliverability for Chinese Android devices
article_title: Push deliverability for Chinese Android Devices
page_order: 10

page_type: reference
description: "This article covers push deliverability nuances you should be aware of when targeting users on Android devices manufactured by Chinese OEMs."
channel: push

---

# Push deliverability for Chinese Android devices

> Some Android devices manufactured by Chinese Original Equipment Manufacturers (OEMs), such as Xiaomi, OPPO, Vivo, and Huawei, optimize for longer battery lives through aggressive app lifecycle management. This optimization may have the unintended consequence of shutting down background app processing, which can reduce the deliverability of your push notifications.<br><br>To make sure that your app's messaging performance works as expected on these devices, your marketing and engineering teams should collaborate and follow the steps outlined in this article.

## Steps for developers
These OEMs perform their optimizations through aggressive killing of background applications and blocking them from self starting to run background tasks. As a developer, you'll need to configure your app to ask the user to ease these restrictions whenever possible.

This can be achieved by having your app automatically start on your end user's device, which gives your app permission to run in the background and listen for messages from Braze. Unfortunately, since this is an OEM-specific problem and not an Android problem, there are no documented APIs for bringing up the auto-start permission prompt for each OEM.

To solve for this, integrate a library like [AutoStarter](https://github.com/judemanutd/AutoStarter) into your application. AutoStarter supports multiple manufacturers, giving you an easy way to call the startup permission manager on a wide array of devices. After you have integrated AutoStarter, call `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` to bring up the startup permission manager on your end user's device. Couple this action with a prompt encouraging the end user to enable "auto-start" for your app. Your marketing team will craft this message—see the next section!

## Steps for marketers
After your users opt in to receive push notifications, there are additional steps they can take on their end to improve message delivery for these devices. We recommend you follow up your [push primer message]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) with an in-app message targeted to users on Chinese OEM devices with these additional steps:

- Enable "auto-start" for the app
- Disable battery optimization for the app

### Identifying users on Chinese OEM devices

To target your in-app message to users on specific Chinese OEM devices, use the **Device Model** or **Device OS** [segmentation filters]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters):

- **Device Model:** Use this filter to target users by their mobile phone's model. For example, to identify Huawei devices, use a regex pattern containing `huawei` to match model names. For step-by-step setup instructions, see [Build a Device Model regex for Huawei devices](#build-a-device-model-regex-for-huawei-devices).
- **Device OS:** Use this filter to target users by operating system. Some Chinese OEMs, such as Huawei, may explicitly specify their custom Android version in the device OS field. For verification steps, see [Verify Device OS values before you target](#verify-device-os-values-before-you-target).

#### Build a Device Model regex for Huawei devices

1. Go to **Audience** > **Segments**, then create or edit a segment.
2. Add the **Device Model** filter.
3. Set the operator to **matches regex**.
4. Enter `huawei` to match Huawei model names.
5. (Optional) If you also want Honor-branded devices, use `(huawei|honor)`.

For more information on regex behavior in Braze and pattern testing, see [Regular expressions]({{site.baseurl}}/user_guide/audience/segments/regex).

#### Verify Device OS values before you target

Some OEM variants can report customized OS naming in device metadata. Because this value can vary by device model and Android distribution, verify what your users send in Braze before building the segment:

1. Go to **Search Users**, then open a profile for a known target user.
2. In the **Overview** tab, check **Recent devices** and review the OS value shown for that device.
3. Copy the exact OS string into your segment filter:
   - Use **Device OS** when you need an exact or regex-based OS string match.
   - Use **Device OS Version Number** when you need numeric version ranges.
4. In the segment composer, use **User Lookup** to confirm that test users match as expected.

For details on where to find device metadata in profiles, see [User profiles]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). For details on testing segment logic, see [Create a segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).
