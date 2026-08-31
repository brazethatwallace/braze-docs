---
nav_title: CataBoom
article_title: CataBoom
description: "CataBoomのゲーミフィケーション体験をCatapult、リクエストユニークURL、Connected Contentを使用してBrazeに接続する方法を説明します。"
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> [CataBoom](https://www.cataboom.com/)はゲーミフィケーションプラットフォームです。ブランドはこれを使用して、スピン・トゥ・ウィンゲーム、クイズ、インスタントウィンゲームなどのインタラクティブなデジタルエクスペリエンスを構築・起動します。これらの体験はエンゲージメントを深め、ファーストパーティデータを収集します。

*この連携はCataBoomによって管理されています。*

## この連携について {#about-this-integration}

BrazeとCataBoomの連携を使用して、パーソナライズされたゲームリンクをメッセージに追加できます。Catapultキャンペーンと Brazeの間でユーザー識別子と属性をリアルタイムでやり取りできます。そのデータを活用して、パーソナライズされたキャンペーン、トリガー、フォローアップジャーニーを構築できます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Catapult アカウント | このインテグレーションを使用するには、Catapult アカウントが必要です。 |
| Braze REST APIキー（オプション） | Catapult webhookを使用する場合は、ユースケースに必要なユーザーデータ権限を持つBraze REST APIキーが必要です。Brazeの**設定** > **APIと識別子** > **APIキー**でキーを作成してください。 |
| Braze RESTエンドポイント（オプション） | Catapult webhookを使用する場合は、[お使いのBrazeインスタンス]({{site.baseurl}}/api/basics#endpoints)のBraze URLに一致するRESTエンドポイントURLを使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ1:ゲームエクスペリエンスを作成する {#step-1-create-your-game-experience}

Catapultプラットフォームでゲームエクスペリエンスを作成します。以下のステップでは、**Link Configuration**ページのRequest Unique URL APIを使用するシンプルなスピナー設定を説明します。CataBoomは、チャンスベースのメカニクス、スキルベースのメカニクス、パンチカードやコレクト・アンド・ウィンなどのユーティリティを含む200種類以上のゲームオプションを提供しています。他のゲームタイプでも同様のフローに従うことができます。CataBoomとCatapultの詳細については、[CataBoomのWebサイト](https://www.cataboom.com)を参照してください。

1. キャンペーンを作成します。

上部のナビゲーションエリアで**New キャンペーン**を選択します。キャンペーン名を入力し、URLスラッグを選択し、ゲームカテゴリとゲームタイプを選択します。

![キャンペーン名、URL、ゲームカテゴリ、ゲームタイプのフィールドが表示されたCataBoomダッシュボードのNew キャンペーンフォーム。]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Request Unique URL APIを有効にします。

ナビゲーションメニューで**Link Configuration**を選択します。

**Link Configuration**ページで**Request Unique URL API**を有効にします。このオプションにより、Content Cardなど、後でBrazeで使用できるシステム間URLが作成されます。

![Request Unique URL APIが有効になっており、API URLが表示されているCataBoom Link Configurationページ。]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. プレイトラッキングをAccount IDに設定します。

ナビゲーションメニューで**Play Control**を選択します。

**Play Control**ページの**Play Tracking**で、**Play Count Tracked By**を**Account ID Parameter**に設定します。

トラッキング、プレイ制限、webhook、その他のプレイヤー固有の動作のために、各プレイヤーのAccount IDを渡すことができます。他のシステムでは、Account IDをメンバーID、プレイヤーID、ロイヤルティID、または類似の名前で呼ぶことがよくあります。

![Play Count Tracked ByがAccount ID Parameterに設定されたCataBoom Play Controlページ。]({% image_buster /assets/img/cataboom/play_control.png %})

これで、Brazeでテストを実行するのに十分な設定が完了しました。このセクションのオプションのステップでは、一般的なフルゲーム設定を完了します。Catapultには、ゲームプレイをカスタマイズするために使用できる他の多くの設定もあります。

{: start="4"}
4. クリエイティブを追加します（オプション）。

ナビゲーションメニューで**Creative**を選択します。

アセットをアップロードします。Catapultはゲームエクスペリエンスのフルブランディングコントロールをサポートしています。

![グラフィックのダウンロードおよびアップロードアクションとゲームプレビューが表示されたCataBoom Creativeページ。]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. チャンスベースのゲームの賞品を設定します（オプション）。

ナビゲーションメニューで**Summary**を選択します。

**Summary**ページで**Prize Options**を展開します。

Catapultは、時間ベースの賞品、確率ベースの賞品、またはその両方をサポートしています。設定するには、必要に応じて**Timed Prizes and Codes**、**Prize Control and Odds Setup**、またはその両方を使用します。

以下のスクリーンショットは、キャンペーンサマリーの**Prize Options**と、レベル1で50%の当選確率を持つシンプルな確率設定を示しています。

![Prize Optionsセクションが展開されたCataBoom Summaryページ。]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![賞品レベル、パーセンテージ、レベルコントロールが表示されたCataBoom Oddsページ。]({% image_buster /assets/img/cataboom/prize_odds.png %})

## ステップ 2: Braze でメッセージを作成する {#step-2-create-a-message-in-braze}

この例では、**Link Configuration** ページの Request Unique URL を使用する **Content Cards** の作成方法を示します。

1. プレイ URL 用の Connected Content を追加します。

Content Cards にコピーとダイナミックなコンテンツを必要に応じて追加します。CataBoom の Request Unique URL を [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) タグで囲みます。Catapult で使用する識別子と一致する Braze パーソナライゼーションタグを使用して、`AccountID` クエリパラメーターを追加します。この例では {% raw %}`{{${user_id}}}`{% endraw %} を使用しています。

ベース URL と `username` および `password` クエリパラメーターを、Catapult のキャンペーン用 **Link Configuration** ページの値に置き換えます。

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

保存された `result` をカードで使用します（例: リンク URL やメッセージ本文など）。キャンペーンの CataBoom API からのレスポンス形式に従ってください。クエリパラメーターと URL 内の Liquid の詳細については、[API コールの実行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を参照してください。

![メッセージフィールドに Connected Content が表示された Braze Content Cards コンポーザーと、カードのモバイルプレビュー。]({% image_buster /assets/img/cataboom/braze_content_card.png %})

Connected Content は、ユーザーが Content Cardsを開封した際に一意のプレイリンクをリクエストします。他のクエリパラメーターを追加することで、よりカスタマイズされたエクスペリエンスを実現できます。