---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "このリファレンス記事では、BrazeとDyspatchの連携について概説します。Dyspatchはドラッグアンドドロップのメールビルダーで、コードを記述することなく、美しくレスポンシブで魅力的なメールを作成できます。"
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io)は、コードを書く必要なく、美しくレスポンシブで魅力的なメールを作成できる直感的なドラッグアンドドロップのメールビルダーを提供します。チームと協力してDyspatch内でメールを作成・承認し、わずか数ステップでBrazeにエクスポートできます。

_この統合はDyspatchによって管理されています。_

## 統合について {#about-the-integration}

DyspatchとBrazeの統合により、Dyspatchのメールテンプレートを直接Brazeにエクスポートすることで、メール作成のライフサイクルを簡素化できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dyspatchアカウント | このパートナーシップを利用するには、[所有者権限または管理者権限](https://docs.dyspatch.io/administration/dyspatch_roles/)を持つ[Dyspatchアカウント](https://www.dyspatch.io/login/)が必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

BrazeとDyspatchの統合により、DyspatchのメールテンプレートをBrazeのメディアライブラリに直接エクスポートしたり、テンプレートをダウンロードして手動でアップロードしたりできます。

### ステップ1:Braze統合の作成 {#step-1-create-the-braze-integration}

Dyspatch管理ポータルでユーザー名のドロップダウンメニューを開き、**Integrations**を選択します。新しい統合を作成し、**Braze**を選択して、Braze APIキーを入力します。

**Localize Exports By**フィールドで、ローカライゼーションの管理方法を選択できます。このフィールドを使用すると、[メールテンプレートをローカライズ](https://docs.dyspatch.io/localization/localizing_a_template/)し、Brazeにエクスポートして、言語やロケールに合わせてパーソナライズされたメールを簡単に送信できます。

![Dyspatchエクスポートテンプレート]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### ステップ2:Brazeへのテンプレートのエクスポート {#step-2-export-template-to-braze}

Dyspatchでメールを完成させた後、テンプレートをBrazeに送信するには、公開済みのメールテンプレートを表示し、**Download/Export**をクリックしてから、**Export to Integration**をクリックします。

テンプレートを手動でアップロードする場合は、公開済みのメールテンプレートを表示し、**Download/Export**をクリックしてから、**Download HTML**をクリックします。次に、Brazeアカウントの**テンプレートとメディア > メールテンプレート**セクションで、**From File**を選択してテンプレートをアップロードします。

![Dyspatchエクスポートテンプレート]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
BrazeのDyspatchメールテンプレートの**Sending Info**セクションで**Inline CSS**を選択しないでください。Dyspatchがこの処理を行い、メールの堅牢性、レスポンシブ対応、送信準備完了を保証します。
{% endalert %}

### 使用方法 {#usage}

Brazeアカウントの**テンプレートとメディア > メールテンプレート**セクションで、アップロードしたDyspatchテンプレートを見つけます。このメールテンプレートを使用して、顧客に魅力的なメールメッセージの送信を開始できます。