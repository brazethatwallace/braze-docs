---
nav_title: Analyze
article_title: Operator Analyze
page_order: 100
description: "Ask plain-language questions about your channel engagement, attributed revenue, and how you compare to industry benchmarks. You get charts, comparisons, and actionable insights in seconds."
page_type: reference
hidden: true
---

# Operator Analyze

> Operator Analyze answers plain-language performance questions in BrazeAI Operator<sup>TM</sup>. Responses include charts, comparisons, and short insights. You do not need to build a dashboard or pull a full report first.

{% alert important %}
Operator Analyze is currently in beta. Capabilities and supported analyses are evolving. To request access for your account, reach out to your Customer Success Manager.
{% endalert %}

## Why use Operator Analyze?

Most performance questions still require switching tools, building views, or waiting on someone else. Examples include "How did last week go", "Are we tracking against the benchmark", and "Which campaign is driving the strongest results?"

Operator Analyze covers engagement metrics, *Attributed Revenue*, and industry benchmarks. That is the same data you would otherwise pull into a report or dashboard. Ask in your own words from the Operator panel. You get a chart, ranked comparison, or table plus one to five actionable insights.

## Access Operator Analyze

Operator Analyze runs in the Operator conversation panel.

1. Select **BrazeAI Operator<sup>TM</sup>** next to your user profile from any page in the Braze dashboard.
2. Ask about channel engagement or benchmark comparisons (see [Example questions](#example-questions)).
3. Operator returns the answer and, when helpful, a chart or table and a short list of insights.

For more information about the Operator chat panel, see [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/).

## Example questions

Describe what you want to know. No fixed phrasing is required. Select a tab for sample prompts.

{% tabs %}
{% tab Benchmark comparisons %}

* "How does our email *Open Rate* compare to industry benchmarks for the last 30 days?"
* "Are we above or below the benchmark for SMS *Click-Through Rate* this quarter?"
* "Where are we underperforming the industry across our channel mix?"

{% endtab %}
{% tab Channel overviews %}

* "Which channels are performing best for us in FY26 to date?"
* "Break down engagement by channel for the last 90 days."
* "How much *Attributed Revenue* did each marketing channel drive last quarter?"

{% endtab %}
{% tab Campaign and Canvas drill-downs %}

* "What are our top 10 email campaigns by *Click-Through Rate* this fiscal quarter?"
* "Which Canvases drove the most *Clicks* last month?"
* "Which campaigns generated the most *Attributed Revenue* in FY26 Q1?"
* "Show our worst-performing push campaigns over the last 30 days."

{% endtab %}
{% tab Trend analysis %}

* "What's the month-over-month trend in push engagement for FY26?"
* "How has email *Click-Through Rate* changed quarter-over-quarter over the last year?"
* "How has our *Attributed Revenue* trended over the last 12 months?"
* "Show me our weekly engagement trend for in-app messages over the last 90 days."

{% endtab %}
{% tab Revenue and conversions %}

Ask about *Attributed Revenue* and *Conversions* aggregated to the campaign, Canvas, channel, or program level.

* "Compare *Attributed Revenue* and *Conversions* for the most recent quarter against the prior quarter."
* "Which campaigns drove the most *Attributed Revenue* in the last 90 days?"
* "Break down *Attributed Revenue* by channel for FY26 to date."

{% endtab %}
{% tab Comprehensive reviews %}

* "Give me a full review of our engagement program with recommendations."
* "Where are our biggest opportunities and risks across channels right now?"

{% endtab %}
{% endtabs %}

## Visualizations

Operator adds a chart when the data supports it. **Line charts** suit time series, **bar charts** suit category comparisons, and **tables** cover other cases. Tables show percentages to two decimal places and use commas for large numbers.

When a response includes multiple metrics, Operator prioritizes engagement rates (*Open Rate*, *Click Rate*, *Push Open Rate*) over raw counts.

## Supported channels and metrics

*Attributed Revenue* and *Conversions* use the same campaign, Canvas, channel, and program aggregation shown under [Example questions](#example-questions) in the **Revenue and conversions** tab.

| Channel | Metrics | Industry benchmarks |
| --- | --- | --- |
| Email | *Sends*, *Deliveries*, *Unique Opens*, *Unique Clicks*, *Unsubscribes* | Yes |
| Push (iOS, Android, Web) | *Sends*, *Deliveries*, *Opens* | Yes |
| SMS | *Sends*, *Deliveries*, *Link Clicks* | Yes |
| In-App Messages | *Impressions*, *Clicks* | Yes |
| Content Cards | *Sends*, *Impressions*, *Clicks* | Yes |
| WhatsApp | *Sends*, *Deliveries*, *Reads*, *Clicks* | Not yet |
| RCS | *Sends*, *Deliveries*, *Reads*, *Clicks* (including text URL, button, action, reply action, and reply button sub-types) | Not yet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported channels, metrics, and benchmark availability" }

{% alert tip %}
Operator uses unique counts for rates (for example, *Unique Opens* divided by *Deliveries* for *Email Open Rate*). If a figure differs from a dashboard, compare attribution window, time range, and definition. Operator lists all three in each response.
{% endalert %}

## Time periods and attribution windows

### Fiscal year vs. calendar year

Operator Analyze defaults to the **Braze fiscal year**, which runs February 1 through January 31.

| Fiscal quarter | Months |
| --- | --- |
| FQ1 | Feb – Apr |
| FQ2 | May – Jul |
| FQ3 | Aug – Oct |
| FQ4 | Nov – Jan |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze fiscal quarters and calendar months" }

For calendar-year questions, include "CY", "calendar year", or "standard year". Ambiguous "last year" prompts Operator to confirm which calendar you mean.

You can also use ISO-style ranges such as `Q4 2025` or `2025-03-01 to 2025-05-31`.

### Attribution windows

Operator Analyze defaults to **7 days**. Name a window in your question to override:

* **1-day** for quick engagement checks
* **3-day** for short-cycle campaigns
* **7-day** for general overviews and campaign reads (default)
* **30-day** for strategic or long-range views
* **All windows** for a 1D / 3D / 7D / 30D side-by-side comparison

If results differ by more than 50% across windows, Operator shows all four side by side.

## Data freshness

Data refreshes daily. Same-day activity appears after the next refresh. Each response states the latest date in the dataset. If that date looks stale, contact your Customer Success Manager.

## What's out of scope

* **Product-level performance breakdowns.** *Attributed Revenue* and engagement roll up to the campaign, Canvas, channel, or program level. They do not break out to products or SKUs. Product- or SKU-level questions are not supported. Reach out to your Customer Success Manager for those analyses.
* **Industry benchmarks for WhatsApp and RCS.** Engagement metrics for both channels are supported. Benchmarks are not available yet.

Out-of-scope questions get a direct answer, a suggested alternative where possible, or a pointer to your Customer Success Manager.

## Tips for better results

* **Time range:** Prefer explicit ranges ("FY26 Q2", "the last 90 days") over vague phrases like "last quarter" when you need precision.
* **Metrics:** Name the rate you care about (*Open Rate*, *Click-Through Rate*, *Click-to-Open Rate*). Operator reports the formula it used.
* **Follow-ups:** Drill into a result, change the window, or switch channels. Operator keeps context across the thread.
* **Channel wording:** WhatsApp and RCS use *Read Rate* (not *Open Rate*). SMS uses *Link Click Rate*.
* **Combined asks:** Benchmark plus trend in one prompt is supported.

## Data privacy and security

Operator Analyze follows the same privacy and security model as BrazeAI Operator<sup>TM</sup>. For more information, see [Data privacy and security]({{site.baseurl}}/user_guide/brazeai/operator/#data-privacy-and-security).

## Next steps

* [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)
* [Review actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)
