---
nav_title: Custom events
article_title: Custom Events
page_order: 1
page_type: reference
description: "This article describes custom events and properties, segmentation, usage, Canvas entry properties, where to view relevant analytics, and more."
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom events

> This article describes custom events and properties, user profile event history, related segmentation filters, Canvas entry properties, relevant analytics, and more. To learn about Braze events in general, refer to [Events]({{site.baseurl}}/user_guide/data/activation/events).

Custom events are actions taken by, or updates about, your users. When custom events are logged, they can trigger any number and type of follow-up campaigns. You can then use [segmentation filters](#segmentation-filters) to segment users based on how recently and frequently those custom events occurred. This makes custom events best suited for tracking high-value user interactions within your application.

## Use cases

Some common custom event use cases include:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Managing custom events

You can manage, create, or blocklist custom events in the dashboard by going to **Data Settings** > **Custom Events**.

### Troubleshooting duplicate custom attributes or events

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Select the menu next to a custom event for the following actions:

### Blocklisting

You can blocklist individual custom events through the actions menu, or select and blocklist up to 100 events in bulk. 

When you block a custom event:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Additionally, if a blocked custom event is currently referenced by filters or triggers in other areas of Braze, a warning modal will appear explaining that all instances of the filters or triggers that reference it will be removed and archived.

For more details on blocklisting and deleting custom data, see [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Adding descriptions

You can add a description to a custom event after it's created if you have the `Manage Events, Attributes, Purchases` [user permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Select **Edit description** for the custom event and input whatever you like, such as a note for your team.

### Adding tags

You can add tags to a custom event after it's created if you have the "Manage Events, Attributes, Purchases" [user permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). The tags can then be used to filter the list of events.

### Exporting data

To export the list of custom events as a CSV file, select **Export all** at the top of the page. The CSV file is generated, and a download link is emailed to you.

{% alert note %}
There is no fixed dashboard cap on how many distinct **custom events** or **custom attributes** you can define or store on a profile; practical limits depend on data shape, ingestion volume, and workspace performance. If you plan to track a very large catalog of events or attributes, work with your Braze account team on modeling and hygiene (for example, [blocklisting]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) unused data).
{% endalert %}

## Viewing usage reports

The usage report lists all the Canvases, campaigns, and segments using a specific custom event. This list doesn't include uses of Liquid. 

You can view up to 100 usage reports at a time by selecting the checkboxes next to the respective custom events and then selecting **View usage report**.

## Logging custom events

Custom events require additional setup. Refer to the following platform documentation for the methods used to log custom events and how to add properties and quantities to your custom events.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (formerly Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## Custom event storage

All data stored on the **User Profile**, including custom event metadata (first or last occurrence, total count, and X in Y over 30 days), is retained indefinitely as long as each profile is <a href="/docs/user_archival#active-users">active</a>.

## View a user's event history

Use the **Event History** tab on a user's profile to view that user's recent custom events and purchases. This helps you confirm your integration is logging events correctly and troubleshoot user-level issues directly in the dashboard.

To view a user's event history:

1. Go to **Audience** > **Search Users**, then select a user to open their profile.
2. Select the **Event History** tab.

The tab lists the user's custom events and purchases from the past 30 days, up to their 100 most recent events, ordered from newest to oldest.

Each event includes:

- **Event type:** Whether the event is a custom event or a purchase.
- **Event name:** The event name as it was logged.
- **Time:** When the event occurred.
- **Properties:** The full event properties for that occurrence, shown as JSON.

Common use cases include:

- Verifying your SDK or API integration is sending events as expected during development or after a release.
- Troubleshooting why a user did or did not enter an event-triggered campaign or Canvas.
- Investigating a support issue for a specific user without setting up a data export.

{% alert note %}
Viewing the **Event History** tab requires the **Search Users**, **View PII**, and **View User Event Properties** user permissions because event properties can contain personal data. For more information, refer to [Company user permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Segmentation filters

The following table shows the filters available for segmenting users by custom events.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred **more than X number of times** | **MORE THAN** | **NUMBER** |
| Check if the custom event has occurred **less than X number of times** | **LESS THAN** | **NUMBER** |
| Check if the custom event has occurred **exactly X number of times** | **EXACTLY** | **NUMBER** |
| Check if the custom event last occurred **after X date** | **AFTER** | **TIME** |
| Check if the custom event last occurred **before X date** | **BEFORE** | **TIME** |
| Check if the custom event last occurred **more than X days ago** | **MORE THAN** | **NUMBER OF DAYS AGO** (Positive Number) |
| Check if the custom event last occurred **less than X days ago** | **LESS THAN** | **NUMBER OF DAYS AGO** (Positive Number) |
| Check if the custom event occurred **more than X (Max = 50) number of times** | **MORE THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the custom event occurred **less than X (Max = 50) number of times** | **LESS THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the custom event occurred **exactly X (Max = 50) number of times** | **EXACTLY** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segmentation filters" }

## Analytics

Braze notes the number of times custom events have occurred and the last time they were performed by each user for segmentation. For report setup, filters, and export options, see [Custom events report]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

On the **Custom Events Report** page, you can view in aggregate how often each custom event occurs. The gray lines overlaid on the time series indicate the last time a campaign was sent, which is useful for viewing how your campaigns affected custom event activity.

![Custom event counts graph on the Custom Events page in the dashboard showing trends for a custom event]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

You can also use **Filters** to break down your custom events by hour, monthly average users (MAU), segments, or KPI formulas. 

![Custom event graph filters]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Increment custom attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) to keep a counter on a user action similar to a custom event. However, you can't view custom attribute data in a time series. User actions that don't need to be analyzed in a time series should be recorded using this method.
{% endalert %}

### Why custom events analytics aren't showing

Segments created with custom event data can't show previous historical data from before they were created.

## Custom event properties

Custom event properties are custom event metadata or attributes that describe a specific occurrence of an event. These properties can be used for further qualifying trigger conditions, increasing personalization in messaging, tracking conversions, and generating more sophisticated analytics through raw data export.

To learn more, refer to [Custom event properties]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

