---
nav_title: .NET MAUI (Xamarin) SDK
article_title: .NET MAUI (Xamarin) SDK 리포지토리 가이드
page_order: 10
description: "GitHub에서 미러링된 Braze .NET MAUI (Xamarin) SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze .NET MAUI (Xamarin) SDK 소개 {#about-the-braze-net-maui-xamarin-sdk}

Braze .NET MAUI (Xamarin) SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드](https://www.braze.com/docs/user_guide/introduction/)
- [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=xamarin)

## 구성요소 {#components}

이 리포지토리는 Xamarin 구성요소 형식으로 되어 있습니다. `appboy-component` 아래에 `src`, `libs`, `component`, `nuget`, `samples` 디렉토리가 있습니다. `libs`, `src`, `samples`에는 각각 Android용과 iOS용 두 개의 디렉토리가 포함되어 있습니다. 각 디렉토리에는 다음이 포함됩니다:

- `libs`: Braze SDK에 대한 컴파일된 DLL 바인딩입니다.
- `src`: libs 폴더에 있는 DLL을 생성한 Xamarin 바인딩 프로젝트입니다.
- `samples`: 바인딩을 사용하여 Braze 기능 세트에 접근하는 방법을 보여주는 Xamarin 애플리케이션입니다.
- `nuget`: Xamarin NuGet 패키지용 Nuspec 파일입니다.

## 버전 관리 {#versioning}

### 네이티브 바인딩 {#native-bindings}

| 바인딩 파일 이름 | 지원되는 Xamarin 프레임워크 | 네이티브 Braze 프레임워크 | Braze Xamarin SDK 버전 |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln` | .NET 9+ | Android SDK 41.0.0+ | 9.0.0+ |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 이하 | Android SDK 23.3.0 이하 | 1.26.0 이하 |
| `BrazeiOSBinding.sln` | .NET 9+ | Swift SDK 14.0.1+ | 9.0.0+ |
| `AppboyPlatformXamariniOSBinding.sln` | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 이하 | `Appboy_iOS_SDK.framework` 버전 4.4.1 이하 | 1.27.0 이하 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="네이티브 바인딩" }

### Xamarin 및 Xamarin.Forms {#xamarin-xamarinforms}

2024년 5월 1일부로, [Microsoft는 Xamarin 및 Xamarin.Forms에 대한 지원 종료를 발표했습니다](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

Braze SDK는 버전 `4.0.0`부터 Xamarin 및 Xamarin.Forms에 대한 지원을 중단하고 [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui)에 대한 지원을 추가했습니다.

## 질문이 있으신가요? {#questions}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 문의해 주세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk)를 참조하세요.