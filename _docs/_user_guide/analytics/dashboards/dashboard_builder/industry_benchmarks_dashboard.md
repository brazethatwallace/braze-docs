---
nav_title: Industry Benchmarks dashboard
article_title: Industry Benchmarks dashboard
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "This article provides an overview of the Industry Benchmarks dashboard."
---

# Industry Benchmarks dashboard

> The **Industry Benchmarks** dashboard compares your workspace's engagement performance against aggregated, privacy-conscious benchmarks from peer companies in each industry.

Use the **Industry Benchmarks** dashboard to compare your email, push, Content Card, and SMS performance to industry peers and to identify channels and regions where there are opportunities to optimize.

To view the **Industry Benchmarks** dashboard, go to **Analytics** > **Dashboard Builder**, then select **Industry Benchmarks**. If the dashboard has no data, select **Run Dashboard** to generate the latest results. Use the filters at the top of the dashboard to refine results by industry vertical or timeframe.

## About the dashboard

The dashboard is organized into four channel sections: **Email**, **Push Notification**, **Content Card**, and **SMS**:

| Section              | Description                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| KPI cards            | Show your workspace's rate for each key metric, along with the delta compared to the industry rate. A green up arrow indicates your workspace is higher than the industry rate; a red down arrow indicates it is lower. |
| Monthly trend chart  | Plots your workspace rate against the industry rate over time, so you can identify seasonality and longer-term trends.                                   |
| Regional breakdown   | Breaks down your workspace rate against the industry rate across regions, so you can spot where regional performance diverges from the industry.         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Section" }

In every chart, the lighter-colored series represents the industry benchmark and the darker series (prefixed with **Workspace**) represents your own performance.

## Available metrics

Each channel-based metric is available in two types:

| Metric type     | Description                           | Example                                              |
|----------|---------------------------------------|------------------------------------------------------|
| _Total_  | Counts every engagement event.        | If a user clicks three times, that is counted as three clicks. |
| _Distinct_ | Counts unique users.                  | If a user clicks three times, that is counted as one click.   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metric type" }

Metrics are grouped by the following combinations of industry, region, sub-industry, and date:

- Industry + Date
- Industry + Region + Date
- Industry + Sub-Industry + Region + Date

Select a tab to view metrics for each channel.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab Email %}

<table aria-label="Email metrics"><thead><tr><th>Metric</th><th>Description</th><th>Formula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Unique Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} This rate excludes machine opens.</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Unique Click Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Unique Click to Open Rate</i></td><td class="no-split">The percentage of users who clicked an email after opening it.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Email metrics" }

![Email industry benchmarks metrics displayed in line graphs and bar graphs.]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab Push %}

Push metrics are available for iOS, Android, Web, and across all platforms combined.

<table aria-label="Push metrics"><thead><tr><th>Metric</th><th>Description</th><th>Formula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Direct Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Influenced Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Total Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push metrics" }

![Push industry benchmarks metrics displayed in line graphs and bar graphs.]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="SMS metrics"><thead><tr><th>Metric</th><th>Description</th><th>Formula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Delivery Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Short Link Click Rate</i></td><td class="no-split">The percentage of users who clicked a short link after receiving an SMS.</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS metrics" }

![SMS industry benchmarks metrics displayed in line graphs and bar graphs.]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Content Cards metrics"><thead><tr><th>Metric</th><th>Description</th><th>Formula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Click Rate</i></td><td class="no-split">The percentage of users who received a Content Card and clicked a link.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Cards metrics" }

![Content Cards industry benchmarks metrics displayed in line graphs and bar graphs.]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## Methodology

Braze benchmarks are calculated using a three-step process designed to produce stable, representative figures.

### Step 1: Dynamic sampling

Rather than analyzing every data point, Braze selects a representative sample. The sampling method over-samples smaller user groups for adequate representation and adjusts for company size so that a small number of very large companies don't skew the results for an entire industry.

### Step 2: Outlier removal

Braze identifies and removes statistical outliers. This significantly reduces volatility in the data with minimal impact on average performance rates, meaning anomalies are removed without changing the underlying trends.

### Step 3: Post-stratification weighting

The sample is weighted to mirror the real-world population. Weights are applied to subgroups to correct any imbalances left over from sampling, resulting in final benchmarks that are representative and unbiased.

## Data governance

- **Refresh cycle:** Data refreshes monthly on the 5th of every month and is current through the last completed month.
- **Privacy:** All benchmarks are aggregated and de-identified to protect user information.
