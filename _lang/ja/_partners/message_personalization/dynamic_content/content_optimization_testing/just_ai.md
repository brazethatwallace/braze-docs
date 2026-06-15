---
nav_title: JustAI
article_title: JustAI
description: "このリファレンス記事では、BrazeとJustAIのパートナーシップについて説明します。JustAIはAIベースのSaaSビジネスプラットフォームで、既存のCampaignsのパーソナライズバージョンを作成し、件名、クリエイティブコンテンツ、HTMLメールレイアウトを時間の経過とともに最適化します。"
alias: ["/partners/just_ai/", "/partners/just_words/"]
page_type: partner
---

# JustAI統合ガイド {#justai-integration-guide}

> [JustAI](https://www.getjust.ai/)は、ライフサイクルマーケティングチャネルにおいてメッセージングを大規模にハイパーパーソナライズし、数百のバリエーションを動的にテストしてパフォーマンスの低いコンテンツを自動更新する機能を提供します。

JustAIをBrazeの[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)と組み合わせて既存のBraze CampaignsやCanvasesをパーソナライズすると、JustAIはBraze Currentsを使用してコンテンツを動的に最適化します。手動での対応は不要です。

## メリット {#what-are-the-benefits}

統合が完了すると、JustAIプラットフォームを活用して以下のことが可能になります。

- リアルタイムの実験結果を確認する
- コピーを動的に編集する
- パフォーマンスインサイトを表示する

{% alert note %}
ご質問がありますか？JustAIの[予約ページ](https://www.getjust.ai/book-demo)または共有Slackチャネルからお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| JustAIアカウント | このパートナーシップを利用するには、[JustAI](https://www.getjust.ai/)アカウントが必要です。JustAIアカウントをお持ちでない場合は、[30分のオンボーディングコールを予約](https://www.getjust.ai/book-demo)してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## JustAIとBrazeの統合 {#integrating-justai-with-braze}

### ステップ 1: JustAIテンプレートを作成する {#step-1-create-a-justai-template}

1. JustAIコンソールに移動し、[新しいテンプレートを作成](https://console.getjust.ai/new)します。
2. 文字、数字、アンダースコアのみを使用した覚えやすいIDを選択します。
3. 基本的なCampaignの詳細を入力します。
4. AIを使用してパーソナライズされたバリエーションを生成します。

![JustAIテンプレート作成プラットフォーム。]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### ステップ 2: JustAI APIキーを作成する {#step-2-create-a-justai-api-key}

1. **Org Settings** > **API Keys** > **Generate API Key** に移動します。
2. APIキーをコピーし、安全な場所に保存します。

![JustAI APIキーフォーム。]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### ステップ 3: BrazeコンテンツでJustAIを使用する {#step-3-use-justai-in-your-braze-content}

JustAIはコネクテッドコンテンツを使用してCanvasesやCampaignsと連携します。Canvasを作成する場合、各メールステップは固有のJustAIテンプレートに対応する必要があります。

#### ステップ 3.1: ABテストを設定する {#step-31-set-up-your-ab-test}

{% tabs %}
{% tab Canvas %}

1. Canvasで、**バリアントを追加** > **バリアントを追加**を選択して、希望するバリアント数になるまで追加し、各バリアントにステップ（メールメッセージステップなど）を追加します。
2. オーディエンストラフィックを希望どおりに分割します。たとえば、2つのバリアントがある場合、それぞれに50%を割り当てることができます。または、2つのバリアントにそれぞれ40%、コントロールグループに20%を割り当てることもできます。CanvasのABテストの詳細については、[Canvasの作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)を参照してください。
3. コネクテッドコンテンツで使用するメッセージステップの作成画面で、JustAIコンソールからコネクテッドコンテンツスニペットを貼り付けます。以下はスニペットの例です。

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Braze ABテストCanvasの設定。]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. Campaignの**メッセージを作成**ステップで、2つのバリアントを作成します。
2. **ターゲットオーディエンス**ステップで、**ABテスト**セクションに移動し、各バリアント（およびオプションのコントロールグループ）を受け取るユーザーの割合を変更します。最適化オプションを選択して、テストをさらにカスタマイズすることもできます。CampaignsのABテストの詳細については、[多変量テストとABテストの作成]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)を参照してください。
3. メッセージ作成画面で、JustAIコンソールからコネクテッドコンテンツスニペットを貼り付けます。以下のLiquidスニペットはその例です。

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### ステップ 3.2: カスタム属性でパーソナライゼーションを追加する（オプション） {#step-32-add-personalization-with-custom-attributes-optional}

カスタム属性（`industry` など）を使用してメッセージをパーソナライズするには、以下のLiquid形式を使用します。

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

`industry` のカスタム属性は {% raw %}`&attrs.industry={{ custom_attribute.industry }}`{% endraw %} で指定されていることに注意してください。

![HTMLメッセージ作成画面でのBraze Liquidロジック。]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### ステップ 4: メールをプレビューする {#step-4-preview-the-email}

Brazeでメールをプレビューし、パーソナライズされたコンテンツが正しくレンダリングされることを確認してください。

![JustAIメールのBrazeメッセージプレビュー。]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### ステップ 5: Braze Currentsを設定する {#step-5-set-up-braze-currents}

Braze Currentsにより、パフォーマンスのトラッキングと時間の経過に伴う最適化が可能になります。

1. Brazeで、**パートナー連携** > **データのエクスポート**に移動します。
2. **Create New Test Current**を選択し、次に**Test Amazon S3 Data Export**を選択します。

![「Test Amazon S3 Data Export」オプションを含む「Create New Test Current」ドロップダウン。]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. オンボーディング時にJustAIから提供されたS3アクセスID、AWSシークレットアクセスキー、バケット名、フォルダーを入力します。

![AWSシークレットアクセスキーの認証情報セクション。]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. 送信、開封、クリック、配信停止、コンバージョンなど、トラッキングするイベントを選択します。

![選択可能なイベントを含むメッセージエンゲージメントイベントセクション。]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Braze Currentを起動します。

以上で設定は完了です！これで、JustAIをBrazeのコネクテッドコンテンツと組み合わせて使用できます。