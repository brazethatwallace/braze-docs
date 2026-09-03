---
nav_title: サンプルアプリ
article_title: iOS 用サンプルアプリ
platform: iOS
page_order: 9
description: "この参照記事では、iOS サンプルアプリについて説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# サンプルアプリ {#sample-apps}

Braze SDKにはそれぞれ、利便性を高めるためにリポジトリ内にサンプルアプリケーションが付属しています。これらのアプリはそれぞれ完全にビルド可能であるため、独自のアプリケーション内で実装すると同時に、Brazeの機能をテストできます。ご自身のアプリケーション内での動作のテストと、サンプルアプリケーション内での予期される動作やコードパスとの比較は、問題が発生した場合にデバッグするための優れた方法です。

## テストアプリケーションのビルド {#building-test-applications}
[iOS SDK GitHubリポジトリ](https://github.com/appboy/appboy-ios-sdk)には、いくつかのテストアプリケーションが用意されています。以下の手順に従って、テストアプリケーションをビルドし、実行してください。

1. 新しい[ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces)を作成し、アプリ識別子APIキーをメモします。
2. `AppDelegate.m`ファイルの適切なフィールドにAPIキーを入力します。

iOSテストアプリケーションのプッシュ通知には、追加の設定が必要です。詳細については、[iOSプッシュ通知の統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)を参照してください。