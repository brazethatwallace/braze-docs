---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "この記事では、シングルサインオンにOktaを使用するようにBrazeを設定する方法を順に説明します。"

---

# Okta

> Oktaは、あらゆるデバイス上のあらゆるアプリケーションとあらゆるユーザーを接続します。Oktaはクラウド向けに構築されたエンタープライズクラスのID管理サービスですが、多くのオンプレミスアプリケーションと互換性があります。Oktaを使用すると、ITチームはあらゆる従業員によるあらゆるアプリケーションやデバイスへのアクセスを管理できます。

## 要件 {#requirements}

| 要件 | 詳細 |
| ----------- | ------- |
| アカウントでOktaがオンになっている | Brazeアカウントマネージャーに連絡し、アカウントでこれをオンにしてもらいます。 |
| Okta管理者権限 | Oktaを設定する前に、管理者権限があることを確認してください。 |
| Braze管理者権限 | Oktaを設定する前に、管理者権限があることを確認してください。 |
| RelayState APIキー | IdPログインを有効にするには、**設定** > **APIキー**に移動し、`sso.saml.login` 権限を持つAPIキーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## ステップ1:Brazeの設定 {#step-1-configure-braze}

### ステップ1a:Brazeのセキュリティ設定に移動 {#step-1a-navigate-to-security-settings-in-braze}

アカウントマネージャーがアカウントのSAML SSOを有効にした後、**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSOセクションを**オン**に切り替えます。

![セキュリティ設定ページでOkta SAML SSOが有効になっている画面。]({% image_buster/assets/img/Okta/okta1.png %})

### ステップ1b:SAML SSO設定の編集 {#step-1b-edit-saml-sso-settings}

Okta管理者ダッシュボードから、Oktaがターゲット URL（ログインURL）と `x.509` 証明書を提供するので、Brazeアカウントの**セキュリティ設定**ページに入力する必要があります。

![SAML SSO設定の編集に関するスクリーンショット。]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示されます。通常、IDプロバイダーの名前です（例:「Okta」）。 |
| `Target URL` | これは、Okta管理者ダッシュボードで提供されるログインURLです。これを確認するには、**Applications** > 自分のアプリケーション > **General**タブ > **App Embed Link** > **Embed Link**に移動します。 |
| `Certificate` | PEMエンコードされた `x.509` 証明書は、IDプロバイダーから提供されます。このフィールドにコピーアンドペーストする必要があります。Oktaで取得するには、**SAML Signing Certificates**に移動し、**Actions** > **Download certificate**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1b: SAML SSO設定の編集" }

完了したら、ページの下部にある**変更内容を保存**を選択します。

## ステップ2:Oktaの設定 {#step-2-configure-okta}

Oktaで、Braze SAMLアプリの**Sign On**タブを選択し、**Edit**をクリックします。

次に、`sso.saml.login` 権限を持つRelayState APIキーを**Default Relay State**フィールドに入力します。

![OktaのSign OnタブにあるデフォルトのRelayState。]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

これらの新しい設定を必ず保存してください。

{% alert tip %}
BrazeアカウントユーザーがSAML SSOのみでサインインするようにしたい場合は、**会社の設定**ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)できます。
{% endalert %}

## ステップ3:ログイン {#step-3-log-in}

これで、Oktaを使用してBrazeにログインできるようになります。

![Okta SSOが有効になったBrazeダッシュボードのログイン画面。]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}