---
nav_title: Twilioパートナーシップ
alias: /partners/twilio/

description: "この記事では、BrazeとTwilioのパートナーシップについて概説します。"
page_type: update
channel:
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Twilio Webhookインテグレーションのサポートは2020年1月31日に廃止されます。Brazeで引き続きSMSサービスにアクセスしたい場合は、[SMSドキュメント]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)を参照してください。
{% endalert %}

この例では、Twilioの[メッセージ送信API](https://www.twilio.com/docs/api/rest/sending-messages)を介して、SMSとMMSをユーザーに送信するようにBraze Webhookチャネルを設定します。便宜上、ダッシュボードにはTwilio Webhookテンプレートが含まれています。

## HTTP URL

WebhookのURLは、ダッシュボードでTwilioから提供されます。このURLにはTwilioアカウントID（`TWILIO_ACCOUNT_SID`）が含まれているため、Twilioアカウントに固有のURLとなります。

Twilioの例では、Webhook URLは`https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`です。このURLは、Twilioコンソールの*Getting Started*セクションに記載されています。

![Twilioコンソール]({% image_buster /assets/img_archive/Twilio_Console.png %})

## リクエスト本文 {#request-body}

Twilio APIでは、リクエスト本文がURLエンコードされていることを想定しているため、まずBraze Webhookコンポーザーのリクエストタイプを`Raw Text`に変更する必要があります。リクエスト本文に必要なパラメーターは、*To*、*From*、*Body*です。

次のスクリーンショットは、各ユーザーの電話番号に「Hello from Braze!」という本文でSMSを送信する場合のリクエストの例です。

- ターゲットオーディエンスの各ユーザープロファイルに、有効な電話番号が必要です。
- Twilioのリクエスト形式に対応するため、メッセージコンテンツに`url_param_escape` Liquidフィルターを使用します。このフィルターは文字列をエンコードし、HTMLリクエストですべての文字が許可されるようにします。例えば、電話番号`+12125551212`のプラス文字（`+`）はURLエンコードデータでは禁止されており、`%2B12125551212`に変換されます。

![Webhook本文]({% image_buster /assets/img_archive/Webhook_Body.png %})

## リクエストヘッダーとメソッド {#request-headers-and-method}

Twilioでは、リクエストのContent-Typeと[HTTP基本認証](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side)ヘッダーの2つのリクエストヘッダーが必要です。Webhookコンポーザーの横にある歯車アイコンをクリックし、*Add New Pair*を2回クリックして、Webhookに追加します。

ヘッダー名 | ヘッダー値
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Authorization | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

`TWILIO_ACCOUNT_SID`と`TWILIO_AUTH_TOKEN`は、必ずTwilioダッシュボードの値に置き換えてください。最後に、TwilioのAPIエンドポイントはHTTP POSTリクエストを想定しているため、*HTTP Method*のドロップダウンでそのオプションを選択します。

![Webhookメソッド]({% image_buster /assets/img_archive/Webhook_Method.png %})

## リクエストのプレビュー {#preview-your-request}

Webhookコンポーザーを使って、ランダムなユーザーまたは特定の認証情報を持つユーザーのリクエストをプレビューし、リクエストが正しくレンダリングされていることを確認します。

![Webhookプレビュー]({% image_buster /assets/img_archive/Webhook_Preview.png %})