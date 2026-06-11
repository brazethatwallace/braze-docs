---
nav_title: Email analytics glossary
article_title: Email analytics glossary
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "This glossary includes the terms you will find in the analytics section of your email campaign or Canvas, post-launch. This glossary does not include Currents metrics."
channel: 
  - email
---

> This glossary defines metrics on the **Analytics** tab for email campaigns and Canvases. Braze doesn't offer a hosted "view this email in a browser" page—see [Can I add a "view this email in a browser" link to my emails?]({{site.baseurl}}/user_guide/channels/email/faq/#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails) for a workaround. For other troubleshooting that spans multiple metrics, see [Email FAQ]({{site.baseurl}}/user_guide/channels/email/faq/).

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variation

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Emailable

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Audience %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Calculation: (Number of Recipients in Variant) / (Unique Recipients)</span>

{% endapi %}

{% api %}

### Unique Recipients

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} This number is received from Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Sends

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  This metric is provided by Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Messages Sent

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  This metric is provided by Braze.

<span class="calculation-line">Calculation: Count</span>

{% endapi %}

{% api %}

### Deliveries

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} For emails, *Deliveries* is the total number of messages (Sends) successfully sent to and received by emailable parties.

<span class="calculation-line">Calculation: (Sends) - (Bounces) </span>

{% alert note %}
For user-level **received** state and related logic (such as frequency capping), Braze generally marks a user when the send is processed and handed off for delivery—not when the email service provider (ESP) confirms final delivery to the inbox. That avoids timing gaps between ESP confirmation and in-product rules. It may differ from ESP- or third-party delivery reports.
{% endalert %}

{% endapi %}

{% api %}

### Deliveries %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calculation: (Sends - Bounces) / (Sends) </span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

For email, *Bounce %* or *Bounce Rate* is the percentage of messages that were unsuccessfully sent or designated as "returned" or "not received" from send services used or not received by the intended emailable users.

An email bounce for customers using SendGrid consists of hard bounces, spam (`spam_report_drops`), and emails sent to invalid addresses (`invalid_emails`).

{% alert note %}
In [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), temporary ESP deferrals are often represented as soft bounces. Deliverability tools (for example, native SendGrid reporting or Looker models) may use deferrals for the same situation. Deferrals are usually temporary, and mail is often delivered after retries. After extended retries (up to roughly 72 hours for soft bounces in campaign analytics), a message may be treated as undeliverable depending on your ESP. Currents email events are append-only—a logged soft bounce is not removed later if the message eventually delivers.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Bounces</i>:</b> Count</li>
        <li><b><i>Bounce %</i> or <i>Bounce Rate %</i>:</b> (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

When an email hard bounces or is marked as spam, Braze marks the email address as invalid but does not update the user's [subscription status]({{site.baseurl}}/user_guide/channels/email/subscriptions/). Braze stops any future sends to that email address. To remove an email address from your hard bounce list, use the [Remove hard bounced emails endpoint]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces).

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver. 

While soft bounces aren’t tracked in your campaign analytics, you can monitor the soft bounces in the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) or exclude these users from your sending with the [Soft Bounced segment filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced). In the Message Activity Log, you can also see the reason for the soft bounces and understand possible discrepancies between the “sends” and “deliveries” for your email campaigns.

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Spam</i>:</b> Count</li>
        <li><b><i>Spam %</i> or <i>Spam Rate %</i>:</b> (Marked as Spam) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Unique Opens

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} For email, this is tracked over a seven-day period. This means a single user who opens the same email again after seven days counts as a new unique open. As a result, dashboard unique open counts may be higher than a simple `DISTINCT user_id` query on Currents data. To match dashboard counts from Currents, filter for events where `is_unique` is `true`.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unique Opens</i>:</b> Count</li>
        <li><b><i>Unique Opens %</i> or <i>Unique Open Rate</i>:</b> (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Unique Clicks

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} This is tracked over a seven-day period for email and measured per <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a> (a single send attempt). This includes clicks on Braze-provided unsubscribe links. Tracked custom unsubscribe URLs also count toward *Unique Clicks* when a user selects the link. After seven days, another unique click counts for the same user if they click again. Dashboard email engagement metrics, including _Unique Clicks_, are calculated in Braze and are not reconciled from ESP aggregate reports. To match dashboard counts from Currents, filter for events where `is_unique` is `true`.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unique Clicks</i>:</b> Count</li>
        <li><b><i>Unique Clicks %</i> or <i>Click Rate</i>:</b> (Unique Clicks) / (Deliveries)</li>
    </ul>
</span>
{:/}

#### Unexpected links on the email heatmap

When the [email heatmap]({{site.baseurl}}/user_guide/channels/email/reporting/) shows links you do not expect, inspect the message HTML for [content blocks]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/) or spacing between words that create tracked URLs. Use the **Link Table by Total Clicks** on the heatmap view to identify URLs that do not match visible copy.

{% endapi %}

{% api %}

### Total Clicks

{% apitags %}
Count, Percentage
{% endapitags %}

<i>Total Clicks</i> is the total number of times users clicked links in the delivered email, including multiple clicks by the same user. This includes clicks on Braze unsubscribe links and tracked custom unsubscribe URLs.

When *Total Clicks* is much higher than *Unique Clicks*, security tools or mailbox providers scan links without users opening the message. Compare *Unique Clicks* when you evaluate engagement internally.

{% endapi %}

{% api %}
  
### Unsubscribers or Unsub

{% apitags %}
Count, Percentage
{% endapitags %}

_Unsubscribes_ reflect the standard unsubscribe link for Braze. Custom unsubscribe pages won't increment this metric unless you update users using the API. **Subscription Group Timeseries** still reflects API-driven changes.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unsubscribers</i> or <i>Unsub</i>:</b> Count</li>
        <li><b><i>Unsubscribers %</i> or <i>Unsub Rate</i>:</b> (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>
{:/}

#### Why *Unsubscribes* and unsubscribe-link clicks can differ

On the **Analytics** page for an email campaign or Canvas, compare the *Unsubscribes* count to clicks on the Braze unsubscribe URL in the per-link breakdown when you expand **Total Clicks** or **Unique Clicks**. The two often match but can differ:

- **More *Unsubscribes* than clicks on the body unsubscribe URL:** [List-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe) is an additional unsubscribe path in the email header (not the link in your message body). When a user unsubscribes that way, it counts toward *Unsubscribes* but does not count as a click on the tracked unsubscribe URL in the body.
- **More clicks on the body unsubscribe URL than *Unsubscribes*:** A user may select that link more than once. If they unsubscribe, resubscribe, and unsubscribe again, email analytics can record multiple clicks (for example, two) in the click breakdown.

For more information, see [Why am I seeing a different number of unsubscribes than clicks on my unsubscribe link?]({{site.baseurl}}/user_guide/channels/email/faq/#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

{% endapi %}

{% api %}

### Revenue

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Primary Conversions (A) or Primary Conversion Event

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} For email, push, and webhooks, we start tracking conversions after the initial send.

{::nomarkdown}
<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Primary Conversions (A)</i> or <i>Primary Conversion Event</i>:</b> Count</li>
        <li><b><i>Primary Conversions (A) %</i> or <i>Primary Conversion Event Rate</i>:</b> (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confidence

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Machine Opens
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Other Opens

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Note that a user can also open an email (such as the open counts toward <i>Other Opens</i>) before a <i>Machine Opens</i> count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward <i>Other Opens</i> and only once toward <i>Unique Opens</i>.

<span class="calculation-line">Calculation: Count </span>

{% endapi %}

{% api %}

### Estimated Real Opens

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Braze recalculates this estimate as new open and click data arrives. The value typically stabilizes a few days after send but continues to update when new qualifying events occur.

{% endapi %}

{% api %}

### Click-to-Open Rate

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calculation: (Unique Clicks) / (Unique Opens) (for Email)</span>

#### Message Open Likelihood scores (segmentation)

The [`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) segment filter scores how likely a user is to open email on a scale of 0–100%. Users without enough send or open history for the channel appear as blank. For email, machine opens are excluded from the calculation, which uses recent message history on that channel (see [Message Open Likelihood filter for individual channels]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#individual-channels)).

{% endapi %}

## Email reporting troubleshooting and FAQs

### Unsubscribe links and Unique Clicks

When a recipient clicks an unsubscribe link, Braze counts it as a click because the action uses a URL. This applies to Braze-provided unsubscribe links and custom unsubscribe links in your message body. Those clicks contribute to *Unique Clicks* and *Total Clicks* alongside other link clicks. For metric definitions, see [Unique Clicks](#unique-clicks) above and [Why am I seeing a different number of unsubscribes than clicks on my unsubscribe link?]({{site.baseurl}}/user_guide/channels/email/faq/#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

### View in browser

Braze does not include a built-in "View this email in a browser" feature. Host the email content on an external landing page (such as your website) and add a link from the message using the email editor **Link** tool. For more information, see [Can I add a "view this email in a browser" link to my emails?]({{site.baseurl}}/user_guide/channels/email/faq/#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails).

### Custom unsubscribe page updates

Changes to your [custom unsubscribe page]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/) appear within a few minutes. Live sends use a short-lived cache of the page that's refreshed when you save changes.

### Over-quota and full mailbox bounces

An over-quota or mailbox-full bounce means the recipient's mailbox cannot accept new mail. You may see these addresses among new sign-ups with invalid or risky addresses, or among long-inactive profiles whose inboxes filled while they were dormant.

Review bounce rates by segment and source, remove or sunset addresses that repeatedly hard-bounce, and use confirmed or double opt-in for new subscribers. For list hygiene practices, see [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/) and [Email reporting]({{site.baseurl}}/user_guide/channels/email/reporting/#troubleshooting).

### 550 5.7.1 unsolicited mail

A `550 5.7.1` response such as "Our system has detected that this message is likely unsolicited mail" often comes from strict mailbox providers (for example, Gmail) when reputation or engagement signals look poor. Common contributors include spam complaints, low engagement, purchased or rented lists, and sudden volume spikes.

Focus on consent-based list growth, sunset inactive subscribers, and monitor complaint and bounce rates. For more information, see [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/).

### Good email deliverability rates

**Delivery** is whether the receiving server accepts your message; you can measure it with metrics such as *Deliveries* and bounce rate. **Deliverability** (inbox placement) depends on provider filtering and isn't shown as a single Braze metric.

As a general guide, aim for delivery near 99% with hard bounces under about 1%, and watch opens and clicks for engagement trends. Exact targets vary by industry and sending pattern. For practices that support reputation, see [Improve email deliverability]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/) and [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/).

### "Campaign is already in delay window, so not enqueueing another"

In message activity or diagnostic logs for [action-based campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/), this processing outcome means Braze blocked a duplicate send while an earlier trigger for the same user is still within the campaign's delivery window. A debounce lock prevents multiple enqueues for the same trigger burst.

You can see this outcome even when the campaign shows **Send immediately** if any of the following apply:

- The campaign uses an [exception event]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/#exception-events) or a send-time delay that affects timing.
- Users have a [re-eligibility]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) period, so they can't receive the message again until that window passes.
- Another campaign or Canvas message step with higher priority consumed the send slot when triggers overlap.

If a user should have received the message but did not, check earlier outcomes for the same trigger (for example, email bounce or not enabled for the channel). Another message in the same workflow may have prevented this send.
