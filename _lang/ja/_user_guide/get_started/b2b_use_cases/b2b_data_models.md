---
nav_title: データモデル
article_title: B2Bデータモデルを作成する
page_order: 0
page_type: reference
description: "Brazeデータツールを使用してB2Bモデルを作成する方法について説明します。"
---

# B2Bデータモデルを作成する {#create-a-b2b-data-model}

> このユースケースでは、Brazeデータツールを使用して、効果的で効率的なB2Bデータモデルを作成する方法を示しています。B2Bデータモデルは、メッセージのターゲット設定、トリガー、パーソナライゼーション、およびビジネスユーザーへの送信に役立ちます。

{% alert note %}
これらの推奨事項は、BrazeがB2B機能を構築するにつれて、時間の経過とともに変化する可能性があります。
{% endalert %}

B2Bデータモデルの設定方法を説明する前に、知っておくべきいくつかの概念と用語について説明します。

B2Bキャンペーンを実行するために必要な主要なB2Bオブジェクトは4つあります。

| オブジェクト | 説明 |
| --- | --- |
| リード | 製品やサービスに興味を示したが、まだ機会として認定されていない潜在的な顧客の記録。 |
| 連絡先 | 通常、適格と判断され、セールス案件を追求するためにリードから連絡先に変換された個人。 |
| 機会 | 潜在的な売却または進行中の取引の詳細を追跡するレコード |
| アカウント | 適格な見込み顧客、既存の顧客、パートナー、または類似する重要な関係性を持つ競合他社である組織のレコード。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="B2Bデータモデルを作成する" }

Braze内では、この4つのオブジェクトが結合され、ユーザープロファイルとビジネスオブジェクトという2つのオブジェクトに集約されます。

| Braze B2Bオブジェクト | 説明 | 元のB2Bオブジェクト  |
| --- | --- | --- |
| ユーザープロファイル | 営業用CRMシステムのリードおよび連絡先に直接マップされます。リードはBrazeによってキャプチャされるため、営業用CRMシステムでは自動的にリードとして作成されます。連絡先に変換されると、連絡先IDと詳細がBrazeに同期されます。 |リード<br> 連絡先 |
| ビジネスオブジェクト | 営業用CRMシステム内のすべての非ユーザーオブジェクトにマップされます。これには、アカウントオブジェクトや案件オブジェクトなど、営業固有のオブジェクトが含まれます。 | アカウント<br> 機会 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="B2Bデータモデルを作成する" }

## ステップ 1:Brazeでビジネスオブジェクトを作成する {#step-1-create-your-business-objects-in-braze}

ビジネスオブジェクトは、ユーザー中心でない任意のデータセットです。B2Bコンテキストでは、アカウントと商談データ、および会社が追跡するその他の関連するユーザー中心でないデータセットが含まれます。

Brazeでビジネスオブジェクトを作成および管理するには、カタログと接続されたソースの2つの方法があります。

| 方法 | 説明 |
| --- | --- |
| [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs) | Brazeのプライマリユーザープロファイル上の独立したデータオブジェクト（補足データオブジェクト）です。B2Bのコンテキストでは、アカウントと案件のカタログがある可能性があります。 |
| [接続されたソース]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) | Brazeがデータウェアハウスに直接クエリを実行できるようにします。すでにリード、連絡先、案件、アカウントの各オブジェクトをデータウェアハウスと定期的に同期している可能性があるため、Brazeセグメンテーションをそのウェアハウスに直接ポイントし、ゼロコピー環境で有効化することができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1:Brazeでビジネスオブジェクトを作成する" }

{% tabs %}
{% tab Catalogs %}

### オプション 1:アカウントと案件のカタログを使用する {#option-1-use-catalogs-for-accounts-and-opportunities}

カタログは、Brazeでホストおよび管理されるデータテーブルです。アカウントデータと案件データは使用している営業用CRMシステムから作成されますが、Brazeでこれらのデータを複製して、マーケティング目的（アカウントベースのセグメンテーション、アカウントベースのマーケティング、リード管理など）で使用できます。

このオプションでは、アカウント用と商談用にそれぞれ1つずつカタログを作成し、[カタログAPI]({{site.baseurl}}/api/endpoints/catalogs)または[カタログクラウドデータ取り込み（CDI）]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を通じてBrazeに更新を送信することで、頻繁に更新することをお勧めします。これらのカタログを作成するときは、カタログの`id`（最初の列）が営業用CRMシステムの`id`と一致していることを確認してください。

#### CRMフィールドにマップする {#map-over-your-crm-fields}

以下の表に、CRMのアカウントオブジェクトと案件オブジェクトからマップできるフィールドの例をいくつか示します。

{% subtabs %}
{% subtab Account catalog %}

このユースケースでは、SalesforceがCRMシステムの例です。CRMのオブジェクトに含まれる任意のフィールドにマップできます。

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

{% endsubtab %}
{% subtab Opportunity catalog %}

このユースケースでは、SalesforceがCRMシステムの例です。CRMのオブジェクトに含まれる任意のフィールドにマップできます。

<table aria-label="マッピングされたアカウントフィールドの例" border="1">
  <caption>マッピングされたアカウントフィールドの例</caption>
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

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### オプション 2:アカウントと案件に接続されたソースを使用する {#option-2-use-connected-sources-for-accounts-and-opportunities}

接続されたソースは、自社データウェアハウスにホストされているデータテーブルであり、Braze [CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)によってクエリが実行されます。カタログとは異なり、Brazeでビジネスオブジェクト（アカウントと案件）を複製する代わりに、データウェアハウスにこれらのオブジェクトを維持し、ウェアハウスを信頼できる情報源として使用します。

接続されたソースを設定するには、[接続されたソースの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources#integrating-connected-sources)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 2:ビジネスオブジェクトをユーザープロファイルに関連付ける {#step-2-relate-your-business-objects-to-user-profiles}

ユーザープロファイルは、Brazeの主要なオブジェクトであり、人口統計セグメンテーション、トリガー、パーソナライゼーションの大部分の処理に使用されます。ユーザープロファイルには、SDKやその他のソースによって収集された[デフォルトのユーザーデータ]({{site.baseurl}}/user_guide/data/unification/user_data)と、[カスタムデータ]({{site.baseurl}}/user_guide/data/activation)が含まれます。カスタムデータは、属性（人口統計データ）、イベント（行動データ）、購入（トランザクションデータ）のいずれかの形式になります。

### ステップ 2.1:営業用CRMのIDをBrazeにマッピングする {#step-21-map-sales-crm-ids-to-braze}

まず、Brazeとご利用のCRMに、データを共有するための共通の識別子があることを確認します。次の表を使用して、営業用CRMのIDフィールドをBrazeユーザーオブジェクトにマップすることをお勧めします。以下の表ではCRMシステムとしてSalesforceが使用されていますが、これはあらゆるCRMに適用できます。

#### Brazeオブジェクト:ユーザー {#braze-object-user}

| Brazeフィールド | CRMオブジェクト（Salesforce） | CRMフィールド（Salesforce） | 追加情報 |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | リード | `id` |  - ユーザー別名ラベル: `salesforce_lead_id` <br>- ユーザー別名: `lead_id`|
| `Aliases.salesforce_contact_id` | 連絡先 | `id` | - ユーザー別名ラベル: `salesforce_contact_id` <br>- ユーザー別名: `contact_id` |
| `AccountId` | 連絡先 | `AccountId` |
| `OpportunityId`（オプション、スカラー） <br>または<br> `Opportunities`（オプション、配列） | 案件 | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Brazeオブジェクト:ユーザー" }

{% alert note %}
Salesforceのリードと連絡先の識別子をBrazeにマップするには、`external_id`ではなく[エイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)を使用することをお勧めします。これは、製品主導の成長スタイルのイニシアチブを特定して実行する際に必要なルックアップの量を減らすためです。
{% endalert %}

IDを同期したら、Brazeユーザープロファイルをビジネスオブジェクトに関連付ける必要があります。

### ステップ 2.2:ユーザープロファイルとビジネスオブジェクト間の関係を作成する {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catalogs %}

#### オプション 1:カタログを使用する場合 {#option-1-when-using-catalogs}

商談およびアカウントの詳細がBrazeカタログとして登録されたので、これらのカタログと、メッセージを送信するユーザープロファイルとの間に関係を作成する必要があります。現在、これには2つのステップが必要です。

1. アカウント（`account_id (string)`など）または案件ID（`opportunity_ids (array)`など）、あるいはこの両方を、属性としてユーザープロファイルに含めます。
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
{% tab Connected sources %}

#### オプション 2:接続されたソースを使用する場合 {#option-2-when-using-connected-sources}

接続されたソースのテーブルの1つに、Brazeでユーザーに対して設定された`external_user_id`に一致する`user_id`が含まれている必要があります。前述のユーザープロファイル設定では、リードと`contact_ids`を`external_id`として使用しています。このため、リード/連絡先のテーブルにこれらのIDが含まれていることを確認する必要があります。

IDの一致を確認することに加え、効率的なセグメンテーションとパーソナライゼーションのために、基本的なアカウントレベルデータ（`account_id`、`opportunity_id`など）と一般的な企業統計属性（`industry`など）をユーザープロファイルに書き込むことをお勧めします。

{% endtab %}
{% endtabs %}