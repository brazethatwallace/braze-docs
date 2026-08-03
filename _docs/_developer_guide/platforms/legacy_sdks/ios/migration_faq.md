---
nav_title: Migration FAQ
article_title: iOS SDK Migration FAQ
platform: iOS
page_order: 12
description: "This page answers frequently asked questions about migrating from the Appboy iOS SDK (Objective-C) to the Braze Swift SDK."
noindex: true
---

# iOS SDK migration FAQ

> This page answers frequently asked questions about migrating from the legacy Appboy iOS SDK (also known as the Objective-C SDK) to the Braze Swift SDK.

{% multi_lang_include deprecations/objective-c.md %}

## Version support and end-of-life

### Is Appboy iOS SDK 4.7.0 end-of-life?

Yes, Appboy iOS SDK 4.7.0 (and all 4.x versions) has reached end-of-life. No security fixes or critical bug fixes are provided. While messaging and analytics continue to function normally, version 4.7.0 should be treated as unsupported from a security posture.

### What is the minimum Swift SDK version for production support?

Current major versions (16.x and later) are the target for ongoing support, bug fixes, and new features. Older minor versions may not receive ongoing maintenance.

## Compatibility libraries

### Are BrazeKitCompat and BrazeUICompat supported for production use on Swift SDK 17.x?

Yes, `BrazeKitCompat` and `BrazeUICompat` are supported for production use during migration. They are positioned as a minimal-migration "stepping stone" to help you move from the Appboy SDK to the Swift SDK with minimal code changes, not as a long-term destination. While they are formally supported and still receiving bug fixes, the intent is to eventually migrate away from these compatibility libraries to the modern Swift SDK APIs.

### When will BrazeKitCompat and BrazeUICompat be removed?

The Swift SDK team has plans to sunset the `BrazeKitCompat` library, but no specific timeline has been announced yet. It is recommended to plan for full migration to the modern Swift SDK APIs (`BrazeKit`, `BrazeUI`) rather than relying on the compatibility libraries indefinitely.

## Delayed initialization

### Can I delay SDK initialization until after user consent?

Yes. The Swift SDK supports delayed initialization, which is useful for apps that need to wait for user consent before starting the SDK. Call `Braze.prepareForDelayedInitialization()` (optionally with an `analyticsBehavior` parameter) early in `application(_:didFinishLaunchingWithOptions:)`, then initialize the SDK later by calling the standard Braze initializer after consent is gathered.

For detailed implementation, see [Set up delayed initialization]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_step-2-set-up-delayed-initialization-optional).

### What is the minimum Swift SDK version required for delayed initialization?

Swift SDK 11.2.0 is the minimum version for delayed initialization. Push and deep-link robustness for delayed initialization was further improved in version 14.1.0. Swift SDK 17.0.0 is well past both of these thresholds.

### What happens to events received before the SDK is initialized?

When the SDK is initialized, queued items are processed. However, behavior varies by channel:

| Channel | Pre-initialization behavior |
|---------|----------------------------|
| Push tokens | Enqueued; processed on initialization |
| Push opens/analytics | Enqueued by default (configurable to drop via `analyticsBehavior`) |
| Deep links | Enqueued; processed on initialization |
| In-app messages | Not buffered pre-initialization; require the SDK to be running |
| Content Cards | Not buffered pre-initialization; synced from server after initialization |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
In-app messages and Content Cards received before initialization are not guaranteed to be delivered. Make sure the SDK is initialized before attempting to display these channels.
{% endalert %}

## Resource bundles and SPM integration

### Why am I seeing a runtime error about missing `braze-swift-sdk_BrazeUI.bundle`?

This is not a known SDK bug and is likely due to an integration misconfiguration. Starting with Swift SDK 12.0.0, static XCFrameworks include resources directly instead of relying on external resource bundles.

### What are the SPM/Xcode/archive requirements for resource embedding?

Starting with Swift SDK 12.0.0, you must select **Embed & Sign** for the Braze XCFrameworks in your Xcode project settings—this applies to both static and dynamic variants. This is the most common root cause for missing bundle errors at archive or release time.

### How do I override resource bundles for non-standard build systems?

For non-standard build systems (Tuist, Bazel, Buck, CI), use the approved override APIs:

- `BrazeKit.overrideResourcesBundle` (note the plural "Resources")
- `BrazeUI.overrideResourcesBundle` (note the plural "Resources")

The singular `overrideResourceBundle` was deprecated in Swift SDK 8.1.0 and should not be used.

## User identity and push tokens

### Is there a validation checklist for preserving profiles, device associations, and push tokens?

No official migration-specific checklist exists in the documentation. We recommend that you perform the following validation steps:

1. Confirm `registerDeviceToken` or push automation is wired correctly post-migration.
2. Verify push-registered user counts in the dashboard before and after rollout.
3. Spot-check a few specific external IDs to confirm device associations remain intact.

### Does `changeUser` guarantee that push tokens follow the new user?

There is no explicit guarantee documented in writing. However, the design intent is that push tokens follow the device, not the user. Calling `changeUser` should re-associate the existing device token with the new user profile. You should test `changeUser`, check the dashboard, and confirm the token appears on the new profile before mass rollout.

