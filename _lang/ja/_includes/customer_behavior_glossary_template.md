---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: 顧客行動とユーザーイベント
article_title: 顧客行動とユーザーイベント
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Brazeが追跡し、Currentsを使用して選択したデータウェアハウスに送信できるさまざまな顧客行動イベントとユーザーイベントを一覧にしています。"
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details スキーマの範囲と関連リソース %}

ストレージスキーマは、データウェアハウスストレージパートナー（Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage）に送信するフラットファイルイベントデータに適用されます。ここに記載されているイベントと送信先の組み合わせの一部は、まだ一般提供されていません。各パートナーがサポートしているイベントについては、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)の一覧を参照し、それぞれのページをご確認ください。

{% alert tip %}
これらのイベントは、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)、および[Snowflakeデータシェアリング]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)でSQLテーブルとしても利用できます。SQLテーブルスキーマとカラムの詳細については、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。
{% endalert %}

追加のイベントエンタイトルメントへのアクセスが必要な場合は、Brazeの担当者に連絡するか、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。このページで必要な情報が見つからない場合は、[メッセージエンゲージメントイベントライブラリ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)または[Currentsサンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご確認ください。

{% enddetails %}

{% details 顧客行動とユーザーイベントの構造およびプラットフォーム値の説明 %}

## イベント構造 {#event-structure}

この顧客行動とユーザーイベントの内訳は、顧客行動またはユーザーイベントに一般的に含まれる情報の種類を示しています。その構成要素をしっかり理解することで、開発者やビジネスインテリジェンス戦略チームは、受信したCurrentsイベントデータを使用してデータドリブン型のレポートやチャートを作成し、その他の貴重なデータ指標を活用できます。

![ユーザー固有のプロパティ、行動固有のプロパティ、デバイス固有のプロパティごとにグループ化された購入イベントを示すユーザーイベントの内訳]({% image_buster /assets/img/customer_engagement_event.png %})

顧客行動とユーザーイベントは、**ユーザー固有**のプロパティ、**行動固有**のプロパティ、および**デバイス固有**のプロパティで構成されています。

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

{% details 顧客行動とユーザーイベントに関する考慮事項 %}

- Currentsは、900&nbsp;KBを超える過度に大きなペイロードを持つイベントをドロップします。
- この用語集のイベントの多くはSDKによって開始されます。`token_state_change`などの一部のイベントは、SDKまたはバックエンドのいずれかによって開始される場合があります（たとえば、プッシュバウンスへの応答として）。`sdk_version`、`gender`、`language`、`country`フィールドは、SDKによって開始されたイベントに対してのみ設定されます。バックエンドによって開始されたイベント、またはその情報が利用できないかユーザーに設定されていない場合、これらのフィールドは`null`になることがあります。

{% enddetails %}

</div>

<!--overview-end-->