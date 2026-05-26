---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "このリファレンス記事では、BrazeとBetter Emailのパートナーシップについて説明します。Better Emailは、メールデザインシステムを中心に構築されたコラボレーティブなメール作成プラットフォームで、本番環境対応のテンプレートをBrazeにエクスポートできます。"
page_type: partner
search_tag: Partner
---

# Better Email

> [Better Email](https://www.betteremail.dev)は、メールデザインシステムを中心に構築されたコラボレーティブなメール作成プラットフォームです。チームはブロックとスタイルの共有システムからメールをデザイン、管理、エクスポートでき、開発者やエージェンシーに頼ることなく、大規模なブランドの一貫性を確保できます。

_この統合はBetter Emailによって管理されています。_

## 統合について {#about-the-integration}

BrazeとBetter Emailの統合により、Better Emailのコラボレーティブエディターでメールテンプレートを作成・管理し、すぐに使えるメールテンプレートとしてBrazeに直接エクスポートできます。

メールを再エクスポートすると、重複を作成するのではなく既存のBrazeテンプレートが更新されるため、テンプレートライブラリーが整理された状態を保てます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Better Emailアカウント | 統合を作成するための管理者アクセス権を持つBetter Emailアカウント |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。ダッシュボードURLではなくRESTホストを使用してください（例：`rest.fra-01.braze.eu`）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

Better Emailは、デザインシステムを通じてメールを管理し、手動のHTML作業なしでBrazeにエクスポートしたいマーケティングチーム向けに構築されています。以下のようなチームに最適です：

- 大規模なメールテンプレートライブラリーを維持し、すべてのテンプレートで一貫性を確保する必要がある
- 共有メールデザインシステムを通じてブランドガイドラインを適用したい
- デザイナー、マーケター、開発者がチーム横断でメール制作にコラボレーションする
- メールキャンペーンの実行にBrazeを使用し、デザインとデプロイメント間の引き継ぎのボトルネックを解消したい

## Better EmailとBrazeの統合 {#integrate-better-email-with-braze}

### ステップ 1：Brazeの値を確認する {#step-1-find-your-braze-values}

Brazeダッシュボードで、以下の情報を収集します：

- **インスタンスURL** — ダッシュボードURLではなくRESTホストを使用してください（例：`rest.fra-01.braze.eu`）。
- **APIキー** — **設定** > **APIキー**で作成した、完全な**テンプレート**権限を持つREST APIキー。

### ステップ 2：Better Emailで統合を設定する {#step-2-set-up-the-integration-in-better-email}

1. **Integrations**に移動します。
2. 新しい統合を作成します。
3. 統合の名前を入力します（例：`Braze`）。
4. タイプとして**Braze**を選択します。
5. 必要に応じて、**Access**で統合を特定のユーザーまたはグループに制限します。
6. **Save**を選択します。
7. **Instance URL**と**API Key**を入力します。
8. 統合を有効にします。
9. 再度**Save**を選択します。

### ステップ 3：Brazeにエクスポートする {#step-3-export-to-braze}

統合がアクティブになったら、Better Emailで任意のメールを開き、**Export** > **Braze**を選択します。

Better Emailは対応するBrazeメールテンプレートを作成または更新します。最初のエクスポート後、Better EmailはBrazeテンプレートIDを保存します。同じメールを再エクスポートすると、重複を作成するのではなくそのテンプレートが更新されます。

### オプション：Brazeから受信者フィールドを同期する {#optional-sync-recipient-fields-from-braze}

Better Emailは、マージタグやセグメンテーションフィールドとして使用するためにBrazeのカスタム属性を同期できます。

1. Better EmailでBraze統合を開きます。
2. **Sync recipient fields**を有効にします。
3. **Save**を選択します。
4. **Recipient Fields**に移動します。
5. 統合名から**Sync from**を実行します。

Better Emailは利用可能なBrazeカスタム属性を読み取り、受信者フィールドにマッピングします。

## トラブルシューティング {#troubleshooting}

エクスポートまたは同期が失敗した場合は、以下を確認してください：

- **Instance URL**がダッシュボードURLではなくREST URLであること
- APIキーがまだアクティブで、必要な**テンプレート**権限を持っていること
- Better Emailで統合が有効になっていること
- 正しいユーザーまたはグループが統合にアクセスできること

さらにサポートが必要な場合は、[support@better.email](mailto:support@better.email)にお問い合わせください。

## 統合の使用 {#use-the-integration}

エクスポートしたBetter Emailテンプレートは、Brazeの**テンプレートとメディア** > **メールテンプレート**で確認できます。任意のBraze CampaignまたはCanvasで使用してください。