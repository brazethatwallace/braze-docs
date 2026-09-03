---
nav_title: Apple Private Relayにメールを送る
article_title: Apple Private Relayにメールを送る
alias: /email_relay/
page_order: 0
description: "この記事では、Apple Private Relayにメールを送信する手順について説明します。"
channel:
  - email
toc_headers: h2
---

# Apple Private Relayにメールを送る {#send-emails-to-apple-private-relay}

> Appleのシングルサインオン（SSO）機能を使用すると、ユーザーは自分のメールアドレス（`example@icloud.com`）を共有するか、パーソナルメールアドレスの代わりにマスキングされたアドレス（`tq1234snin@privaterelay.appleid.com`）をブランドに提供してメールアドレスを非公開にすることができます。Appleは、リレーアドレスに送信されたメッセージをユーザーの実際のメールアドレスに転送します。

Appleのプライベートメールリレーにメールを送信するには、送信ドメインをAppleに登録してください。Appleでドメインを設定しないと、リレーアドレスに送信されたメールはバウンスされます。

ユーザーがアプリのリレーメールへのメール転送を無効にした場合、Brazeは通常通りメールのバウンス情報を受信します。これらのユーザーは、Apple IDの設定ページから、Appleでサインインを使用するアプリを管理できます（[Appleのドキュメント](https://support.apple.com/en-us/HT210426)を参照してください）。

## メールプロバイダーを設定する {#configure-your-email-provider}

{% tabs %}
{% tab SendGrid %}

メールプロバイダーとしてSendGridを使用している場合、DNSの変更なしにAppleにメールを送信できます。

1. [Apple Developer Portal](https://developer.apple.com/) にログインします。
2. **Certificates, Identifiers & Profiles** ページに移動します。
3. **Services** > **Sign in with Apple for Email Communication** を選択します。
4. **Email Sources** セクションで、ドメインとサブドメインを追加します。
- アドレスは次の形式にする必要があります：`bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`（例：`bounces+1234567@braze.online.docs.com`）。

希望する差出人アドレスが `abmail` アドレスの場合は、サブドメインにそれを含めてください。たとえば、`docs.braze.com` の代わりに `abmail.docs.braze.com` を使用します。

{% endtab %}
{% tab SparkPost %}

SparkPost用にApple Private Relayを設定するには、以下のステップに従ってください：

1. Appleでサインインします。
2. [Appleのドキュメント](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service)に従ってメールドメインを登録します。
3. Appleが自動的にドメインを確認し、検証済みのドメインを表示し、再検証または削除のオプションを提供します。

### 送信ドメインがバウンスドメインも兼ねている場合 {#when-the-sending-domain-is-also-the-bounce-domain}

送信ドメインがバウンスドメインとしても使用されている場合、レコードを保存できないため、以下の追加ステップに従う必要があります：

1. ドメインがすでにSparkPostで検証済みの場合、MXレコードとTXTレコードを作成する**必要があります**：

| インスタンス | MXレコード                   | TXTレコード                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="送信ドメインがバウンスドメインも兼ねている場合" }

{% alert important %}
SPFの失敗を回避するには、CNAMEレコードを削除する**前に**、MXレコードとTXTレコードを作成し、DNSに反映させる必要があります。
{% endalert %}

{:start="2"}
2. CNAMEレコードを削除します。
3. 適切なルーティングのためにMXレコードとTXTレコードに置き換えます。
4. CDNまたはファイルホスティングを指すAレコードを作成します。

{% endtab %}
{% tab Amazon SES %}

Apple Private Relayを設定するには、カスタムMAIL FROMドメインを事前に設定しておくことが理想的です。

1. Appleでサインインします。
2. [Appleのドキュメント](https://developer.apple.com/help/account/capabilities/configure-private-email-relay-service)に従ってメールドメインを登録します。

{% alert important %}
リンク先の手順に従って、登録内容とDKIM/SPFが一致していることを確認してください。
{% endalert %}

{:start="3"}
3. Appleが自動的にドメインを確認し、検証済みのドメインを表示し、再検証または削除のオプションを提供します。

{% endtab %}
{% endtabs %}

その他のご質問がある場合は、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を作成してください。