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

計算式は、データに存在する複雑な関係を理解するのに役立ちます。例えば、特定のセグメントに該当する日次アクティブユーザーが完了したカスタムイベントの数を、一般層（または他のセグメント）と比較できます。

## ユースケース {#use-cases}

数式は、特にカスタムイベントと組み合わせることで、アプリ内でのユーザーの行動を理解するのに役立ちます。また、数式を使用すると、Google 広告やテレビなどの有料メディアをBrazeと併用している場合でも、セグメントの購買パターンについてより深いインサイトを得ることができます。

以下は、数式を使用して検出できる行動パターンの例です。

- **ライドシェアアプリ:** ユーザーが乗車をキャンセルしたときのカスタムイベントがある場合、キャンセルされた乗車数 / DAU の関数を設定して、特定のユーザーセグメントが他のセグメントよりも多く乗車をキャンセルする傾向があるかどうかを確認できます。
- **eコマースアプリ:** 特定の商品 ID の購入数 / MAU の関数を設定することで、すべてのプロモーションがBrazeでトラッキングできなかった場合でも、最近プロモーションされた商品の人気度をセグメント間で比較できます。
- **広告を使用するメディアアプリ:** 動画や音声クリップの間に広告が挿入されてユーザー体験が中断される場合、広告途中の離脱をカスタムイベントとして記録し、広告途中の離脱数 / DAU の比率を計算することで、広告なしのプレミアム購読キャンペーンのターゲットに最適なセグメントを見つけるのに役立ちます。

## 数式の作成 {#creating-formulas}

数式は、ダッシュボードの[ホーム]({{site.baseurl}}/user_guide/analytics/dashboards/home)、[収益レポート]({{site.baseurl}}/user_guide/analytics/reports/revenue_report)、[カスタムイベントレポート]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)ページからアクセスできます。**ホーム**および**収益レポート**では、**経時パフォーマンス**チャートを開き、**統計の対象**を**KPI数式**に設定して、少なくとも1つの数式を選択します。**カスタムイベントレポート**ページでは、**フィルター**を開き、1つ以上の**KPI数式**オプションを選択して、**適用**を選択します。

![BrazeダッシュボードでKPI数式の統計を表示する]({% image_buster /assets/img_archive/kpi_forms.png %})

新しい数式を作成するには:

1. 適切なダッシュボード（**ホーム**、**収益レポート**、または**カスタムイベントレポート**）に移動します。
2. **KPI数式を管理**を選択します。
3. 数式の名前を入力します。
4. 関連する分子と分母を選択します。
5. **保存**を選択します。

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
| 特定の購入（ギフトカードや商品IDなど） | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="収益ダッシュボード" }

### カスタムイベントダッシュボード {#custom-event-dashboard}

| 分子 | 分母 |
| --- | --- |
| カスタムイベント数 | MAU |
|  | DAU |
|  | セグメントサイズ（[分析トラッキング]({{site.baseurl}}/viewing_and_understanding_segment_data)が有効になっているセグメントのみ使用できます） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムイベントダッシュボード" }