---
nav_title: BrazeのSSL
article_title: SSLの概要
page_order: 5
page_type: reference
description: "この参考記事では、SSLについて、その使用目的、Brazeでの使用方法について説明します。"
channel: email

---

# BrazeのSSL {#ssl-at-braze}

> セキュアソケットレイヤー（SSL）は、URLをHTTPではなくHTTPSで暗号化します。HTTPSは、有効で信頼できるSSLまたはTLS証明書が存在し、そのWebサイトが安全にアクセスできることを示します。

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## なぜSSLが重要なのか {#why-is-ssl-important}

ほとんどのドメインはSSLを必要としませんが、Brazeは以下の理由からSSLの使用を強く推奨しています。

WebサイトやリンクをSSLで保護することは、機密性の高い顧客情報を直接扱わない企業でも一般的に行われています。SSLで保護されたリンクはユーザーからの信頼度が高く、認証のレイヤーが増えることでデータの保護に役立ちます。

### クリックと開封のトラッキングに必要 {#necessary-for-click-and-open-tracking}

Brazeは、クリック数と開封をトラッキングするために、ブランド化されたリンクトラッキングサブドメインを使用してリンクを変換します。デフォルトでは、これらのリンクはHTTPで始まります。非セキュアな通信を制限するブラウザや拡張機能を使用しているユーザーは、たとえURLがセキュアであっても、送信先URLへのリダイレクトを通過できない可能性があります。これにより画像が破損したり、トラッキングが不正確になったりすることがあります。リンクトラッキングサブドメインにSSLを適用して、安全なリダイレクトを確保してください。

### ブラウザの要件 {#browser-requirement}

Google Chromeなどの主要ブラウザは、ユーザーを保護するため、非セキュアなURL経由の通信を制限しています。SSLを使用することで、コンテンツが信頼できるものであることを確認でき、メール内のリンク切れや画像の表示不良といった問題を最小限に抑えられます。

### HSTSドメインの要件 {#hsts-domains-requirement}

HTTP Strict Transport Security（HSTS）ドメインをお持ちの場合は、SSLを設定し、必要なセキュリティ証明書を送信するようにCDNを構成してください。SSLがないと、画像やWebリンクが壊れます。

## SSL証明書を取得する {#acquire-an-ssl-certificate}

SSL証明書はサードパーティ、通常はコンテンツ配信ネットワーク（CDN）を通じて取得します。CDNは証明書をホストし、ユーザーがリンクをクリックした際に、トラフィックをCDN経由でリダイレクトして証明書を適用してから、SendGridやSparkPostに送信することでブラウザに証明書を提供します。

SSLの設定を開始するには、Brazeのカスタマーサクセスマネージャーに連絡し、Brazeメールの完全な設定の開始を依頼してください。

Brazeが設定を開始したら、以下のステップに従ってください：
1. Brazeが、ドメインレジストリに追加するDNSレコードを提供します。
2. Brazeが、レコードがレジストリに正しく追加されているかどうかを確認します。
3. その後、CDNを選択し、サードパーティのプロバイダーからSSL証明書を取得します。
4. この時点で、CDNを設定します。なお、BrazeではCDN設定のトラブルシューティングをサポートできません。追加のサポートが必要な場合は、CDNプロバイダーにお問い合わせください。
5. カスタマーサクセスマネージャーに連絡して、SSLを有効にしてもらいます。

## CDNとは何か、なぜ必要なのか {#what-is-a-cdn-and-why-do-i-need-it}

コンテンツ配信ネットワーク（CDN）は、セキュリティ証明書の処理も行いながら、複数のメディアにわたるコンテンツの高速な読み込み時間を確保するサーバープラットフォームです。

{% alert important %}
CDNの設定は、常にBrazeによるDNSレコードの検証が完了した後に行います。このステップをまだ開始していない場合は、カスタマーサクセスマネージャーに連絡して、開始方法の詳細情報を確認してください。
{% endalert %}

クリックおよび開封トラッキングでは、配信パートナーがブランド化されたサブドメインを使用してリンクを変換し、CDNがそれらの変換されたリンクにSSL証明書を適用します。パートナーは、リンクや画像を正しく表示するために、受信者のブラウザに有効な証明書を提示する必要があることが多いです。Brazeは証明書のリクエストや管理を行わないため、CDNを通じてこの設定を行う必要があります。

{% alert note %}
SSLのクリックおよび開封トラッキングに記載されているCDNを使用できない場合や使用したくない場合は、カスタムSSL設定をセットアップできます。代替のCDNやカスタムプロキシを使用すると、設定がより複雑になる場合があります。[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/)および[SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/)のドキュメントを参照してください。
{% endalert %}

### その他のリソース {#additional-resources}

{% alert important %}
CDN設定のトラブルシューティングについては、CDNプロバイダーにお問い合わせください。
{% endalert %}

特定のCDNの設定方法については、メールサービスプロバイダー（ESP）パートナーによる以下のリソースを参照してください。お使いのCDNが一覧にない場合でも、CDNがSSL証明書を適用できることを確認してください。

CDNのクリックトラッキングドメインを設定する際は、ホストヘッダー攻撃などの潜在的なセキュリティ問題を防ぐために、`X-Forwarded-Host`ヘッダーを有効にしてください。手順については、CDNのドキュメントまたはサポートチームを参照してください。

| パートナー | CDN | ドキュメント |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Get started with SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Setting up TLS with certificates Fastly manages](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [How to set up custom SSL](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [How to configure SSL for click tracking using CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Using CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Using Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Using KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Step-by-step guide with AWS CloudFront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Step-by-step guide with Cloudflare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Step-by-step guide with Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Step-by-step guide with Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Step-by-step guide with Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="その他のリソース" }

### Amazon SES

メールサービスプロバイダー（ESP）としてAmazon SESを使用している場合は、[Amazon SESのドキュメント](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)の**Option 2: Configuring an HTTPS domain**を参照し、Brazeクラスターに基づいてリージョン別のAWSトラッキングドメインを指定してください：

- **Braze USクラスター:** `r.us-east-1.awstrack.me`
- **Braze EUクラスター:** `r.eu-central-1.awstrack.me`

## トラブルシューティング {#troubleshooting}

CDNの設定、証明書、プロキシの問題はCDNプロバイダーに対応を依頼する必要がありますが、一般的なSSLクリックトラッキングの問題を特定するために以下のヒントを活用してください。

### メール開封率が低い {#low-email-open-rates}

メール開封率が突然低下した場合は、SSL証明書が最新であることを確認してください。有効期限が切れている場合は、CDNまたは証明書プロバイダーでSSL証明書を更新する必要があります。

### ドメインレジストリの問題 {#domain-registry-issues}

digコマンドを実行して、リンクトラッキングがCDNを指していることを確認してください。ターミナルで`dig CNAME link_tracking_subdomain`を実行します。`ANSWER SECTION`にCNAMEの指し先が表示されます。CDNではなくメールサービスプロバイダー（SendGridまたはSparkPost）を指している場合は、ドメインレジストリをCDNを指すように再設定してください。

### CDNの問題 {#cdn-issues}

セットアップ中にライブメールのリンクが破損する場合は、適切な設定が完了する前にDNSをCDNに向けた可能性があります。これは「間違ったリンク」エラーとして表示されることがあります。CDNプロバイダーに連絡し、そのドキュメントを確認して設定のトラブルシューティングを行ってください。

接続がプライベートではないというエラーメッセージが表示される場合は、SSLまたはCDNが正しく設定されていない可能性があります。ターミナルで`dig`コマンドを実行してください（例：`dig CNAME your_link_tracking_subdomain`）。`ANSWER SECTION`で、結果がCDNではなくESPを指している場合、設定ミスが原因です。BrazeのSSLクリックトラッキングが機能するには、CNAMEがCDNを指している必要があります。SSLとCDNの設定を管理しているチームと連携して、さらなるサポートを受けてください。

#### リダイレクトリンクでHTTP 403が発生する場合 {#http-403-on-redirect-links}

トラッキング対象のリダイレクトリンクが**403 Forbidden**を返す場合、多くの場合、コンテンツ配信ネットワーク（CDN）やWebアプリケーションファイアウォール（WAF）で障害が発生しています。たとえば、AWS WAFやAmazon CloudFrontで特定のユーザーエージェント、クエリ文字列、またはリダイレクトパターンをブロックするルールが原因となることがあります。CDNまたはクラウドプロバイダーでブロックされたリクエストのログと指標を確認してください。AWSの場合は、[Troubleshooting issues with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html)を参照してください。

問題がクリックトラッキングに固有のものかどうかを確認するには、テストリンク1つでクリックトラッキングをオフにしてください（[リンク単位でクリックトラッキングをオフにする]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis)を参照）。クリックトラッキングをオフにすると送信先URLが読み込まれるのに、トラッキングをオンにすると403が返される場合は、クリックトラッキングドメイン、CDN、WAFの設定に焦点を当ててください。

### SSL有効化のステータス {#ssl-enablement-status}

SSLの設定を完了してもリンクがHTTPのまま表示される場合は、BrazeのカスタマーサクセスマネージャーにSSLが有効になっているか確認してください。Brazeは、すべてのセットアップステップが完了した後にのみSSLを有効にします。