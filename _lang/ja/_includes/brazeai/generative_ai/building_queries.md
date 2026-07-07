> クエリビルダーの使用方法について説明します。SnowflakeのBrazeデータを使用してレポートを生成できます。クエリビルダーには、すぐに使えるSQL [クエリテンプレート]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)が付属しているので、すぐに始めることができます。また、独自のカスタムSQLクエリを作成して、より多くのインサイトを得ることもできます。

## 前提条件 {#prerequisites}

クエリビルダーを使用するには、[「View PII」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)が必要です。これにより、一部の顧客データに直接アクセスできるようになります。

## クエリビルダーの使用 {#using-the-query-builder}

### ステップ 1: SQLクエリの作成 {#step-1-create-an-sql-query}

新しいクエリを作成するには、**Analytics** > **クエリビルダー**に移動し、**Create SQL Query** を選択します。

![「Create SQL Query」ドロップダウン内にある「Query Template」および「SQL Editor」オプション。]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

インスピレーションが必要な場合やクエリの作成にヘルプが必要な場合は、**Query Template** を選択し、[事前作成テンプレート]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)を選択します。空のクエリで開始するには、**SQL Editor** を選択します。

レポートには、現在の日時からなる名前が自動的に付けられます。名前の上にカーソルを合わせ、<i class="fas fa-pencil" alt="編集"></i>を選択して、SQLクエリにわかりやすい名前を付けます。

![レポート名の例「Channel engagement for May 2025」。]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### ステップ 2: クエリを作成する {#step-2-build-your-query}

クエリを作成する際に、AIのサポートを受けるか、自分で作成するかを選択できます。

{% tabs local %}
{% tab Using BrazeAI %}
AIクエリビルダーはOpenAIを搭載した[GPT](https://openai.com/gpt-4)を活用して、クエリのSQLを提案します。AIクエリビルダーでSQLを生成するには、次の手順に従います。

1. クエリビルダーでレポートを作成したら、**AI Query Builder** タブを選択します。
2. プロンプトを入力するか、サンプルプロンプトを選択し、**Generate** を選択してプロンプトをSQLに変換します。
3. 生成されたSQLが正しいかどうかを確認し、**Insert into Editor** を選択します。

![SQL AIクエリビルダー。]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### ヒント {#tips}

- 利用可能な[Snowflakeデータテーブル]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)をよく理解してください。これらのテーブルに存在しないデータを要求すると、ChatGPTが架空のテーブルを作成する可能性があります。
- この機能の[SQL記述ルール]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql)をよく理解してください。このルールに従わないと、エラーが発生します。
- AIクエリビルダーでは、1分あたり最大20個のプロンプトを送信できます。

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab On My Own %}
[Snowflake構文](https://docs.snowflake.com/en/sql-reference)を使用してSQLクエリを記述します。クエリ可能なテーブルとカラムの全リストについては、[テーブルリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を参照してください。

クエリビルダー内でテーブルの詳細を表示するには、次の手順に従います。

1. **クエリビルダー**ページから**参照**パネルを開き、**Available Data Tables** を選択すると、利用できるデータテーブルとその名前が表示されます。
3. <i class="fas fa-chevron-down" alt=""></i> **See Details** を選択して、テーブルの説明やデータタイプなどのテーブル列に関する情報を表示します。
4. テーブル名をSQLに挿入するには、<i class="fas fa-copy" title="テーブル名をSQLエディターにコピー"></i>を選択します。

クエリを特定期間に限定すると、結果をより迅速に生成できます。以下に、過去1時間の購入数と収益を取得するクエリの例を示します。

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

次のクエリは、先月のメール送信数を取得します。

`````````sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

`CANVAS_ID`、`CANVAS_VARIATION_API_ID`、`CAMPAIGN_ID`に対するクエリを実行すると、それらに関連付けられている名前列が自動的に結果テーブルに含まれます。`SELECT`クエリ自体にこれらを含める必要はありません。

| ID名 | 関連する名前列 |
| --- | --- |
| `CANVAS_ID` | キャンバス名 |
| `CANVAS_VARIATION_API_ID` | キャンバスバリアント名 |
| `CAMPAIGN_ID` | キャンペーン名 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tips" }

このクエリは、3つのすべてのIDと、それらに関連付けられている名前の列を取得します。行数の上限は100行です。

`````````sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### トラブルシューティング {#troubleshooting}

クエリは次のいずれかの理由で失敗する可能性があります。

- SQLクエリの構文エラー
- 処理タイムアウト（6分後）
    - レポートの実行が6分を超えると、タイムアウトします。
    - レポートがタイムアウトした場合は、クエリするデータの時間範囲を限定するか、より具体的なデータセットをクエリしてみてください。
{% endtab %}
{% endtabs %}

### ステップ 3: レポートの生成 {#step-3-generate-your-report}

クエリの構築が完了したら、**Run Query** を選択します。エラーや[レポートタイムアウト](#report-timeouts)がない場合、クエリからCSVファイルが生成されます。

CSVレポートをダウンロードするには、**Export** を選択します。

![テンプレートクエリ「Channel engagement and revenue for the last 30 days」の結果を表示するクエリビルダー。]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
それぞれのレポートは、1日に1回のみ結果を生成できます。1日に同じレポートを複数回実行すると、それぞれのレポートに同じ結果が表示されます。
{% endalert %}

## レポートのタイムアウト {#report-timeouts}

実行に6分以上かかるレポートはタイムアウトになります。これがしばらくぶりに実行する最初のクエリである場合、処理に時間がかかるため、タイムアウトする可能性が高くなります。タイムアウトした場合は、レポートをもう一度実行してみてください。

複数回試行してもレポートのタイムアウトが続く場合は、[サポートにお問い合わせ]({{site.baseurl}}/help/support/#braze-support)ください。

## 中止理由のクエリ {#querying-abort-reasons}

任意の `USERS_MESSAGES_*_ABORT_SHARED` テーブルの `ABORT_TYPE` 列をクエリして、メッセージが送信されなかった理由を分析できます。`ABORT_TYPE` フィールドには中止の具体的な理由を示す文字列値が含まれ、関連する `ABORT_LOG` フィールドには追加の詳細（トリガーされたフリークエンシーキャップルールなど）が含まれます。

たとえば、過去30日間のメール中止をタイプ別にカウントするには、次のようにします。

`````````sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

`ABORT_TYPE` の値とその説明の全リストについては、[中止タイプ]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/#abort-types)を参照してください。

## データと結果 {#data-and-results}

すべてのクエリは過去60日間のデータを表示します。結果をエクスポートすると、最大1,000行のみが含まれます。大量のデータを必要とするレポートの場合は、[Currents]({{site.baseurl}}/user_guide/data/braze_currents/)や[エクスポートAPIエンドポイント]({{site.baseurl}}/api/endpoints/export/)などのツールを使用できます。

## Snowflakeクレジット {#snowflake-credits}

各会社は、すべてのワークスペースで共有される月5つのSnowflakeクレジットを使用できます。Snowflakeクレジットのごく一部が、クエリを実行したりテーブルをプレビューしたりするたびに使用されます。

{% alert note %}
Snowflakeクレジットは機能間で共有されません。たとえば、SQLセグメントエクステンションとクエリビルダーのクレジットは互いに独立しています。
{% endalert %}

クレジット使用量はSQLクエリの実行時間と相関しています。実行時間が長いほど、クエリで消費されるSnowflakeクレジットの量が多くなります。実行時間は、時間の経過に伴うクエリの複雑さとサイズによって異なります。実行するクエリが複雑で頻繁になるほど、リソースの割り当てが大きくなり、実行時間が短縮されます。

BrazeのSQLエディターでレポートの作成、編集、保存を行う場合、クレジットは使用されません。クレジットは、毎月1日午前12時（UTC）にリセットされ5に戻ります。クエリビルダーページの上部で、月次クレジット使用量を監視できます。

![今月のクレジット使用量を表示するクエリビルダー。]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

クレジット上限に達すると、クエリの実行はできませんが、SQLレポートの作成、編集、および保存はできます。クエリビルダーのクレジットをさらに購入する場合は、アカウントマネージャーにお問い合わせください。