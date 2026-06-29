---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "このリファレンス記事では、BrazeとDOTS.ECOの統合について説明します。"
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco)は、追跡可能なデジタル証明書を通じて、ユーザーに実際の環境インパクトを報酬として提供できるサービスです。各証明書には、共有可能な証明書URLや画像URLなどのメタデータを含めることができるため、ユーザーはインパクトの証明を閲覧（および再確認）することができます。

_この統合はDOTS.ECOによって管理されています。_

## この統合について {#about-this-integration}

BrazeとDOTS.ECOは、カスタマーエンゲージメントジャーニーを現実世界のインパクト報酬につなげます。BrazeのCanvasまたはCampaignステップから、コネクテッドコンテンツを使用してDOTS.ECO証明書作成リクエストをトリガーできます。DOTS.ECOは証明書メタデータ（`certificate_url`や`certificate_image_url`など）を返し、これをユーザープロファイルにカスタム属性として保存して、アプリ内メッセージ、Content Cards、プッシュ通知などのチャネルで再利用できます。

## ユースケース {#use-cases}

- ユーザーがキーイベント（購入、レベル完了、サブスクリプション、紹介）を完了したときにインパクト証明書をトリガーする。
- コネクテッドコンテンツのステップが成功した後、アプリ内メッセージでパーソナライズされた証明書画像を表示する。
- 証明書URLを記載した「証明書を見る」Content Cardsを追加し、後からアクセスできるようにする。
- 証明書メタデータ（`certificate_url`、`certificate_image_url`、`certificate_header`、`greeting`など）をカスタム属性として保存し、将来のメッセージングで再利用できるようにする。
- リモートユーザーIDを使用して証明書を割り当てることで、ユーザーが後からインパクトを請求・確認できるようにする。
- 同じDOTS.ECOユーザー更新フローを維持しながら、インパクトメッセージング（異なるコピー/画像）のA/Bテストを実施する。


## 前提条件 {#prerequisites}

始める前に、以下が必要です。

| 要件 | 説明 |
|---|---|
| DOTS.ECOアカウント | DOTS.ECOアカウントへのアクセス。 |
| DOTS.ECO認証情報 | この記事のリクエストには、DOTS.ECOアプリトークン、APIキー、アロケーションIDが必要です。これらを取得するには、DOTS.ECOのカスタマーサクセスマネージャーにお問い合わせください。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。このキーはBrazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## DOTS.ECOの統合 {#integrating-dotseco}

### ステップ1：Canvasを作成し、ユーザー更新ステップを追加する {#step-1-create-a-canvas-and-add-a-user-update-step}

Brazeダッシュボードで、ユーザーがキーイベント（購入、サブスクリプション、マイルストーンなど）を完了したときにトリガーする新しいCanvasを作成します。

エントリステップの直後にユーザー更新ステップを追加します。このステップは、コネクテッドコンテンツ経由でDOTS.ECO APIを呼び出し、返された証明書データをユーザープロファイルに保存するために使用します。

このステップを使用して、コネクテッドコンテンツ経由でDOTS.ECO APIを呼び出し、返された証明書データをユーザープロファイルに保存します。

### ステップ2：高度なJSONを作成する：コネクテッドコンテンツを使ってDOTS.ECOにPOSTリクエストを行う {#step-2-compose-advanced-json-make-a-post-request-to-dotseco-using-connected-content}

**ユーザーの更新**ステップで、**Advanced JSON Editor**に切り替え、コネクテッドコンテンツを使用してDOTS.ECO証明書APIにPOSTリクエストを行います。

`capture`タグとコネクテッドコンテンツリクエストを使用して、DOTS.ECOの証明書エンドポイントを呼び出します。次に、レスポンスをカスタム属性としてユーザープロファイルに保存します。

**コネクテッドコンテンツとユーザー更新の例**
{% raw %}
```
{% capture post_body %}
{
  "remote_user_email": "{{${email_address} | default: 'braze+user@example.com'}}",
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",
  "impact_qty": 1,
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"
}
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk
  :method post
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }
  :body {{post_body}}
  :content_type application/json
  :save result
%}

{
  "attributes": [
    {
      "certificate_image_url": "{{result.certificate_image_url}}",
      "certificate_url": "{{result.certificate_url}}",
      "certificate_id": "{{result.certificate_id}}"
    }
  ]
}
```
{% endraw %}

`https://impact.dots.eco/api/v1/certificate/add?format=sdk`にリクエストを送信します。

![DOTS.ECOユーザー更新ステップ。]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}
この統合では、Canvasの**ユーザーの更新**ステップ内でコネクテッドコンテンツを使用してDOTS.ECO APIを呼び出します。トークンとペイロードを検証するために、まずAPIクライアント（例：Postman）でリクエストをテストしてください。
{% endalert %}

### ステップ3：メッセージに証明書を表示する {#step-3-display-the-certificate-in-messages}

証明書の属性がユーザープロファイルに保存されると、下流のCanvasメッセージステップで参照できるようになります。

![DOTS.ECOフロー。]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECOメッセージステップ。]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECOメッセージ作成セクション。]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

以下に例を示します。
- {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}を使用して、アプリ内メッセージに証明書画像を表示する
- {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}を使用して、ホストされた証明書にリンクする

![DOTS.ECOメッセージのクリック時の動作。]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


これにより、アプリ内メッセージ、Content Cards、またはプッシュ通知をインパクト確認でパーソナライズできます。

## トラブルシューティング {#troubleshooting}

Brazeダッシュボードの**設定** > **メッセージアクティビティログ**でコネクテッドコンテンツのエラーを確認してください。

- **コネクテッドコンテンツが空を返す**：`:save result`が設定されていること、および期待されるレスポンスフィールドを参照していることを確認してください。
- **属性がメッセージステップに表示されない**：
  - Brazeのカスタム属性名が、ユーザー更新ステップで設定した属性と完全に一致していることを確認してください。
  - ユーザー更新ステップで、**プレビューとテスト**タブを使用して属性が入力されていることを確認してください。次に、ユーザーにテストを送信し、ユーザープロファイルに属性が保存されていることを確認してください。
- **`422`エラー（処理不能なエンティティ）**：アプリトークンとインパクト数量が有効であることを確認してください。
- **`401`エラー**：認証トークンが存在し、正しいことを確認してください。
- **メッセージステップに画像プレビューがない**：ユーザー更新ステップで**ユーザーにテスト送信**を選択し、同じユーザーを使用してメッセージをプレビューしてください。