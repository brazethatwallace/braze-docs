---
nav_title: SAML ジャストインタイムプロビジョニング
article_title: SAML ジャストインタイムプロビジョニング
page_order: 1
page_type: tutorial
description: "この記事では、SAML ジャストインタイムプロビジョニングを設定して、新しい会社ユーザーが初回サインイン時に Braze アカウントを作成できるようにする方法を説明します。"

---

# SAML ジャストインタイムプロビジョニング {#saml-just-in-time-provisioning}

> ジャストインタイムプロビジョニングは [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) と連携して、新しい会社ユーザーが初回サインイン時に Braze アカウントを作成できるようにします。これにより、管理者が新しい会社ユーザーのアカウントを手動で作成し、権限を選択し、ワークスペースに割り当て、アカウントの有効化を待つ必要がなくなります。

セキュリティ対策として、SAML ジャストインタイムプロビジョニング（JITP）は、会社に既に存在するメールドメインを持つユーザーに対してのみ機能します。JITPは、会社内に少なくとも1人の確認済みで、なりすましではない開発者が既に存在するドメインでのみ可能です。

例えば、アカウント `jon.smith@decorumsoft.com` がJITPを使用して Decorumsoft にログインできるとします。アカウント `jane.smith@decorumsoft.com` は同じドメインを持つため、プロビジョニングも許可されます。しかし、`jon.smith@decorumsoft.eu` でJITPを使用しようとすると、Decorumsoft の Braze ダッシュボード内に `decorumsoft.eu` のアカウントが存在しないため、プロビジョニングは許可されません。

会社の例外を設定するには、[サポート]({{site.baseurl}}/braze_support)にお問い合わせください。

## 前提条件 {#prerequisites}

SAML JITPを使用するには、SAML SSOがセットアップおよび統合されている必要があります。Google SSOとは互換性がなく、IDプロバイダー開始（IdP開始）のログインワークフローでのみサポートされています。

## SAML ジャストインタイムプロビジョニング（JITP）のセットアップ {#setting-up-saml-just-in-time-provisioning-jitp}

Braze 管理者に以下の手順を実行してもらいます。

1. **設定** > **管理者設定** > **セキュリティ設定**に移動します。
2. **SAML SSO** セクションで、**Automatic user provisioning** オプションをオンに切り替えます。
3. 新しい会社ユーザーを追加するデフォルトのワークスペースを選択します。
4. 新しい会社ユーザーに割り当てるデフォルトの権限セットを選択します。権限セットの作成方法については、[ユーザー権限の設定]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。
6. ページ下部の**変更内容を保存**を選択します。
7. SSOプロバイダーの設定で、Brazeへのアクセスが必要なすべてのユーザーをSSOプロバイダーのディレクトリに追加します。
8. ユーザーに、初回ログイン時にIdPポータルからBrazeにアクセスするよう指示します。その後、以降のログインではSAML シングルサインオンボタンが表示されます。

## よくある質問 {#frequently-asked-questions}

### SAML JITPを無効にするにはどうすればよいですか？ {#how-do-i-disable-saml-jitp}

JITPをセットアップした後、無効にするには[サポートにお問い合わせ]({{site.baseurl}}/braze_support)ください。

## トラブルシューティング {#troubleshooting}

### Microsoft Entra ID でシングルサインオンボタンが表示されない {#single-sign-button-doesnt-appear-with-microsoft-entra-id}

Microsoft Entra の Braze 用**基本 SAML 構成**フォームの**サインオン URL** フィールドが原因で、IdP開始のログイン時にユーザーにSSOボタンではなくパスワードオプションのみが表示される場合があります。この問題を防ぐには、Microsoft Entra 管理センターで Braze を設定する際に**サインオン URL** フィールドを空白のままにしてください。