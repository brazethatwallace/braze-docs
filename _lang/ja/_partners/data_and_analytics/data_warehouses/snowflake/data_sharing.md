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

データ配信のエンタイトルメントにより、データ共有で利用できるイベントタイプが決まります。Brazeはイベントを以下のカテゴリに分類しています。

| エンタイトルメント | イベントカテゴリ | 説明 | イベント用語集リファレンス |
|------------|----------------|-------------|--------------------------|
| **エンゲージメントイベント** | メッセージエンゲージメントイベント | メッセージの送信、配信、開封、クリック、バウンス、その他のメッセージングチャネルのインタラクションに関連するイベント | [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **顧客行動イベント** | メッセージエンゲージメントイベントおよび顧客行動イベント | すべてのメッセージエンゲージメントイベントに加え、購入、カスタムイベント、セッション、アトリビューション、アプリ内ユーザーアクションに関連するイベントを含みます | [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、[顧客行動とユーザーイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **ユーザープロファイルと属性** | メッセージエンゲージメントイベント、顧客行動イベント、およびユーザープロファイルイベント | メッセージエンゲージメントイベントと顧客行動イベントに加え、ユーザープロファイルや属性の変更に関連するイベントを含みます | [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、[顧客行動とユーザーイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)、[ユーザープロファイルイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データ配信のエンタイトルメント" }

エンタイトルメントに含まれるイベントについてご不明な点がある場合は、Brazeアカウント担当者またはカスタマーサクセスマネージャーまでお問い合わせください。

## セキュアデータシェアリングについて {#about-secure-data-sharing}

データシェアリングでは、アカウント間で実際のデータがコピーまたは転送されることはありません。すべての共有は、Snowflake独自のサービスレイヤーとメタデータストアを通じて行われます。これは重要な概念です。共有データはお客様のアカウントのストレージを消費しないため、月々のデータストレージ料金に影響しません。発生する**唯一の**料金は、共有データのクエリに使用されるコンピューティングリソース（仮想ウェアハウスなど）に対するものです。

さらに、Snowflakeに組み込まれたロールおよび権限機能を使用することで、Brazeから共有されたデータへのアクセスを、お客様のSnowflakeアカウントやそのデータに対して既に設定されているアクセス制御を利用して管理・統制できます。アクセスの制限と監視は、お客様自身のデータと同じ方法で行うことができます。

- **インサイトまでの時間を短縮**<br>構築に数週間かかるETLプロセスに別れを告げましょう。BrazeとSnowflakeの独自アーキテクチャにより、すべてのカスタマーエンゲージメントおよびキャンペーンデータは、データレイクに到着した瞬間からすぐにアクセスおよびクエリが可能になります。データのコピーや移動は行われないため、最も関連性の高い最新の情報のみに基づいて顧客体験を提供できます。
- **データのサイロ化を解消**<br>チャネルやプラットフォーム全体で顧客の全体像を構築できます。データシェアリングにより、Brazeのカスタマーエンゲージメントデータとその他のすべてのSnowflakeデータの結合がこれまで以上に簡単になり、信頼できる単一の情報源からより豊富なインサイトを得ることができます。
- **エンゲージメントの水準を確認**<br>Braze Benchmarksを使用して、カスタマーエンゲージメント戦略を最適化しましょう。BrazeとSnowflakeを活用したこのインタラクティブツールを使用すると、チャネル、業界、デバイスプラットフォーム全体のベンチマークとブランドのエンゲージメントデータを比較できます。

Snowflakeのデータシェアリングの詳細については、[セキュアデータシェアリングの概要](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)を参照してください。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Braze アクセス | データ共有を設定するには、Braze アカウントまたはカスタマーサクセスマネージャーにお問い合わせください。 |
| Snowflake アカウント | `admin` 権限を持つ Snowflake アカウント。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## セキュアデータ共有の設定 {#setting-up-secure-data-sharing}

Snowflakeでは、[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)と[データ消費者](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)の間でデータ共有が行われます。このコンテキストでは、Brazeアカウントはデータシェアを作成して送信するため、データプロバイダーとなります&#8212;一方、Snowflakeアカウントはデータシェアを使用してデータベースを作成するため、データ消費者となります。詳細については、[Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers)を参照してください。

### ステップ1:Brazeからデータシェアを送信する {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### ステップ2:Snowflakeでデータベースを作成する {#step-2-create-the-database-in-snowflake}

1. 数分後、Snowflakeアカウントにインバウンドデータシェアが届きます。
2. インバウンドデータシェアを使用して、テーブルを表示およびクエリするためのデータベースを作成します。例:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. 新しいデータベースにクエリするための権限を付与します。

{% alert warning %}
Brazeダッシュボードで共有を削除して再作成した場合、以前に作成したデータベースを削除し、`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` を使用して再作成することで、インバウンド共有をクエリできるようになります。
複数のワークスペースから同じSnowflakeアカウントにデータを共有している場合は、マルチワークスペース構成の管理に関するガイダンスについて[Snowflake Data Sharing FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs)を参照してください。
{% endalert %}

## 使用方法と可視化 {#usage-and-visualization}

データ共有がプロビジョニングされたら、受信したデータ共有からデータベースを作成してください。共有されたすべてのテーブルがSnowflakeインスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリを実行できるようになります。ただし、共有データは読み取り専用であり、クエリの実行のみが可能で、いかなる方法でも変更や削除はできない点に注意してください。

Currentsと同様に、Snowflakeのセキュアデータ共有を使用して以下のことが可能です。

{% multi_lang_include partners/data_sharing_use_cases.md %}

[未加工のテーブルスキーマをダウンロードできます。](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

### ユーザー IDスキーマ {#user-id-schema}

ユーザー IDに関するBrazeとSnowflakeの命名規則の違いに注意してください。

| Brazeスキーマ | Snowflakeスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されるユーザープロファイルの一意の識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー IDスキーマ" }

## 重要な情報と制限事項 {#important-information-and-limitations}

### 破壊的変更と非破壊的変更 {#breaking-versus-non-breaking-changes}

#### 非破壊的変更 {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
新しいカラムは非破壊的変更と見なされるため、Brazeでは`SELECT *`クエリを使用する代わりに、各クエリで必要なカラムを明示的にリストすることを強くお勧めします。または、カラムを明示的に指定したビューを作成し、テーブルに直接クエリする代わりにそれらのビューに対してクエリを実行する方法もあります。
{% endalert %}

#### 破壊的変更 {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflakeのリージョン {#snowflake-regions}

Brazeは現在、以下のSnowflake AWSリージョンですべてのユーザーレベルのデータをホストしています:

 - US East-1
 - EU-Central（フランクフルト）
 - AP-Northeast-1（東京）
 - AP-Southeast-2（シドニー）
 - AP-Southeast-3（ジャカルタ）

これらのリージョン以外のユーザーに対しては、Brazeは任意のAWS、Azure、またはGCPリージョンでSnowflakeインフラをホストしている共同顧客にデータ共有を提供できます。

### データ保持 {#data-retention}

#### 保持ポリシー {#retention-policy}

2年以上経過したデータはアーカイブされ、長期ストレージに移動されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報（PII）の機密フィールドは削除されます（`properties`などのオプションのPIIフィールドも含まれます）。アーカイブされたデータには引き続き`user_id`フィールドが含まれており、すべてのイベントデータにわたるユーザーごとの分析が可能です。

各イベントについて、対応する`USERS_*_SHARED`ビューで直近2年間のデータに対してクエリを実行できます。さらに、各イベントには`USERS_*_SHARED_ALL`ビューがあり、匿名化されたデータと匿名化されていないデータの両方を返すクエリを実行できます。

#### 履歴データ {#historical-data}

Snowflakeの履歴イベントデータのアーカイブは2019年4月まで遡ります。BrazeがSnowflakeにデータを保存し始めた最初の数か月間は、製品の変更が行われたため、一部のデータが若干異なって見えたり、一部のnull値が含まれている可能性があります（この時点ではすべての利用可能なフィールドにデータを渡していなかったためです）。2019年8月以前のデータを含む結果は、期待とわずかに異なる可能性があると想定することをお勧めします。

### 一般データ保護規則（GDPR）への準拠 {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### クエリの速度、パフォーマンス、コスト {#speed-performance-cost-of-queries}

データに対して実行されるクエリの速度、パフォーマンス、コストは、データのクエリに使用するウェアハウスのサイズによって決まります。分析のためにアクセスするデータ量によっては、クエリを正常に実行するためにより大きなウェアハウスサイズを使用する必要がある場合があります。Snowflakeには、どのサイズを使用すべきかを判断するための優れたリソースが用意されています。[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスに関する考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)をご覧ください。

{% alert tip %}
Snowflakeの設定時に参考にできるクエリの例については、[サンプルクエリ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries)および[ETLイベントパイプラインの設定]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup)の例をご確認ください。
{% endalert %}