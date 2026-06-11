---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "このリファレンス記事では、BrazeとPersonalize.AIのパートナーシップについて説明します。Personalize.AIは、パーソナライズされたレコメンデーションによる収益成長を促進するAIベースのSaaSビジネスプラットフォームです。"
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/)はBrazeと連携し、Brazeから送信されるパーソナライズされたメッセージやオファーを配信することで、増分収益を生み出します。

BrazeとPersonalize.AIの統合により、メッセージのパーソナライゼーションとターゲティングのためにPersonalize.AIからBrazeプラットフォームにデータをエクスポートできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Personalize.AIインスタンス | このパートナーシップを利用するには、Personalize.AIインスタンスが必要です。 |
| Braze REST APIキー | すべての権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

* 柔軟な層別化を含むテストを展開し、顧客フィードバックから成果を導き出す
* 施策、タイミング、コンテンツなど、アイテムやオファーに対してパーソナライズされたレコメンデーションを提供する
* 優先する目標を特定し、Brazeを通じて最適なオーディエンスをターゲティングする
* 離脱したユーザーを再エンゲージする機会を特定する
* ジオロケーションデータを使用して、新規オープン店舗に適したオーディエンスを見つける
* 類似モデリングを使用して、新規ユーザー向けの限られたデータを活用し、最も関連性の高いレコメンデーションとマッチングさせる
* 顧客のライフサイクル全体を通じて適切なエンゲージメント方法を特定する
* 解約の可能性について顧客を事前に評価し、リスクスコアを割り当てて解約の早期兆候を発見する
* パーソナライズされた介入策で顧客をターゲティングし、非アクティブになるのを防ぐ

## 統合 {#integration}

### Personalize.AIでBrazeとの接続を設定する {#configure-a-connection-with-braze-in-personalizeai}

1. Personalize.AIで、Personalize.AIインスタンスの**Operationalization**にある**Integrations**タブに移動します。
2. **Braze**をクリックします。
3. Brazeとの統合を設定します。
    * **Connection Name:** 接続に名前を付けます。これがPersonalize.AIで統合を参照する際の名前になります。
    * **Sync Frequency:** 同期頻度は、Personalize.AIがBrazeにデータをエクスポートする頻度を制御します。**Daily**、**Weekly**、または**Monthly**を選択します。
    * **API Key:** BrazeのAPIキーを追加します。
    * **API URL:** Braze RESTエンドポイントURLを追加します。
4. **EXPORT**をクリックしてBrazeにデータをエクスポートします。

データがエクスポートされると、Personalize.AIは統合時に設定した同期頻度で決められた間隔でBrazeにデータを渡し続けます。

## この統合の使用方法 {#using-this-integration}

Personalize.AIにより、パーソナライズされたターゲティングに使用される識別子がBrazeにエクスポートされます。これらのカスタム属性は、各顧客のタイミング、コンテンツ、施策、オファーを示します。統合によっては、フィールドを顧客のプロファイルに保存する代わりに、イベントとして渡すか、[コネクテッドコンテンツAPI]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/public_apis/)に取り込むことができます。Personalize.AIでは、識別子として`external_id`の使用がサポートされています。

Brazeにインポートされたデータ属性には、一貫した用語に従って、Canvasesで使用するために直感的な名前が付けられています。たとえば、Personalize.AIの属性`C402_Target_Variant`は、Brazeに`"P.AI_Model_Treatment"`としてエクスポートされます。Personalize.AIからエクスポートされる属性は、既存の属性やトラッキングを妨げないように設計されています。これらの属性は継続的に検証されるため、確実に参照できます。

たとえば、解約防止に焦点を当てたCanvasの例に関連する顧客属性のセットを次に示します。

| Personalize.AI属性 | 値 |
| ----------- | ------------- |
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Treatment |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 aria-label="この統合の使用方法" }