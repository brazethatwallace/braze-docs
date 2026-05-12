---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "この参考記事では、インタラクティブな要素を含む洗練されたメールを作成するためのドラッグ＆ドロップメールテンプレートビルダーであるStripoとBrazeのパートナーシップについて説明しています。"
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/)は、インタラクティブな要素を含むレスポンシブメールをデザインできるドラッグ＆ドロップのメールテンプレートビルダーです。Stripoユーザーは HTML で編集することもでき、Stripoエディターを通じてさまざまなデバイスで表示・非表示にする要素を決めることができます。

_この統合はStripoによって管理されています。_

## 統合について {#about-the-integration}

BrazeとStripoの統合により、カスタマイズしたStripoメールをエクスポートし、Braze内でテンプレートとしてアップロードできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ------------| ----------- |
| Stripoアカウント | このパートナーシップを利用するには、Stripoアカウントが必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| クラスターインスタンス | Brazeの[クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、BrazeダッシュボードとRESTエンドポイントに対応しています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1：Stripoメールを作成する {#step-1-create-stripo-email}

Stripoプラットフォームでメールを作成し、**Export**をクリックします。

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### ステップ2：テンプレートをBrazeにエクスポートする {#step-2-export-template-to-braze}

表示されるダイアログで、エクスポート方法として**Braze**を選択します。

次に、**アカウント名**（ワークスペース名など）、**APIキー**、**クラスターインスタンス**を入力します。

![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
これは1回限りのセットアップであり、今後のエクスポートでは自動的にこのAPIキーが使用されます。
{% endalert %}

## 使用方法 {#usage}

アップロードしたStripoテンプレートは、Brazeアカウントの**テンプレートとメディア > メールテンプレート**セクションで確認できます。このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信しましょう！