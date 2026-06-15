{% comment %}
  Shared Braze surveys documentation.
  Parameters:
  - channel (required): "in_app_message" or "landing_page"
{% endcomment %}

{% multi_lang_include early_access_beta_alert.md feature='Braze surveys' %}

## Prerequisites

Before creating a survey, you must:

{% if include.channel == 'in_app_message' %}
- Have access to in-app messages in your Braze workspace
- Be familiar with [creating in-app messages in the drag-and-drop editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
{% elsif include.channel == 'landing_page' %}
- Have access to landing pages in your Braze workspace
- Be familiar with [creating landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)
{% else %}
- Have access to landing pages, in-app messages, or both in your Braze workspace
- Be familiar with [creating landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/) and [creating in-app messages in the drag-and-drop editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
{% endif %}

## Create a survey

During early access, surveys are built inside your existing message composition flow.

{% if include.channel == 'in_app_message' %}
1. Create an [in-app message]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) in a campaign or Canvas.
2. Select **Survey** as your message type.
{% elsif include.channel == 'landing_page' %}
1. Go to **Messaging** > **Landing Pages**.
2. Create a new landing page.
3. Select **Survey** as your message type.
{% else %}
1. Go to **Messaging** > **Landing Pages**, or create an [in-app message]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) in a campaign or Canvas.
2. Create a new message.
3. Select **Survey** as your message type.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Compose an in-app message survey

In-app message surveys contain two pages by default:

- **Page 1**, where users answer questions
- **Confirmation page**, where the survey is submitted

By default, buttons are linked to **Next page**. To change this behavior, update each button in the **Actions** panel.

![In-app message survey page flow and action settings.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Use survey form blocks

For shared styling and composition controls, see:

{% if include.channel == 'in_app_message' %}
- [In-app message drag-and-drop editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Landing page form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% else %}
- [In-app message drag-and-drop editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Landing page form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% endif %}

You can add the following form blocks to surveys:

- Phone capture
- Email capture
- Radio button group
- Short text capture
- Long text capture
- Dropdown
- Single checkbox
- Checkbox group

### Long text capture

Long text capture is useful for qualitative feedback.

You can configure:

- Minimum and maximum character counts (up to 1,000)
- Whether to show character limits during composition
- Text area height (rows)
- Placeholder text

During early access, long text responses are available in reporting and exports, but they can't be logged as user profile custom attributes.

![Long text capture block settings.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configure required fields and attributes

For each form block, enter an **Identifier for Reporting** in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

During early access:

- You can log most survey responses to user profile custom attributes.
- Long text responses can't be logged as custom attributes.
- If you choose not to log a response as a user attribute, you can't segment users by that response value.

![Identifier for reporting and attribute logging settings.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## View reporting and analytics

After launch, review results in:

{% if include.channel == 'in_app_message' %}
- The **Responses** tab for in-app message surveys
{% elsif include.channel == 'landing_page' %}
- The landing page analytics view for landing page surveys
{% else %}
- The **Responses** tab for in-app message surveys
- The landing page analytics view for landing page surveys
{% endif %}

![Landing page analytics tab.]({% image_buster /assets/img/surveys/survey-analytics-1.png %})

Top-level analytics include:

- **All responses:** Total complete and incomplete responses
- **Completed:** Users who completed all required questions
- **Partially complete:** Users who submitted some data, but did not complete all required questions
- **Unique impressions:** Total page views

{% if include.channel == 'landing_page' %}
{% alert note %}
Landing page surveys do not track partially complete responses during early access.
{% endalert %}
{% endif %}

You can also review per-question response breakdowns and export data as CSV.

### Choose a chart type

For radio button, dropdown, and checkbox form blocks, you can choose among three chart types in the survey analytics view. This gives you more flexibility to interpret and share insights without exporting to a third-party tool.

| Chart type | Best for |
| --- | --- |
| Bar chart | The default horizontal view of response counts and percentages. |
| Column chart | A vertical view of response counts and percentages. Use this chart to compare responses side-by-side, especially for multi-select questions or questions with more answer options. |
| Pie chart | A proportional breakdown of responses. Use this chart for single-select questions when you want to see how responses are distributed across options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey chart types" }

Each chart updates in real time as responses come in. You can switch chart types at any time without affecting the underlying data.

![Survey question-level breakdown using a bar chart.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Retarget and trigger

During early access, you can:

- Segment users by survey responses that are logged as user attributes.
- Segment users by survey completion status.

{% if include.channel == 'in_app_message' %}

![Trigger setup and segmentation filters for survey follow-up.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Trigger campaigns and Canvases when a user completes a survey in an in-app message campaign.

![Trigger setup and segmentation filter for in-app message campaign survey follow up.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Trigger setup and segmentation filter for landing page survey follow up.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Trigger campaigns and Canvases when a user completes a survey on a landing page.

{% else %}

![Trigger setup and segmentation filters for survey follow-up.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Trigger campaigns and Canvases when a user completes a survey in a landing page or an in-app message campaign.

![Trigger setup and segmentation filter for landing page survey follow up.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Trigger setup and segmentation filter for in-app message campaign survey follow up.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitations

During early access, you are restricted by the following:

- You can't segment users by long-form text responses.
- Question-and-answer triggering that does not rely on logged user attributes is not available.
