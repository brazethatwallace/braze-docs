---
nav_title: Celebrus
article_title: Celebrus 統合
description: "BrazeとCelebrusの統合。"
---

# Celebrus

> CelebrusはWebおよびモバイルアプリチャネルでBraze SDKとシームレスに統合され、チャネルアクティビティデータをBrazeに取り込みやすくなります。これには、特定期間におけるデジタルアセット全体のビジタートラフィックに関する包括的なインサイトも含まれます。<br><br>さらにCelebrusは、個々の顧客の豊富なプロファイルデータを取得し、Brazeと同期できます。これにより、包括的で正確かつ詳細なファーストパーティデータに基づき、効果的なBraze分析とコミュニケーション戦略を策定できます。この機能はCelebrusの機械学習を活用したシグナルによりさらに強化されます。これにより、大規模なタグ付け作業を必要とせずに、簡単にデータを取り込むことができます。堅牢なファーストパーティのIDグラフを導入することで、すべてのデータに即座にアクセスしてすぐに使用できるようになります。

_この統合はCelebrusによって管理されています。_

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Celebrusアカウント | このパートナーシップを活用するには、Celebrusアカウントが必要です。 |
| データウェアハウス（オプション） | Brazeカスタム属性用のCelebrusコネクターを使用する場合は、Brazeクラウドデータ取り込み（CDI）統合でサポートされるデータウェアハウスが必要です。また、BrazeダッシュボードでCDIを設定する必要があります。 |
| Braze SDKの設定（オプション） | Braze SDK用のCelebrusコネクターを使用する場合は、SDKエンドポイントとSDK APIキーを渡す必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 実装 {#implementation}
Celebrusの実装をインストールした後、Braze用のCelebrusコネクターを使用してCelebrusデータをBrazeに統合します。BrazeのCelebrus統合には、Braze SDKとBrazeカスタム属性という2つの要素があります。Brazeの使い方と必要なユースケースに応じて、いずれかまたは両方をデプロイできます。

WebチャネルにBraze SDKがまだ実装されていない場合は、Celebrusを使用してBraze SDKをデプロイできます。CelebrusはWebページにBraze SDKを追加し、CelebrusのIDグラフを使用してWeb訪問者のBraze IDを設定します。顧客属性は、クラウドデータ取り込み（CDI）を介してBrazeと同期できます。このためには、Braze CDIでサポートされるデータウェアハウスと、BrazeでのCDIの設定が必要です。

### Braze SDK用Celebrusコネクター {#celebrus-connector-for-braze-sdk}

Braze SDK用Celebrusコネクターは、BrazeのハイレベルなWebおよびモバイルアプリのチャネルデータを提供します。Braze SDKでは、CelebrusのIDグラフのCelebrus `System Identity`がBraze統合の識別子として使用されます。その他の識別子は、Brazeカスタム属性用Celebrusコネクターを介してカスタム属性を同期するためにサポートされています。

このコネクターによりチャネルにBraze SDKがデプロイされ、設定されます。このため、Braze SDKデータストリームでいくつかの設定を行い、次の3つの設定の値を指定する必要があります。

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Braze SDK用のCelebrusコネクターは、ユーザーを識別し、識別子をCelebrusのIDグラフに追加するためにBraze SDKを挿入および初期化します。このコネクターは、ユーザープロファイルにデータを記録したり、他のBraze SDKメソッドをトリガーしたりしません。<br><br>コードベース内で必要なメソッドを直接呼び出すことで、[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)経由でデータを記録したり、Braze SDKがサポートする他の機能を利用したりできます。
{% endalert%}

### Brazeカスタム属性用Celebrusコネクター {#celebrus-connector-for-braze-custom-attributes}

#### ステップ1:Celebrusで接続の詳細を設定する {#step-1-configure-connected-details-in-celebrus}

Brazeカスタム属性用のCelebrusコネクターは、カスタム属性を中間データベースに送信します。このときカスタム属性は、Brazeが受け取る形式で事前にフォーマットされています。Celebrusでは、使用しているデータベースの種類（SnowflakeやRedshiftなど）に応じて、データベースの接続詳細を設定します。

#### ステップ2:Brazeダッシュボードでクラウドデータ取り込みを設定する {#step-2-configure-cloud-data-ingestion-in-your-braze-dashboard}

この統合では、Brazeのクラウドデータ取り込みを使用します。[データウェアハウスの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)の手順に従って、使用するウェアハウスのタイプに応じて[クラウドデータ取り込みの設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を行ってください。

#### ステップ3:CelebrusからBrazeにデータを同期する {#step-3-sync-data-from-celebrus-to-braze}

Celebrusは、メール、電話番号、`external_id`またはユーザーエイリアスなどの一意の識別子をキャプチャして個人に割り当て、CDIを介してBrazeに送信します。これにより、同一の個人に関するデータをBrazeと同期できます。

Celebrusは、属性値が変更された場合にのみ、定義されている識別子を使用して、Celebrusプロファイルビルダーで定義された顧客属性を送信します。なお、Celebrusプロファイルビルダーで定義された属性名は、デフォルトでBrazeで使用されます。そのため、[Brazeの命名規則]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)に準拠するように、これらの名前を更新してください。

{% alert important %}
現時点では、このリリースではイベントと購入はサポートされていません。<br><br>この統合では、属性を文字列値として送信するため、一部の属性はリストになります（シグナルなど）。現時点では、リストを配列に変換することはできません。ネストされた属性はありません。
{% endalert%}