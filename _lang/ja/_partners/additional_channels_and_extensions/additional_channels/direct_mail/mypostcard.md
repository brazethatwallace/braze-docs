---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "このリファレンス記事では、CRMワークフローの追加チャネルとしてダイレクトメールを使用できるようにする、BrazeとMyPostcardのパートナーシップについて説明します。"
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com)は世界有数のポストカードアプリで、ダイレクトメールキャンペーンを簡単に実行でき、シームレスで収益性の高い方法で顧客とつながることができます。

MyPostcardとBrazeの統合を使用すると、印刷物の郵送を簡単に顧客に送信できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2Bアカウント | この統合を利用するには、MyPostcardへの登録が必要です。 |
| B2B APIキーと認証情報 | APIキーと認証情報は、MyPostcard B2B管理ツールで確認できます。 |
| 承認されたMyPostcard B2Bキャンペーン | この統合を利用するには、MyPostcard B2Bツールで印刷郵送キャンペーンを設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

ダイレクトメールキャンペーンを向上させるには、従来の大量郵送を超える方法を採用し、印刷物の郵送をワークフローにシームレスに統合することが重要です。このアプローチにより、メールマガジンをオプトアウトした顧客や、メールがスパムとしてマークされている特定の顧客にアプローチできます。MyPostcardを使えば、Brazeから直接、印刷物の郵送キャンペーンを簡単に送ることができます。

- 専門知識がなくても、Brazeで直感的なワークフローを構築し、印刷メールを強力な新しいチャネルとして組み込めます。
- いくつかの簡単なステップで、パーソナライズされた印刷物の可能性を引き出せます。
- 専任チームによるパーソナライズされたサポートに裏打ちされた、わかりやすい導入のメリットを享受できます。

## 統合 {#integration}

MyPostcardと統合するには、[ログインまたはサインアップ](https://www.mypostcard.com/b2b/admin/)して、[Braze webhook]({{site.baseurl}}/user_guide/channels/webhooks/)を使って最初のキャンペーンを作成します。

### ステップ 1:Braze Webhookテンプレートを作成する {#step-1-create-your-braze-webhook-template}

今後のCampaignsやCanvasesで使用するMyPostcard Webhookテンプレートを作成するには、Brazeプラットフォームで**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。

単発のMyPostcard Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新規キャンペーン作成時にBrazeで**Webhook**を選択します。以下のフィールドに入力してください。

| フィールド | 説明 |
|---------------|-----------------------------------------------------------|
| **Webhook URL** | B2B管理ツールに表示されるWebhook URL。 |
| **リクエスト本文** | 生テキスト（B2B管理ツールにあるJSON形式）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create your Braze webhook template" }

#### リクエストメソッドとヘッダー {#request-method-and-headers}

MyPostcardでは、HTTPメソッドと以下のHTTPヘッダーをテンプレートに含める必要があります。

{% raw %}
<table aria-label="Request method and headers">
  <caption>リクエストメソッドとヘッダー</caption>
  <thead>
    <tr>
      <th><strong>フィールド</strong></th>
      <th><strong>詳細</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTPメソッド</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>ユーザー名</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>パスワード</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request method and headers" }

#### リクエスト本文 {#request-body}

B2B管理ツールに表示されているリクエスト本文をコピーし、Liquidパーソナライゼーションタグを使用してプレースホルダーにコンテンツを入力します。

![JSON本文とWebhook情報を示す「作成」タブ。]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### ステップ 2:リクエストをプレビューする {#step-2-preview-your-request}

次に、**プレビュー**パネルでリクエストをプレビューするか、**テスト**タブに移動して、ランダムユーザー、既存ユーザーを選択するか、カスタムユーザーを作成してWebhookをテストします。ページを離れる前にテンプレートを保存することを忘れないでください。

![実装を検証するためのさまざまなフィールドを持つWebhookテストタブ。]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}