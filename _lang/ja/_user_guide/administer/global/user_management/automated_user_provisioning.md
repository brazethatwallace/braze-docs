---
nav_title: 自動ユーザープロビジョニング
article_title: 自動ユーザープロビジョニング
page_order: 3
page_type: reference
description: "このリファレンス記事では、自動ユーザープロビジョニングを行うために提供する必要がある情報と、生成されたクロスドメイン ID 管理用システム（SCIM）トークンの使用方法と使用場所について説明します。"
alias: /scim/automated_user_provisioning/

---

# 自動ユーザープロビジョニング

> 自動ユーザープロビジョニングを使用すると、ダッシュボードで手動で行う代わりに、API を通じて Braze ユーザーを作成・管理できます。Braze はクロスドメイン ID 管理用システム（SCIM）を通じてこの機能をサポートしています。この記事では、提供すべき情報、SCIM トークンの生成方法、SCIM API エンドポイントの場所について説明します。

{% multi_lang_include early_access_beta_alert.md feature='SCIM provisioning' %}

## SCIM プロビジョニング設定へのアクセス {#accessing-scim-provisioning-settings}

1. Braze のダッシュボードで、**設定** > **管理者設定** > **SCIM プロビジョニング**に移動し、**SCIM 連携の設定**を選択します。
2. **Braze の設定**ステップでは、プロビジョニング方法を選択し、アクセス設定を提供します。

![SCIM 統合を設定するページで、プロビジョニング方法の選択とアクセス設定の提供を行うセクションがあります。]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. **IdP 設定**ステップでは、選択したプロビジョニング方法に対応するプラットフォーム内のステップに従ってください。

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Okta で Braze アプリを SAML SSO 用に設定した場合、**Okta - Braze アプリ**オプションを使用します。SSO 用のカスタムアプリを設定する場合は、[Okta - カスタムアプリ統合]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning)タブの手順に従ってください。

## ステップ 1: SCIM プロビジョニングを設定する {#step-1-set-up-scim-provisioning}

### ステップ 1.1: SCIM を有効にする

1. Okta で、**Applications** > **Applications** に移動し、**Create App Integration** を選択します。サインイン方法として **SAML 2.0** を選択します。
2. カスタムアプリを作成するには、以下の詳細（Braze の [**IdP 設定**ステップ](#accessing-scim-provisioning-settings)にあります）を入力します：
- アプリのロゴ
- シングルサインオン URL
- オーディエンス URL（サービスプロバイダーエンティティ ID）
3. **Finish** を選択します。
4. **General** タブを選択します。
5. **App Settings** のセクションで、**Edit** を選択します。
6. **Provisioning** フィールドで、**SCIM** を選択します。

### ステップ 1.2: アプリケーションの表示を無効にする

1. **Application visibility** フィールドで、**Do not display application icon to user** チェックボックスを選択します。これにより、ユーザーがアプリを通じて SSO にアクセスすることを防ぎます。このアプリは SCIM 専用です。
2. **Save** を選択します。

### ステップ 1.3: SCIM 連携を設定する

1. **Provisioning** タブを選択します。
2. **Settings** > **Integration** > **SCIM Connection** で **Edit** を選択し、**Setup SCIM provisioning** ページのテーブルに表示されるフィールド値を入力します。

### ステップ 1.4: API 認証情報をテストする

**Test API Credentials** を選択します。統合が成功すると確認メッセージが表示され、保存できます。

### ステップ 1.5: アプリへのプロビジョニングを有効にする

1. **Provisioning** > **Settings** > **To App** > **Provisioning to App** で、**Edit** を選択します。
2. 以下を有効にします：
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. **Setup SCIM provisioning** ページのテーブルに表示されるマッピングを使用して、**Attribute Mapping** セクションを確認・設定します。

## ステップ 2: ユーザーをアプリに割り当てる

1. **Assignment** タブを選択します。
2. **Assign** を選択し、オプションを選択します。
3. Braze へのアクセス権を持つべきユーザーにアプリを割り当てます。
4. 割り当てが完了したら **Done** を選択します。

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

SSO 用のカスタムアプリを設定した場合、**Okta - カスタムアプリ統合**オプションを使用します。Okta で Braze アプリを SAML SSO 用に設定した場合は、[Okta - Braze アプリ]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning)タブの手順に従ってください。

## ステップ 1: SCIM プロビジョニングを設定する {#step-1-set-up-scim-provisioning}

### ステップ 1.1: SCIM を有効にする

1. Okta で、Braze アプリに移動します。
2. **General** タブを選択します。
3. **App Settings** のセクションで、**Edit** を選択します。
4. **Provisioning** フィールドで、**SCIM** を選択します。
5. **Save** を選択します。

### ステップ 1.2: SCIM 連携を設定する

1. **Provisioning** タブを選択します。
2. **Settings** > **Integration** > **SCIM Connection** で、**Edit** を選択し、**Setup SCIM provisioning** ページのテーブルに表示されるフィールド値を入力します。
3. **Test API Credentials** を選択して API 認証情報をテストします。
4. **Save** を選択します。

### ステップ 1.3: アプリへのプロビジョニングを有効にする

1. **Provisioning** > **Settings** > **To App** > **Provisioning to App** で、**Edit** を選択します。
2. 以下を有効にします：
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. **Setup SCIM provisioning** ページのテーブルに表示されるマッピングを使用して、**Attribute Mapping** セクションを確認・設定します。

## ステップ 2: ユーザーをアプリに割り当てる

1. **Assignment** タブを選択します。
2. **Assign** を選択し、オプションを選択します。
3. Braze へのアクセス権を持つべきユーザーにアプリを割り当てます。
4. **Done** を選択します。

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## ステップ 1: SCIM プロビジョニングアプリを設定する

### ステップ 1.1: Microsoft Entra 管理センターにログインする

Microsoft Entra 管理センターにログインします。

### ステップ 1.2: SCIM アプリを作成・設定する

1. ナビゲーションメニューで、**Entra ID** > **Enterprise apps** に移動します。
2. **New application** を選択します。
3. **Create your own application** を選択します。
4. パネルで、アプリの名前を入力します。
5. **What are you looking to do with your application?** セクションで、**Integrate application you don't find in the gallery (Non-gallery)** を選択します。
6. **Create** を選択します。

### ステップ 1.3: SCIM 連携を設定する

1. SCIM アプリケーションの **Manage** > **Provisioning** セクションに移動します。
2. **Connect your application** または **New configuration** を選択し、**Setup SCIM provisioning** ページのテーブルに表示されるフィールド値を入力します。

### ステップ 1.4: アプリへのプロビジョニングを有効にする

1. SCIM アプリケーションの **Manage** > **Attribute mapping (Preview)** セクションに移動します。
2. **Provision Microsoft Entra ID Users** を選択します。
3. **Setup SCIM provisioning** ページのテーブルに表示される属性と一致するように、**Attribute Mapping** セクションを確認・設定します。
4. **Attribute Mapping** ページを閉じます。

## ステップ 2: ユーザーをアプリに割り当てる

1. **Manage** > **Users and Groups** に移動します。
2. **Add user/group** を選択します。
3. **None Selected** を選択して、ユーザーをアプリに割り当てます。
4. **Select** ボタンを選択して割り当てを確認します。

{% endtab %}
{% tab Custom %}

## ステップ 1: SCIM 設定を構成する

- **デフォルトワークスペース:** 新しいユーザーがデフォルトで追加されるワークスペースを選択します。[SCIM API リクエスト]({{site.baseurl}}/post_create_user_account/)でワークスペースを指定しない場合、Braze はユーザーをこのワークスペースに割り当てます。
- **サービス Origin:** SCIM リクエストの Origin ドメインを入力します。Braze はリクエストの送信元を確認するために `X-Request-Origin` ヘッダーでこれを使用します。
- **IP 許可リスト（オプション）:** SCIM リクエストを特定の IP アドレスに制限できます。許可する IP アドレスのカンマ区切りリストまたは範囲を入力します。各リクエストの `X-Request-Origin` ヘッダーを使用して、リクエストの IP アドレスが許可リストと照合されます。

![SCIM プロビジョニング設定フォームで、デフォルトワークスペース、サービス Origin、オプションの IP 許可リストの3つのフィールドがあります。「SCIM トークンを生成」ボタンは無効になっています。]({% image_buster /assets/img/scim_unfilled.png %})

## ステップ 2: SCIM トークンを生成する

必須フィールドの入力が完了したら、**SCIM トークンを生成**を押して SCIM トークンを生成し、SCIM API エンドポイントを確認します。ページを離れる前に SCIM トークンをコピーしてください。**このトークンは一度しか表示されません。**

![SCIM API エンドポイントと SCIM トークンのフィールドがマスクされた値とコピーボタンとともに表示されています。トークンフィールドの下に「トークンをリセット」ボタンがあります。]({% image_buster /assets/img/scim.png %})

Braze はすべての SCIM リクエストに、HTTP `Authorization` ヘッダーに添付された SCIM API ベアラートークンが含まれていることを要求します。

{% endtab %}
{% endtabs %}