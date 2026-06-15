---
nav_title: トレジャーデータ
article_title: トレジャーデータのコホートインポート
description: "このリファレンス記事では、トレジャーデータのコホートインポート機能について説明します。"
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# トレジャーデータのコホートインポート {#treasure-data-cohort-import}

> この記事では、トレジャーデータからBrazeにユーザーコホートをインポートする方法について説明します。これにより、ウェアハウスにしか存在しないデータに基づいてターゲットキャンペーンを送信できるようになります。

{% alert important %}
この機能は現在ベータ版です。詳細については、トレジャーデータおよびBrazeの担当者にお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| トレジャーデータのアカウント | このパートナーシップを利用するには、[トレジャーデータ](https://www.treasuredata.com/)のアカウントが必要です。 |
| Brazeデータインポートキー | これは、Brazeダッシュボードの**パートナー連携** > **テクノロジーパートナー**から**トレジャーデータ**を選択して取得できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
| トレジャーデータの静的IPアドレス | トレジャーデータの静的IPアドレスは、この統合のリンクのアクセスポイントおよびソースです。静的IPアドレスを確認するには、トレジャーデータのカスタマーサクセス担当者またはトレジャーデータの技術サポートにご連絡ください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## データインポート統合 {#data-import-integration}

### ステップ1:Brazeデータインポートキーを取得する {#step-1-get-your-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**トレジャーデータ**を選択します。ここで、RESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。

### ステップ2:データ接続を作成する {#step-2-create-a-data-connection}

トレジャーデータ内でデータ接続を作成する前に、認証が必要になります。まず、**Integrations Hub**を選択し、次に**Catalog**を選択します。

![Treasure Data Integrations Hubのカタログ]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %})

**Catalog**でBraze統合を検索し、アイコンにカーソルを合わせて**Create Authentication**を選択します。認証情報を入力し、認証に名前を付けて、**Done**を選択します。

![Treasure Data Integrations Hubのカタログ]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %})

### ステップ3:コホートオーディエンスを定義する {#step-3-define-your-cohort-audience}

**Audience Studio**でのアクティベーション、または**Data Workbench**でのクエリ実行を通じて、コホートをBrazeに同期します。

{% alert important %}
Braze内にすでに存在するユーザーのみが、コホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### ステップ3.1:クエリを定義する {#step-31-define-your-query}

{% alert note %}
クエリ列は正確な列名とデータ型で指定する必要があります。クエリの列には、`user_ids`、`device_ids`、またはUIの設定と一致するBrazeエイリアス列のうち、少なくとも1つが含まれている必要があります。Braze内に存在するユーザープロファイルのみがコホートに追加されます。コホートインポートでは、新しいユーザープロファイルは作成されません。
{% endalert %}

1. **Data Workbench** > **Queries**に移動します。
2. **New Query**を選択します。
3. クエリを実行して結果セットを検証します。

![Treasure Data Integrations Hubのカタログ]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### ユースケース:識別子によるコホートの同期 {#use-case-syncing-cohorts-by-identifier}

{% subtabs local %}
{% subtab Syncing External IDs %}
次にトレジャーデータのテーブルの例を示します。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
列名は`user_ids`である必要があります。そうでないと同期が失敗します。
{% endalert %}

external IDを使用してコホートを同期するには、次のクエリを実行します:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

クエリを実行すると、これらのユーザーエイリアスがBrazeのコホートに追加されます:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
次にトレジャーデータのテーブルの例を示します。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

ユーザーエイリアスを使用してコホートを同期するには、次のクエリを実行します:

`````````sql
SELECT
  email
FROM
  example_cohort_table
```

クエリを実行すると、これらのユーザーエイリアスがBrazeのコホートに追加されます:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
次にトレジャーデータのテーブルの例を示します。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
列名は`device_ids`である必要があります。そうでないと同期が失敗します。
{% endalert %}

デバイスIDを使用してコホートを同期するには、次のクエリを実行します:

`````````sql
SELECT
  device_ids
FROM
  example_cohort_table
```

クエリを実行すると、これらのデバイスIDがBrazeのコホートに追加されます:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### ステップ3.2:結果のエクスポートターゲットを指定する {#step-32-specify-the-result-export-target}

クエリが構築されたら、**Export Results**を選択します。既存の認証（前のステップで作成した認証など）を選択するか、出力に使用する新しい認証を作成できます。

![Treasure Data Integrations Hubのカタログ]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %})


| エクスポート結果マッピング |	説明	|
| ----------- | ----------- |
| コホートID	| Brazeに送信されるバックエンドのコホート識別子です。	|
| コホート名（任意）	| Brazeのセグメンテーションツール内のコホートフィルターに表示される名前です。設定されていない場合、`Cohort ID`が`Cohort Name`として使用されます。	|
| Operation	| クエリがBrazeのコホートからプロファイルを追加するか削除するかを判断するために使用されます。	|
| 別名（オプション） | 定義されている場合、クエリ内の対応する列の名前が`alias_label`として送信され、列内の各行の値が`alias_name`として送信されます。	|
| スレッド数 | 同時API呼び出しの数です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Specify the result export target" }

[トレジャーデータの手順](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget)に従ってエクスポートを設定し、ユースケースに対応させます。

#### ステップ3.3:クエリを実行する {#step-33-execute-the-query}

クエリに名前を付けて保存して実行するか、そのままクエリを実行します。クエリが正常に完了すると、クエリ結果は自動的にBrazeにエクスポートされます。

{% endtab %}
{% tab Audience Studio %}
#### ステップ3.1:アクティベーションを作成する {#step-31-create-an-activation}

新しいセグメントを作成するか、既存のセグメントを選択して、コホートとしてBrazeに同期します。セグメント内で、**Create Activation**を選択します。

#### ステップ3.2:アクティベーションの詳細を入力する {#step-32-fill-out-your-activation-details}

![トレジャーデータ統合のアクティベーションの詳細]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %})

| アクティベーション詳細設定 |	説明	|
| ----------- | ----------- |
| アクティベーション名	| アクティベーションの名前です。	|
| アクティベーションの説明| アクティベーションの簡単な説明です。	|
| 認証	| ステップ2で作成したBrazeコホート認証を選択します。	|
| コホートID	| Brazeに送信されるバックエンドのコホート識別子です。	|
| コホート名（任意）	| Brazeのセグメンテーションツール内のコホートフィルターに表示される名前です。設定されていない場合、`Cohort ID`が`Cohort Name`として使用されます。	|
| Operation	| クエリがBrazeのコホートからプロファイルを追加するか削除するかを判断するために使用されます。	|
| 別名（オプション） | 定義されている場合、クエリ内の対応する列の名前が`alias_label`として送信され、列内の各行の値が`alias_name`として送信されます。	|
| スレッド数 | 同時API呼び出しの数です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Fill out your activation details" }

#### ステップ3.3:出力マッピングを設定する {#step-33-set-up-output-mapping}

![トレジャーデータ統合のアクティベーション出力マッピング]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %})

| アクティベーション出力マッピング |	説明	|
| ----------- | ----------- |
| 属性カラム	| セグメントデータベースの列を指定し、プロファイルをBrazeコホートに同期する際の識別子としてマッピングします。	|
| String Builder| Braze統合には文字列ビルダーは必要ありません。	|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.3: Set up output mapping" }

{% alert important %}
 - `device_id`を識別子として使用する場合、**出力列名**は`device_ids`にする必要があります。
 - エイリアスを識別子として使用する場合、**出力列名**はクエリ内の対応する列の名前にする必要があり、`alias_label`として送信されます。列内の各行の値は`alias_name`として送信されます。
 - `external_id`を識別子として使用する場合、**出力列名**は`user_ids`にする必要があります。
{% endalert %}

無関係または誤った名前の列名はすべて無視されます。同期で複数の識別子を使用することもできます。

#### ステップ3.4:アクティベーションスケジュールを定義する {#step-34-define-your-activation-schedule}

希望する同期スケジュールを定義し、アクティベーションを保存します。

![トレジャーデータ統合のアクティベーションスケジュール]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### ステップ4:トレジャーデータのエクスポートからBraze セグメントを作成する {#step-4-create-a-braze-segment-from-the-treasure-data-export}

Brazeで、**セグメント**に移動し、新しいセグメントを作成して、フィルターとして**Treasure Data Cohorts**を選択します。ここから、含めるトレジャーデータコホートを選択できます。トレジャーデータのコホートセグメントを作成したら、キャンペーンまたはキャンバスを作成する際にオーディエンスフィルターとして選択できます。

![Treasure Data Integrations Hubのカタログ]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %})

## ユーザーマッチング {#user-matching}

識別されたユーザーは、`external_id`または`alias`のどちらかで照合できます。匿名ユーザーは、`device_id`で照合できます。元々匿名ユーザーとして作成された識別済みユーザーは、`device_id`では識別できず、`external_id`または`alias`で識別する必要があります。