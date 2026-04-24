---
nav_title: Amazon SES のセットアップ
article_title: Amazon SES のセットアップ
page_order: 1
page_type: reference
description: "このリファレンス記事では、Amazon SES をメールサービスプロバイダーとしてセットアップする方法について説明します。"
channel: email
---

# Amazon SES のセットアップ

> Braze は、新しいメールセットアップ時のデフォルトのメールサービスプロバイダーとして Amazon Simple Email Service (SES) を使用します。必要なセットアップが Amazon SES の機能と合わない場合は、Braze サポートに連絡して、SparkPost または SendGrid でセットアップを完了するオプションについてご相談ください。

## 前提条件

Amazon SES のセットアップを開始する前に、以下を確認してください。

- 送信ドメイン名
- IP プール名（マーケティング、トランザクション、ステージングなど）
- 各 IP プールの IP アドレス数
- クリックトラッキングドメインの優先付加文字列（「clicks」や「click」、「links」や「link」など）

## セットアップ例

一般的な Amazon SES のセットアップは以下のようになります。

- **サブアカウント名:** braze
- **クラスター:** eu-02

| IP プール | IP 数 | 設定セット | 送信ドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }

{% alert note %}
クラスターとサブアカウント名は、IP プールと設定セットに自動的に付加されます。
{% endalert %}

## クリックトラッキングドメインの設定例

以下の表は、ブランディングの好みに基づいたクリックトラッキングドメイン設定の例です。

### 各送信ドメインに1つのクリックトラッキングドメイン

| マーケティング IP プール | 設定セット | 送信サブドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### すべての送信ドメインに1つのクリックトラッキングドメイン

これは、クリックトラッキングドメインが設定セット内の少なくとも1つの送信ドメインと一致する必要があるというルールに基づいています。

| マーケティング IP プール | 設定セット | 送信サブドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 考慮事項

- Amazon SES の IP プールは IP アドレス自体のみをホストし、設定セットが送信ドメインとクリックトラッキングドメインをホストします。
- 各設定セットには一度に1つの IP プールのみを割り当てることができますが、同じ IP プールを使用しつつ異なる送信ドメインを持つ複数の設定セットを作成できます。
- Amazon SES は、受信トレイプロバイダーとの密接な関係を活用して IP アドレスの認識を支援するため、rDNS と A レコードを内部的に処理します。
- 各送信ドメインには、SPF 検証を支援するための MAIL FROM 識別子が付加されています。
    - 各送信ドメインの値は「e」です。
    - MAIL FROM の値は、顧客に表示される From アドレスを変更しません。
- Amazon SES がメールサービスプロバイダーの場合、Microsoft Smart Network Data Services (SNDS) はサポートされません。

## 次のステップ

- [SSL のセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl)