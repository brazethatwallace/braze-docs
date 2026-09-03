---
nav_title: プッシュ通知
article_title: Braze SDKを通じてプッシュ通知データをログに記録する
page_order: 7.2
description: "Braze SDKを通じてプッシュ通知データをログに記録する方法を説明します。"
noindex: true
---

# プッシュ通知データをログに記録する {#log-push-notification-data}

> Braze SDKを通じてプッシュ通知データをログに記録する方法を説明します。

{% sdktabs %}
{% sdktab android %}
## Braze APIを使用したデータのログ記録（推奨） {#logging-data-with-the-braze-api-recommended}

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を呼び出すことで、リアルタイムで分析データをログに記録できます。分析データをログに記録するには、Brazeダッシュボードから`braze_id`の値を送信して、更新するユーザープロファイルを特定します。

![パーソナライズされたプッシュダッシュボードの例]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## 手動でデータをログに記録する {#manually-logging-data}

ペイロードの詳細に応じて、`FirebaseMessagingService.onMessageReceived`の実装内またはスタートアップアクティビティ内で手動で分析データをログに記録できます。`FirebaseMessagingService`のサブクラスは、Androidシステムによって[フラグ付けまたは終了](https://firebase.google.com/docs/cloud-messaging/android/receive)されないよう、呼び出しから9秒以内に実行を完了する必要があります。

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}