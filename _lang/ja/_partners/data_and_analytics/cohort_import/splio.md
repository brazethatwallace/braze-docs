---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "このリファレンス記事では、BrazeとSplioのパートナーシップについて説明します。このパートナーシップにより、よりターゲットを絞ったキャンペーンを送信し、新しい製品機会を見つけ、収益を向上させることができます。"
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/)は、カスタマーエクスペリエンスを損なうことなくキャンペーン数と収益を増やすことができるオーディエンス構築ツールであり、オンラインとオフラインの両方でCRM キャンペーンのパフォーマンスを追跡するための分析を提供します。

BrazeとSplioの統合により、より優れたCRM戦略を計画・実行し、よりターゲットを絞ったキャンペーンを送信し、新しい製品機会を見つけ、収益を向上させることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Splioアカウント | このパートナーシップにはSplioアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## データインポート統合 {#data-import-integration}

BrazeとSplioを統合するには、Splioプラットフォームを設定し、既存のSplio キャンペーンをエクスポートし、今後のキャンペーンでユーザーをターゲットにするためのコホートセグメントをBrazeで作成する必要があります。

### ステップ 1: Brazeデータインポートキーを取得する {#step-1-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Splio**を選択します。

RESTエンドポイントを確認し、Brazeデータインポートキーを生成します。キーを生成した後、新しいキーを作成したり、既存のキーを無効にしたりできます。<br><br>![RESTエンドポイントとデータインポートキーが表示されたSplioテクノロジーパートナーページ。]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

統合を完了するには、データインポートキーとRESTエンドポイントをSplioデータオペレーションチームに提供してください。Splioが接続を確立し、セットアップ完了後に連絡します。

### ステップ 2: Splioプラットフォームからキャンペーンをエクスポートする {#step-2-export-a-campaign-from-the-splio-platform}

BrazeでSplioユーザーのコホートを作成するたびに、まずSplioプラットフォームからエクスポートする必要があります。

Splioで、エクスポートしたいキャンペーンを選択し、**Export キャンペーン**をクリックします。エクスポート後、オーディエンスは自動的にBrazeアカウントにアップロードされます。

![Splioプラットフォームからキャンペーンをエクスポートする。]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### ステップ 3: Splioカスタムオーディエンスからセグメントを作成する {#step-3-create-a-segment-from-the-splio-custom-audience}

Brazeで**セグメント**に移動し、Splioコホートセグメントに名前を付け、フィルターとして**Splio Cohorts**を選択します。ここから、含めるSplioコホートを選択します。Splioコホートセグメントを作成した後、キャンペーンやキャンバスを作成する際にオーディエンスフィルターとして選択できます。

![BrazeでSplioコホートセグメントを作成する。]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![Brazeセグメントビルダーで、ユーザー属性フィルター「Splioコホート」が「次を含む」と「Primary cohort」に設定されている。]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

コホートが見つからない場合は、[トラブルシューティング](#troubleshooting)セクションを参照してください。

{% alert important %}
すでにBrazeに存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

## この統合の使用方法 {#using-this-integration}

Splioセグメントを使用するには、Braze キャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択します。

![Brazeキャンペーンビルダーのターゲティングステップで、「セグメントを基準にユーザーをターゲットに設定」フィルターが「Splioコホート」に設定されている。]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## ユーザーマッチング {#user-matching}

Brazeは、識別されたユーザーを`external_id`または`alias`でマッチングします。匿名ユーザーは`device_id`でマッチングされます。もともと匿名ユーザーとして作成された識別済みユーザーは、`device_id`ではマッチングできず、`external_id`または`alias`でマッチングする必要があります。

## トラブルシューティング {#troubleshooting}

リストで正しいコホートが見つからない場合は、Splioでキャンペーンの詳細を表示し、**Export File Name**を確認して名前を検証してください。

![キャンペーン詳細ページの下部にコホート名が表示されている。]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

オーディエンスの取得に問題がある場合は、[Splioチーム](mailto:support-team@splio.com)に連絡してサポートを受けてください。