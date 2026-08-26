---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "This reference article outlines the partnership between Braze and Mixpanel, a business analytics platform, allowing you to import Mixpanel Cohorts into Braze to create Braze segments that can be used to target users in future Braze campaigns or Canvases."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/) is a business analytics platform that allows you to export events from Mixpanel into other platforms to perform deeper analysis. The data collected can then be used to build custom reports and measure user engagement and retention.

The Braze and Mixpanel integration allows you to [import Mixpanel Cohorts into Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) to create Braze segments that can target users in future Braze campaigns or Canvases. Cohort sync updates cohort membership in Braze and does not import Mixpanel events or user properties. For details, see [Mixpanel cohort import]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/#data-import-integration).

You can also use Braze Currents to [export your Braze events to Mixpanel](#data-export-integration) to drive deeper analytics into conversions, retention, and product usage.

## Prerequisites

| Requirement | Description |
|---|---|
| Mixpanel account | A [Mixpanel account](https://mixpanel.com/) is required to take advantage of this partnership. |
| Currents | In order to export data back into Mixpanel, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Data export integration

A full list of the events that can be exported from Braze to Mixpanel can be found in this section. All events sent to Mixpanel will include the user's `external_user_id` as the Mixpanel Distinct ID. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

You can export two types of events to Mixpanel: [Message Engagement Events](#supported-currents-events) consisting of the Braze Events directly related to message sending, and [Customer Behavior Events](#supported-currents-events) including other app or website activity such as sessions, custom events, and purchases tracked through the platform. All custom events are prefixed with `[Braze Custom Event]`. Custom event properties and purchase event properties are prefixed with `[Custom event property]` and `[Purchase property]`, respectively.

Contact your account manager or open a [support ticket]({{site.baseurl}}/braze_support) if you need access to additional event entitlements.

### Step 1: Get Mixpanel credentials

In your Mixpanel dashboard, click into the **Project Settings** in either a new or existing project. Here you will find the Mixpanel API secret and Mixpanel Token. These credentials will be used in the next step to create your Currents connection. 

### Step 2: Create Braze Current

1. In Braze, go to **Currents** > **+ Create Current** > **Create Mixpanel Export**. 
2. Provide an integration name, contact email, Mixpanel API secret, and Mixpanel token in the listed fields. 
3. Select the events you want to track; a list of available events is provided.
4. Select **Launch Current**.

![The Braze Mixpanel Currents page. This page includes fields for integration name, contact email, API secret, and mixpanel export token. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Check out Mixpanel's [integration docs](https://help.mixpanel.com/hc/en-us/articles/360001243663) to learn more. 
{% endtab %}

## Supported Currents events

Braze supports exporting the following events to Mixpanel:

- [Message engagement events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Customer behavior events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

For the payload structure of each event, select the **Mixpanel** tab in the [message engagement events glossary]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) and [customer behavior events glossary]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

## Troubleshooting

### Verify Mixpanel API key and Braze external ID

Confirm that your Mixpanel API key and `braze_external_id` values match what you expect across Braze and Mixpanel. The cohort sync API shares user groups between products, and the sync won't behave correctly if the `external_id` in Braze and the identifier Mixpanel sends don't align. Cohort syncs from Mixpanel run on Mixpanel's schedule—for example, once or approximately every two hours—so allow time between checks.

### Check implementation status

Confirm that `braze_external_id` is implemented in Mixpanel.

### Set the user property directly

To reduce ambiguity, set `braze_external_id` directly in Mixpanel.

### Automatic property setting (SDKs)

The Mixpanel SDK can set `braze_external_id` automatically when the Braze SDK is integrated in the same application. If you implement both Mixpanel and Braze together, you typically don't need extra wiring beyond installing both SDKs.

{% alert note %}
`braze_external_id` is not set when `changeUser()` is called in Braze; it is set when Mixpanel initializes or starts a session (during the "init" or "start session").
{% endalert %}