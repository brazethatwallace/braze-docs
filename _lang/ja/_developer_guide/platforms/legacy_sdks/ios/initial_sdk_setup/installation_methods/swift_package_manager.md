---
nav_title: Swift Package マネージャー
article_title: iOS 向け Swift Package マネージャー の統合
platform: iOS
page_order: 3
description: "このチュートリアルでは、iOS 用 Swift Package マネージャー を使用した Braze SDKのインストールについて説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Swift Package マネージャー の統合 {#swift-package-manager-integration}

[Swift Package マネージャー](https://swift.org/package-manager/) (SPM) 経由で iOS SDKをインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、Xcode 12 以降を使用していることを確認してください。

{% alert note %}
tvOS は現在、Swift Package マネージャー 経由では利用できません。
{% endalert %}

## ステップ 1:依存関係をプロジェクトに追加する {#step-1-adding-the-dependency-to-your-project}

### SDKバージョンのインポート {#import-sdk-version}

プロジェクトを開き、プロジェクトの設定に移動します。**Swift Packages** タブを選択し、パッケージリストの下にある <i class="fas fa-plus"></i> 追加ボタンをクリックします。

![Swift Packages タブが選択された Xcode プロジェクト設定。]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

SDKバージョン `3.33.1` 以降をインポートする場合、iOS SDKリポジトリのURL (`https://github.com/braze-inc/braze-ios-sdk`) をテキストフィールドに入力し、**Next** をクリックします。

バージョン `3.29.0` から `3.32.0` の場合、URL `https://github.com/Appboy/Appboy-ios-sdk` を使用してください。

![Braze iOS SDKリポジトリURLの Xcode パッケージ依存関係追加ダイアログ。]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

次の画面で、SDKバージョンを選択し、**Next** をクリックします。バージョン `3.29.0` 以降は Swift Package マネージャー と互換性があります。

![Braze iOS SDKの Xcode パッケージバージョン選択画面。]({% image_buster /assets/img/ios/spm/select_version.png %})

### パッケージの選択 {#select-packages}

ニーズに最も適したパッケージを選択し、**Finish** をクリックします。必ず `AppboyKit` または `AppboyUI` のどちらかを選択してください。両方のパッケージを含めると、望ましくない動作が発生する可能性があります。

- `AppboyUI`
  - Brazeが提供するUIコンポーネントを使用する場合に最適です。
  - `AppboyKit` が自動的に含まれます。
- `AppboyKit`
  - Brazeが提供するUIコンポーネント（Content Cards、アプリ内メッセージなど）を使用する必要がない場合に最適です。
- `AppboyPushStory`
  - アプリに Push Stories を統合している場合は、このパッケージを含めます。これはバージョン `3.31.0` 以降でサポートされています。
  - **Add to Target** のドロップダウンで、メインアプリのターゲットの代わりに `ContentExtension` ターゲットを選択してください。

![Braze SDKライブラリターゲットを選択する Xcode パッケージ追加画面。]({% image_buster /assets/img/ios/spm/add_package.png %})

## ステップ 2:プロジェクトの構成 {#step-2-configuring-your-project}

次に、プロジェクトの**ビルド設定**に移動し、`-ObjC` フラグを **Other Linker Flags** 設定に追加します。SDKをさらに統合するには、このフラグを追加し、[エラー](https://developer.apple.com/library/archive/qa/qa1490/_index.html)を解決する必要があります。

![Other Linker Flags フィールドが表示された Xcode ビルド設定。]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
`-ObjC` フラグを追加しない場合、APIの一部が欠落し、動作が未定義になる可能性があります。「unrecognized selector sent to class」などの予期しないエラー、アプリケーションのクラッシュ、その他の問題が発生する可能性があります。
{% endalert %}

## ステップ 3:ターゲットのスキームの編集 {#step-3-editing-the-targets-scheme}
{% alert important %}
Xcode 12.5 以降を使用している場合は、このステップをスキップしてください。
{% endalert %}

Xcode 12.4 以前を使用している場合は、Appboy パッケージを含むターゲットのスキームを編集します（**Product > Scheme > Edit Scheme** メニュー項目）。
1. **Build** メニューを展開し、**Post-actions** を選択します。プラス (+) ボタンを押して、**New Run Script Action** を選択します。
2. **Provide build settings from** ドロップダウンで、アプリのターゲットを選択します。
3.  このスクリプトを開いたフィールドにコピーしてください:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![実行スクリプトビルドフェーズを追加するための Xcode Build Phases メニュー。]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## 次のステップ {#next-steps}

手順に従って[統合を完了]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration)してください。