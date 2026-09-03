---
nav_title: Jasper
article_title: Jasper
description: "このリファレンス記事では、BrazeとJasperの連携について説明します。"
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jasper

> [Jasper](https://www.jasper.ai/)は、ブログ、広告、ソーシャルメディアなど、さまざまなチャネルにわたって高品質でブランドに沿ったコンテンツの作成、管理、スケーリングを可能にするAI搭載のコンテンツプラットフォームです。

_この連携はJasperによって管理されています。_

## 概要 {#overview}

JasperとBrazeの連携により、コンテンツ作成とキャンペーン実行を効率化できます。Jasperを使用すると、マーケティングチームは高品質でブランドに沿ったコピーを数分で生成できます。Brazeは、これらのメッセージを最適なタイミングで適切なオーディエンスに配信します。この連携により、シームレスなワークフローが促進され、手作業が削減され、より強力なエンゲージメント成果が得られます。

この連携を使用する利点は以下のとおりです。

- **迅速なキャンペーン実行：** 数週間ではなく、数分でキャンペーンを起動できます。
- **一貫したブランドボイス：** Jasperテンプレートを使用して、生成されたコピーがブランドガイドラインに厳密に準拠していることを確認できます。
- **ターゲットコンテンツの生成：** オーディエンスセグメント、スタイルガイド、独自のナレッジアイテムを使用して、高度にカスタマイズされたメッセージングを作成できます。
- **ダイナミックなパーソナライゼーション：** Braze内でスケーラブルなパーソナライゼーションを実現するために、{% raw %}`{{${first_name}}}`{% endraw %}のようなLiquidプレースホルダーを使用できます。
- **エラーの削減：** 自動化されたワークフローにより、コピー＆ペーストのエラーが最小化され、手動ステップが削減されます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ------------------- | ---------------- |
| Jasperアカウント | このパートナーシップを利用するにはJasperアカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー。<br><br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>このキーは、Brazeダッシュボードで**設定** > **API キー**に移動して生成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。具体的なエンドポイントは、インスタンスのBraze URLによって異なります。詳細については、[Braze APIの基本：エンドポイント]({{site.baseurl}}/api/basics/#endpoints)のドキュメントを参照してください。 |
{: .reset-td-br-1 .rest-td-br-2 aria-label="Prerequisites" }

## 連携方法 {#integration-methods}

Jasperでコンテンツを生成し、Brazeテンプレートを更新するには、2つの方法があります。

1. Jasper APIを直接使用する
2. Jasper Studioを使用してBraze対応のカスタムアプリを構築する

{% tabs %}
{% tab Jasper API %}

## 方法：Jasper APIを直接使用する {#method-use-jasper-api-directly}

この方法は、JasperおよびBrazeでの手動設定をバイパスして、BrazeでメールHTMLテンプレートをプログラムで作成・更新する場合に最適です。

### ステップ1：Jasperのセットアップ {#step-1-set-up-jasper}

1. [Getting Started](https://developers.jasper.ai/docs/getting-started-1)の手順に従って、Jasper APIキーを生成します。
2. Braze HTMLメールテンプレートの生成に最適化されたJasperのビルド済みテンプレートを使用します。テンプレートIDは`skl_BC53D8AC5B4B47E8BE557EBB706E9B47`です。
3. 以下のフィールドの値を収集します。これらは、Braze HTMLメールテンプレートのコンテンツを生成するリクエストを行うために必要です。

| フィールド | 説明 |
| --- | --- |
| `emailObjective` | メールの目標を明確に定義します。 |
| `ctaLink` | コールトゥアクションのURL。 |
| `unsubscribeLink` | マーケティングメールに必須です。 |
| `brandColor` | 16進数形式のブランドのプライマリカラー（例：`#4dfa8a`）。 |
{: .reset-td-br-1 .rest-td-br-2 aria-label="Step 1: Set up Jasper" }

**オプションフィールド**

| フィールド | 説明 |
| --- | --- |
| `toneId` | ブランドボイス |
| `audienceId` | オーディエンスセグメンテーション |
| `styleId` | スタイルガイド |
| `knowledgeIds` | コンテンツコンテキストの拡張。最大3つのIDを追加できます。 |
{: .reset-td-br-1 .rest-td-br-2 aria-label="Step 1: Set up Jasper" }

{: start="4"}
4. Jasper APIを使用してテンプレートを実行し、出力を生成します。これにより、`subject`、`preheader`、および`body`（HTMLコンテンツ）を含むJSONペイロードが生成されます。

{% subtabs %}
{% subtab Sample request %}

### サンプルリクエスト {#sample-request}

{% raw %}
```bash
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### 出力例 {#sample-output}
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### ステップ2：Brazeのセットアップ {#step-2-set-up-braze}

ステップ1でJasperによって生成された`subject`、`preheader`、および`body`を使用して、Braze REST APIにPOSTリクエストを行い、[新しいメールテンプレートを作成]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)します。Braze REST APIキーに`templates.email.create`および`templates.email.update`の権限があることを確認してください。

### メールテンプレートを作成するためのBraze APIリクエストの例 {#sample-braze-api-request-to-create-an-email-template}

`````````bash
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## 方法：Jasper StudioでBraze対応のカスタムアプリを構築する {#method-build-a-braze-ready-custom-app-with-jasper-studio}

Jasper Studioは、ITサポートを必要とせずにカスタマイズされたAIアプリを構築できるJasper内のノーコードプラットフォームです。Braze API用に特別にフォーマットされたJSON構造を生成するカスタムアプリを設計したり、Brazeメッセージに手動で追加できるコンテンツを生成したりできます。

1. Jasperのホーム画面で、**Create an App**を選択します。
2. 作成するアプリを指定します。たとえば、**Braze HTML Email Template**や**Content Block Template**などです。
3. Jasperが生成する入力プロンプトフィールドを編集します。HTMLメールテンプレートの場合、件名行、プリヘッダー、HTML本文、タグ、インラインCSS切り替え、テンプレート名の入力フォームを含めることができます。
4. 一貫したパーソナライゼーションとダイナミックコンテンツのためのLiquidベストプラクティスに関するガイダンスとナレッジの埋め込みを統合します。
5. コンテンツ生成のためにLarge Language Model（LLM）に提供する指示を調整します。
6. 目的の出力のサンプルを提供します。これには、Brazeペイロード用にフォーマットされた自動化されたJSON出力を含めることができます。
7. 以下を生成してエクスポートします。
- **ダイレクトコピー＆ペースト：** コンテンツをコピーしてBrazeプラットフォームに直接貼り付けることができます。
- **JSON出力：** JSON出力を生成します。このペイロードは、`curl`またはミドルウェアを介してBrazeエンドポイントを直接呼び出すか、メールオペレーションワークフローに統合するために使用できます。

![Jasper Brazeカスタムアプリ。]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## JSON出力の例（カスタムアプリ） {#sample-json-output-custom-app}

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## Braze APIリクエストの例（カスタムアプリ出力を使用） {#sample-braze-api-request-using-custom-app-output}

{% raw %}
`````````bash
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

また、マーケターの場合は、ブランドガイドラインに沿ったカスタムアプリを作成し、HTMLやコピー＆ペーストなしでコンテンツを生成し、Brazeテンプレートを使用してスタイリングすることもできます。

{% endtab %}
{% endtabs %}

{% alert note %}
その他のサポートについては、[Jasper APIドキュメント](https://developers.jasper.ai/reference/gettemplate-1)および[Jasper Studioヘルプセンター](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio)を参照してください。
{% endalert %}