---
nav_title: CataBoom
article_title: CataBoom
description: "CataBoomのゲーミフィケーション体験をCatapult、リクエストユニークURL、コネクテッドコンテンツを使用してBrazeに接続する方法を説明します。"
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> [CataBoom](https://www.cataboom.com/)はゲーミフィケーションプラットフォームです。ブランドはこれを使用して、スピン・トゥ・ウィンゲーム、クイズ、インスタントウィンゲームなどのインタラクティブなデジタルエクスペリエンスを構築・起動します。これらの体験はエンゲージメントを深め、ファーストパーティデータを収集します。

*この連携はCataBoomによって管理されています。*

## この連携について {#about-this-integration}

BrazeとCataBoomの連携を使用して、パーソナライズされたゲームリンクをメッセージに追加できます。ユーザー識別子と属性をCatapultのキャンペーンとBrazeの間でリアルタイムに受け渡すことができます。そのデータを使用して、パーソナライズされたキャンペーン、トリガー、フォローアップジャーニーを実行できます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Catapultアカウント | この連携を使用するにはCatapultアカウントが必要です。 |
| Braze REST APIキー（オプション） | Catapult webhookを使用する場合、ユースケースに必要なユーザーデータ権限を持つBraze REST APIキーが必要です。Brazeの**設定** > **APIキー** > **APIキー**でキーを作成してください。 |
| Braze RESTエンドポイント（オプション） | Catapult webhookを使用する場合、[お使いのBrazeインスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLに一致するRESTエンドポイントURLを使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ 1: ゲーム体験を作成する {#step-1-create-your-game-experience}

Catapultプラットフォームでゲーム体験を作成します。以下のステップでは、**Link Configuration**ページでRequest Unique URL APIを使用するシンプルなスピナーのセットアップを示します。CataBoomは、チャンスベースのメカニクス、スキルベースのメカニクス、パンチカードやコレクト・アンド・ウィンなどのユーティリティを含む200以上のゲームオプションを提供しています。他のゲームタイプでも同様のフローに従うことができます。CataBoomとCatapultの詳細については、[CataBoomのWebサイト](https://www.cataboom.com)を参照してください。

1. キャンペーンを作成します。

右上の**New キャンペーン**を選択します。キャンペーン名を入力し、URLスラッグを選択し、ゲームカテゴリとゲームタイプを選択します。

![キャンペーン名、URL、ゲームカテゴリ、ゲームタイプのフィールドがあるCataBoomダッシュボードのNew キャンペーンフォーム。]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Request Unique URL APIを有効にします。

左メニューで**Link Configuration**を選択します。

**Link Configuration**ページで、**Request Unique URL API**を有効にします。このオプションにより、コンテンツカードなど、後でBrazeで使用できるシステム間URLが作成されます。

![Request Unique URL APIが有効になり、API URLが表示されているCataBoom Link Configurationページ。]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. プレイトラッキングをアカウントIDに設定します。

左メニューで**Play Control**を選択します。

**Play Control**ページの**Play Tracking**で、**Play Count Tracked By**を**Account ID Parameter**に設定します。

各プレイヤーのアカウントIDを渡すことで、トラッキング、プレイ制限、webhook、その他のプレイヤー固有の動作に使用できます。他のシステムでは、アカウントIDをメンバーID、プレイヤーID、ロイヤルティID、または類似の名前で呼ぶことがよくあります。

![Play Count Tracked ByがAccount ID Parameterに設定されているCataBoom Play Controlページ。]({% image_buster /assets/img/cataboom/play_control.png %})

これでBrazeでテストを実行するのに十分な設定が完了しました。以下のオプションステップは、一般的なフルゲームセットアップを完了するためのものです。Catapultには、ゲームプレイをカスタマイズするために使用できる他の多くの設定もあります。

{: start="4"}
4. クリエイティブを追加します（オプション）。

左メニューで**Creative**を選択します。

アセットをアップロードします。Catapultはゲーム体験のフルブランディングコントロールをサポートしています。

![グラフィックのダウンロードとアップロードアクション、およびゲームプレビューがあるCataBoom Creativeページ。]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. チャンスベースのゲームの賞品を設定します（オプション）。

左メニューで**Summary**を選択します。

**Summary**ページで、**Prize Options**を展開します。

Catapultは時間制限付き賞品、確率ベースの賞品、またはその両方をサポートしています。設定するには、必要に応じて**Timed Prizes and Codes**、**Prize Control and Odds Setup**、またはその両方を使用します。

以下のスクリーンショットは、キャンペーンサマリーの**Prize Options**と、レベル1で50%の当選確率を持つシンプルな確率設定を示しています。

![Prize Optionsセクションが展開されたCataBoom Summaryページ。]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![賞品レベル、パーセンテージ、レベルコントロールがあるCataBoom Oddsページ。]({% image_buster /assets/img/cataboom/prize_odds.png %})

## ステップ 2: Brazeでメッセージを作成する {#step-2-create-a-message-in-braze}

この例では、**Link Configuration**ページのRequest Unique URLを使用する**コンテンツカード**の作成方法を示します。

1. プレイURLのコネクテッドコンテンツを追加します。

コンテンツカードに、必要に応じてコピーとダイナミックコンテンツを追加します。CataBoomのRequest Unique URLを[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)タグで囲みます。Catapultで使用する識別子に一致するBrazeパーソナライゼーションタグを使用する`AccountID`クエリパラメーターを追加します。この例では{% raw %}`{{${user_id}}}`{% endraw %}を使用しています。

ベースURLと`username`および`password`クエリパラメーターを、Catapultのキャンペーンの**Link Configuration**ページの値に置き換えてください。

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

保存された`result`をカードで使用します（例えば、リンクURLやメッセージ本文として）。キャンペーンに対するCataBoomのAPIのレスポンス形式に従ってください。クエリパラメーターとURL内のLiquidの詳細については、[APIコールの実行]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)を参照してください。

![メッセージフィールドにコネクテッドコンテンツが表示され、カードのモバイルプレビューが表示されているBrazeコンテンツカードコンポーザー。]({% image_buster /assets/img/cataboom/braze_content_card.png %})

コネクテッドコンテンツは、ユーザーがコンテンツカードを開いたときにユニークなプレイリンクをリクエストします。他のクエリパラメーターを追加して、よりカスタマイズされた体験を提供できます。