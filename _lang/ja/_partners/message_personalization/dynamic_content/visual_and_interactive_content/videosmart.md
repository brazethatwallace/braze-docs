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
> VideoSmartとの連携により、Brazeのコネクテッドコンテンツとliquidテンプレートを使用してVideoSmartから動画アセットをリクエストし、パーソナライズされた動画コンテンツをメールキャンペーンに埋め込むことができます。この連携は通常、再利用可能なBraze Content Blockテンプレートを通じて実装され、キャンペーン全体で一貫したデプロイを可能にしながら、キャンペーンの選択やパーソナライゼーションロジックの柔軟性を維持します。

_この連携はVideoSmartによって開発・維持されています。_

## この連携について {#about-this-integration}

VideoSmartはBrazeと連携し、送信時にパーソナライズされた動画アセットを動的に生成し、Brazeのキャンペーンおよびキャンバスのメールコンテンツに直接埋め込みます。

Brazeでは、関連するVideoSmart キャンペーンを選択し、送信時にLiquidテンプレートを通じて顧客属性をVideoSmartに渡します。これらの属性は、各受信者に対してユニークでパーソナライズされた動画体験をレンダリングするために使用されます。その後、Brazeのコネクテッドコンテンツを使用して、VideoSmartのAPIからリアルタイムで動画URLやアセットをリクエストでき、スケーラブルなパーソナライゼーションが可能になります。

この連携は、LiquidテンプレートとコネクテッドコンテンツをサポートするBrazeメールメッセージ向けに設計されており、標準的なBrazeユーザープロファイル属性またはカスタムデータフィールドと連携するように設定できます。

## ユースケース {#use-cases}


一般的なユースケースには以下が含まれます。

- 顧客のオンボーディングとウェルカムジャーニー
- 金融教育（年金や保険契約など）
- 年次報告書と規制関連のコミュニケーション
- 製品認知とクロスセルキャンペーン
- カスタマーリテンションと再エンゲージメントキャンペーン
- カート放棄リマインダー：顧客がカートに商品を追加したが購入しなかった場合、カートに残した商品をハイライトするパーソナライズされた動画付きのメールを送信します
- 購入後のフォローアップ：購入後にパーソナライズされたお礼動画を送信し、関連商品をおすすめします

## 前提条件 {#prerequisites}

開始する前に、以下を確認してください。

| 要件 | 説明 |
| --- | --- |
| Brazeコネクテッドコンテンツの認証情報 | VideoSmartから提供された値で設定された、**basic_credentials**という名前のコネクテッドコンテンツBasic認証の認証情報 |
| **VideoSmart Content Block**テンプレート | Brazeダッシュボードに追加された**VideoSmart Content Block**テンプレート（VideoSmartから提供） |
| Brazeメールメッセージ | **VideoSmart Content Block**を挿入するBraze キャンペーンメールまたはキャンバスメールステップ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

以下のステップに従って、**VideoSmart Content Block**を有効にし、メールで使用します。

### ステップ 1：BrazeでVideoSmart Content Blockテンプレートを設定する {#step-1-set-up-the-videosmart-content-block-template-in-braze}

VideoSmartの担当者に**VideoSmart Content Block**テンプレートをリクエストし、Brazeダッシュボードに追加します。

VideoSmartは、Content Blockで使用されるコネクテッドコンテンツ認証用の認証情報を提供します。

### ステップ 2：コネクテッドコンテンツ認証を設定する {#step-2-set-up-connected-content-authentication}

Brazeで「basic_credentials」という名前のコネクテッドコンテンツBasic認証の認証情報を作成します。

- [Basic認証の使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-basic-authentication)の手順に従ってください。
- VideoSmartから提供されたユーザー名とパスワードを使用します。

### ステップ 3：メールにContent Blockを追加する {#step-3-add-the-content-block-to-your-email}

動画コンテンツを表示したい場所に、**VideoSmart Content Block**をメールに挿入します。

ほとんどのBrazeセットアップでは、Content Blocksは以下のパターンで参照されます（「VideoSmart_Campaign」をアカウント内のContent Block名に置き換えてください）。

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
Content Block名は大文字と小文字が区別され、Brazeで設定した名前と完全に一致する必要があります。
{% endalert %}

### ステップ 4：キャンペーンの上書きとレコードデータ（オプション） {#step-4-override-campaign-and-record-data-optional}

Content Blockがデフォルト値をサポートしている場合、変数を設定せずに使用できます。

特定のVideoSmart キャンペーンを選択したり、カスタムパーソナライゼーションフィールドを渡したり、またはその両方を行う必要がある場合は、Content Blockをレンダリングする前に以下のLiquid変数を設定します。

- `vs_campaign_id`：VideoSmart キャンペーン識別子
- `vs_record_data`：VideoSmartテンプレートに渡す値を含むJSON文字列

#### 例 {#example}

この例では、名と姓にBrazeユーザー属性を使用しています。

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
- Brazeのメールプレビューが正しく表示されるように、`vs_record_data`で使用する値には必ずデフォルト値を設定してください。
- `vs_record_data`は有効なJSONであり、単一の文字列としてエンコードされている必要があります（例では`strip_newlines`を使用しています）。
{% endalert %}

### ステップ 5：VideoSmartのContent Blockテンプレートで生成された変数を使用する {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

Content Blockの実行後、メール内の他の場所で参照できる変数が生成されます。

一般的な変数には以下が含まれます。

{% raw %}
| 変数 | 説明 |
| --- | --- |
| `{{ video_url }}` | パーソナライズされた動画のURL |
| `{{ poster_url }}` | 動画のポスター画像のURL |
| `{{ output_data.VARIABLE_NAME }}` | Content Blockによって公開される追加の出力フィールド |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 5：VideoSmartのContent Blockテンプレートで生成された変数を使用する" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 5：VideoSmartのContent Blockテンプレートで生成された変数を使用する" }

## レート制限 {#rate-limits}

VideoSmartのAPIには、1分あたり10,000リクエストのレート制限があります。この制限を超えると、エラーが発生したり、動画生成に遅延が生じたりする場合があります。

このリスクを軽減するために、メッセージ送信レートがVideoSmart APIの容量を下回るようにBraze キャンペーンのレート制限を設定してください。

配信速度とレート制限に関するBrazeのガイダンスについては、[配信速度とレート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#delivery-speed-rate-limiting)を参照してください。

## 考慮事項 {#considerations}

- コネクテッドコンテンツはメッセージのレンダリング時に実行されるため、デフォルト値や属性が異なる場合、プレビューと送信で値が異なることがあります。
- `video_url`などの変数を参照する前に、メールにContent Blockが含まれていることを確認してください。
- `vs_record_data`でカスタムフィールドを使用する場合は、VideoSmartに期待されるフィールド名を確認してください。

## トラブルシューティング {#troubleshooting}

### プレビューが機能しない {#preview-not-working}

Brazeのプレビューが失敗する場合（例：繰り返しのリトライや認証エラー）、以下を確認してください。

- コネクテッドコンテンツの認証情報「basic_credentials」が存在し、正しく設定されていること。
- **VideoSmart Content Block**テンプレートがBrazeアカウントに存在すること。
- 必要な変数（例：`vs_campaign_id`や`vs_record_data`の必須フィールド）にプレビュー用のデフォルト値が設定されていること。

### VideoSmartのContent Blockテンプレート変数が期待される出力を生成しない {#videosmarts-content-block-template-variables-not-generating-expected-output}

VideoSmartのContent Blockテンプレートで生成された変数が期待される出力を生成しない場合は、以下を確認してください。

- **VideoSmart Content Block**テンプレートがBrazeで正しく設定されていること。
- コネクテッドコンテンツ認証が適切な認証情報で正しく設定されていること。
- メール内で変数を出力して、値が設定されていることを確認してください。例：`{% raw %}{{ video_url }}{% endraw %}`

カスタムキャンペーンを使用している場合は、以下も確認してください。

- `vs_campaign_id`が有効なキャンペーン識別子に設定されていること。
- `vs_record_data`が有効なJSONであり、期待されるフィールドが含まれていること。