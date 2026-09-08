---
nav_title: Census
article_title: Census
description: "このリファレンス記事では、クラウドウェアハウスのデータを使用してターゲットユーザーセグメントを動的に作成できるデータ統合プラットフォームであるCensusとBrazeのパートナーシップについて概説しています。"
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/)は、SnowflakeやBigQueryなどのクラウドデータウェアハウスをBrazeに接続するデータアクティベーションプラットフォームです。マーケティングチームは、ファーストパーティデータの力を解き放ち、ダイナミックなオーディエンスセグメントを構築し、顧客属性を同期してキャンペーンをパーソナライズし、Braze内のすべてのデータを最新の状態に保つことができます。信頼できる実用的なデータで、これまで以上に簡単にアクションを起こすことができます。CSVのアップロードや開発チームへの依頼は必要ありません。

BrazeとCensusの統合により、オーディエンスや製品データをBrazeにダイナミックにインポートし、パーソナライズされたキャンペーンを送信できます。例えば、Brazeで「CLV > 1000のニュースレター購読者」のコホートを作成して価値の高い顧客をターゲットにしたり、「過去30日間にアクティブだったユーザー」のコホートを作成して次期ベータ機能をテストする特定のユーザーをターゲットにしたりできます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| Census アカウント | このパートナーシップを利用するには、[Census アカウント](https://www.getcensus.com/)が必要です。 |
| Braze REST APIキー | すべてのユーザーデータ権限（`users.delete` を除く）と `segments.list` 権限を持つ Braze REST APIキー。Census が対応する Braze オブジェクトを追加するのに伴い、権限セットが変更される場合があります。そのため、今のうちに多めの権限を付与しておくか、将来的にこれらの権限を更新する計画を立てておくことをお勧めします。<br><br>これは Braze ダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | REST エンドポイントURL。エンドポイントは [お使いの Braze インスタンスの URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) によって異なります。 |
| データウェアハウスとデータモデル | 連携を開始する前に、Census でデータウェアハウスをセットアップし、Braze に同期するデータのサブセットのモデルを定義する必要があります。利用可能なデータソースの一覧やモデル作成のガイダンスについては、[Census のドキュメント](https://docs.getcensus.com/destinations/braze)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1: Braze サービス接続を作成する {#step-1-create-braze-service-connection}

Census プラットフォームで Census を連携するには、**Connections** タブに移動し、**New Destination** を選択して新しい Braze サービス接続を作成します。

表示されるプロンプトで、この接続に名前を付け、Braze エンドポイントURLと Braze REST APIキー（およびオプションでコホートを同期するためのデータインポートキー）を入力します。

![Braze 接続の認証情報が設定された Census の新しい送信先ダイアログ。]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### ステップ2: Census の同期を作成する {#step-2-create-a-census-sync}

顧客を Braze に同期するには、同期を作成する必要があります。ここでは、データの同期先と、2つのプラットフォーム間でフィールドをどのようにマッピングするかを定義します。

1. **Syncs** タブに移動し、**New Sync** を選択します。<br><br>
2. コンポーザーで、データウェアハウスからソースデータモデルを選択します。<br><br>
3. モデルの同期先を設定します。送信先として **Braze** を選択し、同期する[サポート対象オブジェクトタイプ](#supported-objects)を選択します。<br>![「Select a Destination」プロンプトで接続として「Braze」が選択されており、さまざまなオブジェクトが一覧表示されている。]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. 適用する同期ルールを選択します（**Update or Create** が最も一般的な選択肢ですが、データの削除を処理するなど、より高度なルールを選択することもできます）。<br><br>
5. 次に、レコードのマッチング目的で、Braze オブジェクトをモデルフィールドに[マッピング](#supported-objects)するための同期キーを選択します。<br>![「Select a Sync Key」プロンプトで、Braze の「External User ID」がソースの「user_id」にマッチしている。]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. 最後に、Census のデータフィールドを対応する Braze フィールドにマッピングします。<br>![Census のマッピング画面]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. 詳細を確認し、同期を作成します。

同期が実行されると、ユーザーデータが Braze に反映されます。Braze セグメントを作成し、今後の Braze キャンペーンやキャンバスに追加して、これらのユーザーをターゲットにすることができます。

{% alert note %}
Census と Braze の連携を使用する場合、Census は各同期で差分（変更されたデータ）のみを Braze に送信します。
{% endalert %}

## サポートされるオブジェクト {#supported-objects}

Census は現在、以下の Braze オブジェクトの同期をサポートしています。

| オブジェクト名 | 同期動作 |
| --- | --- |
| User | Update、Create、Mirror、Delete |
| Cohort | Update、Create、Mirror |
| Catalog | Update、Create、Mirror |
| Subscription Group Membership | Mirror |
| Event | Append |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされるオブジェクト" }

さらに、Census は Braze への[構造化データ](https://docs.getcensus.com/destinations/braze#supported-objects)の送信もサポートしています。ユーザーのプッシュトークンを送信するには、データを2〜3個の値（`app_id`、`token`、およびオプションの `device_id`）を持つオブジェクトの配列として構造化する必要があります。