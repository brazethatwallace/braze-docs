---
nav_title: HTMLメールテンプレートのアップロード
article_title: HTMLメールテンプレートのアップロード
page_order: 2
description: "このリファレンス記事では、Brazeダッシュボードを使用してHTMLメールテンプレートを作成、管理、トラブルシューティングする方法について説明します。"
tool:
  - Templates
channel:
  - email

---

# HTMLメールテンプレートのアップロード {#upload-an-html-email-template}

> Brazeダッシュボードでは、独自のHTMLメールテンプレートをアップロードして保存し、後からCampaignsで使用できます。また、エディターを使用して[メールテンプレートを作成]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template/)することもできます。

## 要件 {#upload-requirements}

まず、HTMLメールテンプレートを作成する必要があります。これは以下を含むZIPファイルである必要があります。

* 単一のHTMLファイル — メールの本文
* HTMLファイルで参照されている画像のフォルダー
* 画像ファイルは50個未満
* 5&nbsp;MB未満

## テンプレートのアップロード {#uploading-your-template}

### ステップ 1: メールテンプレートエディターに移動する {#step-1-go-to-the-email-template-editor}

**Content** > **Email**に移動します。**Create email template**を選択します。

### ステップ 2: テンプレートの詳細を追加する {#step-2-add-template-details}

テンプレート名を入力します。必要に応じて、説明、チーム、タグを追加します。

### ステップ 3: テンプレートをアップロードする {#step-3-upload-your-template}

**Template content**セクションで、**HTML code editor**タイルの下にある**Upload file**を選択します。コンピューターからテンプレートを選択します。テンプレートがアップロード要件を満たしていることを確認するには、[要件](#upload-requirements)セクションを参照してください。

### ステップ 4: テンプレートを完成させて保存する {#step-4-finish-and-save-your-template}

**Save template**を選択してテンプレートを保存してください。これで、任意のCampaignまたはCanvasでこのテンプレートを使用する準備が整いました。

{% alert note %}
既存のテンプレートに編集を加えた場合、その変更は以前のバージョンのテンプレートを使用して作成されたCampaignsには反映されません。
{% endalert %}

## APIキャンペーンでテンプレートを使用する {#api_for_upload_email_templates}

APIキャンペーンでメールを使用するには、`email_template_id`が必要です。これはBrazeで作成されたメールテンプレートの下部に記載されています。

![HTMLメールテンプレートのAPI識別子セクション。]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## メールテンプレートの管理 {#managing-email-templates}

メールテンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)したり[アーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)したりできます。テンプレートとクリエイティブコンテンツの作成と管理の詳細については、[テンプレート]({{site.baseurl}}/user_guide/messaging/templates/)を参照してください。

## トラブルシューティング {#troubleshooting}

HTMLテンプレートファイルをアップロードする際に、いくつかのメールエラーメッセージが表示される場合があります。エラーが発生した場合は、以下の表で一般的な問題とその推奨される修正方法を参照してください。

| エラー | 修正方法 |
|------|---|
| `.zip over 5&nbsp;MB` | ファイルサイズを縮小して、再度アップロードしてください。|
| `.zip corrupt` | ファイルを確認して、再度アップロードしてください。|
| `Missing HTML` | ZIPファイルにHTMLファイルを追加して、再度アップロードしてください。|
| `Multiple HTML` | HTMLファイルを1つ削除して、再度アップロードしてください。|
| `Images over 5&nbsp;MB` | 画像の数を減らして、再度アップロードしてください。|
| `Extra Images` | HTMLファイルで参照されていない追加の画像がファイルに含まれている可能性があります。これはエラーの原因にはなりませんが、余分な画像は破棄されます。それらの画像がHTMLファイルで参照されるべきものであった場合は、コンテンツを確認し、エラーを修正して、再度アップロードしてください。|
| `Missing Images` | HTMLファイルで参照されている画像がZIPファイルの画像フォルダーに含まれていない場合、ファイルエラーが発生します。ファイルを確認してエラー（スペルミスなど）を修正するか、不足している画像をZIPファイルに追加して、再度アップロードしてください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

Windowsマシンでメールメッセージを含むHTMLキャンペーン、キャンバスステップ、またはテンプレートのファイルをダウンロードする場合、`|`（パイプ文字）はサポートされていないため、ZIPファイルからダウンロード内容を抽出するには別のアプリケーションを使用する必要がある場合があります。

## よくある質問 {#frequently-asked-questions}

メールテンプレートに関するよくある質問への回答については、[メールとリンクテンプレートのFAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq/)ページをご覧ください。