---
nav_title: Prompt library
article_title: Prompt library for BrazeAI Operator
page_order: 5
page_type: reference
description: "Browse example prompts for BrazeAI Operator, organized by the dashboard page you're viewing when you open Operator."
---

# Prompt library for BrazeAI Operator

> Browse example prompts organized by the dashboard page you're viewing when you open Operator. Because Operator uses page-aware context, these prompts work best when you open Operator from the corresponding page in your dashboard.

{% alert tip %}
For best results, open Operator from the relevant dashboard page before using these prompts. For more information, see [Leverage page-aware context]({{site.baseurl}}/user_guide/brazeai/operator/#leverage-page-aware-context).
{% endalert %}

{% sdktabs local %}
{% sdktab Home page %}

### Data analysis

```
Summarize the key trends for MAU, DAU, and New Users in this date range and what to do next.
```

```
Show the MAU, DAU, and New Users trends for the last 90 days—where are the biggest dips and spikes?
```

```
Break down sessions by app (if available) and highlight which app is driving the most growth this month.
```

### Strategy and optimization

```
What are 3 ways to use these app usage insights to shape a re-engagement Canvas for churn risk users?
```

```
What does our x% stickiness imply, and what are 3 ways to improve it with lifecycle messaging?
```

### Onboarding

```
Based on what's on this dashboard, what are the first 5 places I should visit in Braze to understand our setup (data, channels, sending, and targeting)?
```

```
Give me a 5-bullet health check of our engagement program for the last 30 days, with the biggest opportunities.
```

{% endsdktab %}
{% sdktab Campaigns %}

### Maintenance and organization

```
Show me the 5 idle active campaigns and recommend which to pause, refresh, or archive.
```

```
What are 3 ways to reduce 'complex audience' in these campaigns without losing targeting accuracy?
```

```
Show the top 10 active campaigns by engagement rate in the last 30 days (by channel)
```

### Audience management

```
What does "Complex audience" mean here, and how can I simplify those campaigns without losing targeting?
```

```
What are 3 ways to reduce 'complex audience' in these campaigns without losing targeting accuracy?
```

### Onboarding

```
I'm feeling overwhelmed, I want to get started with Agent Console but don't know how. Based on my currently running campaigns, what might I do?
```

```
Summarize this Campaign Digest in 5 bullets: biggest wins, biggest issues, and what changed vs the prior period.
```

{% endsdktab %}
{% sdktab Canvas %}

### Campaign and Canvas performance

```
Which Active Canvases drove the most attributed conversions and revenue in FY26 Q1 (7-day attribution)?
```

### Strategy and optimization

```
What are 3 ways to optimize our active lifecycle Canvases to increase activation and reduce churn?
```

```
What are 3 ways to restructure our onboarding Canvases to reduce drop-off and improve activation?
```

```
Show my idle Canvases and summarize what they last sent and when users last entered (last 90 days).
```

{% endsdktab %}
{% sdktab Individual campaign %}

### Campaign performance

```
Show this campaign's key engagement metrics (open/click rates) for the last 30 days and the prior 30 days.
```

```
How much Attributed Revenue and Conversions did this campaign drive in the last 90 days (7-day window)?
```

```
Compare this campaign's conversion rate vs our other in-app campaigns in this quarter to date.
```

```
Show the top 10 active campaigns by engagement rate in the last 30 days (by channel).
```

{% endsdktab %}
{% sdktab Segments %}

### Audience management

```
Which of our active segments were edited most recently, and which ones look like duplicates we should consolidate?
```

### Strategy and optimization

```
How can we use the [your segment name] segment to build a re-engagement journey and reduce churn?
```

### Campaign performance

```
What channels performed best for campaigns targeting 'C&L Newsletter Clickers' vs 'Openers but not Clickers' in the last 30 days?
```

{% endsdktab %}
{% sdktab Segment Extensions %}

### Cost savings

```
Which Segment Extensions are active but haven't been processed recently, and are they safe to archive for free slots?
```

### Strategy and optimization

```
How should we structure frequency-capping extensions (email/SMS/48h) to reduce over-messaging without hurting conversions?
```

### Campaign performance

```
How much Attributed Revenue and Conversions did campaigns generate for users excluded by our caps in the last 90 days (7-day window)?
```

{% endsdktab %}
{% sdktab Email Performance %}

### Campaign performance

```
Compare our email Open Rate and Click-Through Rate vs industry benchmarks for the last 30 days.
```

```
Which email campaigns had the lowest CTR (with high opens) in the last 30 days?
```

{% endsdktab %}
{% sdktab Query Builder %}

### Cost savings

```
How can we reduce Query Builder credit usage without losing reporting coverage? Suggest 3 tactics.
```

```
Which saved queries haven't been run in 90 days—can you help me identify candidates to archive?
```

{% endsdktab %}
{% sdktab Agent Console %}

### Onboarding

```
What can I do on the Knowledge Sources page, and what's the fastest way to get my first source set up?
```

{% endsdktab %}
{% sdktab Report Builder %}

### Strategy and optimization

```
What are 3 high-impact reports we should create here to monitor weekly campaign & Canvas health and catch issues early?
```

{% endsdktab %}
{% endsdktabs %}
