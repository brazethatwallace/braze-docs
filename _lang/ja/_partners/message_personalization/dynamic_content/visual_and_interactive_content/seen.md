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
> この統合により、ユーザーデータをBrazeからSeenに送信し、パーソナライズされた動画を生成し、固有のプレーヤーURLやサムネイルなどのアセットをBrazeに返して、キャンペーンやキャンバスで使用できます。


## ユースケース {#use-cases}

Seenは、カスタマーライフサイクル全体にわたって、以下のような自動化されたパーソナライズ済み動画配信をサポートしています。

- **オンボーディング**: ユーザープロファイルやサインアップのコンテキストに合わせてパーソナライズされた動画で新規ユーザーを歓迎します
- **コンバージョンとアクティベーション**: 文脈に応じた動画メッセージングで重要なアクションを強化します
- **ロイヤルティとアップセル**: パーソナライズされたオファーや利用マイルストーンをハイライトします
- **ウィンバックと解約防止**: カスタマイズされた動画コンテンツで非アクティブユーザーを再エンゲージします


## 前提条件 {#prerequisites}

始める前に、以下の表に記載されているアクセス権とデータがあることを確認してください。

| 前提条件 | 説明 |
|--------------|-------------|
| Seenプラットフォームへのアクセス | 公開済みプロジェクトを持つSeenプラットフォームのサブスクリプション、またはアクティブなSeenキャンペーンが必要です。プロジェクトエンドポイントの取得とAPIトークンの生成には、プロジェクトへのアクセスも必要です。 |
| Brazeデータ変換Webhook URL | Brazeデータ変換を使用して、Seenからの受信データをBrazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)で受け入れられる形式に再フォーマットします。 |
| Brazeユーザーデータ | 動画のパーソナライゼーションには、ユーザーレベルのデータが必要です。関連する属性がBrazeで利用可能であることを確認し、一意識別子として**`braze_id`**を渡してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }




## Seenプロジェクトの仕組み {#how-seen-projects-work}

Seenは、プロジェクト内の[Run](https://docs.seen.io/run)タブを使用して、受信データの処理方法と動画出力の生成方法をコントロールします。

プロジェクトのワークフロー:

- 外部システム（Brazeなど）からデータを受信する
- ロジックとパーソナライゼーションルールを適用する
- 動画と関連アセットを生成する
- 設定可能なレスポンスペイロードを返す

Runタブには以下が含まれます。

- **Create via API**: プロジェクトAPIの詳細を開きます。
- **Import CSV**: パーソナライゼーションデータを手動でインポートします（このウォークスルーでは使用しません）。
- **Add webhook**: Brazeに返送されるレスポンスペイロードを定義します。
- **View videos**: 生成された動画と受信データのステータスを表示します。

Webhookレスポンスは設定可能であるため、Seenが返す出力フィールドが、Brazeデータ変換が期待する属性と一致するように調整してください。


## レート制限 {#rate-limit}

Seen APIは10秒ごとに最大100コールを受け付けます。


## 統合 {#integration}

この例では、BrazeがユーザーデータをSeenに送信し、パーソナライズされた動画を生成します。Seenは次に、固有の動画プレーヤーURLとサムネイルURLを返し、これらは[メッセージング]({{site.baseurl}}/user_guide/messaging/)で使用するためにBrazeの[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)として保存されます。

Seenで複数の動画キャンペーンを実施している場合は、各キャンペーンに対してこのプロセスを繰り返してください。

### ステップ1: Webhookキャンペーンを作成してSeenにデータを送信する {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Brazeで新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/)を作成します。

以下のようにWebhookを設定します。

- **Webhook URL**:
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`
  SeenプラットフォームプロジェクトのRunタブでプロジェクトエンドポイントを確認してください。

- **HTTPメソッド**: POST

- **リクエスト本文**: Raw Text
  以下の例を出発点として使用してください。フィールドのオプションと制限については、[Seenのデータ作成ドキュメント](https://docs.seen.io/create-data)を参照してください。

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

  SeenプラットフォームプロジェクトのRunタブで[APIトークン](https://docs.seen.io/authorization)を生成してください。サポートが必要な場合は、Seenのカスタマーサクセスマネージャーにお問い合わせください。

- **Test**タブでユーザーを使用してWebhookをテストします。
- テストが成功したら、Webhookのセットアップを完了してください。


### ステップ2: Seenプラットフォームでプロジェクトを設定する {#step-2-configure-a-project-in-the-seen-platform}

Seenプロジェクトで、[Run](https://docs.seen.io/run)タブを使用して動画を公開し、アウトバウンドWebhookを登録します。Runタブの概念的な概要については、[Seenプロジェクトの仕組み](#how-seen-projects-work)を参照してください。

1. Seenプラットフォームでプロジェクトを作成し、動画を構築してから、**Publish**を選択します。プロジェクトが公開されると、受信データから動画の生成が開始されます。
2. Runタブで、**Add a webhook**を選択します。

#### Webhookレスポンスの要件 {#webhook-response-requirements}

レスポンスペイロードは設定可能です。次のステップのBrazeデータ変換がマッピングできるように、以下の表のフィールドを返してください。

| フィールド | 説明 |
|-------|-------------|
| `id` | Brazeから送信される`braze_id`と一致する必要があります |
| `player_url` | パーソナライズされた動画プレーヤーのユニークなURL |
| `email_thumbnail_url` | パーソナライズされた動画サムネイルのURL |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhookレスポンスの要件" }

追加の属性が必要な場合は、レスポンスに追加し、Brazeでマッピングしてください。


### ステップ3: Seenからデータを受け取るためのデータ変換を作成する {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Brazeデータ変換を使用して、Seenのレスポンスを処理し、ユーザープロファイルに動画アセットを保存します。

1. Brazeで以下の[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)を作成します。
   - `player_url`
   - `email_thumbnail_url`

2. **データ設定** > **データ変換**に移動し、**Create transformation**を選択します。

3. 変換を設定します。
   - **Start from scratch**
   - **Destination** > POST: Track users

4. 生成されたWebhook URLをSeenと共有するか、プロジェクトのRunタブの**Webhook**に追加します。

5. 以下の変換コードを使用します。

```javascript
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
6. 指定されたエンドポイントにテストペイロードを送信します。Seenプラットフォームプロジェクトにデータを送信する（先にプロジェクトを公開してください）か、[Postman](https://www.postman.com/)または同様のツールを使用してペイロードをBrazeに直接送信します。
7. **Validate**を選択して、変換が期待どおりに動作することを確認します。
8. **Save**および**Activate**を選択します。