---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: メッセージエンゲージメントイベント
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Brazeがトラッキングし、Currentsを使用して選択したデータウェアハウスに送信できるさまざまなメッセージエンゲージメントイベントを一覧にしています。"
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details スキーマの範囲と関連リソース %}

ストレージスキーマは、データウェアハウスストレージパートナー（Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage）に送信するフラットファイルイベントデータに適用されます。他のパートナーに適用されるスキーマについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)の一覧を参照し、それぞれのページをご確認ください。

{% alert tip %}
これらのイベントは、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)、および[Snowflakeデータシェアリング]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)でSQLテーブルとしても利用できます。SQLテーブルスキーマとカラムの詳細については、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。
{% endalert %}

追加のイベント権限へのアクセスが必要な場合は、アカウントマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。この記事で必要な情報が見つからない場合は、[顧客行動イベントライブラリ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)または[Currentsサンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご確認ください。

{% enddetails %}

{% details メッセージエンゲージメントイベントの構造とプラットフォーム値の説明 %}

## イベント構造 {#event-structure}

このイベントの内訳は、メッセージエンゲージメントイベントに一般的に含まれる情報の種類を示しています。その構成要素をしっかり理解することで、開発者やビジネスインテリジェンス戦略チームは、受信したCurrentsイベントデータを使用してデータドリブン型のレポートやチャートを作成し、その他の貴重なデータ指標を活用できます。

![メッセージエンゲージメントイベントの内訳。メール購読解除イベントを示し、リストされたプロパティがユーザー固有のプロパティ、キャンペーンまたはキャンバスのトラッキングプロパティ、イベント固有のプロパティにグループ化されています]({% image_buster /assets/img/message_engagement_event.png %}){: width="2300" height="770" style="max-width:100%;height:auto;"}

メッセージエンゲージメントイベントは、**ユーザー固有**のプロパティ、**キャンペーン/キャンバスのトラッキング**プロパティ、および**イベント固有**のプロパティで構成されています。

### ユーザーIDスキーマ {#user-id-schema}

ユーザーIDの命名規則に注意してください。

| Brazeスキーマ | Currentsスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されるユーザープロファイルの一意の識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーIDスキーマ" }

### プラットフォーム値 {#platform-values}

一部のイベントは、ユーザーのデバイスのプラットフォームを指定する`platform`値を返します。
<br>次の表は、返される可能性のある値の詳細を示しています。

| ユーザーデバイス | プラットフォーム値 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プラットフォーム値" }

{% enddetails %}

{% details メッセージエンゲージメントイベントに関する考慮事項 %}

- Currentsは、ペイロードが900&nbsp;KBを超えるイベントをドロップします。
- キャンバスフローに関連するオブジェクトには、グループ化に使用でき、[キャンバス詳細エクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)を通じて人間が読める名前に変換できるIDがあります。
- キャンペーンまたはキャンバスを更新した直後に、特定のフィールドが最新の状態を表示しない場合があります：
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- これらのフィールドの完全な一貫性が必要な場合は、最後の更新から1時間待ってからユーザーにメッセージを送信してください。

{% enddetails %}

</div>

<!--overview-end-->