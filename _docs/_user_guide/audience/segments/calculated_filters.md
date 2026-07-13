---
nav_title: Calculated filters
article_title: Calculated filters
page_order: 5.5
page_type: reference
description: "This reference article covers how calculated filters work, how they compare to SQL Segment Extensions, and how to create and manage calculated filters."
tool: Segments
---

# Calculated filters

> Calculated filters allow you to build very precise segments over an extended period of a user's history. For example, use calculated filters to target users who have purchased a particular product in the last 16 months or have spent a certain amount of money with your service. Refine this audience by using event properties to make targeting even more granular.

{% alert important %}
Calculated filters are currently in early access. If you're interested in participating in the early access, contact your customer success manager.
{% endalert %}

## How it works

Braze segments give you powerful targeting tools to create dynamic groups of users. For most use cases, this is enough to reach your audience effectively. Calculated filters are designed for advanced use cases where you need to analyze behaviors from up to two years ago or apply complex logic—without compromising data retention or system performance. You can use data from your own [data warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) to refine your audience further.

For example, Braze default segmentation finds users that fit specific criteria you define, such as identifying a user who recently purchased one of your products. Calculated filters let you go deeper—like identifying users who bought a particular color of a specific product at least twice between 18 to 24 months ago. Calculated filters are an enhancement, not a requirement. If you need more advanced filters or a longer historical window, they're a great tool to help while keeping your data usage optimized.

## Calculated filters and SQL Segment Extensions

[SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) and calculated filters both help you build audiences from purchase and custom event behavior, but they use different tools and data sources. SQL Segment Extensions use SQL you write against your connected Snowflake data.

| Behavior | Calculated filters | SQL Segment Extensions |
|---|---|---|
| How you define the audience | Choose purchases, eCommerce recommended events, message interaction, or custom events, and counts, time windows, and optional property filters | Write SQL against your Snowflake connection; use templates, incremental refresh, or full refresh |
| Where the logic runs | Criteria and refresh are managed in Braze as calculated filters | Query runs in your warehouse context according to your extension configuration |
| Filter list page | One calculated filter type, the **Segments** column shows how many segments use each filter, **Processing** and **Processing Failed** statuses reflect generation state | Includes a **Type** column and filters that vary by extension type |
| Typical use cases | Purchase frequency, total spend, custom event counts, and property-based rules over your selected window | Warehouse-backed logic, joins across tables, and historical windows or aggregations beyond the calculated filter form |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Calculated filters and SQL Segment Extensions" }

### When to use calculated filters

Use calculated filters when dashboard-guided purchase, eCommerce, message interaction, and custom event rules are enough and you do not need arbitrary SQL across warehouse tables.

### When to use other segment extension types

Use [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) when you need full SQL, Snowflake-backed data, templates, or refresh modes designed for large or complex warehouse queries. Use [CDI Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) when you need SQL that directly queries your data warehouse using data from [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) connections.

### Use calculated filters and Segment Extensions together

A segment can reference a calculated filter alongside a SQL or CDI Segment Extension—for example, a warehouse-defined cohort from an extension plus purchase or custom event rules you maintain in the calculated filter builder.

## Create a calculated filter

To create a calculated filter, define criteria based on user behavior, then save and activate the filter before using it in a segment.

### Step 1: Set up details

1. Go to **Audience** > **Calculated Filters**.
2. Select **Create Calculated Filter**.
3. Name your calculated filter by describing the users you intend to target. A descriptive name makes the filter easier to find when you add it to a segment.
4. (Optional) Add [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) to organize calculated filters in your workspace.

You can also select **Enable recurring audience update** to refresh the filter on a recurring schedule. If you don't turn on this setting, the Calculated Filter won't refresh unless you update the filter or select **Update audience**.

### Step 2: Choose your criteria

Choose a purchase, eCommerce, custom, or message interaction event criterion for targeting. After you select an event type, choose the specific event, how many times the user must have completed it (more than, less than, or equal to), and the time period.

When choosing your time period, you can specify a relative date range (the past X days), a start date, an end date, or an exact date range.

![Calculated filter criteria for users who performed a custom event more than zero times in the date range of June 21, 2026 through June 27, 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Event property segmentation

To increase targeting precision, select **Add Property Filters**. This lets you filter on properties of your purchase, eCommerce event, or custom event. Braze supports event property segmentation based on string, numeric, boolean, and time objects.

For string properties, enter multiple values at once—for example, targeting users with a status equal to gold, silver, or bronze. For eCommerce recommended events, the property dropdown populates with the properties available for that event.

{% alert note %}
You don't need calculated filters to use event properties in your segment. Calculated filters just extend the historic window used to create a default segment. You can create a real-time default [segment]({{site.baseurl}}/user_guide/audience/segments/) that uses event properties from the past 30 days. Similarly, you can [schedule your message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) to trigger in real time based on an event property—no calculated filter required. 
{% endalert %}

### Step 3: Save and activate your filter

Select **Save** to save your calculated filter. You can save a filter without activating it, but you must activate a filter before it appears as an option when you build a segment.

After you activate a calculated filter, Braze evaluates it in real time when a segment, campaign, or Canvas that references it is evaluated.

## Use a calculated filter in a segment

After you create and activate a calculated filter, add it when building a segment or defining an audience for a campaign or Canvas.

1. In the segment builder, open the filter list.
2. Under **Other Filters**, select **Existing Calculated Filter**.
3. Select the calculated filter to include in the segment definition.

After you add the filter, select the icon next to the filter dropdown to view the filter's details and confirm the criteria applied to your audience.

![Calculated filter in a segment builder with an icon to view more details.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

For more information on building segments, see [Create a segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).

## Manage calculated filters

Go to **Audience** > **Calculated Filters** to view, edit, and manage calculated filters in your workspace.

The **Calculated Filters** page lists all calculated filters in your workspace. You can narrow the list with the available controls. Because there is only one calculated filter type, there is no option to filter by type, and the table does not include a **Type** column. Use the **Segments** column to see how many segments use each calculated filter.

### Status labels

Each calculated filter displays one of the following statuses. **Processing** and **Processing Failed** show when membership generation is in progress or did not complete successfully.

| Status | Description |
|---|---|
| Active | The filter is activated and available to use in segments. |
| Draft | The filter is saved but not activated. |
| Archived | The filter is archived. |
| Processing | Braze is processing an update to the filter. |
| Processing Failed | The most recent processing attempt did not complete successfully. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status labels" }

### Edit and manage individual filters

Open a calculated filter's row menu to edit, archive, refresh the audience, or view how it is being used in messaging. You cannot edit a calculated filter while it is processing.

{% alert note %}
Your workspace can have up to 500 activated calculated filters at a time. Contact your Braze account manager if you need to increase this limit.
{% endalert %}

#### Save versus activate

You can save a calculated filter without activating it. Inactive filters remain in your workspace but cannot be added to segments until you activate them. Select **Activate filter** to use the filter in segmentation.

## Frequently asked questions

### Can I create a calculated filter that uses multiple custom events?

When using calculated filters, you can select one custom event, one purchase event, one eCommerce event, or one channel interaction. However, you can combine multiple calculated filters with an AND or OR when creating the segment.

You can add multiple events or reference multiple Snowflake tables when using [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/). 

### Can I archive calculated filters if they exist in an active campaign?

No. Before you can archive a calculated filter, you need to remove it from all active messaging.

### Can I use arrays in calculated filters?

Yes. To use arrays, append brackets (`[]`) to your property name. If your property is `location_code`,  you would enter `location_code[]`. 

Braze uses `[]` to traverse arrays and check if any item in the traversed array matches the event property. For example, you could create a calculated filter of users who match at least one value of an array property.

### How does Braze calculate the time period for a relative time period of "last X days"?

When calculated filters calculate the relative time period ("last X days"), the start time is set to midnight UTC. For example, for a calculated filter that refreshes at 2024-09-16 21:00 UTC and specifies 10 days, the start time is set to 2024-09-06 00:00 UTC, not 2024-09-06 21:00 UTC. 

However, you can specify the time zones by using SQL segments to identify users who performed the custom event 10 days ago based on midnight in company time, or users who performed the event 10 days ago based on the current time.