---
nav_title: 到達性センター
article_title: 到達性センター
alias: "/deliverability_center/"
page_order: 4
description: "このリファレンス記事では、到達性センターのセットアップ方法について説明します。到達性センターは、マーケターがメール送信ドメインとIPレピュテーションを確認し、メールの到達性を把握できる機能です。"
channel:
  - email

---

# 到達性センター

> 到達性センターは、[Gmail Postmaster Tools](https://www.gmail.com/postmaster/) の使用をサポートし、送信済みメールのデータを追跡して送信ドメインに関するデータを収集することで、メールパフォーマンスに関するより深いインサイトを提供します。

メールの到達性は、キャンペーン成功の核心です。Braze ダッシュボードの到達性センターを使用すると、**IPレピュテーション**または**配信エラー**別にドメインを表示し、メールの到達性に関する潜在的な問題を発見してトラブルシューティングできます。

到達性センターにアクセスするには、「キャンペーン、キャンバス、カード、セグメント、メディアライブラリへのアクセス」および「使用状況データの表示」の[レガシーユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=legacy%20permissions)、またはワークスペースに対する以下のドロップダウンに記載されている[詳細権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions)が必要です。

{% details 到達性センターのユーザー権限 %}

{% multi_lang_include deprecations/user_permissions.md %}

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
- コンテンツブロックの表示
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
- Webhook テンプレートの表示
- Webhook テンプレートの編集
- Webhook テンプレートのアーカイブ
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

## Google Postmaster アカウントのセットアップ

到達性センターに接続する前に、Google Postmaster Tools アカウントをセットアップする必要があります。仕事用または個人用の Gmail アカウントを使用して Google Postmaster をセットアップできます。

1. [Google Postmaster Tools ダッシュボード](https://postmaster.google.com/managedomains?pli=1)にアクセスします。
2. 右下の <i class="fas fa-plus-circle"></i> プラスアイコンを選択します。
3. ルート（親）ドメインを入力してメールを認証します。TXT レコードが、Braze で使用しているサブドメインでは**なく**、このルート（親）ドメインに紐付けられていることを確認してください。ルート（親）ドメインを検証すると、追加の TXT レコードを作成せずに、後から Postmaster Tools にサブドメインを追加できます。例えば、`braze.com` を検証すると、後から `demo.braze.com` を Postmaster Tools に別のサブドメインとして追加し、サブドメインレベルの指標を確認できます。
4. Google が TXT レコードを生成します。このレコードはドメインの DNS に直接追加できます。通常、DNS を管理している担当者がこの作業を行います。特定の DNS の更新方法に関する情報とガイダンスについては、[Verify your domain (host-specific steps)](https://support.google.com/a/topic/1409901) を参照してください。
5. **Next** を選択します。<br>![メールを認証するためのドメイン「demo.braze.com」の例。]({% image_buster /assets/img_archive/domain_authentication.png %})
6. TXT レコードを DNS に追加した後、Google Postmaster Tools ダッシュボードに戻り、**Verify** を選択します。このステップでドメインの所有権が確認され、Postmaster アカウントで Gmail の到達性指標にアクセスできるようになります。<br>![ドメイン「demo.braze.com」の所有権を確認するプロンプト。]({% image_buster /assets/img_archive/domain_verification.png %})
7. ルート（親）ドメインを検証した後、送信サブドメインを Google Postmaster に追加します。

{% alert note %}
サブドメインが Google Postmaster の到達性センターに表示されない場合、ルート（親）ドメインのみを Google Postmaster に追加したことが原因である可能性があります。Google Postmaster でルートドメインが検証された後、サブドメインを追加すると自動的に検証されます。このプロセスにより、Google がサブドメインレベルの指標を報告できるようになり、その情報を Braze の到達性センターに取り込むことができます。
{% endalert %}

## Google Postmaster の統合 {#integrating-google-postmaster}

到達性センターをセットアップする前に、ドメインが [Gmail Postmaster Tools に追加](https://support.google.com/mail/answer/9981691?hl=en)されていることを確認してください。

以下の手順に従って Google Postmaster と統合し、到達性センターをセットアップします。

1. **分析** > **メールのパフォーマンス**に移動します。
2. **到達性センター**タブを選択します。<br>![Google Postmaster が未接続の到達性センター。]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. **Connect with Google Postmaster** を選択します。
4. Google アカウントを選択し、**Allow** を選択して、Postmaster Tools に登録されたドメインのメールトラフィック指標を Braze が表示できるようにします。

検証済みのドメインが到達性センターに表示されます。

![Google Postmaster の2つの検証済みドメイン。レピュテーションは中と低。]({% image_buster /assets/img_archive/deliverability_center2.png %})

Braze ダッシュボードで**パートナー連携** > **テクノロジーパートナー** > **Google Postmaster** に移動して Google Postmaster にアクセスすることもできます。統合後、Braze は過去30日間のレピュテーションとエラーデータを取得します。データはすぐに利用できない場合があり、反映されるまで数分かかることがあります。

### 無効または期限切れの認証

Google Postmaster Tools の認証情報が無効であるというアラートを受け取った場合でも、Braze からのメール送信には**影響しません**。Braze と Google Postmaster 間の接続のみが切断され、再接続するまで Gmail のレピュテーションとエラーデータが到達性センターに同期されなくなります。

統合を復元するには、**パートナー連携** > **テクノロジーパートナー**に移動し、**Google Postmaster** を開いて **Disconnect** を選択し、接続フローを再度実行します（[Google Postmaster の統合](#integrating-google-postmaster)と同じ手順です）。

### 指標と定義

以下の指標と定義は Google Postmaster Tools に適用されます。

#### IPレピュテーション

IPレピュテーションの評価を理解するには、以下の表を参照してください。

| レピュテーション評価 | 定義 |
| ----- | ---------- |
| 高 | スパム苦情（ユーザーが「スパム」ボタンをクリックするなど）の発生率が低い良好な実績があります。 |
| 中/普通 | ポジティブなエンゲージメントを生成することで知られていますが、時折スパム苦情を受けることがあります。このドメインからのメールのほとんどは受信トレイに配信されますが、スパム苦情が増加した場合は例外です。 |
| 低 | 定期的にスパム苦情率が高いことで知られています。この送信者からのメールはスパムフォルダーにフィルタリングされる可能性が高いです。 |
| 悪い | スパム苦情率が高い履歴があります。このドメインからのメールは、接続時にほぼ常に拒否されるか、スパムフォルダーにフィルタリングされます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### ドメインレピュテーション

以下の表を使用して、ドメインレピュテーションの評価を監視・把握し、スパムフォルダーにフィルタリングされることを防ぎましょう。

| レピュテーション評価 | 定義 |
| ----- | ---------- |
| 高 | スパム苦情率が非常に低い良好な実績があります。Gmail の送信者ガイドラインに準拠しています。メールがスパムフォルダーにフィルタリングされることはほとんどありません。スパム率が非常に低い良好な実績があります。[Gmail の送信者ガイドライン](https://developers.google.com/gmail/markup/registering-with-google)に準拠しています。 |
| 中/普通 | ポジティブなエンゲージメントを生成することで知られていますが、時折少量のスパム苦情を受けることがあります。このドメインからのメールのほとんどは受信トレイに到達します（スパムレベルが著しく増加した場合を除く）。 |
| 低 | 定期的にスパム苦情を受けることで知られています。この送信者からのメールはスパムフォルダーにフィルタリングされる可能性が高いです。 |
| 悪い | スパム苦情率が高い履歴があります。このドメインからのメールは、接続時にほぼ常に拒否されるか、スパムフォルダーにフィルタリングされます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 認証

認証ダッシュボードを使用して、Sender Policy Framework（SPF）、DomainKeys Identified Mail（DKIM）、Domain-based Message Authentication, Reporting and Conformance（DMARC）に合格したメールの割合を確認できます。

| グラフの種類 | 定義 |
| ----- | ---------- |
| SPF | SPF を試行したドメインからのすべてのメールに対して、SPF に合格したメールの割合を表示します。なりすましメールは除外されます。 |
| DKIM | DKIM を試行したドメインからのすべてのメールに対して、DKIM に合格したメールの割合を表示します。 |
| DMARC | SPF または DKIM のいずれかに合格したドメインから受信したすべてのメールに対して、DMARC アライメントに合格したメールの割合を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 暗号化

この表を参照して、受信および送信トラフィックのうち暗号化されている割合を把握してください。

| 用語 | 定義 |
| ----- | ---------- |
| TLS 受信 | そのドメインから受信したすべてのメールに対して、TLS に合格した受信メール（Gmail 宛）の割合を表示します。 |
| TLS 送信 | そのドメインに送信されたすべてのメールに対して、TLS 経由で受け入れられた送信メール（Gmail から）の割合を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

到達性の改善に関するその他のアイデアについては、[到達性の落とし穴とスパムトラップ]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#deliverability-pitfalls-and-spam-traps)をお読みください。メールキャンペーンを送信する前に確認すべき事項については、[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices/)も参照してください。

## Microsoft Smart Network Data Services（SNDS）のセットアップ

Microsoft がメインのメールボックスプロバイダーである場合、この統合を使用して Microsoft のレピュテーションデータにアクセスし、表示できます。これにより、IP の健全性を監視し、メールがどのように受信されているかを判断するのに役立ちます。

{% alert important %}
到達性センターにデータが表示されない場合は、IP アドレスのリストを添えて[サポート]({{site.baseurl}}/user_guide/administer/personal/braze_support/)にお問い合わせください。
{% endalert %}

![Microsoft SNDS の結果の例。サンプル IP、受信者数、RCPT コマンド、DATA コマンド、フィルター結果、苦情率、トラップメッセージ期間の開始と終了、スパムトラップヒット数が含まれています。]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### 指標と定義

以下の指標は Microsoft SNDS に適用されます。

#### 受信者数

この指標は、IP から送信されたメッセージの受信者数を示します。

#### DATA コマンド

この指標は、IP から送信された DATA コマンドの数を追跡します。DATA コマンドは、メール送信に使用される SMTP プロトコルの一部です。

#### フィルター結果

フィルター結果を理解するには、以下の表を参照してください。

| 結果 | 定義 |
| ----- | ---------- |
| 緑 | 指定された期間の最大10%が Microsoft のスパムフィルターによってスパムと判定されました。 |
| 黄 | 指定された期間の10%から90%が Microsoft のスパムフィルターによってスパムと判定されました。 |
| 赤 | 指定された期間の90%以上が Microsoft のスパムフィルターによってスパムと判定されました。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 苦情率

これは、アクティビティ期間中に IP から受信したメッセージに対して、Hotmail または Windows Live ユーザーが苦情を報告した割合です。ユーザーは Web ユーザーインターフェイスを通じて、ほぼすべてのメッセージを迷惑メールとして報告できます。

苦情率を計算するには、苦情数をメッセージ受信者数で割ります。

| 結果 | 定義 |
| ----- | ---------- |
| 0.3%未満 | 理想的な苦情率です。 |
| 0.3%超 | サインアッププロセスを見直し、配信停止リンクが機能していることを確認してください。また、メールをオーディエンスに合わせてよりパーソナライズできないか検討してください。 |
| 100%超 | SNDS は苦情が報告された日に苦情を表示し、苦情対象のメールが配信された日に遡って表示するわけではないことに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### スパムトラップヒット

スパムトラップヒットは、「トラップアカウント」に送信されたメッセージの数です。トラップアカウントとは、Outlook.com が管理する、メールを一切要求しないアカウントです。これらのトラップアカウントに送信されたメッセージはスパムと見なされる可能性が高いため、この指標を監視して低く保つことが重要です。スパムトラップヒットが低いということは、メッセージがこれらのアカウントに送信されておらず、実際のアカウントに送信されていることを意味します。

{% alert tip %}
Braze で検証済みのドメインに関連するレコードを探している場合、到達性センターには Google Postmaster または Microsoft SNDS からのデータが表示されます。つまり、いずれかのプラットフォームに Braze と共有するデータがない可能性があります。あるいは、一貫したメール配信を維持することで、より高いレピュテーションにつながる可能性があります。
{% endalert %}