{% comment %}
  Shared Braze surveys documentation.
  Parameters:
  - channel (required): "in_app_message" or "landing_page"
{% endcomment %}

For an overview of Surveys and the capabilities shared across channels, see [Surveys]({{site.baseurl}}/user_guide/messaging/surveys).

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

Surveys are built inside your existing message composition flow.

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
- [Landing page form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [In-app message drag-and-drop editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Landing page form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
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
- Rating scale
- NPS

### Randomize answer choices

Radio button group, checkbox group, and dropdown blocks support randomized answer choices. Turn on **Randomize choice order** to shuffle the choices each time the survey loads. For more information, see [Randomized choice order]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order).

### Long text capture

Long text capture is useful for qualitative feedback, up to 1,000 characters. For more information, see [Long-form text capture]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture).

### Rating scale

Rating scale (also called a number scale question) is useful for capturing sentiment, satisfaction, or likelihood to recommend as a single number. For more information, see [Number scale questions]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions).

{% if include.channel == 'in_app_message' %}
![Rating scale to rate your store experience from 1 to 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Rating scale to give likelihood of recommending product to a friend from 1 to 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Rating scale to give likelihood of recommending product to a friend from 1 to 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Configure required fields and attributes

For each form block, enter an **Identifier for Reporting** in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

Keep in mind:

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

For definitions of the top-level analytics available for every survey (all responses, completed, partially complete, and unique impressions), see [Analytics]({{site.baseurl}}/user_guide/messaging/surveys#analytics).

{% if include.channel == 'landing_page' %}
{% alert note %}
Landing page surveys track partially complete responses when the survey uses [multi-step forms]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms).
{% endalert %}
{% endif %}

You can also review per-question response breakdowns, choose among three chart types, and export data as CSV. For more information, see [Chart types]({{site.baseurl}}/user_guide/messaging/surveys#chart-types).

## Retarget and trigger

You can:

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

You're restricted by the following:

- You can't segment users by long-form text responses.
- Question-and-answer triggering that does not rely on logged user attributes is not available.
