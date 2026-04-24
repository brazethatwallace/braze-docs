---
nav_title: メッセージエンゲージメントイベント
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Braze が追跡し、Currents を使用して選択したデータウェアハウスに送信できるさまざまなメッセージエンゲージメントイベントを一覧にしています。"
tool: Currents
search_rank: 6
---

ストレージスキーマは、データウェアハウスストレージパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルイベントデータに適用されます。他のパートナーに適用されるスキーマについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。

{% alert tip %}
これらのイベントは、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder/)、[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/)、および [Snowflake データ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)で SQL テーブルとしても利用できます。SQL テーブルスキーマとカラムの詳細については、[SQL テーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/)を参照してください。
{% endalert %}

追加のイベント権限へのアクセスが必要な場合は、アカウントマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。この記事で必要な情報が見つからない場合は、[顧客行動イベントライブラリー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)または [Currents サンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご覧ください。

{% details メッセージエンゲージメントイベントの構造とプラットフォーム値の説明 %}

### イベントの構造

このイベントの内訳は、メッセージエンゲージメントイベントに一般的に含まれる情報のタイプを示しています。構成要素をしっかり理解することで、開発者やビジネスインテリジェンス戦略チームは、受信した Currents イベントデータを使用してデータドリブン型のレポートやグラフを作成し、その他の貴重なデータ指標を活用できます。

![メッセージエンゲージメントイベントの内訳。メール配信停止イベントを示し、リストされたプロパティはユーザー固有のプロパティ、キャンペーンまたはキャンバストラッキングプロパティ、イベント固有のプロパティごとにグループ化されています。]({% image_buster /assets/img/message_engagement_event.png %})

メッセージエンゲージメントイベントは、**ユーザー固有**のプロパティ、**キャンペーン / キャンバストラッキング**プロパティ、および**イベント固有**のプロパティで構成されます。

### ユーザー ID スキーマ

ユーザー ID の命名規則に注意してください。

| Braze スキーマ | Currents スキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze によって自動的に割り当てられるユニークな識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されたユーザープロファイルのユニークな識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### プラットフォームの値

特定のイベントは、ユーザーのデバイスのプラットフォームを示す `platform` 値を返します。
<br>次の表に、返される可能性のある値の詳細を示します。

| ユーザーデバイス | プラットフォーム値 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents は、900&nbsp;KB を超える過度に大きなペイロードを持つイベントをドロップします。
{% endalert %}

{% alert note %}
キャンバスフローに関連するオブジェクトには、グループ化に使用できる ID があり、[キャンバスの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)を通じて人間が読める名前に変換できます。
{% endalert %}

{% alert note %}
キャンペーンやキャンバスの更新後、特定のフィールドが最新の状態を表示するまでに時間がかかる場合があります。対象のフィールドは以下のとおりです。
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
完全な一貫性が必要な場合は、これらのフィールドの最終更新から1時間待ってからユーザーにメッセージを送信することをお勧めします。
{% endalert %}