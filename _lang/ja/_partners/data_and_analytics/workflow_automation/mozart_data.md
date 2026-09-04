---
nav_title: Mozart Data
article_title: Mozart Data
description: "このリファレンス記事では、BrazeとMozart Dataのパートナーシップについて説明します。Mozart Dataはオールインワンの最新データプラットフォームであり、Fivetranを使用してSnowflakeへのデータのインポート、トランスフォームの作成、データの結合などを行うことができます。"
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/)は、Fivetran、Portable、Snowflakeを利用するオールインワンの最新データプラットフォームです。

BrazeとMozart Dataの統合により、以下のことが可能になります。
{% multi_lang_include partners/workflow_automation/mozart_data_integration_bullets.md %}

## 前提条件 {#prerequisites}

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| 要件 | 説明 |
| ----------- | ----------- |
| Mozart Dataアカウント | このパートナーシップを利用するには、Mozart Dataアカウントが必要です。[Mozart Dataアカウントに登録する](https://app.mozartdata.com/signup)|
| Snowflakeアカウント<br>オプション1：新規アカウント | Mozart Dataアカウント作成プロセスで**Create a New Snowflake Account**を選択すると、Mozart Dataが新しいSnowflakeアカウントをプロビジョニングします。 |
| Snowflakeアカウント<br>オプション2：既存アカウント | 組織がすでにSnowflakeアカウントを持っている場合は、Mozart Data Connectedオプションを使用できます。<br><br>**Already Have a Snowflake Account**オプションを選択して、既存のSnowflakeアカウントを接続します。このオプションを利用するには、アカウントレベルの権限を持つユーザーが[こちらの手順に従う](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount)必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

この連携は、[BrazeからMozart Dataへのデータ同期](#syncing-data-from-braze-to-mozart-data)と[Mozart DataからBrazeへのデータ同期](#syncing-data-from-mozart-data-to-braze)の両方をサポートしています。

### BrazeからMozart Dataへのデータ同期 {#syncing-data-from-braze-to-mozart-data}

#### ステップ1:Brazeコネクターを設定する {#step-1-set-up-braze-connector}

1. Mozart Dataで、**Connectors**に移動し、**Add Connector**を選択します。
2. 「Braze」を検索し、コネクターカードを選択します。
3. Brazeから同期されたすべてのデータが保存される宛先スキーマ名を入力します。デフォルトのスキーマ名`braze`を使用することをお勧めします。
4. **Add Connector**を選択します。

#### ステップ2:Fivetranコネクターフォームに入力する {#step-2-fill-out-the-fivetran-connector-form}

ステップ1を完了すると、Fivetranコネクターページが開きます。指定されたフィールドに入力し、**Continue** > **Save & Test**を選択してFivetranコネクターの設定を完了します。

FivetranがBrazeアカウントからSnowflakeデータウェアハウスへのデータ同期を開始します。コネクターの同期が完了すると、Mozart Dataからクエリデータにアクセスできます。

### Mozart DataからBrazeへのデータ同期 {#syncing-data-from-mozart-data-to-braze}

#### ステップ1:Snowflakeデータウェアハウスを設定する {#step-1-set-up-a-snowflake-data-warehouse}

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake)の手順に従って、Snowflakeインターフェイスからテーブル、ユーザー、権限を設定します。このステップには管理者レベルのSnowflakeアクセスが必要です。

#### ステップ2:BrazeでSnowflake連携を設定する {#step-2-set-up-your-snowflake-integration-in-braze}

Snowflakeウェアハウスを設定した後、Mozart Dataで**Integration**ページに移動し、**Braze**を選択します。**Braze**連携ビューに、Brazeにコピーする認証情報が表示されます。

![Mozart DataのBraze連携ページ。Brazeが選択され、Brazeで使用するSnowflake接続認証情報が表示されています。]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

次に、Brazeにサインインした状態で、**連携 > テクノロジーパートナー > Snowflake**に移動して連携プロセスを開始します。Mozart Dataから認証情報をコピーし、Snowflakeデータインポートページに追加します。**同期の詳細を設定**を選択し、Snowflakeアカウントとソーステーブルの情報を入力します。

![BrazeのSnowflakeパートナー連携フォーム。アカウント、ウェアハウス、データベース、スキーマの各フィールドにMozart Dataの認証情報が入力されています。]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

次に、Braze Snowflakeインポート設定画面で、同期の名前を選択し、連絡先メールアドレスを入力し、データタイプと同期頻度を選択します。

#### ステップ3:Brazeユーザーに公開キーを追加する {#step-3-add-a-public-key-to-the-braze-user}
この時点で、Snowflakeに戻って設定を完了します。BrazeがSnowflakeに接続するために作成したユーザーに、Brazeダッシュボードに表示される公開キーを追加します。

この方法の詳細については、[Snowflakeドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。キーをローテーションしたい場合、Mozart Dataが新しいキーペアを生成し、新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### ステップ4:接続をテストする {#step-4-test-connection}

ユーザーが公開キーで更新されたら、Brazeダッシュボードに戻り、**接続をテスト**を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続が失敗した場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![BrazeのSnowflake連携テスト接続結果。公開キーの適用後、成功したプレビューが表示されています。]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
連携を下書きからアクティブ状態に移行するには、テストに成功する必要があります。作成ページを閉じる必要がある場合、連携は保存され、詳細ページに戻って変更やテストを行うことができます。
{% endalert %}

## この連携の使い方 {#using-this-integration}

### Mozart Dataユーザーとして Brazeデータにアクセスする方法 {#how-to-access-braze-data-as-a-mozart-data-user}
Mozart Dataアカウントの作成が完了すると、SnowflakeデータウェアハウスにBrazeから同期されたデータにMozart Dataからアクセスできます。

#### 変換 {#transforms}
Mozart DataはSQLの変換レイヤーを提供しており、ユーザーがビューやテーブルを作成できます。ユーザーレベルのディメンションテーブル（例：`dim_users`）を作成して、各ユーザーの製品利用データ、取引履歴、Brazeメッセージとのエンゲージメントアクティビティを集約できます。

#### 分析 {#analysis}
変換モデルやBrazeから同期された生データを使用して、Brazeメッセージに対するユーザーのエンゲージメントを分析できます。さらに、Brazeデータを他のアプリケーションデータと組み合わせて、Brazeメッセージとのインタラクションから得られたインサイトが、ユーザーに関する他のデータとどのように関連しているかを分析できます。たとえば、人口統計情報、購買履歴、製品利用状況、カスタマーサービスとのエンゲージメントなどです。

これにより、ユーザーリテンションを向上させるためのエンゲージメント戦略について、より情報に基づいた意思決定を行うことができます。これらはすべてMozart Dataのインターフェイス内でクエリツールを使用して実行でき、結果をGoogle SheetやCSVにエクスポートしてプレゼンテーションの準備を行えます。

#### ビジネスインテリジェンス（BI） {#business-intelligence-bi}
インサイトを可視化して他のチームメンバーと共有する準備はできましたか？Mozart Dataはほぼすべてのビジネスインテリジェンスツールと連携できます。まだビジネスインテリジェンスツールをお持ちでない場合は、Mozart Dataに連絡して無料のMetabaseアカウントを設定してください。