---
nav_title: Analyze
article_title: Operator Analyze
page_order: 100
description: "Ask plain-language questions about your channel engagement, attributed revenue, and how you compare to industry benchmarks — and get back charts, comparisons, and actionable insights in seconds."
page_type: reference
hidden: true
---

# Operator Analyze

> Operator Analyze answers plain-language questions about your performance data. Instead of building a dashboard or pulling a report, you ask the question in the BrazeAI Operator<sup>TM</sup> chat panel and get back the numbers, the comparison, and a short set of actionable insights.

{% alert important %}
Operator Analyze is currently in beta. Capabilities and supported analyses are evolving. To request access for your account, reach out to your Customer Success Manager.
{% endalert %}

## Why use Operator Analyze?

Most performance questions — *how did last week go, are we tracking against the benchmark, which campaign is pulling the most weight* — usually require switching tools, building views, or waiting on someone else.

Operator Analyze reduces this effort. You ask the question in your own words, in the chat panel you already have open, and Operator returns the analysis: a chart, a ranked comparison, a table, and one to five actionable insights pointing at what to do next.

Operator Analyze focuses on performance data — engagement metrics, attributed revenue, and benchmark comparisons — that previously required building a report or dashboard.

## Access Operator Analyze

Operator Analyze runs inside the existing BrazeAI Operator chat panel — there's no separate page, button, or tool to find.

1. Select **BrazeAI Operator<sup>TM</sup>** next to your user profile from any page in the Braze dashboard.
2. Ask a question about your channel engagement performance or how you compare to industry benchmarks (see [What you can ask](#what-you-can-ask)).
3. Operator responds with the answer, a chart or table where it applies, and a short list of actionable insights.

For more on the chat panel itself, see [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/).

## What you can ask

Operator Analyze handles a range of question shapes. You don't need to phrase your question in a specific way — just describe what you want to know.

### Benchmark comparisons

Compare your performance against sub-industry peers (for example, apparel retail or quick-service restaurants — not just "retail").

* "How does our email open rate compare to industry benchmarks for the last 30 days?"
* "Are we above or below the benchmark for SMS click-through rate this quarter?"
* "Where are we underperforming the industry across our channel mix?"

### Channel overviews

See how each channel is performing relative to the others.

* "Which channels are performing best for us in FY26 to date?"
* "Break down engagement by channel for the last 90 days."
* "How much attributed revenue did each marketing channel drive last quarter?"

### Campaign and Canvas drill-downs

Surface top or bottom performers ranked by any supported metric.

* "What are our top 10 email campaigns by click-through rate this fiscal quarter?"
* "Which canvases drove the most clicks last month?"
* "Which campaigns generated the most attributed revenue in FY26 Q1?"
* "Show our worst-performing push campaigns over the last 30 days."

### Trend analysis

Track how performance has changed over time, with charts for time-series questions.

* "What's the month-over-month trend in push engagement for FY26?"
* "How has email click-through rate changed quarter-over-quarter over the last year?"
* "How has our attributed revenue trended over the last 12 months?"
* "Show me our weekly engagement trend for in-app messages over the last 90 days."

### Revenue and conversions

Ask about attributed revenue and conversions aggregated to the campaign, Canvas, channel, or program level.

* "Compare revenue and conversions for the most recent quarter against the prior quarter."
* "Which campaigns drove the most attributed revenue in the last 90 days?"
* "Break down attributed revenue by channel for FY26 to date."

### Comprehensive reviews

Get a full read on your engagement program — strengths, weaknesses, opportunities, and risks — with ranked recommendations.

* "Give me a full review of our engagement program with recommendations."
* "Where are our biggest opportunities and risks across channels right now?"

## Visualizations

When the data you ask about supports it, Operator returns a chart alongside the table.

* **Line charts** for time-series questions — trends over weeks, months, or quarters.
* **Bar charts** for comparisons across categories — channels, campaigns, periods.
* **Tables** for everything else, with percentages formatted to two decimal places and large numbers comma-separated for readability.

When a response includes multiple metrics, Operator prioritizes charting engagement rates (open rates, click rates, push open rates) over raw counts, since rates are usually the more decision-useful view.

## Supported channels and metrics

Beyond the engagement metrics below, Operator Analyze can also answer questions about **attributed revenue** and **conversions**, aggregated to the campaign, Canvas, channel, or program level.

| Channel | Metrics | Industry benchmarks |
| --- | --- | --- |
| Email | Sends, deliveries, unique opens, unique clicks, unsubscribes | Yes |
| Push (iOS, Android, Web) | Sends, deliveries, opens | Yes |
| SMS | Sends, deliveries, link clicks | Yes |
| In-App Messages | Impressions, clicks | Yes |
| Content Cards | Sends, impressions, clicks | Yes |
| WhatsApp | Sends, deliveries, reads, clicks | Not yet |
| RCS | Sends, deliveries, reads, clicks (including text URL, button, action, reply action, and reply button sub-types) | Not yet |

{% alert tip %}
Operator always uses unique counts for rate calculations (such as unique opens divided by deliveries for email open rate). If a number doesn't match what you see in a dashboard, it's most often because of a different attribution window, time range, or rate definition. Operator states the window, time range, and formula it used in every response — check those first when reconciling.
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

To use the standard calendar year instead, include "CY", "calendar year", or "standard year" in your question. If you say "last year" without specifying, Operator will ask which calendar you mean.

For specific historical periods, you can also use ISO date literals like `Q4 2025` or `2025-03-01 to 2025-05-31`.

### Attribution windows

Operator Analyze defaults to a 7-day attribution window for general analysis. You can override it explicitly:

* **1-day** for fast engagement checks
* **3-day** for short-cycle campaigns
* **7-day** (default) for general overviews and campaign performance
* **30-day** for long-term or strategic analysis
* **All windows** when you want a 1D / 3D / 7D / 30D side-by-side comparison

If results vary by more than 50% across windows, Operator will automatically present all four side-by-side so you can see the spread.

## Data freshness

Operator Analyze refreshes data daily. Today's activity isn't reflected until the next day. Every response includes the most recent date covered by the underlying data.

If the date shown looks unusually old, contact your Customer Success Manager.

## What's out of scope

The following are out of scope for the beta:

* **Product-level performance breakdowns.** Revenue and engagement are aggregated to the campaign, Canvas, channel, or program level — not to individual products or SKUs. Questions like "what are our top-performing products" or "revenue by SKU" aren't supported. Reach out to your Customer Success Manager for product-level analyses.
* **Industry benchmarks for WhatsApp and RCS.** Engagement metrics for both channels are fully supported; benchmark coverage isn't available yet.

If you ask a question that falls outside the supported scope, Operator will say so explicitly and either offer an alternative analysis it can run or direct you to your Customer Success Manager.

## Tips for better results

* **Be specific about the time range.** "Last quarter" works, but "FY26 Q2" or "the last 90 days" produces a cleaner answer.
* **Name the metric you care about** when you have one in mind — "open rate", "click-through rate", "click-to-open rate". Operator uses precise rate definitions and will tell you which formula it used.
* **Ask follow-ups.** Treat the first answer as a starting point — drill into the top performer, change the time range, or pivot to a different channel. Operator keeps context across the conversation.
* **Use the right channel terminology.** For WhatsApp and RCS, Operator uses "read rate" rather than "open rate". For SMS, it uses "link click rate".
* **Mix patterns.** Combine a benchmark comparison with a trend ("how has my email open rate moved versus the benchmark over the last four quarters?") — Operator handles multi-part questions natively.

## Data privacy and security

Operator Analyze is part of BrazeAI Operator<sup>TM</sup> and follows the same data privacy and security model as the rest of Operator. For full details, see [Data privacy and security]({{site.baseurl}}/user_guide/brazeai/operator/#data-privacy-and-security) on the BrazeAI Operator page.

## Next steps

* [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/): Learn how to access and use the Operator chat panel
* [Reviewing actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Learn how Operator proposes and executes changes in the dashboard
