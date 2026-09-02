---
nav_title: ディスパッチ ID
article_title: ディスパッチ IDの動作
page_order: 5.2
page_type: reference
description: "このリファレンス記事では、キャンペーン、キャンバス、Liquid、Currentsにおけるディスパッチ IDの動作について説明します。"
---

# ディスパッチ IDの動作 {#dispatch-id-behavior}

> `dispatch_id` は、Brazeから送信される各メッセージディスパッチ（「送信」）に固有のIDです。

## キャンペーンにおけるディスパッチ ID の動作 {#dispatch-id-behavior-in-campaigns}

スケジュールされたキャンペーンメッセージには、同じ `dispatch_id` が割り当てられます。アクションベースまたは API トリガーのキャンペーンメッセージには、ユーザーごとに一意の `dispatch_id` が割り当てられる場合や、近接したタイミングまたは同じ API コールで送信された場合には複数のユーザーに同じ `dispatch_id` が割り当てられる場合があります。たとえば、スケジュールされたキャンペーンのオーディエンスに含まれる 2 人のユーザーは、キャンペーンがスケジュールされるたびに同じ `dispatch_id` を持ちます。一方、API トリガーのキャンペーンのオーディエンスに含まれる 2 人のユーザーは、キャンペーンが別々の API コールで送信され、互いに近接したタイミングでなかった場合、異なるディスパッチ ID を持つ可能性があります。

マルチチャネルキャンペーンでも、配信タイプに応じて同様の動作になります。

{% alert warning %}
Brazeはキャンバスステップを「スケジュールされた」ものであってもトリガーイベントとして扱うため、すべてのキャンバスステップに対して `dispatch_id` がランダムに生成されます。これにより、ID の生成に不整合が生じる場合があります。キャンバスコンポーネントが送信ごとにユーザーごとの一意の `dispatch_id` を持つこともあれば、送信ごとにユーザー間で共有されるディスパッチ ID を持つこともあります。
{% endalert %}

## メッセージ内でLiquidを使用してディスパッチIDをテンプレート化する {#template-dispatch-id-into-messages-with-liquid}

メッセージ内から（URLなどで）メッセージのディスパッチを追跡したい場合、`dispatch_id`をテンプレート化できます。このフォーマットは、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)のリストにあるキャンバス属性の項目で確認できます。

この動作は`api_id`と同様です。`api_id`はキャンペーン作成時に利用できないため、Brazeはプレースホルダーとしてテンプレート化し、プレビューでは`dispatch_id_for_unsent_campaign`と表示されます。IDはメッセージの送信前に生成され、送信時に含まれます。

{% alert warning %}
`dispatch_id_for_unsent_campaign`のLiquidテンプレート化は、アプリ内メッセージでは機能しません。アプリ内メッセージには`dispatch_id`がないためです。
{% endalert %}

## メールのディスパッチID Currentsフィールド {#dispatch-id-currents-field-for-email}

`dispatch_id`フィールドは、すべてのコネクタータイプにわたるCurrentsメールイベントで利用できます。`dispatch_id`は、Brazeプラットフォームから送信される各トランスミッション（ディスパッチ）ごとに生成される一意のIDです。

スケジュールされたメッセージを受信するすべての顧客は同じ`dispatch_id`を取得しますが、アクションベースまたはAPIトリガーのメッセージを受信する顧客は、メッセージごとに一意の`dispatch_id`を取得します。`dispatch_id`フィールドを使用すると、定期的なキャンペーンのどのインスタンスがコンバージョンに寄与したかを特定でき、どのタイプのキャンペーンが成果を生み出しているかを確認できます。

`dispatch_id`は、[パーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)で使用できるほか、Currentsで[セグメント]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)、[Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel#supported-currents-events)、または[Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)を使用する場合にも利用できます。