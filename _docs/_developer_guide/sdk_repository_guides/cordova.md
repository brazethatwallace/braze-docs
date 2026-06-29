---
nav_title: Cordova SDK
article_title: Cordova SDK repository guide
page_order: 5
description: "Braze Cordova SDK README reference mirrored from GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## About the Braze Cordova SDK

The Braze Cordova SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Minimum version requirements

| Braze Plugin | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Minimum version requirements" }

This SDK additionally inherits the requirements of its underlying Braze native SDKs. Be sure to also adhere to the lists below:
* [Android SDK requirements](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Swift SDK requirements](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## Installing the SDK
{% alert warning %}
Only add the Braze Cordova SDK using the methods below. Do not attempt to install using other methods as it could lead to a security breach.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Running the sample application
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

For repository details and sample projects, see [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk).
