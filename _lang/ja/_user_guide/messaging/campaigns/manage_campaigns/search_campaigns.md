---
nav_title: Campaignの検索
article_title: Campaignの検索
page_order: 10
page_type: reference
description: "この記事では、Campaignリストページでキャンペーンを検索するさまざまな方法について説明します。"
tool:
  - Campaigns

---

# Campaignの検索 {#search-for-campaigns}

> ワークスペースでCampaignを作成していくにつれて、Campaignリストのフィルターや列を調整して、Campaignの並べ替えや整理ができます。これらの検索方法を組み合わせることで、特にCampaignのリストが増えてきた場合に、結果を絞り込むことができます。

Campaignリストページでは、以下を選択してCampaignを検索できます。

- ステータス
- タグ
- フィルター
- 列

検索バーを使用して、Campaign名に関連するキーワードやフレーズを入力できます。完全一致検索を行うには、検索フレーズを引用符（""）で囲みます。たとえば、Webhookテストキャンペーンを具体的に検索するには、検索バーに `"webhook test"` と入力します。

![3つのCampaignが表示されたCampaignリストページ。アクティブなCampaignを表示するように整理されています。ビューを整理するために、名前、ステータス、停止日、Campaignタイプ、送信先の列が表示されています。]({% image_buster /assets/img/campaign_list_example.png %})

## ステータスの選択 {#selecting-a-status}

デフォルトでは、CampaignリストにはアクティブなCampaignとアイドル状態のCampaignが表示されます。ドロップダウンを選択して、ステータス別（アクティブ、下書き、アーカイブ、停止、アイドル）にCampaignを表示できます。

たとえば、Campaignの下書きを確認したい場合は、**ステータス** > **下書き**を選択して、Campaignリストを絞り込みます。

### タグによる検索 {#searching-by-tags}

[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)でCampaignを検索すると、結果をさらに絞り込むことができます。たとえば、新規顧客、リピーター、離脱顧客をターゲットにするために作成したすべてのCampaignを見つけたい場合、共通のタグ**顧客タイプ別ターゲティング**でこれらのCampaignを検索できます。

### フィルターの調整 {#adjusting-filters}

フィルターを使用して、以下のCampaign詳細で結果をグループ化できます。

- Campaignタイプ
- Campaignの作成者
- Campaignの最終編集者
- エントリスケジュール
- ターゲットSegment
- チーム
- インタラクションデータが期限切れのCampaign

また、Campaignが最後に作成された日付や最終編集された日付の範囲を選択して検索することもできます。これは、プロモーション期間中に使用されたCampaignを検索する場合に特に便利です。

### 列の整理 {#organizing-columns}

**列**を選択すると、該当するチェックボックスを選択して、CampaignリストページのCampaign詳細の表示情報を調整できます。たとえば、マーケティングチームによるアクションベースのWebhook Campaignのみを表示するようにCampaignリストを設定したい場合は、**Campaignタイプ**、**エントリスケジュール**、**チーム**を列として選択します。