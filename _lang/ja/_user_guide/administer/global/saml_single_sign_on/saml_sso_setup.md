---
nav_title: SAML SSO セットアップ
article_title: SAML SSO セットアップ
page_order: 0
page_type: tutorial
toc_headers: h2
description: "この記事では、Braze アカウントで SAML シングルサインオンを有効にする方法について説明します。"

---

# サービスプロバイダー (SP) 主導のログイン

> この記事では、Braze アカウントで SAML シングルサインオンを有効にする方法と、SAML トレースを取得する方法について説明します。

## 要件

セットアップ時に、サインオン URL と Assertion Consumer Service (ACS) URL の入力を求められます。

| 要件 | 詳細 |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 欧州連合ドメインの場合、ACS URL は `https://<SUBDOMAIN>.braze.eu/auth/saml/callback` です。<br><br> 一部の IdP では、Reply URL、Sign-On URL、Audience URL、または Audience URI と呼ばれることもあります。 |
| Entity ID | `braze_dashboard` |
| RelayState API キー | **設定** > **API キー**に移動し、`sso.saml.login` 権限を持つ API キーを作成してから、生成された API キーを IdP 内の `RelayState` パラメーターとして入力します。詳細な手順については、[RelayState のセットアップ](#setting-up-your-relaystate)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SAML SSO のセットアップ

### ステップ 1: ID プロバイダーを設定する

以下の情報を使用して、ID プロバイダー (IdP) で Braze をサービスプロバイダー (SP) として設定します。さらに、SAML 属性マッピングを設定します。

{% alert important %}
ID プロバイダーとして Okta を使用する予定の場合は、[Okta サイト](https://www.okta.com/integrations/braze/)にある事前構築済みの統合を使用してください。
{% endalert %}

| SAML 属性 | 必須？ | 受け入れ可能な SAML 属性 |
|---|---|---|
|`email` | 必須 | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | オプション | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | オプション | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze は SAML アサーションで `email` のみを必要とします。
{% endalert %}

### ステップ 2: Braze を設定する

ID プロバイダーで Braze の設定が完了すると、ID プロバイダーからターゲット URL と `x.509` 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にした後、**設定** > **管理者設定** > **セキュリティ設定**に移動し、SAML SSO セクションを**オン**に切り替えます。

同じページで以下を入力します:

| 要件 | 詳細 |
|---|---|
| SAML 名 | ログイン画面のボタンテキストとして表示されます。<br>通常、「Okta」のような ID プロバイダーの名前です。 |
| ターゲット URL | IdP 内で Braze を設定した後に提供されます。<br> 一部の IdP では、SSO URL または SAML 2.0 エンドポイントと呼ばれます。 |
| 証明書 | ID プロバイダーから提供される `x.509` 証明書です。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ダッシュボードに追加する際、`x.509` 証明書が以下の形式に従っていることを確認してください:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![SAML SSO 設定のトグルが選択された状態。]({% image_buster /assets/img/samlsso.png %})

### ステップ 3: Braze にサインインする

セキュリティ設定を保存してログアウトします。その後、ID プロバイダーを使用して再度サインインします。

![SSO が有効になったダッシュボードのログイン画面]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## RelayState のセットアップ {#setting-up-your-relaystate}

1. Braze で、**設定** > **API キー**に移動します。
2. **API キー**タブで、**API キーを作成**ボタンを選択します。
3. **API キー名**フィールドにキーの名前を入力します。
4. **権限**の下にある **SSO** ドロップダウンを展開し、**sso.saml.login** にチェックを入れます。<br><br>![sso.saml.login にチェックが入った「権限」セクション。]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. **API キーを作成**を選択します。
6. **API キー**タブで、作成した API キーの横にある識別子をコピーします。
7. RelayState API キーを IdP の RelayState に貼り付けます（IdP によっては「Relay State」または「Default Relay State」と表示される場合があります）。

## SSO の動作

SSO の使用を選択したメンバーは、以前のようにパスワードを使用してログインできなくなります。パスワードを引き続き使用するユーザーは、以下の設定で制限されない限り、パスワードでログインできます。

## 制限

組織のメンバーが Google SSO または SAML SSO のみでサインインするように制限できます。制限を有効にするには、**セキュリティ設定**に移動し、**Google SSO のみのログインを強制**または**カスタム SAML SSO のみのログインを強制**を選択します。

![「認証ルール」セクションのセットアップ例。最小パスワード長は8文字、パスワードの再利用可能回数は3回です。パスワードは180日後に期限切れとなり、ユーザーは1,440分の非アクティブ後にログアウトされます。]({% image_buster /assets/img/sso3.png %})

制限を有効にすると、以前パスワードでログインしていた場合でも、会社の Braze ユーザーはパスワードを使用してログインできなくなります。

## SAML トレースの取得

SSO に関連するログインの問題が発生した場合、SAML トレースを取得することで、SAML リクエストで送信される内容を特定し、SSO 接続のトラブルシューティングに役立てることができます。

### 前提条件

SAML トレースを実行するには、SAML トレーサーが必要です。ブラウザに応じて、以下の2つのオプションがあります:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### ステップ 1: SAML トレーサーを開く

ブラウザのナビゲーションバーから SAML トレーサーを選択します。**Pause** が選択されていないことを確認してください。選択されていると、SAML トレーサーが SAML リクエストで送信される内容をキャプチャできなくなります。SAML トレーサーを開くと、トレースが表示されます。

![Google Chrome 用の SAML トレーサー。]({% image_buster /assets/img/saml_tracer_example.png %})

### ステップ 2: SSO を使用して Braze にサインインする

Braze ダッシュボードに移動し、SSO を使用してサインインを試みます。エラーが発生した場合は、SAML トレーサーを開いて再試行してください。`https://dashboard-XX.braze.com/auth/saml/callback` のような URL とオレンジ色の SAML タグを含む行がある場合、SAML トレースが正常に収集されています。

### ステップ 3: エクスポートして Braze に送信する

**Export** を選択します。**Select cookie-filter profile** で **None** を選択します。次に、**Export** を選択します。これにより JSON ファイルが生成され、Braze サポートに送信してさらなるトラブルシューティングを行うことができます。

![「None」オプションが選択された「Export SAML-trace preferences」メニュー。]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## トラブルシューティング

### ユーザーのメールアドレスは正しく設定されていますか？

`ERROR_CODE_SSO_INVALID_EMAIL` エラーが表示される場合、ユーザーのメールアドレスが無効です。SAML トレースで `saml2:Attribute Name="email"` フィールドが、ユーザーがログインに使用しているメールアドレスと一致していることを確認してください。Microsoft Entra ID（旧 Azure Active Directory）を使用している場合、属性マッピングは `email = user.userprincipalname` です。

メールアドレスは大文字と小文字が区別され、ID プロバイダー（Okta、OneLogin、Microsoft Entra ID など）で設定されたものを含め、Braze で設定されたものと完全に一致する必要があります。

ユーザーのメールアドレスに問題があることを示すその他のエラー:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: ユーザーのメールアドレスがダッシュボード内に存在しません。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: ユーザーのメールアドレスが空白であるか、正しく設定されていません。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` または `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: ユーザーのメールアドレスが SSO のセットアップに使用されたものと一致しません。

### 有効な SAML 証明書（x.509 証明書）がありますか？

[この SAML 検証ツール](https://www.samltool.com/validate_response.php)を使用して SAML 証明書を検証できます。期限切れの SAML 証明書も無効な SAML 証明書であることに注意してください。

### 正しい SAML 証明書（x.509 証明書）をアップロードしましたか？

SAML トレースの `ds:X509Certificate` セクションにある証明書が、Braze にアップロードしたものと一致していることを確認してください。これには `-----BEGIN CERTIFICATE-----` ヘッダーと `-----END CERTIFICATE-----` フッターは含まれません。

### SAML 証明書（x.509 証明書）を誤入力またはフォーマットミスしていませんか？

Braze ダッシュボードに送信した証明書に空白や余分な文字がないことを確認してください。

Braze に証明書を入力する際は、Privacy Enhanced Mail (PEM) エンコードされ、正しくフォーマットされている必要があります（`-----BEGIN CERTIFICATE-----` ヘッダーと `-----END CERTIFICATE-----` フッターを含む）。

以下は正しくフォーマットされた証明書の例です:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ユーザーのセッショントークンは有効ですか？

影響を受けるユーザーに[ブラウザのキャッシュと Cookie をクリア](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser)してもらい、再度 SAML SSO でログインを試みてください。

### RelayState を設定しましたか？

`ERROR_CODE_SSO_INVALID_RELAY_STATE` エラーが表示される場合、RelayState が正しく設定されていないか、存在しない可能性があります。まだ設定していない場合は、IdP 管理システムで RelayState を設定する必要があります。手順については、[RelayState のセットアップ](#setting-up-your-relaystate)を参照してください。

### ユーザーが Okta と Braze の間でサインインループに陥っていませんか？

Okta SSO と Braze ダッシュボードの間を循環してサインインできないユーザーがいる場合、Okta に移動して SSO URL の送信先を [Braze インスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)（例: `https://dashboard-07.braze.com`）に設定する必要があります。

別の IdP を使用している場合は、会社が正しい SAML または x.509 証明書を Braze にアップロードしたかどうかを確認してください。

### 手動統合を使用していますか？

会社が IdP のアプリストアから Braze アプリをダウンロードしていない場合は、事前構築済みの統合をダウンロードする必要があります。例えば、IdP が Okta の場合は、[統合ページ](https://www.okta.com/integrations/braze/)から Braze アプリをダウンロードします。

## 次のステップ

SAML SSO を設定した後、以下のことができます:

- セキュリティ設定で [SSO のみのログインを強制]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#restriction)し、ユーザーがパスワードでログインすることを制限します。
- [SAML ジャストインタイムプロビジョニングを設定]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning/)して、新しいユーザーが初回の SSO サインイン時に自動的に Braze アカウントを作成できるようにします。