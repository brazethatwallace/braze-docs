---
nav_title: 到達性センター
article_title: 到達性センター
alias: "/deliverability_center/"
page_order: 4
description: "このリファレンス記事では、到達性センターのセットアップ方法について説明します。到達性センターは、マーケターがメール送信ドメインとIPレピュテーションを確認し、メールの到達性を把握できる機能です。"
channel:
  - email

---

# 到達性センター {#deliverability-center}

> 到達性センターは、[Gmail Postmaster Tools](https://www.gmail.com/postmaster/)の使用をサポートし、送信済みメールのデータを追跡して送信ドメインに関するデータを収集することで、メールパフォーマンスに関するより深いインサイトを提供します。

メールの到達性は、キャンペーン成功の核心です。Brazeダッシュボードの到達性センターを使用すると、**IPレピュテーション**または**配信エラー**別にドメインを表示し、メールの到達性に関する潜在的な問題を発見してトラブルシューティングできます。

到達性センターにアクセスするには、ワークスペースに対する以下のドロップダウンに記載されている[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。

{% details 到達性センターのユーザー権限 %}

- キャンペーンの表示
- キャンペーンの編集
- キャンペーンのアーカイブ
- キャンバスの表示
- キャンバスの編集
- キャンバスのアーカイブ
- フリークエンシーキャップルールの表示
- フリークエンシーキャップルールの編集
- メッセージ優先度の表示
- メッセージ優先度の編集
- Content Blocksの表示
- フィーチャーフラグの表示
- フィーチャーフラグの編集
- フィーチャーフラグのアーカイブ
- セグメントの表示
- セグメントの編集
- IAMテンプレートの表示
- IAMテンプレートの編集
- IAMテンプレートのアーカイブ
- メールテンプレートの表示
- メールテンプレートの編集
- メールテンプレートのアーカイブ
- Webhookテンプレートの表示
- Webhookテンプレートの編集
- Webhookテンプレートのアーカイブ
- メールリンクテンプレートの表示
- メールリンクテンプレートの編集
- メディアライブラリアセットの表示
- メディアライブラリアセットの編集
- メディアライブラリアセットの削除
- ロケーションの表示
- ロケーションの編集
- ロケーションのアーカイブ
- プロモーションコードの表示
- プロモーションコードの編集
- プロモーションコードのエクスポート
- ユーザー設定センターの表示
- ユーザー設定センターの編集
- レポートの表示
- レポートの編集
- 使用状況データの表示

{% enddetails %}

## Google Postmasterアカウントのセットアップ {#set-up-your-google-postmaster-account}

到達性センターに接続する前に、Google Postmaster Toolsアカウントをセットアップする必要があります。仕事用または個人用のGmailアカウントを使用してGoogle Postmasterをセットアップできます。

1. [Google Postmaster Toolsダッシュボード](https://postmaster.google.com/managedomains?pli=1)にアクセスします。
2. ページ下部の<i class="fas fa-plus-circle"></i> **Add domain**を選択します。
3. ルート（親）ドメインを入力してメールを認証します。TXTレコードが、Brazeで使用しているサブドメインでは**なく**、このルート（親）ドメインに紐付けられていることを確認してください。ルート（親）ドメインを検証すると、追加のTXTレコードを作成せずに、後からPostmaster Toolsにサブドメインを追加できます。例えば、`braze.com`を検証すると、後から`demo.braze.com`をPostmaster Toolsに別のサブドメインとして追加し、サブドメインレベルの指標を確認できます。
4. GoogleがTXTレコードを生成します。このレコードはドメインのDNSに直接追加できます。通常、DNSを管理している担当者がこの作業を行います。特定のDNSの更新方法に関する情報とガイダンスについては、[ドメインの確認（ホスト固有の手順）](https://support.google.com/a/topic/1409901)を参照してください。
5. **Next**を選択します。<br>![メールを認証するためのドメイン「demo.braze.com」の例。]({% image_buster /assets/img_archive/domain_authentication.png %})
6. TXTレコードをDNSに追加した後、Google Postmaster Toolsダッシュボードに戻り、**Verify**を選択します。このステップでドメインの所有権が確認され、PostmasterアカウントでGmailの到達性指標にアクセスできるようになります。<br>![ドメイン「demo.braze.com」の所有権を確認するプロンプト。]({% image_buster /assets/img_archive/domain_verification.png %})
7. ルート（親）ドメインを検証した後、送信サブドメインをGoogle Postmasterに追加します。

{% alert note %}
サブドメインがGoogle Postmasterの到達性センターに表示されない場合、ルート（親）ドメインのみをGoogle Postmasterに追加したことが原因である可能性があります。Google Postmasterでルートドメインが検証された後、サブドメインを追加すると自動的に検証されます。このプロセスにより、Googleがサブドメインレベルの指標を報告できるようになり、その情報をBrazeの到達性センターに取り込むことができます。
{% endalert %}

## Google Postmasterの統合 {#integrating-google-postmaster}

{% alert important %}
**Google Postmaster Tools v2への移行**<br>
Googleは旧Postmaster Tools（v1）を廃止し、モダンなユーザーインターフェイスと新しいダッシュボード（Gmailの送信者ガイドラインへの準拠を監視するためのコンプライアンスダッシュボードを含む）を備えた次世代バージョン（v2）をリリースしました。すべてのユーザーは2026年10月31日までにv2に移行する必要があります。<br><br>
Google Postmaster Toolの接続を再認証するには、**パートナー連携** > **テクノロジーパートナー**に移動し、**Google Postmaster**を開いて**Change Account**を選択し、新しいv2権限で再認証します。完了すると、v2にアップグレードされ、新しいダッシュボードとデータにアクセスできるようになります。<br><br>
詳細については、[新しいPostmaster Toolsに関するGoogleの発表](https://support.google.com/mail/answer/16594218?hl=en)を参照してください。
{% endalert %}

到達性センターをセットアップする前に、ドメインが[Gmail Postmaster Toolsに追加](https://support.google.com/mail/answer/9981691?hl=en)されていることを確認してください。

以下の手順に従ってGoogle Postmasterと統合し、到達性センターをセットアップします。

1. **Analytics** > **メールのパフォーマンス**に移動します。
2. **到達性センター**タブを選択します。<br>![Google Postmasterが未接続の到達性センター。]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. **Connect with Google Postmaster**を選択します。
4. Googleアカウントを選択し、**Allow**を選択して、Postmaster Toolsに登録されたドメインのメールトラフィック指標をBrazeが表示できるようにします。

検証済みのドメインが到達性センターに表示されます。

![Google Postmasterの2つの検証済みドメイン。レピュテーションは中と低。]({% image_buster /assets/img_archive/deliverability_center2.png %})

Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー** > **Google Postmaster**に移動してGoogle Postmasterにアクセスすることもできます。統合後、Brazeは過去30日間のレピュテーションとエラーデータを取得します。データはすぐに利用できない場合があり、反映されるまで数分かかることがあります。

### 無効または期限切れの認証 {#invalid-or-expired-authorization}

Google Postmaster Toolsの認証情報が無効であるというアラートを受け取った場合でも、Brazeからのメール送信には**影響しません**。BrazeとGoogle Postmaster間の接続のみが切断され、再接続するまでGmailのレピュテーションとエラーデータが到達性センターに同期されなくなります。

統合を復元するには、**パートナー連携** > **テクノロジーパートナー**に移動し、**Google Postmaster**を開いて**Disconnect**を選択し、接続フローを再度実行します（[Google Postmasterの統合](#integrating-google-postmaster)と同じ手順です）。

### 指標と定義 {#metrics-and-definitions}

以下の指標と定義はGoogle Postmaster Toolsに適用されます。

#### IPレピュテーション {#ip-reputation}

IPレピュテーションの評価を理解するには、以下の表を参照してください。

| レピュテーション評価 | 定義 |
| ----- | ---------- |
| 高 | スパム苦情（ユーザーが「スパム」ボタンをクリックするなど）の発生率が低い良好な実績があります。 |
| 中/普通 | ポジティブなエンゲージメントを生成することで知られていますが、時折スパム苦情を受けることがあります。このドメインからのメールのほとんどは受信トレイに配信されますが、スパム苦情が増加した場合は例外です。 |
| 低 | 定期的にスパム苦情率が高いことで知られています。この送信者からのメールはスパムフォルダーにフィルタリングされる可能性が高いです。 |
| 悪い | スパム苦情率が高い履歴があります。このドメインからのメールは、接続時にほぼ常に拒否されるか、スパムフォルダーにフィルタリングされます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="IPレピュテーション" }

#### ドメインレピュテーション {#domain-reputation}

以下の表を使用して、ドメインレピュテーションの評価を監視・把握し、スパムフォルダーにフィルタリングされることを防ぎましょう。

| レピュテーション評価 | 定義 |
| ----- | ---------- |
| 高 | スパム苦情率が非常に低い良好な実績があります。Gmailの送信者ガイドラインに準拠しています。メールがスパムフォルダーにフィルタリングされることはほとんどありません。スパム率が非常に低い良好な実績があります。[Gmailの送信者ガイドライン](https://developers.google.com/gmail/markup/registering-with-google)に準拠しています。 |
| 中/普通 | ポジティブなエンゲージメントを生成することで知られていますが、時折少量のスパム苦情を受けることがあります。このドメインからのメールのほとんどは受信トレイに到達します（スパムレベルが著しく増加した場合を除く）。 |
| 低 | 定期的にスパム苦情を受けることで知られています。この送信者からのメールはスパムフォルダーにフィルタリングされる可能性が高いです。 |
| 悪い | スパム苦情率が高い履歴があります。このドメインからのメールは、接続時にほぼ常に拒否されるか、スパムフォルダーにフィルタリングされます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ドメインレピュテーション" }

#### 認証 {#authentication}

認証ダッシュボードを使用して、Sender Policy Framework（SPF）、DomainKeys Identified Mail（DKIM）、Domain-based Message Authentication, Reporting and Conformance（DMARC）に合格したメールの割合を確認できます。

| グラフの種類 | 定義 |
| ----- | ---------- |
| SPF | SPFを試行したドメインからのすべてのメールに対して、SPFに合格したメールの割合を表示します。なりすましメールは除外されます。 |
| DKIM | DKIMを試行したドメインからのすべてのメールに対して、DKIMに合格したメールの割合を表示します。 |
| DMARC | SPFまたはDKIMのいずれかに合格したドメインから受信したすべてのメールに対して、DMARCアライメントに合格したメールの割合を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="認証" }

#### 暗号化 {#encryption}

この表を参照して、受信および送信トラフィックのうち暗号化されている割合を把握してください。

| 用語 | 定義 |
| ----- | ---------- |
| TLS受信 | そのドメインから受信したすべてのメールに対して、TLSに合格した受信メール（Gmail宛）の割合を表示します。 |
| TLS送信 | そのドメインに送信されたすべてのメールに対して、TLS経由で受け入れられた送信メール（Gmailから）の割合を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="暗号化" }

到達性の改善に関するその他のアイデアについては、[到達性の落とし穴とスパムトラップ]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)をお読みください。メールキャンペーンを送信する前に確認すべき事項については、[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices)も参照してください。

## Microsoft Smart Network Data Services（SNDS）のセットアップ {#set-up-microsoft-smart-network-data-services-snds}

Microsoftがメインのメールボックスプロバイダーである場合、到達性センターでMicrosoft SNDSデータを表示できます。これには、Amazon SES、SendGrid、またはSparkPostを使用するワークスペースの専用送信IPが含まれます。このデータを使用して、IPの健全性を監視し、Microsoftの受信トレイプロバイダーが送信をどのように評価しているかを把握できます。

Microsoft SNDSは、Outlook、Hotmail、LiveなどのMicrosoft受信トレイプロバイダーから報告された、スパム苦情、スパムトラップヒット、送信量に関するIPレベルのデータを提供します。

{% alert important %}
到達性センターにデータが表示されない場合は、IPアドレスのリストを添えて[サポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。
{% endalert %}

### Amazon SES

Amazon SESを通じてメールを送信するワークスペースの場合、到達性センターには専用送信IPのMicrosoft SNDS指標が表示されます。Brazeは、この機能がワークスペースで有効になった際に、最大90日間のSNDS履歴データをバックフィルします。

{% alert note %}
Amazon SESは**トラップメッセージ期間の開始**または**トラップメッセージ期間の終了**の指標を提供しません。SES送信IPの場合、これらの列はMicrosoft SNDSテーブルで非表示になります。それ以外のSNDS指標（スパムトラップヒットを含む）は引き続き表示できます。
{% endalert %}

![Microsoft SNDSの結果の例。サンプルIP、受信者数、RCPTコマンド、DATAコマンド、フィルター結果、苦情率、トラップメッセージ期間の開始と終了、スパムトラップヒット数が含まれています。]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### 指標と定義

以下の指標はMicrosoft SNDSに適用されます。

#### 受信者数 {#recipients}

この指標は、IPから送信されたメッセージの受信者数を示します。

#### DATAコマンド {#data-commands}

この指標は、IPから送信されたDATAコマンドの数を追跡します。DATAコマンドは、メール送信に使用されるSMTPプロトコルの一部です。

#### フィルター結果 {#filter-results}

フィルター結果を理解するには、以下の表を参照してください。

| 結果 | 定義 |
| ----- | ---------- |
| 緑 | 指定された期間の最大10%がMicrosoftのスパムフィルターによってスパムと判定されました。 |
| 黄 | 指定された期間の10%から90%がMicrosoftのスパムフィルターによってスパムと判定されました。 |
| 赤 | 指定された期間の90%以上がMicrosoftのスパムフィルターによってスパムと判定されました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="フィルター結果" }

#### 苦情率 {#complaint-rate}

これは、アクティビティ期間中にIPから受信したメッセージに対して、HotmailまたはWindows Liveユーザーが苦情を報告した割合です。ユーザーはWebユーザーインターフェイスを通じて、ほぼすべてのメッセージを迷惑メールとして報告できます。

苦情率を計算するには、苦情数をメッセージ受信者数で割ります。

| 結果 | 定義 |
| ----- | ---------- |
| 0.3%未満 | 理想的な苦情率です。 |
| 0.3%超 | サインアッププロセスを見直し、購読解除リンクが機能していることを確認してください。また、メールをオーディエンスに合わせてよりパーソナライズできないか検討してください。 |
| 100%超 | SNDSは苦情が報告された日に苦情を表示し、苦情対象のメールが配信された日に遡って表示するわけではないことに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="苦情率" }

#### スパムトラップヒット {#spam-trap-hits}

スパムトラップヒットは、「トラップアカウント」に送信されたメッセージの数です。トラップアカウントとは、Outlook.comが管理する、メールを一切要求しないアカウントです。これらのトラップアカウントに送信されたメッセージはスパムと見なされる可能性が高いため、この指標を監視して低く保つことが重要です。スパムトラップヒットが低いということは、メッセージがこれらのアカウントに送信されておらず、実際のアカウントに送信されていることを意味します。

#### トラップメッセージ期間の開始と終了 {#trap-message-period-start-and-end}

これらの列は、アクティビティ期間中にIPからトラップアカウントに送信された最初と最後のメッセージが受信された時刻を示します。Amazon SESはこれらの指標を提供しないため、Microsoft SNDSテーブルでSES送信IPのみを表示している場合、これらの列は非表示になります。

{% alert tip %}
Brazeで検証済みのドメインに関連するレコードを探している場合、到達性センターにはGoogle PostmasterまたはMicrosoft SNDSからのデータが表示されます。つまり、いずれかのプラットフォームにBrazeと共有するデータがない可能性があります。あるいは、一貫したメール配信を維持することで、より高いレピュテーションにつながる可能性があります。
{% endalert %}