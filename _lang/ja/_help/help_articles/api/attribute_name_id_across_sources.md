---
nav_title: Brazeにおけるキャンペーンとキャンバスの属性の違い
article_title: Brazeにおけるキャンペーンとキャンバスの属性の違い
page_order: 1

page_type: reference
description: "このヘルプ記事では、Brazeのソースごとにキャンペーンとキャンバスの属性名およびIDを比較します。"
platform: API
---

# Brazeのソースによるキャンペーンとキャンバスの属性の違い {#how-campaign-and-canvas-attributes-differ-across-sources-in-braze}

キャンペーン、キャンバス、キャンバスステップの名前とIDはすべて、Liquid、REST API、Currentsで利用できます。これらの属性は3つのソースすべてで同じ値にマッピングされますが、名前が異なる場合があります。このページは、3つのソース間の関連性を理解するのに役立ちます。

## ユースケース {#use-cases}

### Liquid

キャンペーンおよびキャンバスの属性は、ダッシュボードで{% raw %}（`{{campaign.${api_id}}}` など）{% endraw %}Liquidタグとして利用できます。Liquidを使用して、これらの属性をメッセージ自体、コネクテッドコンテンツの呼び出し、またはキーと値のペアとして渡すことができます。これは通常、トラッキングの目的で行われます。

### REST API

キャンペーンとキャンバスの属性は、[キャンペーンの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)や[キャンバスの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)でも利用できます。REST APIを使用してマッピング（すべてのキャンバス名と対応するIDのリスト）を構築できます。

### Currents

キャンペーンとキャンバスの属性は、Currentsの[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)に関連付けられています。メッセージステップのみがキャンペーン属性にアクセスでき、その他のキャンバスステップはキャンバス属性にのみアクセスできる点に注意してください。これは、プッシュ送信やメール開封がどのキャンペーンまたはキャンバスコンポーネントに関連付けられているかを特定するために重要です。

## キャンペーン属性 {#campaign-attributes}

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| キャンペーン名 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Campaign ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | 該当なし（API呼び出し自体の入力として使用されます） | campaign_id |
| バリアント名 | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | 該当なし（キャンペーンの詳細エクスポートエンドポイントを使用してバリアント名をバリアントIDにマッピングします） |
| バリアントID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="キャンペーン attributes" }

## キャンバス属性 {#canvas-attributes}

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| キャンバス名 | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | 該当なし（API呼び出し自体の入力として使用されます） | canvas_id |
| バリアント名 | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| バリアントID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| ステップ名（メッセージステップのみ） | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ステップID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| メッセージチャネル | 該当なし | `steps.messages.message_variation_id.channel` | 該当なし（プッシュ送信やメール開封など、イベントタイプに固有です） |
| メッセージID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="キャンバス attributes" }