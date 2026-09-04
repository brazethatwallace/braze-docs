---
nav_title: BrazeのSSL
article_title: BrazeのSSL
page_order: 5
page_type: reference
description: "この参考記事では、SSLについて、その使用目的、Brazeでの使用方法について説明します。"
channel: email
---

# BrazeのSSL {#ssl-at-braze}

> セキュアソケットレイヤー（SSL）は、URLをHTTPではなくHTTPSで暗号化します。HTTPSは、有効で信頼できるSSLまたはTLS証明書が存在し、そのWebサイトが安全にアクセスできることを示します。

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## SSLが重要な理由 {#why-is-ssl-important}

ほとんどのドメインではSSLは必須ではありませんが、Brazeでは以下の理由からSSLの使用を強く推奨しています。

WebサイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業にとっても一般的な慣行です。ユーザーはSSLで保護されたリンクをより信頼する傾向があり、追加の認証レイヤーによってデータの保護が強化されます。

### クリックトラッキングと開封トラッキングに必要 {#necessary-for-click-and-open-tracking}

Brazeは、クリックと開封をトラッキングするために、ブランド付きリンクトラッキングサブドメインを使用してリンクを変換します。デフォルトでは、これらのリンクはHTTPで始まります。非セキュアなトラフィックを制限するブラウザーや拡張機能を使用しているユーザーは、リダイレクト先のURLがセキュアであっても、リダイレクトを通過する際に問題が発生する場合があります。これにより、画像が壊れたり、トラッキングが不正確になったりする可能性があります。リンクトラッキングサブドメインにSSLを適用して、セキュアなリダイレクトを確保してください。

## 要件 {#requirements}

### ブラウザ {#browser}

Google Chrome などの主要なブラウザは、ユーザーを保護するために安全でない URL を介したトラフィックを制限しています。SSL を使用すると、コンテンツが信頼できるものであることを確認でき、メール内のリンク切れや画像の表示不良などの問題を最小限に抑えることができます。

### HSTS ドメイン {#hsts-domains}

HTTP Strict Transport Security（HSTS）ドメインを使用している場合は、SSL を設定し、必要なセキュリティ証明書を送信するように CDN を構成してください。SSL がないと、画像やWebリンクが正しく表示されません。

## SSL証明書を取得する {#acquire-an-ssl-certificate}

サードパーティ（通常はコンテンツデリバリーネットワーク（CDN））を通じてSSL証明書を取得します。CDNは証明書をホストし、ユーザーがリンクをクリックした際にトラフィックをCDN経由にリダイレクトして証明書を適用してから、SendGridまたはSparkPostに送信することでブラウザに証明書を提供します。

SSLの設定を開始するには、Brazeのカスタマーサクセスマネージャーに連絡して、Brazeメールの完全な設定を開始してください。

Brazeが設定を開始した後、以下のステップに従ってください。

1. Brazeがドメインレジストリに追加するDNSレコードを提供します。
2. Brazeがレコードがレジストリに正しく追加されたかどうかを確認します。
3. その後、CDNを選択し、サードパーティプロバイダーからSSL証明書を取得します。
4. この時点で、CDNを設定します。BrazeはCDNの設定に関するトラブルシューティングのサポートはできません。詳細については、CDNプロバイダーにお問い合わせください。
5. カスタマーサクセスマネージャーに連絡して、SSLを有効にしてもらいます。

## CDNとは何か、なぜ必要なのか？ {#what-is-a-cdn-and-why-do-i-need-it}

コンテンツデリバリーネットワーク（CDN）は、セキュリティ証明書を処理しながら、複数のメディアにわたってコンテンツの高速な読み込み時間を確保するサーバープラットフォームです。

{% alert important %}
CDNの設定は、常にBrazeによるDNSレコードの検証が完了した後に行います。このステップをまだ開始していない場合は、カスタマーサクセスマネージャーに連絡して、開始方法の詳細をご確認ください。
{% endalert %}

クリックおよび開封トラッキングのために、配信パートナーはブランドサブドメインを使用してリンクを変換し、CDNはそれらの変換されたリンクにSSL証明書を適用します。パートナーは、リンクや画像を正しく表示するために、受信者のブラウザーに有効な証明書を提示する必要があることがよくあります。Brazeは証明書を要求または管理しないため、CDNを通じてこの設定を行う必要があります。

{% alert note %}
SSLクリックおよび開封トラッキングにリストされているCDNを使用できない、または使用したくない場合は、カスタムSSL設定をセットアップすることもできます。代替CDNやカスタムプロキシを使用すると、設定がより複雑になる場合があります。詳細については、[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/)および[SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)のドキュメントを参照してください。
{% endalert %}

### その他のリソース {#additional-resources}

{% alert important %}
CDN設定のトラブルシューティングについては、CDNプロバイダーに問い合わせるか、一般的なガイダンスについて[トラブルシューティング]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting)を参照してください。
{% endalert %}

特定のCDNの設定方法については、メールサービスプロバイダー（ESP）パートナーによる以下のリソースを参照してください。お使いのCDNがリストに含まれていない場合でも、CDNにSSL証明書を適用する機能があることを確認してください。

CDNのクリックトラッキングドメインを設定する際は、ホストヘッダー攻撃などのセキュリティ上の問題を防ぐために、`X-Forwarded-Host` ヘッダーを有効にしてください。手順についてはCDNのドキュメントまたはサポートチームを参照してください。

| パートナー | CDN | ドキュメント |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [CloudFrontでのHTTPSの使用](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [SSL/TLSの使用を開始する](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Fastlyが管理する証明書によるTLSの設定](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [カスタムSSLの設定方法](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Googleマネージド SSL証明書](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [CloudFrontを使用してクリックトラッキング用SSLを設定する方法](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [CloudFlareの使用](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Fastlyの使用](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [KeyCDNの使用](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [AWS CloudFrontによるステップバイステップガイド](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Cloudflareによるステップバイステップガイド](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Fastlyによるステップバイステップガイド](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Google Cloud Platformによるステップバイステップガイド](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Microsoft Azureによるステップバイステップガイド](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="その他のリソース" }

### Amazon SES

ESPとしてAmazon SESを使用している場合は、[Amazon SESのドキュメント](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)の**Option 2: Configuring an HTTPS domain**を参照し、Brazeクラスターに基づいてリージョン別のAWSトラッキングドメインを指定してください。

- **Braze USクラスター:** `r.us-east-1.awstrack.me`
- **Braze EUクラスター:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDNのクリックトラッキングドメインを設定する際は、ホストヘッダー攻撃などのセキュリティ上の問題を防ぐために、`X-Forwarded-Host` ヘッダーを有効にしてください。手順についてはCDNプロバイダーにお問い合わせください。
{% endalert %}

## クリックおよび開封トラッキングURLパターン {#click-and-open-tracking-url-patterns}

メールサービスプロバイダー（ESP）は、トラッキング対象の各リンクをクリックトラッキングドメインを指すように書き換え、そのリクエストがトラッキングされたクリックまたは開封であることを示すパスプレフィックスを追加します。Brazeはこれらのパスを構築しません。ESPがリンクを書き換える際に追加します。CDNまたはプロキシルール、セキュリティ許可リスト、モバイルアプリのリンク処理については、ESPのドキュメントを正式な情報源として使用してください。

| ESP | パスパターン | ESPドキュメント |
| --- | --- | --- |
| SendGrid | トラッキングされたクリックの場合は `/wf/click?upn=...`、ユニバーサルリンクとしてフラグを付けたリンクの場合は `/uni/wf/click?upn=...` です。設定によっては、ブランドリンクで `/ls/click`（長い署名付き）や `/ss/`（短縮）を使用することもできます。 | [ユニバーサルリンク](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links)および[短縮リンク](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | トラッキングされたクリックの場合は `/f/`、トラッキングされた開封の場合は `/q/` です。`data-msys-sublink` カスタムパスを設定したリンクは `/f/{custom_path}/` に従います。 | [ディープリンク](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | トラッキングされたクリックの場合は `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` です。`ses:custom-path` 属性を設定したリンクは `/CL1/{customPath}/{encodedUrl}/...` に従います。 | [カスタム開封およびクリックドメイン](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ESPごとのクリックおよび開封トラッキングURLパターン" }

たとえば、クリックトラッキングドメインが `clicks.example.com` でESPがSparkPostの場合、トラッキングされたクリックは `https://clicks.example.com/f/` で始まるURLに解決されます。

{% alert important %}
これらのパスプレフィックスはESPが所有しており、変更や追加が行われる可能性があるため、Brazeは恒久的または網羅的なリストを保証できません。セキュリティツールが対応している場合は、個別のパスではなくクリックトラッキングドメイン全体を許可リストに登録し、現在のパターンについてはESPのドキュメントで確認してください。
{% endalert %}

モバイルアプリでこれらのパスを処理する方法については、[ユニバーサルリンクとApp Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)を参照してください。

## トラブルシューティング {#troubleshooting}

CDNの設定、証明書、プロキシの問題はCDNプロバイダーで対処する必要がありますが、以下のヒントを使用して、一般的なSSLクリックトラッキングの問題を特定できます。トラブルシューティングのガイダンスについては、[トラブルシューティング]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting)を参照してください。