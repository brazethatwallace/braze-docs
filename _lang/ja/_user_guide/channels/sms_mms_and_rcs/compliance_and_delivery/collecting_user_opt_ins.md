---
nav_title: "ユーザーオプトインの収集"
article_title: ユーザーSMSオプトイン収集のベストプラクティス
page_order: 3
description: "このリファレンス記事では、ユーザーオプトインを収集するための3つのベストプラクティスについて説明します。"
page_type: reference
channel:
  - SMS

---

# ユーザーオプトインの収集 {#collect-user-opt-ins}

> 以下の記事では、一般的なSMSオプトインの方法を紹介します。

## オプション1：ユーザーにショートコードまたはロングコードにテキストを送信してもらう {#option-1-ask-users-to-text-your-short-or-long-code}

ユーザーに「START」、「UNSTOP」、「YES」、またはカスタムオプトインキーワードを番号にテキスト送信してもらうことで、自動的にサブスクリプショングループに追加できます。Webサイト、モバイルアプリ、さらには広告でも、ユーザーにオプトインを依頼でき、必要に応じてインセンティブを提供することもできます。

## オプション2：アプリ内メッセージからオプトインする {#option-2-users-opt-in-via-in-app-message}

ユーザーがアプリ内メッセージからSMSにオプトインできるようにするには、Brazeが提供する[電話番号キャプチャフォーム]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture)を使用して、電話番号を収集しSMSリストを拡大するためのブランド化されたフォームを作成します。

![電話番号キャプチャ用テンプレートを使用したアプリ内メッセージ作成画面。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Brazeでは、[SMSダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)機能も併用することを推奨しています。この機能はアプリ内メッセージの電話番号キャプチャフォームと自動的に連携し、ユーザーがフォームから電話番号を送信した後に意思確認を促します。

## オプション3：サインアップフロー {#option-3-sign-up-flow}

新規ユーザーがWebサイトまたはアプリでサインアップまたは登録する際に、電話番号とメールアドレスを入力してもらいます。プロモーションメールとSMSの受信に同意するチェックボックスを含めてください。

ユーザーがサインアップした後、以下を行います。

1. [`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status#update-users-subscription-group-status)を使用して、ユーザーを作成し属性を保存します。

{% raw %}
```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```
{% endraw %}

{: start="2"}
2. [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザーをSMSに登録します。

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```
{% endraw %}

{% alert tip %}
REST APIを通じてユーザーを登録する際に[SMSダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)ワークフローに入れるには、リクエストで`use_double_opt_in_logic`パラメーターを`true`に設定します。このパラメーターを省略すると、ユーザーはダブルオプトイン確認を受け取らずに登録されます。

このパラメーターは以下のエンドポイントでサポートされています。<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
{% endalert %}