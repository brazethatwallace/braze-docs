---
nav_title: カード作成
article_title: カード作成
alias: /card_creation/
description: "この記事では、Campaign起動時またはキャンバスステップエントリ時と、初回インプレッション時のContent Cards作成の違いについて説明します。"
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# カード作成 {#card-creation}

> カードの作成タイミングを指定することで、新しいContent CardsのCampaignやCanvasステップに対してBrazeがオーディエンスの適格性とパーソナライゼーションを評価するタイミングを選択できます。

## 前提条件 {#prerequisites}

この機能を利用するには、以下の最小SDKバージョンにアップグレードする必要があります。

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

SDKをアップグレードした後、モバイルユーザーはアプリをアップグレードする必要があります。CampaignまたはCanvasのオーディエンスをフィルタリングして、[これらの最小アプリバージョンのユーザーのみをターゲット]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)にすることができます。

## 概要 {#overview}

{% tabs %}
{% tab Campaign %}

スケジュール配信で新しい[Content CardsのCampaign]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/)を作成する際、**Delivery**ステップでBrazeがカードを作成するタイミングを選択できます。

![スケジュールされたContent Cardsの配信を編集する際のContent Cardsコントロールセクション。]({% image_buster /assets/img_archive/card_creation.png %})

以下のオプションが利用可能です。

- **At campaign launch:** Content Cardsの以前のデフォルト動作です。BrazeはCampaign起動時にオーディエンスの適格性とパーソナライゼーションを計算し、カードを作成してユーザーがアプリを開くまで保存します。
- **At first impression（推奨）:** ユーザーが次にアプリを開いた（新しい[セッション](https://www.braze.com/resources/articles/whats-an-app-session-anyway)を開始した）とき、BrazeはそのユーザーがどのContent Cardsの対象であるかを判定し、Liquidやコネクテッドコンテンツなどのパーソナライゼーションをテンプレート化してからカードを作成します。このオプションは通常、より良いパフォーマンスを提供します。

選択したオプションに関係なく、Content Cardsの有効期限のカウントダウンはCampaign起動時に開始されます。

{% endtab %}
{% tab Canvas %}

Content Cardsの[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)の**Messaging Channels**タブで、Brazeがカードを作成するタイミングを選択できます。

![スケジュールされたContent Cardsの配信を編集する際のContent Cardsコントロールセクション。]({% image_buster /assets/img_archive/card_creation_canvas.png %})

以下のオプションが利用可能です。

- **At step entry:** Content Cardsの以前のデフォルト動作です。Brazeはユーザーがキャンバスステップに入った時点でオーディエンスの適格性を計算し、カードを作成してユーザーがアプリを開くまで保存します。
- **At first impression（推奨）:** Brazeはユーザーがキャンバスステップに入った時点でオーディエンスの適格性を計算します。ユーザーが次にアプリを開いた（新しい[セッション](https://www.braze.com/resources/articles/whats-an-app-session-anyway)を開始した）とき、BrazeはLiquidやコネクテッドコンテンツなどのパーソナライゼーションをテンプレート化してからカードを作成します。このオプションは、カード配信のパフォーマンスが向上し、より最新のパーソナライゼーションを提供します。

選択したオプションに関係なく、Content Cardsの有効期限のカウントダウンはユーザーがキャンバスステップに入った時点で開始されます。

{% alert tip %}
匿名ユーザーの最初のセッションでContent Cardsを表示したい場合は、CanvasではなくCampaignを使用してください。匿名ユーザーがCanvasに入る時点ではセッションがすでに開始されているため、新しいセッションを開始するまでContent Cardsを受け取ることができません。
{% endalert %}

### 削除イベント {#removal-event}

ユーザーが購入を完了したりカスタムイベントを実行したりしたときにContent Cardsを削除するオプションを選択します。**Perform Custom Event**を削除イベントとして使用するには、プロパティフィルターを使用する際にコンテキスト変数またはカスタム属性を比較対象として選択します。

![「Perform Custom Event」が選択され、コンテキスト変数またはカスタム属性を使用したプロパティフィルターが設定されたContent Cards削除イベント設定。]({% image_buster /assets/img/content_card_removal_event.png %})

### 有効期限 {#expiration}

**Expiration (Time in Feed)**設定で、**Personalize duration**を選択してコンテキスト変数を使用したContent Cardsの有効期限を設定できます。

![Content Cardsの有効期限にコンテキスト変数を使用して「Personalize duration」が設定された有効期限設定。]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Content Cardsの最大有効期限は30日間です。コンテキスト変数を使用したパーソナライズされた期間を使用する場合でも同様です。30日を超える値を設定しても、30日に制限されます。詳細については、[カードの有効期限]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/#card-expiration)を参照してください。
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
どちらのオプションでも、カードが作成された後、Brazeはオーディエンスの適格性やパーソナライゼーションを再計算しません。
{% endalert %}

### 起動時またはエントリ時と初回インプレッション時のカード作成の違い {#differences}

このセクションでは、Campaign起動時またはステップエントリ時と初回インプレッション時のカード作成の主な違いについて説明します。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Differences between creating cards at launch or entry versus at first impression #differences" class="tg">
  <caption>起動時またはエントリ時と初回インプレッション時のカード作成の違い</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Campaign起動時 / キャンバスステップエントリ時</th>
    <th class="tg-0pky">初回インプレッション時</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">使用するタイミング</td>
    <td class="tg-0pky">特定の時点（起動時）でコンテンツのスナップショットを取得する必要がある場合。</td>
    <td class="tg-0pky"><ul><li>起動後にSegmentに入る可能性のある新規ユーザーや匿名ユーザーにカードを表示する必要がある場合（<a href="#campaign_note">Campaignのみ*</a>）。</li><li>パーソナライゼーションを使用しており、カードに最新のコンテンツを表示したい場合。</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">オーディエンス</td>
    <td class="tg-0pky">BrazeはCampaign送信時にオーディエンスメンバーシップを評価します。<br><br>Campaign送信後にカードを表示しようとする新規ユーザーや匿名ユーザーは、適格性の評価対象になりません。定期Campaignの場合、次の繰り返し間隔で評価されます。</td>
    <td class="tg-0pky">Brazeはユーザーが次にアプリを開いた（セッションを開始した）ときにメンバーシップを評価します（<a href="#campaign_note">Campaignのみ*</a>）。<br><br>この設定では、新規ユーザーや匿名ユーザーがカードを表示しようとする際に常に適格性が評価されるため、より広いオーディエンスにリーチできます。<br><br>また、初回インプレッション時に設定した場合、レート制限（カードを受け取る人数の制限）は適用されません。</td>
  </tr>
  <tr>
    <td class="leftHeader">パーソナライゼーション</td>
    <td class="tg-0pky">Brazeは、Campaign起動時またはユーザーがキャンバスステップに入った時点でLiquid、コネクテッドコンテンツ、Content Blocksを評価します。定期Campaignの場合、次の繰り返し間隔で評価されます。</td>
    <td class="tg-0pky">Brazeは初回インプレッション時または次の繰り返し間隔後にLiquid、コネクテッドコンテンツ、Content Blocksを評価します。</td>
  </tr>
  <tr>
    <td class="leftHeader">分析</td>
  <td class="tg-0pky"><em>送信済みメッセージ</em>は、Brazeが作成して利用可能にしたカードの数を指します。ユーザーがカードを閲覧したかどうかはカウントされません。</td>
  <td class="tg-0pky"><em>送信済みメッセージ</em>は、セッション開始後にBrazeがユーザーに送信したカードの数を指します。Canvasでは、ユーザーがセッションを開始せずにステップに入った場合、Brazeはカードを送信しないため、この指標はステップに入ったユーザー数と一致しない場合があります。<br><br>到達可能なユーザー数とインプレッション数は変わりませんが、初回インプレッション時にカードを作成する場合、Campaign起動時やキャンバスステップエントリ時と比較して送信量（<em>送信済みメッセージ</em>）は少なくなることが予想されます。</td>
  </tr>
  <tr>
    <td class="leftHeader">処理時間</td>
  <td class="tg-0pky">Brazeは起動時にSegment内のすべての対象ユーザーに対してカードを作成します。大規模なオーディエンスの場合は、<b>At first impression</b>を選択すると、起動後にカードがより迅速に利用可能になります。</td>
  <td class="tg-0pky">Brazeはユーザーが初めてカードを表示しようとしたときにカードを作成するため、初回インプレッション時に表示されるまで1〜2秒かかる場合があります。</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* このシナリオはCampaignにのみ適用されます。CanvasのオーディエンスはステップレベルではなくCanvasエントリ時に評価されるためです。</sup></p>

## 考慮事項 {#considerations}

### マルチチャネルCampaign {#multichannel-campaigns}

マルチチャネルCampaignでは初回インプレッション時のカード作成はサポートされていないため、すべてのContent CardsはCampaign起動時に送信されます。

### Canvasコンテキストプロパティの使用 {#using-canvas-context-properties}

Content Cardsを[Canvasコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)でパーソナライズする場合は、`${...}` 構文を使用してください（例: {%raw%}`{{context.${property_name}}}`{%endraw%}）。この構文を使用しないドット記法（例: {%raw%}`{{context.property_name}}`{%endraw%}）は、プッシュやメールなどの他のチャネルでは動作しても、Content Cardsでは正しく解決されない場合があります。

### 起動後のカード作成方法の変更 {#changing-card-creation-after-launch}

Brazeでは、Campaign起動後にカードの作成方法を変更しないことを推奨しています。2つのカード作成タイプ間で送信済みメッセージの計算方法が異なるため、Campaign起動後にカードの作成方法を変更すると、送信量の正確性に影響を与える可能性があります。

### 処理時間について {#potential-processing-time}

大規模なオーディエンスの場合は、初回インプレッション時にカードを作成するオプションを選択すると、起動後にカードが迅速に利用可能になります。セッション開始時にトリガーされるCampaignも、パフォーマンスを向上させるために初回インプレッション時の作成（スケジュール配信で利用可能）に移行することで恩恵を受ける場合があります。

初回インプレッション時にカードを作成する場合、カードの処理に数秒かかることがあります。この処理時間の長さは、カードサイズやメッセージテンプレートオプションの複雑さなど、さまざまな要因によって異なります。例えば、コネクテッドコンテンツを使用するカードの処理時間は、少なくともコネクテッドコンテンツの応答時間と同程度になります。

### 以前のSDKバージョン {#previous-sdk-versions}

ユーザーのアプリが以前のSDKバージョンを実行している場合でも、送信したContent Cardsは受信されます。ただし、カードの表示に時間がかかり、次のContent Cards同期まで表示されない場合があります。