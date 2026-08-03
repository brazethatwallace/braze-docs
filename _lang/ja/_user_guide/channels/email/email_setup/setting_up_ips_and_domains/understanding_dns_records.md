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

プロバイダー固有の構造を確認する前に、これらのレコードが何をするのか、そしてBrazeがどのようにそれらを使用して適切なアライメントを実現するのかを理解しましょう。

### Sender Policy Framework (SPF) {#spf}

SPFは、ドメイン上のDNSレコードであり、そのドメインに代わってメールを送信することが許可されているIPアドレスを指定します。

Brazeは、企業のルートドメイン（`example.com`など）のSPFレコードを変更または追加することを求めません。代わりに、Brazeは専用のカスタムReturn-Pathドメイン（バウンスドメイン、MAIL FROMドメイン、またはエンベロープFromドメインとも呼ばれます）を使用して配信を分離します（例：`bounce.mail.example.com`）。

受信メールボックスプロバイダーは、表示される`From:`ヘッダードメインではなく、このReturn-Pathドメインに対してSPFを検証するため、SPF設定は完全にサブドメインレベルに存在します。基盤となるESPに応じて、Brazeはこの検証を2つの方法のいずれかで処理します。

- CNAME委任（SendGridおよびSparkPost）：サブドメインをESPに戻す`CNAME`を作成します。ESPがインフラ上でSPFポリシーをホストおよび更新し、SPFチェックを自動的にパスします。
- 明示的TXTレコード（Amazon SES）：バウンスサブドメインに明示的な認証文字列を含むハードコードされた`TXT`レコードを直接公開します（例：`v=spf1 include:amazonses.com ~all`）。これにより、AWSにそのゾーンからメールを送信する権限を付与します。

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIMは、メールヘッダーに暗号デジタル署名を追加します。受信サーバーは、送信者の公開キー（DNSで公開）を使用して、メールがドメイン所有者から発信され、転送中に改ざんされていないことを検証します。

Brazeでは、受信ISPがESPによって生成された暗号署名を検証できるように、`TXT`または`CNAME`レコードを通じて公開DKIMキーを公開する必要があります。

### DMARCアライメント {#dmarc}

メールがDMARCをパスするには、ユーザーに表示される`From:`ヘッダーのドメインが、SPF（Return-Path）またはDKIMのいずれかによって検証されたドメインと一致（アライメント）する必要があります。Brazeの設定はSPFとDKIMの両方を通じてアライメントを実現するため、DMARCポリシーは安全に満たされます。

Brazeはデフォルトで基本的なSPFおよびDKIM認証を処理しますが、送信ドメインにDMARCレコードを追加する必要があります。DMARCは、ほぼすべての主要な受信トレイプロバイダーが要求する重要な認証ツールです。メールが正当であることを証明し、ドメインのレピュテーションを構築し、到達率を長期的に健全に保ちます。

これには会社のドメインレジストリへのアクセスが必要なため、あなたまたはネットワーク管理者がルートドメインレベルでこのレコードを追加する必要があります。始めたばかりの場合、`p=none`のような基本的なポリシーで最低限の受信トレイ要件を満たすことができます。DMARCの詳細については、[DMARC.org](https://dmarc.org/)を参照してください。Braze固有のDMARCガイダンスについては、[メール認証]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc)を参照してください。

## ESP固有のDNSアーキテクチャ {#esp-specific-dns-architecture}

ESPアーキテクチャによって、DNS委任の処理方法が異なります。環境をプロビジョニングする際は、特定のESPクラスターにマッピングされた正確なレコードを使用してください。

### SparkPostアーキテクチャ {#sparkpost-architecture}

SparkPostはハイブリッド設定を使用します。明示的な`CNAME`レコードを使用してトラッキングとReturn-PathインフラをSparkPostに戻す一方、DKIM認証には生の`TXT`レコードを使用します。

- SPFとReturn-Pathの設定：SparkPostは、バウンス用に指定されたサブドメイン（例：`mail.example.com`）を要求します。`CNAME`レコードがこのサブドメインをSparkPostのインバウンドバウンスプロセッサーに向けます。これにより、バウンストラフィックが正しくルーティングされ、SparkPostの宛先サーバーがプロトコルを管理するため、SPFが自動的に検証されます。
- DKIMの設定：SparkPostは、特定のセレクターにマッピングされた正確な公開キー文字列を含む`TXT`レコードを必要とします。
- クリックおよび開封トラッキング：SparkPostのトラッキングエンドポイント（またはSSLトラッキングが要求された場合はCDNプロキシ）を指す`CNAME`でトラッキングサブドメインを設定します。

#### SparkPost DNSテーブルの例 {#example-sparkpost-dns-table}

以下の表は、SparkPost設定のDNSレコードの例を示しています。

| レコードタイプ | ホスト/名前 | 値/ターゲット | 目的 |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Return-Path / SPFアライメント |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | 暗号DKIM認証 |
| CNAME | click.mail.example.com | spgo.io（またはCDNエンドポイント） | クリックおよび開封トラッキング |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SparkPost DNSテーブルの例" }

### SendGridアーキテクチャ {#sendgrid-architecture}

SendGridは、ドメイン認証と呼ばれる自動化されたインフラに依存しています。生の`TXT`キーを提供する代わりに、SendGridはSendGrid管理サーバーを直接指す一連の`CNAME`レコードを提供します。

- SPFとReturn-Pathの設定：SendGridは、送信サブドメインを`uXXXXXX.wl.sendgrid.net`にマッピングする特定の`CNAME`（多くの場合`em`プレフィックス付き）を使用します。SendGridはそのエンドポイント上でSPFレコードをホストし、動的に更新します。
- DKIMの設定：SendGridは、DKIM用に2つの別々の`CNAME`レコードを生成します（多くの場合`s1`や`s2`のようなセレクターを使用）。これらはSendGridのキーを指します。
- SendGridが2つのDKIM `CNAME`レコードを提供するのは、DNSを手動で更新することなく暗号キーを自動的にローテーションできるようにするためです。

#### SendGrid DNSテーブルの例 {#example-sendgrid-dns-table}

以下の表は、SendGrid設定のDNSレコードの例を示しています。

| レコードタイプ | ホスト/名前 | 値/ターゲット | 目的 |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.sendgrid.net | Return-Path / 動的SPF |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.sendgrid.net | プライマリDKIMキー（ローテーション） |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.sendgrid.net | セカンダリDKIMキー（ローテーション） |
| CNAME | email.mail.example.com | sendgrid.net（またはCDNエンドポイント） | クリックおよび開封トラッキング |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SendGrid DNSテーブルの例" }

### Amazon SESアーキテクチャ {#amazon-ses-architecture}

Amazon SESは、`CNAME`レコードによるEasy DKIMと、カスタマイズされたバウンストラッキング用の明示的な`MX`および`TXT`ルーティングを使用します。

- DKIMの設定：Amazon SESはEasy DKIMを使用し、3つの`CNAME`レコードを提供します。これらは公開キーを含むAWS管理サブドメインを指します。SESはセキュリティコンプライアンスを維持するために、これらのキーを透過的に自動ローテーションします。
- SPFとカスタムMAIL FROMの設定：SendGridとSparkPostは`CNAME`を通じてバウンスドメインルーティングを管理します。Amazon SESでは、指定されたMAIL FROMサブドメインに直接配置される明示的な`MX`レコードと`TXT`レコードが必要です。`MX`レコードはバウンス通知がAmazonのサーバーに返されることを保証し、`TXT`レコードには認証済みのハードコードされたSPF文字列が含まれます。

詳細については、[Amazon SESの設定]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses)を参照してください。

#### Amazon SES DNSテーブルの例 {#example-amazon-ses-dns-table}

以下の表は、Amazon SES設定のDNSレコードの例を示しています。

| レコードタイプ | ホスト/名前 | 値/ターゲット | 目的 |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Easy DKIMキー1（ローテーション） |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Easy DKIMキー2（ローテーション） |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Easy DKIMキー3（ローテーション） |
| MX | bounce.mail.example.com | 10 feedback-smtp.us-east-1.amazonses.com | バウンス処理をAWSにルーティング |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | 明示的SPF認証 |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me（またはCDN） | クリックおよび開封トラッキング |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Amazon SES DNSテーブルの例" }

## 高度なDNSの考慮事項 {#advanced-dns-considerations}

### TXT DKIMレコードの文字列分割 {#txt-dkim-record-string-splitting}

SparkPostまたは手動DKIM設定をデプロイする際、長い暗号キー（2048ビットDKIMキー）に遭遇することがあります。

コアDNS仕様（RFC 1035）では、`TXT`レコード内の単一の文字列を最大255文字に制限しています。2048ビットの公開キーは通常400文字を超えるため、ドメインレジストリが単一の文字列を拒否するか切り捨て、署名が無効になります。

文字列分割はこの問題を解決します。文字列を255文字未満のチャンクに分割します。各チャンクをストレート引用符で囲み、同じ`TXT`レコード内でスペースで区切ります。

{% alert note %}
CloudflareやAWS Route 53などのDNSプロバイダーを使用する場合、これらのインターフェイスは長い文字列を貼り付けると自動的に分割を処理します。レガシーシステム（GoDaddyやNetwork Solutionsなど）では、ダブルクォートテクニックを使用して手動で分割をフォーマットする必要があります。
{% endalert %}

### 専用サブドメインの使用 {#dedicated-subdomains}

オンボーディング時によくあるエラーは、トップレベルの組織ドメイン（`example.com`など）をBrazeの送信ドメインとして直接使用しようとすることです。Brazeでは、専用サブドメイン（例：`mail.example.com`や`engage.example.com`）の使用が必要です。

親ドメインを使用すると、以下の方法で企業インフラが破損する可能性があります。

#### MXレコードの競合 {#mx-record-conflicts}

ドメインは、プライマリルーティング`MX`レコードのセットを1つしかサポートできません。親ドメイン（`example.com`）をBrazeのESPインフラにマッピングすると、バウンスに必要なカスタム`MX`レコードが企業メールレコードを上書きします。これにより、Google WorkspaceやMicrosoft 365などの企業内部メッセージングプラットフォームが中断される可能性があります。

#### SPFインクルードの肥大化と10ルックアップ制限 {#spf-include-bloat-and-the-10-lookup-limit}

SPF仕様（RFC 7208）では、SPFレコードを検証する際に受信メールサーバーが実行できるDNSルックアップを最大10回に制限しています。

- 親ドメインがBrazeのESPメカニズム（`include:sparkpostmail.com`や`include:amazonses.com`）を追加すると、その制限に大きく影響します。
- 制限を超えると、永続的なSPF PermErrorがトリガーされ、すべての企業メールが認証に失敗します。

#### IPおよびドメインレピュテーションの分離 {#ip-and-domain-reputation-isolation}

マーケティングキャンペーン、トランザクションレシート、および内部従業員メールが同一のルートドメインスペースを共有している場合、マーケティングスパム苦情の急増が親ドメインのレピュテーションを損なう可能性があります。これにより、重要な企業コミュニケーションがスパムフォルダーにルーティングされるリスクがあります。専用サブドメインを使用することで、マーケティングアウトリーチのレピュテーションを分離できます。

## 実装ワークフロー {#implementation-workflow}

スムーズな引き継ぎと実装を確保するために、以下の手順に従ってください。

1. 構造化されたレコードをIT部門またはネットワーク管理者に提供し、ホスティングプラットフォーム（Cloudflare、Route 53など）に追加してもらいます。
2. 初期テスト用に低いTime-To-Live（TTL）値（例：300秒または5分）を設定します。これにより、入力時にタイプミスがあった場合の迅速な復旧が可能になります。
3. DNSルックアップ（例：`dig CNAME mail.example.com`）を実行するか、検証ツールを使用して、ウォーミングフェーズに進む前にレコードが正しく解決されることを確認します。

## DNSプロバイダーのドキュメント {#dns-provider-documentation}

すべてのDNSプロバイダーには固有のインターフェイスがあります。これらの仕様をネットワーク管理者と共有するか、特定のプロバイダーのドキュメントを参照して、ゾーンファイルにエントリを正しくマッピングしてください。

以下の表は、一般的に使用されるDNSプロバイダーの公式ドキュメントを一覧にしています。

| DNSプロバイダー | リソース |
| --- | --- |
| Cloudflare | [DNSレコードの管理](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [リソースレコードセットの作成](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [DNSレコードの管理](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [ドメイン名のDNSレコードの設定](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Azureポータルを使用したDNSレコードの管理](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="DNSプロバイダーのドキュメント" }

その他のドメインプロバイダーリソースについては、[IPとドメインの設定]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-3-add-dns-records)を参照してください。