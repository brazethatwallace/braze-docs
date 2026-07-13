---
nav_title: EmailShepherd
article_title: EmailShepherd
alias: /partners/emailshepherd/
description: "このリファレンス記事では、BrazeとEmailShepherdのパートナーシップについて説明します。EmailShepherdは、メールデザインシステムに基づいて構築されたエージェント型メール作成プラットフォームで、承認済みメールをBrazeワークスペースに公開します。"
page_type: partner
search_tag: Partner
---

# EmailShepherd

> [EmailShepherd](https://emailshepherd.com/)は、メールデザインシステムに基づいて構築されたエージェント型メール作成プラットフォームです。マーケティングチーム全体とAIエージェントが、ボトルネックなしにブランドに沿った本番対応のメールを作成できます。Brazeとの統合により、承認済みメールをBrazeワークスペースに直接公開できるため、マーケターはブランドの一貫性を損なうことなく、Brazeでのメール制作を拡大できます。

_この統合はEmailShepherdによって管理されています。_

## 統合について {#about-the-integration}

BrazeとEmailShepherdの統合により、EmailShepherdでメールデザインシステムに基づいたメールを作成し、メールテンプレートとしてBrazeにエクスポートできます。チームはEmailShepherdでメールを作成・承認し、手動のHTMLの受け渡しなしに本番対応のテンプレートをBrazeに公開します。

## 前提条件 {#prerequisites}

この統合を使用するには、以下が必要です。

| 要件 | 説明 |
| ----------- | ----------- |
| EmailShepherdアカウント | この統合を使用するには、EmailShepherdアカウントが必要です。 |
| Braze REST APIキー | 「テンプレート」の完全な権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | Brazeの[クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、BrazeダッシュボードおよびRESTエンドポイントと対応しています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

EmailShepherdは、すべての送信をブランドに沿ったものに保ちながらメール制作を拡大したいチーム向けに構築されています。以下のような場合に最適です。

- **大規模なブランドの一貫性を確保する:** メールデザインシステムが承認済みのコンポーネント、カラー、レイアウトを定義します。Brazeに公開されるすべてのメールは、設計上ブランドに沿ったものになります。
- **チーム全体にメール制作を開放する:** メールデザインシステムを活用したドラッグ＆ドロップビルダーにより、誰でも本番対応のメールを作成できます。
- **エージェント型キャンペーン作成を活用する:** AIエージェントがメールデザインシステムのガードレール内で構築するため、作成されたキャンペーンはブランドに沿っており、すぐに送信できます。

## 統合 {#integration}

### ステップ 1: EmailShepherdコネクターを作成する {#step-1-create-your-emailshepherd-connector}

{% alert note %}
これは一度だけのセットアップです。コネクターを作成すると、EmailShepherdはこれらの認証情報を今後のすべてのBrazeへのエクスポートに使用します。
{% endalert %}

1. EmailShepherdで、**Connectors** > **Add connector**に移動します。
2. **Braze**を選択し、コネクター名を入力します。
3. APIキーを入力し、Brazeインスタンスを選択します。
4. **Create Connector**を選択して接続を保存します。

![BrazeインスタンスとAPIキーフィールドを含むEmailShepherdコネクターフォーム]({% image_buster /assets/img_archive/emailshepherd_step1.png %}){: style="max-width:60%;"}

### ステップ 2: EmailShepherdからメールをエクスポートする {#step-2-export-an-email-from-emailshepherd}

EmailShepherdで、Brazeにエクスポートしたいメールを見つけます。公開済みであることを確認し、**Export**を選択します。

![エクスポートアクションを含むEmailShepherdメールエディター]({% image_buster /assets/img_archive/emailshepherd_step2.png %}){: style="max-width:60%;"}

### ステップ 3: 設定してBrazeに公開する {#step-3-configure-and-publish-to-braze}

1. エクスポートページで、**Connectors**の下にあるBrazeコネクターを選択します（例: **Braze Prod**）。
2. EmailShepherd画像ライブラリーの画像に対する**Image hosting**オプションを選択します。URLで入力された画像はエクスポート時に変更されません。
3. **Locale**を確認し、Brazeでのメールの**Template name**を入力します。
4. **Start export**を選択します。

![Brazeコネクター、画像ホスティング、テンプレート名フィールドを含むEmailShepherdエクスポートページ]({% image_buster /assets/img_archive/emailshepherd_step3.png %}){: style="max-width:60%;"}

## 統合の使用 {#use-the-integration}

Brazeで、エクスポートされたメールを**コンテンツ** > **メール**で確認できます。これらのテンプレートはBrazeのキャンペーンやキャンバスで使用できます。

## サポート {#support}

EmailShepherdの統合に関する詳細については、[EmailShepherdドキュメント](https://emailshepherd.com/docs/)を参照してください。