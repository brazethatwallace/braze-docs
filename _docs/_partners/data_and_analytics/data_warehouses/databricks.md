---
nav_title: Databricks
article_title: Databricks
description: "This article outlines Databricks Delta Sharing with Braze (closed beta), which allows you to access Braze engagement and campaign data in your Databricks account."
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks


> [Databricks](https://www.databricks.com/) is a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions at scale. The Databricks Data Intelligence Platform integrates with cloud storage and security in your cloud account, and manages and deploys cloud infrastructure for you.

{% alert important %}
Databricks Delta Sharing with Braze is in **closed beta**. Availability, supported regions, and product behavior can change. Contact your Braze customer success manager to participate or to confirm whether this feature is enabled for your workspace.
{% endalert %}

## Delta Sharing (Braze to Databricks)

Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) allows you to securely share data with business units and subsidiaries across clouds or regions without copying or replicating the data.

**Use Delta Sharing when you want to:**
- Query Braze event and campaign data using Databricks SQL
- Create complex reports and perform attribution modeling
- Join Braze data with other data in your Databricks account
- Benchmark your engagement data across channels, industries, and device platforms

For setup instructions, see [Databricks Delta Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/).

To learn more about Delta Sharing on Databricks, see [What is Delta Sharing?](https://www.databricks.com/product/delta-sharing).

## Prerequisites

Before you can use this feature, complete the following:

| Requirement | Description |
| ----------- | ----------- |
| Braze access | To access this feature in Braze, contact your Braze account or customer success manager. |
| Databricks account | A Databricks account with `admin` permissions. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

When you're ready to configure sharing and query shared data, continue to [Databricks Delta Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/).
