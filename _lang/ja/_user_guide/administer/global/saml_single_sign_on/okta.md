---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "この記事では、シングルサインオンに Okta を使用するように Braze を設定する方法を順に説明します。"

---

# Okta

> Okta は、あらゆるデバイス上のあらゆるアプリケーションとあらゆるユーザーを接続します。Okta はクラウド向けに構築されたエンタープライズクラスの ID 管理サービスですが、多くのオンプレミスアプリケーションと互換性があります。Okta を使用すると、IT チームはあらゆる従業員によるあらゆるアプリケーションやデバイスへのアクセスを管理できます。

## 要件 {#requirements}

| 要件 | 詳細 |
| ----------- | ------- |
| アカウントで Okta がオンになっている | Braze アカウントマネージャーに連絡し、アカウントでこれをオンにしてもらいます。 |
| Okta 管理者権限 | Okta を設定する前に、管理者権限があることを確認してください。 |
| Braze 管理者権限 | Okta を設定する前に、管理者権限があることを確認してください。 |
| RelayState API キー | IdP ログインを有効にするには、**設定** > **API キー**に移動し、`sso.saml.login` 権限を持つ API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## ステップ 1: Brazeの設定 {#step-1-configure-braze}

### ステップ 1a: Brazeのセキュリティ設定に移動 {#step-1a-navigate-to-security-settings-in-braze}

アカウントマネージャーがアカウントの SAML SSO を有効にした後、**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSO セクションを**オン**に切り替えます。

![セキュリティ設定ページで、Okta SAML SSO が有効になっています。]({% image_buster/assets/img/Okta/okta1.png %})

### ステップ 1b: SAML SSO 設定の編集 {#step-1b-edit-saml-sso-settings}

Okta 管理者ダッシュボードから、Okta がターゲット URL（ログイン URL）と `x.509` 証明書を提供するので、Braze アカウントの**セキュリティ設定**ページに入力する必要があります。

![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示されます。これは通常、ID プロバイダーの名前です（例:「Okta」）。 |
| `Target URL` | これは、Okta 管理者ダッシュボードで提供されるログイン URL です。これを確認するには、**Applications** > 自分のアプリケーション > **General** タブ > **App Embed Link** > **Embed Link** に移動します。 |
| `Certificate` | PEM エンコードされた `x.509` 証明書は、ID プロバイダーから提供されます。このフィールドにコピーアンドペーストする必要があります。Okta で取得するには、**SAML Signing Certificates** に移動し、**Actions** > **Download certificate** を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1b: Edit SAML SSO settings" }

完了したら、ページの下部にある**変更内容を保存**を選択します。

## ステップ 2: Oktaの設定 {#step-2-configure-okta}

Okta で、Braze SAML アプリの **Sign On** タブを選択し、**Edit** をクリックします。

次に、`sso.saml.login` 権限を持つ RelayState API キーを **Default Relay State** フィールドに入力します。

![Okta の Sign On タブにあるデフォルトの RelayState。]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

これらの新しい設定を必ず保存してください。

{% alert tip %}
Braze アカウントユーザーが SAML SSO のみでサインインするようにしたい場合は、**会社の設定**ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#restriction)できます。
{% endalert %}

## ステップ 3: ログイン {#step-3-log-in}

これで、Okta を使用して Braze にログインできるようになります。

![Okta SSO が有効になった Braze ダッシュボードのログイン画面。]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}