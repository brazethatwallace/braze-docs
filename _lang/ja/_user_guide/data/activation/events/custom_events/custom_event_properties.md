---
nav_title: カスタムイベントプロパティ
article_title: カスタムイベントプロパティ
page_order: 0
page_type: reference
description: "この記事では、カスタムイベントプロパティ、その想定されるフォーマット、使用方法、およびカスタムイベントプロパティのストレージについて説明します。"
---

# カスタムイベントプロパティ {#custom-event-properties}

> この記事では、カスタムイベントプロパティ、その想定されるフォーマット、メッセージングやセグメンテーションでの使用方法、およびカスタムイベントプロパティのストレージについて説明します。

カスタムイベントプロパティは、イベントの特定の発生を記述するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングにおけるパーソナライゼーションの向上、コンバージョンのトラッキング、および生データエクスポートによるより高度な分析の生成に使用できます。

カスタムイベントプロパティはBrazeプロファイルに保存されないため、データポイントを記録しません（例外については[データポイント](#data-points)を参照してください）。

## ユーザーのイベントプロパティ値を表示する {#viewing-event-property-values-for-a-user}

特定のユーザーのカスタムイベントプロパティの値を表示するには、設定に応じて以下のオプションが利用できます。

- **Currents:** 顧客行動イベントが有効になっている場合、イベントプロパティはCurrentsエクスポートに含まれます。
- **イベントユーザーログ:** ユーザーがテストユーザーであり、最近そのイベントを実行した場合、イベントとそのプロパティは**[設定]** > **[イベントユーザーログ]** に表示されます。
- **セグメンテーション:** そのプロパティに対してカスタムイベントプロパティストレージが有効になっている場合、イベントプロパティフィルターを使用してセグメントを作成し、ユーザーが条件を満たすかどうかを確認できます。

{% alert important %}
各カスタムイベントまたは購入には、最大256個の異なるカスタムイベントプロパティを設定できます。カスタムイベントまたは購入が256を超えるプロパティとともに記録された場合、最初の256個のみがキャプチャされ、使用可能になります。
{% endalert %}

## 想定されるフォーマット {#expected-format}

プロパティ値はオブジェクトである必要があります。キーはプロパティ名（空でない文字列、255文字以下、先頭に `$` なし）で、値はプロパティ値です。サポートされるデータタイプ、フォーマット要件、およびペイロード制限については、[データタイプ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#event-property-data-types)を参照してください。

カスタムイベントプロパティのデータタイプは変更できますが、データが収集された後に[データタイプを変更する]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type)ことの影響に注意してください。

### 予約キー {#reserved-keys}

予約キーをイベントプロパティ名として使用することはできません。`properties` オブジェクトで予約キーを使用すると、「Invalid 'properties' field」というエラーが返されます。

| プロパティ | 予約キー |
| --- | --- |
| カスタムイベント | `time` および `event_name` |
| 購入イベント | `time`、`product_id`、`quantity`、`event_name`、`price`、`currency` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="予約キー" }

## カスタムイベントプロパティの使用 {#using-custom-event-properties}

カスタムイベントプロパティは、キャンペーンのトリガー条件の設定、コンバージョンのトラッキング、メッセージングのパーソナライゼーションに使用できます。

### メッセージのトリガー {#trigger-messages}

カスタムイベントプロパティを使用して、特定のキャンペーンやキャンバスのオーディエンスをさらに絞り込むことができます。たとえば、eコマースアプリケーションがあり、ユーザーがカートを放棄したときにメッセージを送信したい場合、`price` のカスタムイベントプロパティを追加してターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを強化できます。

![放棄カートのカスタムイベントプロパティフィルター。2つのフィルターがAND演算子で組み合わされ、価格が100ドルから200ドルの間でカートを放棄したユーザーにこのキャンペーンを送信します]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

ネストされたカスタムイベントプロパティは、[アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)でもサポートされています。

![放棄カートのカスタムイベントプロパティフィルター。カート内のいずれかのアイテムの価格が100ドルを超える場合に1つのフィルターが選択されます。]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### メッセージのパーソナライズ {#personalize-messages}

メッセージングテンプレート内でのパーソナライゼーションにもカスタムイベントプロパティを使用できます。トリガーイベントを使用した[アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を使用するキャンペーンでは、そのイベントのカスタムイベントプロパティをメッセージングのパーソナライゼーションに使用できます。

#### フィルターに関する注意事項 {#considerations-with-filters}

- **API呼び出し:** API呼び出しを行い「is blank」フィルターを使用する場合、カスタムイベントプロパティは呼び出しから除外されるか、値が空文字列（`""`）の場合に「blank」と見なされます。たとえば、`"event_property": ""` を含めると、ユーザーは「blank」と見なされます。
- **整数:** 数値のカスタムイベントプロパティでフィルタリングする際に数値が非常に大きい場合、「exactly」フィルターは使用しないでください。数値が大きすぎると、特定の桁数で丸められる可能性があるため、フィルターが期待どおりに機能しないことがあります。

#### 比較のための型変換 {#type-coercion-for-comparisons}

Liquidの条件文でイベントプロパティを使用する場合、整数のイベントプロパティを大なり、小なり、等しいなどの演算子で比較すると、`Liquid error: comparison of String with 0 failed` というエラーが発生することがあります。これは、Liquidがデフォルトでプロパティを文字列として扱うために発生します。

これを修正するには、比較の前に `plus: 0` フィルターを使用してプロパティを数値に変換します。

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent >= 100 %}
  Great job completing the level quickly!
{% endif %}
```
{% endraw %}

たとえば、ゲームアプリがあり、レベルをクリアしたユーザーにメッセージを送信したい場合、ユーザーがそのレベルをクリアするのにかかった時間のプロパティを使用して、メッセージをさらにパーソナライズできます。

以下のメッセージは、[条件ロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)を使用して3つの異なるセグメント向けにパーソナライズされています。`time_spent` というカスタムイベントプロパティは、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` を呼び出すことでメッセージに含めることができます。

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif time_spent < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
ユーザーがインターネットに接続していない場合、テンプレート化されたカスタムイベントプロパティ（たとえば {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}）を含むトリガーされたアプリ内メッセージは失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化されたアプリ内メッセージとして配信するLiquidタグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages)を参照してください。

#### キャンバス {#canvas}

キャンバスでは、`context` と `event_properties` は異なる目的で使用されます。

- **`context`**: キャンバスへのエントリをトリガーしたイベントまたはAPI呼び出しのプロパティです。最初のステップを含む任意のメッセージステップで `context` を使用します。
- **`event_properties`**: ジャーニー中に発生したカスタムイベントまたは購入のプロパティです。[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)ステップの後の最初のメッセージステップでのみ使用します。Everyone Elseパスや、それ以降のメッセージステップでは使用できません。

{% alert important %}
キャンバスの最初のメッセージステップでは、`event_properties` の代わりに `context` を使用するか、メッセージステップの前にアクションパスステップを追加してください。例外: アプリ内メッセージの場合、そのイベントがキャンバスのエントリトリガーであれば、最初のメッセージステップで `event_properties` を使用できます。
{% endalert %}

詳細については、[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)および[キャンバスエントリプロパティとイベントプロパティ](#canvas-entry-properties-and-event-properties)を参照してください。

### セグメンテーション {#segmentation}

イベントプロパティセグメンテーションを使用して、実行されたカスタムイベントとそれらのイベントに関連するプロパティに基づいてユーザーをターゲットにします。これにより、購入やカスタムイベントによるセグメンテーション時のフィルタリングオプションが増えます。

カスタムイベントのイベントプロパティは、それらを使用するセグメントに対してリアルタイムで更新されます。プロパティを管理するには、**データ設定** > **カスタムイベント**に移動し、関連するカスタムイベントの**プロパティを管理**を選択します。特定のセグメントフィルターで使用されるカスタムイベントプロパティには、最大30日間のルックバック履歴があります。

#### セグメンテーション用のイベントプロパティの追加 {#adding-event-properties-for-segmentation}

イベントプロパティの頻度と最新性に基づいてセグメントを作成するには、「Edit Custom Event Property Segmentation」の[ユーザー権限]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage)が必要です。

デフォルトでは、ワークスペースごとに20個のセグメント可能なイベントプロパティを設定できます。この制限を引き上げるには、Brazeアカウントマネージャーにお問い合わせください。

セグメンテーション用のイベントプロパティを追加するには、以下の手順を実行します。

1. カスタムイベントに移動し、**プロパティを管理**を選択します。
2. **セグメンテーションを有効にする**トグルを選択して、セグメンテーション用のイベントプロパティを追加します。セグメンテーション時に追加のフィルタリングオプションにアクセスできます。

イベントプロパティセグメンテーションフィルターには以下が含まれます。

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![「放棄カート」のフィルターグループ。プロパティ「number of items」が値2で、過去30暦日間に1回以上発生した条件が設定されています。]({% image_buster /assets/img/nested_object3.png %})

データは、特定のイベントプロパティを有効にした後にのみ記録され、イベントプロパティはその日付以降のみ利用可能です。

#### データポイント {#data-points}

サブスクリプションの使用量に関して、以下のフィルターでセグメンテーション用に有効化されたカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、それぞれ個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスエントリプロパティとイベントプロパティ {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### ネストされたオブジェクト {#nested-objects}

ネストされたオブジェクト（別のオブジェクト内のオブジェクト）を使用して、カスタムイベントや購入のプロパティとしてネストされたJSONデータを送信できます。このネストされたデータは、メッセージ内のパーソナライズされた情報のテンプレート化、メッセージ送信のトリガー、ユーザーのセグメンテーションに使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)の専用ページを参照してください。

## カスタムイベントプロパティの保存 {#custom-event-property-storage}

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージをよりパーソナライズされたものにするために設計されています。カスタムイベントプロパティは、Braze内で短期的にも長期的にも保存できます。

イベントプロパティの値に基づいてセグメント化するには、2つの方法があります。

1. **30日以内:** Brazeセグメント内で、特定のイベントプロパティ値の頻度と最新性に基づくイベントプロパティセグメンテーションを使用できます。このオプションはデータ使用量に影響します。<br><br>
2. **30日以内および30日を超える場合:** 短期的および長期的なイベントプロパティセグメンテーションの両方に対応するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用できます。この機能は、過去2年間にトラッキングされたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションはデータ使用量に影響しません。

お客様の具体的なニーズに応じた最適なアプローチについては、Brazeカスタマーサクセスマネージャーにお問い合わせください。