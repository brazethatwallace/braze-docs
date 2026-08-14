---
nav_title: "Bot click filtering"
article_title: "SMS and RCS bot click filtering"
description: "This reference article covers SMS and RCS bot click filtering."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# SMS and RCS bot click filtering

> SMS and RCS bot click filtering enhances campaign analytics and workflows by excluding suspected bot clicks. A “bot click” refers to automated clicks on shortened links in SMS and RCS messages, such as those from web crawlers, Android and iOS link previews, or CPaaS security software. This feature facilitates accurate reporting, segmentation, and orchestration to engage real users. <br><br> For email campaign bot click filtering, refer to [Bot filtering for emails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering).

## How it works

Braze has a proprietary detection system that uses multiple inputs to identify suspected bot clicks, also known as non-human interactions (NHI). Bot clicks can inflate click rates, skewing engagement metrics. By filtering these, Braze facilitates the capture of reliable data for decision making.

Our system analyzes user agents associated with web crawlers, Android and iOS link previews, or CPaaS security software. A few examples of filtered user agents include `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3`, and `Barracuda Sentinel (EE)`.

## Affected metrics and workflows

The following Braze metrics and workflows are impacted by bot clicks:

- **_Total Clicks_:** Campaign analytics and Canvas analytics exclude bot clicks, reflecting only human interactions.
- **Segmentation filters:** Segment filters referencing SMS link interactions exclude bot clicks for more accurate retargeting in campaigns and Canvases.
- **Orchestration:** Bot clicks are filtered from action-based triggers and Canvas action paths that reference SMS link interactions, allowing for triggers to reflect human behavior.
- **Braze Intelligence:**
    - **Intelligent Selection:** Excludes bot clicks when optimizing variant selection.
    - **Intelligent channel:** Excludes bot clicks when SMS or RCS is selected for accurate channel selection.
    - **Experiment steps:** Excludes bot clicks for reliable experiment outcomes.
    - **Currents data exports:** Includes `is_suspected_bot_click` and `suspected_bot_click_reason` fields to help analyze human versus bot clicks. These fields are available in [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), and [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).

Unsubscribes from suspected bot clicks are unaffected. Braze processes all unsubscribe requests as usual. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Currents fields in SMS click events

Braze includes the following Currents fields for SMS click events:

| Field | Data type | Description |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | Indicates if the click is a suspected bot click. For SMS and RCS short-link clicks, Braze evaluates bot detection on every click and populates this field with `true` or `false`. |
| `suspected_bot_click_reason` | String, Array | Indicates the reason for a suspected bot click (such as `user_agent`). Populates when bot detection runs for SMS and RCS short-link clicks. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents fields in SMS click events" }

## Query Builder template

For help analyzing your data, you can use the pre-built mobile template **SMS click events by bots** in [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

## Frequently asked questions

### How does bot click filtering impact campaign performance?

Bot click filtering runs automatically for SMS and RCS shortened-link clicks. Dashboard click rates exclude suspected bot clicks, so reported rates reflect human interactions rather than automated link previews or crawler traffic.

### Does bot click filtering prevent bots from clicking unsubscribe links?

No. All unsubscribe requests are processed as usual.

### Are link previews included in bot click filtering?

Yes. Link previews (such as Android and iOS link previews) are flagged as bot clicks and filtered out.
