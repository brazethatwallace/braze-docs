---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "この記事では、シングルサインオンに OneLogin を使用するように Braze を設定する方法を順に説明します。"

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) は、ユーザーID管理用の包括的なソリューションを提供するクラウドIDプラットフォームです。OneLoginはSAML 2.0を使用してクラウドおよびオンプレミスアプリケーションと連携し、シングルサインオン（SSO）、ユーザープロビジョニング、多要素認証などを実現します。

## 要件 {#requirements}

設定時に、サインオン URL と Assertion Consumer Service (ACS) URL の入力を求められます。

| 要件 | 詳細 |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 欧州連合ドメインの場合、ACS URL は `https://<SUBDOMAIN>.braze.eu/auth/saml/callback` です。 |
| Entity ID | デフォルトでは `braze_dashboard` です。IdP が企業固有の Entity ID を必要とする場合は、**セキュリティ設定**で**カスタム Entity ID** を有効にし、`braze_dashboard_<companyID>` を使用してください。 |
| Braze ドメイン | OneLogin 内で Braze を設定するには、Braze ドメインが必要です。インスタンスが `US-01` の場合、OneLogin ダッシュボードにダッシュボード URL を入力する必要があります。<br><br> たとえば、ダッシュボード URL が `https://dashboard-01.braze.com` の場合、`dashboard-01.braze.com` と入力します。 |
| RelayState API キー | IdP ログインを有効にするには、**設定** > **設定とテスト** > **API と識別子**に移動し、**API キー**タブを開いて、`sso.saml.login` 権限を持つ API キーを作成します。手順については、[RelayState の設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#setting-up-your-relaystate)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## OneLogin における IdP 始動のログイン {#idp-initiated-login-within-onelogin}

### ステップ 1: Braze アプリを構成する {#step-1-configure-the-braze-app}

1. [OneLogin](https://app.onelogin.com/login) にログインします。**Administration** をクリックします。![OneLogin の管理ページ。]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. 上部ナビゲーションバーで **Apps** > **Add Apps** に移動します。「Braze」を検索し、Braze アプリを選択します。![OneLogin での Braze の検索結果。]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Braze アプリを自社に保存します。![Braze アプリを自社に保存する画面。]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. 保存したら **Configuration** に移動し、**Braze Domain** と **RelayState** API キーを追加します。IdP が企業固有のエンティティ ID を要求する場合は、**ACS URL**（`https://<SUBDOMAIN>.braze.com/auth/saml/callback`）とエンティティ ID も [SAML SSO の設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements)から構成してください。![Braze アプリの OneLogin Configuration タブ。]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze は SAML アサーションを[特定の形式]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider)で受け取ることを想定しています。**Parameters** で Braze がサポートする属性があらかじめ入力されているはずです。正しいことを確認してください。![OneLogin での Braze SAML パラメーター。]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. **SSO** タブから、Braze ダッシュボードの設定に必要な**証明書**と **SAML 2.0 Endpoint (HTTP)** をコピーします。![OneLogin の Braze アプリ SSO タブからコピーする証明書。]({% image_buster /assets/img/onelogin_6.jpg %})

### ステップ 2: Braze 内で OneLogin を構成する {#step-2-configure-onelogin-within-braze}

OneLogin 内で Braze の設定が完了すると、ターゲット URL（`SAML 2.0 Endpoint (HTTP)`）と `x.509` 証明書が提供されるので、それを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSO セクションを**オン**に切り替えます。

このページで以下の内容を入力します。

| 要件 | 詳細 |
|---|---|
| `SAML Name` | ログイン画面のボタンテキストとして表示されます。通常は「OneLogin」のような ID プロバイダーの名前です。 |
| `Target URL` | OneLogin から提供される `SAML 2.0 Endpoint (HTTP)` の URL です。|
| `Certificate` | OneLogin から提供される `x.509` PEM エンコードされた証明書です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2: Braze 内で OneLogin を構成する" }

IdP が企業固有のエンティティ ID を要求する場合は、**セキュリティ設定**で**カスタムエンティティ ID** をオンにし、生成された値をコピーして OneLogin のエンティティ ID フィールドに貼り付けます。詳しくは SAML SSO の設定に関する記事の[カスタムエンティティ ID]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#custom-entity-id) を参照してください。

![SAML SSO 設定でトグルが選択された状態。]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Braze アカウントユーザーが SAML SSO でのみサインインするようにしたい場合は、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**から[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)できます。
{% endalert %}

## 次のステップ {#next-steps}

OneLogin SSOが動作するようになったら、以下を行います。

- パスワードログインを無効にする場合は、[SAML SSOのみのログインを強制]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)します。
- [SAMLジャストインタイムプロビジョニングを設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)して、初回のIdPサインイン時にダッシュボードユーザーを自動作成します。
- ユーザーがログインエラーに遭遇した場合は、[SAMLトレースの取得]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#obtaining-a-saml-trace)を使用します。