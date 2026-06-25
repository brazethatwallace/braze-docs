---
nav_title: "データ共有"
article_title: Snowflake データ共有
page_order: 0
description: "このリファレンス記事では、Snowflake セキュアデータ共有の統合について説明します。この統合により、BrazeのエンゲージメントおよびCampaignデータにSnowflakeインスタンスから直接アクセスできます。"
page_type: partner
search_tag: Partner

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake データ共有 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> Snowflakeの[セキュアデータ共有](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)を使用すると、一般的なデータプロバイダーとの関係で生じるワークフローの摩擦や遅延、障害点、不要なコストを心配することなく、BrazeのSnowflakeポータル上のデータに安全にアクセスできます。データ共有は、以下の統合または[Snowflakeリーダーアカウント]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)を通じて設定できます。

Snowflakeデータ共有は、Brazeデータディストリビューションの一部です。データディストリビューションオプションの全体的な概要については、[データディストリビューション]({{site.baseurl}}/user_guide/data/distribution/)を参照してください。

{% alert tip %}
**Snowflakeアカウントなしで Snowflakeレベルのデータにアクセスしたいですか？**<br>[Snowflakeリーダーアカウント]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)をご確認ください。リーダーアカウントでは、Brazeがアカウントを作成してデータを共有し、ログインしてデータにアクセスするための認証情報を提供します。これにより、すべてのデータ共有と使用料金は完全にBrazeが処理します。
{% endalert %}

## セキュアデータ共有について {#about-secure-data-sharing}

データ共有では、アカウント間で実際のデータがコピーまたは転送されることはありません。すべての共有は、Snowflake独自のサービスレイヤーとメタデータストアを通じて行われます。これは重要な概念です。共有データはアカウントのストレージを消費しないため、月額データストレージ料金に影響しません。発生する**唯一の**料金は、共有データのクエリに使用されるコンピューティングリソース（仮想ウェアハウスなど）の料金です。

さらに、Snowflakeの組み込みロールと権限機能を使用することで、Brazeから共有されたデータへのアクセスは、Snowflakeアカウントおよびそのデータに対して既に設定されているアクセス制御を使用して管理・統制できます。アクセスは、自社データと同じ方法で制限および監視できます。

- **インサイトまでの時間を短縮**<br>構築に数週間かかるETLプロセスに別れを告げましょう。BrazeとSnowflakeの独自のアーキテクチャにより、すべてのカスタマーエンゲージメントおよびCampaignデータは、データレイクに到着した瞬間からすぐにアクセスおよびクエリが可能です。データのコピーや移動は行われないため、最も関連性が高く最新の情報のみに基づいてカスタマーエクスペリエンスを提供できます。
- **データのサイロ化を解消**<br>チャネルやプラットフォーム全体で顧客の全体像を構築できます。データ共有により、Brazeのカスタマーエンゲージメントデータと他のすべてのSnowflakeデータの結合がこれまで以上に簡単になり、単一の信頼できる情報源からより豊富なインサイトを得ることができます。
- **エンゲージメントの比較評価**<br>Brazeベンチマークを使用してカスタマーエンゲージメント戦略を最適化しましょう。BrazeとSnowflakeを活用したこのインタラクティブツールにより、チャネル、業界、デバイスプラットフォーム全体のベンチマークとブランドのエンゲージメントデータを比較できます。

Snowflakeのデータ共有の詳細については、[セキュアデータ共有の概要](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)を参照してください。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Brazeへのアクセス | データ共有を設定するには、Brazeアカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。 |
| Snowflakeアカウント | `admin` 権限を持つSnowflakeアカウント。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## セキュアデータ共有の設定 {#setting-up-secure-data-sharing}

Snowflakeでは、データ共有は[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)と[データコンシューマー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)の間で行われます。このコンテキストでは、Brazeアカウントがデータシェアを作成して送信するデータプロバイダーであり、Snowflakeアカウントがデータシェアを使用してデータベースを作成するデータコンシューマーです。詳細については、[Snowflake: 共有データの利用](https://docs.snowflake.com/en/user-guide/data-share-consumers)を参照してください。

### ステップ1: Brazeからデータシェアを送信する {#step-1-send-the-datashare-from-braze}

1. Brazeで、**Partner Integrations** > **Data Sharing**に移動します。
2. Snowflakeアカウントの詳細とロケーターを入力します。アカウントロケーターを取得するには、送信先アカウントで `SELECT CURRENT_ACCOUNT()` を実行します。
3. CRRシェアを使用している場合は、クラウドプロバイダーとリージョンを指定します。
4. 完了したら、**Create Datashare**を選択します。これにより、データシェアがSnowflakeアカウントに送信されます。

### ステップ2: Snowflakeでデータベースを作成する {#step-2-create-the-database-in-snowflake}

1. 数分後、Snowflakeアカウントでインバウンドデータシェアを受信します。
2. インバウンドデータシェアを使用して、テーブルを表示およびクエリするためのデータベースを作成します。例:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. 新しいデータベースをクエリするための権限を付与します。

{% alert warning %}
Brazeダッシュボードでシェアを削除して再作成した場合は、以前に作成したデータベースを削除し、`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` を使用して再作成する必要があります。
複数のワークスペースが同じSnowflakeアカウントにデータを共有している場合は、マルチワークスペース設定の管理に関するガイダンスについて[Snowflakeデータ共有FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/)を参照してください。
{% endalert %}

## 使用方法と可視化 {#usage-and-visualization}

データシェアがプロビジョニングされたら、受信データシェアからデータベースを作成します。共有されたすべてのテーブルがSnowflakeインスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリ可能になります。ただし、共有データは読み取り専用であり、クエリのみ可能で、変更や削除はできません。

Currentsと同様に、Snowflakeセキュアデータ共有を使用して以下のことができます:

- 複雑なレポートの作成
- アトリビューションモデリングの実行
- 社内でのセキュアな共有
- 生のイベントまたはユーザーデータをCRM（Salesforceなど）にマッピング
- その他

[生のテーブルスキーマをダウンロードできます。](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

### ユーザーIDスキーマ {#user-id-schema}

ユーザーIDに関するBrazeとSnowflakeの命名規則の違いに注意してください。

| Brazeスキーマ | Snowflakeスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられるユニーク識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客が設定するユーザープロファイルのユニーク識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーIDスキーマ" }

## 重要な情報と制限事項 {#important-information-and-limitations}

### 破壊的変更と非破壊的変更 {#breaking-versus-non-breaking-changes}

#### 非破壊的変更 {#non-breaking-changes}

非破壊的変更はいつでも発生する可能性があり、通常は追加機能を提供します。非破壊的変更の例:
- 新しいテーブルまたはビューの追加
- 既存のテーブルまたはビューへのカラムの追加

{% alert important %}
新しいカラムは非破壊的変更と見なされるため、Brazeでは各クエリで `SELECT *` クエリを使用する代わりに、対象のカラムを明示的にリストすることを強く推奨します。または、カラムを明示的に指定するビューを作成し、テーブルを直接クエリする代わりにそのビューをクエリすることもできます。
{% endalert %}

#### 破壊的変更 {#breaking-changes}

可能な場合、破壊的変更の前にアナウンスと移行期間が設けられます。破壊的変更の例:
- テーブルまたはビューの削除
- 既存のテーブルまたはビューからのカラムの削除
- 既存カラムの型またはnull許容性の変更

### Snowflakeリージョン {#snowflake-regions}

Brazeは現在、すべてのユーザーレベルデータを以下のSnowflake AWSリージョンでホストしています:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Northeast-1 (Tokyo)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)

これらのリージョン外のユーザーに対しては、Brazeは任意のAWS、Azure、またはGCPリージョンでSnowflakeインフラをホストしている共同顧客にデータ共有を提供できます。

### データ保持 {#data-retention}

#### 保持ポリシー {#retention-policy}

2年以上前のデータはアーカイブされ、長期ストレージに移動されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報（PII）の機密フィールドは削除されます（これには `properties` などのオプションのPIIフィールドも含まれます）。アーカイブされたデータには引き続き `user_id` フィールドが含まれており、すべてのイベントデータにわたるユーザーごとの分析が可能です。

各イベントの直近2年間のデータは、対応する `USERS_*_SHARED` ビューでクエリできます。さらに、各イベントには `USERS_*_SHARED_ALL` ビューがあり、匿名化されたデータと匿名化されていないデータの両方を返すクエリが可能です。

#### 過去のデータ {#historical-data}

Snowflakeの過去のイベントデータのアーカイブは2019年4月まで遡ります。BrazeがSnowflakeにデータを保存し始めた最初の数か月間は、製品の変更が行われたため、一部のデータが若干異なって見えたり、一部のnull値が含まれている場合があります（当時はすべての利用可能なフィールドにデータを渡していなかったため）。2019年8月以前のデータを含む結果は、期待と若干異なる可能性があることを前提としてください。

### 一般データ保護規則（GDPR）への準拠 {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### クエリの速度、パフォーマンス、コスト {#speed-performance-cost-of-queries}

データに対して実行されるクエリの速度、パフォーマンス、コストは、データのクエリに使用するウェアハウスのサイズによって決まります。場合によっては、分析でアクセスするデータ量に応じて、クエリを正常に実行するためにより大きなウェアハウスサイズを使用する必要があることがあります。Snowflakeには、最適なサイズの決定方法に関する優れたリソースがあります。[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスに関する考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)を参照してください。

{% alert tip %}
Snowflakeの設定時に参照できるクエリの例については、[サンプルクエリ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries/)および[ETLイベントパイプラインの設定]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup/)の例をご確認ください。
{% endalert %}