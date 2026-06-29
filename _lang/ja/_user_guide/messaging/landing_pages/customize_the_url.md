---
nav_title: URLのカスタマイズ
article_title: URLのカスタマイズ
description: "ドメインをBrazeワークスペースに接続して、ランディングページのURLを自社ブランドでカスタマイズする方法を説明します。"
page_order: 1
---

# ランディングページURLのカスタマイズ {#customize-landing-page-urls}

> ドメインをBrazeワークスペースに接続して、ランディングページのURLを自社ブランドでカスタマイズする方法を説明します。

## 仕組み {#how-it-works}

[ドメインをBrazeに接続](#connect-your-domain-to-braze)すると、そのドメインがすべてのランディングページのデフォルトドメインとして使用されます。たとえば、サブドメイン`forms.example.com`を接続した場合、ランディングページのURLは`forms.example.com/holiday-sale`のようになります。

Brazeアカウントに接続できるカスタムドメインの数は、[プランティア]({{site.baseurl}}/user_guide/messaging/landing_pages/#plan-tiers)によって異なります。上限を引き上げるには、Brazeアカウントマネージャーにお問い合わせください。

## ドメインをBrazeに接続する {#connect-your-domain-to-braze}

ドメインをBrazeアカウントに接続するには、管理者が以下の手順に従ってください。

1. **Settings** > **Landing Page Settings**に移動します。
2. 接続するドメインを入力し、**Submit**を選択します。たとえば、`forms.example.com`と入力します。
3. **TXT**レコードと**CNAME**レコードをコピーして、ドメインプロバイダーのDNS設定に貼り付けます。
4. Brazeダッシュボードに戻り、接続を確認します。

![ランディングページの設定ページ。1つのTXTレコードと2つのCNAMEレコードが、それぞれの名前と値とともに表示されています。]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
ドメインプロバイダーによっては、接続に最大48時間かかる場合があります。プロセスが完了すると、Brazeダッシュボードのランディングページにカスタムドメインが使用されるようになります。
{% endalert %}

### SSL証明書の設定 {#ssl-certificate-setup}

Brazeは、Cloudflareを使用して[ACME DNS-01チャレンジ](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge)を通じてカスタムドメインのSSL証明書を自動的にプロビジョニングします。この継続的な検証方法は、セットアップ時に提供したCNAMEレコードの1つによって有効になり、証明書認証局（LetsEncrypt）がBrazeにドメインの所有権を持たせることなく、DNSレコードを通じてドメインの所有権を確認できるようにします。

## ドメインを削除する {#remove-your-domain}

Braze管理者の場合、以下の手順で以前に設定したドメインを削除できます。

1. **Settings** > **Landing Page Settings**に移動します。
2. **Remove Custom Domain**を選択します。
3. ドメインの削除を確認します。
4. ドメイン設定から、表示されているDNSレコードを削除します。

{% alert important %}
カスタムドメインを削除すると、そのURLは無効になります。このドメインを使用していたランディングページは、Brazeが設定したデフォルトドメインに自動的に戻ります。
{% endalert %}

## ドメインを移行する {#migrate-your-domain}

カスタムドメインを別のワークスペースに移行するには：

1. カスタムドメインを削除します。
2. 移行先のワークスペースで新しいカスタムドメインを作成します。
3. 新しいDNSレコードでカスタムドメインを再設定します。このプロセス中、サブドメインは利用できなくなりますのでご注意ください。

## DNSリソース {#dns-resources}

{% multi_lang_include channels/email/dns_records.md %}

## トラブルシューティング {#troubleshooting}

### ドメイン接続に失敗した場合 {#my-domain-connection-failed}

ドメインが正しく入力されていること、およびドメインプロバイダーアカウントからBrazeに送信した内容と一致していることを確認してください。正しく一致している場合は、Brazeが提供したTXTレコードとCNAMEレコードを確認してください。ドメインプロバイダーアカウントに入力したレコードと一致している必要があります。

## よくある質問 {#frequently-asked-questions}

### カスタムドメインにネストされたサブドメインを使用できますか？ {#can-i-use-nested-subdomains-for-my-custom-domain}

はい、ランディングページにネストされたサブドメインを使用できます。たとえば、`forms.braze.com`、`pages.forms.braze.com`、またはそれ以上の深い階層もすべてサポートされています。唯一の制約は、BrazeがCNAMEレコードを使用して接続するため、エイペックスドメイン（`braze.com`など）は使用できないことです。

### ワークスペースに複数のサブドメインを接続したり、1つのサブドメインを複数のワークスペースに接続したりできますか？ {#can-i-connect-multiple-subdomains-to-my-workspace-or-connect-one-subdomain-to-multiple-workspaces}

いいえ、現在は1つのサブドメインを1つのワークスペースにのみ接続できます。

### メインWebサイトや送信ドメインに現在使用しているサブドメインと同じものを使用できますか？ {#can-i-use-the-same-subdomain-that-i-currently-use-for-my-main-website-or-my-sending-domain}

いいえ、すでに使用中のサブドメインは使用できません。これらのサブドメインは有効ですが、他の目的にすでに割り当てられている場合や、必要なCNAMEレコードと競合するDNSレコードがある場合は、ランディングページには使用できません。

### DNSレコードが有効なのに、カスタムドメインが「接続中」のままになっているのはなぜですか？ {#why-is-my-custom-domain-stuck-on-connecting-despite-valid-dns-records}

カスタムドメインのすべてのDNSレコードが「接続済み」と表示されているにもかかわらず、ドメインのステータスが4時間以上「接続中」のままの場合、組織がCAA（Certificate Authority Authorization）レコードまたはCloudflareゾーンホールドを使用しており、Brazeがページを保護できない可能性があります。

#### CAAレコード {#caa-records}

CAAレコードは、ドメインのSSL証明書を発行できる認証局を制限します。CAAレコードにLetsEncryptが含まれていない場合、Braze（Cloudflare経由）は必要なSSL証明書を発行できません。

これを解決するには、ITチームにサブドメインに以下の値でCAAレコードを追加するよう依頼してください。
- **レコードタイプ:** CAA
- **値:** `0 issue "letsencrypt.org"`

詳細については、[LetsEncryptのCAAドキュメント](https://letsencrypt.org/docs/caa/)を参照してください。

#### Cloudflareゾーンホールド {#cloudflare-zone-holds}

組織がCloudflareを使用している場合、ゾーンホールドセキュリティ機能がBrazeによるカスタムドメインの作成を妨げている可能性があります。

これを解決するには、ITチームにゾーンホールドを一時的に解除するよう依頼してください。詳細については、[Cloudflareのゾーンホールドドキュメント](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds)を参照してください。

#### 検証プロセスの再開 {#restarting-the-validation-process}

いずれかの問題を解決した後、Brazeダッシュボードでカスタムドメインを削除して再作成し、検証プロセスを再開してください。

### リバースプロキシを使用して、メインドメインやサブディレクトリでランディングページを配信できますか？ {#can-i-use-a-reverse-proxy-to-serve-landing-pages-under-my-main-domain-or-a-subdirectory}

いいえ、ランディングページのURL Liquidタグはリバースプロキシでは正しく動作しません。