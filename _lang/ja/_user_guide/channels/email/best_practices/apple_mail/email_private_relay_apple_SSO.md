---
nav_title: Apple Private Relay へのメール送信
article_title: Apple Private Relay へのメール送信
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relay にメールを送信するプロセスについて説明します。"
channel:
  - email
toc_headers: h2
---

# Apple Private Relay へのメール送信

> Apple のシングルサインオン (SSO) 機能を使用すると、ユーザーは自分のメールアドレス (`example@icloud.com`) を共有するか、個人のメールアドレスの代わりにブランドに提供されるアドレスをマスクしてメールアドレスを非公開にする (`tq1234snin@privaterelay.appleid.com`) かを選択できます。Apple は、リレーアドレスに送信されたメッセージをユーザーの実際のメールアドレスに転送します。

Apple のプライベートメールリレーにメールを送信するには、送信ドメインを Apple に登録してください。ドメインを Apple で設定しない場合、リレーアドレスに送信されたメールはバウンスになります。

ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Braze は通常どおりメールバウンス情報を受信します。これらのユーザーは、Apple ID の設定ページから Apple でサインインを使用するアプリを管理できます（[Apple のドキュメント](https://support.apple.com/en-us/HT210426)を参照）。

## メールプロバイダーの設定

{% tabs %}
{% tab SendGrid %}

メールプロバイダーとして SendGrid を使用している場合、DNS の変更なしで Apple にメールを送信できます。

1. [Apple Developer Portal](https://developer.apple.com/) にログインします。
2. **Certificates, Identifiers & Profiles** ページに移動します。
3. **Services** > **Sign in with Apple for Email Communication** を選択します。
4. **Email Sources** セクションで、ドメインとサブドメインを追加します。
- アドレスは次の形式にする必要があります: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`（例: `bounces+1234567@braze.online.docs.com`）。

希望する「From」アドレスが `abmail` アドレスの場合は、サブドメインにそれを含めてください。たとえば、`docs.braze.com` ではなく `abmail.docs.braze.com` を使用します。

{% endtab %}
{% tab SparkPost %}

SparkPost で Apple Private Relay を設定するには、次のステップに従ってください:

1. Apple でサインインします。
2. [Apple のドキュメント](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service)に従ってメールドメインを登録します。
3. Apple が自動的にドメインを確認し、検証済みのドメインを表示し、再検証または削除のオプションを提供します。

### 送信ドメインがバウンスドメインでもある場合

送信ドメインがバウンスドメインとしても使用されている場合、レコードを保存できないため、以下の追加ステップに従う必要があります:

1. ドメインが既に SparkPost で検証されている場合、MX レコードと TXT レコードを作成する**必要があります**:

| インスタンス | MX レコード                   | TXT レコード                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
SPF の失敗を避けるために、CNAME レコードを削除する**前に** MX レコードと TXT レコードを作成し、DNS に反映させる必要があります。
{% endalert %}

{:start="2"}
2. CNAME レコードを削除します。
3. 適切なルーティングのために MX レコードと TXT レコードに置き換えます。
4. CDN またはファイルホスティングを指す A レコードを作成します。

{% endtab %}
{% tab Amazon SES %}

Apple Private Relay を設定するには、カスタム MAIL FROM ドメインを事前に設定しておくことが理想的です。

1. Apple でサインインします。
2. [Apple のドキュメント](https://developer.apple.com/help/account/capabilities/configure-private-email-relay-service)に従ってメールドメインを登録します。

{% alert important %}
リンク先の手順に従って登録した内容と DKIM/SPF が一致していることを確認してください。
{% endalert %}

{:start="3"}
3. Apple が自動的にドメインを確認し、検証済みのドメインを表示し、再検証または削除のオプションを提供します。

{% endtab %}
{% endtabs %}

その他のご質問がある場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を作成してください。