---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "This reference article outlines the partnership between Braze and Databricks Mosaic, which lets you connect Databricks models to Braze for use with custom AI agents."
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence) is Databricks' unified platform for building, deploying, and managing AI and machine learning models at scale on the Databricks Data Intelligence Platform.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_This integration is maintained by Databricks._

## About the integration

The Braze and Databricks Mosaic integration lets you connect your Databricks token and workspace to Braze so you can use Databricks models when building custom AI agents. Braze uses your Databricks Mosaic credentials to generate content for your customers. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using Databricks models.

## Prerequisites

| Requirements | Description |
|---|---|
| Databricks account with personal access token | A Databricks account with a [personal access token](https://docs.databricks.com/en/dev-tools/auth/pat.html). For help, contact your admin or [Databricks support](https://help.databricks.com/). |
| Databricks workspace name | The workspace name (or instance) for your Databricks account. This is the subdomain before `.cloud.databricks.com` or `.azuredatabricks.net` (for example, `dbc-eb57d699-f22c`). |
| Braze instance | You can find your Braze instance on the [API overview page]({{site.baseurl}}/api/basics/#endpoints) or from your Braze onboarding manager. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

To connect your Databricks Mosaic credentials to Braze:

1. Go to **Partner Integrations** > **Technology Partners** in the Braze dashboard and find **Databricks Mosaic Integration**.
2. Enter your **Databricks Token**.
3. Enter your **Databricks Workspace Name**. This is the subdomain before `.cloud.databricks.com` or `.azuredatabricks.net`.
4. Select **Save**.

After saving, Braze displays a connected status with the date and time of the connection. You can select Databricks models when [creating a custom agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) in the Agent Console.

To remove the integration, select **Disconnect** on the **Databricks Mosaic Integration** page.

Contact [Databricks support](https://help.databricks.com/) with any issues or questions regarding your integration.
