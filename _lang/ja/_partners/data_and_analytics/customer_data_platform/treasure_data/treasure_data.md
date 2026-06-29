---
nav_title: トレジャーデータ
article_title: トレジャーデータ
description: "このリファレンス記事では、Brazeとトレジャーデータのパートナーシップについて説明します。トレジャーデータはエンタープライズ顧客データプラットフォームであり、Brazeに直接ジョブの結果を書き込むことができます。"
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# トレジャーデータ {#treasure-data}

> [トレジャーデータ](https://www.treasuredata.com/)は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所に情報をルーティングする顧客データプラットフォーム（CDP）です。

Brazeとトレジャーデータの統合により、トレジャーデータのジョブ結果をBrazeに直接書き込むことができます。これにより、以下のことが可能になります。
* **external IDをマッピングする**：CRMシステムからBrazeユーザーアカウントにIDをマッピングします。
* **オプトアウトを管理する**：エンドユーザーが参加しないことを選択して同意を更新した場合に対応します。
* **イベント、購入、またはカスタムプロファイル属性のトラッキングをアップロードする**。この情報は、正確な顧客セグメントの作成に役立ち、キャンペーンのユーザーエクスペリエンスを向上させます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| トレジャーデータのアカウント | このパートナーシップを活用するには、[トレジャーデータのアカウント](https://www.treasuredata.com/custom-demo/)が必要です。 |
| Braze REST APIキー | `users.track`、`users.delete`、`users.alias.new`、`users.identify`の権限を持つBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**Settings** > **API Keys**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

ターゲットセグメントを構築するために、統合された顧客プロファイルをトレジャーデータからBrazeに同期できます。トレジャーデータは、ファーストパーティのCookieデータ、モバイルID、CRMなどのサードパーティシステムなどをサポートしています。

## 統合 {#integration}

### ステップ1：新しい接続を作成する {#step-1-create-a-new-connection}

トレジャーデータで、**Integrations Hub**の下にある**Catalog**に移動し、**Braze**を検索して選択します。

**New Authentication**プロンプトが表示されたら、接続に名前を付け、Braze REST APIキーとRESTエンドポイントを入力します。完了したら**Done**を選択します。

![]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### ステップ2：クエリを定義する {#step-2-define-your-query}

トレジャーデータで、**Data Workbench**の下にある**Queries**に移動し、データをエクスポートしたいクエリを選択します。このクエリを実行して結果セットを検証します。

{% alert note %}
HIVEを使用してクエリを作成するユーザーの場合、HIVEではアンダースコアで始まる列またはテーブルをバッククォートで囲む必要があります。たとえば `_merge_objects` です。
{% endalert %}

次に、**Export Results**を選択し、既存の統合認証を選択します。

![]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

次の[カスタマイズセクション](#customization)に概説されているように、追加のエクスポート結果パラメータを定義します。エクスポート統合コンテンツで、統合パラメータを確認してください。

![「Export Results」ページ。このページには「mode」、「track record type」、および「pre-formatted fields」のフィールドがあります。この例では、それぞれのフィールドに「User-Track」と「Custom Events」が設定されています。]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

最後に、**Done**を選択し、クエリを実行して、データがBrazeに移動したことを確認します。

### カスタマイズ {#customization}

エクスポート結果のパラメータは次の表に含まれています。

| パラメータ | 値 | 説明 |
|---------------------------|---|---|
| `mode` | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | コネクターモード |
| `pre_formatted_fields` | 文字列 | 配列またはJSON列に使用してフォーマットを保持します。 |
| `track_record_type` | Custom Events<br>Purchases<br>User Profile Attributes | **User - Track**モードのレコードタイプ |
| `skip_on_invalid_records` | ブール値 | 有効にした場合、続行してJSON列の無効なレコードを無視します。<br> それ以外の場合は、ジョブが停止します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Customization" }

{% alert note %}
事前にフォーマットされたフィールド、サンプルクエリ、パラメータの詳細、およびクエリエクスポートジョブのスケジューリングについては、[トレジャーデータ](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration)を参照してください。
{% endalert %}

## Webhook {#webhooks}

トレジャーデータのユーザーは、パブリックREST APIを介してデータを取り込むことができます。トレジャーデータを使用して、データにカスタムWebhookを作成できます。詳細については、[トレジャーデータ](https://docs.treasuredata.com/display/public/PD/Postback+API)を参照してください。