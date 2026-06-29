---
nav_title: OneTrust
article_title: OneTrust
description: "このリファレンス記事では、Braze と OneTrust のパートナーシップについて説明します。OneTrust は、データプライバシーおよびセキュリティソフトウェアのプロバイダーであり、OneTrust ワークフロービルダーを使用して自社製品のセキュリティワークフローを作成できます。"
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) は、プライバシーおよびセキュリティソフトウェアのプロバイダーであり、信頼の状況をより詳しく理解するために必要な可視化機能、強力なインサイトを活用するためのアクション、そして競争で常に優位に立つためのオートメーションを提供します。

_この統合は OneTrust によって管理されています。_

## 統合について {#about-the-integration}

Braze と OneTrust の統合により、OneTrust ワークフロービルダーを使用してプロダクトのセキュリティワークフローを作成できます。
## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| OneTrust アカウント | このパートナーシップを活用するには、[OneTrust](https://www.onetrust.com/) アカウントが必要です。 |
| Braze APIキー | OneTrust アクションが使用するエンドポイントに必要な権限を持つ Braze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | Brazeインスタンスは Braze オンボーディングマネージャーから入手できます。また、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)でも確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

次の統合では、ユーザー同意更新ワークフローとユーザー削除ワークフローを作成するためのガイダンスを提供します。追加でサポートされるBrazeエンドポイントの詳細については、[サポートされるその他のアクション](#Other-supported-actions)を参照してください。

### OneTrust にBraze認証情報を追加する {#add-braze-credentials-to-onetrust}

OneTrustの**Integrations**メニューで、**Credentials** > **Add New**ボタンに移動して、**Select System**画面を表示します。ここで**Braze**を見つけ、**Next**ボタンをクリックします。

**Enter Credential Details**画面のプロンプトに従って、次の情報を入力します。完了したら、認証情報を保存します。
  - 認証情報名
  - コネクタータイプを**Web App**に設定します
  - ホスト名: `<your-braze-instance-url>`
  - **リクエストヘッダー**:
    - **Authorization**: Bearer
    - **Content-Type**: application/json
  - トークン: `<your-braze-api-key>`

### Brazeをシステムとして追加する {#add-braze-as-a-system}

#### ステップ 1: ワークフローの作成 {#step-1-create-a-workflow}

{% tabs %}
{% tab User Consent Update %}
1. OneTrust統合メニューで、**Gallery** > **Braze** > **Add**に移動し、新しいワークフローを作成します。![追加ボタンが表示された OneTrust ギャラリーのBraze統合。]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. ワークフローモーダルに名前と通知メールを入力します。**Create**ボタンをクリックします。作成時にWorkflow Builderが表示されます。Brazeワークフローには、削除リクエストの処理に使用できるAPIコールとアクションがシードされます。<br><br>
3. Workflow Builderで、ワークフローでトリガーするアクションを選択します。<br>![データ主体の同意更新イベント用のOneTrustワークフロービルダー。]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab User Deletion %}

1. OneTrust統合メニューで、**Gallery** > **Braze** > **Add**に移動し、新しいワークフローを作成します。![追加ボタンが表示された OneTrust ギャラリーのBraze統合。]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. ワークフローモーダルに名前と通知メールを入力します。**Create**ボタンをクリックします。作成時にWorkflow Builderが表示されます。Brazeワークフローには、削除リクエストの処理に使用できるAPIコールとアクションがシードされます。<br><br>
3. Workflow Builderで、ワークフローでトリガーするアクションを選択します。<br>![データ主体の削除イベント用のOneTrustワークフロービルダー。]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### ステップ 2: アクションの選択 {#step-2-select-action}
{% tabs %}
{% tab User Consent Update %}

1. 完了したら、**Done**をクリックし、**Add Action**を選択します。選択するアクションは、更新される設定のタイプと使用するエンドポイントによって異なります。
- ユーザーのグローバルサブスクリプション設定を更新するには、**POST User track - attributes**アクションを選択します。
- ユーザーのサブスクリプショングループ設定を更新するには、**POST User Track - Attributes**アクションまたは**POST Set Users Subscription Group Status**アクションを選択します。<br>![POST User track - attributesが表示されたOneTrustのアクション追加メニュー。]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. 目的のアクションを選択し、以前に作成したBraze認証情報を選択して、**Next**をクリックします。<br>![POST User track - attributesアクションのOneTrust認証情報選択画面。]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab User Deletion %}

1. 完了したら、**Done**をクリックし、**Add Action**を選択します。
- ユーザーをBrazeから削除するには、**POST User Delete Action**アクションを選択します。
<br>![POST User Deleteが表示されたOneTrustのアクション追加メニュー。]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. 目的のアクションを選択し、以前に作成したBraze認証情報を選択して、**Next**をクリックします。<br>![POST User DeleteアクションのOneTrust認証情報選択画面。]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### ステップ 3: リクエストボディの更新 {#step-3-update-request-body}
{% tabs %}
{% tab User Consent Update %}

1. ボディを更新して、必要なすべての動的な値を含めます。アクションのボディが[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)と[`/subscription/status/set` エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)に一致することを確認します。
2. 組織のニーズを満たすように、追加のパラメータまたは条件付きロジックを使用してワークフローをカスタマイズします。
3. 編集が終了したら、**Finish**をクリックし、次に**Activate**をクリックしてワークフローを有効にします。

{% alert note %}
OneTrustワークフローを使用してBrazeでサブスクリプショングループの設定を更新する場合、`subscription_group_id` は、サブスクリプショングループの作成時にBrazeにより設定されたIDと一致している必要があります。サブスクリプショングループの `subscription_group_id` にアクセスするには、Brazeダッシュボードの**サブスクリプショングループ**ページに移動します。
{% endalert %}

![サブスクリプショングループフィールドを含むPOST User track - attributesのOneTrustリクエストボディ。]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab User Deletion %}

1. ボディを更新して、必要なすべての動的な値を含めます。アクションのボディが[`/users/delete` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)と一致することを確認します。
2. 編集が終了したら、**Finish**、次に**Activate**を選択してワークフローを有効にします。

![external_idフィールドを含むPOST User DeleteのOneTrustリクエストボディ。]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### データ主体リクエストワークフローの更新 {#update-the-data-subject-request-workflow}
1. **Privacy Rights Automation**メニューで**Workflows**を選択します。
2. Braze統合で更新するワークフローを選択します。
3. **Edit**ボタンを選択して編集を有効にします。
4. 次に、Braze統合を追加するワークフローステップを選択し、**Add Connection**をクリックします。
5. 以前に作成したBrazeワークフローをシステムサブタスクとして追加します。

{% endtab %}
{% endtabs %}

## サポートされるその他のアクション {#other-supported-actions}

**POST User track - Attributes**、**POST Set Users Subscription Group Status**、および**POST User Delete**アクションに加えて、Brazeはカスタムワークフローの作成や、既存のワークフロー内でサブタスクとして使用できる他のエンドポイントもサポートしています。

サポートされているアクションの一覧を表示するには:
1. OneTrustで、**Integrations**メニューから**Systems**をクリックします。
2. **Braze**システムを選択します。
3. **Actions**タブに移動します。

![サポートされているAPIアクションが一覧表示されたOneTrust BrazeシステムのActionsタブ。]({% image_buster /assets/img/onetrust/onetrust7.png %})