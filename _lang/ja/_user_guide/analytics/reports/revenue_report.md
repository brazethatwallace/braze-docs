---
nav_title: 収益レポート
article_title: 収益レポート
page_order: 7
page_type: reference
description: "このページでは、収益レポートページを使用して、特定の期間の収益データ、特定の製品の収益、およびアプリの総収益を表示する方法について説明します。"
tool: Reports
---

# 収益レポート {#revenue-report}

> **収益レポート**ページでは、特定の期間の収益データ、特定の製品の収益、およびアプリの総収益を表示できます。

ダッシュボードから収益レポートを表示するには、**Analytics** > **収益レポート**に移動します。

## 収益レポートのカスタマイズ {#customizing-your-revenue-report}

日付範囲、レポート対象のアプリ、およびパラメーターを選択して、収益レポートをカスタマイズできます。

![パラメーターに「収益」が設定された「経時パフォーマンス」グラフを表示する「収益レポート」ページ。]({% image_buster /assets/img/revenue_report.png %})

### 日付とアプリによるフィルタリング {#filtering-by-date-and-apps}

収益レポートの日付範囲を選択し、必要に応じて特定のアプリまたは複数のアプリを選択します。

### パラメーターによるフィルタリング {#filtering-by-parameters}

**Performance Over Time**グラフには、さまざまなパラメーターのデータが表示されます。パラメーターは**Statistics for**ドロップダウンで選択できます。オプションで、**Breakdown**ドロップダウンで特定のパラメーターのデータを分類できます。

**Performance Over Time**グラフでは、以下のデータを表示できます。
- KPI計算式
- 購入
    - （オプション）製品別購入
- 収益
    - （オプション）セグメント別収益
    - （オプション）製品別収益
- 時間あたりの収益
    - （オプション）セグメント別の時間あたりの収益
- ユーザーあたりの収益

## 収益計算の理解 {#understanding-revenue-calculations}

{% alert note %}
為替レートのない通貨で収益を記録した場合、Brazeはそれを0.00米ドルの購入として記録します。
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="収益計算の理解">
  <caption>収益計算の理解</caption>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">ライフタイム収益</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">ユーザーあたりのライフタイムバリュー</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='LTV Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">1日あたりの平均収益</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">1日あたりの購入数</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">ユーザーあたりの1日の収益</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## 製品内訳の表示 {#viewing-the-product-breakdown}

**Product Breakdown**テーブルを参照すると、選択した日付範囲内に購入された製品の一覧、各製品の購入数、および各製品が生み出した収益を確認できます。

![「Product Name」、「Purchased」、「Revenue」の列を表示する「Product Breakdown」テーブル。]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## 収益データのエクスポート {#exporting-revenue-data}

収益データをエクスポートするには、**Performance Over Time**グラフの<i class="fas fa-bars" title="チャートコンテキストメニュー"></i> **チャートコンテキストメニュー**を選択し、エクスポートオプションを選択します。

{% alert tip %}
収益データを取得する他の方法をお探しですか？購入行動（および製品の購入）を[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)としてキャンペーンやキャンバスに追加してみてください。
{% endalert %}

また、[キャンペーン分析]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)ページや[キャンバス分析]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)ページで、ケースバイケースで収益統計を確認することもできます。

{% alert tip %}
収益レポートはAPIを通じてエクスポートできません。CSVエクスポートについては、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を参照してください。
{% endalert %}