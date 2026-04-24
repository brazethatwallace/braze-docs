---
nav_title: Salesforce Sales Cloud
article_title: Salesforce Sales Cloud でリードを管理する
page_order: 3
page_type: reference
description: "Braze の Webhook を使用して、Salesforce sobjects/Lead エンドポイントを通じて Salesforce Sales Cloud でリードを作成および更新する方法を学びます。"
---

# Salesforce Sales Cloud でリードを管理する

> [Salesforce](https://www.salesforce.com/) は、リードジェネレーション、オポチュニティトラッキング、アカウント管理など、企業が営業プロセス全体を管理できるように設計された、世界有数のクラウドベースの CRM プラットフォームです。<br><br>このページでは、コミュニティから投稿された統合を通じて、Braze の Webhook を使用して Salesforce Sales Cloud でリードを作成および更新する方法を紹介します。

{% alert important %}
これはコミュニティから提出された統合であり、Braze が直接サポートするものではありません。Braze が提供する公式の Webhook テンプレートのみが Braze によってサポートされます。
{% endalert %}

## 仕組み

Braze と Salesforce Sales Cloud の統合は、Braze の Webhook を使用して、Salesforce の [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) エンドポイントを通じて Salesforce Sales Cloud でリードを作成および更新します。

Braze は現在、以下のユースケース向けに Salesforce Sales Cloud との2つの統合を提供しています。
1. [Salesforce Sales Cloud でリードを作成する](#creating-lead)
2. [Salesforce Sales Cloud でリードを更新する](#updating-lead)

{% alert note %}
この統合は、リード獲得と育成の取り組みの一環として Braze から Salesforce を更新することのみを目的としています。Salesforce から Braze にデータを同期するには、[B2B データモデル]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/)を確認するか、[テクノロジーパートナー]({{site.baseurl}}/partners/home/)にお問い合わせください。
{% endalert %}

## 前提条件

この統合では、Salesforce のドキュメントに記載されたステップに従って、Salesforce Sales Cloud で接続アプリを作成する必要があります：[OAuth 2.0 クライアント認証情報フロー用に接続アプリを設定する](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)。

接続アプリに必要な OAuth 設定を構成する際は、以下を除き、すべての OAuth 設定をデフォルトの値と選択のままにしてください。
1. **Enable for device** フローを選択します。**Callback URL** はデフォルトでプレースホルダーになるため、空白のままで構いません。
2. 選択した **OAuth Scopes** に、**Manage user data via APIs (api)** を追加します。
3. **Enable Client Credentials Flow** を選択します。

## Salesforce Sales Cloud でリードを作成する {#creating-lead}

カスタマーエンゲージメントプラットフォームとして、Braze はランディングページのフォーム入力などのユーザーフローに基づいて新しいリードを生成できます。その場合、Braze Salesforce Sales Cloud の Webhook を使って、Salesforce で対応するリードを作成できます。

### ステップ 1: `client_id` と `client_secret` を収集する

1. Salesforce で、**Platform Tools** > **Apps** > **App Manager** に移動します。
2. 新しく作成した Braze アプリを見つけ、**View** を選択します。
3. **Consumer Key and Secret** で、**Manage Consumer Details** を選択します。
4. 表示されたページで、**Consumer Key** と **Consumer Secret** をメモします。**Consumer Key** が `client_id`、**Consumer Secret** が `client_secret` です。

### ステップ 2: Webhook テンプレートをセットアップする

テンプレートを使って、この Webhook を Braze プラットフォーム全体ですばやく再利用できます。

1. Braze で、**Templates** に移動し、**Webhook Templates** を選択してから、**+ Create Webhook Template** を選択します。
2. テンプレートの名前を指定します（「Salesforce Sales Cloud > Create Lead」など）。
3. **Compose** タブで、以下の詳細を入力します。

#### Webhook の作成

| フィールド | 詳細 |
| --- | --- |
| Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP メソッド | `POST` |
| リクエスト本文 | JSON キーと値のペア |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 本文プロパティのキー値

Braze から Salesforce にマッピングするキーと値のペアごとに、**+ Add New Body Property** を選択します。任意のフィールドをマッピングできるため、以下の表は一例です。

| キー | 値 |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### リクエストヘッダー

次の各リクエストヘッダーに対して **+ Add New Header** を選択します。

| キー | 値 |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4" }
4. **Save Template** を選択します。

![リードを作成するために入力された Webhook テンプレート。]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Salesforce Sales Cloud でリードを更新する {#updating-lead}

Salesforce でリードを更新する Braze Salesforce Sales Cloud Webhook を設定するには、Salesforce Sales Cloud と Braze の間に共通の識別子が必要です。以下の例では、Salesforce の `lead_id` を Braze の `external_id` として使用していますが、`user_alias` を使用して実現することもできます。詳細については、[B2B データ]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/)を参照してください。

この例では、リードが一定のリードしきい値を超えた後に、リードのリードステージを「MQL」（Marketing Qualified Lead）に更新する方法を具体的に示しています。これは、[B2B リードスコアリングワークフロー]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/)ユースケースの核となる部分です。

### ステップ 1: `client_id` と `client_secret` を収集する

1. Salesforce で、**Platform Tools** > **Apps** > **App Manager** に移動します。
2. 新しく作成した Braze アプリを見つけ、**View** を選択します。
3. **Consumer Key and Secret** で、**Manage Consumer Details** を選択します。
4. 表示されたページで、**Consumer Key** と **Consumer Secret** をメモします。
    - **Consumer Key** が `client_id`、**Consumer Secret** が `client_secret` です。

### ステップ 2: Webhook テンプレートをセットアップする

1. Braze で、**Templates** に移動し、**Webhook Templates** を選択してから、**+ Create Webhook Template** を選択します。
2. テンプレートの名前を指定します（「Salesforce Sales Cloud > Update Lead to MQL」など）。
3. **Compose** タブで、以下の詳細を入力します。

#### Webhook の作成

| フィールド | 詳細 |
| --- | --- |
|Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP メソッド | `PATCH` |
| リクエスト本文 | JSON キーと値のペア |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 本文プロパティのキー値

次のキーと値のペアに対して **+ Add New Body Property** を選択します。なお、`Lead_Stage__c` は名前の例です。Salesforce で MQL をトラッキングするために使用するカスタムフィールドの名前が異なる場合があるため、両者が一致していることを確認してください。

| キー | 値 |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### リクエストヘッダー

次の各リクエストヘッダーに対して **+ Add New Header** を選択します。

| キー | 値 |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4. **Save Template** を選択します。

![リードを更新するために入力された Webhook テンプレート。]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## 運用ワークフローでこれらの Webhook を使用する

テンプレートを Braze の運用ワークフローにすばやく追加できます。例えば以下のようなケースがあります。

1. Salesforce でリードを作成する[新規リードキャンペーン](#new-lead)の一部として
2. MQL しきい値を超えたユーザーを「MQL」に更新し、同じ情報で Salesforce Sales Cloud を更新する[リードスコアリングキャンバス](#lead-scoring)の一部として

### 新規リードキャンペーン {#new-lead}

ユーザーがメールアドレスを提供したときに Salesforce でリードを作成するには、「Update Lead」Webhook テンプレートを使用するキャンペーンを作成し、ユーザーがメールアドレスを追加したとき（例えば、Web フォームに入力したとき）にトリガーします。

![アクションベースで「メールアドレスを追加する」というトリガーアクションを持つキャンペーン作成のステップ 2。]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### マーケティング適格リード（MQL）しきい値を超えた場合のリードスコアリングキャンバス {#lead-scoring}

この Webhook は[リードスコアリング]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring#lead-handoff)のユースケースで取り上げていますが、リードスコアリングキャンバス内で MQL をチェックし、Salesforce を直接更新することもできます（別途 Webhook キャンペーンを作成する代わりに）。

ユーザーの更新に後続ステップを追加し、ユーザーが定義した MQL しきい値を超えたかどうかをチェックします。超えた場合、そのユーザーのステータスを「MQL」に更新し、この Webhook テンプレートを使用して同じ「MQL」ステータスで Salesforce を更新します。Salesforce は、定義されたリードルーティングルールを使用して、このリードを適切な営業チームにルーティングすることで残りの処理を行います。

#### MQL しきい値を通過したユーザーをチェックするキャンバスステップを追加する

1. 2つのグループを持つ**オーディエンスパス**ステップを追加します：「MQL Threshold」と「Everyone Else」。
2. 「MQL Threshold」グループで、現在ステータスが「MQL」ではないが（例えば、`lead_stage` が「Lead」に等しい）、定義したしきい値を超えるリードスコア（例えば、`lead_score` が 50 より大きい）を持っているユーザーを探します。該当する場合は次のステップに進み、該当しない場合は終了します。

![「MQL Threshold」オーディエンスパスグループ。`lead_stage` が「Lead」に等しく、`lead_score` が「50」より大きいフィルターが設定されています。]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. ユーザーの `lead_stage` 属性値を「MQL」に更新する**ユーザーの更新**ステップを追加します。

![`lead_stage` 属性の値を「MQL」に更新する「Update to MQL」ユーザーの更新ステップ。]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. 新しい MQL ステージで Salesforce を更新する Webhook ステップを追加します。

![完了した詳細を含む「Update Salesforce」Webhook ステップ。]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

これで、キャンバスフローが MQL しきい値を超えたユーザーを更新するようになります。

![ユーザーが MQL しきい値を超えたかどうかをチェックし、超えた場合は Salesforce を更新するキャンバスのユーザーの更新ステップ。]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## トラブルシューティング

これらのワークフローは Salesforce 内でのデバッグ機能が限られているため、Webhook が失敗した理由やエラーが発生したかどうかを調べるには、Braze の[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#message-activity-log)を参照することをおすすめします。

例えば、OAuth トークンの取得に使用された無効な URL によるエラーは、`https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL` と表示されます。

![URL が有効な URL ではないことを示すエラー応答本文。]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})