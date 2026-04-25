---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 2
page_type: tutorial
description: "この記事では、Braze で Microsoft Entra シングルサインオン機能を設定する方法について説明します。"

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) は、Microsoft のクラウドベースの ID およびアクセス管理サービスで、従業員のサインインやリソースへのアクセスを支援します。Entra SSO を使用すると、ビジネス要件に基づいてアプリやアプリリソースへのアクセスを制御できます。

## 要件

セットアップ時に、Assertion Consumer Service (ACS) URL の入力を求められます。

| 要件 | 詳細 |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> 一部の ID プロバイダーでは、Reply URL、Audience URL、または Audience URI と呼ばれることもあります。 |
| Entity ID | `braze_dashboard`|
| RelayState API キー | ID プロバイダーログインを有効にするには、**設定** > **API キー**に移動し、`sso.saml.login` 権限を持つ API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Microsoft Entra SSO 内でのサービスプロバイダー（SP）起点のログイン

### ステップ 1: ギャラリーから Braze を追加する

1. Microsoft Entra 管理センターで、**Identity** > **Applications** > **Enterprise Applications** に移動し、**New application** を選択します。
2. 検索ボックスで **Braze** を検索し、結果パネルから選択して、**Add** を選択します。

### ステップ 2: Microsoft Entra SSO を設定する

1. Microsoft Entra 管理センターで、Braze アプリケーション統合ページに移動し、**Single sign-on** を選択します。
2. **Select a single sign-on method** ページで、方法として **SAML** を選択します。
3. **Set up Single Sign-On with SAML** ページで、**Basic SAML Configuration** の編集アイコンを選択します。
4. [Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/#braze-instances)と次のパターンを組み合わせた **Reply URL** を入力して、IdP 起点モードでアプリケーションを設定します: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`。
5. **Relay State** フィールドに、生成した Relay State API キーを入力して RelayState を設定します。

{% alert important %}
**Sign-On URL** フィールドは設定**しないでください**。このフィールドを空白のままにして、IdP 起点の SAML SSO に関する問題を防止してください。
{% endalert %}

{: start="6"}
6. Braze が期待する特定の形式で SAML アサーションをフォーマットします。これらの属性と値のフォーマット方法については、ユーザー属性とユーザークレームに関する以下のタブを参照してください。

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
メールフィールドが Braze でユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じですが、異なる設定の場合は、システム管理者と協力してこれらのフィールドが正確に一致するようにしてください。
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
メールフィールドが Braze でユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じですが、異なる設定の場合は、システム管理者と協力してこれらのフィールドが正確に一致するようにしてください。
{% endalert %}

これらのユーザークレームと値は、**Manage claim** セクションから管理できます。

{% endtab %}
{% endtabs %}

{: start="8"}
8. **Set up Single Sign-On with SAML** ページに移動し、**SAML Signing Certificate** セクションまでスクロールして、要件に基づいて適切な **Certificate (Base64)** をダウンロードします。
9. **Set up Braze** セクションに移動し、[Braze の設定](#step-3)で使用する適切な URL をコピーします。

### ステップ 3: Braze 内で Microsoft Entra SSO を設定する {#step-3}

Microsoft Entra 管理センターで Braze を設定すると、Microsoft Entra からターゲット URL（ログイン URL）と **x.509** 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にした後、以下を行います:

1. **設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSO セクションを**オン**に切り替えます。
2. 同じページで、以下を追加します:

| 要件 | 詳細 |
|---|---|
| `SAML Name` | ログイン画面のボタンテキストとして表示されます。通常は「Microsoft Entra」のような ID プロバイダーの名前です。 |
| `Target URL` | Microsoft Entra が提供するログイン URL です。|
| `Certificate` | `x.509` PEM エンコード証明書は、ID プロバイダーから提供されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Braze アカウントユーザーが SAML SSO のみでサインインするようにしたい場合は、**会社の設定**ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#restriction)できます。
{% endalert %}