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

Amazon SESの設定を始める前に、以下の情報を確認してください。

- 送信ドメイン名
- IPプール名（マーケティング、トランザクション、ステージングなど）
- 各IPプールのIPアドレス数
- クリックトラッキングドメインの優先サフィックス（「clicks」や「click」、「links」や「link」など）

## 設定例 {#setup-example}

一般的なAmazon SESの設定は以下のようになります。

- **サブアカウント名:** braze
- **クラスター:** eu-02

| IPプール | IP数 | 設定セット | 送信ドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="設定例" }

{% alert note %}
クラスターとサブアカウント名は、IPプールと設定セットに自動的に付加されます。
{% endalert %}

## クリックトラッキングドメインの設定例 {#click-tracking-domain-configuration-examples}

以下の表は、ブランディングの方針に基づいたクリックトラッキングドメイン設定の例です。

### 送信ドメインごとに1つのクリックトラッキングドメイン {#one-click-tracking-domain-for-each-sending-domain}

| マーケティング IP プール | 設定セット | 送信サブドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="送信ドメインごとに1つのクリックトラッキングドメイン" }

### すべての送信ドメインに対して1つのクリックトラッキングドメイン {#one-click-tracking-domain-for-all-sending-domains}

これは、クリックトラッキングドメインが設定セット内の少なくとも1つの送信ドメインと一致する必要があるというルールに基づいています。

| マーケティング IP プール | 設定セット | 送信サブドメイン | クリックトラッキングドメイン |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="すべての送信ドメインに対して1つのクリックトラッキングドメイン" }

## 考慮事項 {#considerations}

- Amazon SES の IP プールは IP アドレスそのもののみをホストし、設定セットが送信ドメインとクリックトラッキングドメインをホストします。
- 各設定セットには一度に 1 つの IP プールしか割り当てられませんが、同じ IP プールを使用しつつ異なる送信ドメインを持つ複数の設定セットを作成できます。
- Amazon SES は rDNS および A レコードを内部的に処理します。これは、受信トレイプロバイダーとの緊密な関係を活かして IP アドレスの認識を支援するためです。
- 各送信ドメインには SPF 検証を支援するための MAIL FROM 識別子が付加されています。
    - 各送信ドメインの値は「e」です。
    - MAIL FROM の値は、顧客に表示される差出人アドレスには影響しません。
- メールサービスプロバイダー（ESP）として Amazon SES を使用している場合、トラップメッセージ期間の開始およびトラップメッセージ期間の終了は利用できません。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: SSLの設定
  link: /docs/user_guide/channels/email/email_setup/ssl
{% endarticle_tiles %}