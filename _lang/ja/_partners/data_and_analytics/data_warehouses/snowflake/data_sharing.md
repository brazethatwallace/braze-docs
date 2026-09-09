---
nav_title: "データ共有"
article_title: Snowflake データ共有
page_order: 0
description: "このリファレンス記事では、Snowflake セキュアデータ共有の統合について説明します。この統合により、BrazeのエンゲージメントおよびキャンペーンデータにSnowflakeインスタンスから直接アクセスできます。"
page_type: partner
search_tag: Partner

---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake データ共有 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> Snowflakeの[セキュアデータ共有](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)を使用すると、一般的なデータプロバイダーとの関係で生じるワークフローの摩擦や遅延、障害点、不要なコストを心配することなく、BrazeのSnowflakeポータル上のデータに安全にアクセスできます。データ共有は、以下の統合または[Snowflakeリーダーアカウント]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts)を通じて設定できます。

Snowflakeデータ共有は、Brazeデータディストリビューションの一部です。データディストリビューションオプションの全体的な概要については、[データディストリビューション]({{site.baseurl}}/user_guide/data/distribution)を参照してください。

{% alert tip %}
**Snowflakeアカウントなしで Snowflakeレベルのデータにアクセスしたいですか？**<br>[Snowflakeリーダーアカウント]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts)をご確認ください。リーダーアカウントでは、Brazeがアカウントを作成してデータを共有し、ログインしてデータにアクセスするための認証情報を提供します。これにより、すべてのデータ共有と使用料金は完全にBrazeが処理します。
{% endalert %}

## データ配信のエンタイトルメント {#data-distribution-entitlements}

データ配信のエンタイトルメントにより、データ共有で使用可能なイベントタイプが決まります。Brazeはイベントを以下のカテゴリに分類しています。

| エンタイトルメント | イベントカテゴリ | 説明 | イベント用語集リファレンス |
|------------|----------------|-------------|--------------------------|
| **エンゲージメントイベント** | メッセージエンゲージメントイベント | メッセージの送信、配信、開封、クリック、バウンス、その他のメッセージングチャネルのインタラクションに関連するイベント | [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **顧客行動イベント** | メッセージエンゲージメントイベントおよび顧客行動イベント | すべてのメッセージエンゲージメントイベントに加え、購入、カスタムイベント、セッション、アトリビューション、アプリ内ユーザーアクションに関連するイベントを含みます | [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、[顧客行動およびユーザーイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **ユーザープロファイルと属性** | メッセージエンゲージメントイベント、顧客行動イベント、およびユーザープロファイルイベント | メッセージエンゲージメントイベントと顧客行動イベントに加え、ユーザープロファイルや属性の変更に関連するイベントを含みます | [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、[顧客行動およびユーザーイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)、[ユーザープロファイルイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データ配信のエンタイトルメント" }

エンタイトルメントに含まれるイベントについてご不明な点がある場合は、Brazeのアカウント担当者またはカスタマーサクセスマネージャーまでお問い合わせください。

## セキュアデータ共有について {#about-secure-data-sharing}

データ共有では、アカウント間で実際のデータがコピーまたは転送されることはありません。すべての共有は、Snowflake独自のサービスレイヤーとメタデータストアを通じて行われます。共有データはアカウントのストレージを占有せず、したがって月額データストレージ料金に影響しないため、これは重要な概念です。発生する**唯一**の料金は、共有データのクエリに使用されるコンピューティングリソース（仮想ウェアハウスなど）に対するものです。

さらに、Snowflakeの組み込みロールおよびパーミッション機能を使用することで、Brazeから共有されたデータへのアクセスは、Snowflakeアカウントおよびそのデータに対して既に設定されているアクセスコントロールを使用して制御・管理できます。自社データと同様に、アクセスを制限および監視できます。

- **インサイト取得までの時間を短縮**<br>構築に数週間かかるETLプロセスに別れを告げましょう。BrazeとSnowflakeの独自のアーキテクチャにより、すべてのカスタマーエンゲージメントおよびキャンペーンデータは、データレイクに到着した瞬間からすぐにアクセスおよびクエリが可能です。データのコピーや移動は発生しないため、最も関連性が高い最新の情報のみに基づいて顧客体験を提供できます。
- **データサイロの解消**<br>チャネルやプラットフォームを横断した顧客の包括的なビューを構築しましょう。データ共有により、Brazeのカスタマーエンゲージメントデータを他のすべてのSnowflakeデータと結合することがこれまで以上に簡単になり、信頼できる唯一の情報源でより豊富なインサイトを得ることができます。
- **エンゲージメントのパフォーマンスを確認**<br>Braze Benchmarksを使用して、カスタマーエンゲージメント戦略を最適化しましょう。BrazeとSnowflakeを活用したこのインタラクティブツールでは、チャネル、業界、デバイスプラットフォーム全体のベンチマークと自社ブランドのエンゲージメントデータを比較できます。

Snowflakeのデータ共有について詳しくは、[Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)を参照してください。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Brazeへのアクセス | データ共有を設定するには、Brazeアカウントまたはカスタマーサクセスマネージャーにお問い合わせください。 |
| Brazeワークスペースの権限 | データ共有を表示するには、[Currentsインテグレーションの表示]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。データ共有の作成、更新、削除を行うには、[Currentsインテグレーションの編集]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。 |
| Snowflakeアカウント | `admin` 権限を持つSnowflakeアカウント。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## セキュアデータシェアリングの設定 {#setting-up-secure-data-sharing}

Snowflakeの場合、データ共有は[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)と[データ消費者](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)の間で行われます。このコンテキストでは、Brazeアカウントがデータプロバイダーとなり、データシェアを作成して送信します。一方、Snowflakeアカウントはデータ消費者となり、データシェアを使用してデータベースを作成します。詳しくは、[Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers)を参照してください。

### ステップ1:Brazeからデータシェアを送信する {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### ステップ2:Snowflakeでデータベースを作成する {#step-2-create-the-database-in-snowflake}

1. 数分後、Snowflakeアカウントでインバウンドデータシェアを受信します。
2. インバウンドデータシェアを使用して、テーブルを表示およびクエリするためのデータベースを作成します。例:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. 新しいデータベースに対するクエリ権限を付与します。

{% alert warning %}
Brazeダッシュボードでシェアを削除して再作成した場合、以前に作成したデータベースを削除し、`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` を使用して再作成する必要があります。これにより、インバウンドシェアをクエリできるようになります。
同じSnowflakeアカウントにデータを共有している複数のワークスペースがある場合は、マルチワークスペース構成の管理に関するガイダンスについて、[Snowflakeデータシェアリング FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs)を参照してください。
{% endalert %}

## 利用と可視化 {#usage-and-visualization}

データ共有がプロビジョニングされた後、受信したデータ共有からデータベースを作成すると、共有されたすべてのテーブルがSnowflakeインスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリが可能になります。ただし、共有データは読み取り専用であり、クエリのみが可能で、いかなる方法でも変更や削除はできないことに注意してください。

Currentsと同様に、Snowflakeセキュアデータシェアリングを使用して以下のことが可能です。

{% multi_lang_include partners/data_sharing_use_cases.md %}

[未加工のテーブルスキーマをダウンロードする。](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
未加工のスキーマダウンロードには、ユーザープロファイル属性のビューは含まれていません。`USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`、`USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`、およびその他のユーザー属性ビューの完全なスキーマと使用方法については、[ユーザープロファイル属性]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes)を参照してください。
{% endalert %}

### ユーザーIDスキーマ {#user-id-schema}

ユーザーIDに関するBrazeとSnowflakeの命名規則の以下の違いに注意してください。

| Brazeスキーマ | Snowflakeスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されるユーザープロファイルの一意の識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーIDスキーマ" }

## 重要な情報と制限事項 {#important-information-and-limitations}

### 破壊的変更と非破壊的変更 {#breaking-versus-non-breaking-changes}

#### 非破壊的変更 {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
新しいカラムは非破壊的変更とみなされるため、Brazeでは`SELECT *`クエリを使用する代わりに、各クエリで対象のカラムを明示的にリストすることを強く推奨しています。あるいは、カラムを明示的に指定したビューを作成し、テーブルに直接クエリするのではなく、それらのビューに対してクエリを実行することもできます。
{% endalert %}

#### 破壊的変更 {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflakeリージョン {#snowflake-regions}

Brazeは現在、すべてのユーザーレベルのデータを以下のSnowflake AWSリージョンでホストしています：

 - US East-1
 - EU-Central（フランクフルト）
 - AP-Northeast-1（東京）
 - AP-Southeast-2（シドニー）
 - AP-Southeast-3（ジャカルタ）

これらのリージョン外のユーザーに対しては、AWS、Azure、またはGCPのいずれかのリージョンでSnowflakeインフラをホストしている共通の顧客にデータ共有を提供できます。

### データ保持 {#data-retention}

#### 保持ポリシー {#retention-policy}

2年以上前のデータはすべてアーカイブされ、長期ストレージに移動されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報（PII）に該当する機密フィールドは削除されます（これには`properties`などのオプションのPIIフィールドも含まれます）。アーカイブされたデータには引き続き`user_id`フィールドが含まれており、すべてのイベントデータにわたるユーザー単位の分析が可能です。

各イベントの対応する`USERS_*_SHARED`ビューで直近2年間のデータに対してクエリを実行できます。さらに、各イベントには`USERS_*_SHARED_ALL`ビューがあり、匿名化されたデータと匿名化されていないデータの両方を返すクエリを実行できます。

#### 過去データ {#historical-data}

Snowflakeにおけるイベントの過去データのアーカイブは2019年4月まで遡ります。BrazeがSnowflakeにデータを保存し始めた最初の数か月間は、製品の変更により一部のデータの外観がわずかに異なったり、一部のnull値が含まれたりする場合があります（当時、利用可能なすべてのフィールドにデータを渡していなかったためです）。2019年8月より前のデータを含む結果は、期待とわずかに異なる可能性があると想定しておくことをお勧めします。

### 一般データ保護規則（GDPR）への準拠 {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### クエリの速度、パフォーマンス、コスト {#speed-performance-cost-of-queries}

データに対して実行されるクエリの速度、パフォーマンス、コストは、データのクエリに使用するウェアハウスのサイズによって決まります。分析用にアクセスするデータ量によっては、クエリを正常に実行するためにより大きなウェアハウスサイズを使用する必要がある場合があります。Snowflakeには、最適なサイズの選び方に関する優れたリソースがあります。[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスに関する考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)をご参照ください。

{% alert tip %}
Snowflakeの設定時に参照できるクエリの例については、[サンプルクエリ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries)や[ETLイベントパイプライン設定]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup)の例をご確認ください。
{% endalert %}