---
nav_title: ユーザープロファイル
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Brazeが追跡し、Currentsを使用して選択したデータウェアハウスに送信できるユーザープロファイルの更新を一覧にしています。"
tool: Currents
search_rank: 7
---

{% alert tip %}
これらのイベントは、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/query_builder/)、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)、および[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)でSQLテーブルとしても利用できます。SQLテーブルスキーマとカラムの詳細については、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables/)を参照してください。
{% endalert %}

追加のイベント権限へのアクセスが必要な場合は、Brazeの担当者に連絡するか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。このページで必要な情報が見つからない場合は、[顧客行動イベントライブラリー]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)、[メッセージエンゲージメントイベントライブラリー]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)、または[Currentsサンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)を参照してください。

{% details ユーザープロファイル更新イベント構造の説明 %}

### イベント構造 {#event-structure}

この顧客行動およびユーザーイベントの内訳は、ユーザープロファイル更新イベントに一般的に含まれる情報の種類を示しています。そのコンポーネントをしっかり理解することで、開発者やビジネスインテリジェンス戦略チームは、受信したCurrentsイベントデータを使用してデータドリブン型のレポートやチャートを作成し、その他の貴重なデータ指標を活用できます。

{% alert important %}
ストレージスキーマは、Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storageなどのデータウェアハウスストレージパートナーに送信されるフラットファイルイベントデータに適用されます。ここに記載されているイベントと送信先の組み合わせの一部は、まだ一般提供されていない場合があります。パートナーごとのサポート対象イベントについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)および関連するパートナーページを参照してください。

Currentsは、ペイロードが900KBを超えるイベントを破棄します。
{% endalert %}