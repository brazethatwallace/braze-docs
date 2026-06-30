---
page_order: 10.9
nav_title: トラブルシューティング
article_title: Braze SDKのプッシュ通知のトラブルシューティング
channel:
  - push notifications
---

# プッシュ通知のトラブルシューティング {#troubleshoot-push-notifications}

> Braze SDKのプッシュ通知のトラブルシューティング方法について説明します。

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/push_notifications/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}

## プッシュ通知の改行 {#push-linebreaks}

Liquidタグを使用してプッシュ通知を作成する場合、Liquidタグに隣接する改行はメッセージ送信前に自動的に削除されます。[プッシュ通知コンポーザー]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)では、編集中にメッセージが読みやすいようにこれらの改行が再追加されます。メッセージを保存する際にLiquidタグの前後に改行が表示される場合、これは想定どおりの動作です。