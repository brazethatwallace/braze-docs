---
nav_title: サイレントプッシュ通知
article_title: iOS 向けのサイレントプッシュ通知
platform: iOS
page_order: 4
description: "この参考記事では、iOS アプリケーションでのサイレントプッシュ通知の実装について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# サイレントプッシュ通知 {#silent-push-notifications}

プッシュ通知を使用すると、重要なイベントが発生したときにアプリに通知できます。新しいインスタントメッセージを配信したり、ニュース速報を送信したり、ユーザーのお気に入りのテレビ番組の最新エピソードがオフライン視聴用にダウンロードできるようになったときに、プッシュ通知を送信できます。プッシュ通知は、アラートメッセージやサウンドを含まず、アプリのインターフェイスの更新やバックグラウンド作業のトリガーにのみ使用されるサイレント通知にすることもできます。

プッシュ通知は、バックグラウンドでの取得間の遅延が許容できないような、散発的だが即時に必要なコンテンツに適しています。プッシュ通知は、アプリケーションが必要な場合にのみ起動するため、バックグラウンドでの取得よりもはるかに効率的です。

プッシュ通知にはレート制限があるため、アプリケーションで必要なだけ送信しても構いません。iOSとAPNsサーバーが配信頻度をコントロールするため、送信しすぎても問題が発生することはありません。プッシュ通知がスロットリングされている場合、デバイスが次にキープアライブパケットを送信するか、別の通知を受信するまで遅延する可能性があります。

## サイレントプッシュ通知の送信 {#sending-silent-push-notifications}

サイレントプッシュ通知を送信するには、プッシュ通知ペイロードで `content-available` フラグを `1` に設定します。サイレントプッシュ通知を送信する場合、アプリケーションがイベントを参照できるように、通知ペイロードにデータを含めることもできます。これにより、ネットワークリクエストがいくらか節約され、アプリの応答性が向上する可能性があります。

{% alert warning %}
タイトルと本文の両方を `content-available=1` で付加することは、未定義の動作につながる可能性があるため、推奨されません。通知が本当にサイレントであることを確認するには、`content-available` フラグを `1` に設定するときに、タイトルと本文の両方を除外してください。詳細については、[バックグラウンド更新に関するAppleの公式ドキュメント](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)を参照してください。
{% endalert %}

`content-available` フラグは、Brazeダッシュボードおよび[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging)の[Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object)内で設定できます。

![プッシュコンポーザーの「設定」タブにある「content-available」チェックボックスを表示するBrazeダッシュボード。]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

## サイレントプッシュ通知を使用してバックグラウンド作業をトリガーする {#use-silent-push-notifications-to-trigger-background-work}

サイレントプッシュ通知を使用すると、ユーザーに通知することなく、アプリを「一時停止」または「非実行」状態からウェイクし、コンテンツを更新したり、特定のタスクを実行したりできます。

サイレントプッシュ通知を使用してバックグラウンド作業をトリガーするには、前述の手順に従って、メッセージやサウンドなしで `content-available` フラグを設定します。アプリのバックグラウンドモードを設定して、プロジェクト設定の**Capabilities**タブで `remote notifications` を有効にします。リモート通知は、`content-available` フラグが設定された通常のプッシュ通知です。

![Xcodeの「capabilities」の下に「remote notifications」モードのチェックボックスが表示されています。]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

[アンインストール追跡]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift)では、リモート通知のバックグラウンドモードを有効にする必要があります。

リモート通知バックグラウンドモードが有効になっている場合でも、ユーザーがアプリケーションを強制終了した場合、システムはアプリをバックグラウンドで起動しません。システムによってアプリがバックグラウンドで自動的に起動される前に、ユーザーはアプリケーションを明示的に起動するか、デバイスを再起動する必要があります。

詳細については、[バックグラウンド更新のプッシュ](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc)および [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) を参照してください。

## iOSのサイレント通知の制限事項 {#ios-silent-notifications-limitations}

iOSオペレーティングシステムは、一部の機能の通知をゲートする場合があります。これらの機能で問題が発生している場合は、iOSのサイレント通知ゲートが原因である可能性があることに注意してください。

Brazeには、iOSサイレントプッシュ通知に依存するいくつかの機能があります。

| 機能 | ユーザーエクスペリエンス |
|---|---|
| アンインストール追跡 | ユーザーはサイレントな夜間アンインストール追跡プッシュを受け取ります。|
| ジオフェンス | サーバーからデバイスへのジオフェンスのサイレント同期。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="iOSのサイレント通知の制限事項" }

詳細については、Appleの[インスタンスメソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)および[未受信通知](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23)のドキュメントを参照してください。

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23