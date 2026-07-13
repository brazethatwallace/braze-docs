---
nav_title: 単体テスト (オプション)
article_title: iOS のプッシュ通知単体テスト
platform: iOS
page_order: 29.5
description: "この参考記事では、iOS プッシュ実装のオプションの単体テストを実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 単体テスト {#unit-tests}

このオプションガイドでは、アプリデリゲートが[プッシュ統合手順]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)に記載されているステップに正しく従っているかどうかを検証するいくつかの単体テストを実装する方法について説明します。

すべてのテストに合格した場合、通常はプッシュ設定のコードベース部分が正しく機能していることを意味します。テストが失敗した場合は、ステップを誤って実行したか、有効なカスタマイズがデフォルトの手順と正確に一致していないことが原因である可能性があります。

いずれにせよ、これは統合ステップに従っていることを確認し、リグレッションを監視するのに役立つアプローチです。

## ステップ 1: 単体テストターゲットの作成 {#step-1-creating-a-unit-tests-target}

Xcodeのアプリプロジェクトにすでに単体テストバンドルが含まれている場合は、このステップをスキップしてください。

アプリプロジェクトで、メニューの **File > New > Target** に移動し、新しい「Unit Testing Bundle」を追加します。このバンドルではObjective-CまたはSwiftを使用でき、任意の名前を付けることができます。「Target to be Tested」をメインのアプリターゲットに設定します。

## ステップ 2: Braze SDKを単体テストに追加する {#step-2-add-the-braze-sdk-to-your-unit-tests}

最初に[Braze SDKをインストール]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)するために使用したのと同じ方法を使用して、同じSDKインストールが単体テストのターゲットでも使用できることを確認します。たとえば、CocoaPodsを使用する場合は次のようになります。

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## ステップ 3: OCMockを単体テストに追加する {#step-3-add-ocmock-to-your-unit-tests}

CocoaPods、Carthage、またはその静的ライブラリーを介して[OCMock](https://ocmock.org/)をテストターゲットに追加します。たとえば、CocoaPodsを使用する場合は次のようになります。

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## ステップ 4: 追加したライブラリーのインストールを完了する {#step-4-finish-installing-the-added-libraries}

Braze SDKとOCMockのインストールを完了します。たとえば、CocoaPodsを使用して、ターミナルでXcodeアプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。

```
pod install
```

この時点で、CocoaPodsによって作成されたXcodeプロジェクトワークスペースを開くことができるはずです。

## ステップ 5: プッシュテストの追加 {#step-5-adding-push-tests}

単体テストのターゲットに新しいObjective-Cファイルを作成します。

単体テストのターゲットがSwiftの場合、Xcodeは「Would you like to configure an Objective-C bridging header?」と尋ねることがあります。ブリッジングヘッダーはオプションであるため、**Don't Create** をクリックしてもこれらの単体テストを正常に実行できます。

HelloSwiftサンプルアプリの[`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m)のコンテンツを新しいファイルに追加します。

## ステップ 6: テストスイートを実行する {#step-6-run-test-suite}

アプリの単体テストを実行します。これは1回限りの検証ステップにすることも、リグレッションを検出するためにテストスイートに無期限に含めることもできます。