> クエリビルダーの使用方法について説明します。Snowflakeの Brazeデータを使用してレポートを生成できます。クエリビルダーには、すぐに使えるSQL [クエリテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)が付属しているので、すぐに始めることができます。また、独自のカスタムSQLクエリを作成して、さらに多くのインサイトを得ることもできます。

## 前提条件 {#prerequisites}

クエリビルダーを使用するには、以下の[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。

- **PIIを表示:** クエリビルダーでは、一部の顧客データに直接アクセスできます。
- **ダッシュボードレポートを表示:** この権限は、管理者以外のユーザーがダッシュボードでクエリビルダーを表示するために必要です。

## クエリビルダーの使用 {#using-the-query-builder}

### ステップ1:SQLクエリを作成する {#step-1-create-an-sql-query}

新しいクエリを作成するには、**分析** > **クエリビルダー**に移動し、**SQLクエリを作成**を選択します。

![「SQLクエリを作成」ドロップダウン内にある「クエリテンプレート」と「SQLエディター」のオプション。]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

クエリの作成にインスピレーションやヘルプが必要な場合は、**クエリテンプレート**を選択し、[既成のテンプレート]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)を選択してください。空白のクエリから始めるには、**SQLエディター**を選択します。

レポートには現在の日時が自動的に名前として付与されます。名前にカーソルを合わせて<i class="fas fa-pencil" alt="編集"></i>を選択し、SQLクエリにわかりやすい名前を付けてください。

![レポート名の例「Channel engagement for May 2025」。]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### ステップ2:クエリを作成する {#step-2-build-your-query}

クエリを作成する際に、AIの支援を受けるか、自分で作成するかを選択できます。

{% tabs local %}
{% tab BrazeAIを使用 %}
AIクエリビルダーは、OpenAIが提供する[GPT](https://openai.com/gpt-4)を活用して、クエリ用のSQLを推奨します。AIクエリビルダーでSQLを生成するには:

1. クエリビルダーでレポートを作成した後、**AIクエリビルダー**タブを選択します。
2. プロンプトを入力するか、サンプルプロンプトを選択し、**生成**を選択してプロンプトをSQLに変換します。
3. 生成されたSQLが正しいかどうか確認し、**エディターに挿入**を選択します。

![SQL AIクエリビルダー。]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### ヒント {#tips}

- 利用可能な[Snowflakeデータテーブル]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を把握しておいてください。これらのテーブルに存在しないデータを要求すると、ChatGPTが架空のテーブルを作成する可能性があります。
- この機能の[SQL記述ルール]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#custom-sql)を把握しておいてください。これらのルールに従わないと、エラーが発生します。
- AIクエリビルダーでは、1分あたり最大20個のプロンプトを送信できます。

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab 自分で作成 %}
[Snowflake構文](https://docs.snowflake.com/en/sql-reference)を使用してSQLクエリを記述します。クエリ可能なテーブルとカラムの完全なリストについては、[テーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)を参照してください。

クエリビルダー内でテーブルの詳細を表示するには:

1. **クエリビルダー**ページから、**リファレンス**パネルを開き、**利用可能なデータテーブル**を選択して、利用可能なデータテーブルとその名前を確認します。
3. <i class="fas fa-chevron-down" alt=""></i> **詳細を表示**を選択して、テーブルの説明やデータ型などのテーブルカラムに関する情報を表示します。
4. SQLにテーブル名を挿入するには、<i class="fas fa-copy" title="テーブル名をSQLエディターにコピー"></i>を選択します。

クエリを特定の期間に制限すると、結果をより迅速に生成できます。以下は、過去1時間の購入数と発生した収益を取得するクエリの例です。

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
| `CANVAS_ID` | キャンバス名 |
| `CANVAS_VARIATION_API_ID` | キャンバスバリアント名 |
| `CAMPAIGN_ID` | キャンペーン名 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ヒント" }

このクエリは、3つすべてのIDとそれらに関連する名前カラムを最大100行で取得します:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### トラブルシューティング {#troubleshooting}

クエリは以下のいずれかの理由で失敗する可能性があります:

- SQLクエリの構文エラー
- 処理タイムアウト（6分後）
    - 実行に6分以上かかるレポートはタイムアウトします。
    - レポートがタイムアウトした場合は、データをクエリする期間を制限するか、より具体的なデータセットをクエリしてみてください。
{% endtab %}
{% endtabs %}

### ステップ3:レポートを生成する {#step-3-generate-your-report}

クエリの作成が完了したら、**クエリを実行**を選択します。エラーや[レポートタイムアウト](#report-timeouts)がなければ、クエリからCSVファイルが生成されます。

CSVレポートをダウンロードするには、**エクスポート**を選択します。

![テンプレートクエリ「過去30日間のチャネルエンゲージメントと収益」の結果を表示するクエリビルダー。]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
各レポートは1日に1回のみ結果を生成できます。同じレポートを1日のうちに複数回実行しても、各レポートで同じ結果が表示されます。
{% endalert %}

## レポートのタイムアウト {#report-timeouts}

レポートの実行に6分以上かかると、タイムアウトが発生します。しばらくぶりにクエリを実行する場合は、処理に時間がかかることがあり、タイムアウトが発生する可能性が高くなります。タイムアウトが発生した場合は、レポートを再度実行してみてください。

複数回試行してもレポートがタイムアウトし続ける場合は、[サポートに連絡]({{site.baseurl}}/help/support#braze-support)してください。

## 中止理由のクエリ {#querying-abort-reasons}

任意の`USERS_MESSAGES_*_ABORT_SHARED`テーブルの`ABORT_TYPE`カラムをクエリすることで、メッセージが送信されなかった理由を分析できます。`ABORT_TYPE`フィールドには中止の具体的な理由を示す文字列値が含まれ、`ABORT_LOG`フィールドには追加の詳細情報（トリガーされたフリークエンシーキャップルールなど）が含まれます。

たとえば、過去30日間のメール中止をタイプ別にカウントするには、次のクエリを使用します。

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

`ABORT_TYPE`の値とその説明の完全なリストについては、[中止タイプ]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables#abort-types)を参照してください。

## データと結果 {#data-and-results}

すべてのクエリは過去60日間のデータを表示します。結果をエクスポートする場合、最大1,000行までしか含まれません。より大量のデータが必要なレポートについては、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)や[エクスポートAPIエンドポイント]({{site.baseurl}}/api/endpoints/export)などのツールを使用できます。

## Snowflakeクレジット {#snowflake-credits}

各企業には月あたり5 Snowflakeクレジットが利用可能で、すべてのワークスペースで共有されます。クエリを実行したり、テーブルをプレビューしたりするたびに、Snowflakeクレジットのごく一部が消費されます。

{% alert note %}
Snowflakeクレジットは機能間で共有されません。たとえば、セグメントエクステンション（SQL）とクエリビルダーのクレジットはそれぞれ独立しています。
{% endalert %}

クレジットの使用量は、SQLクエリの実行時間に相関します。実行時間が長いほど、クエリが消費するSnowflakeクレジットの割合が高くなります。実行時間は、クエリの複雑さやサイズによって異なる場合があります。複雑なクエリを頻繁に実行するほど、リソース割り当てが増加し、実行時間が短縮されます。

Braze SQLエディターでレポートの作成、編集、保存を行う際にはクレジットは消費されません。クレジットは毎月1日の午前0時（UTC）に5にリセットされます。月間のクレジット使用量は、クエリビルダーページの上部で確認できます。

![当月に使用されたクレジット量を表示するクエリビルダー。]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

クレジットのキャップに達すると、クエリを実行できなくなりますが、SQLレポートの作成、編集、保存は引き続き可能です。クエリビルダーのクレジットを追加購入したい場合は、アカウントマネージャーにお問い合わせください。