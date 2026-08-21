---
article_title: カスタムイベント
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Braze Learningコース]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> この記事では、カスタムイベントとプロパティ、関連するセグメンテーションフィルター、キャンバスエントリプロパティ、関連する分析などについて説明します。Brazeのイベント全般については、[イベント]({{site.baseurl}}/user_guide/data/custom_data/events)を参照してください。

カスタムイベントは、ユーザーが行ったアクション、またはユーザーに関する更新です。カスタムイベントが記録されると、任意の数やタイプのフォローアップキャンペーンをトリガーできます。その後、[セグメンテーションフィルター](#segmentation-filters)を使用して、カスタムイベントの発生頻度や最終発生日に基づいてユーザーをセグメント化できます。これにより、カスタムイベントはアプリケーション内の価値の高いユーザーインタラクションのトラッキングに最適です。

## ユースケース {#use-cases}

一般的なカスタムイベントのユースケースには、以下のようなものがあります。

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## エンタイトルメント {#entitlements}

エンタイトルメントは、カスタムイベントの容量を決定します。これは、定義できるさまざまなイベント名の数を追跡するものです。ワークスペースごとに最大2,000件のカスタムイベントを使用できます。容量を増やす必要がある場合は、Brazeアカウントマネージャーに連絡して詳細をご確認ください。

ワークスペースがカスタムイベントの上限数に近づくと、ダッシュボードおよびメールで通知が届き、状況を把握できるようになります。

容量に達した後も、既存のカスタムイベントは引き続き受信できます。ただし、新しいカスタムイベントを作成することはできません。まだ存在しないカスタムイベントに対して受信されたデータは処理されません。

## カスタムイベントの管理 {#managing-custom-events}

ダッシュボードで**データ設定** > **カスタムイベント**に移動すると、カスタムイベントの管理、作成、またはブロックリストへの登録を行うことができます。

カスタムイベントの横にあるメニューを選択すると、以下のアクションを実行できます。

### ブロックリストへの登録 {#blocklisting}

アクションメニューから個々のカスタムイベントをブロックリストに登録したり、最大100件のイベントを選択して一括でブロックリストに登録したりできます。

カスタムイベントをブロックすると、以下のようになります。

{% multi_lang_include data_activation/custom_event_block_effects.md %}

さらに、ブロックされたカスタムイベントがBrazeの他の領域でフィルターやトリガーによって現在参照されている場合、そのイベントを参照しているフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることを説明する警告モーダルが表示されます。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases`の[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)を持っている場合、カスタムイベントの作成後に説明を追加できます。カスタムイベントの**説明を編集**を選択し、チームへのメモなど、任意の内容を入力してください。

## タグの追加 {#adding-tags}

カスタムイベントの作成後にタグを追加するには、「イベント、属性、購入の管理」[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)が必要です。タグを使用して、イベントのリストをフィルタリングできます。

### 使用状況レポートの表示 {#viewing-usage-reports}

使用状況レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

複数のカスタムイベントのチェックボックスを選択し、**使用状況レポートを表示**を選択すると、一度に最大100件の使用状況レポートを表示できます。

## データのエクスポート {#exporting-data}

カスタムイベントのリストをCSVファイルとしてエクスポートするには、ページ上部の**Export all**ボタンを選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

## カスタムイベントのログ記録 {#logging-custom-events}

カスタムイベントには追加の設定が必要です。カスタムイベントのログ記録やプロパティ・数量の追加に使用するメソッドについては、各プラットフォームのドキュメントリンクを参照してください。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android および FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## カスタムイベントのストレージ {#custom-event-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタムイベントのメタデータ（最初または最後の発生、合計カウント、30日間のY中X）を含む）は、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users)である限り、無期限に保持されます。

## セグメンテーションフィルター {#segmentation-filters}

以下の表は、カスタムイベントによってユーザーをセグメント化するために使用できるフィルターを示しています。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが**X回より多く**発生したかどうかを確認する | **MORE THAN** | **NUMBER** |
| カスタムイベントが**X回未満**発生したかどうかを確認する | **LESS THAN** | **NUMBER** |
| カスタムイベントが**正確にX回**発生したかどうかを確認する | **EXACTLY** | **NUMBER** |
| カスタムイベントが最後に**X日以降に**発生したかどうかを確認する | **AFTER** | **TIME** |
| カスタムイベントが最後に**X日より前に**発生したかどうかを確認する | **BEFORE** | **TIME** |
| カスタムイベントが最後に**X日以上前に**発生したかどうかを確認する | **MORE THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが最後に**X日未満前に**発生したかどうかを確認する | **LESS THAN** | **NUMBER OF DAYS AGO**（正の数） |
| カスタムイベントが**X回（最大50回）より多く**発生したかどうかを確認する | **MORE THAN** | 過去**Y日間（Y = 1、3、7、14、21、30）** |
| カスタムイベントが**X回（最大50回）未満**発生したかどうかを確認する | **LESS THAN** | 過去**Y日間（Y = 1、3、7、14、21、30）** |
| カスタムイベントが**正確にX回（最大50回）**発生したかどうかを確認する | **EXACTLY** | 過去**Y日間（Y = 1、3、7、14、21、30）** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 分析 {#analytics}

Brazeは、カスタムイベントが発生した回数と、各ユーザーが最後にそのイベントを実行した日時をセグメンテーション用に記録します。レポートの設定、フィルター、エクスポートオプションについては、[カスタムイベントレポート]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)を参照してください。

**カスタムイベントレポート**ページでは、各カスタムイベントの発生頻度を集計して確認できます。時系列に重ねて表示されるグレーの線は、最後にキャンペーンが送信された日時を示しており、キャンペーンがカスタムイベントのアクティビティにどのような影響を与えたかを確認するのに役立ちます。

![ダッシュボードのカスタムイベントページに表示されるカスタムイベントのカウントグラフ。カスタムイベントのトレンドが表示されています][8]

また、**フィルター**を使用して、カスタムイベントを時間別、月間アクティブユーザー数（MAU）別、セグメント別、またはKPI計算式別に分類することもできます。

{% alert tip %}
[カスタム属性のインクリメント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers)を使用すると、カスタムイベントと同様のユーザーアクションのカウンターを保持できます。ただし、カスタム属性データを時系列で表示することはできません。時系列で分析する必要のないユーザーアクションは、この方法で記録してください。
{% endalert %}

### カスタムイベントの分析が表示されない理由 {#why-custom-events-analytics-arent-showing}

カスタムイベントデータで作成されたセグメントでは、そのセグメントが作成される前の過去の履歴データを表示することはできません。

## カスタムイベントプロパティ {#custom-event-properties}

カスタムイベントプロパティは、イベントの特定の発生を説明するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングにおけるパーソナライゼーションの向上、コンバージョンのトラッキング、および生データエクスポートによるより高度な分析の生成に使用できます。

カスタムイベントプロパティはBrazeプロファイルに保存されないため、データポイントを消費しません（例外については[データポイント](#data-points)を参照してください）。

{% alert important %}
各カスタムイベントまたは購入には、最大256個の異なるカスタムイベントプロパティを設定できます。カスタムイベントまたは購入が256個を超えるプロパティとともに記録された場合、最初の256個のみがキャプチャされ、使用可能になります。
{% endalert %}

### 想定されるフォーマット {#expected-format}

プロパティ値は、キーがプロパティ名、値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、先頭にドル記号（`$`）を含まない、255文字以下の空でない文字列である必要があります。

プロパティ値には、以下のデータ型のいずれかを使用できます。

| データ型 | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)のいずれか |
| ブール値 | `true`または`false`の値。 |
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列としてフォーマットされます。配列内ではサポートされていません。 |
| 文字列 | 255文字以下。 |
| 配列 | 配列には日時を含めることができません。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
| ネストされたオブジェクト | 他のオブジェクトの内部にあるオブジェクトです。詳細については、この記事の[ネストされたオブジェクト](#nested-objects)のセクションを参照してください。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトは、最大100&nbsp;KBのイベントプロパティペイロードを持つことができます。

カスタムイベントプロパティのデータ型を変更できますが、データが収集された後に[データ型を変更する]({{site.baseurl}}/help/help_articles/data/change_custom_data_type)ことの影響に注意してください。

### カスタムイベントプロパティの使用 {#using-custom-event-properties}

カスタムイベントプロパティは、キャンペーンのトリガーの絞り込み、コンバージョンのトラッキング、およびメッセージングのパーソナライズに使用できます。

#### メッセージのトリガー {#trigger-messages}

カスタムイベントプロパティを使用して、特定のキャンペーンまたはキャンバスのオーディエンスをさらに絞り込みます。たとえば、eコマースアプリケーションがあり、ユーザーがカートを放棄したときにメッセージを送信したい場合、`cart value`のカスタムイベントプロパティを追加して、ターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを向上させることができます。

![放棄カートのカスタムイベントプロパティフィルター。2つのフィルターがAND演算子で組み合わされ、カート値が100ドルから200ドルの間でカートを放棄したユーザーにこのキャンペーンを送信します][16]

ネストされたカスタムイベントプロパティは、[アクションベース配信][19]でもサポートされています。

![放棄カートのカスタムイベントプロパティフィルター。カート内のいずれかのアイテムの価格が100ドルを超える場合に1つのフィルターが選択されています。][20]

#### メッセージのパーソナライズ {#personalize-messages}

メッセージングテンプレート内でのパーソナライゼーションにもカスタムイベントプロパティを使用できます。トリガーイベントを使用した[アクションベース配信][19]を使用するキャンペーンでは、そのイベントのカスタムイベントプロパティをメッセージングのパーソナライゼーションに使用できます。

たとえば、ゲームアプリがあり、レベルをクリアしたユーザーにメッセージを送信したい場合、ユーザーがそのレベルをクリアするのにかかった時間のプロパティを使用して、メッセージをさらにパーソナライズできます。この例では、[条件付きロジック][18]を使用して3つの異なるセグメントに対してメッセージがパーソナライズされています。`time_spent`というカスタムイベントプロパティは、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``を呼び出すことでメッセージに含めることができます。

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
ユーザーがインターネットに接続していない場合、テンプレート化されたカスタムイベントプロパティ（例：{% raw %}``{{event_properties.${time_spent}}}``{% endraw %}）を含むトリガーされたアプリ内メッセージは失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化されたアプリ内メッセージとして配信するLiquidタグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)を参照してください。

##### フィルターに関する考慮事項 {#considerations-with-filters}

- **API呼び出し：** API呼び出しを行い、「is blank」フィルターを使用する場合、カスタムイベントプロパティは呼び出しから除外されると「blank」と見なされます。たとえば、`"event_property": ""`を含めた場合、ユーザーは「not blank」と見なされます。
- **整数：** 数値のカスタムイベントプロパティでフィルタリングし、その数値が非常に大きい場合、「exactly」フィルターを使用しないでください。数値が大きすぎると、特定の桁で丸められる可能性があるため、フィルターが期待どおりに機能しない場合があります。

#### セグメンテーション {#segmentation}

イベントプロパティセグメンテーションを使用して、実行されたカスタムイベントとそれらのイベントに関連付けられたプロパティに基づいてユーザーをターゲットにします。これにより、購入およびカスタムイベントによるセグメンテーション時のフィルタリングオプションが増えます。

カスタムイベントのイベントプロパティは、それらを使用するセグメントに対してリアルタイムで更新されます。プロパティを管理するには、**データ設定** > **カスタムイベント**に移動し、関連するカスタムイベントの**プロパティを管理**を選択します。特定のセグメントフィルターで使用されるカスタムイベントプロパティには、最大30日間のルックバック履歴があります。

##### セグメンテーション用のイベントプロパティの追加 {#adding-event-properties-for-segmentation}

イベントプロパティの頻度と最新性に基づいてセグメントを作成するには、「Manage Custom Event Property Segmentation」の[ユーザー権限]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage)が必要です。

デフォルトでは、ワークスペースごとに20個のセグメント可能なイベントプロパティを設定できます。この制限を引き上げるには、Brazeアカウントマネージャーにお問い合わせください。

セグメンテーション用のイベントプロパティを追加するには、以下の手順を実行します。

1. カスタムイベントに移動し、**プロパティを管理**を選択します。
2. **セグメンテーションを有効にする**トグルを選択して、セグメンテーション用のイベントプロパティを追加します。セグメンテーション時に追加のフィルタリングオプションにアクセスできます。

イベントプロパティセグメンテーションフィルターには以下が含まれます。

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![「放棄カート」のプロパティ「number of items」の値が「2」で「more than」「1」回、過去「30」暦日以内であるフィルターグループ。][3]

データは、カスタマーサクセスマネージャーによって有効化された後にのみ、特定のイベントプロパティに対して記録され、イベントプロパティはその日付以降のみ利用可能です。

##### データポイント {#data-points}

サブスクリプションの使用に関して、以下のフィルターでセグメンテーション用に有効化されたカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスエントリプロパティとイベントプロパティ {#canvas-entry-properties-and-event-properties}

キャンバスのユーザージャーニーで`canvas_entry_properties`と`event_properties`を使用できます。詳細と例については、[キャンバスエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)を参照してください。

{% tabs local %}
{% tab キャンバスエントリプロパティ %}

[キャンバスエントリプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object)は、アクションベースまたはAPIトリガーのキャンバスにマッピングするプロパティです。`canvas_entry_properties`オブジェクトの最大サイズ制限は50 KBであることに注意してください。

{% alert note %}
特にアプリ内メッセージチャネルの場合、`canvas_entry_properties`は、以前の早期アクセスの一部としてオリジナルエディターで永続的なエントリプロパティを有効にしている場合にのみ、キャンバスフローとオリジナルキャンバスエディターで参照できます。
{% endalert %}

キャンバスフローのメッセージングでは、`canvas_entry_properties`は次のLiquid形式で任意のメッセージステップで使用できます：``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``。イベントはこの方法で使用するには、カスタムイベントまたは購入イベントである必要があることに注意してください。

#### ユースケース {#use-case}

{% raw %}
小売店RetailAppが次のリクエストを持っているとします：`"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`。RetailAppは、Liquid `{{canvas_entry_properties.${product_name}}}`を使用して、メッセージに商品名（shoes）を取り込むことができます。
{% endraw %}

RetailAppは、購入イベントをトリガーした後のユーザーをターゲットにするキャンバスで、異なる`product_name`プロパティに対して特定のメッセージを送信するようにトリガーすることもできます。たとえば、靴を購入したユーザーとそれ以外のものを購入したユーザーに異なるメッセージを送信するには、メッセージステップに次のLiquidを追加します。

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details オリジナルキャンバスエディターの場合は展開 %}

2023年2月28日以降、オリジナルエディターを使用したキャンバスの作成または複製はできなくなりました。このセクションは参照用としてのみ提供されています。

オリジナルエディターで構築されたキャンバスの場合、`canvas_entry_properties`はキャンバスの最初のフルステップでのみ参照できます。

{% enddetails %}
{% endtab %}

{% tab イベントプロパティ %}

{% alert important %}
リードメッセージステップでは`event_properties`を使用できません。代わりに、`canvas_entry_properties`を使用するか、`event_properties`を含むメッセージステップの**前に**対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

イベントプロパティは、カスタムイベントと購入に設定するプロパティを指します。これらの`event_properties`は、アクションベース配信のキャンペーンとキャンバスで使用できます。

キャンバスフローでは、カスタムイベントと購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップのLiquidで使用できます。これらの`event_properties`を参照する場合は、{% raw %} ``{{event_properties.${property_name}}}``{% endraw %}を使用してください。これらのイベントは、メッセージコンポーネントでこの方法で使用するには、カスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連する`event_properties`を使用できます。これらの`event_properties`は、ユーザーが実際にアクションを実行した場合にのみ使用できます（Everyone Elseグループに進まなかった場合）。このアクションパスとメッセージステップの間に、他のステップ（別のアクションパスやメッセージステップではないもの）を配置できます。

{% details オリジナルキャンバスエディターの場合は展開 %}

2023年2月28日以降、オリジナルエディターを使用したキャンバスの作成または複製はできなくなりました。このセクションは参照用としてのみ提供されています。

オリジナルキャンバスエディターの場合、`event_properties`はスケジュールされたフルステップでは使用できません。ただし、アクションベースのキャンバスの最初のフルステップでは、フルステップがスケジュールされている場合でも`event_properties`を使用できます。

{% enddetails %}

{% endtab %}
{% endtabs %}

### ネストされたオブジェクト {#nested-objects}

ネストされたオブジェクト（別のオブジェクトの内部にあるオブジェクト）を使用して、カスタムイベントと購入のプロパティとしてネストされたJSONデータを送信できます。このネストされたデータは、メッセージ内のパーソナライズされた情報のテンプレート化、メッセージ送信のトリガー、およびユーザーのセグメンテーションに使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects)の専用ページを参照してください。

## カスタムイベントプロパティの保存 {#custom-event-property-storage}

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージをよりパーソナライズされたものにするために設計されています。カスタムイベントプロパティは、Braze内で短期的にも長期的にも保存できます。

イベントプロパティの値に基づいてセグメンテーションを行うには、2つの方法があります。

1. **30日以内:** Brazeサポート担当者は、Brazeセグメント内で特定のイベントプロパティ値の頻度と最新性に基づくイベントプロパティセグメンテーションを有効にできます。セグメント内でイベントプロパティを活用したい場合は、Brazeアカウントエグゼクティブまたはカスタマーサクセスマネージャーにお問い合わせください。このオプションはデータ使用量に影響します。<br><br>
2. **30日以内および30日を超える場合:** 短期的および長期的なイベントプロパティセグメンテーションの両方に対応するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension)を使用できます。この機能は、過去2年間にトラッキングされたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションはデータ使用量に影響しません。

お客様の具体的なニーズに応じた最適なアプローチについては、Brazeカスタマーサクセスマネージャーにお問い合わせください。

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