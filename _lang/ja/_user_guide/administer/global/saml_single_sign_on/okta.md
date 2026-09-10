---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "この記事では、シングルサインオンにOktaを使用するようにBrazeを設定する方法を順に説明します。"

---

# Okta

> Oktaは、あらゆるデバイス上のあらゆるアプリケーションとあらゆるユーザーを接続します。Oktaはクラウド向けに構築されたエンタープライズクラスのID管理サービスですが、多くのオンプレミスアプリケーションと互換性があります。Oktaを使用すると、ITチームはあらゆる従業員によるあらゆるアプリケーションやデバイスへのアクセスを管理できます。

{% alert note %}
ビルド済みのBraze Oktaマーケットプレイスアプリは、共有エンティティID `braze_dashboard` を使用します。このダッシュボード用に一意のエンティティIDが必要な場合（たとえば、Oktaを通じて複数のBrazeダッシュボードを接続する場合など）は、マーケットプレイスアプリの代わりにカスタムSAMLアプリを設定し、[カスタムエンティティIDの使用]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id)の手順に従ってください。
{% endalert %}

## 要件 {#requirements}

| 要件 | 詳細 |
| ----------- | ------- |
| アカウントでOktaが有効であること | Brazeアカウントマネージャーに連絡して、アカウントでこの機能を有効にしてもらってください。 |
| Okta管理者権限 | Oktaを設定する前に、管理者権限があることを確認してください。 |
| Braze管理者権限 | Oktaを設定する前に、管理者権限があることを確認してください。 |
| RelayState APIキー | IdPログインを有効にするには、**設定** > **設定とテスト** > **APIと識別子**に移動し、**APIキー**タブを開いて、`sso.saml.login`権限を持つAPIキーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## ステップ1: Brazeを設定する {#step-1-configure-braze}

### ステップ1a: Brazeのセキュリティ設定に移動する {#step-1a-navigate-to-security-settings-in-braze}

アカウントマネージャーがアカウントのSAML SSOを有効にしたら、**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSOセクションを**オン**に切り替えます。

![セキュリティ設定ページでOkta SAML SSOが有効化されている画面。]({% image_buster/assets/img/Okta/okta1.png %})

### ステップ1b: SAML SSO設定を編集する {#step-1b-edit-saml-sso-settings}

Okta管理者ダッシュボードから、OktaがターゲットURL（ログインURL）と`x.509`証明書を提供します。これらをBrazeアカウントの**セキュリティ設定**ページに入力する必要があります。

![ステップ1b: SAML SSO設定の編集に関するスクリーンショット。]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| 要件 | 詳細 |
|---|---|
| `SAML Name` | ログイン画面のボタンテキストとして表示されます。通常はIDプロバイダーの名前です。例：「Okta」。 |
| `Target URL` | Okta管理者ダッシュボードが提供するログインURLです。**Applications** > 対象のアプリケーション > **General**タブ > **App Embed Link** > **Embed Link**に移動して確認してください。 |
| `Certificate` | `x.509` PEMエンコード証明書はIDプロバイダーから提供されます。コピーしてこのフィールドに貼り付ける必要があります。Oktaで取得するには、**SAML Signing Certificates**に移動し、**Actions** > **Download certificate**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1b: SAML SSO設定を編集する" }

完了したら、ページ下部の**Save Changes**を選択します。

{% alert note %}
IDプロバイダーが会社固有のSAMLエンティティIDを必要とし、アカウントがそれをサポートしている場合は、**セキュリティ設定**で**カスタムエンティティID**を有効にし、Oktaで`braze_dashboard_<companyID>`を設定してください。デフォルトのエンティティIDは`braze_dashboard`です。**カスタムエンティティID**設定はすべての会社で利用できるわけではありません。詳細については、[SAML SSOの設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements)を参照してください。
{% endalert %}

## ステップ2：Oktaを設定する {#step-2-configure-okta}

Oktaで、Braze SAMLアプリの**サインオン**タブを選択し、**編集**をクリックします。

次に、`sso.saml.login` 権限を持つRelayState APIキーを**デフォルトリレーステート**フィールドに入力します。

![サインオンタブにおけるOktaのデフォルトリレーステート。]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

これらの新しい設定を必ず保存してください。

{% alert tip %}
Brazeアカウントのユーザーに対してSAML SSOのみでのサインインを求める場合は、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**から[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)できます。
{% endalert %}

## ステップ3: ログイン {#step-3-log-in}

これで、Oktaを使用してBrazeにログインできるようになります。

![OktaのSSOが有効になっているBrazeダッシュボードのログイン画面。]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}