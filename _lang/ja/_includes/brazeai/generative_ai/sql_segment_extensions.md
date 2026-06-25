# SQL セグメントエクステンション {#sql-segment-extensions}

> [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) データのSnowflake SQLクエリを使用してセグメントエクステンションを生成できます。SQLでは、他のセグメンテーション機能では実現できない方法でデータ間の関係を柔軟に記述できるため、新しいセグメントのユースケースを開拓するのに役立ちます。
>
> 標準のセグメントエクステンションと同様に、SQLセグメントエクステンションでも過去2年間（730日）までのイベントをクエリできます。標準のセグメントエクステンションとは異なり、SQLセグメントエクステンションは[クレジットを消費します](#credits)。

## 前提条件 {#prerequisites}

この機能を通じて個人識別情報（PII）データにアクセスできるため、SQLセグメントクエリを実行するにはPII権限が必要です。

## セグメントエクステンションを作成する {#creating-a-segment-extension}

### ステップ 1: エディターを選ぶ {#step-1-choose-an-editor}

SQLセグメントエクステンションの作成時に選択できるSQLエディターには、SQLエディターとインクリメンタルSQLエディターの2種類があります。

- **完全リフレッシュ：**セグメントが更新されるたびに、Brazeは利用可能なすべてのデータをクエリしてセグメントを更新します。これにより、増分更新よりも多くのクレジットが使用されます。完全更新エクステンションでは、メンバーシップを毎日自動的に再生成できますが、増分更新を使用して更新することはできません。
- **増分更新：**増分更新はクエリを設定するより費用対効果の高い方法ですが、設定にはいくつかの追加[ステップ](#step-2-write-your-sql)が必要です。セグメントを構築する際にこれらの追加ステップを完了できるなら、このオプションを選択する価値があります。クエリの実行に必要なクレジットが少なくなるためです。
- **AI SQLジェネレーター：**AI SQLジェネレーターは、平易な言語でプロンプトを入力すると、それを対象セグメント向けのSQLクエリに変換します。自分でSQLを書く必要なく、すぐに始められる方法です。

{% alert tip %}
いずれかのSQLエディターで作成されたすべてのSQL Segmentsを手動で完全更新できます。
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

完全更新SQLセグメントエクステンションを作成するには:

1. **オーディエンス** > **セグメントエクステンション**に移動します。
2. **新規エクステンションを作成**を選択し、次に**完全リフレッシュ**を選択します。<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. セグメントエクステンションの名前を追加し、SQLを入力します。要件とリソースについては[ステップ 2](#step-2-write-your-sql)を参照してください。<br><br>
   ![SQLエディターがSQLセグメントエクステンションの例を示している。]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. セグメントエクステンションを保存します。

{% endtab %}
{% tab Incremental refresh %}

増分更新SQLセグメントエクステンションを作成するには:

1. **オーディエンス** > **セグメントエクステンション**に移動します。
2. **新規エクステンションを作成**を選択し、**増分更新**を選択します。<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. セグメントエクステンションの名前を追加し、SQLを入力します。要件とリソースについては、[SQLの作成](#writing-sql)セクションを参照してください。<br><br>
   ![SQLエディターが増分SQLセグメントエクステンションの例を示している。]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. 必要に応じて、**エクステンションを毎日再生成する**を選択します。<br><br>
   ![エクステンションを毎日再生成するチェックボックス。]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   選択すると、Brazeはセグメントメンバーシップを毎日自動的に更新します。つまり、毎日会社のタイムゾーンの午前0時（最大1時間遅れる可能性があります）に、Brazeはセグメントの新規ユーザーを確認し、自動的にセグメントに追加します。セグメントエクステンションが7日間使用されなかった場合、Brazeは毎日の再生成を自動的に一時停止します。未使用のセグメントエクステンションとは、CampaignやCanvasの一部ではないエクステンションです（エクステンションが「使用済み」と見なされるために、CampaignまたはCanvasがアクティブである必要はありません）。<br><br>
5. セグメントエクステンションを保存します。

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
AI SQLジェネレーターは現在、ベータ機能としてご利用いただけます。このベータトライアルへの参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

AI SQLジェネレーターはOpenAIを搭載した[GPT](https://openai.com/gpt-4)を活用して、SQL セグメント用のSQLを推奨します。

![「先月通知を受け取ったユーザー」というプロンプトを持つAI SQLジェネレーター]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

AI SQLジェネレーターを使用するには、以下の手順を実行します。

1. 完全更新または増分更新のいずれかを使用して[SQL セグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)を作成した後、**AI SQLジェネレーターを起動**を選択します。
2. プロンプトを入力し、**生成**を選択すると、プロンプトがSQLに変換されます。
3. 生成されたSQLを確認して正しいことを確認し、セグメントを保存します。

#### プロンプトの例 {#example-prompts}

- 先月にメールを受信したユーザー
- 過去1年間に購入回数が5回未満のユーザー

#### ヒント {#tips}

- 利用可能な[Snowflakeデータテーブル]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)をよく理解してください。これらのテーブルに存在しないデータを要求すると、ChatGPTが架空のテーブルを作成する可能性があります。
- この機能の[SQL記述ルール]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql)をよく理解してください。これらのルールに従わないと、エラーが発生します。たとえば、SQLコードでは`user_id`列を選択する必要があります。プロンプトの冒頭に「Users who」と入力すると役に立ちます。
- AI SQLジェネレーターでは、1分あたり最大20のプロンプトを送信できます。

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
実行に20分以上かかるSQLクエリはタイムアウトします。
{% endalert %}

エクステンションの処理が完了したら、セグメントエクステンションを使って[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment)し、この新しいセグメントをCampaignsやCanvasesでターゲットに設定できます。

### ステップ 2: SQLを記述する {#step-2-write-your-sql}

SQLクエリは、[Snowflake構文](https://docs.snowflake.com/en/sql-reference.html)を使用して記述する必要があります。クエリ可能なテーブルとカラムの全リストについては、[テーブルリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を参照してください。

{% alert important %}
クエリに使用できるテーブルにはイベントデータのみが含まれていることに注意してください。ユーザー属性をクエリする場合は、SQL セグメントを[クラシックセグメンター]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)のカスタム属性フィルターと組み合わせる必要があります。
{% endalert %}

{% tabs %}
{% tab SQL Editor %}

SQLはさらに、次のルールに従う必要があります。

- 単一のSQLステートメントを記述します。セミコロンは含めないでください。
- SQLでは、`user_id`列の1つのみを選択する必要があります。つまり、SQLには以下が含まれている必要があります。

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- イベントがゼロのユーザーをクエリすることはできません。つまり、イベントの実行回数がX回未満のユーザーに対するクエリは、次の回避策に従う必要があります。
   1. イベントがX回以上発生したユーザーを選択するクエリを記述します。
   2. セグメント内のセグメントエクステンションを参照する場合、`doesn't include`を選択すると結果が反転します。

#### その他のルール {#additional-rules}

さらに、標準的なSQLクエリは以下のルールに従う必要があります。

- `DECLARE`ステートメントは使用できません。
{% endtab %}
{% tab Incremental SQL Editor %}

すべての増分更新クエリは、クエリとスキーマの詳細という2つの部分で構成されます。

1. エディターで、目的のテーブルから`user_id`を選択するクエリを記述します。
2. エディターの上のフィールドから**Operator**、**回数**、および**期間**を選択して、スキーマの詳細を追加します。クエリでは、集計列の合計が{% raw %}`{{operator}}`および`{{number of times}}`{% endraw %}プレースホルダーで指定された特定の条件を満たすかどうかが確認されます。これは、従来のセグメントエクステンションを作成するワークフローと同様に機能します。<br><br>
   - **Operator：**イベントの発生回数が、指定した回数よりも多いか、少ないか、等しいかを示します。<br>
   ![Operatorフィールドで「より大きい」が選択されている。]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **回数：**Operatorに対してイベントを評価したい回数。<br>
   ![「5」が入力された回数。]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **期間：**イベントのインスタンスを確認する日数（1〜730日）。この期間は、現在の日を基準とした過去の日数を指します。次の例は、過去365日間にイベントを5回以上実行したユーザーのクエリを示しています。<br>
   ![期間フィールドに「365」が入力されている。]({% image_buster /assets/img_archive/sql_segments_period.png %})

次の例では、結果のセグメントには、指定した日付以降の過去30日間に`favorited`イベントを3回以上実行したユーザーが含まれます。

![SQLエディターが増分SQLセグメントエクステンションの例を示している。]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![増分SQLセグメントエクステンションのSQLプレビュー。]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
増分更新Segmentsでは、2日以上前に発生した遅延イベント（キャプチャされた時点で送信されていなかったSDKイベントなど）が考慮されます。
{% endalert %}

#### その他のルール

さらに、増分更新クエリは以下のルールに従う必要があります。

- 単一のSQLステートメントを記述します。セミコロンは含めないでください。
- インクリメンタルSQL セグメントで参照できるのは1つのイベントだけです。日付とカウントのドロップダウンは、選択したイベントに基づいています。
- SQLには次の列が必要です: `user_id`、`$start_date`、および集計関数（`COUNT`など）。これら3つのフィールドなしでSQLを保存すると、エラーになります。
- `DECLARE`ステートメントは使用できません。
{% endtab %}
{% endtabs %}

{% alert note %}
テーブル`CATALOGS_ITEMS_SHARED`を使用するSQL セグメントを作成する場合は、カタログIDを指定する必要があります。以下に例を示します。

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### ステップ 3: クエリをプレビューする {#step-3-preview-the-query}

保存する前に、クエリのプレビューを実行できます。クエリのプレビューは自動的に100行に制限され、60秒後にタイムアウトします。プレビューを実行する場合、`user_id`列の要件は適用されません。

インクリメンタルSQLセグメントエクステンションの場合、プレビューにはOperator、回数、および期間フィールドからの追加条件は含まれません。

### ステップ 4: SQLを反転させる必要があるかどうかを判断する {#step-4-determine-if-you-need-to-invert-sql}

次に、SQLを反転させる必要があるかどうかを判断します。イベントがゼロのユーザーを直接クエリすることはできませんが、**SQLを反転**を使用してこれらのユーザーをターゲットにできます。

{% alert note %}
デフォルトでは、**SQLを反転**はオンになっていません。ただし、AI SQLジェネレーターを使って否定形にする必要があるSQL文を生成する場合、ChatGPTはこの機能を自動的に有効にする出力を返す可能性があります。
{% endalert %}

たとえば、購入回数が3回未満のユーザーをターゲットにするには、まず購入回数が3回以上のユーザーを選択するクエリを記述します。次に、**SQLを反転**を選択して、購入回数が3回未満のユーザー（購入回数が0回のユーザーを含む）をターゲットにします。

{% alert important %}
特にイベントがゼロのユーザーをターゲットにする場合を除き、SQLを反転させる必要はありません。**SQLを反転**を選択した場合、その機能が本当に必要か、またセグメントが目的のオーディエンスに合致しているかを確認してください。たとえば、クエリが少なくとも1つのイベントを持つユーザーを対象とする場合、反転するとイベントがゼロのユーザーのみを対象とします。
{% endalert %}

![「過去30日間で1〜4通のメールをクリックした」という名前のセグメントエクステンション。SQLを反転するオプションが選択されている。]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## セグメントメンバーシップの更新 {#refreshing-segment-membership}

SQLを使用して作成されたセグメントエクステンションのセグメントメンバーシップを更新するには、セグメントエクステンションを開いて**更新**を選択します。

{% alert tip %}
ユーザーが頻繁に出入りすることが予想されるセグメントを作成した場合は、CampaignまたはCanvasでそのセグメントをターゲットにする前に、使用するセグメントエクステンションを手動で更新してください。
{% endalert %}

## セグメントエクステンションの管理 {#managing-your-segment-extensions}

**セグメントエクステンション**ページでは、SQLを使用して生成されたSegmentsは名前の横に<i class="fas fa-code" alt="SQLセグメントエクステンション"></i>で表示されます。

SQLセグメントエクステンションを選択すると、そのエクステンションが使用されている場所を表示したり、エクステンションをアーカイブしたり、[セグメントメンバーシップを手動で更新](#refreshing-segment-membership)したりできます。

![SQLエディターの「メッセージング使用」セクションは、SQL セグメントが使用されている箇所を示している。]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### 更新設定の指定 {#designating-refresh-settings}

{% multi_lang_include segments.md section='Refresh settings' %}

## Snowflakeクレジット {#credits}

各Brazeワークスペースには、1か月あたり5つのSnowflakeクレジットが利用可能です。さらにクレジットが必要な場合は、アカウントマネージャーにお問い合わせください。クレジットは、SQL セグメントのメンバーシップを更新、または保存して更新するたびに使用されます。SQL セグメント内でプレビューを実行したり、従来のセグメントエクステンションを保存または更新したりする場合、クレジットは使用されません。

{% alert note %}
Snowflakeクレジットは機能間で共有されません。たとえば、SQLセグメントエクステンションとクエリビルダーのクレジットは互いに独立しています。
{% endalert %}

クレジット使用量はSQLクエリの実行時間と相関しています。実行時間が長くなるほど、クエリにかかるクレジット数は多くなります。実行時間は、時間の経過に伴うクエリの複雑さとサイズによって異なる場合があります。実行するクエリが複雑で頻繁になればなるほど、リソースの割り当てが大きくなり、実行時間が短縮されます。

クレジットを節約するには、SQLセグメントエクステンションを保存する前に、クエリをプレビューして正しいことを確認してください。

クレジットは、毎月1日午前12時（UTC）に5にリセットされます。クレジット使用状況パネルで、その月のクレジット使用状況を監視できます。**セグメントエクステンション**ページから、<i class="fa-solid fa-chart-column"></i> **SQLクレジット使用状況を表示**をクリックします。

![SQLセグメントエクステンションページのSQLクレジット使用状況パネル]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

クレジットがゼロになると、次のことが起こります。

- 自動更新が設定されたSQLセグメントエクステンションは更新を停止し、これらのSegmentsのメンバーシップ、およびこれらのSegmentsをターゲットとするCampaignsやCanvasesに影響します。
- その月の残りの期間は、新しいSQLセグメントエクステンションを下書きとしてのみ保存できます。

SQL セグメントを作成したすべての会社ユーザーと会社の管理者には、クレジットの50%、80%、100%を使い切った時点で通知メールが届きます。翌月の初めにクレジットがリセットされたら、SQL Segmentsをさらに作成でき、自動更新が再開されます。

SQL セグメントクレジットの追加購入やセグメントエクステンションの追加をご希望の場合は、アカウントマネージャーにお問い合わせください。