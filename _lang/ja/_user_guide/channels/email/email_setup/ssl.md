---
nav_title: Braze における SSL
article_title: SSL の概要
page_order: 5
page_type: reference
description: "このリファレンス記事では、SSL の概要、その用途、および Braze での使用方法について説明します。"
channel: email

---

# Braze における SSL

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> セキュアソケットレイヤー (SSL) は、HTTP ではなく HTTPS で URL を暗号化します。HTTPS は、有効で信頼された SSL または TLS 証明書が存在し、その Web サイトが安全にアクセスできることを示します。

## SSL が重要な理由

ほとんどのドメインでは SSL は必須ではありませんが、Braze では以下の理由から SSL の使用を強く推奨しています。

SSL で Web サイトとリンクを保護することは、機密性の高い顧客情報を直接扱わない企業にとっても一般的な慣行です。ユーザーは SSL で保護されたリンクをより信頼し、追加の認証レイヤーによってデータの保護が強化されます。

### クリックおよび開封トラッキングに必要

Braze は、クリック数と開封を追跡するために、ブランド化されたリンクトラッキングサブドメインを使用してリンクを変換します。デフォルトでは、これらのリンクは HTTP で始まります。安全でないトラフィックを制限するブラウザーや拡張機能を使用しているユーザーは、送信先 URL が安全であっても、リダイレクトを通過する際に問題が発生する可能性があります。これにより、画像の破損やトラッキングの不正確さが生じることがあります。リンクトラッキングサブドメインに SSL を適用して、安全なリダイレクトを確保してください。

### ブラウザーの要件

Google Chrome などの主要なブラウザーは、ユーザーを保護するために安全でない URL を介したトラフィックを制限しています。SSL を使用することで、コンテンツが信頼されていることを確認し、メール内のリンクや画像の破損などの問題を最小限に抑えることができます。

### HSTS ドメインの要件

HTTP Strict Transport Security (HSTS) ドメインをお持ちの場合は、SSL を設定し、必要なセキュリティ証明書を送信するように CDN を設定してください。SSL がないと、画像や Web リンクが破損します。

## SSL 証明書の取得

SSL 証明書は、サードパーティ（通常はコンテンツデリバリーネットワーク (CDN)）を通じて取得します。CDN は証明書をホストし、ユーザーがリンクをクリックした際に CDN を経由してトラフィックをリダイレクトすることで、証明書を適用してから SendGrid または SparkPost に送信し、ブラウザーに証明書を提供します。

SSL の設定を開始するには、Braze カスタマーサクセスマネージャーに連絡して、Braze メールの完全なセットアップを開始してください。

Braze がセットアップを開始した後、以下のステップに従ってください。
1. Braze がドメインレジストリに追加する DNS レコードを提供します。
2. Braze がレコードがレジストリに正しく追加されたかどうかを確認します。
3. その後、CDN を選択し、サードパーティプロバイダーから SSL 証明書を取得します。
4. この時点で CDN を設定します。Braze は CDN 設定のトラブルシューティングをサポートできません。詳細なサポートについては、CDN プロバイダーにお問い合わせください。
5. カスタマーサクセスマネージャーに連絡して、SSL を有効にしてもらいます。

## CDN とは何か、なぜ必要なのか

コンテンツデリバリーネットワーク (CDN) は、セキュリティ証明書の処理も行いながら、複数のメディアにわたるコンテンツの高速な読み込み時間を確保するサーバープラットフォームです。

{% alert important %}
CDN の設定は、常に Braze による DNS レコードの検証が完了した後に行います。このステップをまだ開始していない場合は、カスタマーサクセスマネージャーに連絡して、開始方法の詳細情報を確認してください。
{% endalert %}

クリックおよび開封トラッキングでは、配信パートナーがブランド化されたサブドメインを使用してリンクを変換し、CDN がそれらの変換されたリンクに SSL 証明書を適用します。パートナーは、リンクや画像を正しく表示するために、受信者のブラウザーに有効な証明書を提示する必要があることが多いです。Braze は証明書のリクエストや管理を行わないため、CDN を通じてこの設定を行う必要があります。

{% alert note %}
SSL のクリックおよび開封トラッキングに記載されている CDN を使用できない場合や使用したくない場合は、カスタム SSL 設定をセットアップできます。代替の CDN やカスタムプロキシを使用すると、設定がより複雑になる場合があります。[SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) および [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) のドキュメントを参照してください。
{% endalert %}

### その他のリソース

{% alert important %}
CDN 設定のトラブルシューティングについては、CDN プロバイダーにお問い合わせください。
{% endalert %}

特定の CDN の設定方法については、メールサービスプロバイダー (ESP) パートナーによる以下のリソースを参照してください。お使いの CDN が一覧にない場合でも、CDN が SSL 証明書を適用できることを確認してください。

CDN のクリックトラッキングドメインを設定する際は、ホストヘッダー攻撃などの潜在的なセキュリティ問題を防ぐために、`X-Forwarded-Host` ヘッダーを有効にしてください。手順については、CDN のドキュメントまたはサポートチームを参照してください。

| パートナー | CDN | ドキュメント |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [CloudFront での HTTPS の使用](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [SSL/TLS の使用を開始する](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Fastly が管理する証明書を使用した TLS の設定](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [カスタム SSL の設定方法](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google マネージド SSL 証明書](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [CloudFront を使用したクリックトラッキング用 SSL の設定方法](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [CloudFlare の使用](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Fastly の使用](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [KeyCDN の使用](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [AWS CloudFront を使用したステップバイステップガイド](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Cloudflare を使用したステップバイステップガイド](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Fastly を使用したステップバイステップガイド](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Google Cloud Platform を使用したステップバイステップガイド](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Microsoft Azure を使用したステップバイステップガイド](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Amazon SES

CDN として Amazon SES を使用している場合は、[Amazon SES のドキュメント](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html)の **Option 2: Configuring an HTTPS domain** を参照し、Braze クラスターに基づいてリージョン別の AWS トラッキングドメインを指定してください。

- **Braze US クラスター:** `r.us-east-1.awstrack.me`
- **Braze EU クラスター:** `r.eu-central-1.awstrack.me`

## トラブルシューティング

CDN の設定、証明書、プロキシの問題は CDN プロバイダーに対応を依頼する必要がありますが、一般的な SSL クリックトラッキングの問題を特定するために以下のヒントを活用してください。

### メール開封率が低い

メール開封率が突然低下した場合は、SSL 証明書が最新であることを確認してください。有効期限が切れている場合は、CDN または証明書プロバイダーで SSL 証明書を更新する必要があります。

### ドメインレジストリの問題

dig コマンドを実行して、リンクトラッキングが CDN を指していることを確認してください。ターミナルで `dig CNAME link_tracking_subdomain` を実行します。`ANSWER SECTION` に CNAME の指し先が表示されます。CDN ではなくメールサービスプロバイダー (SendGrid または SparkPost) を指している場合は、ドメインレジストリを CDN を指すように再設定してください。

### CDN の問題

セットアップ中にライブメールのリンクが破損する場合は、適切な設定が完了する前に DNS を CDN に向けた可能性があります。これは「間違ったリンク」エラーとして表示されることがあります。CDN プロバイダーに連絡し、そのドキュメントを確認して設定のトラブルシューティングを行ってください。

接続がプライベートではないというエラーメッセージが表示される場合は、SSL または CDN が正しく設定されていない可能性があります。ターミナルで `dig` コマンドを実行してください（例: `dig CNAME your_link_tracking_subdomain`）。`ANSWER SECTION` で、結果が CDN ではなく ESP を指している場合、設定ミスが原因です。Braze の SSL クリックトラッキングが機能するには、CNAME が CDN を指している必要があります。SSL と CDN の設定を管理しているチームと連携して、さらなるサポートを受けてください。

### SSL 有効化のステータス

SSL の設定を完了してもリンクが HTTP のまま表示される場合は、Braze カスタマーサクセスマネージャーに連絡して、Braze が SSL を有効にしたことを確認してください。Braze は、すべてのセットアップステップが完了した後にのみ SSL を有効にします。