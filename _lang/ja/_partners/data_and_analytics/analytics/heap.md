---
nav_title: Heap
article_title: "Heap Analytics"
description: "このリファレンス記事では、Braze Currentsを使用してHeapでエンゲージメントイベントを自動的に分析する方法について説明します。Heapはデジタルインサイトプラットフォームであり、HeapデータをBrazeにインポートしたり、ユーザーコホートを作成したり、BrazeデータをHeapにエクスポートしてセグメントを作成したりできます。"
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Heap Analytics

> この記事では、分析のためにBrazeからHeapにエンゲージメントイベントを自動送信する方法について説明します。Heapとその他の機能（Brazeへの[Heapコホートの同期]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap#data-import-integration)など）の統合について詳しくは、メインの[Heap記事]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)を参照してください。

## データエクスポート統合 {#data-export-integration}

Braze Currentsを使用して、Brazeからエンゲージメントイベント（メール送信、プッシュ送信など）をHeapに自動的に送信し、分析します。

### ステップ1:Heap認証情報を取得する {#step-1-get-heap-credentials}

この統合を設定するには、WebhookエンドポイントURLが必要です。このURLは、Heapアカウントマネージャーから取得できます。

### ステップ2:Braze Currentsを設定する {#step-2-configure-braze-currents}

Brazeで**パートナー連携** > **データのエクスポート**に移動し、**新しいCurrentsを作成**をクリックし、**Heapエクスポート**を選択します。

エクスポートに名前を付け、**Currentの詳細**ページに進みます。このページでは、エンドポイントとオプションのベアラートークン（提供されている場合）を入力します。

統合の認証情報を設定したら、Heapにエクスポートするすべてのメッセージエンゲージメント、顧客行動、およびユーザーイベントを確認し、**Currentを起動**をクリックします。

![BrazeのHeap Currents設定ページ。エンドポイント、トークン、イベント選択フィールドが表示されています。]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}