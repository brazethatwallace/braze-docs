---
nav_title: IPアドレスとドメインを設定する
article_title: IPアドレスとドメインを設定する
page_order: 0
page_type: tutorial
channel: email
description: "この記事では、Braze経由でメールを送信するためにIPとドメインを設定する方法について説明します。"

---

# IPアドレスとドメインを設定する {#set-up-ips-and-domains}

> この記事では、Brazeでメール送信を開始する前に必要なIPアドレスとプール、およびドメインとサブドメインの設定に関する要件とステップについて説明します。

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
メールサービスプロバイダー (ESP) パートナーとして、SendGrid、SparkPost、またはAmazon Simple Email Service (SES) を使用できます。2026年以降、Brazeは新しいメール設定のデフォルトESPとしてAmazon SESを使用します。詳細については、[Amazon SESのセットアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses)を参照してください。
{% endalert %}

## 方法1: Brazeとの連携（推奨） {#method-1-coordinate-with-braze-recommended}

### ステップ1: 情報の整理 {#step-1-outline-information}

以下の情報をBrazeの担当者に送信してください。

* 選択したドメインとサブドメイン
* 毎月送信するメールのおおよその数（必要なIPの数を判断するのに役立ちます）
* 送信ドメインを割り当てられたIPにどのようにマッピングするかの希望

### ステップ2: Brazeが情報を設定 {#step-2-braze-configures-information}

メールを受け取った後、IP、ドメイン、サブドメイン、IPプールの設定作業を開始します。

### ステップ3: DNSレコードの追加 {#step-3-add-dns-records}

IP、ドメイン、サブドメイン、IPプールが設定された後、DNSレコードのリストをお送りします。開発者やエンジニアに依頼して、必要な場所にこれらのDNSレコードを追加してください。追加が完了したら、Brazeオンボーディングチームにお知らせください。

Brazeのメールサービスプロバイダー（ESP）全体でDNSレコードがどのように機能するか（SPF、DKIM、DMARC、ESP固有のレコード構造を含む）の詳細な説明については、[DNSレコードの理解]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records)を参照してください。

{% multi_lang_include channels/email/dns_records.md %}

BrazeからDNSレコードが提供されたら、DNSチームまたはITチームが対応可能になり次第、すぐに追加してください。ドメイン検証には期限があり、レコードの追加が遅れると、DNSレコードが後で正しく解決されても検証が失敗する場合があります。DNSレコードが正しいにもかかわらず検証が失敗する場合は、Brazeオンボーディングチームまたはサポートチームに連絡して、検証の再開を依頼してください。

### 次のステップ {#next-steps}

セットアップを確認し、内部システムですべての情報を検証します。準備が整った場合、またはDNSレコードに関してエンジニアリングチームと対処が必要な問題がある場合は、Brazeオンボーディングチームからお知らせします。

## 方法2：セルフサービスメール設定 {#method-2-self-service-email-setup}

この方法では、1つの送信ドメイン、1つのトラッキングドメイン、および1つのIPを会社全体でセットアップします。それ以上のセットアップを予定している場合は、Brazeオンボーディングチーム（方法1）にご相談ください。

{% multi_lang_include alerts/early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>セルフサービスメール設定機能を使用している場合は、Brazeオンボーディングチームにも必ずご相談ください。

### 前提条件 {#prerequisites}

セルフサービスメール設定を使用するには、以下の前提条件を満たす必要があります。

1. オンボーディング中の新規顧客であること。
2. 「Manage Company Settings」の会社レベル権限を持っていること。

### ステップ1：設定を開始する {#step-1-begin-setup}

1. **設定** > **会社設定**の**管理者設定**に移動します。
2. 次に、**Sender Verification** タブを選択します。このタブを表示するには、「Manage Company Settings」の会社レベル権限が必要です。
3. **Start setup** を選択します。

### ステップ2：送信ドメインを追加して検証する {#step-2-add-and-verify-a-sending-domain}

送信ドメインは、メール送信時の「差出人」アドレスに使用されます。送信ドメインを入力し、**Submit** をクリックします。

次に、ページ下部のTXTレコードとCNAMEレコードをDNSプロバイダーに追加します。その後、Brazeダッシュボードに戻り、**Verify** をクリックします。

![送信ドメインを検証するためのTXTおよびCNAME DNSレコードが表示されたメール設定ページ。]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

検証に失敗し、DNSレコードが正しいと思われる場合は、Brazeサポートにお問い合わせください。

{% alert important %}
送信ドメインは、所有しているドメインのサブドメインである必要があります。たとえば、「example.com」を所有している場合、サブドメインは「mail.example.com」となり、送信アドレスとして「@mail.example.com」を使用できます。
{% endalert %}

### ステップ3：トラッキングドメインを追加して検証する {#step-3-add-and-verify-a-tracking-domain}

トラッキングドメインは、クリックトラッキングとブランディングの目的でメール内のリンクをラップするために使用されます。ユーザーがメールリンクにカーソルを合わせたりクリックしたりすると、このドメインが表示されます。送信ドメインと一致させることをお勧めします。

1. トラッキングドメインを入力し、**Submit** を選択します。
2. 次に、ページ下部のCNAMEレコードをDNSプロバイダーに追加します。
3. その後、Brazeダッシュボードに戻り、**Verify** を選択します。

### ステップ4：IPアドレスを追加する {#step-4-add-an-ip-address}

Brazeは、リバースDNS（rDNS）と呼ばれる設定で、IPアドレスを送信サブドメインに関連付けるAレコードを生成します。DNSプロバイダーにAレコードを追加し、**Set up rDNS** をクリックして配信性をサポートします。

追加されたドメインは **Sender Verification** セクションには表示されません。ドメインを追加するには、Brazeサポートチームにお問い合わせください。

### 複数の専用IPを持つIPプール {#ip-pools-with-more-than-one-dedicated-ip}

IPプールに複数の専用IPアドレスが含まれている場合、Brazeとメールサービスプロバイダー（ESP）は、キャパシティと配信性のために大量送信をそれらのIP間で分散します。分散は概算であり、キャンペーン内のすべてのメッセージがすべてのIPを使用するわけではなく、少量の送信ではアドレス間で不均等に見える場合があります。SendGridは多くの場合、メールをチャンク単位（おおよそ1チャンクあたり約1,500メッセージ）で処理するため、ボリュームが常にIP間で厳密に1対1の比率で分割されるとは限りません。日常的に非常に大量の送信を行う場合は、Brazeオンボーディングまたはカスタマーサクセスの担当者とプールサイズについてご相談ください。

### 次のステップ

送信者検証が完了したら、メッセージが常に高い割合で受信トレイに届くように、IPウォームアップを行うことをお勧めします。この設定が完了したら、ドメインと[IPアドレス]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)が正しく機能しているかどうかを確認するために、Brazeオンボーディングチームにも必ずご相談ください。