---
nav_title: 購入イベント
article_title: 購入イベント
page_order: 3
page_type: reference
description: "このリファレンス記事では、購入イベントとプロパティ、その使用方法、セグメンテーション、関連する分析の確認方法などについて説明します。"
search_rank: 3
---

# 購入イベント

> このページでは、購入イベントとプロパティ、その使用方法、セグメンテーション、関連する分析の確認方法などについて説明します。

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

購入イベントは、ユーザーが行った購入アクションであり、アプリ内購入を記録し、各ユーザープロファイルの生涯価値 (LTV) を確立するために使用されます。これらのイベントはチームで設定する必要があります。購入イベントをログに記録することで、数量やタイプなどのプロパティを追加でき、これらのプロパティに基づいてユーザーをさらにターゲティングできます。

## 購入イベントのログ記録

購入をログに記録するには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を通じて[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を渡すか、以下に記載されている SDK ライブラリのいずれかを使用します。

{% alert note %}
購入イベントプロパティは、[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#expected-format)と同じデータタイプを使用します。
{% endalert %}

以下は、さまざまなプラットフォームで購入をログに記録するために使用される方法の一覧です。これらのページでは、購入イベントにプロパティや数量を追加する方法についてのドキュメントも確認できます。これらのプロパティに基づいてユーザーをさらにターゲティングできます。

- [Android および FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [.NET MAUI (旧 Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## 購入データの表示

購入イベントの設定とログ記録を開始した後、ユーザーのプロファイルの[概要タブ]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#overview-tab)でこの購入データを確認できます。

## 購入データの使用

Braze では、購入データをいくつかの方法で使用できます。

- **[セグメンテーション](#purchase-event-segmentation):** 購入データを使用して、購入行動に基づいたユーザーセグメントを作成します。
- **[パーソナライゼーション](#personalization):** 購入データを使用して、ユーザーへのメッセージをパーソナライズします。
- **[メッセージのトリガー](#trigger-messages):** 購入イベントに基づいてメッセージがトリガーされるように設定します。
- **[分析](#analytics):** 購入データを分析して、ユーザーの行動やマーケティングキャンペーンの効果に関するインサイトを得ます。

### セグメンテーション {#purchase-event-segmentation}

ログに記録された購入イベントに基づいて、任意の数やタイプのフォローアップキャンペーンをトリガーできます。たとえば、過去30日間に購入を行ったユーザーのセグメントや、一定額以上を支出したユーザーのセグメントを作成できます。

ユーザーをターゲティングする際に、以下のセグメンテーションフィルターを使用できます。

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

各フィルターの詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)用語集を参照し、「Purchase behavior」でフィルタリングしてください。

![ちょうど3回購入したユーザーのフィルタリング]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %} 
特定の購入が発生した回数でセグメンテーションを行うには、その購入を[増分カスタム属性]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage)として個別に記録してください。
{% endalert %}

### パーソナライゼーション

ユーザーから収集する他のタイプのデータと同様に、購入データを使用して Liquid を通じてメッセージングをパーソナライズできます。たとえば、ユーザーが購入した製品に類似した製品を推薦するパーソナライズされたメールを送信できます。

ユーザーが最後に購入した製品名を保存する `last_purchased_product` という購入イベントプロパティがあるとします。このプロパティを使用して、次のようにメールメッセージをパーソナライズできます。

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

この例では、`last_purchased_product` プロパティに基づいてメッセージがパーソナライズされます。ユーザーが最後に購入した製品が「Running Shoes」の場合、ランニングショーツとウォーターボトルを推薦するメッセージが届きます。最後の製品が「Yoga Mat」の場合、ヨガブロックとストラップを推薦するメッセージが届きます。`last_purchased_product` がそれ以外の場合は、一般的なお礼のメッセージが届きます。

### メッセージのトリガー

一般的なユースケースとして、ユーザーが購入を行ったときにメールなどのメッセージを自動的に送信することがあります。たとえば、お礼のメッセージや次回購入用の割引コードを送信できます。

これを行うには、アクションベースのキャンペーンまたはキャンバスを作成し、トリガーアクションを**購入する**に設定します。購入した製品や購入金額など、トリガーの追加条件を指定することもできます。

トリガーされたメッセージを Liquid でパーソナライズすることもできます。以下の例では、`${purchase_product_name}` は、Braze の設定で購入した製品名を保存する実際の属性名に置き換えるカスタム属性です。

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### 分析

セグメンテーション用の購入指標のトラッキングに加えて、Braze は各製品の購入数と経時的な収益も記録します。これは、最も人気のある製品を特定したり、プロモーションキャンペーンが売上に与える影響を測定したりするのに役立ちます。

このデータは[収益レポート]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data)ページで確認できます。

### 収益の計算

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
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
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">ユーザーあたりの生涯価値</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
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

#### 通貨換算

購入イベントが米ドル以外の通貨でログに記録された場合、Braze は [Open Exchange Rates](http://openexchangerates.org) の為替レートを使用して金額を米ドルに換算します。これらのレートは24時間ごとに更新されます。為替レートはキャッシュされるため、特に急激に変動している通貨の場合、リアルタイムの市場レートとわずかな差異が生じる可能性があります。

#### 生涯収益の計算

Braze は購入イベントを使用して、ユーザーの生涯収益（生涯価値または LTV とも呼ばれます）を計算します。これは、顧客との将来の関係全体に帰属する純利益の予測です。これにより、顧客獲得やリテンション戦略について情報に基づいた意思決定を行うことができます。

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Braze でユーザーの LTV を把握するための主な場所は2つあります。

- 各アプリおよびサイトの*生涯収益*や*ユーザーあたりの生涯価値*などの全体的な指標については、[収益レポート]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data)を参照してください。
- 特定のユーザーの生涯収益を把握するには、そのユーザーの[ユーザープロファイル]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab)を参照してください。

##### 返金が生涯収益に与える影響

購入イベントを使用して購入データをトラッキングする場合、返金は負の `price` プロパティを持つ Braze 購入イベントをログに記録することでトラッキングする必要があります。このアプローチにより、生涯収益の正確な合計が維持されます。

ただし、返金は追加の購入イベントとしてカウントされることに注意してください。次の例を考えてみましょう。Sam が最初の購入として12ドルを支払いましたが、購入の一部を返品して5ドルの返金を受けました。Sam のプロファイルには以下が記録されます。

- 12ドルの価格の購入1件
- -5ドルの価格の購入1件
- 生涯収益7ドル

Sam のプロファイルには2つの購入イベントがありますが、実際には1回しか購入していません。ユーザーの購入回数に基づいて構築されたセグメントやユースケースがある場合、これは重要な考慮事項です。頻繁な返金は、ユーザーのプロファイルの購入数を水増しします。

## 購入イベントプロパティ {#purchase-properties}

購入イベントプロパティを使用すると、購入にプロパティを設定でき、トリガー条件のさらなる絞り込み、メッセージングのパーソナライゼーションの向上、生データエクスポートによるより高度な分析の生成に使用できます。プロパティの値のタイプ（文字列、数値、ブール値、日付）はプラットフォームによって異なり、多くの場合キーと値のペアとして割り当てられます。

{% alert warning %}
以下のキーは予約されており、購入イベントプロパティ名として使用できません: `time`、`product_id`、`quantity`、`event_name`、`price`、`currency`。`properties` オブジェクトで予約キーを使用すると、「Invalid 'properties' field」というエラーが返されます。
{% endalert %}

たとえば、e コマースアプリケーションがあり、購入後にユーザーにメッセージを送信したい場合、`brand_name` の購入イベントプロパティを追加することで、ターゲットオーディエンスをさらに改善し、キャンペーンのパーソナライゼーションを向上させることができます。

**購入イベントプロパティに基づくトリガーの例:**

![ブランド名が HeadphoneMart のヘッドフォンを購入したユーザーにキャンペーンを送信するアクションベースの配信設定]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

詳細については、[購入プロパティオブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object)を参照してください。

### イベントプロパティのセグメンテーション

イベントプロパティのセグメンテーションを使用すると、実行されたカスタムイベントだけでなく、それらのイベントに関連付けられたプロパティに基づいてもユーザーをターゲティングできます。これにより、購入やカスタムイベントのセグメンテーション時に追加のフィルタリングオプションが利用できます。

![購入イベントプロパティのセグメンテーションフィルター。特定の購入イベントプロパティ値に基づいてユーザーをフィルタリングするオプションが表示されています（例: 特定の期間内に特定のプロパティを持つ製品を購入したユーザーのフィルタリング）。]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

これらのセグメンテーションフィルターには以下が含まれます。
- プロパティ Y の値が V であるカスタムイベントを過去 Y 日間に X 回実行した
- プロパティ Y の値が V である購入を過去 Y 日間に X 回行った
- すべての購入、イベント、および購入やイベント内のプロパティに対して1〜30日間のセグメンテーションを追加

[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)とは異なり、使用されるセグメントはリアルタイムで更新され、無制限のセグメント数をサポートし、最大30日間の振り返り履歴を提供しますが、データポイントが発生します。追加のデータポイント料金が発生するため、カスタムイベントのイベントプロパティを有効にするには、Braze カスタマーサクセスマネージャーにお問い合わせください。

承認されると、ダッシュボードの**データ設定** > **カスタムイベント**で**プロパティを管理**を選択して追加のプロパティを追加できます。これらのイベントプロパティは、キャンペーンまたはキャンバスビルダーのターゲットステップで使用できます。

### キャンバスのエントリプロパティとイベントプロパティ

{% multi_lang_include canvas_entry_event_properties.md %}

### 注文レベルでの購入のログ記録

製品レベルではなく注文レベルで購入をログに記録するには、注文名または注文カテゴリを `product_id` として使用します。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。

### 製品 ID の命名規則

Braze では、購入オブジェクトの `product_id` に関する一般的な命名規則を提供しています。`product_id` を選択する際、Braze では、この `product_id` でログに記録されたすべてのアイテムをグループ化する目的で、SKU ではなく製品名や製品カテゴリなどのシンプルな名前を使用することを推奨しています。

これにより、セグメンテーションやトリガーで製品を簡単に識別できるようになります。

## 購入イベントのブロックリスト

データポイントを過剰にログに記録する購入イベント、マーケティング戦略にとって不要になった購入イベント、または誤って記録された購入イベントが見つかることがあります。このデータが Braze に送信されないようにするには、エンジニアリングチームがアプリまたは Web サイトのバックエンドから削除する作業を行っている間に、カスタムデータオブジェクトをブロックリストに登録できます。

Braze ダッシュボードでは、**データ設定** > **製品**からブロックリストを管理できます。詳細については、[カスタムデータの管理]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/)を参照してください。