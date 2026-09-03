---
nav_title: "メールオブジェクト"
article_title: メールメッセージングオブジェクト
page_order: 5
page_type: reference
channel: email
description: "このリファレンス記事では、Brazeメールオブジェクトのさまざまなコンポーネントについて説明します。"

---

# メールオブジェクト {#email-object}

> `email` オブジェクトを使用すると、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を通じてメールを変更または作成できます。

## メールオブジェクト

```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address gets added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) recommended length 50-100 characters,
  "email_template_id": (optional, string) if provided, Braze uses the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case Braze overrides the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this is passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name", "url", and optionally "basic_auth_credential",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
    "basic_auth_credential": (optional, string) the name of the stored basic authentication credential to use when the attachment URL requires a login,
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types)
  - ワークスペースに設定されたアプリの有効な `app_id` であれば、そのユーザーのプロファイルにそのアプリがあるかどうかに関係なく、ワークスペース内のすべてのユーザーに対して機能します。
- プリヘッダーの詳細とベストプラクティスについては、[メールのスタイリング]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling)を参照してください。

{% alert warning %}
Brazeでは、添付ファイルの `url` にGoogle ドライブのリンクを使用しないことを推奨しています。サーバーがファイルを取得するための呼び出しがブロックされ、メールメッセージが送信されない場合があるためです。
{% endalert %}

有効な添付ファイルの種類は次のとおりです: `txt`、`csv`、`log`、`css`、`ics`、`jpg`、`jpe`、`jpeg`、`gif`、`png`、`bmp`、`psd`、`tif`、`tiff`、`svg`、`indd`、`ai`、`eps`、`doc`、`docx`、`rtf`、`odt`、`ott`、`pdf`、`pub`、`pages`、`mobi`、`epub`、`mp3`、`m4a`、`m4v`、`wma`、`ogg`、`flac`、`wav`、`aif`、`aifc`、`aiff`、`mp4`、`mov`、`avi`、`mkv`、`mpeg`、`mpg`、`wmv`、`xls`、`xlsx`、`ods`、`numbers`、`odp`、`ppt`、`pptx`、`pps`、`key`、`zip`、`vcf`、`pkpass`。

`email_template_id` は、HTMLエディターで作成したメールテンプレートの下部から取得できます。以下は、このIDがどのように表示されるかの例です。

![HTMLメールテンプレートのAPI識別子セクション。]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"}

## 添付ファイル付きメールオブジェクトの例 {#example-email-object-with-attachment}

```json
{
  "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
  "messages":{
     "email":{
        "app_id":"YOUR_APP_ID",
        "attachments":[{
            "file_name":"YourFileName",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

## メール添付ファイルの認証 {#authentication-for-email-file-attachments}

添付ファイルのURLにログインが必要な場合は、保存済みのBasic認証の認証情報を使用します。これは、[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)のメールオブジェクト内の添付ファイル、および[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)のトップレベルの`attachments`配列に適用されます。

1. **設定** > **Connected Content** に移動します。
2. **認証情報を追加**を選択します。
3. **Basic認証**を選択します。
4. 認証情報名、ユーザー名、パスワードを入力します。
5. 認証が必要な各添付ファイルに`basic_auth_credential`プロパティを含め、その認証情報名に設定します。次の例では、メールオブジェクト内で認証情報名`company_basic_auth_credential_name`を使用しています。

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basic auth attachment test",
      "from": "mail <mail@example.com>",
      "body": "my attachment test",
      "attachments":[
        { "file_name":"checkout_receipt.pdf",
        "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
        "basic_auth_credential": "company_basic_auth_credential_name" }
      ]
    }
  }
}
```

## 添付ファイルの取得、キャッシュ、パフォーマンス {#attachment-retrieval-caching-and-performance}

Brazeが添付ファイルの`url`からファイルを取得する際の注意事項:

- **キャッシュ:** Brazeは最近取得したファイルを約24時間再利用する場合があります。送信のたびに最新バージョンのファイルを確実に取得する必要がある場合は、バージョンごとに異なるURLを使用してください（例: ファイルの変更に応じてパスやクエリを変更するなど）。
- **タイムアウト:** ホストは迅速に応答する必要があります。添付ファイルのURLの応答が遅い場合やハングした場合、メッセージの送信が失敗する可能性があります。約2分以内の応答を目指してください。
- **セキュリティ:** 添付ファイルのURL（クエリ文字列を含む）に個人を特定できる情報（PII）や機密情報を含めないでください。URLはログや下流のシステムに表示される可能性があります。
- **ファイアウォール:** URLが特定のネットワークからのみアクセス可能な場合は、[Connected Content IP許可リスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting)に従ってBrazeからのトラフィックを許可してください。ファイルにログインが必要な場合は、[ベーシック認証の認証情報](#authentication-for-email-file-attachments)を使用してください。