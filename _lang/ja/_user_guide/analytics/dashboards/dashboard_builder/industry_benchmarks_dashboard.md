---
nav_title: 業界ベンチマークダッシュボード
article_title: 業界ベンチマークダッシュボード
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "この記事では、業界ベンチマークダッシュボードの概要を説明します。"
---

# 業界ベンチマークダッシュボード {#industry-benchmarks-dashboard}

> **業界ベンチマーク**ダッシュボードは、ワークスペースのエンゲージメントパフォーマンスを、各業界の同業他社から集計されたプライバシーに配慮したベンチマークと比較します。

**業界ベンチマーク**ダッシュボードを使用して、メール、プッシュ通知、Content Cards、SMSのパフォーマンスを業界の同業他社と比較し、最適化の機会があるチャネルや地域を特定できます。

**業界ベンチマーク**ダッシュボードを表示するには、**Analytics** > **ダッシュボードビルダー**に移動し、**Industry Benchmarks**を選択します。ダッシュボードにデータがない場合は、**Run Dashboard**を選択して最新の結果を生成します。ダッシュボード上部のフィルターを使用して、業界バーティカルや期間で結果を絞り込みます。

## ダッシュボードについて {#about-the-dashboard}

ダッシュボードは、**メール**、**プッシュ通知**、**Content Cards**、**SMS** の4つのチャネルセクションで構成されています。

| セクション              | 説明                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| KPIカード            | ワークスペースの各主要指標の率を、業界平均との差分とともに表示します。緑色の上向き矢印はワークスペースの値が業界平均より高いことを示し、赤色の下向き矢印は低いことを示します。 |
| 月次トレンドチャート  | ワークスペースの率と業界平均の率を時系列でプロットし、季節性や長期的なトレンドを把握できます。                                   |
| 地域別内訳   | ワークスペースの率と業界平均の率を地域ごとに分解し、地域別のパフォーマンスが業界平均とどこで乖離しているかを確認できます。         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="セクション" }

すべてのチャートにおいて、薄い色の系列は業界ベンチマークを表し、濃い色の系列（先頭に **Workspace** と表示）はご自身のパフォーマンスを表します。

## 利用可能な指標 {#available-metrics}

チャネルベースの各指標は、2つのタイプで利用できます。

| 指標タイプ     | 説明                           | 例                                              |
|----------|---------------------------------------|------------------------------------------------------|
| _合計_  | すべてのエンゲージメントイベントをカウントします。        | ユーザーが3回クリックした場合、3回のクリックとしてカウントされます。 |
| _ユニーク_ | ユニークユーザーをカウントします。                  | ユーザーが3回クリックした場合、1回のクリックとしてカウントされます。   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="指標タイプ" }

指標は、業種、地域、サブ業種、日付の以下の組み合わせでグループ化されます。

- 業種 + 日付
- 業種 + 地域 + 日付
- 業種 + サブ業種 + 地域 + 日付

タブを選択して、各チャネルの指標を表示します。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab メール %}

<table aria-label="メール指標"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>ユニーク開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} この率にはマシンオープンは含まれません。</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>ユニーククリック率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>ユニーククリック・トゥ・オープン率</i></td><td class="no-split">メールを開封した後にクリックしたユーザーの割合です。</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="メール指標" }

![折れ線グラフと棒グラフで表示されたメール業界ベンチマーク指標。]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab プッシュ %}

プッシュ指標は、iOS、Android、Web、およびすべてのプラットフォームの合計で利用できます。

<table aria-label="プッシュ指標"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>直接開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>影響を受けた開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>合計開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="プッシュ指標" }

![折れ線グラフと棒グラフで表示されたプッシュ業界ベンチマーク指標。]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="SMS指標"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>配信率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>短縮リンククリック率</i></td><td class="no-split">SMSを受信した後に短縮リンクをクリックしたユーザーの割合です。</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS指標" }

![折れ線グラフと棒グラフで表示されたSMS業界ベンチマーク指標。]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Content Cards指標"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>クリック率</i></td><td class="no-split">Content Cardsを受信し、リンクをクリックしたユーザーの割合です。</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Cards指標" }

![折れ線グラフと棒グラフで表示されたContent Cards業界ベンチマーク指標。]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## 方法論 {#methodology}

Brazeベンチマークは、安定した代表的な数値を算出するために設計された3ステップのプロセスで計算されます。

### ステップ1：ダイナミックサンプリング {#step-1-dynamic-sampling}

Brazeはすべてのデータポイントを分析するのではなく、代表的なサンプルを選択します。このサンプリング手法では、小規模なユーザーグループを十分に代表できるようオーバーサンプリングを行い、少数の非常に大規模な企業が業界全体の結果を歪めないよう企業規模に応じた調整を行います。

### ステップ2：外れ値の除去 {#step-2-outlier-removal}

Brazeは統計的な外れ値を特定し、除去します。これにより、平均パフォーマンス率への影響を最小限に抑えながら、データのボラティリティを大幅に低減します。つまり、基礎となるトレンドを変えることなく異常値が除去されます。

### ステップ3：事後層化ウェイティング {#step-3-post-stratification-weighting}

サンプルは実際の母集団を反映するようにウェイト付けされます。サンプリングで残った不均衡を補正するためにサブグループにウェイトが適用され、代表的で偏りのない最終的なベンチマークが算出されます。

## データガバナンス {#data-governance}

- **更新サイクル:** データは毎月5日に更新され、前月末までの最新データが反映されます。
- **プライバシー:** すべてのベンチマークは集計され、ユーザー情報を保護するために匿名化されています。