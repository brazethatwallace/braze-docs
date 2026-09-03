---
nav_title: マニュアル
article_title: iOSの手動統合オプション
platform: iOS
page_order: 4
description: "この参考記事では、iOS用Braze SDKを手動で統合する方法を説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 手動統合 {#manual-integration}

{% alert tip %}
[Swift パッケージマネージャー]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager)、[CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods)、[Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration) などのパッケージマネージャーを使用してSDKを実装することを強くお勧めします。これにより、時間を大幅に節約し、プロセスの多くを自動化できます。ただし、それができない場合は、手順に従って手動で統合を完了することができます。
{% endalert %}

## ステップ 1:Braze SDKのダウンロード {#step-1-downloading-the-braze-sdk}

### オプション 1:ダイナミック XCFramework {#option-1-dynamic-xcframework}

1. [リリースページ](https://github.com/appboy/appboy-ios-sdk/releases)から `Appboy_iOS_SDK.xcframework.zip` をダウンロードし、ファイルを展開します。
2. Xcode で、この `.xcframework` をプロジェクトにドラッグ＆ドロップします。
3. プロジェクトの**General**タブで、`Appboy_iOS_SDK.xcframework` に**Embed & Sign**を選択します。

### オプション 2:静的統合用の静的 XCFramework {#option-2-static-xcframework-for-static-integration}

1. [リリースページ](https://github.com/appboy/appboy-ios-sdk/releases)から `Appboy_iOS_SDK.zip` をダウンロードします。<br><br>
2. Xcodeのプロジェクトナビゲーターから、Brazeの送信先プロジェクトまたはグループを選択します。<br><br>
3. **File > Add Files > Project_Name** に移動します。<br><br>
4. `AppboyKit` と `AppboyUI` フォルダーをグループとしてプロジェクトに追加します。
	- 初めて統合する場合は、**Copy items into destination group's folder** オプションが選択されていることを確認してください。ファイルピッカーの**Options**を展開して、**Copy items if needed** と **Create groups** を選択します。
	- `AppboyKit/include` と `AppboyUI/include` のディレクトリーを削除します。<br><br>
5. (オプション) 次のいずれかに該当する場合:
  - SDKのコア分析機能のみが必要で、UI機能（アプリ内メッセージやContent Cardsなど）は使用しない。
  - Braze UI機能のカスタムUIがあり、画像のダウンロードを自分で処理する。<br><br>SDKのコアバージョンは、`ABKSDWebImageProxy.m` および `Appboy.bundle` のファイルを削除することで使用できます。これにより、`SDWebImage` フレームワークの依存関係とUI関連のすべてのリソース（Nibファイル、画像、ローカライゼーションファイルなど）がSDKから削除されます。

{% alert warning %}
Braze UI機能なしでコアバージョンのSDKを使用しようとしても、アプリ内メッセージは表示されません。コアバージョンでBraze Content CardsのUIを表示しようとすると、予期しない動作が発生します。
{% endalert %}

## ステップ 2:必要なiOSライブラリーの追加 {#step-2-adding-required-ios-libraries}

1. プロジェクトのターゲットをクリックし（左側のナビゲーションを使用）、**Build Phases**タブを選択します。<br><br>
2. **Link Binary With Libraries**の下の<i class="fas fa-plus"></i>ボタンをクリックします。<br><br>
3. メニューで `SystemConfiguration.framework` を選択します。<br><br>
4. `SystemConfiguration.framework` の横にあるプルダウンメニューを使用して、このライブラリーを必須としてマークします。<br><br>
5. これを繰り返して、次の各必須フレームワークをプロジェクトに追加し、それぞれを「required」としてマークします。
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. 次のフレームワークを追加し、オプションとしてマークします。
	- `CoreTelephony.framework`<br><br>
7. **Build Settings**タブを選択します。**Linking**セクションで、**Other Linker Flags**設定を探し、`-ObjC` フラグを追加します。<br><br>
8. Content Cardsとアプリ内メッセージングが正しく機能するには、`SDWebImage` フレームワークが必要です。`SDWebImage` はGIFを含む画像のダウンロードと表示に使用されます。Content Cardsまたはアプリ内メッセージを使用する場合は、SDWebImageの統合手順に従ってください。

### SDWebImage統合 {#sdwebimage-integration}

`SDWebImage` をインストールするには、[手順](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework)に従い、生成された `XCFramework` をプロジェクトにドラッグ＆ドロップしてください。

### オプションの位置情報の追跡 {#optional-location-tracking}

1. `CoreLocation.framework` を追加して位置情報の追跡を有効にします。
2. アプリで `CLLocationManager` を使用してユーザーの位置情報を認証する必要があります。

## ステップ 3:Objective-Cブリッジヘッダー {#step-3-objective-c-bridging-header}

{% alert note %}
プロジェクトでObjective-Cのみを使用する場合は、このステップをスキップしてください。
{% endalert %}

プロジェクトでSwiftを使用している場合は、ブリッジヘッダーファイルが必要になります。

ブリッジヘッダーファイルがない場合は、**File > New > File > (iOS or OS X) > Source > Header File** を選択して作成し、`your-product-module-name-Bridging-Header.h` という名前を付けます。次に、ブリッジヘッダーファイルの先頭に次のコード行を追加します。
```
#import "AppboyKit.h"
```

プロジェクトの**Build Settings**で、ヘッダーファイルの相対パスを `Swift Compiler - Code Generation` の下の `Objective-C Bridging Header` ビルド設定に追加します。

## 次のステップ {#next-steps}

手順に従って[統合を完了]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration)してください。