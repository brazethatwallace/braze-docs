---
nav_title: 購入イベント
article_title: 購入イベント
page_order: 3
page_type: reference
description: "このリファレンス記事では、購入イベントとプロパティ、その使用方法、セグメンテーション、関連する分析を表示する場所などについて説明します。"
search_rank: 3
---

# 購入イベント {#purchase-events}

> このページでは、購入イベントとプロパティ、その使用方法、セグメンテーション、関連する分析の表示場所などについて説明します。

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

購入イベントは、ユーザーが実行した購入アクションであり、アプリ内購入を記録し、ユーザープロファイルごとにLTV（LTV）を確立するために使用されます。これらのイベントは、チームが設定する必要があります。購入イベントをログに記録すると、数量やタイプなどのプロパティを追加できるため、それらのプロパティに基づいてユーザーのターゲットをさらに絞り込むことができます。

## 購入イベントの記録 {#log-purchase-events}

[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)を[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に渡すか、次のセクションに記載されているSDKライブラリのいずれかを使用して、購入を記録できます。

{% alert note %}
購入イベントプロパティは、[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#expected-format)と同じデータ型を使用します。
{% endalert %}

以下は、さまざまなプラットフォームで購入を記録するために使用されるメソッドの一覧です。これらのページでは、購入イベントにプロパティや数量を追加する方法についてのドキュメントも確認できます。これらのプロパティに基づいて、ユーザーをさらにターゲティングできます。

- [Android および FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics#purchase-events--revenue-tracking)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=unity)
- [.NET MAUI（旧 Xamarin）]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin#purchase-events--revenue-tracking)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=roku)

## 購入データの表示 {#view-purchase-data}

購入イベントの設定とログ記録を開始すると、[概要タブ]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab)でユーザープロファイルの購入データを表示できます。

## 購入データの使用 {#use-purchase-data}

Brazeでは、購入データをいくつかの方法で活用できます。

- **[セグメンテーション](#purchase-event-segmentation):** 購入データを使用して、購買行動に基づいたユーザーのセグメントを作成できます。
- **[パーソナライゼーション](#personalization):** 購入データを使用して、ユーザーへのメッセージをパーソナライズできます。
- **[メッセージのトリガー](#trigger-messages):** 購入イベントに基づいてメッセージをトリガーするよう設定できます。
- **[分析](#analytics):** 購入データを分析して、ユーザーの行動やマーケティングキャンペーンの効果に関するインサイトを得ることができます。

### セグメンテーション {#purchase-event-segmentation}

記録された購入イベントに基づいて、あらゆる数やタイプのフォローアップキャンペーンをトリガーできます。たとえば、過去30日間に購入を行ったユーザーのセグメントや、一定額以上を支出したユーザーのセグメントを作成できます。

ユーザーをターゲティングする際、以下のセグメンテーションフィルターが利用可能です。

- First Made Purchase
- First Purchase For App
- Last Purchased Product
- Money Spent
- Purchased Product
- Total Number of Purchases
- X Money Spent in Y Days
- X Product Purchased in Y Days
- X Purchase Property in Y Days
- X Purchases in Last Y Days

各フィルターの詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)用語集を参照し、「Purchase behavior」でフィルターしてください。

![ちょうど3回購入したユーザーをフィルタリングする例]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
特定の購入が発生した回数でセグメントを作成するには、その購入を[インクリメントするカスタム属性]({{site.baseurl}}/developer_guide/analytics#custom-attribute-storage)として個別に記録してください。
{% endalert %}

### パーソナライゼーション {#personalization}

ユーザーから収集する他のタイプのデータと同様に、購入データを使用してLiquidを通じたメッセージングをパーソナライズできます。たとえば、ユーザーが購入した商品に類似した商品をおすすめするパーソナライズされたメールを送信できます。

`last_purchased_product` という購入イベントプロパティがあり、ユーザーが最後に購入した商品の名前が格納されているとします。このプロパティを使用して、次のようにメールメッセージをパーソナライズできます。

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

この例では、メッセージが `last_purchased_product` プロパティに基づいてパーソナライズされています。ユーザーが最後に購入した商品が「Running Shoes」であれば、ランニングショーツやウォーターボトルをおすすめするメッセージが届きます。最後の商品が「Yoga Mat」であれば、ヨガブロックやストラップをおすすめするメッセージが届きます。`last_purchased_product` がそれ以外の場合は、汎用的な感謝メッセージが届きます。

### メッセージのトリガー {#trigger-messages}

一般的なユースケースとして、ユーザーが購入した際にメールなどのメッセージを自動的に送信することがあります。たとえば、お礼のメッセージや今後の購入に使える割引コードを送信できます。

そのためには、アクションベースのキャンペーンまたはキャンバスを作成し、トリガーアクションを**購入する**に設定します。購入した商品や購入金額など、トリガーの追加条件も指定できます。

トリガーメッセージをLiquidでパーソナライズすることもできます。以下の例では、`${purchase_product_name}` は、Brazeの設定で購入した商品名を格納する実際の属性名に置き換えるカスタム属性です。

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### 分析 {#analytics}

セグメンテーションのための購入指標のトラッキングに加えて、Brazeでは各商品の購入数や経時的な収益も記録されます。これにより、最も人気のある商品を特定したり、プロモーションキャンペーンが売上に与える影響を測定したりできます。

このデータは[収益レポート]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#exporting-revenue-data)ページで確認できます。

### 収益の計算 {#revenue-calculations}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="収益の計算">
  <caption>収益の計算</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">生涯収益</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">ユーザーあたりのLTV</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='LTV Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">1日あたりの平均収益</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">1日あたりの購入数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">ユーザーあたりの1日の収益</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### 通貨換算 {#currency-conversion}

購入イベントがUSD以外の通貨で記録された場合、Brazeは[Open Exchange Rates](http://openexchangerates.org)の為替レートを使用して金額をUSDに換算します。これらのレートは24時間ごと（東部時間の午前4時頃）に更新されます。為替レートはキャッシュされるため、特に急激な変動がある通貨では、リアルタイムの市場レートとわずかな差異が生じる場合があります。

#### 生涯収益の計算 {#lifetime-revenue-calculation}

Brazeは購入イベントを使用して、ユーザーの生涯収益（LTVまたはLTVとも呼ばれます）を計算します。これは、顧客との将来の関係全体に帰属する純利益の予測です。これにより、顧客獲得やリテンション戦略について十分な情報に基づいた意思決定を行うことができます。

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$

BrazeでユーザーのLTVを把握するための主な場所が2つあります。

- 各アプリやサイトの*生涯収益*や*ユーザーあたりのLTV*などの全体的な指標については、[収益レポート]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#exporting-revenue-data)を参照してください。
- 特定のユーザーの生涯収益を確認するには、そのユーザーの[ユーザープロファイル]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab)を参照してください。

##### 返金が生涯収益に与える影響 {#impact-of-refunds-on-lifetime-revenue}

購入イベントを使用して購入データをトラッキングする場合、返金はBrazeの購入イベントで負の `price` プロパティを記録することでトラッキングしてください。このアプローチにより、生涯収益の合計が正確に維持されます。

ただし、返金は追加の購入イベントとしてカウントされる点に注意してください。以下の例を考えてみましょう。Samが最初に12ドルで購入しましたが、購入の一部を返品して5ドルの返金を受けました。Samのプロファイルには以下が記録されます。

- 12ドルの購入1件
- -5ドルの購入1件
- 生涯収益7ドル

Samのプロファイルには2つの購入イベントが記録されていますが、実際の購入は1回のみです。ユーザーの購入回数に基づくセグメントやユースケースがある場合、この点を考慮することが重要です。頻繁な返金は、ユーザーのプロファイルの購入数を膨らませることになります。

## 購入イベントプロパティ {#purchase-properties}

購入イベントプロパティを使用すると、購入にプロパティを設定でき、トリガー条件のさらなる絞り込み、メッセージングのパーソナライゼーションの向上、生データエクスポートによるより高度な分析の生成に使用できます。プロパティの値のタイプ（文字列、数値、ブール値、日付）はプラットフォームによって異なり、多くの場合キーと値のペアとして割り当てられます。

{% alert warning %}
以下のキーは予約されており、購入イベントプロパティ名として使用できません: `time`、`product_id`、`quantity`、`event_name`、`price`、`currency`。`properties` オブジェクトで予約キーを使用すると、「Invalid 'properties' field」というエラーが返されます。
{% endalert %}

たとえば、eコマースアプリケーションがあり、購入後にユーザーにメッセージを送信したい場合、`brand_name` の購入イベントプロパティを追加することで、ターゲットオーディエンスをさらに改善し、キャンペーンのパーソナライゼーションを向上させることができます。

**購入イベントプロパティに基づくトリガーの例:**

![ブランド名がHeadphoneMartのヘッドフォンを購入したユーザーにキャンペーンを送信するアクションベースの配信設定]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

詳細については、[購入プロパティオブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-properties-object)を参照してください。

### イベントプロパティのセグメンテーション {#event-property-segmentation}

イベントプロパティのセグメンテーションを使用すると、実行されたカスタムイベントだけでなく、それらのイベントに関連付けられたプロパティに基づいてもユーザーをターゲティングできます。これにより、購入やカスタムイベントのセグメンテーション時に追加のフィルタリングオプションが利用できます。

![購入イベントプロパティのセグメンテーションフィルター。特定の購入イベントプロパティ値に基づいてユーザーをフィルタリングするオプションが表示されています（例: 特定の期間内に特定のプロパティを持つ製品を購入したユーザーのフィルタリング）。]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

これらのセグメンテーションフィルターには以下が含まれます。
- プロパティYの値がVであるカスタムイベントを過去Y日間にX回実行した
- プロパティYの値がVである購入を過去Y日間にX回行った
- すべての購入、イベント、および購入やイベント内のプロパティに対して1〜30日間のセグメンテーションを追加

[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)とは異なり、使用されるセグメントはリアルタイムで更新され、無制限のセグメント数をサポートし、最大30日間の振り返り履歴を提供しますが、データポイントが発生します。追加のデータポイント料金が発生するため、カスタムイベントのイベントプロパティを有効にするには、Brazeカスタマーサクセスマネージャーにお問い合わせください。

承認されると、ダッシュボードの**データ設定** > **カスタムイベント**で**プロパティを管理**を選択して追加のプロパティを追加できます。これらのイベントプロパティは、キャンペーンまたはキャンバスビルダーのターゲットステップで使用できます。

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

### キャンバスのエントリプロパティとイベントプロパティ {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### 注文レベルでの購入のログ記録 {#log-purchases-at-the-order-level}

製品レベルではなく注文レベルで購入をログに記録するには、注文名または注文カテゴリを `product_id` として使用します。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions)を参照してください。

### 製品IDの命名規則 {#product-id-naming-conventions}

Brazeでは、購入オブジェクトの `product_id` に関する一般的な命名規則を提供しています。`product_id` を選択する際、Brazeでは、この `product_id` でログに記録されたすべてのアイテムをグループ化する目的で、SKUではなく製品名や製品カテゴリなどのシンプルな名前を使用することを推奨しています。

これにより、セグメンテーションやトリガーで製品を簡単に識別できるようになります。

## 購入イベントのブロックリスト登録 {#blocklist-purchase-events}

データポイントの記録が多すぎる、マーケティング戦略に不要になった、または誤って記録されたなどの理由で、購入イベントを特定することがあります。このデータが Braze に送信されないようにするには、開発チームがアプリや Web サイトのバックエンドから該当データを削除する作業を進めている間に、カスタムデータオブジェクトをブロックリストに登録できます。

Braze ダッシュボードでは、**[データ設定]** > **[製品]** からブロックリストを管理できます。詳しくは[カスタムデータの管理]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)をご覧ください。