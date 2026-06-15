---
nav_title: Amazon SES のセットアップ
article_title: Amazon SES のセットアップ
page_order: 1
page_type: reference
description: "このリファレンス記事では、Amazon SES をメールサービスプロバイダーとしてセットアップする方法について説明します。"
channel: email
---

# Amazon SES のセットアップ {#amazon-ses-setup}

> Brazeは、新しいメールセットアップ時のデフォルトのメールサービスプロバイダーとしてAmazon Simple Email Service (SES) を使用します。必要なセットアップがAmazon SESの機能と合わない場合は、Brazeサポートに連絡して、SparkPostまたはSendGridでセットアップを完了するオプションについてご相談ください。

## 前提条件 {#prerequisites}

Amazon SESのセットアップを開始する前に、以下を確認してください。

- 送信ドメイン名
- IPプール名（マーケティング、トランザクション、ステージングなど）
- 各IPプールのIPアドレス数
- クリックトラッキングドメインの優先付加文字列（「clicks」や「click」、「links」や「link」など）

## セットアップ例 {#setup-example}

一般的なAmazon SESのセットアップは以下のようになります。

- **サブアカウント名:** braze
- **クラスター:** eu-02

| IPプール | IP数 | 設定セット | 送信ドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="セットアップ例" }

{% alert note %}
クラスターとサブアカウント名は、IPプールと設定セットに自動的に付加されます。
{% endalert %}

## クリックトラッキングドメインの設定例 {#click-tracking-domain-configuration-examples}

以下の表は、ブランディングの好みに基づいたクリックトラッキングドメイン設定の例です。

### 各送信ドメインに1つのクリックトラッキングドメイン {#one-click-tracking-domain-for-each-sending-domain}

| マーケティングIPプール | 設定セット | 送信サブドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="各送信ドメインに1つのクリックトラッキングドメイン" }

### すべての送信ドメインに1つのクリックトラッキングドメイン {#one-click-tracking-domain-for-all-sending-domains}

これは、クリックトラッキングドメインが設定セット内の少なくとも1つの送信ドメインと一致する必要があるというルールに基づいています。

| マーケティングIPプール | 設定セット | 送信サブドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="すべての送信ドメインに1つのクリックトラッキングドメイン" }

## 考慮事項 {#considerations}

- Amazon SESのIPプールはIPアドレス自体のみをホストし、設定セットが送信ドメインとクリックトラッキングドメインをホストします。
- 各設定セットには一度に1つのIPプールのみを割り当てることができますが、同じIPプールを使用しつつ異なる送信ドメインを持つ複数の設定セットを作成できます。
- Amazon SESは、受信トレイプロバイダーとの密接な関係を活用してIPアドレスの認識を支援するため、rDNSとAレコードを内部的に処理します。
- 各送信ドメインには、SPF検証を支援するためのMAIL FROM識別子が付加されています。
    - 各送信ドメインの値は「e」です。
    - MAIL FROMの値は、顧客に表示されるFromアドレスを変更しません。
- Amazon SESをメールサービスプロバイダーとして使用している場合、トラップメッセージ期間の開始とトラップメッセージ期間の終了は利用できません。

## 次のステップ {#next-steps}

- [SSLのセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/)