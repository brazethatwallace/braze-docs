---
nav_title: ディスパッチ ID
article_title: ディスパッチ ID の動作
page_order: 5.2
page_type: reference
description: "このリファレンス記事では、Campaigns、Canvas、Liquid、Currentsにおけるディスパッチ ID の動作について説明します。"
---

# ディスパッチ ID の動作 {#dispatch-id-behavior}

> `dispatch_id` は、Brazeから送信される各メッセージディスパッチ（「送信」）に固有の ID です。

## Campaignsでのディスパッチ ID の動作 {#dispatch-id-behavior-in-campaigns}

スケジュールされたCampaignメッセージには同じ `dispatch_id` が割り当てられます。アクションベースまたは APIトリガーのCampaignメッセージには、ユーザーごとに一意の `dispatch_id` が割り当てられる場合もあれば、近接して送信された場合や同一の API 呼び出しで送信された場合には複数のユーザー間で同じ `dispatch_id` が共有される場合もあります。例えば、スケジュールされたCampaignオーディエンス内の2人のユーザーには、Campaignがスケジュールされるたびに同じ `dispatch_id` が割り当てられます。ただし、APIトリガーCampaignのオーディエンスに含まれる2人のユーザーは、別々の API 呼び出しで送信され、互いに近接していない場合、異なるディスパッチ ID が割り当てられることがあります。

マルチチャネルCampaignsの動作は、配信タイプの説明と同じになります。

{% alert warning %}
BrazeはCanvasステップが「スケジュール」されている場合でもCanvasステップをトリガーされたイベントとして扱うため、すべてのCanvasステップに対して `dispatch_id` がランダムに生成されます。これにより、ID の生成に不整合が生じる可能性があります。Canvasコンポーネントには各送信でユーザーごとに一意の `dispatch_id` が割り当てられることもあれば、各送信においてユーザー間でディスパッチ ID が共有されることもあります。
{% endalert %}

## Liquidでディスパッチ ID をメッセージにテンプレート化する {#template-dispatch-id-into-messages-with-liquid}

（URL などで）メッセージ内からのメッセージのディスパッチを追跡する場合は、`dispatch_id` でテンプレート化できます。このための書式設定は、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)のリストにあるCanvas属性の項目で確認できます。

これは `api_id` と同様に動作します。`api_id` はCampaign作成時には利用できないため、Brazeはプレースホルダーとしてテンプレート化し、`dispatch_id_for_unsent_campaign` としてプレビューされます。この ID はメッセージの送信前に生成され、送信時に含まれます。

{% alert warning %}
アプリ内メッセージには `dispatch_id` がないため、`dispatch_id_for_unsent_campaign` のLiquidテンプレートはアプリ内メッセージでは機能しません。
{% endalert %}

## メールのディスパッチ ID Currentsフィールド {#dispatch-id-currents-field-for-email}

`dispatch_id` フィールドは、すべてのコネクタータイプのCurrentsメールイベントで利用できます。`dispatch_id` は、Brazeプラットフォームから送信される各送信（ディスパッチ）に対して生成される一意の ID です。

スケジュールされたメッセージが送信されたすべての顧客には同じ `dispatch_id` が割り当てられますが、アクションベースまたは APIトリガーのメッセージを受信した顧客にはメッセージごとに一意の `dispatch_id` が割り当てられます。`dispatch_id` フィールドを使用すると、定期Campaignのどのインスタンスがコンバージョンに寄与したかを特定できるため、どのタイプのCampaignsが成果を上げているかを確認できます。

`dispatch_id` は、[パーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#supported-personalization-tags)、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、またはCurrentsで[Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents#integration-details)、[Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents#email-events)、[Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)を使用する際に利用できます。