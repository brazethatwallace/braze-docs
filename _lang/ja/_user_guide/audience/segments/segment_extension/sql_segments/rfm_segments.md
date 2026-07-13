---
nav_title: "RFMセグメント"
article_title: RFM SQLセグメントエクステンション
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "この記事では、購買行動を測定して優良ユーザーを特定するRFMセグメントエクステンションの作成方法について説明します。"
tool: Segments
---

# RFM SQLセグメント {#rfm-sql-segments}

> RFM（Recency、Frequency、Monetary）セグメントエクステンションを作成して、購買行動を測定することで優良ユーザーをターゲットにできます。

RFM分析は、各カテゴリ（Recency、Frequency、Monetary）について0〜3のスケールでユーザーをスコアリングし、優良ユーザーを特定するマーケティング手法です。3が最高スコア、0が最低スコアです。Recency、Frequency、Monetaryの値はすべて、選択した特定の時間範囲のデータに基づいています。

## RFMカテゴリ {#rfm-categories}

| カテゴリ | 定義 |
| --- | --- |
| Recency | 顧客が最後に購入してからの経過時間です。スコアが高いほど、最近購入したことを意味します。 |
| Frequency | 顧客が購入した頻度です。スコアが高いほど、購入頻度が高いことを意味します。 |
| Monetary value | 顧客が支出した合計金額です。スコアが高いほど、支出額が多いことを意味します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RFMカテゴリ" }

{% alert note %}
RFM SQLセグメントを使用するには、購入イベントを有効にする必要があります。ユーザーのMonetary値は、Brazeの購入イベントを通じて生成された収益によって決定されるためです。
{% endalert %}

## RFMセグメントの作成 {#creating-an-rfm-segment}

1. **オーディエンス** > **セグメントエクステンション**に移動します。
2. **新しいエクステンション**を選択し、**Recency, frequency, and monetary value (RFM) segment**を選択します。

![カタログセグメント、イベント、購入、またはRFMセグメントを作成するオプションを含むモーダル。]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3. **Variables**パネルで、**Time Range**を選択して、分析する購入データの期間を指定します。過去最大60日間まで指定できます。選択した時間範囲は、ユーザー行動データが取得される期間であり、キャンペーンの目標に応じて異なります。

| 時間範囲フィールド | 説明 | ユースケース |
| --- | --- | --- |
| Relative | 過去X日間のアクティビティを指定します | ローリングウィンドウで最新のユーザー行動を分析します。 |
| Start date | 分析の固定開始日を指定します | キャンペーン開始後など、特定の日付以降のユーザーアクティビティを分析します。 |
| End date | 分析の固定終了日を指定します | 製品アップデート前など、特定の日付までのユーザーアクティビティを分析します。 |
| Date range | カスタム期間の開始日と終了日の両方を指定します | プロモーションイベントなど、定義された期間中のユーザー行動を分析します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RFMセグメントの作成" }

{: start="4"}
4. セグメントに含める生成済みの[RFMグループ](#rfm-groups)を選択します。複数のグループを選択した場合、選択したグループのいずれかに属するユーザーがセグメントに含まれます。

![「Champions」と「Loyal Users」のRFMグループが選択されたVariablesパネル。]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5. プレビューを実行し、セグメントを保存します。

{% alert note %}
RFMセグメントを作成するために、テンプレート内のSQLコードを編集する必要はありません。**Variables**パネルのみを使用してセグメントをカスタマイズできます。
{% endalert %}

### RFMグループ {#rfm-groups}

RFMセグメントは特定の順序で評価されます。ユーザーは、優先順位リストの上位から順に、基準を満たす最初のセグメントに割り当てられます。たとえば、「Champions」と「Loyal Users」の両方に該当するユーザーは、優先度が高い「Champions」セグメントに割り当てられます。

| RFMグループ | セグメントの説明 | Recency (R) ランク | Frequency (F) ランク | Monetary (M) ランク |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions          | すべてのカテゴリでトップスコアを持つ、最も価値の高いユーザーセグメントです。                   | 3                | 2-3                | 2-3               |
| Loyal Users        | Recencyが高く、Frequencyも高いユーザーです。ChampionsよりもMonetary値が低い場合があります。 | 2-3              | 2-3                | 1-3               |
| Potential Loyalists| 最近購入し、中程度のFrequencyとMonetary値を持つユーザーです。   | 3                | 1-3                | 1-3               |
| Promising          | 最近、高額の初回購入を行ったが、まだ高い購入頻度を確立していないユーザーです。 | 3                | 0-3                | 1-3               |
| New Customer       | ごく最近に初回購入を行ったユーザーです。                             | 3                | 0-3                | 0-3               |
| Needing Attention  | Recencyは平均以上だが、購入頻度またはMonetary値が平均以下のユーザーです。 | 2-3              | 0-3                | 0-3               |
| Cannot lose them   | 以前は高い価値を持ち、FrequencyとMonetaryのスコアも良好だったが、長期間購入していないユーザーです。 | 0-1              | 2-3                | 2-3               |
| At Risk            | 過去に中程度のFrequencyとMonetaryスコアを持っていたが、長期間購入していないユーザーです。 | 0-1              | 1-3                | 1-3               |
| About to Sleep     | すべての指標で低いスコアを持つユーザーです。                                       | 1                | 0-3                | 0-3               |
| Hibernating        | 中程度のFrequencyを持つが、長期間非アクティブなユーザーです。    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="RFMグループ" }