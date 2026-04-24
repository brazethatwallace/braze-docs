---
nav_title: カスタムイベントプロパティ
article_title: カスタムイベントプロパティ
page_order: 0
page_type: reference
description: "この記事では、カスタムイベントプロパティ、その想定されるフォーマット、使用方法、およびカスタムイベントプロパティのストレージについて説明します。"
---

# カスタムイベントプロパティ

> この記事では、カスタムイベントプロパティ、その想定されるフォーマット、メッセージングやセグメンテーションでの使用方法、およびカスタムイベントプロパティのストレージについて説明します。

カスタムイベントプロパティは、イベントの特定の発生を記述するカスタムイベントのメタデータまたは属性です。これらのプロパティは、トリガー条件のさらなる絞り込み、メッセージングにおけるパーソナライゼーションの向上、コンバージョンのトラッキング、および生データエクスポートによるより高度な分析の生成に使用できます。

カスタムイベントプロパティは Braze プロファイルに保存されないため、データポイントを記録しません（例外については[データポイント](#data-points)を参照してください）。

{% alert important %}
各カスタムイベントまたは購入には、最大256個の異なるカスタムイベントプロパティを設定できます。カスタムイベントまたは購入が256個を超えるプロパティで記録された場合、最初の256個のみがキャプチャされ、使用可能になります。
{% endalert %}

## 想定されるフォーマット {#expected-format}

プロパティ値はオブジェクトである必要があります。キーはプロパティ名（空でない文字列、255文字以下、先頭に `$` なし）で、値はプロパティ値です。サポートされるデータタイプ、フォーマット要件、およびペイロード制限については、[データタイプ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#event-property-data-types)を参照してください。

カスタムイベントプロパティのデータタイプは変更できますが、データが収集された後に[データタイプを変更する]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#changing-custom-attribute-or-event-data-type)ことの影響に注意してください。

### 予約キー

予約キーをイベントプロパティ名として使用することはできません。`properties` オブジェクトで予約キーを使用すると、「Invalid 'properties' field」というエラーが返されます。

| プロパティ | 予約キー |
| --- | --- |
| カスタムイベント | `time` および `event_name` | 
| 購入イベント |`time`、`product_id`、`quantity`、`event_name`、`price`、`currency` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## カスタムイベントプロパティの使用

カスタムイベントプロパティは、キャンペーンのトリガー条件の絞り込み、コンバージョンのトラッキング、およびメッセージングのパーソナライズに使用できます。

### メッセージのトリガー

カスタムイベントプロパティを使用して、特定のキャンペーンやキャンバスのオーディエンスをさらに絞り込みます。たとえば、e コマースアプリケーションがあり、ユーザーがカートを放棄したときにメッセージを送信したい場合、`price` のカスタムイベントプロパティを追加して、ターゲットオーディエンスを改善し、キャンペーンのパーソナライゼーションを向上させることができます。

![放棄カートのカスタムイベントプロパティフィルター。2つのフィルターが AND 演算子で組み合わされ、価格が100ドルから200ドルの間でカートを放棄したユーザーにこのキャンペーンを送信します]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

ネストされたカスタムイベントプロパティも[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)でサポートされています。

![放棄カートのカスタムイベントプロパティフィルター。カート内のいずれかのアイテムの価格が100ドルを超える場合に1つのフィルターが選択されます。]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### メッセージのパーソナライズ

メッセージングテンプレート内でのパーソナライゼーションにもカスタムイベントプロパティを使用できます。トリガーイベントを持つ[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)を使用するキャンペーンでは、そのイベントのカスタムイベントプロパティをメッセージングのパーソナライゼーションに使用できます。

たとえば、ゲームアプリがあり、レベルをクリアしたユーザーにメッセージを送信したい場合、そのレベルのクリアにかかった時間のプロパティでメッセージをさらにパーソナライズできます。この例では、[条件付きロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/)を使用して3つの異なるセグメントに対してメッセージがパーソナライズされています。`time_spent` というカスタムイベントプロパティは、``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` を呼び出すことでメッセージに含めることができます。

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
ユーザーがインターネットに接続していない場合、テンプレート化されたカスタムイベントプロパティを含むトリガーされたアプリ内メッセージ（例: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}）は失敗し、表示されません。
{% endalert %}

アプリ内メッセージをテンプレート化されたアプリ内メッセージとして配信する Liquid タグの完全なリストについては、[よくある質問]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages/)を参照してください。

#### フィルターに関する注意事項

- **API 呼び出し:** API 呼び出しを行い、「is blank」フィルターを使用する場合、カスタムイベントプロパティは呼び出しから除外されると「blank」と見なされます。たとえば、`"event_property": ""` を含めた場合、ユーザーは「not blank」と見なされます。
- **整数:** 数値のカスタムイベントプロパティでフィルタリングする際、数値が非常に大きい場合は「exactly」フィルターを使用しないでください。数値が大きすぎると、特定の桁数で丸められる可能性があり、フィルターが期待どおりに機能しない場合があります。

### セグメンテーション

イベントプロパティセグメンテーションを使用して、実行されたカスタムイベントとそれらのイベントに関連するプロパティに基づいてユーザーをターゲットにします。これにより、購入およびカスタムイベントによるセグメンテーション時のフィルタリングオプションが増えます。

カスタムイベントのイベントプロパティは、それらを使用するセグメントに対してリアルタイムで更新されます。プロパティは、**データ設定** > **カスタムイベント**に移動し、関連するカスタムイベントの**プロパティを管理**を選択することで管理できます。特定のセグメントフィルターで使用されるカスタムイベントプロパティには、最大30日間のルックバック履歴があります。

#### セグメンテーション用のイベントプロパティの追加

イベントプロパティの頻度と最新性に基づいてセグメントを作成するには、「Edit Custom Event Property Segmentation」[ユーザー権限]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage)が必要です。

{% multi_lang_include deprecations/user_permissions.md %}

デフォルトでは、ワークスペースごとに20個のセグメント可能なイベントプロパティを設定できます。この制限を引き上げるには、Braze アカウントマネージャーにお問い合わせください。

セグメンテーション用のイベントプロパティを追加するには、以下の手順を実行します。

1. カスタムイベントに移動し、**プロパティを管理**を選択します。
2. **セグメンテーションを有効にする**トグルを選択して、セグメンテーション用のイベントプロパティを追加します。セグメンテーション時に追加のフィルタリングオプションにアクセスできます。

イベントプロパティセグメンテーションフィルターには以下が含まれます。

- 過去 Y 日間に、プロパティ A の値が B であるカスタムイベントを X 回実行した。
- 過去 Y 日間に、プロパティ A の値が B である購入を X 回行った。
- 1日から30日の範囲内でセグメント化する機能を追加します。

![プロパティ「number of items」の値が2で、過去30暦日間に1回以上の「Abandoned Cart」を持つフィルターグループ。]({% image_buster /assets/img/nested_object3.png %})

データは、有効にした後の特定のイベントプロパティに対してのみ記録され、イベントプロパティはその日付以降のみ利用可能です。

#### データポイント

サブスクリプション使用量に関して、以下のフィルターでセグメンテーション用に有効化されたカスタムイベントプロパティは、カスタムイベント自体でカウントされるデータポイントに加えて、すべて個別のデータポイントとしてカウントされます。

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### キャンバスのエントリプロパティとイベントプロパティ

{% multi_lang_include canvas_entry_event_properties.md %}

### ネストされたオブジェクト {#nested-objects}

ネストされたオブジェクト（別のオブジェクト内のオブジェクト）を使用して、カスタムイベントおよび購入のプロパティとしてネストされた JSON データを送信できます。このネストされたデータは、メッセージ内のパーソナライズされた情報のテンプレート化、メッセージ送信のトリガー、およびユーザーのセグメンテーションに使用できます。

詳細については、[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/)の専用ページを参照してください。

## カスタムイベントプロパティのストレージ

カスタムイベントプロパティは、ターゲティングの精度を高め、メッセージをよりパーソナライズされたものにするために設計されています。カスタムイベントプロパティは、Braze 内で短期および長期の両方で保存できます。

イベントプロパティの値に基づいてセグメント化するには、2つの方法があります。

1. **30日以内:** Braze セグメント内で、特定のイベントプロパティ値の頻度と最新性に基づいたイベントプロパティセグメンテーションを使用できます。このオプションはデータ使用量に影響します。<br><br>
2. **30日以内および30日を超える場合:** 短期および長期の両方のイベントプロパティセグメンテーションに対応するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用できます。この機能は、過去2年間にトラッキングされたカスタムイベントとイベントプロパティに基づいてユーザーをセグメント化します。このオプションはデータ使用量に影響しません。

特定のニーズに応じた最適なアプローチについては、Braze カスタマーサクセスマネージャーにお問い合わせください。