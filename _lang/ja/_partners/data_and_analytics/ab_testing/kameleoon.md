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

開始する前に、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Kameleoonアカウント | このパートナーシップを利用するには、Kameleoonアカウントが必要です。|
| Brazeアカウント | Webページに[Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)が統合されたアクティブなBrazeアカウント。また、イベントプロパティセグメンテーションを有効にする必要があります。リクエストするには、[考慮事項](#considerations)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

KameleoonはカスタムイベントをBrazeに送信し、実験やパーソナライゼーションキャンペーンに参加しているユーザーを特定することで、より正確なターゲティングとパーソナライズされたメッセージングを可能にします。

## Kameleoonの統合 {#integrating-kameleoon}

この統合は、Kameleoonのengine.jsを介してJavaScriptトラッカーとして実行されます。Kameleoonのプラットフォーム内からすぐに有効にできます。

### ステップ 1: Kameleoon統合ページに移動する {#step-1-go-to-the-kameleoon-integrations-page}

Kameleoonアプリで、サイドバーの**Admin**を選択し、次に**Integrations**を選択します。

![Kameleoonプラットフォームの管理パネル。]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### ステップ 2: Brazeツールをインストールする {#step-2-install-the-braze-tool}

デフォルトでは、Brazeツールはインストールされていません。Brazeのアイコンを探し、**Install the tool**を選択します。![下向き矢印の付いた灰色の正方形。]({% image_buster /assets/img/kameleoon/img_2.png %})

Brazeツールを有効にするプロジェクトを選択し、KameleoonデータがBrazeに正しくレポートされるようにします。

![KameleoonのBrazeツールアイコン。]({% image_buster /assets/img/kameleoon/img_3.png %})

ツールを設定したら、**Validate**を選択すると、設定パネルが閉じます。Brazeツールのアイコンの横に**ON**トグルが表示され、ツールが設定されているプロジェクトの数も表示されます。

![Kameleoonで「On」に切り替えられたBrazeツール。]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}
この機能はベータ版です。[Kameleoonベータプログラム](https://help.kameleoon.com/account-and-team-management/join-beta-program/)に参加して、この統合の使用を開始してください。
{% endalert %}

### ステップ 3: BrazeをKameleoon キャンペーンに関連付ける {#step-3-associate-braze-with-kameleoon-campaigns}

#### グラフィック/コードエディターで {#in-the-graphiccode-editor}

実験を完了するには、**Integrations**ステップを選択してBrazeをトラッキングツールとして設定し、**Braze**を選択します。

![Kameleoonの統合ダッシュボード。アクティブな統合であるBrazeを含む、利用可能なすべての統合が表示されています。]({% image_buster /assets/img/kameleoon/img_5.png %})

公開前のサマリーにBrazeが記載されます。Kameleoonは自動的にデータをBrazeに送信し、Braze内で直接分析やセグメンテーションに使用できるようになります。

##### パーソナライゼーションの作成 {#personalization-creation}

**Personalization Creation**ページでは、レポートツールの中からBrazeを選択して、レポートをパーソナライズできます。

![Heap、Mixpanel、Clarityなどの統合を表示し、Brazeが選択された状態のレポートツールセクション。]({% image_buster /assets/img/kameleoon/img_6.png %})

##### フィーチャーフラグの作成 {#feature-flag-creation}

**Integrations**セクションで、フィーチャーフラグ環境での統合を設定します。アクティブにしたい環境で有効にします。

![Kameleoonのフィーチャーフラグページ。利用可能な統合が表示されています。各パートナーに「Delivery rules」と「Feature experiments」の2つのスイッチがあります。]({% image_buster /assets/img/kameleoon/img_7.png %})

##### 結果ページ {#results-page}

Brazeを実験のレポートツールとして設定した後、**Experiment configuration**メニューのKameleoon結果ページで選択（または選択解除）できます。

{% alert note %}
この統合には[ハイブリッド実装](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics)が必要で、Web SDKとのみ互換性があります。
{% endalert %}

![Kameleoonの結果ページのサイドパネル。]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

実験に関連付けられたレポートツールが表示されます。この選択を編集するには、**Edit**を選択します。

### ステップ 4: BrazeでKameleoonデータを分析・活用する {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

統合が設定されると、Kameleoonは`kameleoon_exposure`というカスタムイベントを、**Experiment name**、**Experiment ID**、**Variation name**、**Variation ID**などのプロパティとともにBrazeに送信します。

![Brazeのカスタムイベントユーザーログ。KameleoonからBrazeが受信したイベントのペイロード例が表示されています。]({% image_buster /assets/img/kameleoon/img_9.png %})

このデータをカスタムイベントで表示し、カスタムイベントレポートを作成してKameleoon キャンペーンへの露出を特定し、イベントプロパティに基づくセグメンテーションを有効にできます。カスタムイベントは、[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups)、[アクションベースのトリガー]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)、または[セグメントの作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)を通じて、後続またはリンクされたキャンペーンやキャンバスを作成する際に使用できます。

さらに、これらのイベントは[Currentsカスタムイベントオブジェクト]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)を介してアクセスでき、包括的なレポートと分析が可能になります。

## 考慮事項 {#considerations}

### イベントプロパティセグメンテーションのリクエスト {#request-event-property-segmentation}

イベントプロパティセグメンテーションを使用するには、事前にBrazeで有効にしておく必要があります。以下のテンプレートを使用して、Brazeカスタマーサクセスマネージャーまたはサポートチームにアクセスをリクエストしてください。

   <table aria-label="Request event property segmentation">
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
         <td>Request to Enable Event Property セグメントation for Kameleoon Integration</td>
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
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Request event property segmentation" }

### Brazeデータポイント {#braze-data-points}

KameleoonからBrazeに送信されるカスタムイベント（セグメンテーション用に有効化されたイベントプロパティを含む）は、Brazeインスタンスのデータポイントとして記録されます。