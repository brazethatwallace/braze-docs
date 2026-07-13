---
nav_title: Webhook テンプレート
article_title: Webhook テンプレート
page_order: 5
tool:
  - Templates
channel:
  - webhooks
description: "Brazeプラットフォーム内で後から使用するためのWebhookテンプレートの作成とカスタマイズ方法について説明します。"

---

# Webhook テンプレートを作成する {#create-a-webhook-template}

> webhookを構築してカスタマイズする際に、Brazeプラットフォーム内で後から使用するためのWebhookテンプレートを作成して活用できます。これにより、さまざまなキャンペーンにわたって一貫したwebhookを構築できます。

## ステップ 1:Webhook テンプレートエディターに移動する {#step-1-go-to-the-webhook-template-editor}

Brazeダッシュボードで、**コンテンツ** > **Webhook**に移動します。

![事前にデザインされたWebhookテンプレートと保存済みWebhookテンプレートが表示された「Webhook テンプレート」ページ。]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## ステップ 2:テンプレートを選択する {#step-2-choose-your-template}

ここから、新しいテンプレートを作成するか、事前にデザインされたWebhookテンプレートを使用するか、既存のテンプレートを編集するかを選択できます。

たとえば、メッセージングチャネルとして[LINE]({{site.baseurl}}/user_guide/channels/line)を使用している場合、**LINE Carousel**や**LINE Image**の事前デザインテンプレートを使用して複数のwebhookを設定できます。

## ステップ 3:テンプレートの詳細を入力する {#step-3-fill-out-template-details}

1. Webhookテンプレートにユニークな名前を付けます。
2. （オプション）テンプレートの使用目的を説明するテンプレートの説明を追加します。
3. テンプレートの検索やフィルタリングに役立つよう、必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)や[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。

## ステップ 4:テンプレートを構築する {#step-4-build-your-template}

1. Webhook URLを入力します。
2. HTTPメソッドを選択します。
3. リクエストボディを追加します。**JSON Key/Value Pairs**または**Raw Text**のいずれかを使用できます。
4. （オプション）リクエストヘッダーを追加します。これはwebhookの送信先によって必要になる場合があります。

![Webhookテンプレート作成時の「作成」タブ。使用可能なフィールドはWebhook URL、HTTPメソッド、リクエストボディ、リクエストヘッダーです。言語を追加することもできます。]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## ステップ 5:テンプレートをテストする {#step-5-test-your-template}

ユーザーに送信する前にwebhookがどのように表示されるかを確認するには、**Test**タブを使用してテストwebhookを送信できます。ここでは、ランダムユーザー、既存ユーザー、またはカスタムユーザーとしてメッセージをプレビューすることを選択できます。

## ステップ 6:テンプレートを保存する {#step-6-save-your-template}

**Save Template**を選択してテンプレートを保存してください。これで、任意のキャンペーンでこのテンプレートを使用する準備が整いました。

{% alert note %}
既存のテンプレートに加えた編集は、そのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されません。
{% endalert %}

## テンプレートを管理する {#managing-your-templates}

Webhookテンプレートを[複製およびアーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates)して、テンプレートのリストをより適切に整理・管理できます。