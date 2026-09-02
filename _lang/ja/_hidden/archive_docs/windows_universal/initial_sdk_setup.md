---
nav_title: SDKの初期設定
article_title: Windows Universal 用の SDK 初期設定
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windows ユニバーサルプラットフォームにBraze SDKを統合するための最初のSDK統合ステップについて説明します。"
search_rank: 1
hidden: true
---

# SDKの初期統合 {#initial-sdk-integration}
{% multi_lang_include archive/windows_deprecation.md %}

Braze SDKは、分析、セグメンテーション、エンゲージメントで使用される情報をレポートするためのAPIと、プッシュ通知の登録および通知の受信用にユーザーを登録する機能を提供します。

>  Windows Universal SDKは、.NET MAUI Windowsアプリとも互換性があります。

## ステップ 1: NuGet パッケージマネージャーを使用したSDKのインストール {#step-1-install-the-sdk-via-the-nuget-package-manager}

Windows ユニバーサルSDKは、[NuGet Package マネージャー](http://www.nuget.org/) を使用してインストールします。NuGetを使用してBraze Windows SDKをインストールするには:

1. プロジェクトファイルを右クリックします
2. **Manage NuGet Packages** をクリックします
3. 左側のドロップダウンメニューで **Online** をクリックします
4. 「NuGet.org」で「Appboy」を検索します
5. **AppboyPlatform.Universal.Release** NuGet パッケージをクリックし、**Install** をクリックします

>  Windows Universal ライブラリは、Windows 8.1、Windows Phone 8.1、および UWP のすべてのアプリケーションで使用する必要があります。

## ステップ 2: AppboyConfiguration.xml の作成と設定 {#step-2-creation-and-configuration-of-appboyconfigurationxml}

プロジェクトのルートディレクトリに `AppboyConfiguration.xml` という名前のファイルを作成し、そのファイルに次のコードスニペットを追加します。

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  [API キー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/)ページにあるAPIキーで `YOUR_API_KEY_HERE` を更新してください。

そのスニペットを追加したら、以下の `AppboyConfiguration.xml` のファイルプロパティを変更してください。

1. `Build Action` を `Content` に設定します
2. `Copy to Output Directory` を `Copy Always` に設定します

## ステップ 3: package.appxmanifest の設定 {#step-3-configuring-packageappxmanifest}

**Capabilities** タブで、`Internet (Client)` がオンになっていることを確認します。
![]({% image_buster /assets/img_archive/internet_client.png %})

## ステップ 4: アプリクラスの編集 {#step-4-editing-your-app-class}

- `App.xaml.cs` ファイルの `usings` に以下を追加します。

`````````csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- `OnLaunched` ライフサイクルメソッド内で以下を呼び出します。

`````````csharp
Appboy.SharedInstance.OpenSession();
```

- `OnSuspending` ライフサイクルメソッド内で以下を呼び出します。

`````````csharp
Appboy.SharedInstance.CloseSession();
```

## 基本的なSDK統合の完了 {#basic-sdk-integration-complete}

これでBrazeはアプリケーションからデータを収集するようになります。[属性]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)、[イベント]({{site.baseurl}}/developer_guide/analytics/logging_events/)、および[購入]({{site.baseurl}}/developer_guide/analytics/logging_purchases/)をSDKに記録する方法と、プッシュメッセージングを実装する方法については、次の記事を参照してください。

>  同じアプリでBraze Unityプロジェクトを使用している場合は、Brazeへの呼び出しを「AppboyPlatform.Universal.Appboy」として完全修飾する必要があります。