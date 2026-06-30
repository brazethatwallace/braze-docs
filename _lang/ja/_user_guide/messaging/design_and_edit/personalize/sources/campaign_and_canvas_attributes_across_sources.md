---
nav_title: ソース間のCampaignおよびCanvas属性
article_title: ソース間のCampaignおよびCanvas属性
page_order: 1.5
page_type: reference
description: "このリファレンス記事では、Liquid、REST API、Currents間でのCampaignおよびCanvasの属性名とIDを比較します。"
---

# ソース間のCampaignおよびCanvas属性 {#campaign-and-canvas-attributes-across-sources}

> Campaign、Canvas、キャンバスステップの名前とIDは、Liquid、Braze REST API、Currentsのすべてで利用できます。これらの属性は3つのソースすべてで同じ値にマッピングされますが、名前が異なる場合があります。このページを使用して、3つのソース間の関連性を把握してください。

## ユースケース {#use-cases}

### Liquid

CampaignおよびCanvasの属性は、ダッシュボードでLiquidタグとして利用できます{% raw %}（`{{campaign.${api_id}}}`など）{% endraw %}。Liquidを使用して、これらの属性をメッセージ自体、コネクテッドコンテンツの呼び出し、またはキーと値のペアとして渡すことができます。これは通常、トラッキング目的で行われます。

### REST API

CampaignおよびCanvasの属性は、[Campaignの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)や[Canvasの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)でも利用できます。Braze REST APIを使用して、マッピング（すべてのCanvas名とそれに対応するIDのリスト）を構築できます。

### Currents

CampaignおよびCanvasの属性は、Currentsの[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)に関連付けられています。メッセージステップのみがCampaign属性にアクセスでき、その他のCanvasステップはCanvas属性にのみアクセスできることに注意してください。これは、プッシュ送信やメール開封がどのCampaignまたはCanvasコンポーネントに関連付けられているかを判断するために重要です。

## Campaign属性 {#campaign-attributes}

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Campaign名 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Campaign ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A（API呼び出し自体の入力として使用） | campaign_id |
| バリアント名 | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A（Campaignの詳細をエクスポートするエンドポイントを使用してバリアント名をバリアントIDにマッピング） |
| バリアントID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaign属性" }

## Canvas属性 {#canvas-attributes}

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Canvas名 | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A（API呼び出し自体の入力として使用） | canvas_id |
| バリアント名 | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| バリアントID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| ステップ名（メッセージステップのみ） | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ステップID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| メッセージチャネル | N/A | `steps.messages.message_variation_id.channel` | N/A（プッシュ送信やメール開封などのイベントタイプに固有） |
| メッセージID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas属性" }