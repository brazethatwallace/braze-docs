---
nav_title: 計算式を作成する
article_title: 計算式を作成する
page_order: 3
page_type: reference
description: "このリファレンス記事では、計算式の作成と管理について説明します。計算式は、データ内に存在する複雑な関係を簡単に把握するうえで役立ちます。"
tool: Reports

---
# 計算式を作成する {#create-a-formula}

> Brazeで分析を確認する際、複数のデータポイントを組み合わせてユーザーデータに関する貴重なインサイトを得ることができます。これらは計算式と呼ばれます。計算式を使用して、月間アクティブユーザー（MAU）と日次アクティブユーザー（DAU）の総数に基づいて時系列データを正規化します。

計算式は、データに存在する複雑な関係を理解するのに役立ちます。例えば、特定のSegmentに該当する日次アクティブユーザーが完了したカスタムイベントの数を、一般層（または他のSegment）と比較できます。

## ユースケース {#use-cases}

計算式は、特にカスタムイベントと組み合わせることで、アプリ内のユーザー行動を理解するのに役立ちます。また、Google 広告やテレビなどの有料メディアをBrazeとともに使用している場合でも、計算式によりSegmentの購入パターンについてより深いインサイトが得られます。

以下に、計算式を使用して検出できる行動パターンの例をいくつか示します。

- **ライドシェアアプリ:** ユーザーが乗車をキャンセルしたときのカスタムイベントがある場合、キャンセルされた乗車数 / DAUの関数を設定して、特定のユーザーSegmentが他よりも多くの乗車をキャンセルする傾向があるかどうかを確認できます。
- **eコマースアプリ:** 特定の商品ID / MAUの購入に対する関数を設定することで、すべてのプロモーションをBrazeで追跡できなくても、最近プロモーションした商品の人気をSegment間で比較することができます。
- **広告を使用したメディアアプリ:** ユーザー体験が動画やオーディオクリップの間にある広告によって中断される場合、広告途中の離脱をカスタムイベントとして記録し、広告途中の離脱 / DAUの比率を計算することで、広告なしのプレミアムサブスクリプションのCampaignでターゲットにする最適なSegmentを見つけることができます。

## 計算式の作成 {#creating-formulas}

計算式には、ダッシュボードの[ホーム]({{site.baseurl}}/user_guide/analytics/dashboards/home)、[収益レポート]({{site.baseurl}}/user_guide/analytics/reports/revenue_report)、[カスタムイベントレポート]({{site.baseurl}}/user_guide/data/activation/events/custom_events)の各ページにある統計パネルからアクセスできます。このパネルを表示するには、**Performance Over Time** チャートに移動し、**Statistics For** ドロップダウンを **KPI Formulas** に変更してから、少なくとも1つのKPI計算式を選択してチャートに入力します。

![BrazeダッシュボードでKPI計算式の統計を表示する]({% image_buster /assets/img_archive/kpi_forms.png %})

新しい計算式を作成するには、次の手順に従います。

1. 適切なダッシュボード（**Home**、**Revenue Report**、または **Custom Events Report**）に移動します。
2. **Manage KPI Formulas** を選択します。
3. 計算式の名前を入力します。
4. 該当する分子と分母を選択します。
5. **Save** を選択します。

## 利用可能な分子と分母 {#available-numerators-and-denominators}

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### 概要ダッシュボード {#overview-dashboard}

| 分子 | 分母 |
| --- | --- |
| DAU | MAU |
| セッション | DAU |
| | セグメントサイズ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="概要ダッシュボード" }

### 収益ダッシュボード {#revenue-dashboard}

| 分子 | 分母 |
| --- | --- |
| 購入（すべて） | DAU |
| 選択した購入（ギフトカードや商品IDなど） | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="収益ダッシュボード" }

### カスタムイベントダッシュボード {#custom-event-dashboard}

| 分子 | 分母 |
| --- | --- |
| カスタムイベント数 | MAU |
|  | DAU |
|  | セグメントサイズ（[分析トラッキング]({{site.baseurl}}/viewing_and_understanding_segment_data)が有効なSegmentのみ使用できます） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムイベントダッシュボード" }