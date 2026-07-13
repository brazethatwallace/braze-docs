---
nav_title: SAML SSO セットアップ
article_title: SAML SSO セットアップ
page_order: 0
page_type: tutorial
toc_headers: h2
description: "この記事では、BrazeアカウントでSAMLシングルサインオンを有効にする方法について説明します。"

---

# サービスプロバイダー (SP) 主導のログイン {#service-provider-sp-initiated-login}

> この記事では、BrazeアカウントでSAMLシングルサインオンを有効にする方法と、SAMLトレースを取得する方法について説明します。

## 要件 {#requirements}

セットアップ時に、サインオンURLとAssertion Consumer Service (ACS) URLの入力を求められます。

| 要件 | 詳細 |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 欧州連合ドメインの場合、ACS URLは `https://<SUBDOMAIN>.braze.eu/auth/saml/callback` です。<br><br> 一部のIdPでは、Reply URL、Sign-On URL、Audience URL、またはAudience URIと呼ばれることもあります。 |
| Entity ID | `braze_dashboard` |
| RelayState APIキー | **設定** > **APIキー**に移動し、`sso.saml.login` 権限を持つAPIキーを作成してから、生成されたAPIキーをIdP内の `RelayState` パラメーターとして入力します。詳細な手順については、[RelayStateのセットアップ](#setting-up-your-relaystate)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## SAML SSOのセットアップ {#setting-up-saml-sso}

### ステップ1:IDプロバイダーを設定する {#step-1-configure-your-identity-provider}

以下の情報を使用して、IDプロバイダー (IdP) でBrazeをサービスプロバイダー (SP) として設定します。さらに、SAML属性マッピングを設定します。

{% alert important %}
IDプロバイダーとしてOktaを使用する予定の場合は、[Oktaサイト](https://www.okta.com/integrations/braze/)にある事前構築済みの統合を使用してください。
{% endalert %}

| SAML属性 | 必須？ | 受け入れ可能なSAML属性 |
|---|---|---|
| `email` | 必須 | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | オプション | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | オプション | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 1: Configure your identity provider" }

{% alert note %}
BrazeはSAMLアサーションで `email` のみを必要とします。
{% endalert %}

### ステップ2:Brazeを設定する {#step-2-configure-braze}

IDプロバイダーでBrazeの設定が完了すると、IDプロバイダーからターゲットURLと `x.509` 証明書が提供されます。これらをBrazeアカウントに入力します。

アカウントマネージャーがアカウントのSAML SSOを有効にした後、**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSOセクションを**オン**に切り替えます。

同じページで以下を入力します:

| 要件 | 詳細 |
|---|---|
| SAML名 | ログイン画面のボタンテキストとして表示されます。<br>通常、「Okta」のようなIDプロバイダーの名前です。 |
| ターゲットURL | IdP内でBrazeを設定した後に提供されます。<br>一部のIdPでは、SSO URLまたはSAML 2.0エンドポイントと呼ばれます。 |
| 証明書 | IDプロバイダーから提供される `x.509` 証明書です。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure Braze" }

ダッシュボードに追加する際、`x.509` 証明書が以下の形式に従っていることを確認してください:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![SAML SSO設定のトグルが選択された状態。]({% image_buster /assets/img/samlsso.png %})

### ステップ3:Brazeにサインインする {#step-3-sign-into-braze}

セキュリティ設定を保存してログアウトします。その後、IDプロバイダーを使用して再度サインインします。

## RelayStateのセットアップ {#setting-up-your-relaystate}

1. Brazeで、**設定** > **APIと識別子**に移動します。
2. **APIキー**タブで、**APIキーを作成**ボタンを選択します。
3. **APIキー名**フィールドにキーの名前を入力します。
4. **権限**の下にある**SSO**ドロップダウンを展開し、**sso.saml.login**にチェックを入れます。
5. **APIキーを作成**を選択します。
6. **APIキー**タブで、作成したAPIキーの横にある識別子をコピーします。
7. RelayState APIキーをIdPのRelayStateに貼り付けます（IdPによっては「Relay State」または「Default Relay State」と表示される場合があります）。

## SSOの動作 {#sso-behavior}

SSOの使用を選択したメンバーは、以前のようにパスワードを使用してログインできなくなります。パスワードを引き続き使用するユーザーは、以下の設定で制限されない限り、パスワードでログインできます。

## 制限 {#restriction}

組織のメンバーがGoogle SSOまたはSAML SSOのみでサインインするように制限できます。制限を有効にするには、**セキュリティ設定**に移動し、**Enforce Google SSO only login**または**Enforce custom SAML SSO only login**を選択します。

![「認証ルール」セクションのセットアップ例。最小パスワード長は8文字、パスワードの再利用可能回数は3回です。パスワードは180日後に期限切れとなり、ユーザーは1,440分の非アクティブ後にログアウトされます。]({% image_buster /assets/img/sso3.png %})

制限を有効にすると、以前パスワードでログインしていた場合でも、会社のBrazeユーザーはパスワードを使用してログインできなくなります。

{% alert important %}
SSOが強制された後、SSO認証が失敗した場合のフォールバックオプションはありません。SSOの強制を有効にする前に、SSO設定が正しいこと、すべての証明書が最新で更新されていること、セキュリティ設定が適切に管理されていることを確認して、ログインの問題を防いでください。
{% endalert %}

## SAMLトレースの取得 {#obtaining-a-saml-trace}

SSOに関連するログインの問題が発生した場合、SAMLトレースを取得することで、SAMLリクエストで送信される内容を特定し、SSO接続のトラブルシューティングに役立てることができます。

### 前提条件 {#prerequisites}

SAMLトレースを実行するには、SAMLトレーサーが必要です。ブラウザに応じて、以下の2つのオプションがあります:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### ステップ1:SAMLトレーサーを開く {#step-1-open-the-saml-tracer}

ブラウザのナビゲーションバーからSAMLトレーサーを選択します。**Pause**が選択されていないことを確認してください。選択されていると、SAMLトレーサーがSAMLリクエストで送信される内容をキャプチャできなくなります。SAMLトレーサーを開くと、トレースが表示されます。

![Google Chrome用のSAMLトレーサー。]({% image_buster /assets/img/saml_tracer_example.png %})

### ステップ2:SSOを使用してBrazeにサインインする {#step-2-sign-into-braze-using-sso}

Brazeダッシュボードに移動し、SSOを使用してサインインを試みます。エラーが発生した場合は、SAMLトレーサーを開いて再試行してください。`https://dashboard-XX.braze.com/auth/saml/callback` のようなURLとオレンジ色のSAMLタグを含む行がある場合、SAMLトレースが正常に収集されています。

### ステップ3:エクスポートしてBrazeに送信する {#step-3-export-and-send-to-braze}

**Export**を選択します。**Select cookie-filter profile**で**None**を選択します。次に、**Export**を選択します。これによりJSONファイルが生成され、Brazeサポートに送信してさらなるトラブルシューティングを行うことができます。

![「None」オプションが選択された「Export SAML-trace preferences」メニュー。]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## トラブルシューティング {#troubleshooting}

### ユーザーのメールアドレスは正しく設定されていますか？ {#is-the-users-email-address-correctly-set-up}

`ERROR_CODE_SSO_INVALID_EMAIL` エラーが表示される場合、ユーザーのメールアドレスが無効です。SAMLトレースで `saml2:Attribute Name="email"` フィールドが、ユーザーがログインに使用しているメールアドレスと一致していることを確認してください。Microsoft Entra ID（旧Azure Active Directory）を使用している場合、属性マッピングは `email = user.userprincipalname` です。

メールアドレスは大文字と小文字が区別され、IDプロバイダー（Okta、OneLogin、Microsoft Entra IDなど）で設定されたものを含め、Brazeで設定されたものと完全に一致する必要があります。

ユーザーのメールアドレスに問題があることを示すその他のエラー:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: ユーザーのメールアドレスがダッシュボード内に存在しません。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: ユーザーのメールアドレスが空白であるか、正しく設定されていません。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` または `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: ユーザーのメールアドレスがSSOのセットアップに使用されたものと一致しません。

### 有効なSAML証明書（x.509証明書）がありますか？ {#do-you-have-a-valid-saml-certificate-x509-certificate}

[このSAML検証ツール](https://www.samltool.com/validate_response.php)を使用してSAML証明書を検証できます。期限切れのSAML証明書も無効なSAML証明書であることに注意してください。

### 正しいSAML証明書（x.509証明書）をアップロードしましたか？ {#did-you-upload-a-correct-saml-certificate-x509-certificate}

SAMLトレースの `ds:X509Certificate` セクションにある証明書が、Brazeにアップロードしたものと一致していることを確認してください。これには `-----BEGIN CERTIFICATE-----` ヘッダーと `-----END CERTIFICATE-----` フッターは含まれません。

### SAML証明書（x.509証明書）を誤入力またはフォーマットミスしていませんか？ {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Brazeダッシュボードに送信した証明書に空白や余分な文字がないことを確認してください。

Brazeに証明書を入力する際は、Privacy Enhanced Mail (PEM) エンコードされ、正しくフォーマットされている必要があります（`-----BEGIN CERTIFICATE-----` ヘッダーと `-----END CERTIFICATE-----` フッターを含む）。

以下は正しくフォーマットされた証明書の例です:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ユーザーのセッショントークンは有効ですか？ {#is-the-users-session-token-valid}

影響を受けるユーザーに[ブラウザのキャッシュとCookieをクリア](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser)してもらい、再度SAML SSOでログインを試みてください。

### RelayStateを設定しましたか？ {#did-you-set-your-relaystate}

`ERROR_CODE_SSO_INVALID_RELAY_STATE` エラーが表示される場合、RelayStateが正しく設定されていないか、存在しない可能性があります。まだ設定していない場合は、IdP管理システムでRelayStateを設定する必要があります。手順については、[RelayStateのセットアップ](#setting-up-your-relaystate)を参照してください。

### SSOサインインに成功してもBrazeのログインページに戻されますか？ {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

これはRelayStateが正しく設定されていない場合に発生することがあります。APIキー（**設定** > **APIキー**）をIdPサインイン用に作成し、そのAPIキーをIdPの `RelayState` パラメーターとして設定したことを確認してください。RelayStateは、サインインする会社アカウントを識別します。手順については、[RelayStateのセットアップ](#setting-up-your-relaystate)を参照してください。

それでもサインインできない場合は、可能であればSAMLトレースを添えて[Brazeサポートに連絡]({{site.baseurl}}/braze_support)してください。トレースのキャプチャ方法については、[SAMLトレースの取得](#obtaining-a-saml-trace)を参照してください。

### ユーザーがOktaとBrazeの間でサインインループに陥っていませんか？ {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Okta SSOとBrazeダッシュボードの間を循環してサインインできないユーザーがいる場合、Oktaに移動してSSO URLの送信先を[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)（例: `https://dashboard-07.braze.com`）に設定する必要があります。

別のIdPを使用している場合は、会社が正しいSAMLまたはx.509証明書をBrazeにアップロードしたかどうかを確認してください。

### 手動統合を使用していますか？ {#are-you-using-a-manual-integration}

会社がIdPのアプリストアからBrazeアプリをダウンロードしていない場合は、事前構築済みの統合をダウンロードする必要があります。例えば、IdPがOktaの場合は、[統合ページ](https://www.okta.com/integrations/braze/)からBrazeアプリをダウンロードします。

## Google SSO

会社がカスタムSAMLの代わりにGoogle SSOを使用している場合は、BrazeアカウントマネージャーにワークスペースのGoogle SSOの有効化を依頼してください。有効化された後、**セキュリティ設定**に移動し、**Enforce Google SSO only login**を選択して、すべての会社ユーザーにGoogle認証を要求します。

Google SSOの強制が有効になると、ユーザーはGoogle認証でサインインする必要があり、Brazeパスワードは使用できなくなります。各ユーザーは、Brazeダッシュボードのメールアドレスと一致するGoogleアカウントでサインインする必要があります。サインイン時に別のGoogleアカウントを選択した場合、Brazeは認証の試行を拒否します。

### Google SSOサインインのトラブルシューティング {#troubleshooting-google-sso-sign-in}

一部のユーザーがGoogle SSOでサインインできない場合は、以下を確認してください:

- ユーザーのGoogleアカウントのメールアドレスがBrazeダッシュボードのメールアドレスと完全に一致していること。
- ユーザーが会社のメールアドレスに対応するGoogleアカウントにアクセスできること。
- ユーザーがBrazeで停止されていないこと（**設定** > **会社ユーザー**）。

## 次のステップ {#next-steps}

SAML SSOを設定した後、以下のことができます:

- セキュリティ設定で[SSOのみのログインを強制]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#restriction)し、ユーザーがパスワードでログインすることを制限します。
- [SAMLジャストインタイムプロビジョニングを設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)して、新しいユーザーが初回のSSOサインイン時に自動的にBrazeアカウントを作成できるようにします。