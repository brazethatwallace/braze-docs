---
nav_title: Shareable preview
article_title: Share a message preview with stakeholders
page_order: 5
page_type: reference
description: "This reference article covers how to generate and share a preview link for a message or content, so that stakeholders without dashboard access can review it before it's sent."
---

# Share a message preview with stakeholders

> Shareable preview lets you generate a link to a preview of your message or content and share it with reviewers, such as stakeholders, legal teams, or compliance teams, who don't have access to your Braze dashboard. Recipients can view the preview in their browser without logging in to Braze.

## Supported channels

You can generate a shareable preview link for the following channels and content types:

- Banners
- Content Blocks
- Content Cards
- Email and email footer
- Landing pages
- LINE
- Push notifications
- Subscription pages
- SMS and RCS
- WhatsApp

{% alert note %}
Shareable preview is rolling out gradually and may not yet be available for every channel in your workspace. Contact your Braze account manager if you don't see the option for a channel listed in this section.
{% endalert %}

## How shareable preview works

The following behavior is consistent across all supported channels.

### Generating a link

While composing your message or content, select **Copy preview link** (or a similar option depending on the channel) to generate a shareable link. Braze automatically copies the link to your clipboard.

- The link opens a static, read-only snapshot of your message as it appeared at the moment you generated the link. It doesn't update automatically as you keep editing. Generate a new link to capture your latest changes.
- If your message includes personalization, such as Liquid or Connected Content that resolves against a test user, a custom user profile, or a random user, the preview reflects that same personalization, matching what you see in **Preview and Test**.
- Selecting **Regenerate link** creates a new snapshot with its own new expiration date. This doesn't invalidate the previous link. Both links continue to work independently until each expires.

### Viewing the link

Anyone with the link can view the preview. No Braze login or dashboard permissions are required.

{% alert important %}
Treat a link like any other shareable document: only send it to people you intend to have access, and avoid posting it somewhere public.
{% endalert %}

### Link expiration

- Every shareable preview link expires seven days after it's generated.
- Once a link expires, it no longer opens. Generate a new link from the composer to get a fresh one.
- There's no way to manually revoke or deactivate a link before it expires. Regenerating a link doesn't revoke the previous one; each link simply expires on its own seven-day schedule.

## Per-channel nuances

While the core experience is the same everywhere, a few channels have small differences worth knowing about.

| Channel | What's different |
|---|---|
| Email | The preview includes the message's To, From, and Subject line fields, in addition to the message body. <br><br>If you're personalizing as a custom user, values entered as API-trigger properties or event properties may not appear in the preview, even though they display correctly in **Preview and Test**. Custom attributes, test users, and random users aren't affected. |
| Banner (drag-and-drop editor) | The preview reflects the content as of the last time you opened the **Preview** tab in the composer, not necessarily your most recent edits. <br><br>Open **Preview** again before generating or regenerating a link to make sure it's current. |
| SMS and RCS | These are both governed by the same shareable preview functionality, but each generates its own independent link. |
| WhatsApp | Shareable preview is available separately for both WhatsApp template messages and WhatsApp response messages. |
| Content Blocks, email footers, and subscription pages | These generate a preview of the standalone content, independent of any specific campaign or Canvas it's used in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Per-channel nuances" }

{% alert note %}
Shareable preview is not available for in-app messages.
{% endalert %}

## Frequently asked questions

{% details Does the recipient need a Braze account to view the preview? %}
No. Anyone with the link can view the preview in their browser without logging in.
{% enddetails %}

{% details Does the preview update if I keep editing my message? %}
No. A shareable preview link is a snapshot at the time it was created. Select **Regenerate link** to capture your latest changes and get a new link.
{% enddetails %}

{% details How long does the link stay active? %}
Seven days from when it was generated. If you regenerate the link, the new link gets its own seven-day expiration, separate from the original.
{% enddetails %}

{% details Can I revoke a link early? %}
No, you cannot revoke a link. Regenerating the link doesn't invalidate the previous one. Either link works until it expires after seven days.
{% enddetails %}
