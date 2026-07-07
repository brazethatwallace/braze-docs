---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2019年4月のリリースノートが含まれています。"
---

# 2019年4月 {#april-2019}

## Currentsの新しいイベントとフィールド {#new-currents-events-fields}

セクションの修正に加えて、新しい[サブスクリプションイベント]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events)がMessage Engagement Eventsページに追加されました。

サブスクリプショングループの状態変更データを、Brazeから[セグメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details)と[mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/)にエクスポートできるようになりました。また、[Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)にはそのデータに加えてインストールアトリビューションイベントもエクスポートできます。

また、利用可能な[コンバージョンイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events)にプロパティ`canvas_step_id`が追加されました。

{% alert important %}
これらの更新を活用するには、Currentsコネクターの設定を編集し、使用するイベントを有効にする必要があります。ご不明な点がある場合は、アカウントマネージャーにお問い合わせください。
{% endalert %}

## サブスクリプショングループのアーカイブ {#subscription-groups-archiving}

[サブスクリプショングループのアーカイブ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)が可能になりました！アーカイブされたサブスクリプショングループは編集できず、セグメントフィルターに表示されなくなります。メール、キャンペーン、またはキャンバスでセグメントフィルターとして使用されているグループをアーカイブしようとすると、エラーメッセージが表示され、そのグループの使用をすべて削除するまでアーカイブできません。