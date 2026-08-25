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
| Filter list page | A shared list for user activity and data object filters, the **Segments** column shows how many segments use each filter, and processing statuses reflect generation state | Includes a **Type** column and filters that vary by extension type |
| Typical use cases | Purchase frequency, total spend, custom event counts, and property-based rules over your selected window | Warehouse-backed logic, joins across tables, and historical windows or aggregations beyond the calculated filter form |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Calculated filters and SQL Segment Extensions" }

### When to use calculated filters

Use calculated filters when dashboard-guided user activity or data object rules are enough and you do not need arbitrary SQL across warehouse tables.

### When to use other segment extension types

Use [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) when you need full SQL, Snowflake-backed data, templates, or refresh modes designed for large or complex warehouse queries. Use [CDI Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) when you need SQL that directly queries your data warehouse using data from [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) connections.

### Use calculated filters and Segment Extensions together

A segment can reference a calculated filter alongside a SQL or CDI Segment Extension—for example, a warehouse-defined cohort from an extension plus purchase or custom event rules you maintain in the calculated filter builder.

## Create a calculated filter

To create a calculated filter, choose a filter type if prompted, define your criteria, then save and activate the filter before using it in a segment.

### Step 1: Set up details

1. Go to **Audience** > **Calculated Filters**.
2. Select **Create filter**.
3. If your workspace has [Accounts]({{site.baseurl}}/user_guide/data/activation/accounts/) enabled, select a filter type:
   - **User activity filters:** Actions and behaviors for users.
   - **Data Object filters:** Attributes and relationships for data objects.
4. Enter a name that describes the audience you intend to target. A descriptive name makes the filter easier to find when you add it to a segment.
5. (Optional) Add [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) to organize calculated filters in your workspace.

For **User activity filters**, select **Enable recurring audience update** to refresh the filter on a recurring schedule. If you don't turn on this setting, the filter doesn't refresh unless you update it or select **Update audience**. **Data Object filters** update hourly.

### Step 2: Choose your criteria

{% tabs %}
{% tab Data object filters %}

If you selected **Data Object filters**, choose a data object, then add attribute, relationship, or filter group conditions. For account-based targeting, see [Account objects]({{site.baseurl}}/user_guide/data/activation/accounts/).

{% endtab %}
{% tab User activity filters %}

If you selected **User activity filters**, or **Create filter** opened the user activity builder directly, choose one of the following **Criterion** options for targeting:

- **Made a Purchase**
- **Performed an eCommerce event**
- **Performed a Custom Event**
- **Interacted with Message Channel**

Available **Criterion** options vary based on the features enabled for your workspace. **Performed an eCommerce event** is always available. If you don't see another option that you need, contact your Braze account manager.

After you select an event type, choose the specific event, how many times the user must have completed it (more than, less than, or equal to), and the time period.

{% alert note %}
The **more than** and **less than** filters are exclusive—they don't include the number you specify. For example, a filter for **more than 4 times and less than 16 times** includes users who have had 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, or 15 times.
{% endalert %}

When choosing your time period, you can specify a relative date range (the past X days), a start date, an end date, or an exact date range.

![Calculated filter criteria for users who performed a custom event more than zero times in the date range of June 21, 2026 through June 27, 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Event property segmentation

To increase targeting precision, select **Add Property Filters**. This lets you filter on properties of your purchase, eCommerce event, or custom event. Braze supports event property segmentation based on string, numeric, boolean, and time objects.

For string properties, enter multiple values at once—for example, targeting users with a status equal to gold, silver, or bronze. For eCommerce recommended events, the property dropdown populates with the properties available for that event.

{% alert note %}
You don't need calculated filters to use event properties in your segment. Calculated filters just extend the historic window used to create a default segment. You can create a real-time default [segment]({{site.baseurl}}/user_guide/audience/segments/) that uses event properties from the past 30 days. Similarly, you can [schedule your message]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) to trigger in real time based on an event property—no calculated filter required. 
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 3: Save and activate your filter

Select **Save as draft** to save a new calculated filter without activating it. For an activated filter, select **Save changes** to save your updates. You must select **Activate filter** before a draft appears as an option when you build a segment.

After you activate a calculated filter, Braze starts calculating its audience. When processing is complete, you can select the filter when building an audience.

## Use a calculated filter in a segment

After you create and activate a calculated filter, add it when building a segment or defining an audience for a campaign or Canvas.

1. In the segment builder, open the filter list.
2. Under **Other Filters**, select **Existing calculated filter**.
3. Select the calculated filter to include in the segment definition.

After you add the filter, select the icon next to the filter dropdown to view the filter's details and confirm the criteria applied to your audience.

![Calculated filter in a segment builder with an icon to view more details.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

For more information on building segments, see [Create a segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).

## Manage calculated filters

Go to **Audience** > **Calculated Filters** to view, edit, and manage calculated filters in your workspace.

The **Calculated Filters** page lists user activity and data object filters together. You can narrow the list with the available controls, but the page does not include a filter-by-type control or a **Type** column. Use the **Segments** column to see how many segments use each calculated filter.

### Status labels

Each calculated filter displays one of the following statuses. **Processing** and **Processing failed** show when membership generation is in progress or did not complete successfully.

| Status | Description |
|---|---|
| Active | The filter is activated and available to use in segments. |
| Draft | The filter is saved but not activated. |
| Archived | The filter is archived. |
| Refresh disabled | Recurring audience updates are disabled. |
| Processing | Braze is processing an update to the filter. |
| Processing failed | The most recent processing attempt did not complete successfully. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status labels" }

### Edit and manage individual filters

Open a calculated filter's row menu to take an action. The actions you see depend on the filter's status.

For filters that aren't archived, the row menu includes **Edit**, **Messaging use**, **Archive**, and **Update audience**. **Update audience** is available for active filters that aren't processing. You can edit a calculated filter while it's processing, but you can't save your changes until processing is complete.

{% alert note %}
Your workspace can have up to 100 active calculated filters at a time. Contact your Braze account manager if you need to increase this limit.
{% endalert %}

#### Unarchive

Unarchive an archived filter by:

- Selecting **Unarchive** in the row menu
- Selecting one or more archived filters, then selecting **Unarchive**
- Opening an archived calculated filter and selecting **Unarchive** on its page

After you unarchive:

- A draft returns to **Draft**
- An activated filter returns to **Active**, counts toward the active filter limit, and Braze starts an audience refresh

Wait until processing finishes before you unarchive a filter that shows **Processing**. If you've reached the active filter limit, archive an active filter before you unarchive another active filter.

#### Save versus activate

You can save a calculated filter without activating it. Inactive filters remain in your workspace but cannot be added to segments until you activate them. Select **Activate filter** to use the filter in segmentation.

## Frequently asked questions

### Can I create a calculated filter that uses multiple custom events?

When using calculated filters, you can select one custom event, one purchase event, one eCommerce event, or one channel interaction. However, you can combine multiple calculated filters with an AND or OR when creating the segment.

You can add multiple events or reference multiple Snowflake tables when using [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/). 

### Can I archive a calculated filter if it is in use? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

No. Before you can archive a calculated filter, remove it from all campaigns, Canvases, and segments that use it.

### Can I use arrays in calculated filters?

Yes. To use arrays, append brackets (`[]`) to your property name. If your property is `location_code`,  you would enter `location_code[]`. 

Braze uses `[]` to traverse arrays and check if any item in the traversed array matches the event property. For example, you could create a calculated filter of users who match at least one value of an array property.

### How does Braze calculate the time period for a relative time period of "last X days"?

When calculated filters calculate the relative time period ("last X days"), the start time is set to midnight UTC. For example, for a calculated filter that refreshes at 2024-09-16 21:00 UTC and specifies 10 days, the start time is set to 2024-09-06 00:00 UTC, not 2024-09-06 21:00 UTC. 

However, you can specify the time zones by using SQL segments to identify users who performed the custom event 10 days ago based on midnight in company time, or users who performed the event 10 days ago based on the current time.