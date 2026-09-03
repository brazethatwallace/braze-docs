---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "このリファレンス記事では、BrazeとのDatabricks Delta Sharing（クローズドベータ）について説明します。これにより、Brazeのエンゲージメントデータやキャンペーンデータにお使いのDatabricksアカウントからアクセスできます。"
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html)を使用すると、Brazeのライブエンゲージメントデータやキャンペーンデータをお使いのDatabricks環境に安全に共有できます。この記事では、データプロバイダーとしてのBrazeから受信者としてのDatabricksアカウントへの共有の仕組みと、共有テーブルのクエリ方法について説明します。

{% alert important %}
BrazeとのDatabricks Delta Sharingは**クローズドベータ**です。利用可能なリージョン、サポート対象リージョン、製品の動作は変更される場合があります。参加を希望される場合や、お使いのワークスペースでこの機能が有効かどうかを確認するには、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

Databricks Delta SharingはBrazeデータ配信の一部です。データ配信オプションの全体的な概要については、[データ配信]({{site.baseurl}}/user_guide/data/distribution)を参照してください。

## Delta Sharingのセットアップ {#set-up-delta-sharing}

Databricksでは、データプロバイダーとデータ受信者の間でデータ共有が行われます。Brazeアカウントは共有を作成して送信するため**データプロバイダー**であり、Databricksアカウントは共有を利用してクエリ可能なカタログを作成するため**データ受信者**です。詳細については、Databricksのドキュメント「[reading data shared using Databricks-to-Databricks Delta Sharing (for recipients)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html)」を参照してください。

### ステップ1: Brazeから共有を設定する {#step-1-configure-sharing-from-braze}

1. Brazeで、**パートナー連携** > **データ共有** > **Databricks Delta Sharing**に移動します。
2. Databricks共有識別子を入力します。
3. 完了したら、**Create Datashare**を選択します。BrazeがDatabricksアカウントに共有を送信します。

### ステップ2: Databricksでカタログを作成する {#step-2-create-a-catalog-in-databricks}

1. 数分後、Databricksアカウントでインバウンド共有を受信します。
2. インバウンド共有を使用して、テーブルを表示およびクエリするためのカタログを作成します。例:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. 適切なユーザーとグループが新しいカタログをクエリできるように権限を付与します。

{% alert warning %}
共有データはDatabricksワークスペースでは読み取り専用です。他のデータと同様にクエリできますが、共有を通じて共有テーブルの行を変更または削除することはできません。
{% endalert %}

## 使用方法と可視化 {#usage-and-visualization}

データ共有がプロビジョニングされたら、受信した共有からカタログを作成して、共有テーブルがDatabricksワークスペースに表示され、そこに保存されている他のデータと同様にクエリできるようにします。共有データは読み取り専用のままです。

Currentsと同様に、Databricks Delta Sharingを使用して以下のことができます:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Databricksで利用可能なテーブルとカラムの完全なリストについては、[Databricks生テーブルスキーマをダウンロード](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt)してテキストファイルとして確認してください。このファイルはDatabricks Delta Sharingスキーマを反映しています（例: 取り込み時刻の`DB_CREATED_AT`）。[Snowflake生テーブルスキーマ](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)や[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)とは互換性がありません。これらはSnowflakeの命名規則とフィールドを記述しています。

{% alert note %}
クローズドベータ期間中は、Databricksスキーマファイルに記載されているすべてのテーブルが共有で利用できるとは限りません。カラム名や型もSnowflakeデータ共有と異なる場合があります（例: `SF_CREATED_AT`の代わりに`DB_CREATED_AT`）。お使いのワークスペースの現在のテーブルリストが必要な場合は、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

### ユーザーIDスキーマ {#user-id-schema}

ユーザーIDに関するBrazeとDatabricksの命名規則の違いに注意してください。

| Brazeスキーマ | Databricksスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | Brazeが自動的に割り当てる一意の識別子です。 |
| `external_id` | `EXTERNAL_USER_ID` | Brazeで設定するユーザープロファイルの一意の識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーIDスキーマ" }

## 重要な情報と制限事項 {#important-information-and-limitations}

### クローズドベータの利用可能性 {#closed-beta-availability}

クローズドベータ期間中は、[Databricks生テーブルスキーマ](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt)ファイルに記載されているすべてのテーブルが共有に含まれない場合があります。共有データは、カラム名や型においてSnowflakeデータ共有と異なる場合もあります。例えば、Databricks共有では取り込み時刻に`DB_CREATED_AT`を使用しますが、Snowflake共有では`SF_CREATED_AT`を使用します。

### 破壊的変更と非破壊的変更 {#breaking-versus-non-breaking-changes}

#### 非破壊的変更 {#non-breaking-changes}

非破壊的変更はいつでも発生する可能性があり、一般的に追加機能を提供します。非破壊的変更の例:

- 新しいテーブルまたはビューの追加
- 既存のテーブルまたはビューへのカラムの追加

{% alert important %}
新しいカラムは非破壊的変更と見なされるため、Brazeでは各クエリで`SELECT *`クエリを使用する代わりに、対象のカラムを明示的にリストすることを強く推奨します。または、カラムを明示的に指定したビューを作成し、共有テーブルを直接クエリする代わりにそのビューをクエリしてください。
{% endalert %}

#### 破壊的変更 {#breaking-changes}

可能な場合、破壊的変更の前にはアナウンスと移行期間が設けられます。破壊的変更の例:

- テーブルまたはビューの削除
- 既存のテーブルまたはビューからのカラムの削除
- 既存カラムの型またはnull許容性の変更

### Databricksリージョン {#databricks-regions}

クローズドベータ期間中は、サポートされるクラウドプロバイダーとリージョンがワークスペースやロールアウトによって異なる場合があります。お使いのアカウントに適用されるオプションについては、Brazeカスタマーサクセスマネージャーにお問い合わせください。

### リテンションポリシー {#retention-policy}

クローズドベータ期間中は、標準のリテンション期間を超える過去データのバックフィルが制限される場合があります。

対応する`USERS_*_SHARED`ビューで、各イベントの直近2年間のデータに対してクエリを実行できます。

### 一般データ保護規則（GDPR）コンプライアンス {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### 共有データのクエリ: `TIME`とクエリパフォーマンス {#querying-shared-data-time-and-query-performance}

データ共有ビュー（例: `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`）のイベントデータは`TIME`フィールドでクラスタリングされています。イベントの発生時刻でフィルタリングする場合は、`TIME`を優先フィルターとして使用してください。`TIME`で行を制限するクエリは、クラスタリングがイベント時刻に基づいているため、`DB_CREATED_AT`でフィルタリングするクエリよりも一般的にパフォーマンスが高くなります。

| フィールド | 意味 |
| ----- | ------- |
| `TIME` | イベントが発生したUnixタイムスタンプです。発生時刻でフィルタリングする場合はこちらを使用してください。 |
| `DB_CREATED_AT` | 行がDatabricksに読み込まれたタイムスタンプ（取り込み時刻）です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="共有データのクエリ: TIMEとクエリパフォーマンス" }

### クエリの速度、パフォーマンス、コスト {#speed-performance-and-cost-of-queries}

データに対して実行するクエリの速度、パフォーマンス、コストは、使用するSQLウェアハウスのサイズによって異なります。アクセスするデータ量によっては、クエリを正常に完了するためにより大きなウェアハウスが必要になる場合があります。詳細については、Databricksのドキュメント「[creating and configuring a SQL warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create.html)」（クラスターサイズとスケーリングを含む）を参照してください。