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

セットアップ時に、サインオン URL と Assertion Consumer Service（ACS）URL の入力を求められます。

| 要件 | 詳細 |
|---|---|
| Assertion Consumer Service（ACS）URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 欧州連合ドメインの場合、ACS URL は `https://<SUBDOMAIN>.braze.eu/auth/saml/callback` です。 <br><br> 一部の IdP では、Reply URL、Sign-On URL、Audience URL、または Audience URI と呼ばれることもあります。 |
| Entity ID | デフォルトでは `braze_dashboard` です。IdP が会社固有の Entity ID を必要とする場合は、**セキュリティ設定**で**カスタム Entity ID** を有効にし、`braze_dashboard_<companyID>` を使用します。 |
| RelayState API キー | **設定** > **セットアップとテスト** > **API と識別子**に移動し、**API キー**タブを開いて、`sso.saml.login` 権限を持つ API キーを作成します。生成された API キーを IdP 内で `RelayState` パラメーターとして入力します。詳細な手順については、[RelayState の設定](#setting-up-your-relaystate)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## SAML SSOの設定 {#setting-up-saml-sso}

### ステップ1：IDプロバイダーの設定 {#step-1-configure-your-identity-provider}

以下の情報を使用して、IDプロバイダー（IdP）でBrazeをサービスプロバイダー（SP）として設定します。また、SAML属性マッピングも設定してください。

{% alert important %}
IDプロバイダーとしてOktaを使用する予定がある場合は、[Oktaサイト](https://www.okta.com/integrations/braze/)にある事前構築済みのインテグレーションを使用してください。
{% endalert %}

| SAML属性 | 必須？ | 対応するSAML属性 |
|---|---|---|
|`email` | 必須 | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | 任意 | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | 任意 | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ1：IDプロバイダーの設定" }

{% alert note %}
BrazeのSAMLアサーションでは`email`のみが必須です。
{% endalert %}

### ステップ2：Brazeの設定 {#step-2-configure-braze}

IDプロバイダーでBrazeの設定を完了すると、IDプロバイダーからターゲットURLと`x.509`証明書が提供されます。これらをBrazeアカウントに入力します。

アカウントマネージャーがアカウントのSAML SSOを有効にしたら、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSOセクションを**オン**に切り替えます。

同じページで以下の情報を入力します：

| 要件 | 詳細 |
|---|---|
| SAML名 | ログイン画面のボタンテキストとして表示されます。<br>通常、「Okta」のようにIDプロバイダーの名前を入力します。 |
| ターゲットURL | IdP内でBrazeを設定した後に提供されます。<br>一部のIdPでは、これをSSO URLまたはSAML 2.0エンドポイントと呼びます。 |
| 証明書 | IDプロバイダーから提供される`x.509`証明書です。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2：Brazeの設定" }

### カスタムエンティティID {#custom-entity-id}

デフォルトでは、BrazeはエンティティID（一部のIdPではAudienceまたはAudience URIとも呼ばれます）として`braze_dashboard`を使用します。IdPで会社固有のエンティティIDが必要な場合は、以下の手順に従ってください：

1. **セキュリティ設定**で、**カスタムエンティティID**をオンにします。
2. 生成されたエンティティID（`braze_dashboard_<companyID>`）をコピーします。
3. その値をIdPのエンティティID、Audience、またはAudience URIフィールドに貼り付けます。
4. サインインをテストする前に、BrazeとIdPの両方で変更を保存します。

{% alert important %}
エンティティIDがBrazeとIdPの両方で一致するまで、ユーザーはサインインできません。カスタムエンティティIDを使用するには、IDプロバイダーで追加の設定が必要です。
{% endalert %}

`x.509`証明書をダッシュボードに追加する際は、以下の形式に従ってください：

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![トグルが選択された状態のSAML SSO設定。]({% image_buster /assets/img/samlsso.png %})

### ステップ3：Brazeにサインイン {#step-3-sign-into-braze}

セキュリティ設定を保存してログアウトします。その後、IDプロバイダーを使用して再度サインインします。

## カスタムエンティティIDの使用 {#using-a-custom-entity-id}

デフォルトでは、すべてのBrazeダッシュボードは共有エンティティID `braze_dashboard` を使用します。カスタムエンティティIDを使用すると、ダッシュボードに一意の識別子が付与されるため、IDプロバイダーがサインインリクエストがこの特定のダッシュボード向けであることを検証できます。これは、同一のIDプロバイダーで複数のBraze企業にわたってSAML SSOを設定する場合に便利です。

カスタムエンティティIDの使用は任意です。有効にしない場合、ダッシュボードは引き続き `braze_dashboard` を使用します。

{% alert warning %}
事前構築済みの[Braze Oktaマーケットプレイスアプリ](https://www.okta.com/integrations/braze/)は共有エンティティID `braze_dashboard` を強制しており、カスタムエンティティIDとは互換性がありません。Braze OktaマーケットプレイスアプリでSAML SSOをすでに設定している場合、カスタムSAMLアプリを使ってOktaのエンティティIDフィールドを更新せずにカスタムエンティティIDを有効にすると、サインインが中断し、ユーザーがダッシュボードからロックアウトされる可能性があります。OktaでカスタムエンティティIDを使用するには、代わりにカスタムSAMLアプリを設定してください。
{% endalert %}

### ステップ1：カスタムエンティティIDを有効にする {#step-1-turn-on-the-custom-entity-id}

**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAMLシングルサインオンセクションを開きます。**カスタムエンティティID**トグルをオンにします。Brazeは `braze_dashboard_<COMPANY_ID>` の形式でダッシュボードの一意のエンティティIDを生成します。**カスタムエンティティID**オプションが表示されない場合は、Brazeアカウントマネージャーにお問い合わせください。

### ステップ2：IDプロバイダーを更新する {#step-2-update-your-identity-provider}

生成されたエンティティIDをコピーし、IDプロバイダーのBrazeアプリケーションのエンティティIDフィールドに貼り付けます。プロバイダーによっては、このフィールドは**Entity ID**、**Audience**、または**Audience URI**と表示される場合があります。

{% alert important %}
エンティティIDはBrazeとIDプロバイダーの両方で一致している必要があります。両方が同じ値を使用するまで、ユーザーはSAML SSOでサインインできません。ユーザーがロックアウトされないよう、このページを保存する前にIDプロバイダーを更新してください。
{% endalert %}

### ステップ3：保存してテストする {#step-3-save-and-test}

セキュリティ設定を保存し、ログアウトしてから、IDプロバイダーを通じて再度サインインして、カスタムエンティティIDでサインインが機能することを確認します。

## RelayStateの設定 {#setting-up-your-relaystate}

1. Brazeで、**設定** > **セットアップとテスト** > **APIと識別子**に移動します。
2. **APIキー**タブで、**APIキーを作成**ボタンを選択します。
3. **APIキー名**フィールドに、キーの名前を入力します。
4. **権限**の下にある**SSO**ドロップダウンを展開し、**sso.saml.login**にチェックを入れます。
5. **APIキーを作成**を選択します。
6. **APIキー**タブで、作成したAPIキーの横にある識別子をコピーします。
7. RelayState APIキーをIdPのRelayStateに貼り付けます（IdPによっては「Relay State」または「Default Relay State」と表示される場合があります）。

## IdP 主導のログイン {#idp-initiated-login}

一部の ID プロバイダーは IdP 主導のログインをサポートしており、ユーザーは Braze のログインページではなく IdP ポータルからログインを開始できます。IdP 主導のログインには、有効な RelayState API キーと正しい ACS URL の設定が必要です。プロバイダー別の設定ガイド:

- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)

{% alert note %}
Microsoft Entra SSO の IdP 主導のログインでは、**Sign-On URL** フィールドを空白のままにする必要があります。詳細については、[Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) を参照してください。
{% endalert %}

## SSOの動作 {#sso-behavior}

SSOの使用を選択したメンバーは、パスワードを使用できなくなります。パスワードを引き続き使用するユーザーは、以下の設定で制限されない限り、そのまま使用できます。

## 制限 {#restriction}

組織のメンバーが Google SSO または SAML SSO のいずれかのみでサインインするように制限できます。制限を有効にするには、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**Google SSO のみのログインを強制する**または**カスタム SAML SSO のみのログインを強制する**を選択します。

![「認証ルール」セクションの設定例。最小パスワード長は8文字、パスワードの再利用は3回までに設定されています。パスワードは180日後に期限切れとなり、ユーザーは1,440分間操作がない場合にログアウトされます。]({% image_buster /assets/img/sso3.png %})

制限を有効にすると、組織の Braze ユーザーは、以前にパスワードでログインしたことがあっても、パスワードを使用してログインできなくなります。

{% alert important %}
SSO が強制された後、SSO 認証に失敗した場合のフォールバックオプションはありません。SSO の強制を有効にする前に、SSO の構成が正しいこと、すべての証明書が最新で更新されていること、およびセキュリティ設定が適切に管理されていることを確認して、ログインの問題を防止してください。
{% endalert %}

## SAMLトレースの取得 {#obtaining-a-saml-trace}

SSOに関連するログインの問題が発生した場合、SAMLトレースを取得すると、SAMLリクエストで送信される内容を確認することで、SSO接続のトラブルシューティングに役立ちます。

### 前提条件 {#prerequisites}

SAMLトレースを実行するには、SAMLトレーサーが必要です。お使いのブラウザに応じて、次の2つのオプションがあります。

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### ステップ1:SAMLトレーサーを開く {#step-1-open-the-saml-tracer}

ブラウザのナビゲーションバーからSAMLトレーサーを選択します。**Pause**が選択されていないことを確認してください。選択されていると、SAMLトレーサーがSAMLリクエストで送信される内容をキャプチャできなくなります。SAMLトレーサーを開くと、トレースが表示されます。

![Google Chrome用のSAMLトレーサー。]({% image_buster /assets/img/saml_tracer_example.png %})

### ステップ2:SSOを使用してBrazeにサインインする {#step-2-sign-into-braze-using-sso}

Brazeダッシュボードにアクセスし、SSOを使用してサインインを試みます。エラーが発生した場合は、SAMLトレーサーを開いて再度お試しください。`https://dashboard-XX.braze.com/auth/saml/callback`のようなURLとオレンジ色のSAMLタグが表示された行がある場合、SAMLトレースが正常に取得されています。

### ステップ3:エクスポートしてBrazeに送信する {#step-3-export-and-send-to-braze}

**Export**を選択します。**Select cookie-filter profile**で**None**を選択します。次に**Export**を選択します。これにより、トラブルシューティングのためにBrazeサポートに送信できるJSONファイルが生成されます。

![「Export SAML-trace preferences」メニューで「None」オプションが選択されている状態。]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## トラブルシューティング {#troubleshooting}

### ユーザーのメールアドレスは正しく設定されていますか？ {#is-the-users-email-address-correctly-set-up}

`ERROR_CODE_SSO_INVALID_EMAIL` というエラーが発生している場合、ユーザーのメールアドレスが無効です。SAMLトレースで `saml2:Attribute Name="email"` フィールドが、ユーザーがログインに使用しているメールアドレスと一致しているか確認してください。Microsoft Entra ID（旧 Azure Active Directory）を使用している場合、属性マッピングは `email = user.userprincipalname` です。

メールアドレスは大文字と小文字が区別され、IDプロバイダー（Okta、OneLogin、Microsoft Entra IDなど）で設定されたものを含め、Brazeで設定されたものと完全に一致する必要があります。

ユーザーのメールアドレスに問題があることを示すその他のエラーには、次のものがあります：
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`：ユーザーのメールアドレスがダッシュボード内に存在しません。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`：ユーザーのメールアドレスが空白であるか、その他の設定ミスがあります。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` または `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`：ユーザーのメールアドレスがSSOの設定に使用されたものと一致しません。

### 有効なSAML証明書（x.509証明書）をお持ちですか？ {#do-you-have-a-valid-saml-certificate-x509-certificate}

[このSAML検証ツール](https://www.samltool.com/validate_response.php)を使用してSAML証明書を検証できます。期限切れのSAML証明書も無効なSAML証明書であることにご注意ください。

### 正しいSAML証明書（x.509証明書）をアップロードしましたか？ {#did-you-upload-a-correct-saml-certificate-x509-certificate}

SAMLトレースの `ds:X509Certificate` セクションの証明書が、Brazeにアップロードしたものと一致していることを確認してください。これには `-----BEGIN CERTIFICATE-----` ヘッダーと `-----END CERTIFICATE-----` フッターは含まれません。

### SAML証明書（x.509証明書）に誤字やフォーマットの不備はありませんか？ {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Brazeダッシュボードに送信した証明書に、空白や余分な文字がないことを確認してください。

Brazeに証明書を入力する際は、Privacy Enhanced Mail（PEM）エンコードで正しくフォーマットされている必要があります（`-----BEGIN CERTIFICATE-----` ヘッダーと `-----END CERTIFICATE-----` フッターを含む）。

正しくフォーマットされた証明書の例を次に示します：

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ユーザーのセッショントークンは有効ですか？ {#is-the-users-session-token-valid}

影響を受けたユーザーに[ブラウザのキャッシュとCookieをクリア](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser)してもらい、SAML SSOで再度ログインを試してもらってください。

### RelayStateは設定していますか？ {#did-you-set-your-relaystate}

`ERROR_CODE_SSO_INVALID_RELAY_STATE` というエラーが発生している場合、RelayStateの設定が正しくないか、存在していない可能性があります。まだ設定していない場合は、IdP管理システムでRelayStateを設定する必要があります。手順については、[RelayStateの設定](#setting-up-your-relaystate)を参照してください。

### SSOログインに成功してもBrazeのログインページに戻ってしまいますか？ {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

RelayStateが正しく設定されていない場合に、この問題が発生することがあります。IdPログイン用のAPIキーを（**設定** > **セットアップとテスト** > **APIと識別子**で）作成し、そのAPIキーをIdPの `RelayState` パラメーターとして設定したことを確認してください。RelayStateは、サインインする企業アカウントを識別するものです。詳しい手順については、[RelayStateの設定](#setting-up-your-relaystate)を参照してください。

それでもサインインできない場合は、可能であればSAMLトレースを添えて[Brazeサポートに連絡]({{site.baseurl}}/braze_support)してください。トレースの取得方法については、[SAMLトレースの取得](#obtaining-a-saml-trace)を参照してください。

### ユーザーがOktaとBrazeの間でサインインループに陥っていますか？ {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

ユーザーがOkta SSOとBrazeダッシュボードの間を循環してサインインできない場合は、Oktaに移動してSSOのURL宛先を[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)（例：`https://dashboard-07.braze.com`）に設定する必要があります。

他のIdPを使用している場合は、正しいSAMLまたはx.509証明書がBrazeにアップロードされているか確認してください。

### 手動インテグレーションを使用していますか？ {#are-you-using-a-manual-integration}

IdPのアプリストアからBrazeアプリをダウンロードしていない場合は、事前構築されたインテグレーションをダウンロードする必要があります。たとえば、OktaがIdPの場合は、Oktaの[インテグレーションページ](https://www.okta.com/integrations/braze/)からBrazeアプリをダウンロードします。

## Google SSO

会社がカスタムSAMLの代わりにGoogle SSOを使用している場合は、BrazeアカウントマネージャーにワークスペースのGoogle SSOの有効化を依頼してください。有効化された後、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定**に移動し、**Enforce Google SSO only login**を選択して、すべての会社ユーザーにGoogle認証を要求します。

Google SSOの強制が有効になると、ユーザーはGoogle認証でサインインする必要があり、Brazeパスワードは使用できなくなります。各ユーザーは、Brazeダッシュボードのメールアドレスと一致するGoogleアカウントでサインインする必要があります。サインイン時に別のGoogleアカウントを選択した場合、Brazeは認証の試行を拒否します。

### Google SSOサインインのトラブルシューティング {#troubleshooting-google-sso-sign-in}

一部のユーザーがGoogle SSOでサインインできない場合は、以下を確認してください:

- ユーザーのGoogleアカウントのメールアドレスがBrazeダッシュボードのメールアドレスと完全に一致していること。
- ユーザーが会社のメールアドレスに対応するGoogleアカウントにアクセスできること。
- ユーザーがBrazeで停止されていないこと（**設定** > **会社ユーザー**）。

## 次のステップ {#next-steps}

SAML SSOを設定した後、以下のことができます。

- セキュリティ設定で[SSOのみのログインを強制]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication)し、ユーザーがパスワードでログインすることを制限します。
- [SAMLジャストインタイムプロビジョニングを設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)し、新しいユーザーが初回のSSOサインイン時にBrazeアカウントを自動的に作成できるようにします。