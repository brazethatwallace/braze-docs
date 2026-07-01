---
nav_title: 高度な設定
article_title: 高度なプッシュ設定
platform: iOS
page_order: 5
description: "この参考記事では、アラートオプション、サウンド、有効期限など、iOSの高度なプッシュ通知設定について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 高度な設定 {#advanced-settings}

プッシュキャンペーンを作成する際、作成ステップで**設定**を選択し、利用可能な高度な設定を表示します。

![Brazeダッシュボードに表示されたiOSプッシュキャンペーンの高度な設定。]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## プッシュのキーと値のペアからデータを抽出する {#extracting-data-from-push-key-value-pairs}

Brazeを使用すると、`extras`として知られるカスタム定義の文字列キーと値のペアを、アプリケーションへプッシュ通知と一緒に送ることができます。エクストラは、ダッシュボードまたはAPIを介して定義でき、プッシュデリゲートの実装に渡される`notification`辞書内のキーと値のペアとして利用できます。

## アラートオプション {#alert-options}

**アラートオプション**チェックボックスをオンにすると、デバイスでの通知の表示方法を調整するためのキーと値のドロップダウンが表示されます。

## コンテンツ利用可能フラグを追加する {#adding-content-available-flag}

新しいコンテンツをバックグラウンドでダウンロードするようデバイスに指示するには、**コンテンツ利用可能フラグを追加**チェックボックスをオンにします。最も一般的には、[サイレント通知]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications)の送信に関心がある場合にチェックできます。

## mutable-contentフラグを追加する {#adding-mutable-content-flag}

**Mutable-Contentフラグを追加**チェックボックスをオンにして、iOS 10以上のデバイスで受信者の高度なカスタマイズを有効にします。このフラグは、このチェックボックスの値に関係なく、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications)を作成するときに自動的に送信されます。

## アプリのバッジ数を更新する {#update-app-badge-count}

バッジ数を更新したい数値を入力するか、Liquid構文を使用してカスタム条件を設定します。また、アプリケーションの`applicationIconBadgeNumber`プロパティやプッシュ通知のペイロードを使って、バッジ数を手動で更新することもできます。詳しくは、[バッジ数]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges)についての専用の記事を参照してください。

## サウンド {#sounds}

ここでは、アプリバンドル内のサウンドファイルへのパスを入力し、プッシュメッセージ受信時に再生するサウンドを指定できます。指定されたサウンドファイルが存在しない場合、またはキーワード「default」が入力された場合、Brazeはデフォルトのデバイスアラートサウンドを使用します。カスタマイズの詳細については、[カスタムサウンド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds)についての専用の記事を参照してください。

## 折りたたみID {#collapse-id}

同様の通知をまとめるには、折りたたみIDを指定します。同一の折りたたみIDを使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。[統合された通知](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)については、Appleのドキュメントを参照してください。

## 有効期限 {#expiry}

**有効期限**チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続を失った場合、Brazeは指定された時間までメッセージの送信を試行し続けます。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。配信前に有効期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されないことに注意してください。