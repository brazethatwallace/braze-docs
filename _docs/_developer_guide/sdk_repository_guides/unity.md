---
nav_title: Unity SDK
article_title: Unity SDK repository guide
page_order: 9
description: "Braze Unity SDK README reference mirrored from GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## About the Braze Unity SDK

The Braze Unity SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- [Braze User Guide]({{site.baseurl}}/user_guide/introduction)
- [Braze Developer Guide]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity)

## Plugin Setup

Before you can start using Braze in Unity scripts, you'll need to import the plugin files to your Unity project.

**Recommended:** The Android and iOS plugins are bundled as a Unity package available for download from the [SDK release page][1].

**Manual Plugin Setup:** Alternatively, you can copy the plugins into your Unity project:
  1. First, clone this repo.
  2. If you're not using any other plugins, all you have to do is copy the `Plugins` directory from this repo into the `Assets` folder of your Unity project.
  3. If you already have a `/<your-project>/Assets/Plugins` directory (probably because you're using another plugin already), copy `Plugins/Appboy/AppboyBinding.cs` into `/<your-project>/Assets/Plugins`. Then copy the contents of `Plugins/iOS` and `Plugins/Android` from this repo into `/<your-project>/Assets/Plugins/iOS` and `/<your-project>/Assets/Plugins/Android` respectively.

## Integration Setup

To integrate Braze into your Unity application, complete our instructions for [Integrating the Braze Unity SDK][2].

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: {{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity

## Contact

If you have questions, please contact [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

For repository details and sample projects, see [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk).
