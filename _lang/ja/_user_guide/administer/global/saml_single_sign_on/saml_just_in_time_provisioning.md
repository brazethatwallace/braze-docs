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

SAML JITPを使用するには、SAML SSOが設定・統合されている必要があります。Google SSOとは互換性がなく、IDプロバイダー主導（IdP主導）のログインワークフローのみがサポートされています。

| 要件 | 詳細 |
|---|---|
| SAML SSO | JITPを有効にする前に設定とテストを完了している必要があります。[SAML SSOの設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)を参照してください。 |
| IdP主導のログイン | ユーザーは初回ログイン時にIdPポータルからサインインする必要があります。サービスプロバイダー主導のログインのみでは、新しいユーザーはプロビジョニングされません。 |
| メールドメイン | ユーザーのメールドメインが、すでに会社に存在している必要があります（そのドメインで確認済みの、なりすましでない開発者が少なくとも1人必要です）。 |
| 会社のイネーブルメント | **自動ユーザープロビジョニング**トグルが表示される前に、Brazeが会社の`saml_jit_provisioning`機能を有効にする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JITPの前提条件" }

{% alert important %}
SAMLジャストインタイムプロビジョニングは、Brazeによって会社で有効にする必要があります。**自動ユーザープロビジョニング**トグルが利用できない場合は、アカウントマネージャーまたは[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。
{% endalert %}

## JITPの仕組み {#how-jitp-works}

JITPが有効で、新しいユーザーがIdP経由で初めてサインインすると、以下の処理が行われます。

1. BrazeがSAMLアサーションを検証し、ユーザーのメールドメインがJITPで許可されているかを確認します。
2. BrazeがSAMLアサーションのメールを使用してダッシュボードユーザーアカウントを作成します。
3. Brazeが**セキュリティ設定**で構成されたデフォルトのワークスペースと権限セットを割り当てます。
4. ユーザーは、別途招待やアクティベーションのステップなしで、すぐにBrazeにアクセスできます。

JITPは既存のユーザーの権限を更新しません。会社にまだ存在しないユーザーのアカウントのみを作成します。

## SAML ジャストインタイムプロビジョニング（JITP）の設定 {#setting-up-saml-just-in-time-provisioning-jitp}

Braze 管理者に以下の手順を依頼してください。

1. **設定** > **会社設定** > **管理者設定** > **セキュリティ設定**に移動します。
2. **SAML SSO** セクションで、**自動ユーザープロビジョニング**オプションをオンに切り替えます。
3. 新しい会社ユーザーを追加するデフォルトのワークスペースを選択します。
4. その新しい会社ユーザーに割り当てるデフォルトの権限セットを選択します。権限セットの作成方法については、[ユーザー権限の設定]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。

{% alert note %}
会社で詳細な権限を使用している場合は、移行後にデフォルトの権限セットを確認し、新しい JITP ユーザーが意図したアクセス権を受け取るようにしてください。
{% endalert %}

{: start="5"}
5. **変更を保存**を選択します。
6. SSO プロバイダーの設定で、Braze へのアクセスが必要なすべてのユーザーを SSO プロバイダーのディレクトリに追加します。
7. 初回ログイン時に IdP ポータルから Braze にアクセスするようユーザーに指示します。以降のログインでは、SAML シングルサインオンボタンが表示されます。

## よくあるご質問 {#frequently-asked-questions}

### SAML JITPを無効にするにはどうすればよいですか？ {#how-do-i-disable-saml-jitp}

JITPを設定した後、無効にするには[サポートに連絡]({{site.baseurl}}/braze_support)する必要があります。

### JITPはユーザーごとに異なる権限を割り当てることができますか？ {#can-jitp-assign-different-permissions-per-user}

いいえ。JITPで作成されたすべてのユーザーは、**セキュリティ設定**で構成されたデフォルトのワークスペースと権限セットを受け取ります。異なるアクセス権を割り当てるには、ユーザーを手動で作成するか、[SCIM自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning)を使用してください。

### JITPはサービスプロバイダー起点のログインで機能しますか？ {#does-jitp-work-with-sp-initiated-login}

いいえ。JITPはIdP起点のログイン時、つまりユーザーがIDプロバイダーのポータルからログインを開始した場合にのみ実行されます。

## トラブルシューティング {#troubleshooting}

### 初回SSOサインイン時にユーザーがプロビジョニングされない {#user-was-not-provisioned-on-first-sso-sign-in}

以下を確認してください。

- JITPが有効になっており、**セキュリティ設定**に保存されていること。
- ユーザーがBrazeのログインページからだけでなく、IdPポータル経由（IdP起点）でサインインしたこと。
- ユーザーのメールドメインが既に会社に存在していること。
- SAMLアサーションに、ユーザーがサインインに使用するアドレスと一致する有効な`email`属性が含まれていること。

### Microsoft Entra IDでシングルサインオンボタンが表示されない {#single-sign-on-button-doesnt-appear-with-microsoft-entra-id}

Microsoft Entraの**基本SAML構成**フォームにあるBraze用の**サインオンURL**フィールドに値が入っていると、IdP起点のログイン時にSSOボタンではなくパスワードオプションのみが表示される場合があります。この問題を防ぐには、Microsoft Entra管理センターでBrazeを構成する際に**サインオンURL**フィールドを空欄のままにしてください。