---
nav_title: Snowflakeデータ共有
hidden: true
---

# Snowflakeデータ共有インテグレーション {#snowflake-data-sharing-integration}

> Snowflake Data Shareがインテグレーション方法として使用される場合、Brazeは顧客に代わってSnowflakeインスタンスに共有をプロビジョニングします。この共有には、すべてのメッセージエンゲージメントおよびユーザー行動イベントが自動的に含まれます。

共有は、顧客がSnowflakeデータ共有エンタイトルメントを購入した後、顧客ごとにプロビジョニングされます。顧客がデータ共有をリクエストすると、Brazeは顧客のワークスペースに共有を追加し、顧客はセルフサービスUIを使用して関連するパートナーのSnowflakeアカウントデータを追加できます。

![]({% image_buster /assets/img/snowflake.png %})

共有がプロビジョニングされると、すべてのデータは受信データ共有としてSnowflakeインスタンス内からすぐにアクセスできるようになります。

![]({% image_buster /assets/img/snowflake2.png %})

Snowflakeインスタンス内では、リージョンごとに1つの共有が表示されます。各テーブルには `app_group_id` という列があり、これは実質的にBrazeのテナントキーです。新しい顧客が同じリージョン内の共有に追加されると、既存のテーブル内で異なる `app_group_ids` として表示されます。

{% alert important %}
Brazeは現在、すべてのユーザーレベルのデータをSnowflake AWS US East-1およびEU-Central（フランクフルト）リージョンでホストしています。Brazeはクロスリージョンでの共有が可能ですが、`US-EAST-1` および/または `EU-CENTRAL-1` と共有するのが顧客にとって最もコスト効率が高くなります。
{% endalert %}

{% alert tip %}
[未加工のテーブルスキーマ](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)をダウンロードするか、Snowflakeマーケットプレイスで入手可能な[サンプルイベントデータ](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset)セットを使用して、共有されるイベントに慣れることができます。
{% endalert %}

## 重複イベントの処理 {#handling-duplicate-events}

重複は想定されますが、すべてのイベントにはID列というユニークな識別子があります。重複は `select distinct(id)` を実行することで除去できます。

## 破壊的な変更と非破壊的な変更 {#breaking-versus-non-breaking-changes}

### 非破壊的な変更 {#non-breaking-changes}

非破壊的な変更はいつでも発生する可能性があり、一般的に追加の機能を提供します。非破壊的な変更の例には次のものがあります。
- 新しいテーブルまたはビューを追加する
- 既存のテーブルやビューに列を追加する

{% alert important %}
新しい列の追加は非破壊的な変更と見なされるため、Brazeでは `SELECT *` クエリを使用する代わりに、各クエリで関心のある列を明示的に列挙することを強くお勧めします。または、列に明示的に名前を付けるビューを作成してから、テーブルではなくそれらのビューを直接クエリすることもできます。
{% endalert %}

### 破壊的な変更 {#breaking-changes}

可能な場合には、破壊的な変更の前に通知を行い、移行期間を設けます。破壊的な変更の例には次のものがあります。
- テーブルまたはビューを削除する
- 既存のテーブルやビューから列を削除する
- 既存の列のタイプまたはNULL許容性を変更する

## SNAPSHOTSテーブルとCHANGELOGSテーブルが更新されるタイミング {#when-snapshots-and-changelogs-tables-are-updated}

SNAPSHOTSテーブルとCHANGELOGSテーブルは、CampaignとCanvasの変更を追跡します。これらのテーブルがいつ更新されるかを理解することは、最新のメッセージバリエーションやCanvas設定をクエリする際に重要です。

### CHANGELOGS_CAMPAIGN_SHARED

以下の場合、`CHANGELOGS_CAMPAIGN_SHARED` に行が追加されます。
- Campaignが起動された場合、または
- 以下のスナップショット可能なフィールドのいずれかが変更された場合：
  - 名前
  - アクション（メッセージ内容の変更を含む）
  - コンバージョン動作

{% alert important %}
起動後の下書きを保存または更新しても、更新は自動的にトリガーされません。更新がトリガーされるのは、Campaignを起動した場合、または起動後の下書きの変更をアクティブなCampaignに適用した場合のみです。
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` は `CHANGELOGS_CAMPAIGN_SHARED` から派生したものです。このテーブルは、`CHANGELOGS_CAMPAIGN_SHARED` からアクション列を抽出し、個々のメッセージバリエーションレコードにフラット化します。`CHANGELOGS_CAMPAIGN_SHARED` が更新されると、それに応じて更新されます。

### CHANGELOGS_CANVAS_SHARED

以下の場合、`CHANGELOGS_CANVAS_SHARED` に行が追加されます。
- Canvasが起動された場合、または
- 以下のスナップショット可能なフィールドのいずれかが変更された場合：
  - 名前
  - コンバージョン動作
  - バリエーション（パーセンテージ、最初のステップの割り当て、バリエーション名）

{% alert important %}
起動後の下書きを保存または更新しても、更新は自動的にトリガーされません。更新がトリガーされるのは、Canvasを起動した場合、または起動後の下書きの変更をアクティブなCanvasに適用した場合のみです。
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` は `CHANGELOGS_CANVAS_SHARED` から派生したものです。このテーブルは、`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` と同じ抽出パターンを使用し、`CHANGELOGS_CANVAS_SHARED` が更新されると、それに応じて更新されます。

### SNAPSHOTS_CANVAS_STEP_SHARED

以下の場合、`SNAPSHOTS_CANVAS_STEP_SHARED` に行が追加されます。
- Canvasが起動された場合、または
- アクティブなCanvasが更新された場合（起動後の下書きが適用された場合）、または
- 以下のスナップショット可能なフィールドのいずれかが変更された場合：
  - 名前
  - アクション（メッセージバリエーション内でのメッセージ内容の変更を含む）

{% alert important %}
起動後の下書きを保存しても、更新は自動的にトリガーされません。更新がトリガーされるのは、Canvasを起動した場合、または起動後の下書きの変更をアクティブなCanvasに適用した場合のみです。
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

以下の場合、`SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` に行が追加されます。
- Canvasが起動された場合、または
- アクティブなCanvasが更新された場合（起動後の下書きが適用された場合）、または
- 以下のスナップショット可能なフィールドのいずれかが変更された場合：
  - 名前

{% alert important %}
起動後の下書きを保存しても、更新は自動的にトリガーされません。更新がトリガーされるのは、Canvasを起動した場合、または起動後の下書きの変更をアクティブなCanvasに適用した場合のみです。
{% endalert %}

## 一般データ保護規則（GDPR）への準拠 {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}