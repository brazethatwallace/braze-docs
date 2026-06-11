---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "この参考記事では、Brazeと、チャネルを横断してモバイルレスポンシブなメールテンプレートを作成するためのエンタープライズメールプラットフォームStensulとのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/)は、メールマーケターがキャンペーン作成のためにリアルタイムでBrazeに送信する前に、Stensulでモバイルレスポンシブでブランドに沿ったメールを作成するためのツールを提供します。

_この統合はStensulによって管理されています。_

## 統合について {#about-the-integration}

BrazeとStensulの統合により、HTML形式のStensulメールをエクスポートし、Braze内でテンプレートとしてアップロードできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ------------| ----------- |
| Stensulアカウント | このパートナーシップを活用するには、Stensulアカウントが必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| クラスターインスタンス | Brazeの[クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、BrazeダッシュボードとRESTエンドポイントに対応しています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

Braze REST APIキーとクラスターインスタンスをStensulカスタマーサクセスチームに提供してください。その後、チームが初期統合を設定します。

{% alert important %}
これは1回限りの設定であり、今後のエクスポートではこのAPIキーが自動的に使用されます。
{% endalert %}

### ステップ1：Stensulメールを作成する {#step-1-create-stensul-email}

StensulプラットフォームでStensulメールを作成し、**Complete**をクリックします。

![Stensul保存オプション]({% image_buster /assets/img_archive/stensul_save_options.png %})

### ステップ2：Brazeにテンプレートをエクスポートする {#step-2-export-template-to-braze}
完了ページに表示される新しいダイアログで、**Upload to ESP**を選択します。

![Stensulアップロードオプション]({% image_buster /assets/img_archive/stensul_upload_options.png %})

次に、メールの**template name**、**subject**、および**preheader**を入力し、**Upload**を選択します。アップロードが成功したことを示す確認と、該当する場合はファイルの過去のアップロード履歴が表示されます。

![Stensulアップロード成功]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## 使用方法 {#usage}

アップロードしたStensulテンプレートは、Brazeアカウントの**テンプレートとメディア > メールテンプレート**セクションで確認できます。このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信しましょう！