---
nav_title: トラブルシューティング
article_title: SSLクリックトラッキングのトラブルシューティング
page_order: 5
page_type: reference
description: "症状インデックスと標準的な調査パスを使用して、SSLクリックトラッキングおよびCDN設定の問題を診断します。"
channel: email
---

# SSLクリックトラッキングのトラブルシューティング {#troubleshoot-ssl-click-tracking}

> このページでは、SSLクリックトラッキングに関する一般的な問題を特定します。以下のガイダンスは、CDNがそれぞれ固有であるため、一般的な内容となっています。CDNの設定、証明書、またはプロキシの問題については、CDNのサポートチームにお問い合わせください。これらの設定はBrazeの外部で行われます。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
| --- | --- |
| メールの開封率が突然低下した | [メール開封率が低い](#low-email-open-rates) |
| トラッキングリンクがHTTP 403を返す | [リダイレクトリンクでHTTP 403が発生する](#http-403-on-redirect-links) |
| DNSまたはCNAMEがCDNではなくESPを指している | [ドメインレジストリの問題](#domain-registry-issues) |
| 「接続がプライベートではありません」と表示される、または設定中にリンクが壊れる | [CDNの問題](#cdn-issues) |
| SSLの設定が完了したがリンクがまだHTTPのまま | [SSLの有効化ステータス](#ssl-enablement-status) |
| トラッキングURLが失敗するが、トラッキングなしのURLは機能する | [クリックトラッキングの問題](#click-tracking-issues) |
| Amazon SES固有のSSL有効化エラー | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SSLの症状" }

## 標準的な調査パス {#standard-investigation-path}

1. クリックトラッキングサブドメインが、メールサービスプロバイダー（ESP）（SendGrid、SparkPost、またはAmazon SES）ではなく、[コンテンツデリバリーネットワーク（CDN）]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it)を指していることを確認してください。ITチームまたはWebチームに、ドメイン設定がBrazeの設定と一致しているか確認を依頼してください。Brazeの要件については、[SSL証明書の取得]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)を参照してください。
2. トラッキングドメインのSSL証明書が有効であることを確認してください。ITチームまたはWebチームに、証明書が最新であり、クリックトラッキングサブドメインをカバーしていることを確認してもらってください。設定手順とCDN固有のガイドについては、[SSL証明書の取得]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)と[その他のリソース]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources)を参照してください。
3. [クリックトラッキングのトラブルシューティングテンプレート](#click-tracking-issues)を使用してテストメールを送信してください。トラッキングされたURLとトラッキングされていないURLを比較してください。
4. トラッキングされたリンクが403エラーで失敗する場合は、CDNとWAFのルール（ユーザーエージェント、クエリ文字列、リダイレクトパターン）を確認してください。
5. 設定が完了しているにもかかわらずリンクがHTTPのままの場合は、Brazeのカスタマーサクセスマネージャーに連絡して、BrazeがSSLを有効にしたことを確認してください。
6. 問題が解決しない場合は、CDNチームまたはITチームと連携し、エラーコードとCDNまたはドメインプロバイダーからの詳細情報を添えて[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。

## 主要な概念 {#key-concepts}

- **トラッキングURL：** 元のHTTPSリンクをトラッキングドメインでラップします。ユーザーがクリックすると、トラッキングドメインがリクエストを解決し、最終的な宛先にリダイレクトします。CDNを使用すると、セキュアな（HTTPS）URLをトラッキングできます。CDNがない場合、ユーザーに「接続が安全ではありません」というプライバシーエラーが表示されることがあります。
- **非トラッキングURL：** 元のURLをそのまま維持し、CDNをバイパスしてコントロール環境として機能します。

## メール開封率が低い {#low-email-open-rates}

**症状：** SSLまたはCDNの変更後にメール開封率が突然低下した。

メール開封率が突然低下している場合は、SSL証明書が最新であることを確認してください。有効期限が切れている場合は、CDNまたは証明書プロバイダーでSSL証明書を更新する必要があります。

## リダイレクトリンクでHTTP 403が発生する {#http-403-on-redirect-links}

**症状：** トラッキングされたメールリンクが「403 Forbidden」を返す。

トラッキングされたリダイレクトリンクが「403 Forbidden」を返す場合、障害はコンテンツデリバリーネットワーク（CDN）またはWebアプリケーションファイアウォール（WAF）で発生していることが多いです。たとえば、AWS WAFやAmazon CloudFrontのルールが特定のユーザーエージェント、クエリ文字列、またはリダイレクトパターンをブロックしている場合があります。CDNまたはクラウドプロバイダーでブロックされたリクエストのログとメトリクスを確認してください。AWSについては、[CloudFrontの問題のトラブルシューティング](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html)を参照してください。

問題がクリックトラッキングに固有のものかどうかを確認するには、1つのテストリンクでクリックトラッキングをオフにしてください（[リンクごとにクリックトラッキングをオフにする]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)を参照）。クリックトラッキングがオフの場合に送信先URLが読み込まれ、トラッキングがオンの場合に403が返される場合は、クリックトラッキングドメイン、CDN、およびWAFの設定に焦点を当ててください。

## ドメインレジストリの問題 {#domain-registry-issues}

**症状：** トラッキングサブドメインのDNSまたはCNAMEが、CDNではなくESPを指している。

digコマンドを実行して、リンクトラッキングがCDNを指していることを確認してください。ターミナルで`dig CNAME link_tracking_subdomain`を実行します。`ANSWER SECTION`に、CNAMEの指す先が表示されます。CDNではなくメールサービスプロバイダー（ESP）（SendGrid、SparkPost、またはAmazon SES）を指している場合は、ドメインレジストリをCDNを指すように再設定してください。

## CDNの問題 {#cdn-issues}

**症状：** ユーザーに「接続がプライベートではありません」というエラーが表示される、またはCDNセットアップ中にリンクが壊れる。

セットアップ中にライブメールリンクが壊れた場合、適切な設定が完了する前にDNSをCDNに向けた可能性があります。これは「間違ったリンク」エラーとして表示されることがあります。CDNプロバイダーに連絡し、ドキュメントを確認して設定のトラブルシューティングを行ってください。

接続がプライベートではないというエラーメッセージが表示された場合、SSLまたはCDNが正しく設定されていない可能性があります。ターミナルで`dig`コマンドを実行してください（例：`dig CNAME your_link_tracking_subdomain`）。`ANSWER SECTION`で、結果がCDNではなくESPを指している場合、設定ミスの問題です。BrazeのSSLクリックトラッキングが機能するには、CNAMEがCDNを指している必要があります。SSLとCDNの設定を管理するチームと連携して、さらなるサポートを受けてください。

## SSLの有効化ステータス {#ssl-enablement-status}

**症状：** SSLの設定が完了しているのに、トラッキングリンクがHTTPのまま表示される。

SSLの設定を完了してもリンクがHTTPのまま表示される場合は、Brazeのカスタマーサクセスマネージャーに連絡して、BrazeがSSLを有効にしたことを確認してください。Brazeは、すべての設定ステップが完了した後にのみSSLを有効にします。

### Amazon SES {#amazon-ses}

メールサービスプロバイダー（ESP）としてAmazon SESを使用している場合、以下の設定の問題がBrazeのSSL有効化を妨げたり、設定中にエラーを引き起こしたりする可能性があります。

- **リージョンの不一致：** CDNのオリジンがBrazeクラスターのAWSトラッキングドメインを指していることを確認してください。USクラスターは`r.us-east-1.awstrack.me`を使用します。EUクラスターは`r.eu-central-1.awstrack.me`を使用します。間違ったリージョンを使用すると、SSLの有効化がブロックされる可能性があります。
- **ホストヘッダー：** Amazon SESでは、CDNが正しいホストヘッダーを転送する必要があります。クリックトラッキングドメインで`X-Forwarded-Host`ヘッダーを有効にしてください。詳細については、[Amazon SES](#amazon-ses)セクションを参照してください。
- **プロキシ設定：** ホストヘッダーを上書きまたは競合するプロキシやCDNの設定は、SSLの有効化を失敗させる可能性があります。CDNプロバイダーとプロキシ設定を確認し、ホストヘッダーの転送を妨げていないことを確認してください。
- **Route 53エイリアスレコード：** Route 53を使用してドメインのDNSを管理している場合は、CDNディストリビューション（例：`d111111abcdef8.cloudfront.net`）を指す[Route 53のエイリアスレコード](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html)を作成してください。エイリアスレコードの代わりに標準のCNAMEを使用すると、HTTP 400エラーが返される可能性があります。
- **ヘッダー転送の無効化：** `X-Forwarded-Host`を設定した後もSSLの有効化が失敗する場合は、CDNまたはプロキシでヘッダー転送を無効にしてみてください。一部の設定では、転送を完全にオフにすることで問題が解決します。ITチームまたはCDNプロバイダーと協力して、この設定をテストしてください。

## クリックトラッキングの問題 {#click-tracking-issues}

**症状：** トラッキングされたメールリンクが失敗するが、トラッキングされていないリンクは機能する。またはユーザーがクリック後に証明書エラーやDNSエラーが表示される。

一般的なリダイレクトの問題は、トラッキングドメインをホストするCDNと、関連するSSL証明書またはDNS CNAMEレコードとの間の不適切な設定に起因することが多いです。これらの設定ミスにより、ユーザーがトラッキングされたメールリンクをクリックした後に「接続が安全ではありません」というプライバシーエラーや`404`エラーが発生することがよくあります。

以下のテンプレートを使用して、トラッキングドメインのCDN設定をテストしてください。これは、メール内のリンクの分析をサポートするメカニズムです。

1. 以下のテンプレートをコピーして、BrazeのHTMLメールキャンペーンに貼り付けてください。

{% details クリックトラッキングのトラブルシューティングテンプレート %}
{% raw %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body {
            margin: 0;
            padding: 0;
            background-color: #2b0562;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            color: #ffd1e9;
        }

        .email-container {
            width: 100%;
            max-width: 600px;
            margin: 40px auto;
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid #F3697F;
            border-radius: 16px;
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%);
            padding: 40px 20px 50px 20px;
            text-align: center;
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }

        .header h1 {
            color: #ffffff;
            margin: 0;
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        .content {
            padding: 40px 40px 20px 40px;
            line-height: 1.8;
            font-size: 15px;
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }

        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section {
            padding: 0 40px 40px 40px;
            text-align: center;
        }

        .btn {
            display: inline-block;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 700;
            text-decoration: none;
            margin: 10px;
            font-size: 14px;
        }

        .btn-tracked {
            background-color: #F3697F;
            color: #ffffff;
        }

        .btn-untracked {
            border: 2px solid #FDA7D8;
            color: #FDA7D8;
            background-color: transparent;
        }

        .footer {
            text-align: center;
            font-size: 12px;
            color: #FDA7D8;
            padding-bottom: 40px;
            opacity: 0.6;
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137"
                         width="150"
                         alt="Logo"
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>

                    <a href="{{url}}"
                       class="btn btn-untracked"
                       clicktracking="off"
                       data-msys-clicktrack="0"
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% endraw %}
{% enddetails %}

{: start="2"}
2. URLを設定します。テンプレート本文の上部付近にある`capture`タグ内のURL（`https://example.com`が設定されている箇所）を置き換えてください。たとえば、`https://example.com`を`https://braze.com/docs`に置き換えます。
3. 自分宛にテストメールを送信し、両方のボタンを選択してください。
4. 期待される動作と成功基準がテンプレートに記載されている通りであることを確認してください。

非トラッキングURLは機能するがトラッキングURLが失敗する場合、設定にギャップがある可能性があります。トラブルシューティングするには、お使いのESPとCDNプロバイダーのドキュメントを参照してください。証明書のプロビジョニングに関する詳細な要件については、[BrazeのSSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl)も確認できます。

以下の表を使用して、クリックトラッキングのテスト時に発生する一般的なエラーを診断してください。

| エラーコード | トラブルシューティング |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | トラッキングドメインに有効なSSL証明書があることを確認してください。 |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | DNS設定を確認してください。トラッキングサブドメインがCDNとESPの推奨設定に従って構成されていることを確認してください。 |
| `525 / 526 SSL Error` | CDN（Cloudflareなど）のSSL設定がOriginの機能と一致していることを確認してください。 |
| `404 Not Found` | CDNが空のルートディレクトリを指すのではなく、URLパス全体をESPに転送するように設定されていることを確認してください。 |
| `400 Bad Request: Request Header or Cookie Too Large` | このエラーは通常、クリックトラッキングドメインがWebサイトのドメインから大量のCookieを継承している場合に発生します。Brazeはトラッキングドメインにおいてcookieの設定やブロックを行いません。CDNがクリックトラッキングリクエストをリバースプロキシする際に、それらのCookieをESPに送信しないように設定してください。nginx設定の`large_client_header_buffers`設定を増やす必要がある場合もあります（例：`large_client_header_buffers 4 32k;`で最大32&nbsp;KBのヘッダーを許可）。詳細については、CDNプロバイダーまたはWebサイト開発チームにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エラーコードとトラブルシューティング" }