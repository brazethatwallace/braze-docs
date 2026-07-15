---
nav_title: "メッセージタイプ"
article_title: プッシュメッセージタイプ
page_order: 3
page_type: reference
description: "このリファレンス記事では、Brazeで送信できるさまざまなタイプのプッシュ通知について説明します。"
channel: push
---

# プッシュメッセージタイプ {#push-message-types}

> プッシュ通知には、顧客とやり取りするために使用できるさまざまなタイプがあります。これらの設定のほとんどはプッシュキャンペーンで構成できますが、説明に記載されているように、一部はバックエンドの設定が必要です。

## 標準プッシュ {#standard-push}

包括的なプッシュメッセージです。通知音とメッセージとともにユーザーのデバイスに表示され、スライドインしたり、通知バーやスタックに表示されたりします。

**対応プラットフォーム:** Web、Android、iOS

詳細については、[プッシュメッセージの作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)を参照してください。

## Webプッシュ {#web-push}

これらのプッシュメッセージは、Webアプリまたはブラウザに表示されます。顧客に到達するには許可が必要です。Webプッシュは、ユーザーがシークレットブラウザを使用している場合は機能しません。

**対応プラットフォーム:** Web

詳細については、[Webプッシュ通知]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)を参照してください。

## プッシュプライマーキャンペーン {#push-primer-campaigns}

プッシュのオプトインまたはオプトアウトの明示的なシグナルをユーザーから取得するために使用されるアプリ内メッセージキャンペーンです。プライマーを通じて、デバイス設定でプッシュをオフにする可能性が高いユーザーへの通知送信を回避できます。iOSの場合、フォアグラウンドプッシュ通知（デバイスを起動する通知など）は、ユーザーがiOSのネイティブプッシュプロンプトに明示的にオプトインするまで有効になりません。そのため、プッシュキャンペーンは重要です。

**対応プラットフォーム:** Web、Android、iOS

詳細については、[プッシュプライマーアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を参照してください。

## Push Stories

Push Storiesは、カルーセル形式のビジュアルジャーニーを通じてユーザーを案内する没入型メッセージです。モバイルデバイスでのみ利用可能です。

**対応プラットフォーム:** iOS、Android

詳細については、[Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)を参照してください。

## アクションボタン付きプッシュ {#push-with-action-buttons}

アクションボタン付きプッシュは、ユーザーにオプションを提供し、複数のコールトゥアクションを提示できるメッセージです。

**対応プラットフォーム:** Web、Android、iOS

詳細については、[プッシュアクションボタン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons)を参照してください。

## リッチプッシュ通知 {#rich-push-notifications}

リッチプッシュ通知は、アイコンやコールトゥアクションテキストを超えて拡張できる没入型の画像やクリエイティブコンテンツを含む通知です。

**対応プラットフォーム:** iOS、Android

詳細については、[iOSのリッチ通知の作成]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)または[Androidのリッチ通知の作成]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)を参照してください。

## iOSの仮承認プッシュ通知 {#provisional-push-notifications-for-ios}

AppleがiOS 12で導入した仮承認は、iOSアプリのインストール時に自動的に行われ、ブランドがプッシュプロンプトを表示せずにサイレント通知を送信できるようにします。サイレントプッシュが送信され、デバイスの通知トレイで表示されると、ユーザーにはプッシュ通知を許可するか停止するかのオプションが提示されます。

**対応プラットフォーム:** iOS

詳細については、[iOS通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push)を参照してください。

## HTMLプッシュ通知 {#html-push-notifications}

HTMLプッシュ通知は、HTMLでハードコードされたプッシュメッセージであり、Brazeが提供するプリセットのプッシュテンプレートを使用しません。HTMLプッシュ通知を作成するオプションがあることで、会社はプッシュメッセージの外観について完全なクリエイティブの自由と一貫したブランディングを実現できます。

**対応プラットフォーム:** Android

## 通知IDとチャネルID {#notification-ids-and-channel-ids}

通知IDとチャネルIDを使用すると、ユーザーが受信済みだが未開封のプッシュ通知を置き換えたり更新したりできます。

**対応プラットフォーム:** iOS、Android

詳細については、[通知チャネル]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels)および[高度なプッシュキャンペーン設定]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings)を参照してください。

## バックグラウンドまたはサイレントプッシュ通知 {#background-push-notifications}

デバイスにレンダリングされないプッシュ通知です。通常、バックグラウンドプロセスやアンインストール追跡のためにアプリに情報パケットを送信するために使用されます。バックグラウンドまたはサイレントプッシュを送信するには、バックグラウンド対応のプッシュトークンが必要です。

**対応プラットフォーム:** Web、Android、iOS

詳細については、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent)を参照してください。

## ウェアラブルプッシュ通知 {#wearable-push-notifications}

これらのプッシュ通知により、ブランドはApple Watchなどのウェアラブルデバイスに直接メッセージを送信できます。

**対応プラットフォーム:** iOS