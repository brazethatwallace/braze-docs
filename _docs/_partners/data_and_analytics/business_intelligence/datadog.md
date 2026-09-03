---
nav_title: Datadog
article_title: "Datadog"
description: "This reference article outlines the partnership with Braze and Datadog, an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services through a SaaS-based data analytics platform."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) is an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services through a SaaS-based data analytics platform.

The Braze and Datadog integration allows customers to collect Braze data in Datadog and create alerts on the data we send. For example, setting up a monitor and alert if your weekly newsletter campaign sends an abnormally low volume of messages or if a Canvas step that usually only sends a few messages a day starts sending thousands. 

## Prerequisites 

| Requirement | Description |
|---|---|
| Datadog account | A Datadog account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Generate Datadog key

In Datadog, you will need to create an [API key](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). To add an API key, navigate to **Organization Settings** > **API Keys** > **New Key**.

### Step 2: Add key to Braze

In the Braze dashboard, navigate to **Partner Integrations** > **Technology Partners** and then search **Datadog**. On the Datadog partner page, provide the Datadog API key. This will create a connection to allow Braze to send data to Datadog.

## Braze events

After the connection is integrated, Braze sends the following events to Datadog:

- `braze.messaging.sent` - The count of sends

Each of these events has metadata in the form of Datadog tags to give you information such as:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (if available)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (if available)

These events and tags can be monitored on the Datadog **Metrics Explorer** page. These metrics are logged as [distributions](https://docs.datadoghq.com/metrics/distributions/) to DataDog. Given the nature of metrics and the imprecision of DataDog's aggregations and rollups, Braze does not retry intermittent network errors or other DataDog API errors that may be encountered during transmission. This means that these metric counts may differ slightly from counts seen in the Braze dashboard and/or through Currents.

![Datadog Metrics Explorer showing Braze event metrics and tags.]({% image_buster /assets/img/datadog.png %})

## Troubleshooting

### Why are `braze.messaging.sent` metrics missing in Datadog?

If you connected Braze to Datadog but don't see `braze.messaging.sent` in the Metrics Explorer, confirm the **Datadog site** selected in Braze matches your Datadog organization's site URL. Available sites are:

- `datadoghq.com` (default)
- `us3.datadoghq.com`
- `us5.datadoghq.com`
- `datadoghq.eu`
- `ddog-gov.com`
- `ap1.datadoghq.com`

A site mismatch can prevent metrics from appearing in the workspace where you search. In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** > **Datadog** and check that the site matches the subdomain in your Datadog account URL.

The **Datadog site** field is locked after you connect. To change it, disconnect the integration and reconnect with the correct site.

After you correct the site, wait for new send activity before metrics appear. Historical data isn't backfilled.

