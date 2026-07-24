---
nav_title: FAQ
article_title: Email FAQ
page_order: 30
description: "This page provides answers to frequently asked questions about email messaging."
channel: email

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about emails.

## What happens when an email is sent out, and multiple profiles have the same email address?

If multiple users with matching email addresses are in a segment to receive a campaign, a single user profile with that email address is selected at send time. This way, the email is sent only once and deduplicated, ensuring it doesn't reach the same email address multiple times.

**Unique email addresses:** Braze doesn't enforce unique email addresses across profiles. If you rely on a one-to-one relationship between an email address and a profile, monitor for duplicates internally when creating users.

**Deduplication before Liquid:** For sends where Braze deduplicates by email address within one dispatch (for example, scheduled campaigns where multiple segment members with the same address are processed together), that deduplication happens before Liquid runs for the profile chosen to represent that address. If Liquid aborts for that profile (for example with [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), that address does not receive the message on that dispatch—including profiles already skipped by deduplication. Triggered sends do not apply that same in-dispatch address deduplication; multiple profiles who share an address can all remain eligible in one batch, so this abort behavior does not apply the same way (see the next paragraph).

If multiple profiles share an email address and one profile unsubscribes, Braze updates other profiles (up to 100) with that address to the same subscription state. This applies to unsubscribes and other changes such as global subscription state and individual subscription group statuses.

**Seed Groups:** For campaigns with [Seed Groups]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups), Braze selects one profile for primary delivery when several profiles share an address. That primary recipient might not be in your Seed Group, even when another profile with the same address is.

The following scenarios can make it seem like a user received an email twice:

- **Seed lists or test recipients:** Seed addresses and internal test recipients can receive a send in addition to your main audience, which can look like a duplicate when an inbox matches both a profile and a seed entry.
- **An error occurred during campaign or Canvas creation:** The user may not receive the same send twice, but may receive two separate emails with the same subject line. When a campaign or Canvas is duplicated, check email configuration details such as images or subject lines. You can also refer to changelogs to see if the campaign or Canvas was modified after launch—a duplicate may share the same subject line as the original when the user received it.
- **Multiple user profiles have email forwarding:** If a user has multiple accounts in a given app but one account forwards mail, the user receives the campaign once per inbox; mail can appear twice in the inbox where messages are forwarded. Only some providers indicate when an email was forwarded from another account.
- **Email configuration at the recipient:** Some clients merge inboxes ("universal inbox"). If the same campaign targets multiple accounts that share one inbox, it can look like one person got the campaign twice when two distinct profiles were actually messaged. The recipient can confirm whether multiple accounts are combined in one inbox.

This deduplication applies when targeted users are in the same dispatch. Re-eligibility is evaluated per profile, not per email address. 

Email campaign and Canvas step re-eligibility uses each user's profile—not the inbox—so multiple profiles can qualify for separate sends while that logic is satisfied. Combined with triggers, this can deliver more than one message to the same inbox even when you're trying to honor a single ineligibility period at the address level. Triggered campaigns (excluding API-triggered campaigns) and Canvases can also send twice to one address when different profiles with matching email addresses meet the trigger at different times—for example if user A and user B share `johndoe@example.com` but sit in different time zones while the delivery uses local time zones.

Users are not deduped by email on Canvas entry, so they may not be deduped beyond the first step of a Canvas if they progress at slightly different times due to rate-limited entry. When a user associated with a given email address opens or clicks an email, all user profiles that share that email address are marked as having opened or clicked the campaign.

### Exception: API-triggered campaigns

API-triggered campaigns will deduplicate or send deduplicates depending on where the audience is defined. Duplicate emails must be targeted separately in the API call using distinct `user_ids` to receive multiple deliveries. Here are three possible scenarios for API-triggered campaigns:

- **Scenario 1: Duplicate emails in target segment:** If the same email appears in multiple user profiles that are grouped in the dashboard's audience filters for an API-triggered campaign, only one of the profiles receives the email.
- **Scenario 2: Duplicate emails in different `user_ids` within recipients object:** If the same email appears within multiple `external_user_id` values referenced by the `recipients` object, the email is sent twice.
- **Scenario 3: Duplicate emails due to duplicate `user_ids` within the recipients object:** If you try to add the same user profile twice, only one of the profiles receives the email.

{% alert important %}
If you send an API campaign through an API call (excluding API-triggered campaigns), and multiple users are specified in the segment audience with the same email address, it sends to that address as many times as listed in the call. This is because API calls are assumed to be purposefully constructed.
{% endalert %}

#### A/B testing with duplicate email addresses

Avoid [multivariate and A/B tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing) on email when multiple profiles can share the same email address. Variants are assigned per profile, which can produce more than one message to the same inbox. If you must test in that situation, do not combine a **winning variant** step with [local time zone delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) in a way that delays selecting the winner—those options together can increase the chance of duplicate sends.

#### Canvas and duplicate email addresses

For Canvas journeys, whether duplicate email addresses receive one send or more than one can depend on entry batching, step timing, and other factors. Treat behavior as undefined until you validate it for your journey. Where possible, merge or consolidate duplicate profiles. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### What happens to the subscription state when a user's email address changes to one shared by another user?

If you set or update the email address for user A to another email address that's shared by an existing user B, user A inherits the subscription state that already exists from user B unless the **Resubscribe users when they update their email** setting is turned on.

### Will updates to my outbound email settings apply retroactively?

No. Updates made to the outbound email settings do not retroactively affect existing sends. For example, changing your default display name in the email settings will not automatically replace the existing default display name in your active campaigns or Canvases. 

### What is a "good" email delivery rate?

Typically, the "magic number" is around 98% of messages delivered with a bounce rate no higher than 3%. If fewer than 98% of messages are delivered, there is usually cause for concern.

However, a delivery rate of 98% or higher can still have deliverability issues. For example, if all your bounces come from a single domain, that is a clear signal of a reputation issue with that provider.

Additionally, messages may be getting delivered and ending up in Spam, indicating potentially serious reputation issues. It's important to monitor not just the number of messages being delivered, but also open and click rates to determine whether users are actually seeing the messages in their inboxes. Because providers usually don't report every spam instance, a spam rate of even 1% could be cause for concern and further analysis.

Finally, your business and the types of emails you send may also affect delivery. For example, someone sending mostly [transactional emails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) should expect to see a better rate than someone sending many marketing messages.

### Why are my email delivery metrics not adding up to 100%?

Email delivery metrics (deliveries, bounces, and spam rate) may not add up to 100% because of emails that are soft bounced and then not delivered after the retry period of up to 72 hours.

Soft bounces are emails that bounce due to a temporary or transient issue, such as "mailbox full," "server temporarily not available," and more. If a soft-bounced email is still not delivered after 72 hours, this email will not be accounted for in the campaign delivery metrics.

### What is an email feedback loop?

An email feedback loop (FBL) allows senders to monitor their reputation by identifying campaigns that receive a high volume of complaints. For steps to implement a Gmail feedback loop, see [Google's Feedback Loop](https://support.google.com/a/answer/6254652) article.

### What are open tracking pixels?

[Open tracking pixels]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) leverage a sender's email click tracking domain to track email open events. The pixel is an image tag appended to the email's HTML. It is most commonly the last HTML element within the body tag. When a user loads their email, a request is made to populate the image from the branded tracking domain, which logs an open event.

### What happens when an email campaign or Canvas is stopped?

Users are prevented from entering the Canvas, and no further messages are sent out. 

For email campaigns and Canvases, the stop button does not immediately stop the send. When the send requests are sent, they cannot be stopped from being delivered to the user, which may happen after some delay. 

While Braze won't send further requests once the campaign or Canvas is stopped, analytics may still increase while the ESP finishes processing requests already in flight.

### Why am I seeing more _Total Clicks_ than _Total Opens_ in my email analytics?

_Total Opens_ is the count of how many times the email was opened by users, whereas _Total Clicks_ is the count of how many times users clicked within the delivered email, including any type of clicks such as link clicks. You may be seeing more clicks than opens for any of the following reasons:

- Users are performing multiple clicks on the body of the email within a single open.
- Users click on some email links within the preview pane of their phones. In this case, Braze logs this email as being clicked but not opened.
- Users reopen an email that they previewed earlier.

### Why am I seeing zero email opens and clicks?

You may see no email opens or clicks if there's a misconfiguration in your tracking domain. This can be due to any of the following reasons:
- There is an SSL issue where tracking URLs are `http` instead of `https`.
- There is an issue with your CDN where the user agent string on the open events, click events, or both aren't populating.

### Why am I seeing unusual email open or click behavior?

If you notice unexpected patterns in your email open or click metrics—such as a single user appearing to click every link immediately, or opens not registering as expected—review the following common causes:

#### Email clipping removes the tracking pixel

When an email is clipped by the recipient's email provider (such as Gmail clipping messages over approximately 102 KB), content at the bottom of the email may be truncated. Because the open tracking pixel is typically inserted at the bottom of the email, clipping can prevent open tracking from working.

**How to identify:** Check whether the email displays a "View entire message" or similar link at the bottom. You can use [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) to preview the full scrollable email and verify whether the message is being clipped.

**How to resolve:** You can configure Braze to place the tracking pixel at the top of the email instead of the bottom. Moving the tracking pixel may affect how some email clients render your HTML, so test your emails in Inbox Vision after making this change. Note that if the recipient has images disabled, opens cannot be tracked regardless of pixel placement.

#### Delayed stats or clicks without opens

Open tracking relies on the recipient loading the email with images enabled. In some cases, stats may appear delayed or clicks may be logged without corresponding opens due to:

- The recipient viewing the email in a preview pane without fully opening it, then clicking links directly from the preview.
- The email client not loading images (and therefore the tracking pixel) until after the recipient has interacted with links.

#### Security software simulates link clicks

Some corporate email security tools (such as Barracuda, Proofpoint, and similar services) scan incoming emails by automatically clicking all links in the message to verify they are safe. This can result in click events appearing within seconds of send, often with every link in the email clicked in rapid succession.

This behavior is more common with institutional email domains (such as high schools, universities, and corporate environments) and is more likely when your sending domain differs significantly from your tracking domain. Setting up a [custom branded tracking domain]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) can reduce the frequency of these automated clicks.

**How to identify:** Look up the IP address of the click event (available in Currents data) in a search engine. If the IP is associated with a known security provider (such as Barracuda Networks), the clicks are likely automated. You may also see a consistent User-Agent header across multiple automated clicks.

For additional context on how security scanning affects email metrics, refer to [Handling increases in click rates]({{site.baseurl}}/user_guide/channels/email/reporting).

### What are the potential risks of triggering server clicks?

Certain elements of an email message, such as overly long messages or too many exclamation marks, can trigger email security responses. These responses can affect reporting and IP reputation and lead users to unsubscribe.

For best practices on how to handle these responses, refer to [Handling increases in click rates]({{site.baseurl}}/user_guide/channels/email/reporting).

### Can Braze track unsubscribe links counted toward the "Unsubscribe" metric?

Braze tracks unsubscribe links if the following Liquid is used within emails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Why am I seeing a different number of unsubscribes than clicks on my unsubscribe link?

If there are more _Unsubscribes_ than users who clicked the unsubscribe link in the email body, [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) often explains the gap. List-unsubscribe is an additional unsubscribe path in the email header (not the link in your message body). When a user unsubscribes that way, it counts toward _Unsubscribes_ but does not count as a click on the tracked unsubscribe URL in the body.

If the total number of clicks on the body unsubscribe link is greater than the number of _Unsubscribes_, users may have clicked the link more than once—for example, if they unsubscribe, resubscribe, and unsubscribe again, email analytics can record multiple clicks in the click breakdown.

If a user clicks the unsubscribe link twice (for example, if they unsubscribed, subscribed again, then unsubscribed again), this counts twice in email analytics.

### Can I add a "view this email in a browser" link to my emails?

No. Braze does not offer this functionality. This is because a growing majority of email is opened on mobile devices and in modern email clients, which render images and content without issues.

**Workaround:** To achieve this same result, you can host the content of your email on an external landing page (such as your website), which can then be linked to from the email campaign you are building using the **Link** tool when editing the email body.

### Does Braze automatically turn plain text URLs or "www." text into links?

No. Braze does not scan your message and convert plain text, such as text that starts with `www.` or looks like a URL, into hyperlinks. Only links you define with HTML anchor tags (`<a href="...">`) are processed through normal rendering and link features in Braze.

If a recipient sees plain text shown as a clickable link, that behavior usually comes from their email client (for example, Gmail, Outlook, or Apple Mail). Many clients detect URL-like strings after the message is delivered and turn them into links on the recipient's device. Braze does not control that behavior and cannot turn it off for the recipient.

For predictable link appearance, tracking, and styling, use explicit `<a href>` tags instead of plain text URLs.

### Why are my users being auto-unsubscribed by email security software?

Some corporate email security tools (such as Barracuda, Proofpoint, and similar services) pre-fetch or scan all URLs in incoming emails, including unsubscribe links. This can cause unintended unsubscribes when the security tool follows the one-click list-unsubscribe link.

To mitigate this:

- **Recommend recipients allowlist your sending domain:** Work with the affected recipients' IT teams to add your sending domain and Braze tracking domains to their email security allow list.
- **Use a preference center:** Instead of a direct unsubscribe link, use a [preference center]({{site.baseurl}}/user_guide/channels/email/subscriptions) that requires user interaction to confirm the unsubscribe action. Security scanners typically won't complete multi-step forms.
- **Review unsubscribe logs:** Check the `User-Agent` header and IP address in your Currents unsubscribe event data to identify patterns consistent with automated scanning (such as consistent `User-Agent` headers across multiple unsubscribes).

For more details on how server-side scanning can affect email metrics, refer to [Handling increases in click rates]({{site.baseurl}}/user_guide/channels/email/reporting).

### Why has my machine open rate changed unexpectedly?

[Machine opens]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) are triggered by email security features such as Apple Mail Privacy Protection (MPP), which pre-loads email content (including the tracking pixel) without the user physically opening the email. Machine open rates can fluctuate based on:

- Changes in the proportion of your audience using Apple Mail or other privacy-enabled email clients.
- Updates to email provider privacy features or bot detection behaviors.
- Changes in your audience segmentation or targeting.

Machine open percentages are not a reliable measure of actual engagement. For a more accurate view of email performance, focus on *Other Opens* (non-machine opens) and *Unique Clicks*. You can also compare these metrics over time using the [Email Performance Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance).

### Why are my deep links not working in Gmail?

Gmail strips all non-HTTP/HTTPS links from email messages. If your deep link uses a custom scheme (such as `myapp://path/to/content`), Gmail will remove it, and the link won't function for recipients reading the email in Gmail. This is a Gmail limitation, not a Braze limitation.

To work around this:

- **Use Universal Links (iOS) or App Links (Android).** These use standard `https://` URLs that open your app when installed and fall back to a web page otherwise. Refer to [Universal Links and App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links) for setup instructions.
- **Use a deep linking provider.** Services like [Branch](https://www.branch.io/) generate HTTP-formatted deep links that are compatible with email clients, including Gmail.
- **Set up a redirect endpoint.** Host an `https://` endpoint on your server that redirects to your app's custom-scheme URL. Email clients will preserve the `https://` link, and the redirect handles opening the app.

### Does the *Unique Opens* metric include *Machine Opens*?

Yes. *Unique Opens* include *Machine Opens*. You can view both metrics in the **Campaign Analytics** view and **Report Builder**.

### Why does my email delivery volume not match my send volume?

After an email is sent, the recipient's inbox decides when it is delivered. Messages can be deferred for hours or days because of a full mailbox, ESP throttling from a given IP, and similar reasons.

When deferred messages are delivered on a different calendar day than the send day, _Deliveries_ can exceed _Sends_ for the same date range. When many deferrals land on one day, _Sends_ can exceed _Deliveries_ for that range.

### Why am I seeing a warning to include an unsubscribe link when my email already has one?

This warning can persist for campaigns duplicated from a campaign that did not have an unsubscribe link. To clear it:

- For HTML emails, go to the **Plaintext** tab, then select **Regenerate from HTML**.
- After duplicating, duplicate the variant, then remove the original variant. **Do not** select the original variant, or the warning can carry over.

### Why did a user receive an email they shouldn't have?

Delivery can look wrong even when Braze behaved as configured. Work through the following:

- **Duplicate profiles** that share one inbox (see [What happens when an email is sent out, and multiple profiles have the same email address?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Seed lists, test recipients, or internal addresses** included in the audience or on a send as CC/BCC.
- **Segment or Canvas timing:** the user matched the audience or Canvas step when Braze evaluated eligibility, then attributes or subscription state changed before they read the message.
- **Subscription groups:** the user remained opted in to a group your message targeted even if their global subscription state suggested otherwise.
- **API or file imports** that updated the user after segmentation but before you expected the change to apply.

Review the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), campaign or Canvas changelogs, and segment definition. If you still cannot reconcile the send, contact Braze Support with user identifiers, `dispatch_id` (if available), and timestamps.

### Why hasn't a user received my email message?

There are several reasons why a user does not receive an email that you expected them to get, including:

- They weren't eligible to receive the email.
- Their email address is invalid or doesn't exist.
- They may have missed or deleted the message.
- The message may be in their spam folder.

{% alert tip %}
A delivery event in Braze means the email was accepted by the mailbox provider's server. However, this does not guarantee that the message appears in the user's inbox. The mailbox provider may route the message to spam or, in rare cases, silently prevent display of the message.
{% endalert %}

Use the following tables to narrow down the cause.

#### The email wasn't sent

| Possible cause | What to check |
|---|---|
| The user wasn't eligible for the campaign or Canvas | Check the **Target Audiences** (for campaigns) or **Target Audience** (for Canvas) [settings]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) to confirm the user met all audience filters, segment criteria, and delivery rules at the time of send. |
| The message was aborted | Check the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) for abort reasons, such as Liquid errors or missing required fields. |
| The user's email address was invalid or missing | In **User Search**, check the user's profile to verify that a valid email address was on file at the time of send. |
| The user's email address previously hard bounced | A hard bounce marks the email address as invalid and prevents future sends to that address. Similarly, if a recipient marks your email as spam, Braze sends only transactional emails to that user, not standard campaigns. Check the user's **Engagement** tab in their profile. For more information, see [Unsubscribed email addresses]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) and [Bounces and invalid emails]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| The user is unsubscribed from email | Check the user's subscription status under **Contact Settings** on the **Engagement** tab. Braze does not send emails to users who are unsubscribed. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cause for email not sent" }

#### The email was sent, but didn't arrive in their inbox

| Possible cause | What to check |
|---|---|
| The mailbox provider (MBP) was unreachable | A temporary issue prevented the email from reaching the recipient's MBP. This typically resolves itself with retries. Email service providers retry soft bounces for up to 72 hours. |
| The MBP bounced the email | The recipient's mail server rejected the email. Review the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) for bounce details. |
| The MBP silently dropped the email | The MBP accepted the email but didn't display it to the user and didn't return a bounce. This is outside of Braze's control and cannot be detected in Braze logs. |
| The email went to the spam folder | The MBP identified the message as spam and routed it to the user's spam or junk folder. Ask the user to check their spam folder. |
| The recipient has custom mail filtering | The user or their IT administrator may have configured mailbox rules that filter, redirect, or delete incoming messages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cause for email not in inbox" }

### How do I troubleshoot email deliverability issues?

If your emails are delayed, deferred, or bouncing, review the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) for bounce and deferral details, then identify where the issue occurs in the delivery chain. Common deliverability problems fall into four categories:

#### Reading ESP rate-limit responses

Your email service provider (ESP), such as Amazon SES, SparkPost, or SendGrid, returns SMTP response codes when accepting or deferring messages. Rate-limit responses typically use 4xx codes, which indicate temporary failures:

- 421: Service temporarily unavailable, often due to high volume, connection limits, or server resource constraints. The message remains queued and your ESP retries delivery automatically.
- 429: API rate limit exceeded. You've sent too many requests in a given time window.
- 450 / 451: Temporary deferral due to volume or connections. The recipient server is asking you to slow down.

When you see these codes in the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) or your ESP dashboard, reduce send volume to the affected domain and use progressively longer retry intervals. Continuing at full volume while rate-limited can escalate temporary deferrals to permanent rejections.

#### Mailbox provider rate limits

Mailbox providers enforce their own rate limits on incoming mail, separate from Braze's sending controls. These limits can be strict and are outside your direct control:

- Virgin Media / NTL (UK): Uses hourly rate limiting that triggers `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded` errors. These limits can affect even low-volume senders and are enforced at the IP level across all senders using that IP.
- Gmail, Yahoo, iCloud, Microsoft: Each provider has proprietary throttling thresholds based on your sender reputation, volume, and engagement patterns.

If you encounter provider-specific rate limiting, consider batching your sends over a longer time period or segmenting by mailbox provider to spread volume more gradually. Check your recipient list for concentration at one provider—if most recipients use one domain, stagger delivery.

#### Corporate email delays from antivirus scanning

Business email addresses often pass through corporate security gateways that scan messages before delivery. This can delay emails by 15–20 minutes or longer, especially for messages with:

- Large attachments
- Links to unfamiliar domains
- Content that resembles phishing patterns

These delays occur because security systems queue messages for behavioral analysis in isolated sandbox environments. If a large volume of mail arrives simultaneously, messages queue for analysis and the delay extends further. This is normal behavior for enterprise email security and is not something you can bypass. When sending time-sensitive messages to corporate recipients, account for this processing window in your communication timeline.

#### Google 421-4.7.28 rate-limit responses

Gmail returns a `421-4.7.28` error when it detects an unusual rate of unsolicited email from your IP address, sending IP range, SPF domain, DKIM domain, or URL domain. This is a temporary throttle, not a permanent block, but it signals that your sending volume, velocity, or reputation does not meet Gmail's current expectations.

If you receive this error:

1. Pause non-essential sends immediately for 24–48 hours. Continuing to send while throttled escalates the issue and can lead to permanent 550 rejections.
2. Confirm that SPF, DKIM, and DMARC are correctly configured and that your From: header aligns with your authentication.
3. Check [Google Postmaster Tools](https://postmaster.google.com/) and the Braze [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center/) (after connecting Google Postmaster) for your domain's compliance status and spam complaint rates. Your user-reported spam rate must stay below 0.1% (the hard ceiling is 0.3%).
4. After the pause, resume sending at 10–20% of previous volume to your most engaged recipients only. Increase volume slowly over several weeks only if no further 4xx errors occur.

For additional guidance, refer to [Google's Bulk Email Senders Guidelines](https://support.google.com/mail/answer/81126).

### How can I optimize images in Outlook?

Outlook often uses Microsoft Word rendering rather than standard browser rendering, which can cause images to render incorrectly or add borders around images.

If images display larger than their expected width in Outlook, add the following CSS to the image:

```css
max-width: 100%;
```

For example:

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

You can also wrap content so it hides in Outlook desktop using conditional comments:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Can I use SVG or WebP images in my email messages?

SVG images are not recommended for email due to limited support across email clients. Gmail and several other major email providers do not render SVG images, which can result in broken or missing images for recipients. WebP is not consistently supported across clients.

Instead, use widely supported formats such as PNG or JPEG so images render reliably.

### Can I embed videos in emails?

Embedded videos are not natively supported by many popular email clients such as Gmail, Outlook, and Yahoo. As a result, embedded video elements may not display as intended or may not appear at all. Additionally, embedding video directly in an email can significantly increase the email size, which increases the chance that the message may be marked as spam.

Instead, you can create a GIF or static image that resembles a video in a video player, then link that image to your video. When users click the image, they are directed to the video hosted on your website or a video platform.

### Can Liquid variables assigned in one part of the message composer be used in another?

No. Each part of the email (subject, body, headers, buttons, and so on) is generated separately, so Liquid assigned in one field is not available in another. Assign variables in each field that needs them.

### My email template is missing. Where is it?

First, confirm you have the [user permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) to view templates. To view saved email templates, go to **Content** > **Email**. You can filter templates by status and type (HTML or drag-and-drop).

### Do I need to register domains for relay or masked emails?

[Apple’s Private Email Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) requires you to register your sending domains in the Apple Developer Portal to prevent bounces. Google Shielded Email does not require a manual domain registration or allowlisting process.


### Can I add hyperlinks in email subject lines or preheaders?

No. Adding hyperlinks in email subject lines is not supported by mailbox providers. While some mailbox providers automatically scan subject lines and convert physical addresses, dates, or times into clickable links, this happens automatically on the recipient's device and is outside Braze's (or any ESP's) control.

Similarly, adding hyperlinks within the preheader is not supported across the email industry.

If you need functionality similar to clickable content in the subject line or preheader area, consider using [Gmail Promotions]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab) to add interactive annotations to your emails for Gmail users.

### What does the bounce reason `unable to get mx info` or `failed to get IPs from PTR record` mean?

In the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), a bounce reason similar to the following indicates a problem resolving the receiving domain's mail setup (the domain after the `@` in the address), not to Braze message composition:

Typical causes include:

- Missing, incorrect, or unreachable **MX records** for that domain
- Inbound mail hostnames that don't resolve or that fail **PTR (reverse DNS)** checks expected by receiving infrastructure
- Invalid or mistyped domains in the email address

**Next steps:**

- Confirm the address and domain spelling.
- If the address is correct, contact the mailbox owner or IT team for that domain.
- Ask them to audit MX and related DNS records, including PTR records for their mail servers, with their DNS provider.

Other recipients are usually unaffected. For how soft bounces appear in reporting, see [Soft Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Why do I get a spam alert when sending an email from Braze to myself?

If you send a test email from Braze to your own email address and see a spam warning or phishing alert—such as "the sending domain is similar to your company's domain, but we do not recognize it"—this is a common anti-phishing security feature, not an error with your Braze setup.

This alert typically appears when the sending domain of the email matches the recipient domain (for example, both are `@yourcompany.com`). Email security systems flag this because scammers often spoof domains that look similar to a recipient's company domain.

To verify your email is configured correctly:

1. View the original message (raw email headers) in your email client.
2. Check that SPF, DKIM, and DMARC authentication all pass.
3. If all three pass, your Braze email sending is configured properly.

To prevent this alert from appearing:

Ask your IT team to allowlist your Braze sending domain and IP addresses in your company's email security services or mail gateway. This tells your security system to trust emails from your Braze sending infrastructure.

