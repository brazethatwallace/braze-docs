---
nav_title: Limbik
article_title: Limbik
description: "このリファレンス記事では、BrazeとLimbikのパートナーシップについて説明します。Limbikは、合成オーディエンスと予測を使用して、オーディエンスがメッセージをどのように解釈し反応するかを予測するAIレゾナンスレイヤーです。"
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> [Limbik](https://limbik.com/cognitive-ai)は、AIレゾナンスレイヤーです。実際のオーディエンスがメッセージ、コンセプト、AI出力をどのように解釈し反応するかを、市場に届く前に予測します。60以上の国と25以上の言語にわたる継続的な一次調査を基盤とし、Limbikは人間が検証した合成オーディエンス（マシンスピードかつリサーチグレードの精度（95%信頼度、1.5%〜3%の誤差範囲）で実際のオーディエンスの反応をシミュレートするデジタル集団）を提供します。Limbikを使用すると、メッセージングがターゲットオーディエンスの信念や感情に即座に共鳴するかどうかを確認できます。

_このインテグレーションはLimbikによって管理されています。_

## 前提条件 {#prerequisites}

LimbikをBrazeで使用するには、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Limbik `account_id` | Limbikのアカウントチームに問い合わせるか、Limbikの`/rest/api/organizations`エンドポイントにGETリクエストを送信してください。 |
| Limbikアクセストークン（`access_token`） | Limbikの`login`エンドポイントにPOSTリクエストを送信し、返された`access_token`の値を`Authorization`ヘッダーのBearerトークンとして使用してください。 |
| Braze REST APIキー | 「Messages」権限を持つBraze REST APIキー。Brazeダッシュボードの**設定** > **APIキー**で作成してください。 |
| Braze `campaign_id` | **メッセージング** > **キャンペーン**に移動し、キャンペーンを選択します。使用したいキャンペーンがまだ存在しない場合は、作成して保存してください。キャンペーンページの下部にキャンペーン API識別子があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

予測エンドポイントを使用する前に、まずアクセス可能な組織（`account_id`）を特定する必要があります。ほとんどの顧客は1つの組織のみですが、一部のアカウントでは複数の組織が利用可能な場合があります。

{% details 利用可能な組織を取得する %}

組織エンドポイントにクエリを送信して、利用可能な組織を取得します。

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details レスポンス例 %}

```json
{
  "data": [
    {
      "uid": "aca61bd5-7132-499c-946e-42d092cc1156",
      "name": "Braze API"
    }
  ]
}
```

目的の組織の`uid`を選択し、以降のすべてのAPIリクエストで`account_id`ヘッダーとして使用します。

{% enddetails %}

## 認証 {#authentication}

APIエンドポイントにアクセスするには、認証用のBearerトークンが必要です。認証情報を使用して認証し、トークンを取得してください。

{% details ログインリクエスト %}

`````````sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "your_username",
  "password": "your_password"
}'
```

{% enddetails %}

{% details レスポンス例 %}

レスポンスには、以降のすべてのAPIリクエストでBearerトークンとして使用できる`access_token`が含まれています。

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

すべてのAPIリクエストの`Authorization`ヘッダーにこのトークンを含めてください。

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
PostmanなどのAPIプラットフォームを使用して、以下のワークフローのように、異なる組織から複数のREST APIエンドポイントを呼び出す自動化ワークフローを設定できます。
{% endalert %}

{% enddetails %}

## ユースケース - メッセージコピーの生成 {#use-case-generating-message-copy}

BrazeとLimbikのREST APIエンドポイントの両方を使用することで、Limbikの生成予測を活用してメッセージコピーを作成し、Brazeのメッセージングチャネルを通じて送信したり、既存のコピーを調整してオーディエンスへのインパクトを向上させたりできます。両プラットフォームとも、プログラムで呼び出して高度なワークフローを構築できる機能を公開しています。

このドキュメントでは、2つの例を説明します。Limbikでメッセージコピーを生成し、そのコピーをBrazeを通じて送信する後続のメッセージで使用する例と、Limbikを使用して選択したオーディエンスに対するメッセージの品質をスコアリングする例です。

{% details Limbik生成予測リクエスト %}

このエンドポイントを使用してメッセージを生成し、予測テンプレートで返します。リクエスト例：

`````````sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
  -H 'account_id: YOUR_ACCOUNT_ID' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'accept: application/json'
```

`YOUR_PROMPT`、`YOUR_ACCOUNT_ID`、`YOUR_ACCESS_TOKEN`を、プロンプトテキスト、組織ID（組織エンドポイントから取得）、ログインエンドポイントからのBearerトークンに置き換えてください。

{% enddetails %}

{% details レスポンス例 %}

Limbik予測テンプレートのレスポンス例：

```json
[
  {
    "type": "Message",
    "displayText": "Formula one next race",
    "additionalDetail": "The latest dev in Formula...",
    "messages": [
      {
        "body": "The latest dev in Formula ..."
      }
    ],
    "population": {
      "id": 56,
      "name": "us2",
      "org_enabled": true,
      "org_visible": true,
      "categories": [],
      "display_name": "US Adults",
      "composite_key": "us2",
      "enabled": true
    }
  }
]
```

このユースケースの重要な要素は`additionalDetail`フィールドで、Limbikが生成したメッセージコピーが含まれています。

この値を使用して、Brazeに送信するメッセージを構成します。たとえば、POST `/campaigns/trigger/send`エンドポイントでは、`additionalDetail`を使用してペイロードフィールドを構成します。POST `/messages/send`エンドポイントでは、選択したメッセージオブジェクトを構成するために使用します。

{% enddetails %}

### レスポンスフィールド {#response-fields}

レスポンスには以下の主要フィールドが含まれます。

- **`type`:** メッセージタイプ（例：AI生成コンテンツの場合は`"Generate"`、検証済みメッセージの場合は`"Message"`）
- **`displayText`:** メッセージの短いタイトルまたは要約
- **`additionalDetail`:** **完全なAI生成メッセージコピー** - メッセージングプラットフォームを通じて送信できる完全なメッセージテキストを含む主要フィールドです
- **`population`:** このメッセージのターゲット層とセグメント

### Brazeでの使用 {#using-with-braze}

Limbikのレスポンスの`additionalDetail`フィールドには、Brazeに送信するメッセージコピーが含まれています。一般的なインテグレーションパターンの1つは、Brazeのトリガー送信エンドポイントを呼び出す際に、その値を`trigger_properties.payload`に渡すことです。以下の例では、`{{additionalDetail}}`をLimbikの`additionalDetail`フィールドの実際の文字列に、`{{YOUR_CAMPAIGN_ID}}`をキャンペーン IDに置き換えてください。

### Brazeトリガーメッセージリクエスト例 {#braze-trigger-message-request-example}

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## ユースケース - 合成オーディエンスの詳細 {#use-case-synthetic-audience-details}

最初のユースケースを発展させるために、Limbikのエンドポイント`/rest/api/populations/{account_id}/{population_id}`を使用します。

このエンドポイントは、性別、ロケーションなど、Limbikの合成オーディエンスの構成を説明する主要なデータポイントを返します。これらの値を使用して、Brazeのメッセージングエンドポイントを呼び出す際にConnected Audienceオブジェクトを構成できます。

{% alert note %}
Connected Audienceオブジェクトは、Brazeの「デフォルト」属性に基づいてユーザーをターゲットにすることはできないため、ターゲットにしたい属性はBrazeにカスタム属性として保存する必要があります。
{% endalert %}

特定のセグメントの予測スコアを取得するには、利用可能な国とそれに対応するセグメントを特定します。

### ステップ 1: 利用可能な国を一覧表示する {#step-1-list-available-countries}

アカウントで利用可能な国の一覧を取得します。

`````````sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

レスポンスから、使用したい国を特定します。たとえば、米国の`id`は`56`です。

### ステップ 2: 利用可能なセグメントを取得する {#step-2-retrieve-available-segments}

国IDを取得した後、その国の全セグメント一覧を取得します。

{% details 呼び出し例 %}

`````````sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
レスポンスは大きくなる場合があります。パフォーマンス向上のため、このデータを名前またはキーでキャッシュ（例：Redis）してください。
{% endalert %}

{% enddetails %}

{% details レスポンス例 %}

たとえば、米国の成人集団の女性をターゲットにする場合：

```json
[
  {
    "id": 56,
    "name": "us2",
    "composite_key": "us2",
    "categories": [
      {
        "id": 9331,
        "name": "gender",
        "composite_key": "us2::gender",
        "segments": [
          {
            "id": 63793,
            "name": "female",
            "composite_key": "us2::gender::female"
          }
        ]
      }
    ]
  }
]
```

{% alert note %}
- セグメントは簡略化されたコンポジットキー形式で指定されます（例：`gender::female`）。
- APIレスポンスの完全なコンポジットキー（`us2::gender::female`）は、カテゴリ名とセグメント名のみに短縮されます。
- 利用可能な集団とセグメントの完全なリファレンスについては、[Limbikオーディエンス](https://audiences.limbik.com/)を参照してください。
{% endalert %}

選択した予測メッセージのコンポジットキー値を使用して、これらの合成オーディエンス記述子をBrazeの実際のユーザープロファイルの値にマッピングできます。

たとえば、コンポジットキー（`fr1::education_level::master_s_degree`）をBrazeのConnected Audienceオブジェクトで以下のように使用できます。

```json
{
  "AND": [
    {
      "custom_attribute": {
        "custom_attribute_name": "education_level",
        "comparison": "equals",
        "value": "masters"
      }
    }
  ]
}
```

{% enddetails %}

## ユースケース - 予測スコアの評価 {#use-case-evaluating-forecast-score}

Limbikを使用して、合成オーディエンスに対するメッセージの推定スコアを作成できます。Limbikの`forecasts/synchronous`エンドポイントを使用してプログラムで実行します。

### オプション 1 - 同期予測 {#option-1-synchronous-forecast}

テンプレート生成からのレスポンスペイロードを、同期予測エンドポイントで直接使用できます。

{% details 汎用リクエスト例 %}

`````````sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/synchronous' \
  -H 'accept: application/json' \
  -H 'account_id: aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "Day 1 of the 2026 Formula 1 Bahrain testing session has concluded. Lando Norris recorded the fastest time in the McLaren, with Ferrari in second place. Cadillac drivers Sergio Perez and Valtteri Bottas completed 107 laps, nearly two race distances, and Audi introduced significant upgrades. Which team do you expect to perform best in Australia? #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": []
  }
}'
```

{% enddetails %}

{% details レスポンス例（省略版） %}

```json
{
  "uid": "6c5e28ef-8796-4659-a743-d842a06c9bf7",
  "datetime": "2026-02-11T20:04:06.545+00:00",
  "userId": "9cdd921c-f62f-46a6-902f-a6b0d1702f99",
  "accountId": "aca61bd5-7132-499c-946e-42d092cc1156",
  "name": "Formula one season t...",
  "user_message_context": "",
  "population": [
    {
      "name": "us2",
      "display_name": "US Adults",
      "categories": []
    }
  ],
  "privacy_compliant": false,
  "model_outputs": {
    "belmetrics": {
      "metrics": {
        "moe": 0.02144,
        "pfi": "0.3611",
        "min_val": 0.2941,
        "mean_val": 0.41831
      }
    },
    "virmetrics": {
      "metrics": {
        "moe": 0.02381,
        "pfi": "0.3611",
        "min_val": 0.2,
        "mean_val": 0.30395
      }
    },
    "model_variant": "v4_0_0"
  }
}
```

{% enddetails %}

### オプション 2: セグメントを使用した予測ペイロードの準備 {#option-2-prepare-forecast-payload-with-segments}

選択したセグメントを使用して予測ペイロードを作成します。セグメントは簡略化されたコンポジットキー形式を使用します。

{% details セグメント固有のリクエスト例 %}

```json
{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren's beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac's debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi's radical upgrades already turning heads too. Who's your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": [
      "gender::female"
    ]
  }
}
```

{% enddetails %}