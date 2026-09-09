---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "このリファレンス記事では、Braze Currentsと企業向け顧客データプラットフォームであるトレジャーデータとのパートナーシップについて説明します。トレジャーデータを使用すると、Brazeのイベントデータをトレジャーデータにストリーミングし、分析やアクティベーションに活用できます。"
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data for Currents

> [トレジャーデータ](https://www.treasuredata.com/)は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまなロケーションにルーティングする顧客データプラットフォーム（CDP）です。

Brazeとトレジャーデータの統合により、2つのシステム間の情報の流れを制御できます。Currentsを使用すると、Brazeのイベントデータをトレジャーデータにストリーミングし、グローススタック全体で活用できます。

推奨される方法は、トレジャーデータの**Braze Currents Streaming**コネクターと、Brazeの**カスタムCurrentsエクスポート**を組み合わせることです。このアプローチには以下のメリットがあります。

- Brazeからトレジャーデータへのリアルタイムイベントストリーミング
- イベントタイプごとの自動テーブルルーティング（オプション）
- JSONパースが不要なフラットでSQLクエリ可能なスキーマ

{% alert note %}
Braze Currents Streamingコネクターはリクエストに応じて利用可能です。トレジャーデータアカウントで有効にするには、トレジャーデータサポートにお問い合わせください。パートナー側の設定の詳細については、トレジャーデータの[Braze Currents Import Integration](https://docs.treasuredata.com/int/braze-currents-import-integration)を参照してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| トレジャーデータアカウント | このパートナーシップを利用するには、アクティブな[トレジャーデータアカウント](https://console.treasuredata.com)が必要です。 |
| Currents | トレジャーデータにデータをエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) が設定されている必要があります。 |
| Braze Currents Streaming コネクター | トレジャーデータサポートに連絡して、トレジャーデータアカウントで Braze Currents Streaming コネクターを有効にしてください。 |
| トレジャーデータ Write API キー | トレジャーデータの Write API キーは、Braze からのインバウンドストリームを認証します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Treasure Dataでコネクターを設定する {#step-1-configure-the-connector-in-treasure-data}

1. Treasure Dataコンソールで、**Connections** > **New Connection** に移動します。
2. **Braze Currents Streaming** を選択します。
3. **Authentication** で、Treasure Data Write APIキーを入力します。
4. **Source Settings** で、以下を設定します：

| フィールド | 説明 |
| ----- | ----------- |
| Source Name | この接続のわかりやすい名前 |
| Datastore | **Plazma** を選択 |
| Database | イベントが保存されるTreasure Dataデータベース |
| Table | デフォルトの送信先テーブル |
| Multiple Tables | 各Brazeイベントタイプを個別のテーブルにルーティングする場合に選択 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ソース設定" }

5. 保存後、**Unique ID**（`task_id`）をコピーします。この値は次のステップで必要になります。

### ステップ2：BrazeでカスタムCurrentsエクスポートを作成する {#step-2-create-a-custom-currents-export-in-braze}

Braze Currents UIの **Treasure Data Export** オプションはレガシーのPostback APIメソッドを使用しており、現在は推奨されていません。代わりに **Custom Currents Export** を使用してください。

1. Brazeで、**パートナー連携** > **Data Export** に移動します。
2. **Create New Current** > **Custom Currents Export** を選択します。
3. 連携名と、エラー通知用の連絡先メールアドレスを入力します。
4. **Credentials** で、お使いのTreasure DataリージョンのエンドポイントURLを入力します。Treasure Data Write APIキーを **Bearer Token** として入力します。

| リージョン | エンドポイントURL |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リージョン別エンドポイントURL" }

`{TASK_ID}` を[ステップ1](#step-1-configure-the-connector-in-treasure-data)でコピーしたUnique IDに置き換えてください。

5. エクスポートしたいイベントタイプを選択します。カスタムCurrents接続では、識別済みユーザーと `external_user_id` を持たないユーザーの両方のイベントを送信できます。Treasure Dataはどちらも取り込みます。
6. **Launch Current** を選択します。

{% alert warning %}
Treasure Data Write APIキーとエンドポイントURLを常に最新の状態に保ってください。エンドポイントに**5日間**以上到達できない場合、Brazeはコネクターのイベントを破棄し、データは永久に失われます。
{% endalert %}

## データのクエリ {#query-your-data}

イベントが流れ始めたら、SQLでクエリを実行します。トレジャーデータはペイロードをフラット化するため、JSONのパースは不要です。

```sql
SELECT
  id AS event_id,
  event_type,
  user_external_user_id,
  properties_campaign_name,
  properties_email_address,
  time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')
```

{% alert note %}
トレジャーデータの`time`フィールドは、トレジャーデータがイベントを受信して処理したタイムスタンプであり、Brazeでのイベント発生時刻ではありません。
{% endalert %}

**Multiple Tables** を選択した場合、各イベントタイプはそれぞれのテーブルに格納されます（例: `users_message_email_open` や `users_behaviors_purchase`）。

データが到着していることを確認するには、Currentを起動してから数分後にカウントクエリを実行します。

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## データスキーマ {#data-schema}

トレジャーデータはネストされた JSON を最大2レベルの深さまでフラット化します。

| JSON タイプ | トレジャーデータのカラムタイプ |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (レベル1) | `field_name` |
| object (レベル2) | `parent_field_name_field_name` |
| null | 省略 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データ型のマッピング" }

カラム名には小文字とアンダースコアのみが使用されます。

## 制限 {#limits}

| 項目 | 制限 |
| ---- | ----- |
| 最大ペイロードサイズ | リクエストあたり1&nbsp;MB |
| バッチサイズ | バッチあたり100イベント（デフォルト） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="制限" }

## 連携の詳細 {#integration-details}

Brazeは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents)に記載されているすべてのデータをトレジャーデータにエクスポートすることをサポートしています。これには、[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)と[顧客行動]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)の両方のイベントに含まれるすべてのプロパティが含まれます。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクタのペイロード構造と同じです。サンプルペイロードは、[カスタムHTTPコネクタのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。

## レガシーPostback方式からの移行 {#migrate-from-the-legacy-postback-method}

以前Brazeで**Treasure Data Export**（Postback）を使用していた場合は、以下の手順に従ってください。

1. この記事に記載されているカスタムCurrentsエクスポートの設定を完了します。
2. 新しいテーブルにイベントが流れていることを確認します。
3. Brazeで古いPostbackベースのCurrentを無効にします。

生のJSON配列として保存されたレガシーデータは、`JSON_PARSE`と`UNNEST`で引き続きクエリできます。ストリーミングコネクター経由で取り込まれた新しいデータは、[データスキーマ](#data-schema)で説明されているフラットスキーマを使用します。