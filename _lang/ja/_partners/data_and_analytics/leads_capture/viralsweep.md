---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "このリファレンス記事では、Brazeと、ブランドが懸賞、コンテスト、インスタントウィン、ウェイトリスト、紹介プロモーションなどのデジタルマーケティングプロモーションを構築、実行、管理できるソフトウェアサービスであるViralSweepとのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com)は、懸賞、コンテスト、インスタントウィン、ウェイトリスト、紹介プロモーションなどのデジタルマーケティングプロモーションを、ブランドが構築、実行、管理できるようにするソフトウェアサービスです。

_この統合はViralSweepによって管理されています。_

## 統合について {#about-the-integration}

BrazeとViralSweepの統合により、ViralSweepプラットフォームで懸賞やコンテストを開催し（メールとSMSのリストを拡大）、キャンペーンやキャンバスで使用するために懸賞やコンテストのエントリ情報をBrazeに送信できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| ViralSweepアカウント | このパートナーシップを活用するには、ビジネスプランを利用しているViralSweepアカウントが必要です。 |
| Braze REST APIキー | すべてのユーザーデータおよびメール権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**Settings** > **API Keys**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1：ViralSweep内でBrazeに接続する {#step-1-connect-to-braze-within-viralsweep}

ViralSweepで、**Integrations > Email & SMS > Add Service**に移動し、**Braze**を選択します。

![ViralSweepでBrazeサービスを接続する手順を示すアニメーション]({% image_buster /assets/img/viralsweep/connect.gif %})

### ステップ2：Braze認証情報を追加する {#step-2-add-braze-credentials}

統合設定ウィンドウで、Braze REST APIキーとRESTエンドポイントを入力します。指定するエンドポイントに`https://`が含まれていないことを確認してください（例：`dashboard-03.braze.com`）。

![ユーザーにBraze APIキーとBrazeダッシュボードURLの入力を求めるViralSweepサービス統合ページ。]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

**Connect**をクリックします。

### ステップ3：Braze認証情報を追加する {#step-3-add-braze-credentials}
接続が完了しました。プロモーションがBrazeに接続され、ViralSweepによって収集されたすべてのエントリが自動的にBrazeに送信されます。

## よくある質問 {#frequently-asked-questions}

### ViralSweepからBrazeにはどのフィールドが渡されますか？ {#what-fields-does-viralsweep-pass-to-braze}
- 名
- 姓
- メールアドレス
- 住所
- 住所2
- 市区町村
- 都道府県
- 郵便番号
- 国
- 生年月日
- 電話番号
- プロモーションID
- 紹介リンク
- トラッキングキャンペーン名

### ViralSweepではサブスクライバーが更新されますか？ {#does-viralsweep-update-subscribers}
はい。プロモーションを実行し、ViralSweepが誰かをBrazeに渡した後、将来別のプロモーションを実行して同じ人物がエントリした場合、その人物の情報はBrazeで自動的に更新されます（新しい情報が提供された場合）。主に、紹介URLはエントリした各プロモーションの最新URLに更新され、プロモーションIDフィールドにはこれまでにエントリしたすべてのプロモーションのIDが含まれます。

## トラブルシューティング {#troubleshooting}

Brazeに接続しているにもかかわらず、データがアカウントに追加されない場合は、次のような理由が考えられます。

- **メールがすでにBrazeに存在している**<br>
プロモーションに入力されたメールアドレスがすでにBrazeアカウントに存在している可能性があるため、再度追加されることはありません。その連絡先に新しい情報が提供された場合にのみ更新されます。<br><br>
- **メールがすでにViralSweepに入力されている**<br>
プロモーションに入力されたメールアドレスはすでに以前入力されているため、再度Brazeに渡されることはありません。これは、すでにプロモーションにエントリした後にBraze統合を設定した場合に発生することがあります。