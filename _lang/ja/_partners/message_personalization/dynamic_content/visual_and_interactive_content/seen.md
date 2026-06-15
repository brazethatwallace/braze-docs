---
nav_title: Seen
article_title: Seen
description: "Seenはパーソナライズされた動画体験を大規模に実現し、ブランドがカスタマージャーニー全体でより高いエンゲージメントを促進できるよう支援します。"
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io)は、ブランドがパーソナライズされた動画体験を大規模に作成し、配信することを可能にします。Seenを使えば、データを中心に動画をデザインし、クラウド上で大規模にパーソナライズし、最適な場所に配信できます。
>
> BrazeとSeenの統合により、ユーザーデータをBrazeからSeenに送信し、パーソナライズされた動画をダイナミックに生成し、固有のプレーヤーURLやサムネイルなどの動画アセットをBrazeに戻して、キャンペーンやキャンバスで使用できます。


## ユースケース {#use-cases}

Seenは、カスタマーライフサイクル全体にわたって、以下のような自動化されたパーソナライズ済み動画配信をサポートしています。

- **オンボーディング**: ユーザープロファイルやサインアップのコンテキストに合わせてパーソナライズされた動画で新規ユーザーを歓迎します
- **コンバージョンとアクティベーション**: 文脈に応じた動画メッセージングで重要なアクションを強化します
- **ロイヤルティとアップセル**: パーソナライズされたオファーや利用マイルストーンをハイライトします
- **ウィンバックと解約防止**: カスタマイズされた動画コンテンツで非アクティブユーザーを再エンゲージします


## 前提条件 {#prerequisites}

始める前に、以下のものが必要です。

| 前提条件 | 説明 |
|--------------|-------------|
| Seenプラットフォームへのアクセス | SeenプラットフォームのサブスクリプションまたはアクティブなSeenキャンペーンが必要です。ワークスペースIDを取得し、APIトークンを生成するには、ワークスペース設定にアクセスする必要があります。 |
| Brazeデータ変換Webhook URL | Brazeデータ変換は、Seenからの受信データをBrazeの/users/trackエンドポイントで受け入れられるように再フォーマットします。 |
| Brazeユーザーデータ | 動画のパーソナライゼーションには、ユーザーレベルのデータが必要です。関連する属性がBrazeで利用可能であることを確認し、一意識別子として**braze_id**を渡してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }




## Seen Journeyの仕組み {#how-seen-journeys-work}

Seenは、受信データの処理方法と動画出力の生成方法をコントロールするために[Journey](https://docs.seen.io/journey)を使用しています。

Journeyは、以下を行う設定可能なワークフローです。
- 外部システム（Brazeなど）からデータを受信する
- ロジックとパーソナライゼーションルールを適用する
- 動画と関連アセットを生成する
- 設定可能なレスポンスペイロードを返す

Journeyは**ノード**で構成され、それぞれが特定の機能を持ちます。

- **トリガーノード**: Journeyの開始方法とタイミングを定義します（Braze統合の場合は、`On Create`トリガーを使用）
- **条件ノード**: データ値に基づいて、ユーザーを異なるロジックパスにルーティングします
- **プロジェクトノード**: 受信データを使用してダイナミックな動画パーソナライゼーションを適用します
- **プレーヤーノード**: ユニークな動画プレーヤーURLを生成します
- **Webhookノード**: Brazeに返送されるレスポンスペイロードを定義します

Journeyのレスポンスは設定可能であるため、Seenが返す出力フィールドが、Brazeデータ変換が期待する属性と一致していることを確認してください。


## レート制限 {#rate-limit}
Seen APIは10秒ごとに最大100コールを受け付けます。


## 統合 {#integration}

この例では、BrazeがユーザーデータをSeenに送信し、パーソナライズされた動画を生成します。Seenは次に、固有の動画プレーヤーURLとサムネイルURLを返し、これらはメッセージングで使用するためにBrazeのカスタム属性として保存されます。

Seenで複数の動画キャンペーンを実施している場合は、このプロセスを繰り返してBrazeをすべての動画キャンペーンに接続してください。

### ステップ1: Webhookキャンペーンを作成してSeenにデータを送信する {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Brazeで新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/)を作成します。

以下のようにWebhookを設定します。

- **Webhook URL**:
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`
  Seenプラットフォームの設定でワークスペースIDを確認してください。

- **HTTPメソッド**: POST
- **リクエスト本文**: Raw Text
  以下の例を出発点として使用してください。詳しくは[Seenのデータ作成ドキュメント](https://docs.seen.io/create-data)を参照してください。

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **リクエストヘッダー**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Seenプラットフォームのワークスペース設定で[APIトークン](https://docs.seen.io/authorization)を生成してください。Seenのカスタマーサクセスマネージャーにお問い合わせいただくこともできます。

- ユーザーでWebhookをテストするには、**Test**タブに切り替えてください。
- テストが意図したとおりに動作することを確認したら、Webhookのセットアップを完了してください。


### ステップ2: SeenプラットフォームでJourneyを設定する {#step-2-configure-a-journey-in-the-seen-platform}

Seenは[Journey](https://docs.seen.io/journey)を使用して、受信データをどのように処理し、パーソナライズし、Brazeに返すかを定義します。
各Journeyは、動画生成ロジックとレスポンスペイロードの両方をコントロールできるノードで構成された、設定可能なワークフローです。

Journeyを設定するには、以下の手順に従います。

1. Seenプラットフォームで新しいJourneyを作成します
2. **トリガーノード**を追加し、`On Create`トリガーを選択します
   これにより、BrazeがデータをSeenに送信したときにJourneyが開始されます。必要に応じて、ワークスペース内で[セグメンテーション](https://docs.seen.io/segments)ロジックを作成し、追加してください。
3. 必要に応じて、以下のノードを使用してロジックを構築します。
   - **条件ノード**: 属性値（プランタイプや地域など）に基づいてユーザーをルーティングします
   - **プロジェクトノード**: 受信データを使用してダイナミックな動画パーソナライゼーションを適用します
   - **プレーヤーノード**: ユニークな動画プレーヤーURLを生成します
4. Brazeに送り返すレスポンスを定義する**Webhookノード**を追加します

#### Webhookノードのレスポンス要件 {#webhook-node-response-requirements}

レスポンスペイロードは設定可能であるため、次のステップで説明するBrazeデータ変換をサポートするために、以下のフィールドが返されることを確認してください。

| フィールド | 説明 |
|------|-------------|
| `id` | Brazeから送信される`braze_id`と一致する必要があります |
| `player_url` | パーソナライズされた動画プレーヤーのユニークなURL |
| `email_thumbnail_url` | 生成された動画サムネイルのURL |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook node response requirements" }

ユースケースで追加の属性が必要な場合は、それらをレスポンスに含め、Brazeでマッピングしてください。


### ステップ3: Seenからデータを受け取るためのデータ変換を作成する {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Brazeデータ変換を使用して、Seen Journeyのレスポンスを取り込み、ユーザープロファイルに動画アセットを保存します。

1. Brazeで以下の[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)を作成します。
   - `player_url`
   - `email_thumbnail_url`
2. **データ設定** → **データ変換**を開き、**Create transformation**をクリックします
3. 変換を設定します。
   - **Start from scratch**
   - **Destination** → POST: Track users
4. 生成されたWebhook URLをSeenと共有するか、Journeyの**Webhookノード**に直接追加します
5. 以下の変換コードを使用します。

`````````javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. 指定されたエンドポイントにテストペイロードを送信します。Seenプラットフォームにデータを送信してJourneyを実行するか、[Postman](https://www.postman.com/)または同様のサービスを使用してペイロードをBrazeに直接送信します。
7. **Validate**を選択して、すべてが意図したとおりに動作することを確認します。
8. **Save**および**Activate**を選択します。