---
nav_title: e コマースのユースケース
article_title: e コマースのユースケース
alias: /ecommerce_use_cases/
page_order: 4
description: "このリファレンス記事では、e コマースマーケター向けに特別に設計された、事前構築済みの Braze テンプレートについて説明します。これにより、重要な戦略の実装が容易になります。"
toc_headers: h2
---

# e コマース推奨イベントの使い方

> このページでは、Braze の e コマースキャンバステンプレートの使い方を含め、プラットフォーム全体で e コマース推奨イベントをどのように、どこで使用できるかについて説明します。

{% alert important %}
[e コマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)は現在早期アクセス中です。この早期アクセスへの参加にご興味がある場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しい Shopify コネクターを使用している場合、e コマース推奨イベントは統合を通じて自動的に利用可能になります。
{% endalert %}

## キャンバステンプレートの使用

キャンバステンプレートを使用するには:
1. **メッセージング** > **キャンバス**に移動します。
2. **キャンバスを作成** > **キャンバステンプレートを使用**を選択します。
3. **Braze テンプレート**タブで使用したいテンプレートを探します。テンプレート名を選択するとプレビューできます。
4. 使用したいテンプレートの**テンプレートを適用**を選択します。<br><br>![「キャンバステンプレート」ページが「Braze テンプレート」タブで開かれ、最近使用したテンプレートと選択可能な Braze テンプレートのリストが表示されています。]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## e コマースキャンバステンプレート

Braze は4つの e コマースキャンバステンプレートを提供しています。

{% multi_lang_include canvas/ecommerce_templates.md %}

## メッセージのパーソナライゼーション

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) は、Braze で使用される強力なテンプレート言語で、顧客向けにダイナミックでパーソナライズされたコンテンツを作成できます。Liquid タグを使用することで、顧客データ、製品情報、その他の変数に基づいてメッセージをカスタマイズし、ショッピング体験を向上させてエンゲージメントを促進できます。

### Liquid の主な機能

- **ダイナミックコンテンツ:** 名前、注文の詳細、好みなどの顧客固有の情報をメッセージに挿入します。
- **条件付きロジック:** if/else 文を使用して、特定の条件（顧客のロケーションや購入履歴など）に基づいて異なるコンテンツを表示します。
- **ループ:** 製品や顧客データのコレクションを反復処理して、アイテムのリストやグリッドを表示します。

### Liquid の使い方

Liquid タグを使用してメッセージのパーソナライズを始めるには、以下のリソースを参照してください。

- 事前定義された Liquid タグを含む [Shopify データ]({{site.baseurl}}/shopify_features/#shopify-data)リファレンス
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)

## セグメンテーション

Braze セグメントを使用して、特定の属性や動作に基づいてターゲット顧客セグメントを作成し、パーソナライズされたメッセージングやキャンペーンを配信できます。この強力な機能により、適切なオーディエンスに適切なメッセージを適切なタイミングで届けることで、顧客と効果的にエンゲージできます。

セグメントの使い方の詳細については、[Braze セグメントについて]({{site.baseurl}}/user_guide/audience/segments#about-braze-segments)をご覧ください。

### 推奨イベント

e コマースイベントは[推奨イベント]({{site.baseurl}}/recommended_events/)に基づいています。
推奨イベントはより明確に定義されたカスタムイベントであるため、任意の[カスタムイベントフィルター]({{site.baseurl}}/user_guide/data/activation/events/custom_events#segmentation-filters)を選択して、推奨 e コマースイベント名を検索できます。

### e コマースフィルター

セグメンター内の **Ecommerce** セクションに移動して、**Ecommerce Source** や **Total Revenue** などの e コマースフィルターでユーザーをセグメントします。

e コマースフィルターとその定義のリストについては、[セグメントフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を参照し、「eCommerce」検索カテゴリを選択してください。

![「Ecommerce」フィルターが表示されたセグメントフィルターのドロップダウン。]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## ネストされたイベントプロパティ

ネストされたイベントプロパティでセグメントするには、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension#why-use-segment-extensions)を活用できます。例えば、セグメントエクステンションを使用して、過去90日間に製品「SKU-123」を購入したユーザーを見つけることができます。

## 分析

### カスタムイベントレポート

e コマース推奨イベントのボリュームは[カスタムイベントレポート]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics)で追跡できます。**カスタムイベントを実行**でフィルターし、[e コマース推奨イベント名]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events)を指定して、時間の経過に伴うパフォーマンスを確認します。

![6つの選択されたイベントの結果を表示するカスタムイベントチャート。]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### ダッシュボード

#### コンバージョンダッシュボード

「Places Order」コンバージョンイベントを使用してキャンペーンまたはキャンバスを起動した後、対応する[コンバージョンレポート]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#setting-up-your-report)を作成してパフォーマンスを追跡できます。

![キャンペーンとキャンバス、および関連するコンバージョン統計を含むコンバージョン詳細テーブル。]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### e コマース収益ダッシュボード

ユーザーが注文する前に最後にインタラクションしたキャンペーンまたはキャンバスに帰属する収益のインサイトを得るには、[e コマース収益ダッシュボード]({{site.baseurl}}/ecommerce_revenue_dashboard/)を使用してコンバージョン時間枠を選択します。

### 収益レポート

これらの新しいイベントからのデータを分析するには、[ダッシュボードビルダー]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/)に移動し、[**eCommerce Revenue - Last Touch Attribution** ダッシュボード]({{site.baseurl}}/ecommerce_revenue_dashboard/)を表示します。