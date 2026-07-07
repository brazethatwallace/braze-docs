---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "この記事では、シングルサインオンに OneLogin を使用するように Braze を設定する方法を順に説明します。"

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) は、ユーザー ID 管理用の包括的なソリューションを提供するクラウド ID プラットフォームです。OneLoginは SAML 2.0 を使用してクラウドおよびオンプレミスアプリケーションと連携し、シングルサインオン（SSO）、ユーザープロビジョニング、多要素認証などを実現します。

## 要件 {#requirements}

設定時に、サインオン URL と Assertion Consumer Service (ACS) の URL を指定するように求められます。

| 必要条件 | 詳細 |
|---|---|
| Braze ドメイン | OneLogin 内で Braze を設定するには、Braze ドメインが必要です。インスタンスが `US-01` の場合、OneLogin ダッシュボードにダッシュボード URL を入力する必要があります。<br><br> 例えば、ダッシュボードの URL が `https://dashboard-01.braze.com` の場合、`dashboard-01.braze.com` と入力する必要があります。 |
| RelayState API キー | IdP ログインを有効にするには、**設定** > **API キー**に移動し、`sso.saml.login` 権限を持つ API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## OneLogin 内での IdP 開始ログイン {#idp-initiated-login-within-onelogin}

### ステップ 1:Braze アプリを設定する {#step-1-configure-the-braze-app}

1. [OneLogin](https://app.onelogin.com/login) にログインします。**Administration** をクリックします。![OneLoginのAdministrationページ。]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. 上部のナビゲーションバーで **Apps** > **Add Apps** に移動します。「Braze」を検索し、Braze アプリを選択します。![OneLoginにおけるBrazeの検索結果。]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Braze アプリを会社に保存します。![Brazeアプリを会社に保存する画面。]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. 保存したら、**Configuration** に進み、**Braze Domain** と **RelayState** API キーを追加します。![BrazeアプリのOneLogin Configurationタブ。]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Brazeでは SAML アサーションが[特定の形式]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#configure-your-identity-provider)であることが求められます。**Parameters** で、Brazeがサポートする属性が事前に入力されているはずです。正しいことを確認してください。![OneLoginのBraze SAMLパラメーター。]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. **SSO** タブから、Braze ダッシュボードの設定に必要な **Certificate** と **SAML 2.0 Endpoint (HTTP)** をコピーします。![OneLoginのBrazeアプリSSOタブからコピーする証明書。]({% image_buster /assets/img/onelogin_6.jpg %})

### ステップ 2:Braze 内で OneLogin を設定する {#step-2-configure-onelogin-within-braze}

OneLogin 内で Braze を設定すると、ターゲット URL（`SAML 2.0 Endpoint (HTTP)`）と `x.509` 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSO セクションを **ON** に切り替えます。

このページで、以下を入力します。

| 必要条件 | 詳細 |
|---|---|
| `SAML Name` | ログイン画面のボタンテキストとして表示されます。通常は「OneLogin」のような ID プロバイダーの名前です。 |
| `Target URL` | OneLoginが提供する `SAML 2.0 Endpoint (HTTP)` URL です。|
| `Certificate` | OneLoginが提供する `x.509` PEM エンコード証明書です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2: Braze 内で OneLogin を設定する" }

![トグルが選択された SAML SSO 設定。]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Braze アカウントユーザーが SAML SSO のみでサインインするようにしたい場合は、**会社の設定**ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)できます。
{% endalert %}