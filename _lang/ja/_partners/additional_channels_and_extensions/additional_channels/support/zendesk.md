---
nav_title: Zendesk
article_title: Zendesk
description: "このリファレンス記事では、BrazeとZendeskのパートナーシップについて説明します。Zendeskは人気の高いサポートスイートであり、2つのプラットフォーム間でサポートデータを同期できるBraze Webhookを利用できます。"
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/)（ZSS）は、メール、ウェブチャット、音声、ソーシャルメッセージングアプリを使ったオムニチャネルサポートを通じて、顧客との自然な会話を可能にします。Zendeskは対応の追跡と優先順位付けを重視する効率的なチケット発行システムを提供し、企業が顧客の履歴を一元的に把握できるようにしています。

BrazeとZendeskのサーバー間統合により、以下を利用できます。
- BrazeのWebhookを使用して、Brazeのユーザージャーニーでのメッセージエンゲージメントに基づくZendeskでのサポートチケット作成を自動化します。例えば、統合の実装とテストに成功した後、Brazeは「Enjoying our App?」というアプリ内メッセージに否定的な回答をしたユーザーからサポートチケットを作成し、サポートチームが顧客をフォローアップできるようにします。
- Zendeskでのアクティビティに基づくBrazeでのユーザープロファイルの更新など、双方向ユースケースをサポートするためのZendesk Webhook。例えば、チケットが解決した後、Brazeのユーザープロファイルにイベントを記録します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Zendeskアカウント | このパートナーシップを活用するには、[Zendesk管理者アカウント](https://`<your-zendesk-instance>`.zendesk.com/agent/admin)が必要です。 |
| Zendesk APIトークン | BrazeからZendeskチケットエンドポイントにリクエストを送信するには、Zendesk [APIトークン](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\)が必要です。 |
| 共通識別子（推奨） | BrazeとZendesk間で[共通の識別子](#common-identifier)を使用することを推奨します。 |
| Braze APIキー | ZendeskからBrazeエンドポイントにリクエストを送信するには、Braze APIキーが必要です。使用するAPIキーが、Zendesk Webhookが使用するBrazeエンドポイントに対して正しい権限を持っていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## BrazeからZendeskへの統合 {#braze-to-zendesk-integration}

### ステップ1:BrazeのWebhookを作成する {#step-1-create-your-braze-webhook}

Webhookを作成するには：

- **キャンペーン：** Brazeダッシュボードの**キャンペーン**ページに移動します。**キャンペーンを作成**をクリックし、**Webhook**を選択します。
- **キャンバス：** 新しいキャンバスまたは既存のキャンバスから、キャンバスビルダーでフルステップまたはメッセージステップを作成します。次に、**Messages**をクリックし、メッセージオプションから**Webhook**を選択します。

Webhookに以下のフィールドを記入します：
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **リクエスト本文**：Raw Text

その他のユースケースは、[Zendesk support API](https://developer.zendesk.com/rest_api/docs/support/introduction)を使用して対処できます。これにより、Webhook URLの末尾の `/api/v2/` エンドポイントが適宜変更されます。

#### リクエストヘッダーとメソッド {#request-header-and-method}

Zendeskは認証のためのHTTPヘッダーとHTTPメソッドを要求します。**Settings**タブで、<email_address>をZendesk管理者のメールに、<api_token>をZendesk APIトークンに置き換えます。

- **HTTPメソッド**：POST
- **リクエストヘッダー**：
  - **Authorization**：Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### リクエスト本文 {#request-body}

Webhookペイロードで、タイプ、サブジェクト、ステータスなどのチケットの詳細を定義します。チケットの詳細は拡張可能であり、[Zendesk ticket API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket)に基づいてカスタマイズされます。以下の例を参考に、ペイロードを構成し、希望するフィールドを入力してください。

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}",
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### ステップ2:リクエストをプレビューする {#step-2-preview-your-request}

テキストがBrazeタグであれば、自動的にハイライトされます。

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザーか既存のユーザーを選択するか、Webhookをテストするために自分でカスタマイズします。

最後に、Zendesk側でチケットが作成されているかどうかを確認します。

## 共通識別子 {#common-identifier}

BrazeとZendeskの間に共通の識別子がある場合は、それを `requester_id` として使用することをお勧めします。これにより、2つのユーザーセットを統一できます。それ以外の場合は、名前、メールアドレス、電話番号などの一連の識別属性を渡すことをお勧めします。

## ZendeskからBrazeへの統合 {#zendesk-to-braze-integration}

### ステップ1:Webhookを作成する {#step-1-create-a-webhook}

1. [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)で、サイドバーにある**Apps and integrations**をクリックし、**Webhooks > Webhooks**を選択します。<br><br>
2. **Create webhook**をクリックします。<br><br>
3. **Trigger**または**Automation**を選択し、**Next**をクリックします。<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Webhookに以下の情報を指定します。
- Webhookの名前と説明を入力します。
- Webhookが使用するBrazeエンドポイントURLを入力します。{% raw %}この例では `https://{{instance_url}}/users/track` を使用します。{% endraw %}
- Webhookのリクエストメソッドとして POST を選択し、リクエストフォーマットを JSON に設定します。
- Webhookにベアラートークン認証方式を選択し、[Braze APIキー]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys)を入力します。
  - 使用するAPIキーに、Webhookが使用するBrazeエンドポイントに対して[正しい権限]({{site.baseurl}}/api/basics/#rest-api-key-permissions)があることを確認してください。<br><br>
5. （推奨）Webhookをテストし、正しく動作していることを確認します。<br><br>
6. トリガーとオートメーションのWebhookについては、セットアップを終了する前に、Webhookをトリガーまたはオートメーションに接続する必要があります。Webhookのトリガーを作成する例については、次のステップを参照してください。トリガーが作成されたら、このページに戻り、**Finish setup**を選択します。

### ステップ2:トリガーまたはオートメーションを作成する {#step-2-create-a-trigger-or-automation}

[Zendeskの指示に従って](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb)、Webhookをトリガーまたはオートメーションに接続します。

以下の例では、サポートケースのステータスが「Solved」（解決済み）または「Closed」（クローズ済み）に変更されたときにWebhookを呼び出すトリガーを使用しています。

1. **Admin Center**で、サイドバーにある**Objects and rules**をクリックし、**Business rules > Triggers**を選択します。<br><br>
2. **Add trigger**を選択します。<br><br>
3. トリガーに名前を付け、カテゴリーを選択します。<br><br>
4. **Add condition**を選択して、Webhookをトリガーする条件を設定します。例えば、「Status category changed to closed」や「Status category changed to solved」などです。![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. **Add action**を選択し、**Notify active webhook**を選択し、前のステップで作成したWebhookをドロップダウンから選択します。<br><br>
6. Brazeのエンドポイントに適合するようにJSON本文を定義し、Zendeskの変数プレースホルダーを使用して、関連するフィールドに動的に入力します。<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. **Create**を選択します。<br><br>
8. Webhookに戻り、**Finish setup**をクリックします。