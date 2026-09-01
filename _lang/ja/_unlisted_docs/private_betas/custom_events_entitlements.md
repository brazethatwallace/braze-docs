---
article_title: カスタムイベント
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Braze Learningコース]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}カスタムイベント {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> この記事では、カスタムイベントとプロパティ、関連するセグメンテーションフィルター、キャンバスエントリプロパティ、関連する分析などについて説明します。Brazeのイベント全般については、[イベント]({{site.baseurl}}/user_guide/data/activation/events)を参照してください。

カスタムイベントは、ユーザーが行ったアクション、またはユーザーに関する更新です。カスタムイベントが記録されると、任意の数やタイプのフォローアップキャンペーンをトリガーできます。その後、[セグメンテーションフィルター](#segmentation-filters)を使用して、カスタムイベントの発生頻度や最終発生日に基づいてユーザーをセグメント化できます。これにより、カスタムイベントはアプリケーション内の価値の高いユーザーインタラクションのトラッキングに最適です。

## ユースケース {#use-cases}

一般的なカスタムイベントのユースケースには、以下のようなものがあります。

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## エンタイトルメント {#entitlements}

エンタイトルメントは、カスタムイベントの容量を決定します。これは、定義するさまざまなイベント名の数を追跡するものです。ワークスペースごとに最大2,000のカスタムイベントを設定できます。容量を増やす必要がある場合は、Brazeアカウントマネージャーに詳細をお問い合わせください。

ワークスペースがカスタムイベントの上限に近づくと、ダッシュボードおよびメールで通知が届き、状況を把握できます。

容量に達した後も、既存のカスタムイベントは引き続き受信できます。ただし、新しいカスタムイベントを作成することはできません。まだ存在しないカスタムイベントに対して受信されたデータは処理されません。

## カスタムイベントの管理 {#managing-custom-events}

ダッシュボードでカスタムイベントの管理、作成、またはブロックリスト登録を行うには、**データ設定** > **カスタムイベント**に移動します。

カスタムイベントの横にあるメニューを選択すると、以下のアクションが利用できます。

### ブロックリスト登録 {#blocklisting}

アクションメニューから個々のカスタムイベントをブロックリストに登録できます。また、一括で最大100件のイベントを選択してブロックリストに登録することもできます。

カスタムイベントをブロックすると、以下のようになります。

{% multi_lang_include data_activation/custom_event_block_effects.md %}

さらに、ブロックされたカスタムイベントが現在Brazeの他の領域でフィルターやトリガーによって参照されている場合、警告モーダルが表示され、そのイベントを参照しているフィルターやトリガーのすべてのインスタンスが削除およびアーカイブされることが説明されます。

### 説明の追加 {#adding-descriptions}

`Manage Events, Attributes, Purchases` の[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)がある場合、作成済みのカスタムイベントに説明を追加できます。カスタムイベントの**説明を編集**を選択し、チームへのメモなど任意の内容を入力します。

## タグの追加 {#adding-tags}

カスタムイベントの作成後、「イベント、属性、購入の管理」[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)がある場合は、タグを追加できます。タグを使用して、イベントのリストをフィルタリングできます。

### 使用レポートの表示 {#viewing-usage-reports}

使用レポートには、特定のカスタムイベントを使用しているすべてのキャンバス、キャンペーン、セグメントが一覧表示されます。このリストにはLiquidの使用は含まれません。

複数のカスタムイベントのチェックボックスを選択してから**使用レポートを表示**を選択すると、一度に最大100件の使用レポートを表示できます。

## データのエクスポート {#exporting-data}

カスタムイベントのリストをCSVファイルとしてエクスポートするには、ページ上部の**Export all**ボタンを選択します。CSVファイルが生成され、ダウンロードリンクがメールで送信されます。

## カスタムイベントのログ記録 {#logging-custom-events}

カスタムイベントには追加の設定が必要です。カスタムイベントのログ記録やプロパティと数量の追加に使用されるメソッドについては、各プラットフォームのドキュメントリンクを参照してください。

{% details プラットフォーム別のドキュメントを展開 %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## カスタムイベントのストレージ {#custom-event-storage}

**ユーザープロファイル**に保存されるすべてのデータ（カスタムイベントのメタデータ（初回または最終発生日、合計回数、30日間のうちY日中X回）を含む）は、各プロファイルが[アクティブ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users)である限り、無期限に保持されます。

## セグメンテーションフィルター {#segmentation-filters}

以下の表は、カスタムイベントによるユーザーのセグメンテーションに使用できるフィルターを示しています。

| セグメンテーションオプション | ドロップダウンフィルター | 入力オプション |
| ---------------------| --------------- | ------------- |
| カスタムイベントが **X 回を超えて** 発生したかどうかを確認する | **MORE THAN** | **NUMBER** |
| カスタムイベントが **X 回未満** 発生したかどうかを確認する | **LESS THAN** | **NUMBER** |
| カスタムイベントが **正確に X 回** 発生したかどうかを確認する | **EXACTLY** | **NUMBER** |
| カスタムイベントが最後に **X 日以降に** 発生したかどうかを確認する | **AFTER** | **TIME** |
| カスタムイベントが最後に **X 日より前に** 発生したかどうかを確認する | **BEFORE** | **TIME** |
| カスタムイベントが最後に **X 日以上前に** 発生したかどうかを確認する | **MORE THAN** | **NUMBER OF DAYS AGO** (正の数) |
| カスタムイベントが最後に **X 日未満前に** 発生したかどうかを確認する | **LESS THAN** | **NUMBER OF DAYS AGO** (正の数) |
| カスタムイベントが **X 回 (最大 = 50) を超えて** 発生したかどうかを確認する | **MORE THAN** | 過去 **Y 日間 (Y = 1,3,7,14,21,30)** |
| カスタムイベントが **X 回 (最大 = 50) 未満** 発生したかどうかを確認する | **LESS THAN** | 過去 **Y 日間 (Y = 1,3,7,14,21,30)** |
| カスタムイベントが **正確に X 回 (最大 = 50)** 発生したかどうかを確認する | **EXACTLY** | 過去 **Y 日間 (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 分析 {#analytics}

Brazeでは、カスタムイベントの発生回数と、各ユーザーが最後にそのイベントを実行した時刻をセグメンテーション用に記録しています。レポートの設定、フィルター、エクスポートオプションについては、[カスタムイベントレポート]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)を参照してください。

**カスタムイベントレポート**ページでは、各カスタムイベントの発生頻度を集計で確認できます。時系列に重ねて表示されるグレーの線は、最後にキャンペーンが送信された時刻を示しており、キャンペーンがカスタムイベントのアクティビティにどのような影響を与えたかを確認するのに役立ちます。

![ダッシュボードのカスタムイベントページに表示されるカスタムイベントのカウントグラフ。カスタムイベントのトレンドが表示されています。][8]

また、**フィルター**を使用して、カスタムイベントを時間別、月間アクティブユーザー数（MAU）別、セグメント別、またはKPI式別に分類することもできます。

{% alert tip %}
[カスタム属性のインクリメント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers)を使用すると、カスタムイベントと同様のユーザーアクションに対するカウンターを保持できます。ただし、カスタム属性のデータを時系列で表示することはできません。時系列での分析が不要なユーザーアクションは、この方法で記録してください。
{% endalert %}

### カスタムイベントの分析が表示されない理由 {#why-custom-events-analytics-arent-showing}

カスタムイベントデータで作成されたセグメントでは、そのセグメントが作成される前の過去の履歴データを表示することはできません。

## カスタムイベントプロパティ {#custom-event-properties}

カスタムイベントプロパティは、イベントの特定の発生を説明するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングのパーソナライゼーションの向上、コンバージョンのトラッキング、および生データエクスポートによるより高度な分析の生成に使用できます。

カスタムイベントプロパティはBrazeプロファイルには保存されないため、データポイントを消費しません（例外については[データポイント](#data-points)を参照してください）。

{% alert important %}
各カスタムイベントまたは購入には、最大256個の固有のカスタムイベントプロパティを設定できます。256を超えるプロパティでカスタムイベントまたは購入がログに記録された場合、最初の256個のみがキャプチャされ、使用可能になります。
{% endalert %}

### 想定されるフォーマット {#expected-format}

プロパティ値は、キーがプロパティ名で値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、255文字以下の空でない文字列で、先頭にドル記号（`$`）を付けることはできません。

プロパティ値は、次のいずれかのデータ型にすることができます。

| データ型 | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)のいずれか |
| ブール値 | `true`または`false`の値。 |
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列としてフォーマットされます。配列内ではサポートされていません。 |
| 文字列 | 255文字以下。 |
| 配列 | 配列に日時を含めることはできません。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
| ネストされたオブジェクト | 他のオブジェクトの内部にあるオブジェクト。詳しくは、この記事の[ネストされたオブジェクト](#nested-objects)のセクションを参照してください。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトは、最大100&nbsp;KBのイベントプロパティペイロードを持つことができます。

カスタムイベントプロパティのデータ型は変更できますが、データが収集された後に[データ型を変更する]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type)ことの影響に注意してください。

### カスタムイベントプロパティの使用 {#using-custom-event-properties}

カスタムイベントプロパティは、キャンペーンのトリガーの条件設定、コンバージョンのトラッキング、およびメッセージングのパーソナライズに使用できます。

#### メッセージのトリガー {#trigger-messages}

カスタムイベントプロパティを使用して、特定のキャンペーンまたはキャンバスのオーディエンスをさらに絞り込みます。たとえば、eコマースアプリケーションがあり、カートを放棄したユーザーにメッセージを送信したい場合、`cart value`のカスタムイベントプロパティを追加して、ターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを強化できます。

![放棄カートのカスタムイベントプロパティフィルター。2つのフィルターがAND演算子で組み合わされ、カート値が100ドルから200ドルの間でカートを放棄したユーザーにこのキャンペーンを送信します][16]

ネストされたカスタムイベントプロパティは、[アクションベースの配信][19]でもサポートされています。

![放棄カートのカスタムイベントプロパティフィルター。カート内のいずれかのアイテムの価格が100ドルを超える場合に1つのフィルターが選択されます。][20]

#### メッセージのパーソナライズ {#personalize-messages}

メッセージングテンプレート内でのパーソナライゼーションにもカスタムイベントプロパティを使用できます。トリガーイベントを伴う[アクションベースの配信][19]を使用しているキャンペーンでは、そのイベントのカスタムイベントプロパティをメッセージのパーソナライゼーションに使用できます。

たとえば、ゲームアプリがあり、レベルをクリアしたユーザーにメッセージを送信したい場合、ユーザーがそのレベルをクリアするのにかかった時間のプロパティでメッセージをさらにパーソナライズできます。この例では、[条件付きロジック][18]を使用して3つの異なるセグメントに対してメッセージをパーソナライズしています。`time_spent`というカスタムイベントプロパティは、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``を呼び出すことでメッセージに含めることができます。

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
ユーザーがインターネットに接続していない場合、テンプレート化されたカスタムイベントプロパティ（たとえば {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}）を含むトリガーされたアプリ内メッセージは失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化されたアプリ内メッセージとして配信するLiquidタグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)を参照してください。

##### フィルターに関する考慮事項 {#considerations-with-filters}

- **API呼び出し:** API呼び出しを行い、「空白」フィルターを使用する場合、カスタムイベントプロパティは呼び出しから除外されると「空白」と見なされます。たとえば、`"event_property": ""`を含めた場合、ユーザーは「空白ではない」と見なされます。
- **整数:** 数値のカスタムイベントプロパティでフィルタリングし、その数値が非常に大きい場合、「完全一致」フィルターは使用しないでください。数値が大きすぎると、特定の桁で丸められる可能性があり、フィルターが期待通りに機能しない場合があります。

#### セグメンテーション {#segmentation}

イベントプロパティのセグメンテーションを使用して、実行されたカスタムイベントとそれらのイベントに関連付けられたプロパティに基づいてユーザーをターゲットにします。これにより、購入およびカスタムイベントによるセグメンテーション時のフィルタリングオプションが増加します。

カスタムイベントのイベントプロパティは、それらを使用するセグメントに対してリアルタイムで更新されます。プロパティは、**データ設定** > **カスタムイベント**に移動し、関連するカスタムイベントの**プロパティを管理**を選択することで管理できます。特定のセグメントフィルターで使用されるカスタムイベントプロパティには、最大30日間のルックバック履歴があります。

##### セグメンテーション用のイベントプロパティの追加 {#adding-event-properties-for-segmentation}

イベントプロパティの頻度と最新性に基づいてセグメントを作成するには、「カスタムイベントプロパティのセグメンテーションを管理」の[ユーザー権限]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage)が必要です。

デフォルトでは、ワークスペースごとに20個のセグメント化可能なイベントプロパティを使用できます。この制限を引き上げるには、Brazeアカウントマネージャーにお問い合わせください。

セグメンテーション用のイベントプロパティを追加するには、以下を行います。

1. カスタムイベントに移動し、**プロパティを管理**を選択します。
2. **セグメンテーションを有効にする**トグルを選択して、セグメンテーション用のイベントプロパティを追加します。セグメンテーション時に追加のフィルタリングオプションにアクセスできます。

イベントプロパティのセグメンテーションフィルターには以下が含まれます。

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![「放棄カート」があり、プロパティ「アイテム数」の値が「2」で、過去「30」暦日以内に「1」回より多いフィルターグループ。][3]

データは、カスタマーサクセスマネージャーによって有効化された後に、指定されたイベントプロパティに対してのみログに記録され、イベントプロパティはその日付以降のみ利用可能です。

##### データポイント {#data-points}

サブスクリプションの使用に関して、以下のフィルターでセグメンテーション用に有効化されたカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスのエントリプロパティとイベントプロパティ {#canvas-entry-properties-and-event-properties}

キャンバスのユーザージャーニーで`canvas_entry_properties`と`event_properties`を使用できます。詳しい情報と例については、[キャンバスのエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を参照してください。

{% tabs local %}
{% tab キャンバスのエントリプロパティ %}

[キャンバスのエントリプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object)は、アクションベースまたはAPIトリガーのキャンバスにマッピングするプロパティです。`canvas_entry_properties`オブジェクトの最大サイズ制限は50 KBです。

{% alert note %}
In-App Messagesチャネルについては、`canvas_entry_properties`はキャンバスフローおよびオリジナルのキャンバスエディターでのみ参照できます。ただし、オリジナルのエディターでは、以前の早期アクセスの一部として永続エントリプロパティが有効化されている場合に限ります。
{% endalert %}

キャンバスフローのメッセージングでは、`canvas_entry_properties`は次のLiquid形式を使用して任意のメッセージステップで使用できます：``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``。イベントは、この方法で使用するにはカスタムイベントまたは購入イベントである必要があります。

#### ユースケース {#use-case}

{% raw %}
小売店のRetailAppが次のリクエストを持っているとします：`"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`。RetailAppはLiquid `{{canvas_entry_properties.${product_name}}}`を使用して、メッセージに商品名（shoes）を取り込むことができます。
{% endraw %}

RetailAppはまた、購入イベントをトリガーした後のユーザーをターゲットにしたキャンバスで、異なる`product_name`プロパティに対して特定のメッセージの送信をトリガーすることもできます。たとえば、靴を購入したユーザーとそれ以外のものを購入したユーザーに異なるメッセージを送信するには、メッセージステップに次のLiquidを追加します。

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details オリジナルのキャンバスエディターについて展開 %}

2023年2月28日以降、オリジナルのエディターを使用してキャンバスを作成または複製することはできなくなりました。このセクションは参照用としてのみ提供されています。

オリジナルのエディターで構築されたキャンバスでは、`canvas_entry_properties`はキャンバスの最初のフルステップでのみ参照できます。

{% enddetails %}
{% endtab %}

{% tab イベントプロパティ %}

{% alert important %}
リードのメッセージステップでは`event_properties`を使用できません。代わりに、`canvas_entry_properties`を使用するか、`event_properties`を含むメッセージステップの**前に**対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

イベントプロパティは、カスタムイベントと購入に設定するプロパティを指します。これらの`event_properties`は、アクションベースの配信を使用するキャンペーンやキャンバスで使用できます。

キャンバスフローでは、カスタムイベントおよび購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップでLiquidで使用できます。これらの`event_properties`を参照する場合は、{% raw %} ``{{event_properties.${property_name}}}``{% endraw %}を使用してください。これらのイベントは、メッセージコンポーネントでこの方法で使用するには、カスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連する`event_properties`を使用できます。これらの`event_properties`は、ユーザーが実際にアクションを実行した場合（Everyone Elseグループに移動しなかった場合）にのみ使用できます。このアクションパスとメッセージステップの間に他のステップ（別のアクションパスまたはメッセージステップではないもの）を配置することは可能です。

{% details オリジナルのキャンバスエディターについて展開 %}

2023年2月28日以降、オリジナルのエディターを使用してキャンバスを作成または複製することはできなくなりました。このセクションは参照用としてのみ提供されています。

オリジナルのキャンバスエディターでは、スケジュールされたフルステップで`event_properties`を使用することはできません。ただし、アクションベースのキャンバスの最初のフルステップでは、そのフルステップがスケジュールされている場合でも`event_properties`を使用できます。

{% enddetails %}

{% endtab %}
{% endtabs %}

### ネストされたオブジェクト {#nested-objects}

ネストされたオブジェクト（別のオブジェクトの内部にあるオブジェクト）を使用して、カスタムイベントおよび購入のプロパティとしてネストされたJSONデータを送信できます。このネストされたデータは、メッセージ内のパーソナライズされた情報のテンプレート化、メッセージ送信のトリガー、およびユーザーのセグメンテーションに使用できます。

詳しくは、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)の専用ページを参照してください。

## カスタムイベントプロパティのストレージ {#custom-event-property-storage}

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージをよりパーソナライズされたものにするために設計されています。カスタムイベントプロパティは、Braze内で短期的にも長期的にも保存できます。

イベントプロパティの値に基づいてセグメンテーションを行うには、次の2つの方法があります。

1. **30日以内:** Brazeサポート担当者は、Brazeセグメント内の特定のイベントプロパティ値の頻度と最新性に基づくイベントプロパティセグメンテーションを有効にできます。セグメント内でイベントプロパティを活用したい場合は、Brazeのアカウントエグゼクティブまたはカスタマーサクセスマネージャーにお問い合わせください。このオプションはデータ使用量に影響します。<br><br>
2. **30日以内および30日以降:** 短期と長期の両方のイベントプロパティセグメンテーションに対応するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用できます。この機能は、過去2年以内にトラッキングされたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションはデータ使用量に影響しません。

具体的なニーズに応じた最適なアプローチについては、Brazeのカスタマーサクセスマネージャーにお問い合わせください。

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