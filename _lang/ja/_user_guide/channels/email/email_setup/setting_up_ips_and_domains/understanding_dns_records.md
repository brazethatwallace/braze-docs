---
nav_title: DNSレコードの理解
article_title: DNSレコードの理解
page_order: 2
page_type: reference
description: "このリファレンス記事では、SPF、DKIM、DMARC、およびメールサービスプロバイダー (ESP) 固有のレコード構造を含め、Brazeのメールサービスプロバイダー全体でDNSレコードがどのように機能するかを説明します。"
channel: email
---

# DNSレコードの理解 {#understanding-dns-records}

> このリファレンスでは、SparkPost、SendGrid、Amazon Simple Email Service (SES) の3つの主要なメールサービスプロバイダー (ESP) において、Braze全体でDNSレコードがどのように機能するかを説明します。適切なDNS設定はメール認証 (SPF、DKIM、DMARC) とブランドの整合性に不可欠であり、到達率に直接影響します。

詳細については、[メール認証]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication)を参照してください。

## メール認証の基本 {#core-email-authentication-fundamentals}

プロバイダー固有の構成を確認する前に、これらのレコードが何を行い、Brazeがどのようにそれらを使用して適切なアライメントを実現しているかを理解しましょう。

### Sender Policy Framework (SPF) {#spf}

SPFは、ドメイン上のDNSレコードであり、そのドメインに代わってメールを送信することが許可されているIPアドレスを指定します。

Brazeでは、企業のルートドメイン（`example.com`など）のSPFレコードを変更または追加する必要はありません。代わりに、Brazeは専用のカスタムReturn-Pathドメイン（バウンスドメイン、MAIL FROMドメイン、またはエンベロープFromドメインとも呼ばれます）を使用して配信を分離します（例：`bounce.mail.example.com`）。

受信メールボックスプロバイダーは、表示される`From:`ヘッダードメインではなく、このReturn-Pathドメインに対してSPFを検証するため、SPF設定はサブドメインレベルに完全に存在します。基盤となるメールサービスプロバイダー (ESP) に応じて、Brazeはこの検証を2つの方法のいずれかで処理します。

- CNAME委任（SendGridおよびSparkPost）：サブドメインをESPに戻す`CNAME`を作成します。ESPは自社のインフラでSPFポリシーをホストおよび更新し、SPFチェックを自動的にパスします。
- 明示的TXTレコード（Amazon SES）：バウンスサブドメインに明示的な認証文字列を含むハードコードされた`TXT`レコードを直接公開します（例：`v=spf1 include:amazonses.com ~all`）。これにより、AWSにそのゾーンからメールを送信する権限が付与されます。

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIMは、メールヘッダーに暗号デジタル署名を追加します。受信サーバーは、送信者の公開キー（DNSで公開）を使用して、メールがドメイン所有者から発信され、転送中に改ざんされていないことを検証します。

Brazeでは、受信ISPがESPによって生成された暗号署名を検証できるように、公開DKIMキーを`TXT`または`CNAME`レコードを通じて公開する必要があります。

### DMARCアライメント {#dmarc}

メールがDMARCをパスするには、ユーザーに表示される`From:`ヘッダーのドメインが、SPF（Return-Path）またはDKIMのいずれかによって検証されたドメインと一致（アライメント）する必要があります。Brazeの設定はSPFとDKIMの両方を通じてアライメントを実現するため、DMARCポリシーは安全に満たされます。

BrazeはデフォルトでベースラインのSPFおよびDKIM認証を処理しますが、送信ドメインにDMARCレコードを追加する必要があります。DMARCは、ほぼすべての主要な受信トレイプロバイダーが要求する重要な認証ツールです。メールが正当であることを証明し、ドメインの評価を構築し、長期的に配信到達性を健全に保ちます。

これには企業のドメインレジストリへのアクセスが必要なため、あなたまたはネットワーク管理者がルートドメインレベルでこのレコードを追加する必要があります。始めたばかりの場合、`p=none`のような基本的なポリシーで受信トレイの最低要件を満たすことができます。DMARCの詳細については、[DMARC.org](https://dmarc.org/)を参照してください。Braze固有のDMARCガイダンスについては、[メール認証]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc)を参照してください。

## メールサービスプロバイダー (ESP) 固有の DNS アーキテクチャ {#esp-specific-dns-architecture}

ESP のアーキテクチャによって、DNS 委任の処理方法は異なります。環境をプロビジョニングする際は、使用する ESP クラスターに対応する正確なレコードを使用してください。

### SparkPost アーキテクチャ {#sparkpost-architecture}

SparkPost はハイブリッド構成を使用します。明示的な `CNAME` レコードを使用してトラッキングと Return-Path インフラを SparkPost に向けつつ、DKIM 認証には生の `TXT` レコードを使用します。

- SPF と Return-Path の設定: SparkPost はバウンス用に指定されたサブドメイン（例: `mail.example.com`）を要求します。`CNAME` レコードがこのサブドメインを SparkPost のインバウンドバウンスプロセッサーに向けます。これによりバウンストラフィックが正しくルーティングされ、SparkPost の宛先サーバーがプロトコルを管理するため、SPF が自動的に検証されます。
- DKIM の設定: SparkPost は、特定のセレクターにマッピングされた正確な公開キー文字列を含む `TXT` レコードを必要とします。
- クリックおよび開封トラッキング: SparkPost のトラッキングエンドポイント（SSL トラッキングが要求される場合は CDN プロキシ）を指す `CNAME` でトラッキングサブドメインを設定します。

#### SparkPost DNS テーブルの例 {#example-sparkpost-dns-table}

以下の表は、SparkPost 構成の DNS レコードの例を示しています。

| レコードタイプ | ホスト/名前 | 値/ターゲット | 目的 |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Return-Path / SPF アライメント |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | 暗号化 DKIM 認証 |
| CNAME | click.mail.example.com | spgo.io（または CDN エンドポイント） | クリックおよび開封トラッキング |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SparkPost DNS テーブルの例" }

### SendGrid アーキテクチャ {#sendgrid-architecture}

SendGrid は、Domain Authentication と呼ばれる自動化されたインフラに依存しています。生の `TXT` キーを提供する代わりに、SendGrid は SendGrid が管理するサーバーを直接指す一連の `CNAME` レコードを提供します。

- SPF と Return-Path の設定: SendGrid は、送信サブドメインを `uXXXXXX.wl.sendgrid.net` にマッピングする特定の `CNAME`（多くの場合 `em` プレフィックス付き）を使用します。SendGrid はそのエンドポイント上で SPF レコードをホストし、動的に更新します。
- DKIM の設定: SendGrid は DKIM 用に2つの個別の `CNAME` レコードを生成します（多くの場合 `s1` や `s2` などのセレクターを使用）。これらは SendGrid のキーを指します。
- SendGrid が2つの DKIM `CNAME` レコードを提供するのは、DNS を手動で更新することなく暗号キーを自動的にローテーションできるようにするためです。

#### SendGrid DNS テーブルの例 {#example-sendgrid-dns-table}

以下の表は、SendGrid 構成の DNS レコードの例を示しています。

| レコードタイプ | ホスト/名前 | 値/ターゲット | 目的 |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.sendgrid.net | Return-Path / ダイナミック SPF |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.sendgrid.net | プライマリ DKIM キー（ローテーション） |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.sendgrid.net | セカンダリ DKIM キー（ローテーション） |
| CNAME | email.mail.example.com | sendgrid.net（または CDN エンドポイント） | クリックおよび開封トラッキング |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SendGrid DNS テーブルの例" }

### Amazon SES アーキテクチャ {#amazon-ses-architecture}

Amazon SES は、カスタマイズされたバウンストラッキング用の明示的な `MX` および `TXT` ルーティングとともに、`CNAME` レコードを使用した Easy DKIM を使用します。

- DKIM の設定: Amazon SES は Easy DKIM を使用し、3つの `CNAME` レコードを提供します。これらは公開キーを含む AWS 管理のサブドメインを指します。SES はセキュリティコンプライアンスを維持するために、これらのキーを透過的に自動ローテーションします。
- SPF とカスタム MAIL FROM の設定: SendGrid と SparkPost は `CNAME` を通じてバウンスドメインのルーティングを管理します。Amazon SES では、指定された MAIL FROM サブドメインに直接配置される明示的な `MX` レコードと `TXT` レコードが必要です。`MX` レコードはバウンス通知が Amazon のサーバーに返されることを保証し、`TXT` レコードには承認済みのハードコードされた SPF 文字列が含まれます。

詳細については、[Amazon SES の設定]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses)を参照してください。

#### Amazon SES DNS テーブルの例 {#example-amazon-ses-dns-table}

以下の表は、Amazon SES 構成の DNS レコードの例を示しています。

| レコードタイプ | ホスト/名前 | 値/ターゲット | 目的 |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Easy DKIM キー 1（ローテーション） |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Easy DKIM キー 2（ローテーション） |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Easy DKIM キー 3（ローテーション） |
| MX | bounce.mail.example.com | 10 フィードバック-smtp.us-east-1.amazonses.com | バウンス処理を AWS にルーティング |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | 明示的な SPF 承認 |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me（または CDN） | クリックおよび開封トラッキング |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Amazon SES DNS テーブルの例" }

## 高度なDNSに関する考慮事項 {#advanced-dns-considerations}

### TXT DKIMレコードの文字列分割 {#txt-dkim-record-string-splitting}

SparkPostまたは手動のDKIMセットアップをデプロイする際、長い暗号キー（2048ビットDKIMキー）に遭遇することがあります。

コアDNS仕様（RFC 1035）では、`TXT`レコード内の単一の文字列は最大255文字に制限されています。2048ビットの公開キーは通常400文字を超えるため、ドメインレジストリが単一の文字列を拒否するか、切り捨ててしまい、署名が無効になります。

文字列分割によってこの問題を解決できます。文字列を255文字未満のチャンクに分割し、同じ`TXT`レコード内で各チャンクをストレート引用符で囲み、スペースで区切ります。

{% alert note %}
CloudflareやAWS Route 53などのDNSプロバイダーを使用する場合、これらのインターフェイスは長い文字列を貼り付けると自動的に分割を処理します。レガシーシステム（GoDaddyやNetwork Solutionsなど）では、ダブルクォートのテクニックを使用して手動で分割をフォーマットする必要があります。
{% endalert %}

### 専用サブドメインの使用 {#dedicated-subdomains}

オンボーディング時によくあるエラーは、トップレベルの組織ドメイン（`example.com`など）をBrazeの送信ドメインとして直接使用しようとすることです。Brazeでは、専用のサブドメイン（例：`mail.example.com`や`engage.example.com`）を使用する必要があります。

親ドメインを使用すると、以下の方法で企業インフラに支障をきたす可能性があります。

#### MXレコードの競合 {#mx-record-conflicts}

ドメインがサポートできるプライマリルーティング`MX`レコードのセットは1つだけです。親ドメイン（`example.com`）をBrazeのメールサービスプロバイダー (ESP) インフラにマッピングすると、バウンスに必要なカスタム`MX`レコードが企業メールレコードを上書きします。これにより、Google WorkspaceやMicrosoft 365などの企業内部メッセージングプラットフォームに支障が生じる可能性があります。

#### SPFインクルードの肥大化と10ルックアップ制限 {#spf-include-bloat-and-the-10-lookup-limit}

SPF仕様（RFC 7208）では、SPFレコードの検証時に受信メールサーバーが実行できるDNSルックアップは最大10回に制限されています。

- 親ドメインにBrazeのESPメカニズム（`include:sparkpostmail.com`や`include:amazonses.com`）を追加すると、この制限に対して大きくカウントされます。
- 制限を超えると、恒久的なSPF PermErrorがトリガーされ、すべての企業メールが認証に失敗します。

#### IPおよびドメインレピュテーションの分離 {#ip-and-domain-reputation-isolation}

マーケティングキャンペーン、トランザクションレシート、および社内従業員メールが同一のルートドメインスペースを共有している場合、マーケティングスパムの苦情が急増すると、親ドメインのレピュテーションが損なわれる可能性があります。これにより、重要な企業コミュニケーションがスパムフォルダーにルーティングされるリスクがあります。専用のサブドメインを使用することで、マーケティングアウトリーチのレピュテーションを分離できます。

## 実装ワークフロー {#implementation-workflow}

スムーズな引き継ぎと実装を確保するために、以下の手順に従ってください。

1. 構造化されたレコードをIT担当者またはネットワーク管理者に提供し、ホスティングプラットフォーム（Cloudflare、Route 53など）に追加してもらいます。
2. 初期テスト用に、短いTTL（Time-To-Live）値（例：300秒または5分）を設定します。これにより、入力時にタイプミスがあった場合でも迅速に復旧できます。
3. DNSルックアップ（例：`dig CNAME mail.example.com`）を実行するか、検証ツールを使用して、ウォーミングフェーズに進む前にレコードが正しく解決されることを確認します。

## DNSプロバイダーのドキュメント {#dns-provider-documentation}

DNSプロバイダーごとにインターフェイスは異なります。これらの仕様をネットワーク管理者と共有するか、お使いのプロバイダーのドキュメントを参照して、ゾーンファイルにエントリを正しくマッピングしてください。

以下の表は、一般的に使用されるDNSプロバイダーの公式ドキュメントの一覧です。

| DNSプロバイダー | リソース |
| --- | --- |
| Cloudflare | [DNSレコードの管理](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [リソースレコードセットの作成](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [DNSレコードの管理](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [ドメイン名のDNSレコードの設定](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Azureポータルを使用したDNSレコードの管理](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="DNSプロバイダーのドキュメント" }

ドメインプロバイダーに関するその他のリソースについては、[IPとドメインの設定]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-2-add-and-verify-a-sending-domain)を参照してください。