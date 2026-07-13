---
nav_title: "通知オプション"
article_title: Android通知オプション
page_order: 2
page_type: reference
description: "このリファレンス記事では、Androidの通知オプションと、Braze キャンペーンでの最適な使用方法について説明します。"

platform: Android
channel:
  - Push

---

# 通知オプション {#notification-options}

> これらは、Brazeで利用可能なAndroid固有のプッシュ通知オプションの一部です。

## サイレント通知 {#silent-notifications}

[プッシュ通知メッセージを作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message?tab=android#step-4-compose-your-push-message)する際、タイトルなしでAndroidプッシュメッセージを送信することは**できません**。ただし、代わりにスペースを1つ入力することができます。メッセージにスペース1つしか含まれていない場合、サイレントプッシュ通知として送信されることに注意してください。詳細については、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android)を参照してください。

## 通知グループ {#notification-groups}

メッセージをカテゴリ分けし、ユーザーの通知トレイでグループ化したい場合は、Brazeを通じてAndroidの通知チャネル機能を活用できます。

まず、Androidプッシュキャンペーンを作成し、**作成**タブの上部にある**Notification Channel**ドロップダウンを確認します。

![Androidプッシュキャンペーンの作成タブ上部にあるNotification Channelドロップダウン。]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

ドロップダウンからNotification Channelを選択します。Notification Channelの設定が正常に機能しない場合に備えて、フォールバックチャネルも選択する必要があります。

ここに[Notification Channel]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels)が表示されていない場合は、Notification Channel IDを使用して追加できます。開発者に連絡して、Notification Channel IDを確認するか、必要に応じて新しいIDを作成してもらってください。

Notification Channelに通知IDを追加するには、**Notification Channel**ドロップダウンメニューの**Manage Notification Channel**をクリックし、必須フィールドに入力します。Notification Channelは、Brazeプラットフォームで使用する前にアプリ上で定義されている必要があります。

![Notification Channelドロップダウンメニューの「Manage Notification Channel」をクリックし、必須フィールドに入力してNotification Channelに通知IDを追加する画面。Notification Channelは、Brazeプラットフォームで使用する前にアプリ上で定義されている必要があります。]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }