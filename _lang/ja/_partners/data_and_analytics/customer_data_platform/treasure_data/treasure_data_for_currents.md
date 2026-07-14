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

{% alert important %}
Braze Currents Streamingコネクターはベータ版です。トレジャーデータアカウントで有効にするには、トレジャーデータサポートにお問い合わせください。パートナー側のセットアップの詳細については、トレジャーデータの[Braze Currents Import Integration](https://docs.treasuredata.com/int/braze-currents-import-integration)を参照してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| トレジャーデータアカウント | このパートナーシップを活用するには、アクティブな[トレジャーデータアカウント](https://console.treasuredata.com)が必要です。 |
| Currents | トレジャーデータにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents)を設定する必要があります。 |
| Braze Currents Streamingコネクター | トレジャーデータアカウントでBraze Currents Streamingコネクター（ベータ版）を有効にするには、トレジャーデータサポートにお問い合わせください。 |
| トレジャーデータWrite APIキー | トレジャーデータのWrite APIキーは、Brazeからのインバウンドストリームを認証します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1：トレジャーデータでコネクターを設定する {#step-1-configure-the-connector-in-treasure-data}

1. トレジャーデータコンソールで、**Connections** > **New Connection**に移動します。
2. **Braze Currents Streaming**を選択します。
3. **Authentication**で、トレジャーデータのWrite APIキーを入力します。
4. **Source Settings**で、以下を設定します。

| フィールド | 説明 |
| ----- | ----------- |
| Source Name | この接続のわかりやすい名前 |
| Datastore | **Plazma**を選択 |
| Database | イベントが保存されるトレジャーデータのデータベース |
| Table | デフォルトの宛先テーブル |
| Multiple Tables | 各Brazeイベントタイプを個別のテーブルにルーティングする場合に選択 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ソース設定" }

5. 保存後、**Unique ID**（`task_id`）をコピーします。この値は次のステップで必要になります。

### ステップ2：BrazeでカスタムCurrentsエクスポートを作成する {#step-2-create-a-custom-currents-export-in-braze}

Braze Currents UIの**Treasure Data Export**オプションはレガシーのPostback API方式を使用しており、現在は推奨されていません。代わりに**カスタムCurrentsエクスポート**を使用してください。

1. Brazeで、**パートナー連携** > **Data Export**に移動します。
2. **Create New Current** > **Custom Currents Export**を選択します。
3. 統合名とエラー通知用の連絡先メールアドレスを入力します。
4. **Credentials**で、トレジャーデータリージョンのエンドポイントURLを入力します。トレジャーデータのWrite APIキーを**Bearer Token**として入力します。

| リージョン | エンドポイントURL |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リージョン別エンドポイントURL" }

`{TASK_ID}`を[ステップ1](#step-1-configure-the-connector-in-treasure-data)でコピーしたUnique IDに置き換えてください。

5. エクスポートするイベントタイプを選択します。カスタムCurrents接続では、識別済みユーザーと`external_user_id`を持たないユーザーの両方のイベントを送信できます。トレジャーデータは両方を取り込みます。
6. **Launch Current**を選択します。

{% alert warning %}
トレジャーデータのWrite APIキーとエンドポイントURLを常に最新の状態に保ってください。エンドポイントに**5日間**以上到達できない場合、Brazeはコネクターのイベントを削除し、データは永久に失われます。
{% endalert %}

## データのクエリ {#query-your-data}

イベントが流れ始めたら、SQLでクエリできます。トレジャーデータはペイロードをフラット化するため、JSONのパースは不要です。

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
トレジャーデータの`time`フィールドは、トレジャーデータがイベントを受信して処理したタイムスタンプであり、Brazeでの元のイベント発生時刻ではありません。
{% endalert %}

**Multiple Tables**を選択した場合、各イベントタイプは個別のテーブルに格納されます（例：`users_message_email_open`や`users_behaviors_purchase`）。

データが到着していることを確認するには、Currentを起動してから数分後にカウントクエリを実行します。

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## データスキーマ {#data-schema}

トレジャーデータはネストされたJSONを最大2階層までフラット化します。

| JSONタイプ | トレジャーデータのカラムタイプ |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object（レベル1） | `field_name` |
| object（レベル2） | `parent_field_name_field_name` |
| null | 省略 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データ型マッピング" }

カラム名には小文字とアンダースコアのみが使用されます。

## 制限事項 {#limits}

| 項目 | 制限 |
| ---- | ----- |
| 最大ペイロードサイズ | リクエストあたり1&nbsp;MB |
| バッチサイズ | バッチあたり100イベント（デフォルト） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="制限事項" }

## 統合の詳細 {#integration-details}

Brazeでは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents)にリストされているすべてのデータをトレジャーデータにエクスポートできます。これには、[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)イベントおよび[顧客行動]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)イベントのすべてのプロパティが含まれます。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じです。サンプルペイロードは、[カスタムHTTPコネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。

## レガシーPostback方式からの移行 {#migrate-from-the-legacy-postback-method}

以前Brazeで**Treasure Data Export**（Postback）を使用していた場合は、以下の手順で移行してください。

1. この記事のカスタムCurrentsエクスポートのセットアップを完了します。
2. 新しいテーブルにイベントが流れていることを確認します。
3. Brazeで古いPostbackベースのCurrentを無効にします。

レガシーデータは生のJSON配列として保存されており、`JSON_PARSE`と`UNNEST`でクエリできます。ストリーミングコネクターを通じて取り込まれた新しいデータは、[データスキーマ](#data-schema)で説明されているフラットスキーマを使用します。