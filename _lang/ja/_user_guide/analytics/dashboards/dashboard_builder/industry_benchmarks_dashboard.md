---
nav_title: 業界ベンチマークダッシュボード
article_title: 業界ベンチマークダッシュボード
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "この記事では、業界ベンチマークダッシュボードの概要を説明します。"
hidden: true
noidex: true
---

# 業界ベンチマークダッシュボード {#industry-benchmarks-dashboard}

> **業界ベンチマーク**ダッシュボードは、ワークスペースのエンゲージメントパフォーマンスを、各業界の同業他社から集計されたプライバシーに配慮したベンチマークと比較します。

**業界ベンチマーク**ダッシュボードを使用して、メール、プッシュ通知、Content Cards、SMSのパフォーマンスを業界の同業他社と比較し、最適化の機会があるチャネルや地域を特定できます。

**業界ベンチマーク**ダッシュボードを表示するには、**Analytics** > **ダッシュボードビルダー**に移動し、**Industry Benchmarks**を選択します。ダッシュボードにデータがない場合は、**Run Dashboard**を選択して最新の結果を生成します。ダッシュボード上部のフィルターを使用して、業界バーティカルや期間で結果を絞り込みます。

{% alert note %}
**業界ベンチマーク**ダッシュボードは現在、早期アクセス段階です。早期アクセスへの参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## ダッシュボードについて {#about-the-dashboard}

ダッシュボードは4つのチャネルセクションに分かれています：**Email**、**Push Notification**、**Content Card**、**SMS**：

| セクション | 説明 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| KPIカード | ワークスペースの各主要指標のレートと、業界レートとの差分を表示します。緑色の上向き矢印はワークスペースが業界レートを上回っていることを示し、赤色の下向き矢印は下回っていることを示します。 |
| 月次トレンドチャート | ワークスペースのレートと業界レートを時系列でプロットし、季節性や長期的なトレンドを特定できます。 |
| 地域別内訳 | ワークスペースのレートと業界レートを地域別に分解し、地域ごとのパフォーマンスが業界と乖離している箇所を特定できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Section" }

すべてのチャートにおいて、薄い色のシリーズは業界ベンチマークを表し、濃い色のシリーズ（**Workspace**のプレフィックス付き）は自社のパフォーマンスを表します。

## 利用可能な指標 {#available-metrics}

各チャネルベースの指標は2つのタイプで利用できます：

| 指標タイプ | 説明 | 例 |
|----------|---------------------------------------|------------------------------------------------------|
| _合計_ | すべてのエンゲージメントイベントをカウントします。 | ユーザーが3回クリックした場合、3クリックとしてカウントされます。 |
| _ユニーク_ | ユニークユーザーをカウントします。 | ユーザーが3回クリックした場合、1クリックとしてカウントされます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metric type" }

指標は、業界、地域、サブ業界、日付の以下の組み合わせでグループ化されます：

- 業界 + 日付
- 業界 + 地域 + 日付
- 業界 + サブ業界 + 地域 + 日付

タブを選択して、各チャネルの指標を表示します。

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab メール %}

<table aria-label="Email metrics"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>ユニーク開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} このレートはマシンオープンを除外しています。</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>ユニーククリック率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>ユニーククリック・トゥ・オープン率</i></td><td class="no-split">メールを開封した後にクリックしたユーザーの割合です。</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Email metrics" }

![メールの業界ベンチマーク指標が折れ線グラフと棒グラフで表示されています。]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab プッシュ %}

プッシュ指標は、iOS、Android、Web、およびすべてのプラットフォームの合計で利用できます。

<table aria-label="Push metrics"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>直接開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>影響開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>合計開封率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push metrics" }

![プッシュの業界ベンチマーク指標が折れ線グラフと棒グラフで表示されています。]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="SMS metrics"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>配信率</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>短縮リンククリック率</i></td><td class="no-split">SMSを受信した後に短縮リンクをクリックしたユーザーの割合です。</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS metrics" }

![SMSの業界ベンチマーク指標が折れ線グラフと棒グラフで表示されています。]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Content Cards metrics"><thead><tr><th>指標</th><th>説明</th><th>計算式</th></tr></thead><tbody>
<tr><td class="no-split"><i>クリック率</i></td><td class="no-split">Content Cardsを受信し、リンクをクリックしたユーザーの割合です。</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Cards metrics" }

![Content Cardsの業界ベンチマーク指標が折れ線グラフと棒グラフで表示されています。]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## 方法論 {#methodology}

Brazeのベンチマークは、安定した代表的な数値を生成するために設計された3ステップのプロセスで計算されます。

### ステップ 1: ダイナミックサンプリング {#step-1-dynamic-sampling}

すべてのデータポイントを分析するのではなく、Brazeは代表的なサンプルを選択します。サンプリング方法は、適切な代表性を確保するために小規模なユーザーグループをオーバーサンプリングし、少数の非常に大きな企業が業界全体の結果を歪めないように企業規模を調整します。

### ステップ 2: 外れ値の除去 {#step-2-outlier-removal}

Brazeは統計的な外れ値を特定して除去します。これにより、平均パフォーマンスレートへの影響を最小限に抑えながら、データのボラティリティを大幅に低減します。つまり、基礎となるトレンドを変えることなく異常値が除去されます。

### ステップ 3: 事後層化重み付け {#step-3-post-stratification-weighting}

サンプルは実際の母集団を反映するように重み付けされます。サンプリングから残った不均衡を修正するためにサブグループに重みが適用され、代表的で偏りのない最終的なベンチマークが生成されます。

## データガバナンス {#data-governance}

- **更新サイクル:** データは毎月5日に更新され、前月末までのデータが反映されます。
- **プライバシー:** すべてのベンチマークは集計され、ユーザー情報を保護するために匿名化されています。