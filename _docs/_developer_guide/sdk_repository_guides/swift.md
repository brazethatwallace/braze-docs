---
nav_title: Swift SDK
article_title: Swift SDK repository guide
page_order: 3
description: "Braze Swift SDK README reference mirrored from GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## About the Braze Swift SDK

The Braze Swift SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## Quickstart

The following snippets show the minimum configuration required to add the Braze Swift SDK to your app.

``` swift
// AppDelegate.swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  // ...
  static var braze: Braze? = nil

  // ...
   func application(
      _ application: UIApplication, 
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // ...
        let configuration = Braze.Configuration(
            apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
            endpoint: "YOUR-BRAZE-ENDPOINT"
        )
        let braze = Braze(configuration: configuration)

        AppDelegate.braze = braze
        // ...
    }
}
```

``` swift
AppDelegate.braze?.changeUser(userId: "Jane Doe")
```

For more information about advanced integration options, see the [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift).

## Version support

The following table lists the minimum supported versions for tools used by the Braze Swift SDK.

Tool | Minimum supported version
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## Package Managers
- Swift Package Manager
- CocoaPods

## Libraries

The following table describes each library in the Braze Swift SDK.

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                             | iOS |     tvOS      | macCatalyst |   visionOS    |
|-----------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _Main SDK library providing support for [analytics] and [push notifications]._                            |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _Braze-provided user interface library for [In-App Messages] and [Content Cards]._                         |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _Location library providing support for [location analytics and geofence monitoring]._               |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _Notification service extension library providing support for [rich push notifications]._ |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _Notification content extension library providing support for [Push Stories]._                      |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Libraries" }

<sup>1</sup> _Push notifications not supported on tvOS_<br/>
<sup>2</sup> _Geofence monitoring not supported on tvOS and visionOS_

[analytics]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[push notifications]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[location analytics and geofence monitoring]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[rich push notifications]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## Examples

Explore our [examples project](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples) which showcases multiple features' integrations.

## Alternative Repositories

| Variant                               |                                     Repository | GH Issues, SDK info |
|---------------------------------------|-----------------------------------------------:|--------------------:|
| → **Sources and Static XCFrameworks** |                    [braze-inc/braze-swift-sdk] |                   ✓ |
| Static XCFrameworks                   |    [braze-inc/braze-swift-sdk-prebuilt-static] |                   ✗ |
| Dynamic XCFrameworks                  |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                   ✗ |
| Mergeable XCFrameworks (early access) | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                   ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Alternative Repositories" }

## Contact

For questions, contact [support@braze.com](mailto:support@braze.com).

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

For repository details and sample projects, see [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).
