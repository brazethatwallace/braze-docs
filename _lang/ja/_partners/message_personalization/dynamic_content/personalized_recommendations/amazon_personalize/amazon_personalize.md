---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "このリファレンス記事では、BrazeとAmazon Personalizeのリファレンスアーキテクチャと統合について説明します。このリファレンス記事は、Amazon Personalizeが提供するユースケース、Amazon Personalizeが扱うデータ、サービスの設定方法、Brazeとの統合方法を理解するのに役立ちます。"
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> [Amazon Personalize](https://aws.amazon.com/personalize/)は、あなた専用の終日稼働するAmazon機械学習レコメンデーションシステムを持つようなものです。20年以上にわたるレコメンデーションの経験に基づき、Amazon Personalizeは、リアルタイムでパーソナライズされた商品やコンテンツのレコメンデーション、およびターゲットを絞ったマーケティングプロモーションを提供することで、カスタマーエンゲージメントを向上させます。

_この統合はAmazon Personalizeによって管理されます。_

## 統合について {#about-the-integration}

Amazon Personalizeは、機械学習とあなたが定義したアルゴリズムを使用して、Webサイトやアプリケーション向けに高品質のレコメンデーションを出力するモデルのトレーニングを支援します。これらのモデルにより、ユーザーの過去の行動に基づいたレコメンデーションリストの作成、関連性によるアイテムの並べ替え、類似性に基づく他のアイテムのレコメンデーションが可能になります。Amazon Personalize APIから取得したリストは、Brazeのコネクテッドコンテンツで使用して、パーソナライズされたBrazeレコメンデーションキャンペーンを実行できます。Amazon Personalizeと統合することで、モデルのトレーニングに使用するパラメーターを自由にコントロールし、アルゴリズムの出力を最適化するオプションのビジネス目標を定義できます。

このリファレンス記事は、Amazon Personalizeが提供するユースケース、Amazon Personalizeが扱うデータ、サービスの設定方法、Brazeとの統合方法を理解するのに役立ちます。

## 前提条件 {#prerequisites}

| 必要条件| 説明|
| ---| ---|
| Amazon Web Serviceアカウント | このパートナーシップを利用するには、AWSアカウントが必要です。AWSアカウントを取得したら、Amazon Personalizeコンソール、AWS Command Line Interface（AWS CLI）、またはAWS SDKを使用してAmazon Personalizeにアクセスできます。 |
| 定義されたユースケース | モデルを作成する前に、この統合のユースケースを決定する必要があります。一般的なユースケースについては、以下のリストを参照してください。 |
| データセット | Amazon Personalizeのレコメンデーションモデルには、インタラクション、ユーザー、アイテムの3種類のデータセットが必要です。各データセットの要件については、以下の詳細を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% tabs %}
{% tab ユースケース %}

**ユースケース**

モデルを作成する前に、この統合のユースケースを決定する必要があります。一般的なユースケースには以下のようなものがあります。
- ユーザーの過去のインタラクションに基づいてアイテムをレコメンドし、真にパーソナライズされたエクスペリエンスを提供する。
- 各ユーザーに合わせたアイテムや検索結果のリストを提供し、ユーザーとの関連性によってアイテムを表示することでエンゲージメントを高める。
- 類似アイテムのレコメンデーションを見つけ、ユーザーが新しいものを発見するのを助ける。

以下のガイドでは、ユーザー個別のレコメンデーションレシピに焦点を当てます。

{% endtab %}
{% tab データセット %}

**データセット**

Amazon Personalizeのレコメンデーションモデルを使い始めるには、3種類のデータセットが必要です。

- インタラクション
  - ユーザーとアイテム間のインタラクション履歴を保存します
  - `USER_ID`、`ITEM_ID`、`EVENT_TYPE`、`TIMESTAMP`の値が必要です。オプションでイベントに関するメタデータも受け入れます
- ユーザー
  - ユーザーに関するメタデータを保存します
  - `USER_ID`の値と、性別、年齢、ロイヤルティメンバーシップなどのメタデータフィールド（文字列または数値）が1つ以上必要です
- アイテム
  - アイテムに関するメタデータを保存します
  - `ITEM_ID`と、アイテムを記述するメタデータフィールド（テキスト、カテゴリ、または数値）が1つ以上必要です

ユーザーレコメンデーションレシピの場合、25人以上のユニークユーザー（各ユーザーに2つ以上のインタラクションがある）からの1000ポイント以上のインタラクションデータを含むインタラクションデータセットを提供する必要があります。これらのデータセットは、S3に保存されたCSVファイルを使って一括アップロードすることも、APIを使って段階的にアップロードすることもできます。

{% endtab %}
{% endtabs %}

## モデルの作成 {#creating-models}

### ステップ1:トレーニング {#step-1-training}

データセットがインポートされたら、ソリューションを作成できます。ソリューションは、Amazon Personalizeの[レシピ](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)（アルゴリズム）の1つを使用してモデルをトレーニングします。ここでは`USER_PERSONALIZATION`レシピを使用します。ソリューションをトレーニングすることで、ソリューションバージョン（トレーニング済みモデル）が作成され、モデルのパフォーマンス指標に基づいて評価できます。

Amazon Personalizeでは、モデルがトレーニングに使用するハイパーパラメーターを調整できます。以下に例を示します。
- Amazon Personalizeコンソールにある「User history length percentile」パラメーターで、トレーニングに含めるユーザー履歴のパーセンタイルを調整できます。<br><br>![最小最大ユーザープロファイル設定]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`：履歴の長さが非常に短い一定割合のユーザーを除外します。これは、人気の高いアイテムを排除し、より深い基盤となるパターンに基づいてレコメンデーションを作成する際に役立ちます。
  - `max_user_history_length_percentile`：トレーニングの際に考慮すべき、履歴の長さが非常に長いユーザーの割合を調整します。

隠れ次元の数は、複雑なデータセットのより複雑なパターンを検出するのに役立ちます。一方、通時的誤差逆伝搬法（BPTT）は、一連のイベントが発生し、その結果価値の高いアクションがもたらされた後で、早期のイベントに対するリワードを調整します。

さらに、Amazon Personalizeは、異なる値を持つ複数のバージョンのソリューションを同時に実行することで、ハイパーパラメーターの自動チューニングを提供します。チューニングを使用するには、ソリューションの作成時に**Perform HPO**をオンにします。

### ステップ2:評価と比較 {#step-2-evaluate-and-compare}

ソリューションのトレーニングが完了したら、評価して異なるバージョンを比較する準備が整います。各ソリューションバージョンは、計算された指標を表示します。利用可能な指標には以下のようなものがあります。

- **正規化割引累積利得：**アイテムの推奨順序を実際のアイテムリストと比較し、各アイテムにリスト内の位置に対応する重みを与えます
- **精度@k：**適切にレコメンドされたアイテムの数を、レコメンドされた全アイテムの数で割ったものです。`k`はアイテムの数です
- **平均逆順位：**最初の、最も高いランクのレコメンデーションに焦点を当て、最初にマッチしたレコメンデーションが表示される前に、レコメンドされたアイテムがいくつ表示されたかを計算します
- **カバレッジ：**データセット内のユニークアイテムの総数に対する、ユニークなレコメンドアイテムの割合です

## レコメンデーションの取得 {#getting-recommendations}

満足のいくソリューションバージョンを作成したら、レコメンデーションを活用する番です。レコメンデーションにアクセスするには、次の2つの方法があります。

1. リアルタイムキャンペーン<br>キャンペーンとは、定義された最小トランザクションスループットを持つ、デプロイされたソリューションバージョンのことです。トランザクションとは、レコメンデーション出力を取得するための1回のAPI呼び出しです。TPS（1秒あたりのトランザクション数）として定義され、最小値は1です。負荷が増加した場合、キャンペーンはリソースをスケーリングしますが、最小値を下回ることはありません。コンソール、AWS CLI、またはコード内のAWS SDKでレコメンデーションをクエリできます。<br><br>
2. バッチジョブ<br>バッチジョブはS3バケットにレコメンデーションをエクスポートします。このジョブは、レコメンデーションをエクスポートするユーザーIDのリストを含むJSONファイルを入力として取ります。正しい権限と出力先を指定したら、ジョブを実行できます。実行時間は、データセットのサイズとレコメンデーションリストの長さに依存します。

### フィルター {#filters}

フィルターを使用すると、アイテムのID、イベントタイプ、またはメタデータに基づいてアイテムを除外することで、レコメンデーション出力を調整できます。また、年齢やロイヤルティメンバーシップのステータスなど、メタデータに基づいてユーザーをフィルタリングすることもできます。フィルターは、ユーザーがすでにインタラクションしたアイテムのレコメンドを防ぐ場合に役立ちます。

## 結果をBrazeと統合する {#integrating-results-with-braze}

作成したモデルとレコメンデーションキャンペーンがあれば、Content Cardsとコネクテッドコンテンツを使って、ユーザーに対してBrazeキャンペーンを実行する準備が整います。
Brazeキャンペーンを実行する前に、APIを通じてこれらのレコメンデーションを提供できるサービスを作成する必要があります。[ワークショップ記事のステップ3]({{site.baseurl}}/partners/amazon_personalize_workshop#step-3-send-personalized-emails-from-braze)に従って、AWSサービスを使用してサービスをデプロイできます。レコメンデーションを提供する独自の独立系バックエンドサービスをデプロイすることもできます。

### Content Cardsキャンペーンのユースケース {#content-card-campaign-use-case}

リストの最初のレコメンドアイテムを使用してContent Cardsキャンペーンを実行してみましょう。<br><br>
次の例では、`user_id`パラメーターを指定した`GET http://<service-endpoint.com>/recommendations?user_id=user123`エンドポイントをクエリします。これにより、レコメンドアイテムのリストが返されます。

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Brazeダッシュボードで、新しい[Content Cardsキャンペーン]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)を作成します。メッセージテキストフィールドに、APIにクエリしてレスポンスを`recommendations`変数に保存するコネクテッドコンテンツLiquidブロックを作成します。

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

その後、結果として得られる配列の最初のアイテムを参照し、そのコンテンツをユーザーに表示できます。

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

タイトル、画像、URLのリンクを含めると、Content Cardsの完成形はこのようになります。

![コネクテッドコンテンツがメッセージ本文と「Add Image」フィールドに追加されたキャンペーンの画像。この画像は、「Redirect to Web URL」フィールドに追加されたコネクテッドコンテンツロジックも示しており、ユーザーをレコメンデーションURLにリンクさせています。]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})