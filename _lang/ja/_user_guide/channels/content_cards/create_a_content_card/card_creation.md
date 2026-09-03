---
nav_title: カード作成
article_title: カード作成
alias: /card_creation/
description: "この記事では、キャンペーン起動時またはキャンバスステップエントリ時と、初回インプレッション時のContent Cards作成の違いについて説明します。"
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# カード作成 {#card-creation}

> カードの作成タイミングを指定することで、新しいContent Cardsのキャンペーンやキャンバスステップに対してBrazeがオーディエンスの適格性とパーソナライゼーションを評価するタイミングを選択できます。

## 前提条件 {#prerequisites}

この機能を利用するには、以下の最小SDKバージョンにアップグレードする必要があります。

{% sdk_min_versions swift:5.2.0 objc:4.5.0 android:23.0.0 web:4.2.0 %}

iOSでは、Swift SDKはバージョン5.2.0以降でこの機能をサポートしており、レガシーのObjective-C SDKはバージョン4.5.0以降でサポートしています。Swift SDKのバージョン5.0.0から5.1.xではサポートされていません。

SDKをアップグレードした後、モバイルユーザーはアプリをアップグレードする必要があります。キャンペーンまたはキャンバスのオーディエンスをフィルタリングして、[これらの最小アプリバージョンのユーザーのみをターゲット]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions)にすることができます。

## 概要 {#overview}

{% tabs %}
{% tab キャンペーン %}

スケジュール配信による新しい[Content Cardsキャンペーン]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)を作成するとき、**配信**ステップでBrazeがカードを作成するタイミングを選択できます。

![スケジュールされたContent カードの配信を編集する際のContent カードコントロールセクション。]({% image_buster /assets/img_archive/card_creation.png %})

以下のオプションが利用できます。

- **キャンペーン開始時：** Content Cardsの以前のデフォルト動作です。Brazeはキャンペーン開始時にオーディエンスの適格性とパーソナライゼーションを計算し、カードを作成してユーザーがアプリを開くまで保存します。
- **ファーストインプレッション時（推奨）：** ユーザーが次にアプリを開くと（新しい[セッション](https://www.braze.com/resources/articles/whats-an-app-session-anyway)を開始すると）、Brazeはそのユーザーが対象となるContent Cardsを判定し、LiquidやConnected Contentなどのパーソナライゼーションをテンプレート化してからカードを作成します。このオプションは通常、より優れたパフォーマンスを提供します。

選択したオプションにかかわらず、Content Cardsの有効期限のカウントダウンはキャンペーン開始時に始まります。

{% endtab %}
{% tab キャンバス %}

Content Cardsの[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)の**メッセージングチャネル**タブで、Brazeがカードを作成するタイミングを選択できます。

![スケジュールされたContent カードの配信を編集する際のContent カードコントロールセクション。]({% image_buster /assets/img_archive/card_creation_canvas.png %})

以下のオプションが利用できます。

- **ステップエントリ時：** Content Cardsの以前のデフォルト動作です。ユーザーがキャンバスステップに入った時点でBrazeがオーディエンスの適格性を計算し、カードを作成してユーザーがアプリを開くまで保存します。
- **ファーストインプレッション時（推奨）：** ユーザーがキャンバスステップに入った時点でBrazeがオーディエンスの適格性を計算します。ユーザーが次にアプリを開くと（新しい[セッション](https://www.braze.com/resources/articles/whats-an-app-session-anyway)を開始すると）、BrazeがLiquidやConnected Contentなどのパーソナライゼーションをテンプレート化してからカードを作成します。このオプションはカード配信のパフォーマンスが向上し、より最新のパーソナライゼーションが提供されます。

選択したオプションにかかわらず、Content Cardsの有効期限のカウントダウンはユーザーがキャンバスステップに入った時点で始まります。

{% alert tip %}
匿名ユーザーに最初のセッションでContent カードを表示したい場合は、キャンバスではなくキャンペーンを使用してください。匿名ユーザーがキャンバスに入るとき、セッションはすでに開始されているため、新しいセッションを開始するまでContent カードは表示されません。
{% endalert %}

### 削除イベント {#removal-event}

ユーザーが購入を完了するかカスタムイベントを実行したときにContent Cardsを削除するオプションを選択します。削除イベントとして**カスタムイベントを実行**を使用する場合、プロパティフィルター使用時の比較にコンテキスト変数またはカスタム属性を選択します。

![「カスタムイベントを実行」が選択され、コンテキスト変数またはカスタム属性を使用したプロパティフィルターが設定されたContent Card削除イベント設定。]({% image_buster /assets/img/content_card_removal_event.png %})

### 有効期限 {#expiration}

**有効期限（フィード内の期間）**設定で、**期間をパーソナライズ**を選択してコンテキスト変数を使用したContent Cardsの有効期限を設定できます。

![コンテキスト変数を使用してContent Cardの有効期限が設定された「期間をパーソナライズ」の有効期限設定。]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Content Cardsの最大有効期限は30日間です。コンテキスト変数を使用したパーソナライズされた期間を使用している場合でも同様です。30日を超える値を設定しても、30日に制限されます。詳細については、[カードの有効期限]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-expiration)を参照してください。
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
どちらのオプションでも、カードが作成された後、Brazeはオーディエンスの適格性やパーソナライゼーションを再計算しません。
{% endalert %}

### 開始時またはエントリ時とファーストインプレッション時のカード作成の違い {#differences}

このセクションでは、キャンペーン開始時またはステップエントリ時のカード作成と、ファーストインプレッション時のカード作成の主な違いについて説明します。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="開始時またはエントリ時とファーストインプレッション時のカード作成の違い" class="tg">
  <caption>開始時またはエントリ時とファーストインプレッション時のカード作成の違い</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">キャンペーン開始時／キャンバスステップエントリ時</th>
    <th class="tg-0pky">ファーストインプレッション時</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">使用するタイミング</td>
    <td class="tg-0pky">特定の時点（開始時点）でコンテンツのスナップショットを取得する必要がある場合。</td>
    <td class="tg-0pky"><ul><li>開始後にセグメントに入る可能性のある新規ユーザーや匿名ユーザーにカードを表示する必要がある場合（<a href="#campaign_note">キャンペーンのみ*</a>）。</li><li>パーソナライゼーションを使用しており、カードで最新のコンテンツを利用したい場合。</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">オーディエンス</td>
    <td class="tg-0pky">Brazeはキャンペーン送信時にオーディエンスメンバーシップを評価します。<br><br>キャンペーン送信後にカードを閲覧しようとした新規ユーザーや匿名ユーザーは適格性の評価対象になりません。定期キャンペーンの場合、次の反復間隔で評価されます。</td>
    <td class="tg-0pky">Brazeはユーザーが次にアプリを開いたとき（セッション開始時、<a href="#campaign_note">キャンペーンのみ*</a>）にメンバーシップを評価します。<br><br>この設定はオーディエンスのリーチが広くなります。新規ユーザーや匿名ユーザーがカードを閲覧しようとした際に常に適格性が評価されるためです。<br><br>また、ファーストインプレッション時に設定した場合、レート制限（カードを受信するユーザー数の制限）は適用されません。</td>
  </tr>
  <tr>
    <td class="leftHeader">パーソナライゼーション</td>
    <td class="tg-0pky">Brazeはキャンペーン開始時またはユーザーがキャンバスステップに入った時点で、Liquid、Connected Content、Content Blocksを評価します。定期キャンペーンの場合、次の反復間隔で評価されます。</td>
    <td class="tg-0pky">Brazeはファーストインプレッション時または次の反復間隔後に、Liquid、Connected Content、Content Blocksを評価します。</td>
  </tr>
  <tr>
    <td class="leftHeader">分析</td>
  <td class="tg-0pky"><em>送信メッセージ数</em>は、Brazeが作成して利用可能にしたカードの数を指します。ユーザーがカードを閲覧したかどうかはカウントされません。</td>
  <td class="tg-0pky"><em>送信メッセージ数</em>は、セッション開始後にBrazeがユーザーに送信したカードの数を指します。キャンバスでは、ユーザーがセッションを開始せずにステップに入った場合、Brazeはカードを送信しないため、この指標はステップに入ったユーザー数と一致しない場合があります。<br><br>リーチ可能なユーザー数やインプレッションは変わりませんが、ファーストインプレッション時にカードを作成する場合、キャンペーン開始時やキャンバスステップエントリ時と比較して送信量（<em>送信メッセージ数</em>）は低くなることが予想されます。</td>
  </tr>
  <tr>
    <td class="leftHeader">処理時間</td>
  <td class="tg-0pky">Brazeは開始時にセグメント内のすべての対象ユーザーに対してカードを作成します。大規模なオーディエンスの場合は、開始後すぐにカードが利用可能になるように<b>ファーストインプレッション時</b>を選択してください。</td>
  <td class="tg-0pky">Brazeはユーザーが初めてカードを閲覧しようとしたときにカードを作成するため、最初のインプレッション時に表示まで1～2秒かかる場合があります。</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* このシナリオはキャンペーンにのみ適用されます。キャンバスのオーディエンスはステップレベルではなくキャンバスエントリ時に評価されるためです。</sup></p>

## 考慮事項 {#considerations}

### マルチチャネルキャンペーン {#multichannel-campaigns}

マルチチャネルキャンペーンはファーストインプレッション時のカード作成をサポートしていないため、すべてのContent Cardsはキャンペーン開始時に送信されます。

### キャンバスのコンテキストプロパティを使用する {#using-canvas-context-properties}

Content Cardsを[キャンバスのコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)でパーソナライズする場合は、`${...}` 構文を使用してください（例: {%raw%}`{{context.${property_name}}}`{%endraw%}）。この構文を使わないドット表記（例: {%raw%}`{{context.property_name}}`{%endraw%}）は、プッシュやメールなどの他のチャネルでは動作しても、Content Cardsでは正しく解決されない場合があります。

### 開始後のカード作成方法の変更 {#changing-card-creation-after-launch}

Brazeでは、キャンペーンの開始後にカードの作成方法を変更しないことを推奨しています。2つのカード作成タイプ間で「送信済みメッセージ数」の計算方法が異なるため、開始後にカードの作成方法を変更すると、送信ボリュームの精度に影響する可能性があります。

### 処理時間の可能性 {#potential-processing-time}

大規模なオーディエンスの場合は、ファーストインプレッション時にカードを作成するオプションを選択して、開始後すぐにカードを利用できるようにしてください。セッション開始時にトリガーされるキャンペーンも、ファーストインプレッション時の作成に移行することで（スケジュール配信から利用可能）、パフォーマンスが向上する場合があります。

ファーストインプレッション時にカードが作成される場合、カードの処理に数秒かかることがあります。この処理時間の長さは、カードのサイズやメッセージテンプレートオプションの複雑さなど、さまざまな要因によって異なります。例えば、Connected Contentを使用するカードの処理時間は、少なくともConnected Contentのレスポンス時間と同程度になります。

### 以前のSDKバージョン {#previous-sdk-versions}

ユーザーのアプリが以前のSDKバージョンを実行している場合でも、送信したContent Cardsは受信されます。ただし、カードの表示に時間がかかり、次のContent Cards同期まで表示されない場合があります。