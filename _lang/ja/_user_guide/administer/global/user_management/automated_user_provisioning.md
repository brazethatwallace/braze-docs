---
nav_title: 自動ユーザープロビジョニング
article_title: 自動ユーザープロビジョニング
page_order: 3
page_type: reference
description: "このリファレンス記事では、自動ユーザープロビジョニングを行うために提供する必要がある情報と、生成されたクロスドメインID管理用システム（SCIM）トークンの使用方法と使用場所について説明します。"
alias: /scim/automated_user_provisioning/

---

# 自動ユーザープロビジョニング {#automated-user-provisioning}

> 自動ユーザープロビジョニングを使用すると、ダッシュボードで手動で行う代わりに、APIを通じてBrazeユーザーを作成・管理できます。Brazeはクロスドメインid管理用システム（SCIM）を通じてこの機能をサポートしています。この記事では、提供すべき情報、SCIMトークンの生成方法、SCIM APIエンドポイントの場所について説明します。

## SCIMプロビジョニング設定へのアクセス {#accessing-scim-provisioning-settings}

{% alert important %}
SCIMプロビジョニングの利用可否はプラットフォームのエディションによって異なります。この機能がワークスペースにない場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

1. Brazeダッシュボードで、**設定** > **管理者設定** > **SCIMプロビジョニング**に移動し、**SCIM連携の設定**を選択します。
2. **Brazeの設定**ステップで、プロビジョニング方法を選択し、アクセス設定を入力します。

![SCIM連携を設定するページで、プロビジョニング方法の選択とアクセス設定の提供を行うセクションがあります。]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. **IdP設定**ステップで、選択したプロビジョニング方法に対応するプラットフォーム内のステップに従ってください。

{% tabs %}
{% tab Okta - Brazeアプリ %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

OktaでBrazeアプリをSAML SSO用に設定した場合は、**Okta - Brazeアプリ**オプションを使用します。SSO用のカスタムアプリを設定した場合は、[Okta - カスタムアプリ統合]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning)タブの手順に従ってください。

## ステップ1:SCIMプロビジョニングを設定する {#step-1-set-up-scim-provisioning}

### ステップ1.1:SCIMを有効にする {#step-11-enable-scim}

1. Oktaで、**Applications** > **Applications**に移動し、**Create App Integration**を選択します。サインイン方法として**SAML 2.0**を選択します。
2. カスタムアプリを作成するには、以下の詳細（Brazeの[**IdP設定**ステップ](#accessing-scim-provisioning-settings)にあります）を入力します：
- アプリのロゴ
- シングルサインオンURL
- オーディエンスURL（サービスプロバイダーエンティティID）
3. **Finish**を選択します。
4. **General**タブを選択します。
5. **App Settings**セクションで、**Edit**を選択します。
6. **Provisioning**フィールドで、**SCIM**を選択します。

### ステップ1.2:アプリケーションの表示を無効にする {#step-12-disable-application-visibility}

1. **Application visibility**フィールドで、**Do not display application icon to user**チェックボックスを選択します。これにより、ユーザーがアプリを通じてSSOにアクセスすることを防ぎます。このアプリはSCIM専用です。
2. **Save**を選択します。

### ステップ1.3:SCIM連携を設定する {#step-13-set-up-the-scim-integration}

1. **Provisioning**タブを選択します。
2. **Settings** > **Integration** > **SCIM Connection**で**Edit**を選択し、**Setup SCIM provisioning**ページのテーブルに表示されるフィールド値を入力します。

### ステップ1.4:API認証情報をテストする {#step-14-test-the-api-credentials}

**Test API Credentials**を選択します。統合が成功すると確認メッセージが表示され、保存できます。

### ステップ1.5:アプリへのプロビジョニングを有効にする {#step-15-enable-provisioning-to-the-app}

1. **Provisioning** > **Settings** > **To App** > **Provisioning to App**で、**Edit**を選択します。
2. 以下を有効にします：
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. **Setup SCIM provisioning**ページのテーブルに表示されるマッピングを使用して、**Attribute Mapping**セクションを確認・設定します。

## ステップ2:ユーザーをアプリに割り当てる {#step-2-assign-users-to-the-app}

1. **Assignment**タブを選択します。
2. **Assign**を選択し、オプションを選択します。
3. Brazeへのアクセス権を持つべきユーザーにアプリを割り当てます。
4. 割り当てが完了したら**Done**を選択します。

{% endtab %}
{% tab Okta - カスタムアプリ統合 %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

SSO用のカスタムアプリを設定した場合は、**Okta - カスタムアプリ統合**オプションを使用します。OktaでBrazeアプリをSAML SSO用に設定した場合は、[Okta - Brazeアプリ]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning)タブの手順に従ってください。

## ステップ1:SCIMプロビジョニングを設定する

### ステップ1.1:SCIMを有効にする

1. Oktaで、Brazeアプリに移動します。
2. **General**タブを選択します。
3. **App Settings**セクションで、**Edit**を選択します。
4. **Provisioning**フィールドで、**SCIM**を選択します。
5. **Save**を選択します。

### ステップ1.2:SCIM連携を設定する {#step-12-set-up-scim-integration}

1. **Provisioning**タブを選択します。
2. **Settings** > **Integration** > **SCIM Connection**で、**Edit**を選択し、**Setup SCIM provisioning**ページのテーブルに表示されるフィールド値を入力します。
3. **Test API Credentials**を選択してAPI認証情報をテストします。
4. **Save**を選択します。

### ステップ1.3:アプリへのプロビジョニングを有効にする {#step-13-enable-provisioning-to-the-app}

1. **Provisioning** > **Settings** > **To App** > **Provisioning to App**で、**Edit**を選択します。
2. 以下を有効にします：
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. **Setup SCIM provisioning**ページのテーブルに表示されるマッピングを使用して、**Attribute Mapping**セクションを確認・設定します。

## ステップ2:ユーザーをアプリに割り当てる

1. **Assignment**タブを選択します。
2. **Assign**を選択し、オプションを選択します。
3. Brazeへのアクセス権を持つべきユーザーにアプリを割り当てます。
4. **Done**を選択します。

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Entra ID integration' %}

## ステップ1:SCIMプロビジョニングアプリを設定する {#step-1-set-up-scim-provisioning-app}

### ステップ1.1:Microsoft Entra管理センターにログインする {#step-11-log-into-microsoft-entra-admin-center}

Microsoft Entra管理センターにログインします。

### ステップ1.2:SCIMアプリを作成・設定する {#step-12-create-and-set-up-your-scim-app}

1. ナビゲーションメニューで、**Entra ID** > **Enterprise apps**に移動します。
2. **New application**を選択します。
3. **Create your own application**を選択します。
4. パネルで、アプリの名前を入力します。
5. **What are you looking to do with your application?** セクションで、**Integrate application you don't find in the gallery (Non-gallery)**を選択します。
6. **Create**を選択します。

### ステップ1.3:SCIM連携を設定する {#step-13-set-up-scim-integration}

1. SCIMアプリケーションの**Manage** > **Provisioning**セクションに移動します。
2. **Connect your application**または**New configuration**を選択し、**Setup SCIM provisioning**ページのテーブルに表示されるフィールド値を入力します。

### ステップ1.4:アプリへのプロビジョニングを有効にする {#step-14-enable-provisioning-to-the-app}

1. SCIMアプリケーションの**Manage** > **Attribute mapping (Preview)**セクションに移動します。
2. **Provision Microsoft Entra ID Users**を選択します。
3. **Setup SCIM provisioning**ページのテーブルに表示される属性と一致するように、**Attribute Mapping**セクションを確認・設定します。
4. **Attribute Mapping**ページを閉じます。

## ステップ2:ユーザーをアプリに割り当てる

1. **Manage** > **Users and Groups**に移動します。
2. **Add user/group**を選択します。
3. **None Selected**を選択して、ユーザーをアプリに割り当てます。
4. **Select**ボタンを選択して割り当てを確認します。

{% endtab %}
{% tab カスタム %}

## ステップ1:SCIM設定を構成する {#step-1-configure-your-scim-settings}

- **デフォルトワークスペース:** 新しいユーザーがデフォルトで追加されるワークスペースを選択します。[SCIM APIリクエスト]({{site.baseurl}}/post_create_user_account)でワークスペースを指定しない場合、Brazeはユーザーをこのワークスペースに割り当てます。
- **サービスOrigin:** SCIMリクエストのOriginドメインを入力します。Brazeはリクエストの送信元を確認するために`X-Request-Origin`ヘッダーでこれを使用します。
- **IP許可リスト（オプション）:** SCIMリクエストを特定のIPアドレスに制限できます。許可するIPアドレスのカンマ区切りリストまたは範囲を入力します。各リクエストの`X-Request-Origin`ヘッダーを使用して、リクエストのIPアドレスが許可リストと照合されます。

## ステップ2:SCIMトークンを生成する {#step-2-generate-a-scim-token}

必須フィールドの入力が完了したら、**SCIMトークンを生成**を押してSCIMトークンを生成し、SCIM APIエンドポイントを確認します。ページを離れる前にSCIMトークンをコピーしてください。**このトークンは一度しか表示されません。**

![SCIM APIエンドポイントとSCIMトークンのフィールドがマスクされた値とコピーボタンとともに表示されています。トークンフィールドの下に「トークンをリセット」ボタンがあります。]({% image_buster /assets/img/scim.png %})

Brazeはすべてのsciリクエストに、HTTP `Authorization`ヘッダーに添付されたSCIM APIベアラートークンが含まれていることを要求します。

{% endtab %}
{% endtabs %}