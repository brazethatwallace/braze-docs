---
nav_title: IPアドレスとドメインを設定する
article_title: IPアドレスとドメインを設定する
page_order: 0
page_type: tutorial
channel: email
description: "この記事では、Brazeでメールを送信するためのIPアドレス、IPプール、ドメイン、サブドメインの設定方法について説明します。"
---

# IPアドレスとドメインを設定する {#set-up-ips-and-domains}

> この記事では、Brazeでメール送信を開始する前に必要なIPアドレスとプール、およびドメインとサブドメインの設定に関する要件とステップについて説明します。

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
2026年以降、Brazeは新しいメール設定のデフォルトのメールサービスプロバイダー (ESP) としてAmazon Simple Email Service (SES) を使用します。詳細については、[Amazon SESのセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses)を参照してください。
{% endalert %}

## 方法1: メールセルフサービス設定 {#method-1-self-service-email-setup}

この方法では、企業の送信ドメインとトラッキングドメインを設定します。まずBrazeオンボーディングチームに相談し、IPプールとIPアドレスを追加するために以下の情報をBraze担当者に送信する必要があります。

- 選択したドメインとサブドメイン
- 月間のおおよそのメール送信数（必要なIPの数を決定するために役立ちます）
- 送信ドメインを割り当てられたIPプールにどのようにマッピングするかの希望

### 前提条件 {#prerequisites}

セルフサービスメール設定を使用するには、以下の前提条件を満たしていることを確認してください。

- オンボーディング中の新規顧客であること
- 「Edit Domain Settings」の会社レベル権限を持っていること

### ステップ1: 設定を開始する {#step-1-begin-setup}

1. **設定** > **会社設定**の**メールセルフサービス**に移動します。
2. **設定を開始**を選択します。

### ステップ2: 送信ドメインを追加して検証する {#step-2-add-and-verify-a-sending-domain}

送信ドメインは、メール送信時の差出人アドレスに使用されます。

1. 送信ドメインを入力し、**送信**を選択します。
2. ページ下部のTXTレコードとCNAMEレコードをDNSプロバイダーに追加します。

![ドメイン管理システムにコピーするTXTレコードとCNAMEレコードを表示するDNSレコードセクション。]({% image_buster /assets/img/email_setup/dns_records.png %})

{: start="3"}
3. Brazeダッシュボードに戻り、**検証**を選択します。

エンジニアや開発者に、必要な場所にこれらのDNSレコードを追加するよう依頼してください。SPF、DKIM、DMARC、およびメールサービスプロバイダー (ESP) 固有のレコード構造を含め、Brazeのメールサービスプロバイダー全体でDNSレコードがどのように機能するかの詳細については、[DNSレコードの理解]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records)を参照してください。

{% multi_lang_include channels/email/dns_records.md %}

検証が失敗し、DNSレコードが正しいと考えられる場合は、Brazeサポートに連絡してサポートを受けてください。

{% alert important %}
送信ドメインは、所有するドメインの下位ドメインである必要があります。たとえば、「example.com」を所有している場合、サブドメインは「mail.example.com」とすることができ、送信アドレス「@mail.example.com」を使用できます。
{% endalert %}

### ステップ3: トラッキングドメインを追加して検証する {#step-3-add-and-verify-a-tracking-domain}

トラッキングドメインは、クリックトラッキングとブランディングの目的でメール内のリンクをラップするために使用されます。受信者がメールリンクにカーソルを合わせたりクリックしたりすると、このドメインが表示されます。Brazeでは、これを送信ドメインと一致させることを推奨しています。

1. トラッキングドメインを入力し、**送信**を選択します。
2. ページ下部のCNAMEレコードをDNSプロバイダーに追加します。
3. Brazeダッシュボードに戻り、**検証**を選択します。

### ステップ4: IPアドレスを追加する {#step-4-add-an-ip-address}

Brazeは、リバースDNS（rDNS）と呼ばれる設定で、IPアドレスを送信サブドメインに関連付けるAレコードを生成します。DNSプロバイダーにAレコードを追加し、**rDNSを設定**を選択して配信到達性をサポートします。

IPプールのIPアドレスの追加や編集については、Brazeサポートにお問い合わせください。

#### 複数の専用IPを持つIPプール {#ip-pools-with-more-than-one-dedicated-ip}

IPプールに複数の専用IPアドレスが含まれている場合、Brazeとメールサービスプロバイダーは、キャパシティと配信到達性のために大量送信をそれらのIP間で分散します。分散は概算であり、キャンペーン内のすべてのメッセージがすべてのIPを使用するわけではなく、少量の送信ではアドレス間で不均等に見える場合があります。SendGridはメールをチャンク単位（おおよそ1チャンクあたり約1,500メッセージ）で処理することが多いため、ボリュームが常にIP間で厳密に1対1の比率で分割されるとは限りません。日常的に非常に大量の送信を行う場合は、Brazeのオンボーディングまたはカスタマーサクセス担当者とプールサイズについてご相談ください。

### 次のステップ {#next-steps}

送信者認証が完了したら、メッセージが一貫して高い配信率で受信トレイに届くようにするため、BrazeではIPウォームアップを推奨しています。

{% article_tiles %}
- name: 自動IPウォームアップ
  link: /docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming
- name: IPウォームアップ
  link: /docs/user_guide/channels/email/email_setup/ip_warming
{% endarticle_tiles %}

この設定が完了したら、Brazeオンボーディングチームに相談して、ドメインとIPウォームアップが正常に動作しているかを確認してください。

## 方法2：認証済みドメイン {#method-2-verified-domains}

認証済みドメインを使用すると、特定のサブドメインの管理をBrazeに委任し、メール設定とHTTPSクリックトラッキングを自動化できます。DNSドメイン委任により、Brazeはメール送信とクリックトラッキングに必要なDNSレコードを管理します。たとえば、サブドメインが「mail.example.com」の場合、それをBrazeに委任して送信ドメインとトラッキングドメインを設定できます。

{% alert important %}
認証済みドメインは現在、Amazon SESのみをサポートしています。SendGridまたはSparkPostを使用している場合、この機能は利用できません。<br><br>認証済みドメインはメールのみでサポートされています。{% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

### 設定 {#setup}

#### ステップ1：Brazeとの調整 {#step-1-coordinate-with-braze}

以下の情報をBrazeの担当者に送付してください。

- 選択したドメインとサブドメイン
- ドメインをIPプールにどのようにマッピングするかの希望
- 各サブドメインで月間に送信予定のメールのおおよそのボリューム（IPプールに必要なIP数の決定に役立ちます）
- フラグすべき過去の配信到達性に関する懸念事項

#### ステップ2：Brazeが情報を設定する {#step-2-braze-configures-information}

メールを受信した後、Brazeは想定されるIP数とIPプールを追加します。IPプールとIPアドレスが追加されたら、[認証済みドメイン]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains)の手順に従ってください。