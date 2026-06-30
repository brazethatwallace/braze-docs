---
nav_title: クエリビルダー
article_title: クエリビルダー
page_order: 4
description: "このリファレンス記事では、クエリビルダーでSnowflakeのBrazeデータを使用してレポートを作成する方法について説明します。"
tool: Reports
alias: /query_builder/
---

# クエリビルダー {#query-builder}

> クエリビルダーは、SnowflakeのBrazeデータを使用してレポートを生成します。クエリビルダーには、すぐに使い始められるビルド済みのSQL[クエリテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)が付属しています。また、独自のカスタムSQLクエリを記述して、さらに多くのインサイトを引き出すこともできます。

クエリビルダーでは一部の顧客データに直接アクセスできるため、「PIIを表示」[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持つユーザーのみがクエリビルダーにアクセスできます。

## 利用可能なデータテーブル {#available-data-tables}

クエリビルダーは、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)および[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)と同じSnowflake SQLテーブルを使用します。利用可能なテーブルとそのカラムの完全なリストについては、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。

## クエリビルダーでレポートを実行する {#running-reports-in-the-query-builder}

クエリビルダーレポートを実行するには:

1. **Analytics** > **クエリビルダー**に移動します。
2. **Create SQL Query**を選択します。クエリの作成にインスピレーションやヘルプが必要な場合は、**Query Template**を選択し、リストからテンプレートを選択します。それ以外の場合は、**SQL Editor**を選択してエディターに直接移動します。
3. レポートには現在の日時で自動的に名前が付けられます。名前にカーソルを合わせ、<i class="fas fa-pencil" alt="編集"></i>を選択して、SQLクエリにわかりやすい名前を付けます。
4. エディターでSQLクエリを記述するか、**AI Query Builder**タブから[AIのヘルプを利用](#ai-query-builder)します。独自のSQLを記述する場合は、要件とリソースについて[カスタムSQLクエリの記述](#custom-sql)を参照してください。
5. **Run Query**を選択します。
6. クエリを保存します。
7. レポートのCSVをダウンロードするには、**Export**を選択します。

![テンプレートクエリ「過去30日間のチャネルエンゲージメントと収益」の結果を表示するクエリビルダー。]({% image_buster /assets/img_archive/query_builder.png %})

各レポートの結果は1日に1回生成できます。同じレポートを1暦日に複数回実行した場合、両方のレポートに同じ結果が表示されます。

### クエリテンプレート {#query-templates}

クエリテンプレートにアクセスするには、レポートを最初に作成するときに**Create SQL Query** > **Query Template**を選択します。

利用可能なテンプレートのリストについては、[クエリテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)を参照してください。

### データの期間 {#data-timeframe}

クエリは過去60日間のデータを返します。Currentsまたは[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)を使用している場合は、最大2年間のデータをクエリできる場合があります。これは、Snowflakeでデータが保持される期間です。延長データ保持の詳細については、カスタマーサクセスマネージャーにお問い合わせください。

### クエリビルダーのタイムゾーン {#query-builder-time-zone}

SnowflakeデータベースのクエリのデフォルトタイムゾーンはUTCです。そのため、**Email Channel Engagement**ページ（会社のタイムゾーンに従います）とクエリビルダーの結果の間にデータの不一致が生じる場合があります。

クエリ結果のタイムゾーンを変換するには、以下のSQLをクエリに追加し、会社のタイムゾーンに合わせてカスタマイズしてください:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### クエリ履歴 {#query-history}

クエリビルダーの**クエリ履歴**セクションには、以前に実行したクエリが表示され、作業の追跡と再利用に役立ちます。クエリ履歴は7日間保持され、7日を超えたクエリは自動的に削除されます。

より長い期間のクエリ使用状況を監査したり、7日を超えてレコードを維持したりする必要がある場合は、有効期限が切れる前に重要なクエリ結果をエクスポートまたは保存することをお勧めします。

## AIクエリビルダーを使用してSQLを生成する {#generating-sql-with-the-ai-query-builder}

AIクエリビルダーは、OpenAIを搭載した[GPT](https://openai.com/gpt-4)を活用して、クエリ用のSQLを推奨します。

![SQL AIクエリビルダー。]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

AIクエリビルダーでSQLを生成するには:

1. クエリビルダーでレポートを作成した後、**AI Query Builder**タブを選択します。
2. プロンプトを入力するか、サンプルプロンプトを選択し、**Generate**を選択してプロンプトをSQLに変換します。
3. 生成されたSQLが正しいことを確認し、**Insert into Editor**を選択します。

### ヒント {#tips}

- [SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)で利用可能なテーブルとカラムを確認してください。これらのテーブルに存在しないデータを要求すると、ChatGPTが架空のテーブルを作成する可能性があります。
- この機能の[SQL記述ルール]({{site.baseurl}}/user_guide/analytics/reports/query_builder#custom-sql)を確認してください。これらのルールに従わないとエラーが発生します。
- AIクエリビルダーでは、1分あたり最大20件のプロンプトを送信できます。

#{% multi_lang_include brazeai/generative_ai/policy.md %}

## カスタムSQLクエリの記述 {#custom-sql}

[Snowflake構文](https://docs.snowflake.com/en/sql-reference)を使用してSQLクエリを記述します。クエリ可能なテーブルとカラムの完全なリストについては、[テーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。

クエリビルダー内でテーブルの詳細を表示するには:

1. **クエリビルダー**ページから、**Reference**パネルを開き、**Available Data Tables**を選択して、利用可能なデータテーブルとその名前を表示します。
3. <i class="fas fa-chevron-down" alt=""></i> **See Details**を選択して、テーブルの説明やデータタイプなどのテーブルカラムに関する情報を表示します。
4. SQLにテーブル名を挿入するには、<i class="fas fa-copy" title="テーブル名をSQLエディターにコピー"></i> **Copy table name to SQL editor**を選択します。

Brazeが提供するビルド済みクエリを使用するには、クエリビルダーでレポートを最初に作成するときに**Query Template**を選択します。

クエリを特定の期間に制限すると、結果をより速く生成できます。以下は、過去1時間の購入数と生成された収益を取得するクエリの例です。

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

このクエリは、過去1か月間のメール送信数を取得します:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

`CANVAS_ID`、`CANVAS_VARIATION_API_ID`、または`CAMPAIGN_ID`をクエリすると、関連する名前カラムが結果テーブルに自動的に含まれます。`SELECT`クエリ自体にそれらを含める必要はありません。

| ID名 | 関連する名前カラム |
| --- | --- |
| `CANVAS_ID` | Canvas名 |
| `CANVAS_VARIATION_API_ID` | Canvasバリアント名 |
| `CAMPAIGN_ID` | Campaign名 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムSQLクエリの記述" }

このクエリは、3つのIDすべてとそれに関連する名前カラムを最大100行で取得します:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Campaignバリアント名を自動入力する {#automatically-populate-the-campaign-variant-name}

Campaignバリアント名を自動入力するには、次の例のようにクエリにカラム名`MESSAGE_VARIATION_API_ID`を含めます:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### トラブルシューティング {#troubleshooting}

クエリは以下のいずれかの理由で失敗する場合があります:

- SQLクエリの構文エラー
- 処理タイムアウト（6分後）
    - 実行に6分以上かかるレポートはタイムアウトします。
    - レポートがタイムアウトした場合は、データをクエリする期間を制限するか、より具体的なデータセットをクエリしてみてください。

## 変数の使用 {#using-variables}

変数を使用すると、SQLで事前定義された変数タイプを使用して、値を手動でコピーすることなく参照できます。たとえば、CampaignのIDをSQLエディターに手動でコピーする代わりに、{% raw %}`{{campaign.${My campaign}}}`{% endraw %}を使用して、**Variables**タブのドロップダウンからCampaignを直接選択できます。

変数を作成すると、クエリビルダーレポートの**Variables**タブに表示されます。SQL変数を使用する利点は次のとおりです:

- Campaign変数を作成してレポート作成時にリストから選択することで、Campaign IDを貼り付ける代わりに時間を節約できます。
- 変数を追加して値を入れ替えることで、将来わずかに異なるユースケース（異なるカスタムイベントなど）でレポートを再利用できます。
- 各レポートに必要な編集量を減らすことで、SQLの編集時のユーザーエラーを削減できます。SQLに慣れているチームメイトがレポートを作成し、技術的な知識が少ないチームメイトがそれを使用できます。

### ガイドライン {#guidelines}

変数は次のLiquid構文に従う必要があります: {% raw %}`{{ type.${name}}}`{% endraw %}。ここで、`type`は受け入れられるタイプのいずれかであり、`name`は任意の名前を選択できます。これらの変数のラベルはデフォルトで変数名になります。

デフォルトでは、すべての変数は必須です（変数の値が選択されないとレポートは実行されません）。ただし、日付範囲は値が指定されない場合、デフォルトで過去30日間になります。

### 変数タイプ {#variable-types}

以下の変数タイプが受け入れられます:

- [数値](#number)
- [日付範囲](#date-range)
- [メッセージング](#messaging)
- [製品](#products)
- [カスタムイベント](#custom-events)
- [カスタムイベントプロパティ](#custom-event-properties)
- [ワークスペース](#workspace)
- [カタログ](#catalogs)
- [カタログフィールド](#catalog-fields)
- [オプション](#options)
- [Segments](#segments)
- [文字列](#string)
- [タグ](#tags)

#### 数値 {#number}

- **置換値:** 指定された値（`5.5`など）
- **使用例:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### 日付範囲 {#date-range}

`start_date`と`end_date`の両方を使用する場合、日付範囲として使用できるように同じ名前にする必要があります。

##### 値の例 {#example-values}

日付範囲タイプは、相対、開始日、終了日、または日付範囲にすることができます。

`start_date`と`end_date`の両方が同じ名前で使用されている場合、4つのタイプすべてが表示されます。1つだけ使用されている場合は、関連するタイプのみが表示されます。

| 日付範囲タイプ | 説明 | 必要な値 |
| --- | --- | --- |
| 相対 | 過去X日間を指定します | `start_date`が必要 |
| 開始日 | 開始日を指定します | `start_date`が必要 |
| 終了日 | 終了日を指定します | `end_date`が必要 |
| 日付範囲 | 開始日と終了日の両方を指定します | `start_date`と`end_date`の両方が必要 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="値の例" }

- **置換値:** `start_date`と`end_date`を、UTCで指定された日付のUnixタイムスタンプ（秒単位）に置き換えます（`1696517353`など）。
- **使用例:** 相対、開始日、終了日、日付範囲のすべての変数について:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - 日付範囲が不要な場合は、`start_date`または`end_date`のいずれかを使用できます。

#### メッセージング {#messaging}

すべてのメッセージング変数は、1つのグループ内で状態を関連付ける場合、同じ識別子を共有する必要があります。

##### Canvas

1つのCanvasを選択する場合に使用します。Campaignと同じ名前を共有すると、**Variables**タブ内にCanvasまたはCampaignのいずれかを選択するラジオボタンが表示されます。

- **置換値:** Canvas BSON ID
- **使用例:** {% raw %}`canvas_id = '{{canvas.${some name}}}'`{% endraw %}

##### Canvases

複数のCanvasesを選択する場合に使用します。Campaignと同じ名前を共有すると、**Variables**タブ内にCanvasまたはCampaignのいずれかを選択するラジオボタンが表示されます。

- **置換値:** Canvases BSON ID
- **使用例:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign

1つのCampaignを選択する場合に使用します。Canvasと同じ名前を共有すると、**Variables**タブ内にCanvasまたはCampaignのいずれかを選択するラジオボタンが表示されます。

- **置換値:** Campaign BSON ID
- **使用例:** {% raw %}`campaign_id = '{{campaign.${some name}}}'`{% endraw %}

##### Campaigns

複数のCampaignsを選択する場合に使用します。Canvasと同じ名前を共有すると、**Variables**タブ内にCanvasまたはCampaignのいずれかを選択するラジオボタンが表示されます。

- **置換値:** Campaigns BSON ID
- **使用例:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Campaignバリアント {#campaign-variants}

選択したCampaignに属するCampaignバリアントを選択する場合に使用します。CampaignまたはCampaigns変数と組み合わせて使用する必要があります。

- **置換値:** CampaignバリアントAPI ID（カンマ区切りの文字列、`api-id1, api-id2`など）。
- **使用例:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Canvasバリアント {#canvas-variants}

選択したCanvasに属するCanvasバリアントを選択する場合に使用します。CanvasまたはCanvases変数と組み合わせて使用する必要があります。

- **置換値:** CanvasバリアントAPI ID（カンマ区切りの文字列、`api-id1, api-id2`など）。
- **使用例:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### キャンバスステップ {#canvas-step}

選択したCanvasに属するキャンバスステップを選択する場合に使用します。Canvas変数と組み合わせて使用する必要があります。

- **置換値:** キャンバスステップAPI ID
- **使用例:** {% raw %}`canvas_step_api_id = '{{canvas_step.${some name}}}'`{% endraw %}

##### キャンバスステップ（複数） {#canvas-steps}

選択したCanvasesに属するキャンバスステップを選択する場合に使用します。CanvasまたはCanvases変数と組み合わせて使用する必要があります。

- **置換値:** キャンバスステップAPI ID
- **使用例:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}