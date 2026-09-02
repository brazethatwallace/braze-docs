---
nav_title: Decisioning Studioデータの同期
article_title: "BrazeAI Decisioning Studioデータの同期"
description: "Cloud Data Ingestionを使用して、データウェアハウスのテーブルをBrazeAI Decisioning Studioに同期する方法について説明します。"
page_order: 6.5
page_type: reference
toc_headers: h2
---

# BrazeAI Decisioning Studioデータの同期 {#sync-brazeai-decisioning-studio-data}

> このページでは、Cloud Data Ingestion（CDI）を使用して、データウェアハウスからBrazeAI Decisioning Studio™に直接データを同期する方法について説明します。

CDIのDecisioning Studio宛先を使用すると、CDIはデータウェアハウスのデータをBrazeAI Decisioning Studioに直接同期することもできます。これらの同期からのデータはDecisioning Studioでアクティベーションに利用できますが、ユーザープロファイルやBrazeワークスペースは変更されません。

{% alert important %}
この機能は早期アクセス段階です。アクセスするには、カスタマーサクセスマネージャーまたはアカウントマネージャーにお問い合わせください。
{% endalert %}

## 仕組み {#how-it-works}

同期を作成する際、宛先としてDecisioning Studioを選択し、同期したいデータを返すSQLクエリを記述します。CDIは設定したスケジュールでそのクエリを実行し、結果をDecisioning Studioアセットとして配信します。各同期は1つのアセットにマッピングされるため、同じアセットに複数の同期を紐付けることはできません。

Braze Data Platformへの同期とは異なり、Decisioning Studioの同期ではデータをユーザープロファイル、イベント、またはカタログにマッピングしません。

Decisioning Studioにデータを利用可能にするその他の方法については、[データの接続]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources)を参照してください。

## 前提条件 {#prerequisites}

- BrazeおよびBrazeAI Decisioning Studioへのアクセス。
- アクティブなCloud Data Ingestionデータウェアハウスソース。まだ設定していない場合は、[データウェアハウス連携]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)を参照してください。
- 同期したいテーブルまたはビュー。
- プライマリキーとして使用するテーブル内のカラム（1つまたは複数）、およびCDIが増分同期に使用できるタイムスタンプカラム。

## Decisioning Studio同期の作成 {#create-a-decisioning-studio-sync}

### ステップ1:同期を作成し、宛先を選択する {#step-1-create-the-sync-and-select-the-destination}

1. **Data Settings** > **Cloud Data Ingestion** > **Syncs** に移動します。
2. **Create data sync** を選択します。
3. **Integration Name** を入力し、**Data sources** でソースを選択します。
4. **Destination** で、**Data destination** を **BrazeAI Decisioning Studio™** に設定します。
5. **Data category** で、テーブルに最も適した **Decisioning Studio data** タイプを選択します。**ユーザープロファイル**、**Message engagement events**、**Conversion events**、または **Other** から選択してください。これはDecisioning Studio用にデータにタグ付けするもので、CDIの行処理方法は変わりません。

### ステップ2:SQLクエリを記述する {#step-2-write-your-sql-query}

**Data definition** ステップで、同期したいテーブルまたはビューからデータを返すSQLクエリを記述します。クエリの結果が同期のスキーマになります。

Source Explorerを使用して利用可能なテーブルやビューを参照したり、AI SQLジェネレーターを使用してクエリの作成を支援してもらうことができます。

CDIは増分同期と変更トラッキングに`UPDATED_AT`を使用するため、クエリは`UPDATED_AT`カラムを返す必要があります。各同期実行時に、CDIは`UPDATED_AT`が最後に同期された値より後の行のみを同期します。特定したタイムスタンプカラムの名前がまだ`UPDATED_AT`でない場合は、クエリ内でエイリアスを設定できます。

```sql
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table
```

`UPDATED_AT`が増分同期をどのように制御するか（過去に戻した場合の動作を含む）の詳細については、[UPDATED_ATカラムの理解]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#understanding-the-updated_at-column)を参照してください。

{% alert note %}
`JOIN`句を含む、単一ステートメントの読み取り専用クエリのみがサポートされています。CDIは読み取り専用クエリを実行し、基盤となるテーブルを変更しません。
{% endalert %}

### ステップ3:クエリをプレビューして検証する {#step-3-preview-and-validate-your-query}

**Preview and validate** を選択してクエリを実行します。**Query preview (first 10 rows)** セクションに、ソースから返された最初の10行と各カラムの検出されたデータ型が表示されるため、続行する前にデータが正しいことを確認できます。

### ステップ4:プライマリキーを選択する {#step-4-select-a-primary-key}

すべてのDecisioning Studio同期には、各行を一意に識別する1つまたは複数のカラムであるプライマリキーまたは複合キーが必要です。検証が成功したら、**Primary key** ドロップダウンを開き、プライマリキーとして使用するカラムを選択します。複数のカラムを選択すると複合キーが形成されます。

{% alert tip %}
適切なプライマリキーは、すべての行で一意であり、空でなく、同期実行間で安定しています。`UUID()`や`CURRENT_TIMESTAMP`など、クエリ実行時に生成される値は、行の重複や欠落を引き起こす可能性があるため避けてください。
{% endalert %}

### ステップ5:通知とスケジュールを設定し、同期を作成する {#step-5-set-notifications-schedule-and-create-the-sync}

1. **Notifications** ステップで、同期エラー通知を受け取る **Contact Email(s)** を1つ以上入力します。**Row Error** および **Sync success** 通知をオンにすることもできます。
2. **Schedule** ステップで、**Recurring sync** をオンにすると、スケジュールに従って同期が自動的に実行されます。**Recurring sync** をオフにすると、ダッシュボードから手動で、または[同期のトリガー]({{site.baseurl}}/api/endpoints/cdi/post_job_sync)エンドポイントを通じてトリガーした場合にのみ同期が実行されます。
3. **Summary** を確認し、同期を作成します。

## 同期の編集 {#editing-a-sync}

既存の同期を編集する場合、SQLクエリの変更には保存前に再検証が必要です。プライマリキーと複合キーは変更できず、引き続き返される必要があります。

有効な変更は次回の同期実行時に反映されます。

## スキーマ変更の処理 {#handling-schema-changes}

CDIはソーススキーマの変更を追加的に処理します。同期実行のたびに、CDIはソーススキーマを既存のDecisioning Studioアセットと比較し、既存のカラムを保持しながら新しいカラムを追加します。

| ソーステーブルの変更 | 同期の動作 |
|---|---|
| 新しいカラムが追加された | CDIはDecisioning Studioアセットにカラムを追加します。そのカラムが存在する前に配信された行は、そのカラムに`null`が表示されます。 |
| カラムが削除された | CDIはそのカラムの更新を停止しますが、カラムと既存のデータはアセットに残ります。他のカラムは引き続き同期されます。 |
| カラムの名前が変更された | 削除されたカラムと新しいカラムとして扱われます。元のカラムはアセットに残り、新しいカラムが追加されます。 |
| カラムのデータ型が変更された | CDIは可能な場合に値を変換します。変換できない行は、同期の実行詳細で行エラーとしてレポートされます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="スキーマ変更の処理" }

CDIがスキーマ変更を検出すると、同期の実行詳細と同期編集ページに表示され、通知先にメールアラートが送信されます。配信するカラムを変更するには、SQLクエリを更新して再検証してください。