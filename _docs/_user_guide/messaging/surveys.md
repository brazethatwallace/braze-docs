---
nav_title: Surveys
article_title: Surveys
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Learn how Braze surveys let you collect first-party feedback across landing pages and in-app messages, including analytics, form blocks, and Currents export."
---

# Surveys

> Braze surveys let you collect first-party feedback directly from your users and act on it in follow-up messaging, without leaving the Braze dashboard. Use surveys to understand user sentiment, capture preferences, and build segments and triggers from the responses you collect.


## Channel availability

Surveys are available on two channels. Each channel page covers the channel-specific create flow, composition, and reporting location, while this page covers the concepts and capabilities that apply to both.

| Channel | Build surveys in |
| --- | --- |
| Landing pages | [Landing page surveys]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| In-app messages | [In-app message surveys]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey channel availability" }

## Surveys page

Go to **Messaging** > **Surveys** to find surveys across landing pages, campaigns, and Canvases in one place. Use it as your entry point for reviewing survey performance across channels.

{% alert note %}
If you don't see **Surveys** under **Messaging**, contact your Braze account manager.
{% endalert %}

## Analytics

Every survey question type includes enhanced reporting by default, so you can review response data at a glance without building a segment or exporting to a separate tool first.

Top-level analytics include:

- **All responses:** Total complete and incomplete responses
- **Completed:** Users who completed all required questions
- **Partially complete:** Users who submitted some data, but did not complete all required questions
- **Unique impressions:** Total page views

![Survey responses page showing NPS score analytics with promoter, passive, and detractor percentages and a horizontal bar chart of score distribution.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Chart types

For radio button, dropdown, and checkbox form blocks, you can choose among three chart types in the survey analytics view. This gives you more flexibility to interpret and share insights without exporting to a third-party tool.

| Chart type | Best for |
| --- | --- |
| **Bar chart** | The default horizontal view of response counts and percentages. |
| **Column chart** | A vertical view of response counts and percentages. Use this chart to compare responses side by side, especially for multi-select questions or questions with more answer options. |
| **Pie chart** | A proportional breakdown of responses. Use this chart for single-select questions when you want to see how responses are distributed across options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey chart types" }

Each chart shows real-time data as responses come in. You can switch chart types at any time without affecting the underlying data.

![Survey question-level breakdown using a bar chart.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Multi-step landing page forms

Build a survey as a single landing page with multiple steps that are automatically linked together, instead of creating multiple standalone landing pages and linking them manually. For example, you can define separate steps for each survey question, plus a confirmation step at the end.

This capability is specific to the landing pages channel. In-app message surveys also support a page manager for moving between steps; see [Compose an in-app message survey]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) for details.

![Landing page editor with a multi-step Form preview and the Form properties panel listing steps and a locked Confirmation step.]({% image_buster /assets/img/surveys/multi_step.png %})

## Question and form blocks

Landing pages and in-app messages support all their standard form blocks in surveys too, including radio button group, checkbox, checkbox group, dropdown, phone capture, email capture, and short text capture. This section highlights the three form blocks with reporting built specifically for surveys: NPS, number scale, and long-form text.

{% tabs local %}
{% tab NPS %}
### Standalone NPS block {#standalone-nps-block}

The **NPS** block is a separate form block from the **Rating** (number scale) block, not a configuration option within it. Add it to a survey to ask the standard Net Promoter Score question (0–10) and get reporting built specifically for that use case.

The **NPS** block gives you better dashboard reporting than a plain rating question used for the same purpose. Instead of a flat count of responses per number, Braze automatically groups responses into promoters (9–10), passives (7–8), and detractors (0–6) and surfaces those segments—and the resulting NPS score—directly in the survey analytics view.

Currents exports the numeric score (and, if added, the free-text feedback field) on the **Survey Response** event. Promoter, passive, and detractor segments aren't separate Currents fields.

![A mobile NPS survey next to the Survey responses dashboard, which shows an NPS score with promoter, passive, and detractor breakdowns and a response distribution chart.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Number scale %}
### Number scale questions {#number-scale-questions}

Also called a rating scale on the channel pages; both terms refer to the same **Rating** form block. Capture 1–5, 1–10, or 0–10 number-scale questions to fit different survey and reporting needs, from simple satisfaction ratings to likelihood-to-recommend scores. For channel-specific composition screenshots, see the Rating scale section on the [landing page surveys]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) or [in-app message surveys]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) page.

You can collect a rating as a survey response, log it as an integer custom attribute, or both. Pair a number scale question with a [long-form text capture](#long-form-text-capture) block to collect a numeric score alongside qualitative feedback in the same survey.

![Landing page survey editor with a 1–5 rating question selected and the Rating properties panel open on the right.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Long-form text %}
### Long-form text capture {#long-form-text-capture}

Long-form text capture is useful for qualitative feedback. You can configure the minimum and maximum character count (up to 1,000 characters), whether to show the character limit during composition, the text area height, and placeholder text.

![Long text capture block settings.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

Long text responses are available in reporting and exports, but they can't be logged as user profile custom attributes—so you can't segment users by a long-form response value directly. See [Limitations]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) on either channel page for details.

In Currents, long-form responses use `answer_type = 'free_form_text'` with the text in `answer_long_string`.
{% endtab %}
{% endtabs %}

## Randomized choice order

Radio button group, checkbox group, and dropdown blocks support randomized answer choices. Turn on **Randomize choice order** to shuffle the choices each time the survey loads, which reduces order bias when the same first option could otherwise skew responses.

Randomization changes only the display order for each survey respondent. Reporting labels and values stay mapped to the choices you configured, so analytics, CSV exports, and segmentation use the same response data regardless of the order a given user saw.

## Survey templates

Save a survey as a template from the landing page or in-app message template library so builders can start from it instead of recreating the same questions and form blocks each time. When survey templates are enabled for your workspace, filter the library by **Survey** to find and reuse saved survey structures across campaigns, Canvases, and landing pages.

## Survey Response events

Survey responses flow into [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) so you can export survey data to your data warehouse or a third-party BI tool for downstream analysis, joins with other engagement data, and custom reporting that goes beyond the dashboard's built-in analytics.

Braze exports individual survey answers to Currents through the **Survey Response** event (`users.messages.survey.Response`). Each event represents one respondent's answer to one survey question. For the full field reference, see [Survey Response events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) in the Currents event glossary.

## Landing page engagement funnel

Landing page surveys also generate **Landing Page Impression** and **Landing Page Click** events for page views and tracked clicks. Completing a landing page survey writes a **Survey Response** event; it doesn't also fire the generic **Landing Page Form Submission** event, which is for standard (non-survey) landing page forms. For the full field reference for these events, see the [Currents event glossary]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Related articles

- [Landing page surveys]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): Create flow, composition, and reporting for the landing pages channel
- [In-app message surveys]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): Create flow, composition, and reporting for the in-app messages channel
- [Drag-and-drop editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): Full reference for the form blocks you can add to a survey
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): Set up data export to your warehouse or BI tool
