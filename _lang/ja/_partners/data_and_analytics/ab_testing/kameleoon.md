---
nav_title: Kameleoon
article_title: Kameleoon
description: "KameleoonとBrazeを統合する方法について説明します"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com)は、実験、AI搭載のパーソナライゼーション、フィーチャーフラグ管理機能を1つの統一プラットフォームに備えた最適化ソリューションです。

## 前提条件 {#prerequisites}

始める前に、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Kameleoonアカウント | このパートナーシップを利用するには、Kameleoonアカウントが必要です。|
| Brazeアカウント | [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)がWebページに統合されたアクティブなBrazeアカウントが必要です。また、イベントプロパティのセグメンテーションを有効にする必要があります。リクエストするには、[考慮事項](#considerations)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

Kameleoonは、実験やパーソナライゼーションキャンペーンに参加しているユーザーを識別するために、カスタムイベントをBrazeに送信します。これにより、より精密なターゲティングとパーソナライズされたメッセージングが可能になります。

## Kameleoonの統合 {#integrating-kameleoon}

この統合は、Kameleoonのengine.jsを通じてJavaScriptトラッカーとして動作します。Kameleoonのプラットフォーム内から有効にできます。

### ステップ1:Kameleoonの統合ページに移動する {#step-1-go-to-the-kameleoon-integrations-page}

Kameleoonアプリで、サイドバーの**Admin**、次に**Integrations**を選択します。

![Kameleoonプラットフォームの管理パネル。]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### ステップ2:Brazeツールをインストールする {#step-2-install-the-braze-tool}

デフォルトでは、Brazeツールはインストールされていません。Brazeアイコンを探し、**Install the tool**を選択します。![下向き矢印のある灰色の四角。]({% image_buster /assets/img/kameleoon/img_2.png %})

Brazeツールを有効にするプロジェクトを選択し、KameleoonのデータがBrazeに正しくレポートされるようにします。

![KameleoonのBrazeツールアイコン。]({% image_buster /assets/img/kameleoon/img_3.png %})

ツールの設定後、**Validate**を選択すると、設定パネルが閉じます。Brazeツールのアイコンの横に**ON**トグルが表示され、ツールが設定されているプロジェクト数が示されます。

![Kameleoonで「On」に切り替えられたBrazeツール。]({% image_buster /assets/img/kameleoon/img_4.png %})

### ステップ3:BrazeをKameleoonキャンペーンに関連付ける {#step-3-associate-braze-with-kameleoon-campaigns}

#### グラフィック/コードエディターの場合 {#in-the-graphiccode-editor}

実験を完了するには、**Integrations**ステップを選択してBrazeをトラッキングツールとして設定し、**Braze**を選択します。

![利用可能なすべての統合を表示するKameleoonの統合ダッシュボード。アクティブな統合としてBrazeが含まれています。]({% image_buster /assets/img/kameleoon/img_5.png %})

Brazeは公開前のサマリーに記載されます。Kameleoonは自動的にデータをBrazeに送信するため、Braze内で直接分析やセグメンテーションに使用できます。

##### パーソナライゼーションの作成 {#personalization-creation}

**Personalization Creation**ページでは、レポートツールの中からBrazeを選択して、レポートをパーソナライズできます。

![Heap、Mixpanel、Clarityなどの統合を表示するレポートツールセクション。Brazeが選択されています。]({% image_buster /assets/img/kameleoon/img_6.png %})

##### フィーチャーフラグの作成 {#feature-flag-creation}

フィーチャーフラグ環境の**Integrations**セクションで統合を設定します。有効にしたい環境で有効化します。

![Kameleoonのフィーチャーフラグページ。利用可能な統合が表示されています。各パートナーに対して「Delivery rules」と「Feature experiments」の2つのスイッチがあります。]({% image_buster /assets/img/kameleoon/img_7.png %})

##### 結果ページ {#results-page}

Brazeが実験のレポートツールとして設定された後、Kameleoonの結果ページの**Experiment configuration**メニューでBrazeを選択（または選択解除）できます。

{% alert note %}
この統合には[ハイブリッド実装](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics)が必要で、Web SDKとのみ互換性があります。
{% endalert %}

![Kameleoonの結果ページのサイドパネル。]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

実験に関連付けられたレポートツールが表示されます。**Edit**を選択してこの選択を編集します。

### ステップ4:Braze内でKameleoonデータを分析・活用する {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

統合が設定されると、Kameleoonは**Experiment name**、**Experiment ID**、**Variation name**、**Variation ID**などのプロパティを持つ`kameleoon_exposure`というカスタムイベントをBrazeに送信します。

![Brazeのカスタムイベントユーザーログ。KameleoonからBrazeに受信されたイベントのペイロード例が表示されています。]({% image_buster /assets/img/kameleoon/img_9.png %})

このデータはカスタムイベントで表示でき、Kameleoonキャンペーンのエクスポージャーを特定するカスタムイベントレポートを作成し、イベントプロパティに基づくセグメンテーションを有効にできます。[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-groups)、[アクションベースのトリガー]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を通じて後続のキャンペーンやキャンバスを作成する際や、[セグメント]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)を作成する際にカスタムイベントを使用できます。

さらに、これらのイベントは[Currentsカスタムイベントオブジェクト]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)を通じてアクセスでき、包括的なレポートと分析が可能です。

## 考慮事項 {#considerations}

### イベントプロパティセグメンテーションのリクエスト {#request-event-property-segmentation}

イベントプロパティセグメンテーションを使用するには、事前にBrazeで有効化する必要があります。以下のテンプレートを使用して、Brazeのカスタマーサクセスマネージャーまたはサポートチームにアクセスをリクエストしてください。

   <table aria-label="イベントプロパティセグメンテーションのリクエスト">
     <caption>イベントプロパティセグメンテーションのリクエスト</caption>
   <thead>
      <tr>
         <th>フィールド</th>
         <th>詳細</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>件名</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>本文</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="イベントプロパティセグメンテーションのリクエスト" }

### Brazeデータポイント {#braze-data-points}

Kameleoon から Braze に送信されるカスタムイベント&#8212;セグメンテーション用に有効化されたイベントプロパティを含む&#8212;は、Brazeインスタンスにデータポイントを記録します。