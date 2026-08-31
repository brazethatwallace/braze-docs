---
nav_title: .NET MAUI (Xamarin) SDK
article_title: .NET MAUI (Xamarin) SDK repository guide
page_order: 10
description: "Braze .NET MAUI (Xamarin) SDK README reference mirrored from GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# .NET MAUI (Xamarin) SDK repository guide

## About the Braze .NET MAUI (Xamarin) SDK

The Braze .NET MAUI (Xamarin) SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=xamarin)

## Components

The format of this repository is that of a Xamarin component: under `appboy-component`, you will find the directories `src`,
`libs`, `component`, `nuget`, and `samples`. `libs`, `src`, and `samples` each contain two directories, one for Android and one for iOS. The directories
contain:

- `libs`: The compiled DLL bindings for the Braze SDKs.
- `src`: The Xamarin bindings projects that generated the DLLs found in the `libs` folder.
- `samples`: Xamarin applications that show how to use the bindings to access the Braze feature set.
- `nuget`: Nuspec files for our Xamarin NuGet packages.

## Versioning

### Native Bindings

The following table lists the supported frameworks and native Braze framework versions for each Xamarin binding.

| Binding file name                          | Supported Xamarin Frameworks                              | Native Braze framework                              | Braze Xamarin SDK version |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 43.1.1+                                 | 10.0.0+                   |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 and before | Android SDK 23.3.0 and before                       | 1.26.0 and before         |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 18.2.0+                                   | 10.0.0+                   |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 and before     | `Appboy_iOS_SDK.framework` version 4.4.1 and before | 1.27.0 and before         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Native Bindings" }

### Xamarin & Xamarin.Forms

As of May 1, 2024, [Microsoft announced the end of support for Xamarin and Xamarin.Forms](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

The Braze SDK version dropped support for Xamarin & Xamarin.Forms starting with version `4.0.0` and added support for [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui).

## Questions?

For questions, contact Braze Technical Support for assistance.
<!-- END GENERATED README CONTENT -->

For repository details and sample projects, see [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).
