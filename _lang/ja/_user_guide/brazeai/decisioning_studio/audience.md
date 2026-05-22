---
nav_title: オーディエンスの定義
article_title: オーディエンスの定義
page_order: 3
page_type: reference
description: "BrazeAI Decisioning Studioエージェントのオーディエンスの定義と設定方法（トリートメントグループやプラットフォーム固有のセットアップ手順を含む）について説明します。"
---

# オーディエンスの定義 {#define-your-audience}

> ユースケースのオーディエンスは通常、カスタマーエンゲージメントプラットフォーム（BrazeやSalesforce Marketing Cloudなど）で定義され、Decisioning Studioエージェントに送信されます。エージェントはランダム化比較試験を実施するために、顧客をトリートメントグループに分割します。

## トリートメントグループ {#treatment-groups}

| グループ | 説明 |
|-------|-------------|
| **Decisioning Studio** | AIによって最適化されたおすすめを受け取る顧客 |
| **ランダムコントロール** | ランダムに選択されたオプションを受け取る顧客（ベースライン比較用） |
| **Business-as-Usual（オプション）** | 現在のマーケティングジャーニーを受け取る顧客（既存のパフォーマンスとの比較用） |
| **ホールドアウト（オプション）** | コミュニケーションを受け取らない顧客（キャンペーン全体の影響を測定するため） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Treatment groups" }

## オーディエンスの設定 {#configure-your-audience}

{% tabs %}
{% tab Braze %}

1. ターゲットにしたいオーディエンスのセグメントを作成します。
2. セグメント IDをAI意思決定サービスチームに提供します。

{% alert note %}
Brazeでは、複数のセグメントを取り込み、それらを組み合わせてオーディエンスを作成できます。Decisioning StudioはBusiness-as-Usual比較キャンペーンのためにセグメントを取り込むことができます。これらのパターンはすべて使用可能です。
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. オーディエンス用のSFMCデータエクステンションを設定し、データエクステンションIDを提供します
2. Decisioning Studioが必要とする適切な権限を持つAPI統合用のSFMCインストール済みパッケージをセットアップします
3. Decisioning Studioは利用可能な最新の増分データから取得するため、このデータエクステンションが毎日更新されることを確認します

エクステンションIDとAPIキーをAI意思決定サービスチームに提供してください。チームが顧客データの取り込みにおける次のステップをサポートします。

{% endtab %}
{% tab その他のプラットフォーム %}

### Google Cloud Storage

オーディエンスが現在BrazeまたはSalesforce Marketing Cloudに保存されていない場合、次善のステップとして、Brazeが管理するGoogle Cloud Storage（GCS）バケットへの自動エクスポートを設定します。

これが実現可能かどうかを判断するには、お使いのプラットフォームのドキュメントを参照してください。たとえば、mParticleは[Google Cloud Storageとのネイティブ統合](https://www.mparticle.com/integration/google-cloud-storage/)を提供しています。この場合、オーディエンスデータのエクスポート先としてGCSバケットを提供できます。

### その他のリソース {#additional-resources}

- [Twilio セグメント](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## 次のステップ {#next-steps}

オーディエンスを定義したら、オーケストレーションのセットアップに進みます。

- [オーケストレーションのセットアップ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup/)