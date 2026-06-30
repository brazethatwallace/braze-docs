---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 2
page_type: tutorial
description: "この記事では、Brazeで Microsoft Entra シングルサインオン機能を設定する方法について説明します。"

---

# Microsoft Entra SSO {#microsoft-entra-sso}

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) は、MicrosoftのクラウドベースのIDおよびアクセス管理サービスで、従業員のサインインやリソースへのアクセスを支援します。Entra SSOを使用すると、ビジネス要件に基づいてアプリやアプリリソースへのアクセスを制御できます。

## 要件 {#requirements}

セットアップ時に、Assertion Consumer Service (ACS) URLの入力を求められます。

| 要件 | 詳細 |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> 一部のIDプロバイダーでは、Reply URL、Audience URL、または Audience URI と呼ばれることもあります。 |
| Entity ID | `braze_dashboard`|
| RelayState APIキー | IDプロバイダーログインを有効にするには、**設定** > **APIキー**に移動し、`sso.saml.login` 権限を持つAPIキーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## Microsoft Entra SSO内でのサービスプロバイダー（SP）起点のログイン {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### ステップ 1:ギャラリーからBrazeを追加する {#step-1-add-braze-from-the-gallery}

1. Microsoft Entra管理センターで、**Identity** > **Applications** > **Enterprise Applications** に移動し、**New application** を選択します。
2. 検索ボックスで **Braze** を検索し、結果パネルから選択して、**Add** を選択します。

### ステップ 2:Microsoft Entra SSOを設定する {#step-2-configure-microsoft-entra-sso}

1. Microsoft Entra管理センターで、Brazeアプリケーション統合ページに移動し、**Single sign-on** を選択します。
2. **Select a single sign-on method** ページで、方法として **SAML** を選択します。
3. **Set up Single Sign-On with SAML** ページで、**Basic SAML Configuration** の編集アイコンを選択します。
4. [Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints#braze-instances)と次のパターンを組み合わせた **Reply URL** を入力して、IdP起点モードでアプリケーションを設定します: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`。
5. **Relay State** フィールドに、生成した Relay State APIキーを入力して RelayStateを設定します。

{% alert important %}
**Sign-On URL** フィールドは設定**しないでください**。このフィールドを空白のままにして、IdP起点のSAML SSOに関する問題を防止してください。
{% endalert %}

{: start="6"}
6. Brazeが期待する特定の形式でSAMLアサーションをフォーマットします。これらの属性と値のフォーマット方法については、ユーザー属性とユーザークレームに関する以下のタブを参照してください。

{% tabs %}
{% tab ユーザー属性 %}
これらの属性の値は、**Application Integration** ページの **User Attributes** セクションから管理できます。

以下の属性ペアリングを使用します:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
メールフィールドがBrazeでユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じですが、異なる設定の場合は、システム管理者と協力してこれらのフィールドが正確に一致するようにしてください。
{% endalert %}

{% endtab %}
{% tab ユーザークレーム %}

**Set up Single Sign-On with SAML** ページで、**Edit** を選択して **User Attributes** ダイアログを開きます。次に、適切な形式に従ってユーザークレームを編集します。

以下のクレーム名ペアリングを使用します:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
メールフィールドがBrazeでユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じですが、異なる設定の場合は、システム管理者と協力してこれらのフィールドが正確に一致するようにしてください。
{% endalert %}

これらのユーザークレームと値は、**Manage claim** セクションから管理できます。

{% endtab %}
{% endtabs %}

{: start="8"}
8. **Set up Single Sign-On with SAML** ページに移動し、**SAML Signing Certificate** セクションまでスクロールして、要件に基づいて適切な **Certificate (Base64)** をダウンロードします。
9. **Set up Braze** セクションに移動し、[Brazeの設定](#step-3)で使用する適切なURLをコピーします。

### ステップ 3:Braze内でMicrosoft Entra SSOを設定する {#step-3}

Microsoft Entra管理センターでBrazeを設定すると、Microsoft Entraからターゲット URL（ログイン URL）と **x.509** 証明書が提供されます。これらをBrazeアカウントに入力します。

アカウントマネージャーがアカウントのSAML SSOを有効にした後、以下を行います:

1. **設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSOセクションを**オン**に切り替えます。
2. 同じページで、以下を追加します:

| 要件 | 詳細 |
|---|---|
| `SAML Name` | ログイン画面のボタンテキストとして表示されます。通常は「Microsoft Entra」のようなIDプロバイダーの名前です。 |
| `Target URL` | Microsoft Entraが提供するログインURLです。|
| `Certificate` | `x.509` PEMエンコード証明書は、IDプロバイダーから提供されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 3: Braze内でMicrosoft Entra SSOを設定する" }

{% alert tip %}
Brazeアカウントユーザーが SAML SSOのみでサインインするようにしたい場合は、**会社の設定**ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)できます。
{% endalert %}