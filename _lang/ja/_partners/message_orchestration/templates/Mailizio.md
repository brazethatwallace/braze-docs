---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "この参考記事では、再利用可能でブランドセーフなコンテンツをデザインし、Brazeにエクスポートできるメール作成・管理プラットフォームであるMailizioとBrazeのパートナーシップについて説明しています。"
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/)は、直感的なビジュアルエディターを使って、再利用可能でブランドセーフなコンテンツを簡単にデザインできるメール作成・管理プラットフォームです。MailizioとBrazeの統合により、コンテンツブロックとメールテンプレートをエクスポートし、同じアセットからアプリ内メッセージを自動的に生成できるため、迅速かつ完全にコントロールされたキャンペーン展開が可能になります。

_この統合はMailizioによって維持されています。_

## 統合について {#about-the-integration}

MailizioとBrazeの統合により、Mailizioのエディターを使用してダイナミックなメールテンプレートをデザインし、Brazeの設定で使用されているLiquid変数を活用し、効率的なキャンペーン実行のためにBrazeにプッシュすることができます。

## ユースケース {#use-cases}

- キャンペーンやトランザクションメッセージ用に、すぐに送信できるメールテンプレートをBrazeに直接プッシュできます。
- 再利用可能なコンテンツモジュール（ヘッダー、フッター、プロモーションなど）を構築し、複数のキャンペーンやチャネルにわたって制作を効率化できます。
- メールからアプリ内メッセージを生成：Mailizioはメールの関連セクションを識別し、アプリ内キャンペーンで使用するためにHTMLをエクスポートできます。
- メールとアプリ内メッセージの両方でBraze互換のLiquid変数を使用して、大規模なパーソナライゼーションを実現できます。
- クリエイティブアセットをMailizioで管理し、1回のエクスポートでBrazeを更新することで、ブランディングの一貫性を保てます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Mailizioアカウント | このパートナーシップを利用するには、Mailizioアカウントが必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br>Braze REST APIキーは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Mailizioのカスタマーサクセスマネージャーに、Braze REST APIキーとクラスターインスタンスを提供してください。その後、Mailizioチームが最初の統合設定を行います。

{% alert important %}
これは1回限りのセットアップであり、今後のエクスポートはすべて自動的にこのAPIキーを利用します。
{% endalert %}

### ステップ 1: Mailizioでメールを作成する {#step-1-create-an-email-in-mailizio}

Mailizioで、ドラッグ＆ドロップエディターを使ってブランドアイデンティティを反映したメールを作成し、**Save**をクリックして作業内容を保存します。

![ドラッグ＆ドロップエディターのスクリーンショット]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### ステップ 2: Brazeへメールテンプレートをエクスポートする {#step-2-export-your-email-template-to-braze}

準備ができたら、**Export Newsletter**をクリックします。ポップアップで**Braze-email**を選択し、エクスポートを確認します。

後でコンテンツを更新した場合は、Mailizioから再エクスポートしてBrazeの内容を更新してください。

![エクスポートモーダルのスクリーンショット]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}
Mailizioの**Module**エディターを使用して、同じ方法でコンテンツブロックを作成し、エクスポートすることもできます。
{% endalert %}

## 使用方法 {#usage}

アップロードしたMailizioテンプレートは、Brazeアカウントの**テンプレートとメディア > メールテンプレート**セクションで確認できます。このメールテンプレートを使用して、顧客に魅力的なメールメッセージの送信を開始しましょう！