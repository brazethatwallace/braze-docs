---
nav_title: アカウントベースのセグメンテーション
article_title: アカウントベースのセグメンテーションを設定する
page_order: 2
page_type: reference
description: "B2Bアカウントベースのセグメンテーションのユースケースを強化するためのBrazeのさまざまな機能の使用方法を学びます。"
---

# アカウントベースのセグメンテーションを設定する {#set-up-account-based-segmentation}

> このページでは、さまざまなBraze機能を使用してB2Bアカウントベースのセグメンテーションのユースケースを強化する方法について説明します。

[B2Bデータモデル]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models)の設定方法に応じて、次の2つの方法でB2Bアカウントベースのセグメンテーションを実行できます。

- [ビジネスオブジェクトにカタログを使用する場合](#option-1-when-using-catalogs-for-your-business-objects)
- [ビジネスオブジェクトに接続ソースを使用する場合](#option-2-when-using-connected-sources-for-your-business-objects)

## B2Bアカウントベースのセグメンテーションの設定 {#setting-up-b2b-account-based-segmentation}

### オプション1: ビジネスオブジェクトにカタログを使用する場合 {#option-1-when-using-catalogs-for-your-business-objects}

#### 基本的なSQLテンプレートのセグメンテーション {#basic-sql-template-segmentation}

まずは、シンプルなアカウントベースのセグメンテーションのための基本的なSQLテンプレートを用意しました。

ターゲットのエンタープライズアカウントの従業員であるユーザーをセグメント化するとします。

1. **Audience** > **セグメントエクステンション** > **新規エクステンションを作成** > **テンプレートから開始**の順に移動し、**Catalog segment for events**テンプレートを選択します。<br><br> ![「テンプレートの選択」モーダルで、イベントまたは購入のカタログセグメントオプションを選択できます。]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>SQLエディターには、ユーザーイベントデータとカタログデータを結合し、特定のカタログアイテムにエンゲージしたユーザーをセグメンテーションするテンプレートが自動的に入力されます。<br><br>![「Variables」タブが開いた状態の新しいエクステンションのSQLエディター。]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. **Variables**タブを使用して、セグメントを生成する前にテンプレートに必要なフィールドを指定します。<br><br>Brazeがカタログアイテムへのエンゲージメントに基づいてユーザーを識別するには、次のことを行う必要があります。
- カタログフィールドを含むカタログを選択する
- イベントプロパティを含むカスタムイベントを選択する
- カタログのフィールドとイベントのプロパティ値を一致させる

##### B2Bユースケースの変数ガイドライン {#variables-guidelines-for-b2b-use-cases}

B2Bアカウントベースのセグメンテーションのユースケースについて、以下の変数を選択します。

| 変数 | プロパティ |
| --- | --- |
| カタログ | アカウントカタログ |
| カタログフィールド | ID |
| カスタムイベント | account_linked |
| カスタムイベントプロパティ | account_id |
| (Filter SQL Resultsで) カタログフィールド | Classification |
| (Filter SQL Resultsで) 値 | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="B2Bユースケースの変数ガイドライン" }

#### 高度なSQLセグメンテーション {#sophisticated-sql-segmentation}

より高度で複雑なセグメンテーションについては、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)を参照してください。B2Bアカウントベースのセグメンテーションを開始するのに役立つSQLテンプレートをいくつか紹介します。

1. 1つのカタログで2つのフィルターを比較するセグメントを作成します（エンタープライズレベルのアカウントでレストラン業界に勤務するユーザーなど）。カタログIDとアイテムIDを含める必要があります。

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
;
```

{: start="2"}
2. 2つの別個のカタログにまたがる2つのフィルターを比較するセグメントを作成します（例えば、オープン中の「Stage 3」の商談があるエンタープライズターゲットアカウントに関連するユーザーなど）。

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### オプション2: ビジネスオブジェクトに接続ソースを使用する場合 {#option-2-when-using-connected-sources-for-your-business-objects}

セグメンテーションにおける接続ソースの使用方法の基本については、[CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)を参照してください。[カタログを使用する場合](#option-1-when-using-catalogs-for-your-business-objects)で取り上げたテンプレートを参考に、ソーステーブルのフォーマットを自由に設定できます。

## セグメントでアカウントベースのエクステンションを使用する {#using-your-account-based-extension-in-a-segment}

上記のステップでアカウントレベルのセグメンテーションを作成したら、それらのセグメントエクステンションをターゲティング条件に直接取り込むことができます。また、役割や以前のキャンペーンへのエンゲージメントなど、ユーザーの属性条件を段階的に追加して適用することも簡単です。詳しくは、[セグメントでエクステンションを使用する]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment)を参照してください。