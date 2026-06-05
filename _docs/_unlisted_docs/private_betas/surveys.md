---
nav_title: Surveys
article_title: Braze surveys
description: "Learn how to create surveys in in-app messages and landing pages, review responses, and retarget users during closed beta."
permalink: /braze_surveys/
hidden: true
---

# Braze surveys

> Braze surveys collect feedback in in-app messages and landing pages that you can analyze and use in follow-up messaging.

{% alert important %}
Braze surveys are in closed beta. Send your feedback on the beta to [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com).
{% endalert %}

## Prerequisites

Before creating a survey, you must:

- Gain access to landing pages, in-app messages, or both in your Braze workspace
- Be familiar with [creating landing pages](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/)
- Be familiar with [creating drag-and-drop in-app messages](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)

## Create a survey

During beta, surveys are built inside your existing message composition flow.

1. Go to **Messaging** > **Landing Pages**, or create an [in-app message](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/) in a campaign or Canvas.
2. Create a new message.
3. Select **Survey** as your message type.

## Compose an in-app message survey

In-app message surveys contain two pages by default:

- **Page 1**, where users answer questions
- **Confirmation page**, where the survey is submitted

By default, buttons are linked to **Next page**. To change this behavior, update each button in the **Actions** panel.

![In-app message survey page flow and action settings.]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## Use survey form blocks

For shared styling and composition controls, see:

- [In-app message drag-and-drop editor blocks](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [Landing page form blocks](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

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

During beta, long text responses are available in reporting and exports, but they can't be logged as user profile custom attributes.

![Long text capture block settings.]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configure required fields and attributes

For each form block, enter an **Identifier for Reporting** in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

During beta:

- You can log most survey responses to user profile custom attributes.
- Long text responses can't be logged as custom attributes.
- If you choose not to log a response as a user attribute, you can't segment users by that response value.

![Identifier for reporting and attribute logging settings.]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## View reporting and analytics

After launch, review results in:

- The **Responses** tab for in-app message surveys
- The landing page analytics view for landing page surveys

![Landing page analytics tab.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

Top-level analytics include:

- **All responses:** Total complete and incomplete responses
- **Completed:** Users who completed all required questions
- **Partially complete:** Users who submitted some data, but did not complete all required questions
- **Unique impressions:** Total page views

{% alert note %}
Landing page surveys do not track partially complete responses during beta.
{% endalert %}

You can also review per-question response breakdowns and export data as CSV.

![Survey analytics overview and question-level breakdown.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![Bar charts of survey question-level breakdown.]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## Retarget and trigger

During beta, you can:

- Segment users by survey responses that are logged as user attributes.
- Segment users by survey completion status. <br><br>![Trigger setup and segmentation filters for survey follow-up.]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- Trigger campaigns and Canvases when a user completes a survey in a landing page or an in-app message campaign. <br><br>![Trigger setup and segmentation filter for landing page survey follow up.]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![Trigger setup and segmentation filter for in-app message campaign survey follow up.]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### Limitations

During beta, you are restricted by the following:

- You can't segment users by long-form text responses.
- Question-and-answer triggering that does not rely on logged user attributes is not available.