---
nav_title: リードスコアリング
article_title: リードスコアリングワークフローの作成
page_order: 1
page_type: reference
description: "Brazeを使用してシンプルなリードスコアリング、外部リードスコアリング、リードの引き継ぎを実行する方法について説明します。"
---

# リードスコアリングワークフローの作成 {#create-a-lead-scoring-workflow}

> このユースケースでは、Brazeを使用してユーザーのリードスコアをリアルタイムで更新し、自動的にリードを営業チームに引き継ぐ方法を示します。

Brazeでリードスコアリングワークフローを作成するには、次の2つの重要なステップがあります。

1. Brazeでリードスコアリングキャンバスを作成するか、外部リードスコアリングツールと連携します。
- [シンプルなリードスコアリング](#simple-lead-scoring)
- [外部リードスコアリング](#external-lead-scoring)

2. 適格なリードを営業チームに送信するWebhookキャンペーンを作成します。
- [リードの引き継ぎ: マーケティング適格リード（MQL）を営業へ](#lead-handoff)

## シンプルなリードスコアリング {#simple-lead-scoring}

### ステップ1: キャンバスを作成する {#step-1-create-a-canvas}

1. **メッセージング** > **キャンバス**に移動し、**キャンバスを作成**を選択してから、キャンバスの基本情報を入力します。

2. キャンバスに「Lead Scoring キャンバス」などの関連する名前を付け、探しやすくするために「Lead Management」などのタグを付けます。<br><br>![「Lead Scoring キャンバス」という名前と「Lead Management」というタグでキャンバスを作成するステップ1。]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### ステップ2: エントリ基準を設定する {#step-2-set-up-your-entry-criteria}

1. **エントリスケジュール**ステップに進み、**アクションベース**のエントリスケジュールを選択します。これにより、ユーザーが特定のアクションを実行したときにキャンバスに入ります。

2. **アクションベースのオプション**で、次の2つのアクションを追加します。
    - **カスタム属性値の変更**: リードスコアリング属性の名前（`lead score` など）を指定します。リードスコアリング属性をまだ作成していない場合は、[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)のステップに従ってください。これにより、ユーザーのリードスコアが変化するたびにキャンバスに入ります。
    - **メールアドレスの追加**

![「アクションベース」のエントリスケジュールで、カスタム属性「lead score」の変更とメールアドレスの追加をアクションベースのオプションとしてキャンバスを作成するステップ2。]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### ステップ3: ターゲットオーディエンスを特定する {#step-3-identify-your-target-audience}

#### ステップ3a: セグメントを選択する {#step-3a-select-segments}

すべてのユーザーがリードスコアリングの対象であるため、どのユーザー[セグメント]({{site.baseurl}}/user_guide/audience/segments)をターゲットにするかを選択し、追加の[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を適用することで、スコアリング対象に関する会社固有のルールを追加できます。たとえば、従業員、すでに顧客であるユーザーなどを除外できます。

![セグメントとフィルターを選択してエントリオーディエンスを絞り込むオプションがあるキャンバスの作成ステップ3。]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### ステップ3b: キャンバスの再適格性を設定する {#step-3b-set-canvas-re-eligibility}

ユーザーはライフサイクル全体を通じてこのキャンバスを何度も通過するため、前回終了した後すぐに再エントリできるようにしてください。これは再適格性の設定で実現できます。

**エントリコントロール**で、以下を実行します。
- **ユーザーがこのキャンバスに再エントリできるようにする**を選択します。
- **指定時間枠**を選択します。
- 再適格性を「0」**秒**に設定します。

![「ユーザーがこのキャンバスに再エントリできるようにする」が選択され、「指定時間枠」が0秒に設定された「エントリコントロール」セクション。]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### ステップ3c: 送信設定を更新する {#step-3c-update-send-settings}

このキャンバスは運用目的であり、ユーザーにメッセージが送信されないため、購読ステータスに従う必要はありません。

**購読設定**の**これらのユーザーに送信:**で、**購読解除ユーザーを含むすべてのユーザー**を選択します。

![メッセージ送信オプションを設定するキャンバスの作成ステップ4。]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### ステップ4: キャンバスを構築する {#step-4-build-your-canvas}

#### ステップ4a: アクションパスを追加する {#step-4a-add-an-action-path}

バリアントの下で<i class="fas fa-plus" aria-label="追加"></i> **追加**を選択し、**アクションパス**を選択します。

![プラスアイコンで開いたメニューに「アクションパス」が表示されているキャンバス。]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### ステップ4b: アクショングループを作成する {#step-4b-create-action-groups}

各アクショングループは、同じポイントの増減につながるすべてのアクションを表します。最大8つのアクショングループを設定できます。このシナリオでは、4つのグループを設定します。

アクションパスに次のグループを追加します。

- **グループ1:** 1ポイント増加としてカウントされるすべてのイベント。
- **グループ2:** 5ポイント増加としてカウントされるすべてのイベント。
- **グループ3:** 1ポイント減少としてカウントされるすべてのイベント。
- **その他のユーザー:** アクションパスでは、ユーザーがアクションを実行するかどうかを確認するための待機時間枠を定義してから、「その他のユーザー」グループに振り分けることができます。リードスコアリングの場合、これは「非アクティブ」に対してスコアを減少させる機会です。

![1ポイント、5ポイント、10ポイントの加算、1ポイントと10ポイントの減算、および「その他のユーザー」を含むアクショングループのアクションパス。]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### ステップ4c: 各グループに関連するイベントを含めるように設定する {#step-4c-configure-each-group-to-include-the-relevant-events}

各アクショングループで、**トリガーを選択**を選択し、そのアクショングループのポイント数を加算するイベントを選択します。さらにトリガーを追加して、リードスコアを1つ増加させるすべてのイベントを含めます。たとえば、ユーザーが任意のアプリでセッションを開始したり、カスタムイベント（ウェビナーの登録や参加など）を実行したりすると、スコアが1つ増加します。

![「任意のアプリでセッションを開始」と「カスタムイベントを実行」のトリガーで1ポイント加算するアクショングループ。]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### ステップ4d: ユーザー更新ステップを追加する {#step-4d-add-user-update-steps}

アクションパスで作成された各キャンバスパスに、ユーザー更新ステップを追加します。

![アクションパスと、各アクショングループに分岐したユーザー更新パスが表示されたキャンバス。]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
各ユーザー更新ステップの**作成**タブで、対応するフィールドに対して次の操作を行います。

| フィールド | アクション |
| --- | --- |
| **属性名** | ステップ2で選択したリードスコア属性（`lead score`）を選択します。|
| **アクション** | パスがスコアを上げる場合は**Increment By**に、パスがスコアを下げる場合は**Decrement By**にアクションを変更します。|
| **Increment By**または**Decrement By** | リードスコアから増減するポイント数を入力します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4d: Add User Update steps" }

### ステップ5: キャンバスを起動する {#step-5-launch-your-canvas}

以上です！リードスコアリングキャンバスを起動する準備ができました。

## 外部リードスコアリング {#external-lead-scoring}

当社の[テクノロジーパートナー]({{site.baseurl}}/partners/home)の1社を使用する場合でも、独自の内部リードスコアリングモデル、機械学習、または別のリードスコアリングツールを使用する場合でも、複数の選択肢を用意しています。

### 外部パートナー {#external-partners}

リードスコアリング機能を提供するB2Bパートナーについては、[テクノロジーパートナー]({{site.baseurl}}/partners/home)をご覧ください。お使いのツールが見つからない場合は、[`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) APIエンドポイントを呼び出すことで連携できます。

### 内部リードスコアリングデータモデル {#internal-lead-scoring-data-models}

Brazeは、リードスコアリングモデルを含む内部データモデルとさまざまな方法で連携できます。お客様がBrazeと連携している一般的な例については、以下のセクションをご覧ください。

#### 統合クラウドデータウェアハウス {#integrated-cloud-data-warehouse}

{% tabs %}
{% tab Brazeをデータソースとして使用 %}

マーケティングツールとして、Brazeにはチームの内部リードスコアモデルを補完できる非常に関連性の高いデータが含まれています。

たとえば、メッセージングエンゲージメントデータ（メールの開封やクリック、ランディングページのエンゲージメントなど）でリードのエンゲージメントレベルを判定できます。このデータをクラウドデータウェアハウスに渡し、Brazeのストリーミングエクスポートデータソリューションを使用してリードスコアリングモデルの入力として利用できるようにすることができます。

- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)
- [Snowflakeセキュアデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

{% endtab %}
{% tab Brazeを送信先として使用 %}

内部チームがリードスコアリングモデルを作成して実行したら、そのデータをBrazeに取り込み、関連するメッセージングのためにリードをより適切にセグメント化してターゲティングできます。これは[Brazeクラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)で実行できます。

クラウドデータ取り込みでは、内部チームがユーザー識別子、最新のリードスコア、およびスコアが更新されたタイムスタンプを含む新しいテーブルまたはビューを作成します。Brazeがそのテーブルまたはビューを取得し、リードスコアをユーザープロファイルに追加します。

{% endtab %}
{% endtabs %}

## リードの引き継ぎ: マーケティング適格リード（MQL）を営業へ {#lead-handoff}

リードの引き継ぎの推奨アプローチは、Brazeの各ユーザーに対応するリードまたは連絡先を紐付けることです。これらのリードは、リードステータスがMQLステージに変更されたときに営業チームのキューに入り、その時点でSalesforceがリードのルーティングまたは割り当てワークフローを開始します。

BrazeのリードステータスでSalesforceのリードレコードを更新するには、トリガー型のWebhookテンプレートを使用することをお勧めします。

### ステップ1: Webhookキャンペーンを作成する {#step-1-create-a-webhook-campaign}

### ステップ2: Webhookを設定する {#step-2-configure-your-webhook}

#### ステップ2a: Webhookを作成する {#step-2a-compose-webhook}

1. Webhookキャンペーンに「Salesforce > Update lead to MQL」などの名前を付けます。

2. Webhook URLを{% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}の形式で入力します。{% raw %}`{{${user_id}}}`{% endraw %}のBrazeユーザーIDは、Salesforceの連絡先IDと一致する必要があります。一致しない場合は、{% raw %}`{{${user_id}}}`{% endraw %}の代わりにエイリアスを使用してください。

3. **HTTP Method**を**PATCH**に更新します。

4. リードのリードスコアが事前定義されたしきい値を超えた場合にのみSalesforceのリードレコードを更新するようにペイロードを設定します。リードスコアが100を超える場合のリクエストボディの例を以下に示します。

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. 次のヘッダーを含めます。

| ヘッダー | コンテンツ |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>トークンを取得するには、OAuth 2.0クライアント認証情報フローの[接続アプリを設定](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)してから、Connected Contentを使用してSalesforceからベアラートークンを取得します。<br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content-Type | application/json |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2a: Compose webhook" }

![SalesforceのWebhook URL、PATCH HTTPメソッド、生テキストのリクエストボディ、およびリクエストヘッダーを含む作成中のWebhook。]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### ステップ2b: Webhookの送信をスケジュールする {#step-2b-schedule-webhook-sends}

このキャンペーンは、ユーザーのリードスコアが変更されるたびにトリガーされる必要があります。このキャンペーンはスコアが変化したすべてのユーザーに対してトリガーされますが、現在MQLではなく、前のステップで設定したしきい値を超えたユーザーにのみ影響します。

**配信をスケジュール**ステップで、以下を選択します。
- **アクションベース**の配信タイプ
- **カスタム属性値の変更**のトリガーアクション: リードスコアリング属性の名前を指定し、アクションは**任意の新しい値**を選択します。

#### ステップ2c: ターゲットオーディエンスを特定する {#step-2c-identify-target-audience}

**ターゲットオーディエンス**ステップで、リードステータスがすでにMQL以上のユーザーを除外するフィルターを含めます（例: 「`lead_status` `is none of` `MQL`」）。

![「lead_status」が「MQL」のいずれでもないフィルターを持つWebhookターゲティングオプション。]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### ステップ3: キャンペーンを起動する {#step-3-launch-campaign}

**起動**を選択し、顧客がMQLリードスコアのしきい値を超えたときにSalesforceでリードステータスが変化するのを確認しましょう。