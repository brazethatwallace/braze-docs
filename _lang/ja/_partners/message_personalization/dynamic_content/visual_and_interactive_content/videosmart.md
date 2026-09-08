---
nav_title: VideoSmart
article_title: VideoSmart
description: "このリファレンス記事では、BrazeとVideoSmartのパートナーシップについて説明します。VideoSmartは、パーソナライズされたインタラクティブな動画テクノロジーで、ブランドがデータドリブン型のノンリニアコンテンツを大規模に配信できるようにします。"
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/)は、パーソナライズされたインタラクティブな動画テクノロジーを提供し、データドリブン型のノンリニアコンテンツを大規模に配信できるようにします。各動画は顧客レベルのデータを使用して動的に生成され、単一の動画体験内でカスタマイズされたメッセージングとユーザージャーニーを実現します。
>
> VideoSmartとの連携により、BrazeのConnected ContentとLiquidテンプレートを使用してVideoSmartから動画アセットをリクエストし、パーソナライズされた動画コンテンツをメールキャンペーンに埋め込むことができます。この連携は通常、再利用可能なBrazeコンテンツブロックテンプレートを通じて実装され、キャンペーン全体で一貫したデプロイを可能にしながら、キャンペーンの選択やパーソナライゼーションロジックの柔軟性を維持します。

_この連携はVideoSmartによって開発・維持されています。_

## この連携について {#about-this-integration}

VideoSmartはBrazeと連携し、送信時にパーソナライズされた動画アセットをダイナミックに生成して、Brazeのキャンペーンやキャンバスのメールコンテンツに直接埋め込みます。

Brazeでは、関連するVideoSmartキャンペーンを選択し、送信時にLiquidテンプレートを使用して顧客属性をVideoSmartに渡します。これらの属性は、各受信者にユニークでパーソナライズされた動画体験をレンダリングするために使用されます。その後、Braze Connected Contentを使用して、VideoSmartのAPIから動画URLやアセットをリアルタイムでリクエストでき、スケーラブルなパーソナライゼーションが可能になります。

この連携は、LiquidテンプレートとConnected Contentをサポートする Brazeのメールメッセージ向けに設計されており、標準のBrazeユーザープロファイル属性やカスタムデータフィールドと連携するように設定できます。

## ユースケース {#use-cases}


一般的なユースケースには以下のものがあります。

- 顧客オンボーディングとウェルカムジャーニー
- 金融教育（年金や保険商品など）
- 年次報告書および規制に関するコミュニケーション
- 商品認知およびクロスセルキャンペーン
- カスタマーリテンションおよびリエンゲージメントキャンペーン
- 放棄カートリマインダー：顧客がカートに商品を追加したが購入しなかった場合に、カートに残した商品を紹介するパーソナライズされた動画を含むメールを送信します
- 購入後のフォローアップ：購入後、パーソナライズされたお礼の動画を送信し、関連商品をおすすめします

## 前提条件 {#prerequisites}

始める前に、以下を確認してください。

| 要件                        | 説明                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Braze Connected Content認証情報 | VideoSmartから提供された値で設定された、**basic_credentials**という名前のConnected Contentベーシック認証の認証情報 |
| **VideoSmartコンテンツブロック**テンプレート   | Brazeダッシュボードに追加された**VideoSmartコンテンツブロック**テンプレート（VideoSmartから提供）                                |
| Brazeメールメッセージ               | **VideoSmartコンテンツブロック**を挿入するBrazeキャンペーンメールまたはキャンバスメールステップ                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

以下の手順に従って、**VideoSmart コンテンツブロック**を有効にし、メールで使用します。

### ステップ1：Brazeで VideoSmart コンテンツブロックテンプレートを設定する {#step-1-set-up-the-videosmart-content-block-template-in-braze}

VideoSmart の担当者に **VideoSmart コンテンツブロック**テンプレートをリクエストし、Brazeダッシュボードに追加します。

VideoSmart から、コンテンツブロックで使用するConnected Content認証用の認証情報が提供されます。

### ステップ2：Connected Content認証を設定する {#step-2-set-up-connected-content-authentication}

Brazeで「basic_credentials」という名前のConnected Content Basic Authentication認証情報を作成します。

- [基本認証の使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-basic-authentication)の手順に従います。
- VideoSmart から提供されたユーザー名とパスワードを使用します。

### ステップ3：メールにコンテンツブロックを追加する {#step-3-add-the-content-block-to-your-email}

動画コンテンツを表示したい場所に、**VideoSmart コンテンツブロック**をメールに挿入します。

ほとんどのBrazeの設定では、Content Blocksは以下のパターンで参照されます（「VideoSmart_Campaign」をお使いのアカウントのコンテンツブロック名に置き換えてください）:

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
コンテンツブロック名は大文字と小文字が区別され、Brazeで設定した名前と完全に一致する必要があります。
{% endalert %}

### ステップ4：キャンペーンの上書きとデータの記録（オプション） {#step-4-override-campaign-and-record-data-optional}

コンテンツブロックがデフォルトをサポートしている場合、変数を設定せずに使用できます。

特定の VideoSmart キャンペーンを選択したり、カスタムパーソナライゼーションフィールドを渡したり、またはその両方を行う場合は、コンテンツブロックをレンダリングする前に以下のLiquid変数を設定します:

- `vs_campaign_id`：VideoSmart キャンペーン識別子
- `vs_record_data`：VideoSmart テンプレートに渡す値を含むJSON文字列

#### 例 {#example}

この例では、名と姓にBrazeのユーザー属性を使用しています:

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'Alex' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- `vs_record_data` で使用する値には必ずデフォルトを設定し、Brazeのメールプレビューが正しく表示されるようにしてください。
- `vs_record_data` は有効なJSONでなければならず、単一の文字列としてエンコードされている必要があります（この例では `strip_newlines` を使用しています）。
{% endalert %}

### ステップ5：VideoSmart のコンテンツブロックテンプレートが生成する変数を使用する {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

コンテンツブロックの実行後、メール内の他の場所で参照できる変数が生成されます。

一般的な変数は以下のとおりです:

{% raw %}
| 変数                              | 説明                                                   |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}`                 | パーソナライズされた動画のURL                          |
| `{{ poster_url }}`                | 動画のポスター画像のURL                                |
| `{{ output_data.VARIABLE_NAME }}` | コンテンツブロックによって公開される追加の出力フィールド |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ5：VideoSmart のコンテンツブロックテンプレートが生成する変数を使用する" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ5：VideoSmart のコンテンツブロックテンプレートが生成する変数を使用する" }

## レート制限 {#rate-limits}

VideoSmartのAPIには、1分あたり10,000リクエストのレート制限があります。この制限を超えると、エラーが発生したり、動画生成に遅延が生じたりする可能性があります。

このリスクを軽減するには、Brazeキャンペーンのレート制限を設定して、メッセージ送信速度がVideoSmart APIの処理能力を超えないようにしてください。

Brazeの配信速度とレート制限に関するガイダンスについては、[配信速度とレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を参照してください。

## 注意事項 {#considerations}

- Connected Contentはメッセージのレンダリング時に実行されるため、デフォルト値や属性が異なる場合、プレビューと送信時で値が異なることがあります。
- `video_url`などの変数を参照する前に、メールにコンテンツブロックが含まれていることを確認してください。
- `vs_record_data`でカスタムフィールドを使用する場合は、想定されるフィールド名をVideoSmartに確認してください。

## トラブルシューティング {#troubleshooting}

### プレビューが機能しない {#preview-not-working}

Brazeプレビューが失敗する場合（例えば、再試行の繰り返しや認証エラー）、以下を確認してください：

- Connected Content認証情報「basic_credentials」が存在し、正しく設定されていること。
- **VideoSmart Content Block**テンプレートがBrazeアカウントに存在すること。
- 必要な変数（例えば、`vs_campaign_id`や`vs_record_data`の必須フィールド）にプレビュー用のデフォルト値が設定されていること。

### VideoSmartのContent Blockテンプレート変数が期待される出力を生成しない {#videosmarts-content-block-template-variables-not-generating-expected-output}

VideoSmartのContent Blockテンプレートによって生成された変数が期待される出力を生成しない場合は、以下を確認してください：

- **VideoSmart Content Block**テンプレートがBrazeで正しく設定されていること。
- Connected Content認証が適切な認証情報で正しく設定されていること。
- メール内で変数を出力して、値が設定されていることを確認すること。例：`{% raw %}{{ video_url }}{% endraw %}`

カスタムキャンペーンを使用している場合は、以下も確認してください：

- `vs_campaign_id`が有効なキャンペーン識別子に設定されていること。
- `vs_record_data`が有効なJSONであり、期待されるフィールドが含まれていること。