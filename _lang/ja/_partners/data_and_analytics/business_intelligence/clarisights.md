---
nav_title: Clarisights
article_title: Clarisights
description: "このリファレンス記事では、Brazeとセルフサービス型パフォーマンスマーケティングレポートプラットフォームであるClarisightsとのパートナーシップについて説明します。Brazeのキャンペーンやキャンバスからデータをインポートし、パフォーマンスおよびCRM/リテンションマーケティングの統合レポートインターフェイスを実現できます。"
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com)は、データドリブン型の組織向けのセルフサービス型パフォーマンスマーケティングレポートプラットフォームです。マーケティング、分析、およびアトリビューションのソースからすべてのデータを自動的に統合、処理、視覚化します。

_この統合はClarisightsによって管理されています。_

## 統合について {#about-the-integration}

BrazeとClarisightsの統合により、Brazeのキャンペーンやキャンバスからデータをインポートし、パフォーマンスおよびCRM/リテンションマーケティングの統合レポートインターフェイスを実現できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Clarisightsアカウント | このパートナーシップを利用するには、Clarisightsワークスペースが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー: <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
| Brazeワークスペース名 | Braze APIキーに関連付けられたワークスペースの名前。この名前は、Clarisights上のワークスペース統合を識別するために使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

BrazeとClarisightsの統合により、ユーザーはさまざまなビジュアライゼーションやテーブルを作成し、作成したキャンペーンからインサイトを得ることができます。一般的なユースケースには以下が含まれます。

{% tabs %}
{% tab 可視性の向上 %}
キャンペーンおよびキャンバス全体のパフォーマンスの可視性を向上させます。

![Clarisightsプラットフォームでの可視性向上の例を示すグラフィック。キャンペーンおよびキャンバスの開封数、クリック数、送信数、コンバージョン数などの統計が含まれています。]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab 詳細レポート %}
キャンペーンおよびキャンバスの詳細なレポート。

![「送信チャネル別の送信全体」や「コンバージョン率」などの詳細レポートを示すグラフィック。]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab 統合ダッシュボード %}
CMOおよびCXO向けの統合ダッシュボード。

![統合ダッシュボードの例を示すグラフィック。]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## 統合 {#integration}

BrazeデータをClarisightsに同期するには、Brazeコネクターを作成してBrazeワークスペースを接続する必要があります。

1. Clarisightsで**Integrations**ページに移動し、**Braze**コネクターを見つけ、**+ Connect**を選択します。<br>![Clarisightsの統合マーケットプレイスで利用可能なコネクターのリスト。]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. 次に、統合フローを使用してClarisightsアカウントをBrazeに接続します。これを行うには、Braze REST APIキー、Brazeワークスペース名、およびBraze RESTエンドポイントを指定します。<br>![ClarisightsプラットフォームのBrazeワークスペースコネクター。このページには、Brazeワークスペース名、Braze REST APIキー、およびBraze RESTエンドポイントのフィールドがあります。]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>統合が成功すると、同じページに接続済みのワークスペースが表示されます。<br>![「Braze Accounts」に接続済みワークスペースのリストが表示されます。]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## この統合を使う {#using-this-integration}

ClarisightsレポートにBrazeをデータソースとして含めるには、**Create New Report**に移動します。レポートに名前を付け、表示されるプロンプトでデータソースとして**Braze**を選択します。レポートに含める指標やディメンションを選択することもできます。完了したら、**Create Report**を選択します。

Brazeのデータは、次回のスケジュールされたデータインポートの時点から流入し始めます。長期間のバックフィルをリクエストする場合は、Clarisightsのカスタマーサクセスマネージャーにお問い合わせください。

![Clarisightsのレポート設定で、名前とデータソースのフィールドが表示されています。この例では「Braze」がデータソースとして選択されています。]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

利用可能な[指標とディメンション](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions)または[レポート作成](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights)の詳細については、Clarisightsにアクセスしてください。