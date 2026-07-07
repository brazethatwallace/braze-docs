---
nav_title: Salesforce Sales Cloud
article_title: Salesforce Sales Cloud でリードを管理する
page_order: 3
page_type: reference
description: "BrazeのWebhookを使用して、Salesforce sobjects/Leadエンドポイントを通じてSalesforce Sales Cloudでリードを作成および更新する方法を学びます。"
---

# Salesforce Sales Cloud でリードを管理する {#manage-leads-with-salesforce-sales-cloud}

> [Salesforce](https://www.salesforce.com/) は、リードジェネレーション、オポチュニティトラッキング、アカウント管理など、企業が営業プロセス全体を管理できるように設計された、世界有数のクラウドベースのCRMプラットフォームです。<br><br>このページでは、コミュニティから投稿された統合を通じて、BrazeのWebhookを使用してSalesforce Sales Cloudでリードを作成および更新する方法を紹介します。

{% alert important %}
これはコミュニティから提出された統合であり、Brazeが直接サポートするものではありません。Brazeが提供する公式のWebhookテンプレートのみがBrazeによってサポートされます。
{% endalert %}

## 仕組み {#how-it-works}

BrazeとSalesforce Sales Cloudの統合は、BrazeのWebhookを使用して、Salesforceの[sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html)エンドポイントを通じてSalesforce Sales Cloudでリードを作成および更新します。

Brazeは現在、以下のユースケース向けにSalesforce Sales Cloudとの2つの統合を提供しています。
1. [Salesforce Sales Cloudでリードを作成する](#creating-lead)
2. [Salesforce Sales Cloudでリードを更新する](#updating-lead)

{% alert note %}
この統合は、リード獲得と育成の取り組みの一環としてBrazeからSalesforceを更新することのみを目的としています。SalesforceからBrazeにデータを同期するには、[B2Bデータモデル]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models)を確認するか、[テクノロジーパートナー]({{site.baseurl}}/partners/home)にお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

この統合を進める前に、Salesforceサポートから接続アプリを作成する権限を付与してもらう必要があります。[Salesforceサポートリクエスト](https://help.salesforce.com/s/articleView?id=005167035&type=1)を送信してリクエストできます。

SalesforceサポートからSalesforce Sales Cloudで接続アプリを作成する権限が付与されたら、Salesforceのドキュメントに記載されたステップに従ってください：[Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)。

接続アプリに必要なOAuth設定を構成する際は、以下を除き、すべてのOAuth設定をデフォルトの値と選択のままにしてください。
1. **Enable for device** フローを選択します。**Callback URL** はデフォルトでプレースホルダーになるため、空白のままで構いません。
2. 選択した **OAuth Scopes** に、**Manage user data via APIs (api)** を追加します。
3. **Enable Client Credentials Flow** を選択します。

## Salesforce Sales Cloudでリードを作成する {#creating-lead}

カスタマーエンゲージメントプラットフォームとして、Brazeはランディングページのフォーム入力などのユーザーフローに基づいて新しいリードを生成できます。その場合、Braze Salesforce Sales CloudのWebhookを使って、Salesforceで対応するリードを作成できます。

### ステップ1:`client_id`と`client_secret`を収集する {#step-1-collect-your-client_id-and-client_secret}

1. Salesforceで、**Platform Tools** > **Apps** > **App Manager** に移動します。
2. 新しく作成したBrazeアプリを見つけ、**View** を選択します。
3. **Consumer Key and Secret** で、**Manage Consumer Details** を選択します。
4. 表示されたページで、**Consumer Key** と **Consumer Secret** をメモします。**Consumer Key** が`client_id`、**Consumer Secret** が`client_secret`です。

### ステップ2:Webhookテンプレートをセットアップする {#step-2-set-up-your-webhook-template}

テンプレートを使って、このWebhookをBrazeプラットフォーム全体ですばやく再利用できます。

1. Brazeで、**Templates** に移動し、**Webhook Templates** を選択してから、**+ Create Webhook Template** を選択します。
2. テンプレートの名前を指定します（「Salesforce Sales Cloud > Create Lead」など）。
3. **Compose** タブで、以下の詳細を入力します。

#### Webhookの作成 {#compose-webhook}

| フィールド | 詳細 |
| --- | --- |
| Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTPメソッド | `POST` |
| リクエスト本文 | JSONキーと値のペア |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhookの作成" }

#### 本文プロパティのキー値 {#body-property-key-values}

BrazeからSalesforceにマッピングするキーと値のペアごとに、**+ Add New Body Property** を選択します。任意のフィールドをマッピングできるため、以下の表は一例です。

| キー | 値 |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="本文プロパティのキー値" }

#### リクエストヘッダー {#request-headers}

次の各リクエストヘッダーに対して **+ Add New Header** を選択します。

| キー | 値 |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リクエストヘッダー" }

{: start="4" }
4. **Save Template** を選択します。

![リードを作成するために入力されたWebhookテンプレート。]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}

## Salesforce Sales Cloudでリードを更新する {#updating-lead}

Salesforceでリードを更新するBraze Salesforce Sales Cloud Webhookを設定するには、Salesforce Sales CloudとBrazeの間に共通の識別子が必要です。以下の例では、Salesforceの`lead_id`をBrazeの`external_id`として使用していますが、`user_alias`を使用して実現することもできます。詳細については、[B2Bデータ]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models)を参照してください。

この例では、リードが一定のリードしきい値を超えた後に、リードのリードステージを「MQL」（Marketing Qualified Lead）に更新する方法を具体的に示しています。これは、[B2Bリードスコアリングワークフロー]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring)ユースケースの核となる部分です。

### ステップ1:`client_id`と`client_secret`を収集する

1. Salesforceで、**Platform Tools** > **Apps** > **App Manager** に移動します。
2. 新しく作成したBrazeアプリを見つけ、**View** を選択します。
3. **Consumer Key and Secret** で、**Manage Consumer Details** を選択します。
4. 表示されたページで、**Consumer Key** と **Consumer Secret** をメモします。
    - **Consumer Key** が`client_id`、**Consumer Secret** が`client_secret`です。

### ステップ2:Webhookテンプレートをセットアップする

1. Brazeで、**Templates** に移動し、**Webhook Templates** を選択してから、**+ Create Webhook Template** を選択します。
2. テンプレートの名前を指定します（「Salesforce Sales Cloud > Update Lead to MQL」など）。
3. **Compose** タブで、以下の詳細を入力します。

#### Webhookの作成

| フィールド | 詳細 |
| --- | --- |
| Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTPメソッド | `PATCH` |
| リクエスト本文 | JSONキーと値のペア |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhookの作成" }

#### 本文プロパティのキー値

次のキーと値のペアに対して **+ Add New Body Property** を選択します。なお、`Lead_Stage__c`は名前の例です。SalesforceでMQLをトラッキングするために使用するカスタムフィールドの名前が異なる場合があるため、両者が一致していることを確認してください。

| キー | 値 |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="本文プロパティのキー値" }

#### リクエストヘッダー

次の各リクエストヘッダーに対して **+ Add New Header** を選択します。

| キー | 値 |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リクエストヘッダー" }

{: start="4"}
4. **Save Template** を選択します。

![リードを更新するために入力されたWebhookテンプレート。]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## 運用ワークフローでこれらのWebhookを使用する {#using-these-webhooks-in-an-operational-workflow}

テンプレートをBrazeの運用ワークフローにすばやく追加できます。例えば以下のようなケースがあります。

1. Salesforceでリードを作成する[新規リードキャンペーン](#new-lead)の一部として
2. MQLしきい値を超えたユーザーを「MQL」に更新し、同じ情報でSalesforce Sales Cloudを更新する[リードスコアリングキャンバス](#lead-scoring)の一部として

### 新規リードキャンペーン {#new-lead}

ユーザーがメールアドレスを提供したときにSalesforceでリードを作成するには、「Update Lead」Webhookテンプレートを使用するキャンペーンを作成し、ユーザーがメールアドレスを追加したとき（例えば、Webフォームに入力したとき）にトリガーします。

![アクションベースで「メールアドレスを追加する」というトリガーアクションを持つキャンペーン作成のステップ2。]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### マーケティング適格リード（MQL）しきい値を超えた場合のリードスコアリングキャンバス {#lead-scoring}

このWebhookは[リードスコアリング]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring#lead-handoff)のユースケースで取り上げていますが、リードスコアリングキャンバス内でMQLをチェックし、Salesforceを直接更新することもできます（別途Webhook キャンペーンを作成する代わりに）。

ユーザーの更新に後続ステップを追加し、ユーザーが定義したMQLしきい値を超えたかどうかをチェックします。超えた場合、そのユーザーのステータスを「MQL」に更新し、このWebhookテンプレートを使用して同じ「MQL」ステータスでSalesforceを更新します。Salesforceは、定義されたリードルーティングルールを使用して、このリードを適切な営業チームにルーティングすることで残りの処理を行います。

#### MQLしきい値を通過したユーザーをチェックするキャンバスステップを追加する {#adding-canvas-step-to-check-for-users-who-passed-the-mql-threshold}

1. 2つのグループを持つ**オーディエンスパス**ステップを追加します：「MQL Threshold」と「Everyone Else」。
2. 「MQL Threshold」グループで、現在ステータスが「MQL」ではないが（例えば、`lead_stage`が「Lead」に等しい）、定義したしきい値を超えるリードスコア（例えば、`lead_score`が50より大きい）を持っているユーザーを探します。該当する場合は次のステップに進み、該当しない場合は終了します。

![「MQL Threshold」オーディエンスパスグループ。`lead_stage`が「Lead」に等しく、`lead_score`が「50」より大きいフィルターが設定されています。]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. ユーザーの`lead_stage`属性値を「MQL」に更新する**ユーザーの更新**ステップを追加します。

![`lead_stage`属性の値を「MQL」に更新する「Update to MQL」ユーザーの更新ステップ。]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. 新しいMQLステージでSalesforceを更新するWebhookステップを追加します。

![完了した詳細を含む「Update Salesforce」Webhookステップ。]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

これで、キャンバスフローがMQLしきい値を超えたユーザーを更新するようになります。

![ユーザーがMQLしきい値を超えたかどうかをチェックし、超えた場合はSalesforceを更新するキャンバスのユーザーの更新ステップ。]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## トラブルシューティング {#troubleshooting}

これらのワークフローはSalesforce内でのデバッグ機能が限られているため、Webhookが失敗した理由やエラーが発生したかどうかを調べるには、Brazeの[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#message-activity-log)を参照することをおすすめします。

例えば、OAuthトークンの取得に使用された無効なURLによるエラーは、`https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL` と表示されます。

![URLが有効なURLではないことを示すエラー応答本文。]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})