---
nav_title: データモデル
article_title: B2Bデータモデルを作成する
page_order: 0
page_type: reference
description: "Brazeデータツールを使用してB2Bモデルを作成する方法について説明します。"
---

# B2Bデータモデルを作成する {#create-a-b2b-data-model}

> このユースケースでは、Brazeデータツールを使用して効果的で効率的なB2Bデータモデルを作成し、ビジネスユーザーへのメッセージのターゲット設定、トリガー、パーソナライゼーション、送信に役立てる方法を説明します。

{% alert note %}
これらの推奨事項は、BrazeがB2B機能を構築するにつれて、時間の経過とともに変化する可能性があります。
{% endalert %}

B2Bデータモデルの設定方法を説明する前に、知っておくべきいくつかの概念と用語について確認しましょう。

B2B Campaignsを実行するために必要な主要なB2Bオブジェクトは4つあります。

| オブジェクト | 説明 |
| --- | --- |
| リード | 製品やサービスに興味を示したが、まだ案件として認定されていない潜在顧客の記録です。 |
| 連絡先 | 通常、リードから連絡先に適格と判断されて変換され、営業案件を追求する個人です。 |
| 案件 | 潜在的な販売や進行中の取引の詳細を追跡する記録です。 |
| アカウント | 適格な見込み顧客、既存の顧客、パートナー、または同様に重要な関係を持つ競合他社である組織の記録です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="B2Bデータモデルを作成する" }

Braze内では、この4つのオブジェクトが結合され、ユーザープロファイルとビジネスオブジェクトという2つのオブジェクトに集約されます。

| Braze B2Bオブジェクト | 説明 | 元のB2Bオブジェクト  |
| --- | --- | --- |
| ユーザープロファイル | 営業用CRMシステムのリードおよび連絡先に直接マッピングされます。リードはBrazeによってキャプチャされるため、営業用CRMシステムでは自動的にリードとして作成されます。連絡先に変換されると、連絡先IDと詳細がBrazeに同期されます。 | リード<br> 連絡先 |
| ビジネスオブジェクト | 営業用CRMシステム内のすべての非ユーザーオブジェクトにマッピングされます。これには、アカウントオブジェクトや案件オブジェクトなど、営業固有のオブジェクトが含まれます。 | アカウント<br> 案件 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="B2Bデータモデルを作成する" }

## ステップ1: Brazeでビジネスオブジェクトを作成する {#step-1-create-your-business-objects-in-braze}

ビジネスオブジェクトは、ユーザー中心でない任意のデータセットです。B2Bのコンテキストでは、アカウントと案件のデータ、および会社が追跡するその他の関連するユーザー中心でないデータセットが含まれます。

Brazeでビジネスオブジェクトを作成および管理するには、カタログと接続されたソースの2つの方法があります。

| 方法 | 説明 |
| --- | --- |
| [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/) | Brazeのプライマリユーザープロファイル上の独立したデータオブジェクト（補足データオブジェクト）です。B2Bのコンテキストでは、アカウントと案件のカタログを作成することが多いでしょう。 |
| [接続されたソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) | Brazeがデータウェアハウスに直接クエリを実行できるようにします。すでにリード、連絡先、案件、アカウントの各オブジェクトをデータウェアハウスと定期的に同期している場合、Brazeのセグメンテーションをそのウェアハウスに直接向けて、ゼロコピー環境で有効化できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1: Brazeでビジネスオブジェクトを作成する" }

{% tabs %}
{% tab カタログ %}

### オプション1: アカウントと案件にカタログを使用する {#option-1-use-catalogs-for-accounts-and-opportunities}

カタログは、Brazeでホストおよび管理されるデータテーブルです。アカウントデータと案件データは使用している営業用CRMシステムから取得されますが、Brazeでこれらを複製して、アカウントベースのセグメンテーション、アカウントベースのマーケティング、リード管理などのマーケティング目的で使用します。

このオプションでは、アカウント用と案件用にそれぞれ1つずつカタログを作成し、[カタログAPI]({{site.baseurl}}/api/endpoints/catalogs/)または[カタログクラウドデータ取り込み（CDI）]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)を通じてBrazeに更新を送信することで、頻繁に更新することをお勧めします。これらのカタログを作成する際は、カタログの`id`（最初の列）が営業用CRMシステムの`id`と一致していることを確認してください。

#### CRMフィールドをマッピングする {#map-over-your-crm-fields}

以下の表に、CRMのアカウントオブジェクトと案件オブジェクトからマッピングできるフィールドの例をいくつか示します。

{% subtabs %}
{% subtab Account catalog %}

このユースケースでは、SalesforceをCRMシステムの例として使用しています。CRMのオブジェクトに含まれる任意のフィールドをマッピングできます。

<table aria-label="CRMフィールドのマッピング" border="1">
  <caption>CRMフィールドのマッピング</caption>
  <thead>
  <tr>
    <th><b>Brazeオブジェクト</b></th>
    <th><b>Brazeフィールド</b></th>
    <th><b>CRMオブジェクト（Salesforce）</b></th>
    <th><b>CRMフィールド（Salesforce）</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">カタログ &gt; アカウントカタログ</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tbody>
</table>

##### マッピングされたアカウントフィールドのテーブル例 {#example-table-of-mapped-account-fields}

![Salesforceアカウントの一覧と、請求先住所やアカウント所有者などの関連情報。]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

このユースケースでは、SalesforceをCRMシステムの例として使用しています。CRMのオブジェクトに含まれる任意のフィールドをマッピングできます。

<table aria-label="マッピングされたアカウントフィールドのテーブル例" border="1">
  <caption>マッピングされたアカウントフィールドのテーブル例</caption>
  <thead>
  <tr>
    <th><b>Brazeオブジェクト</b></th>
    <th><b>Brazeフィールド</b></th>
    <th><b>CRMオブジェクト（Salesforce）</b></th>
    <th><b>CRMフィールド（Salesforce）</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">カタログ &gt; 案件カタログ</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
  </tbody>
</table>

##### マッピングされた案件フィールドのテーブル例 {#example-table-of-mapped-opportunity-fields}

![Salesforceの案件一覧と、請求先住所やアカウント所有者などの関連情報。]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 接続されたソース %}

### オプション2: アカウントと案件に接続されたソースを使用する {#option-2-use-connected-sources-for-accounts-and-opportunities}

接続されたソースは、自社のデータウェアハウスにホストされているデータテーブルであり、Brazeの[CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/)によってクエリが実行されます。カタログとは異なり、Brazeでビジネスオブジェクト（アカウントと案件）を複製する代わりに、データウェアハウスにこれらを保持し、ウェアハウスを信頼できる情報源として使用します。

接続されたソースを設定するには、[接続されたソースの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/#integrating-connected-sources)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ2: ビジネスオブジェクトをユーザープロファイルに関連付ける {#step-2-relate-your-business-objects-to-user-profiles}

ユーザープロファイルはBrazeの主要なオブジェクトであり、デモグラフィックセグメンテーション、トリガー、パーソナライゼーションの大部分を支えています。ユーザープロファイルには、SDKやその他のソースによって収集された[デフォルトのユーザーデータ]({{site.baseurl}}/user_guide/data/unification/user_data/)と、[カスタムデータ]({{site.baseurl}}/user_guide/data/activation/)が含まれます。カスタムデータは、属性（デモグラフィックデータ）、イベント（行動データ）、購入（トランザクションデータ）のいずれかの形式を取ります。

### ステップ2.1: 営業用CRMのIDをBrazeにマッピングする {#step-21-map-sales-crm-ids-to-braze}

まず、Brazeとご利用のCRMに、データを共有するための共通の識別子があることを確認します。次の表を使用して、営業用CRMのIDフィールドをBrazeユーザーオブジェクトにマッピングすることをお勧めします。以下の表ではCRMシステムとしてSalesforceを使用していますが、これはあらゆるCRMに適用できます。

#### Brazeオブジェクト: ユーザー {#braze-object-user}

| Brazeフィールド | CRMオブジェクト（Salesforce） | CRMフィールド（Salesforce） | 追加情報 |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | リード | `id` | - ユーザー別名ラベル: `salesforce_lead_id` <br>- ユーザー別名: `lead_id` |
| `Aliases.salesforce_contact_id` | 連絡先 | `id` | - ユーザー別名ラベル: `salesforce_contact_id` <br>- ユーザー別名: `contact_id` |
| `AccountId` | 連絡先 | `AccountId` |
| `OpportunityId`（オプション、スカラー）<br>または<br> `Opportunities`（オプション、配列） | 案件 | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Brazeオブジェクト: ユーザー" }

{% alert note %}
Salesforceのリードと連絡先の識別子をBrazeにマッピングするには、`external_id`ではなく[エイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases)を使用することをお勧めします。これにより、プロダクトレッドグロース型のイニシアチブを特定して実行する際に必要なルックアップの量を削減できます。
{% endalert %}

IDを同期したら、Brazeユーザープロファイルをビジネスオブジェクトに関連付ける必要があります。

### ステップ2.2: ユーザープロファイルとビジネスオブジェクト間のリレーションシップを作成する {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab カタログ %}

#### オプション1: カタログを使用する場合 {#option-1-when-using-catalogs}

案件およびアカウントの詳細がBrazeカタログとして登録されたので、これらのカタログと、メッセージを送信するユーザープロファイルとの間にリレーションシップを作成する必要があります。現在、これには2つのステップが必要です。

1. アカウント（`account_id (string)`など）、案件ID（`opportunity_ids (array)`など）、またはその両方を、属性としてユーザープロファイルに含めます。
2. イベントプロパティとしてアカウントIDを含むイベント（`account_linked`など）をログに記録します。

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab 接続されたソース %}

#### オプション2: 接続されたソースを使用する場合 {#option-2-when-using-connected-sources}

接続されたソースのテーブルの1つに、Brazeでユーザーに対して設定された`external_user_id`に一致する`user_id`が含まれている必要があります。前述のユーザープロファイル設定では、リードと`contact_ids`を`external_id`として使用しているため、リード/連絡先のテーブルにこれらのIDが含まれていることを確認してください。

IDの一致を確認することに加え、効率的なセグメンテーションとパーソナライゼーションのために、`account_id`、`opportunity_id`などの基本的なアカウントレベルデータや、`industry`などの一般的な企業統計属性をユーザープロファイルに書き込むことをお勧めします。

{% endtab %}
{% endtabs %}