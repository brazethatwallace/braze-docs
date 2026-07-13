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

| 必要条件 | 説明 |
| --- | --- |
| Censusアカウント | このパートナーシップを活用するには、[Censusアカウント](https://www.getcensus.com/)が必要です。 |
| Braze REST APIキー | すべてのユーザーデータ権限（`users.delete`を除く）と`segments.list`権限を持つBraze REST APIキー。CensusがサポートするBrazeオブジェクトの増加に伴い、権限セットが変わる可能性があります。このため、この時点でより多くの権限を付与するか、これらの権限を今後更新する計画を立てることをお勧めします。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[BrazeインスタンスのURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)によって異なります。 |
| データウェアハウスとデータモデル | 統合を開始する前に、Censusでデータウェアハウスをセットアップし、Brazeと同期させたいデータのサブセットのモデルを定義しておく必要があります。利用可能なデータソースのリストとモデル作成に関するガイダンスについては、[Censusのドキュメント](https://docs.getcensus.com/destinations/braze)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:Brazeサービス接続を作成する {#step-1-create-braze-service-connection}

CensusプラットフォームでCensusを統合するには、**Connections** タブに移動し、**New Destination** を選択して新しいBrazeサービス接続を作成します。

表示されるプロンプトで、この接続に名前を付け、BrazeエンドポイントURLとBraze REST APIキー（オプションで、コホートを同期するためのデータインポートキー）を入力します。

![Braze接続の認証情報が設定されたCensusの新しい送信先ダイアログ。]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### ステップ2:Censusの同期を作成する {#step-2-create-a-census-sync}

顧客をBrazeに同期するには、同期を作成する必要があります。ここで、データを同期する場所と、2つのプラットフォーム間でどのようにフィールドをマッピングするかを定義します。

1. **Syncs** タブに移動し、**New Sync** を選択します。<br><br>
2. コンポーザーで、データウェアハウスからソースデータモデルを選択します。<br><br>
3. モデルの同期先を設定します。送信先として**Braze**を選択し、同期する[サポートされているオブジェクトタイプ](#supported-objects)を選択します。<br>![「Select a Destination」プロンプトで接続として「Braze」が選択されており、さまざまなオブジェクトが一覧表示されている。]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. 適用する同期ルールを選択します（**Update or Create**が最も一般的な選択肢ですが、データの削除を処理するためのより詳細なルールを選択することもできます）。<br><br>
5. 次に、レコードマッチングのために、Brazeオブジェクトをモデルフィールドに[マッピング](#supported-objects)するシンクキーを選択します。<br>![「Select a Sync Key」プロンプトで、Brazeの「External User ID」がソースの「user_id」にマッチングされている。]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. 最後に、Censusデータフィールドを対応するBrazeフィールドにマッピングします。<br>![Censusでのマッピング]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. 詳細を確認し、同期を作成します。

同期が実行されると、Brazeにユーザーデータが表示されます。今後のBrazeキャンペーンやキャンバスにBrazeセグメントを作成・追加して、これらのユーザーをターゲットにできるようになります。

{% alert note %}
CensusとBrazeの統合を使用する場合、Censusは同期のたびにBrazeへ差分（変更データ）のみを送信します。
{% endalert %}

## サポートされるオブジェクト {#supported-objects}

Censusは現在、以下のBrazeオブジェクトの同期をサポートしています。

| オブジェクト名 | 同期の動作 |
| --- | --- |
| ユーザー | 更新、作成、ミラー、削除 |
| コホート | 更新、作成、ミラー |
| カタログ | 更新、作成、ミラー |
| 購読グループメンバーシップ | ミラー |
| イベント | 追加 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされるオブジェクト" }

さらに、CensusはBrazeへの[構造化データ](https://docs.getcensus.com/destinations/braze#supported-objects)の送信もサポートしています。
- ユーザープッシュトークン：プッシュトークンを送信するには、データを2〜3の値を持つオブジェクトの配列として構造化する必要があります。`app_id`、`token`、およびオプションの`device_id`です。
- 階層化カスタム属性：オブジェクトと配列の両方がサポートされています。2022年4月現在、この機能はまだ早期アクセス段階です。アクセスするには、Brazeのアカウントマネージャーに連絡する必要がある場合があります。