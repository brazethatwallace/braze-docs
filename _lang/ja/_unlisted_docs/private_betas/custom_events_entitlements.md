---
article_title: カスタムイベント
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Brazeラーニングコース]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> この記事では、カスタムイベントとプロパティ、関連するセグメンテーションフィルター、キャンバスエントリプロパティ、関連する分析などについて説明します。Brazeのイベント全般については、[イベント]({{site.baseurl}}/user_guide/data/custom_data/events/)を参照してください。

カスタムイベントは、ユーザーが行ったアクション、またはユーザーに関する更新です。カスタムイベントが記録されると、任意の数やタイプのフォローアップキャンペーンをトリガーできます。その後、[セグメンテーションフィルター](#segmentation-filters)を使用して、カスタムイベントの発生頻度や最終発生日に基づいてユーザーをセグメント化できます。これにより、カスタムイベントはアプリケーション内の価値の高いユーザーインタラクションの追跡に最適です。

## ユースケース {#use-cases}

一般的なカスタムイベントのユースケースには、以下のようなものがあります。

- [アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)を使用して、カスタムイベントに基づいてキャンペーンやキャンバスをトリガーする
- カスタムイベントの実行回数、最終発生日などに基づいてユーザーをセグメント化する
- ダッシュボードの[カスタムイベント分析]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics)を使用して、各イベントの発生回数の集計を表示する
- [ファネル]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps)レポートや[リテンション]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)レポートを使用して追加の分析を行う
- [永続的なエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)を活用して、顧客イベントのメタデータをキャンバスステップでのパーソナライゼーションに使用する
- [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)を使用してより高度な分析を生成する
- [終了条件]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/)を設定して、ユーザーがキャンバスを終了するタイミングを定義する

## エンタイトルメント {#entitlements}

エンタイトルメントは、カスタムイベントの容量を決定します。これは、定義するイベント名の数を追跡します。ワークスペースごとに最大2,000のカスタムイベントを使用できます。容量を増やす必要がある場合は、Brazeアカウントマネージャーにお問い合わせください。

ワークスペースがカスタムイベントの上限に近づくと、ダッシュボードとメールで通知が届きます。

容量に達した後も、既存のカスタムイベントは引き続き受信できます。ただし、新しいカスタムイベントを作成することはできません。まだ存在しないカスタムイベントに対して受信されたデータは処理されません。

## カスタムイベントの管理 {#managing-custom-events}

ダッシュボードで**データ設定** > **カスタムイベント**に移動して、カスタムイベントの管理、作成、またはブロックリスト登録を行えます。

カスタムイベントの横にあるメニューを選択すると、以下のアクションを実行できます。

### ブロックリスト登録 {#blocklisting}

アクションメニューから個々のカスタムイベントをブロックリストに登録するか、最大100件のイベントを選択して一括でブロックリストに登録できます。

カスタムイベントをブロックすると、以下のようになります。

- そのイベントの今後のデータは収集されません。
- そのイベントがブロック解除されない限り、既存のデータは利用できません。
- そのイベントはフィルターやグラフに表示されません。

さらに、ブロックされたカスタムイベントがBrazeの他の領域でフィルターやトリガーによって現在参照されている場合、そのフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることを説明する警告モーダルが表示されます。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases`の[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合、カスタムイベントの作成後に説明を追加できます。カスタムイベントの**説明を編集**を選択し、チームへのメモなど、任意の内容を入力します。

## タグの追加 {#adding-tags}

「Manage Events, Attributes, Purchases」の[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合、カスタムイベントの作成後にタグを追加できます。タグはイベントリストのフィルタリングに使用できます。

### 使用状況レポートの表示 {#viewing-usage-reports}

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

複数のカスタムイベントのチェックボックスを選択し、**使用状況レポートを表示**を選択すると、一度に最大100件の使用状況レポートを表示できます。

## データのエクスポート {#exporting-data}

カスタムイベントのリストをCSVファイルとしてエクスポートするには、ページ上部の**すべてエクスポート**ボタンを選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

## カスタムイベントの記録 {#logging-custom-events}

カスタムイベントには追加のセットアップが必要です。以下のリストで各プラットフォームのドキュメントを参照してください。カスタムイベントの記録に使用されるメソッドや、プロパティと数量の追加方法に関する情報が記載されています。

{% details プラットフォーム別のドキュメントを展開 %}

- [AndroidおよびFireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## カスタムイベントの保存 {#custom-event-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタムイベントのメタデータ（初回または最終発生、合計回数、30日間のX in Y）を含む）は、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users)である限り、無期限に保持されます。

## セグメンテーションフィルター {#segmentation-filters}

以下の表は、カスタムイベントに基づいてユーザーをセグメント化するために使用できるフィルターを示しています。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが**X回を超えて**発生したかどうかを確認する | **MORE THAN** | **NUMBER** |
| カスタムイベントが**X回未満**発生したかどうかを確認する | **LESS THAN** | **NUMBER** |
| カスタムイベントが**正確にX回**発生したかどうかを確認する | **EXACTLY** | **NUMBER** |
| カスタムイベントが**X日以降に**最後に発生したかどうかを確認する | **AFTER** | **TIME** |
| カスタムイベントが**X日以前に**最後に発生したかどうかを確認する | **BEFORE** | **TIME** |
| カスタムイベントが**X日以上前に**最後に発生したかどうかを確認する | **MORE THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが**X日未満前に**最後に発生したかどうかを確認する | **LESS THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが**X回（最大50回）を超えて**発生したかどうかを確認する | **MORE THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
| カスタムイベントが**X回（最大50回）未満**発生したかどうかを確認する | **LESS THAN** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
| カスタムイベントが**正確にX回（最大50回）**発生したかどうかを確認する | **EXACTLY** | 過去**Y日間（Y = 1,3,7,14,21,30）** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 分析 {#analytics}

Brazeは、カスタムイベントの発生回数と各ユーザーによる最終実行日をセグメンテーション用に記録します。これらの分析は、**Analytics** > **カスタムイベントレポート**に移動して表示できます。

ダッシュボードの**カスタムイベントレポート**ページでは、各カスタムイベントの発生頻度を集計で表示できます。時系列に重ねて表示されるグレーの線は、キャンペーンが最後に送信された時刻を示しており、キャンペーンがカスタムイベントのアクティビティにどのように影響したかを確認するのに役立ちます。

![ダッシュボードのカスタムイベントページにあるカスタムイベント数グラフ。カスタムイベントのトレンドを表示しています][8]

**フィルター**を使用して、カスタムイベントを時間別、月間アクティブユーザー（MAU）別、セグメント別、またはKPI数式別に分類することもできます。

{% alert tip %}
カスタムイベントに似たユーザーアクションのカウンターを保持するには、[カスタム属性のインクリメント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers)を使用します。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法で記録する必要があります。
{% endalert %}

### カスタムイベント分析が表示されない理由 {#why-custom-events-analytics-arent-showing}

カスタムイベントデータで作成されたセグメントは、作成前の過去の履歴データを表示できません。

## カスタムイベントプロパティ {#custom-event-properties}

カスタムイベントプロパティは、イベントの特定の発生を説明するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングのパーソナライゼーションの向上、コンバージョンの追跡、および生データエクスポートによるより高度な分析の生成に使用できます。

カスタムイベントプロパティはBrazeプロファイルに保存されないため、データポイントを消費しません（例外については[データポイント](#data-points)を参照してください）。

{% alert important %}
各カスタムイベントまたは購入には、最大256の異なるカスタムイベントプロパティを設定できます。256を超えるプロパティでカスタムイベントまたは購入が記録された場合、最初の256のみがキャプチャされ、使用可能になります。
{% endalert %}

### 期待されるフォーマット {#expected-format}

プロパティ値は、キーがプロパティ名、値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、255文字以下の空でない文字列で、先頭にドル記号（`$`）を含めることはできません。

プロパティ値は、以下のいずれかのデータタイプにすることができます。

| データタイプ | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)として |
| ブール値 | `true`または`false`の値。 |
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列としてフォーマットされます。配列内ではサポートされていません。 |
| 文字列 | 255文字以下。 |
| 配列 | 配列には日時を含めることはできません。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
| ネストされたオブジェクト | 他のオブジェクトの内部にあるオブジェクト。詳細については、この記事の[ネストされたオブジェクト](#nested-objects)のセクションを参照してください。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトは、最大100&nbsp;KBのイベントプロパティペイロードを持つことができます。

カスタムイベントプロパティのデータタイプを変更できますが、データ収集後に[データタイプを変更]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/)する影響に注意してください。

### カスタムイベントプロパティの使用 {#using-custom-event-properties}

カスタムイベントプロパティは、キャンペーンのトリガーの絞り込み、コンバージョンの追跡、メッセージングのパーソナライゼーションに使用できます。

#### メッセージのトリガー {#trigger-messages}

カスタムイベントプロパティを使用して、特定のキャンペーンやキャンバスのオーディエンスをさらに絞り込みます。たとえば、eコマースアプリケーションがあり、ユーザーがカートを放棄したときにメッセージを送信したい場合、`cart value`のカスタムイベントプロパティを追加して、ターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを強化できます。

![放棄カートのカスタムイベントプロパティフィルター。2つのフィルターがAND演算子で組み合わされ、カート値が100ドルから200ドルの間でカートを放棄したユーザーにこのキャンペーンを送信します][16]

ネストされたカスタムイベントプロパティも[アクションベースの配信][19]でサポートされています。

![放棄カートのカスタムイベントプロパティフィルター。カート内のいずれかのアイテムの価格が100ドルを超える場合に1つのフィルターが選択されています。][20]

#### メッセージのパーソナライズ {#personalize-messages}

メッセージングテンプレート内でパーソナライゼーションにカスタムイベントプロパティを使用することもできます。トリガーイベントを使用した[アクションベースの配信][19]を使用するキャンペーンは、そのイベントのカスタムイベントプロパティをメッセージングのパーソナライゼーションに使用できます。

たとえば、ゲームアプリがあり、レベルをクリアしたユーザーにメッセージを送信したい場合、ユーザーがそのレベルをクリアするのにかかった時間のプロパティでメッセージをさらにパーソナライズできます。この例では、[条件付きロジック][18]を使用して3つの異なるセグメントに対してメッセージがパーソナライズされています。`time_spent`というカスタムイベントプロパティは、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``を呼び出すことでメッセージに含めることができます。

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
ユーザーがインターネット接続を持っていない場合、テンプレート化されたカスタムイベントプロパティ（例: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}）を含むトリガーされたアプリ内メッセージは失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化されたアプリ内メッセージとして配信するLiquidタグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)を参照してください。

##### フィルターに関する考慮事項 {#considerations-with-filters}

- **API呼び出し:** API呼び出しを行い、「is blank」フィルターを使用する場合、カスタムイベントプロパティは呼び出しから除外されると「blank」と見なされます。たとえば、`"event_property": ""`を含めた場合、ユーザーは「not blank」と見なされます。
- **整数:** 数値のカスタムイベントプロパティでフィルタリングする際、数値が非常に大きい場合は、「exactly」フィルターを使用しないでください。数値が大きすぎると、特定の桁で丸められる可能性があり、フィルターが期待どおりに機能しない場合があります。

#### セグメンテーション {#segmentation}

イベントプロパティセグメンテーションを使用して、実行されたカスタムイベントとそれらのイベントに関連するプロパティに基づいてユーザーをターゲットにします。これにより、購入やカスタムイベントによるセグメンテーション時のフィルタリングオプションが増えます。

カスタムイベントのイベントプロパティは、それらを使用するセグメントに対してリアルタイムで更新されます。**データ設定** > **カスタムイベント**に移動し、関連するカスタムイベントの**プロパティを管理**を選択してプロパティを管理できます。特定のセグメントフィルターで使用されるカスタムイベントプロパティには、最大30日間のルックバック履歴があります。

##### セグメンテーション用のイベントプロパティの追加 {#adding-event-properties-for-segmentation}

イベントプロパティの頻度と最新性に基づいてセグメントを作成するには、「Manage Custom Event Property Segmentation」の[ユーザー権限]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage)が必要です。

デフォルトでは、ワークスペースごとに20のセグメント化可能なイベントプロパティを使用できます。この制限を増やすには、Brazeアカウントマネージャーにお問い合わせください。

セグメンテーション用のイベントプロパティを追加するには、以下の手順を実行します。

1. カスタムイベントに移動し、**プロパティを管理**を選択します。
2. **セグメンテーションを有効にする**トグルを選択して、セグメンテーション用のイベントプロパティを追加します。セグメンテーション時に追加のフィルタリングオプションにアクセスできます。

イベントプロパティセグメンテーションフィルターには以下が含まれます。

- 過去Y日間にプロパティAの値がBであるカスタムイベントをX回実行した。
- 過去Y日間にプロパティAの値がBである購入をX回行った。
- 1日から30日の範囲でセグメント化する機能を追加します。

![プロパティ「number of items」の値が「2」で「more than」「1」回、過去「30」暦日間に「Abandoned Cart」を実行したフィルターグループ。][3]

データは、カスタマーサクセスマネージャーによって有効化された後にのみ、特定のイベントプロパティに対して記録され、イベントプロパティはその日付以降のみ利用可能です。

##### データポイント {#data-points}

サブスクリプション使用量に関して、以下のフィルターでセグメンテーション用に有効化されたカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスエントリプロパティとイベントプロパティ {#canvas-entry-properties-and-event-properties}

キャンバスユーザージャーニーで`canvas_entry_properties`と`event_properties`を使用できます。詳細と例については、[キャンバスエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)を参照してください。

{% tabs local %}
{% tab キャンバスエントリプロパティ %}

[キャンバスエントリプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)は、アクションベースまたはAPIトリガーのキャンバスにマッピングするプロパティです。`canvas_entry_properties`オブジェクトの最大サイズ制限は50 KBです。

{% alert note %}
特にアプリ内メッセージチャネルの場合、`canvas_entry_properties`はキャンバスフローとオリジナルのキャンバスエディターでのみ参照できます。ただし、オリジナルのエディターでは、以前の早期アクセスの一部として永続的なエントリプロパティが有効になっている場合に限ります。
{% endalert %}

キャンバスフローのメッセージングでは、`canvas_entry_properties`は任意のメッセージステップで次のLiquid形式を使用して使用できます: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``。イベントはこの方法で使用するには、カスタムイベントまたは購入イベントである必要があります。

#### ユースケース {#use-case}

{% raw %}
小売店のRetailAppが次のリクエストを持っているとします: `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`。RetailAppは、Liquid `{{canvas_entry_properties.${product_name}}}`を使用して、メッセージに製品名（shoes）を取り込むことができます。
{% endraw %}

RetailAppは、ユーザーが購入イベントをトリガーした後にターゲットとするキャンバスで、異なる`product_name`プロパティに対して特定のメッセージを送信するようにトリガーすることもできます。たとえば、靴を購入したユーザーとそれ以外のものを購入したユーザーに異なるメッセージを送信するには、メッセージステップに以下のLiquidを追加します。

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details オリジナルのキャンバスエディターの場合は展開 %}

2023年2月28日以降、オリジナルのエディターを使用してキャンバスを作成または複製することはできなくなりました。このセクションは参照用としてのみ提供されています。

オリジナルのエディターで構築されたキャンバスの場合、`canvas_entry_properties`はキャンバスの最初のフルステップでのみ参照できます。

{% enddetails %}
{% endtab %}

{% tab イベントプロパティ %}

{% alert important %}
先頭のメッセージステップでは`event_properties`を使用できません。代わりに、`canvas_entry_properties`を使用するか、`event_properties`を含むメッセージステップの**前に**対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

イベントプロパティは、カスタムイベントと購入に設定するプロパティを指します。これらの`event_properties`は、アクションベースの配信を使用するキャンペーンやキャンバスで使用できます。

キャンバスフローでは、カスタムイベントと購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップのLiquidで使用できます。これらの`event_properties`を参照する場合は、{% raw %} ``{{event_properties.${property_name}}}``{% endraw %}を使用してください。これらのイベントは、メッセージコンポーネントでこの方法で使用するには、カスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連する`event_properties`を使用できます。これらの`event_properties`は、ユーザーが実際にアクションを実行した場合（その他のユーザーグループに進まなかった場合）にのみ使用できます。このアクションパスとメッセージステップの間に、他のステップ（別のアクションパスやメッセージステップではないもの）を配置できます。

{% details オリジナルのキャンバスエディターの場合は展開 %}

2023年2月28日以降、オリジナルのエディターを使用してキャンバスを作成または複製することはできなくなりました。このセクションは参照用としてのみ提供されています。

オリジナルのキャンバスエディターの場合、`event_properties`はスケジュールされたフルステップでは使用できません。ただし、アクションベースのキャンバスの最初のフルステップでは、フルステップがスケジュールされている場合でも`event_properties`を使用できます。

{% enddetails %}

{% endtab %}
{% endtabs %}

### ネストされたオブジェクト {#nested-objects}

ネストされたオブジェクト（別のオブジェクトの内部にあるオブジェクト）を使用して、カスタムイベントと購入のプロパティとしてネストされたJSONデータを送信できます。このネストされたデータは、メッセージ内のパーソナライズされた情報のテンプレート化、メッセージ送信のトリガー、およびユーザーのセグメンテーションに使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)の専用ページを参照してください。

## カスタムイベントプロパティの保存 {#custom-event-property-storage}

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージをよりパーソナライズされたものにするために設計されています。カスタムイベントプロパティは、Braze内で短期および長期の両方で保存できます。

イベントプロパティの値に基づいてセグメント化するには、2つの方法があります。

1. **30日以内:** Brazeサポート担当者は、Brazeのセグメント内で特定のイベントプロパティ値の頻度と最新性に基づいてイベントプロパティセグメンテーションを有効にできます。セグメント内でイベントプロパティを活用したい場合は、Brazeアカウントエグゼクティブまたはカスタマーサクセスマネージャーにお問い合わせください。このオプションはデータ使用量に影響します。<br><br>
2. **30日以内および30日を超える場合:** 短期および長期のイベントプロパティセグメンテーションの両方をカバーするには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用できます。この機能は、過去2年間に追跡されたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションはデータ使用量に影響しません。

特定のニーズに応じた最適なアプローチについての推奨事項は、Brazeカスタマーサクセスマネージャーにお問い合わせください。

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"