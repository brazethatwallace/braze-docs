---
nav_title: Flutter SDK
article_title: Flutter SDK repository guide
page_order: 6
description: "Braze Flutter SDK README reference mirrored from GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Flutter SDK repository guide

## About the Braze Flutter SDK

The Braze Flutter SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)

## Quickstart

The following snippets show the minimum configuration required to add the Braze Flutter SDK to your app.

``` bash
flutter pub add braze_plugin
```

### Android

``` xml
<!-- android/res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### iOS

``` swift
// AppDelegate.swift
import BrazeKit
import braze_plugin

class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
      apiKey: "<BRAZE_API_KEY>",
      endpoint: "<BRAZE_ENDPOINT>"
    )
    // - Enable logging or customize configuration here
    configuration.logger.level = .info
    let braze = BrazePlugin.initBraze(configuration)
    AppDelegate.braze = braze

    return true
  }
}
```

### Dart

``` dart
import 'package:braze_plugin/braze_plugin.dart';

// ...
_braze = new BrazePlugin();

// ...
_braze.changeUser("Jane Doe");
```

For more information about advanced integration options, see the [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Version support

The following table lists the minimum supported versions for tools used by the Braze Flutter SDK.

| Tool                                                         | Minimum supported version |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (integration via CocoaPods)                          | 1.10.0+                   |
| Flutter (integration via CocoaPods or Swift Package Manager) | 3.24.0+                   |
| iOS Deployment Target                                        | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Version support" }

This SDK also inherits requirements from the underlying Braze native SDKs. For more information, see [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) and [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## Sample App

The [`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) folder contains a sample app that illustrates how to integrate and use this package's APIs.

## Contact

For questions, contact Braze Technical Support for assistance.
<!-- END GENERATED README CONTENT -->

For repository details and sample projects, see [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk).
