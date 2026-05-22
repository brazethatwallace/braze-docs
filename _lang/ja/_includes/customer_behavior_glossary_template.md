---
nav_title: 顧客行動とユーザーイベント
article_title: 顧客行動とユーザーイベント
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "この用語集には、BrazeがCurrentsを使用して追跡し、選択したデータウェアハウスに送信できるさまざまな顧客行動とユーザーイベントがリストされています。"
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details スキーマの範囲と関連リソース %}

ストレージスキーマは、データウェアハウスのストレージパートナー（Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage）に送信するフラットファイルのイベントデータに適用されます。ここにリストされているイベントと送信先の組み合わせの中には、まだ一般提供されていないものもあります。さまざまなパートナーがサポートするイベントの情報については、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。

{% alert tip %}
これらのイベントは、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder/)、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/)、および[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)でSQLテーブルとしても利用できます。SQLテーブルスキーマとカラムの詳細については、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/)を参照してください。
{% endalert %}

追加のイベントエンタイトルメントへのアクセスが必要な場合は、Brazeの担当者に問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。このページで必要なものが見つからない場合は、[メッセージエンゲージメントイベントライブラリー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)や[Currentsのサンプルデータ例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご覧ください。

{% enddetails %}

{% details 顧客行動とユーザーイベントの構造およびプラットフォーム値の説明 %}

### イベントの構造 {#event-structure}

この顧客行動とユーザーイベントの内訳は、一般的に顧客行動やユーザーイベントに含まれる情報のタイプを示しています。開発者とビジネスインテリジェンス戦略チームは、構成要素をしっかり理解したうえで、受信したCurrentsイベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。

![ユーザーイベントの内訳。購入イベントを示し、リストされたプロパティはユーザー固有のプロパティ、動作固有のプロパティ、デバイス固有のプロパティごとにグループ分けされている]({% image_buster /assets/img/customer_engagement_event.png %})

顧客行動およびユーザーイベントは、**ユーザー固有**のプロパティ、**動作固有**のプロパティ、および**デバイス固有**のプロパティで構成されます。

### プラットフォームの値 {#platform-values}

特定のイベントは、ユーザーのデバイスのプラットフォームを示す`platform`値を返します。
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Platform values" }

{% enddetails %}

{% details 顧客行動とユーザーイベントに関する考慮事項 %}

- Currentsは900&nbsp;KBを超える過度に大きいペイロードを持つイベントをドロップします。
- この用語集に含まれるイベントの多くはSDKによって開始されます。`token_state_change`などの一部のイベントは、SDKまたはバックエンドのいずれかによって開始される場合があります（例えば、プッシュバウンスへの応答として）。`sdk_version`、`gender`、`language`、`country`フィールドはSDKによって開始されたイベントでのみ設定されます。バックエンドによって開始されたイベントの場合、またはその情報が利用できないかユーザーに設定されていない場合、これらのフィールドは`null`になることがあります。

{% enddetails %}

</div>

<!--overview-end-->