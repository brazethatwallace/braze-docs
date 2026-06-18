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

> [Mozart Data](https://mozartdata.com/) は、Fivetran、Portable、Snowflakeを利用するオールインワンの最新データプラットフォームです。

BrazeとMozart Dataの統合により、以下のことが可能になります。
- Fivetranを使ってBrazeのデータをSnowflakeにインポートする
- Brazeのデータと他のアプリケーションのデータを組み合わせてトランスフォームを作成し、ユーザーの行動を効果的に分析する
- SnowflakeからBrazeにデータをインポートし、新たなカスタマーエンゲージメントの機会を創出する
- Brazeのデータを他のアプリケーションのデータと組み合わせ、ユーザーの行動をより総合的に理解する
- ビジネスインテリジェンスツールと統合し、Snowflakeに保存されているデータをさらに詳しく調査する

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

| 必要条件 | 説明 |
| ----------- | ----------- |
| Mozart Dataアカウント | このパートナーシップを活用するには、Mozart Dataアカウントが必要です。[こちらからご登録ください。](https://app.mozartdata.com/signup)|
| Snowflakeアカウント<br>オプション1: 新規アカウント | Mozart Dataのアカウント作成プロセスで **Create a New Snowflake Account** を選択すると、Mozart Dataにより新しいSnowflakeアカウントがプロビジョニングされます。 |
| Snowflakeアカウント<br>オプション2: 既存アカウント | 組織がすでにSnowflakeアカウントを所有している場合は、Mozart Data Connectedオプションを使用できます。<br><br>既存のSnowflakeアカウントに接続するには、**Already Have a Snowflake Account** オプションを選択します。このオプションを使用する場合は、アカウントレベルの権限を持つユーザーが[以下の手順に従って操作する](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount)必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

この統合は、[BrazeからMozart Dataへの](#syncing-data-from-braze-to-mozart-data)データ同期と[Mozart DataからBrazeへの](#syncing-data-from-mozart-data-to-braze)データ同期の両方でサポートされています。

### BrazeからMozart Dataにデータを同期する {#syncing-data-from-braze-to-mozart-data}

#### ステップ1: Brazeコネクターを設定する {#step-1-set-up-braze-connector}

1. Mozart Dataで **Connectors** に移動し、**Add Connector** をクリックします。
2. 「Braze」を検索し、コネクターカードを選択します。
3. Brazeから同期されたすべてのデータが保存される送信先スキーマ名を入力します。デフォルトのスキーマ名`braze`を使用することを推奨します。
4. **Add Connector** をクリックします。

#### ステップ2: Fivetranコネクターフォームに情報を入力する {#step-2-fill-out-the-fivetran-connector-form}

Fivetranコネクターページにリダイレクトされます。このページで所定のフィールドに入力します。次に、**Continue** > **Save & Test** をクリックしてFivetranコネクターを完成させます。

FivetranがBrazeアカウントからSnowflakeデータウェアハウスへのデータの同期を開始します。コネクターの同期が完了したら、Mozart Dataからクエリデータにアクセスできます。

### Mozart DataからBrazeにデータを同期する {#syncing-data-from-mozart-data-to-braze}

#### ステップ1: Snowflakeデータウェアハウスをセットアップする {#step-1-set-up-a-snowflake-data-warehouse}

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake)の手順に従って、Snowflakeインターフェイスからテーブル、ユーザー、権限を設定します。このステップには、管理者レベルのSnowflakeアクセスが必要であることに注意してください。

#### ステップ2: BrazeでSnowflakeとの統合をセットアップする {#step-2-set-up-your-snowflake-integration-in-braze}

Snowflakeウェアハウスの設定後に、Mozart Dataの **Integration** ページで **Braze** を選択します。ここで、Brazeに提供する必要がある認証情報を確認します。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

次に、Brazeにサインインした状態で **[統合] > [テクノロジーパートナー] > [Snowflake]** に移動し、統合プロセスを開始します。Mozart Dataから認証情報をコピーし、Snowflake Dataのインポートページに追加します。**Set up sync details** をクリックし、Snowflakeアカウントとソーステーブルの情報を入力します。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

次に、BrazeのSnowflakeデータ取り込み画面で、同期の名前を選択し、連絡先のメールアドレスを入力し、データタイプと同期頻度を選択します。

#### ステップ3: Brazeユーザーに公開キーを追加する {#step-3-add-a-public-key-to-the-braze-user}
この時点で、Snowflakeに戻って設定を完了する必要があります。BrazeダッシュボードにBrazeに表示される公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflakeのドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でキーのローテーションを行う場合、Mozart Dataは新規のキーペアを生成して、新規の公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### ステップ4: 接続をテストする {#step-4-test-connection}

ユーザーが公開キーで更新されたら、Brazeダッシュボードに戻って **Test connection** をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続に失敗した場合、トラブルシューティングに役立つエラーメッセージが表示されます。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
統合を下書き状態からアクティブ状態に移行するには、統合のテストに成功する必要があります。作成ページを閉じる必要がある場合は、統合が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。
{% endalert %}

## この統合を使用する {#using-this-integration}

### Mozart Dataユーザーとして Brazeのデータにアクセスする方法 {#how-to-access-braze-data-as-a-mozart-data-user}
Mozart Dataアカウントが作成されたら、Mozart DataからSnowflakeデータウェアハウスに同期されたBrazeデータにアクセスできます。

#### トランスフォーム {#transforms}
Mozart Dataは、ユーザーがビューやテーブルを作成するためのSQL変換レイヤーを提供しています。各ユーザーの製品使用データ、取引履歴、Brazeメッセージとのエンゲージメントアクティビティを要約するユーザーレベルのディメンションテーブル（`dim_users`など）を作成できます。

#### 分析 {#analysis}
Brazeから同期された変換モデルまたは生データを使用して、Brazeメッセージに対するユーザーのエンゲージメントを分析できます。さらに、Brazeデータを他のアプリケーションのデータと組み合わせて、Brazeメッセージに対するユーザーのインタラクションから得たインサイトが、ユーザーに関して所有している他のデータとどのように関連しているかを分析できます。たとえば、顧客のデモグラフィック情報、ショッピング履歴、製品の使用状況、カスタマーサービスエンゲージメントなどです。

これは、ユーザーのリテンションを向上させるためのエンゲージメント戦略について、より多くの情報に基づいた意思決定を行うのに役立ちます。これはすべて、クエリツールを使ってMozart Dataのインターフェイス内で行うことができ、結果をGoogleシートやCSVにエクスポートしてプレゼンテーションに備えることができます。

#### ビジネスインテリジェンス（BI） {#business-intelligence-bi}
インサイトを可視化し、他のチームメンバーと共有する準備はできていますか？Mozart Dataは、ほぼすべてのBIツールと統合されています。BIツールをまだお持ちでない場合は、Mozart Dataに連絡して無料のMetabaseアカウントをセットアップしてください。