---
nav_title: .NET MAUI (Xamarin) SDK
article_title: .NET MAUI (Xamarin) SDK リポジトリガイド
page_order: 10
description: "Braze .NET MAUI (Xamarin) SDK READMEリファレンス（GitHubからミラーリング）。"
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze .NET MAUI (Xamarin) SDKについて {#about-the-braze-net-maui-xamarin-sdk}

Braze .NET MAUI (Xamarin) SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリケーションに統合するのに役立ちます。

開始するには、以下のリソースを参照してください：

- [Brazeユーザーガイド]({{site.baseurl}}/user_guide/introduction/)
- [Braze開発者ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=xamarin)

## コンポーネント {#components}

このリポジトリの形式はXamarinコンポーネントです。`appboy-component`の下に、`src`、`libs`、`component`、`nuget`、`samples`のディレクトリがあります。`libs`、`src`、`samples`にはそれぞれ、Android用とiOS用の2つのディレクトリが含まれています。各ディレクトリには以下が含まれます：

- `libs`：Braze SDKのコンパイル済みDLLバインディング。
- `src`：libsフォルダにあるDLLを生成したXamarinバインディングプロジェクト。
- `samples`：バインディングを使用してBrazeの機能セットにアクセスする方法を示すXamarinアプリケーション。
- `nuget`：Xamarin NuGetパッケージ用のNuspecファイル。

## バージョニング {#versioning}

### ネイティブバインディング {#native-bindings}

| バインディングファイル名                          | サポートされるXamarinフレームワーク                              | ネイティブBrazeフレームワーク                              | Braze Xamarin SDKバージョン |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 41.0.0+                                 | 9.0.0+                    |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android、<br/>Xamarin.Forms、<br/>.NET 5以前 | Android SDK 23.3.0以前                       | 1.26.0以前         |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 14.0.1+                                   | 9.0.0+                    |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS、<br/>Xamarin.Forms、<br/>.NET 5以前     | `Appboy_iOS_SDK.framework` バージョン4.4.1以前 | 1.27.0以前         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Native Bindings" }

### XamarinとXamarin.Forms {#xamarin-xamarinforms}

2024年5月1日をもって、[MicrosoftはXamarinおよびXamarin.Formsのサポート終了を発表しました](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)。

Braze SDKはバージョン`4.0.0`からXamarinおよびXamarin.Formsのサポートを終了し、[.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui)のサポートを追加しました。

## ご質問がありますか？ {#questions}

ご質問がある場合は、[support@braze.com](mailto:support@braze.com)までお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk)を参照してください。