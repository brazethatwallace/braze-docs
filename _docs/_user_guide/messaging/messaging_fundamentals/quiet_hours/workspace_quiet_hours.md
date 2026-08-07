---
nav_title: Workspace quiet hours
article_title: Workspace quiet hours
page_order: 4
page_type: reference
description: "This reference article covers what quiet hours are, how Braze handles messages during the quiet period, and how quiet hours interact with Intelligent Timing."
---

# Workspace quiet hours

> Workspace quiet hours let you set a default quiet hours window for a messaging channel across your entire workspace. Every campaign and Canvas that sends on that channel automatically respects the window, so you don't need to configure quiet hours on each campaign or Canvas individually.

Workspace quiet hours are separate from campaign- and Canvas-level quiet hours, which continue to work as they do today. Workspace quiet hours are meant to cover the default case (for example, a compliance requirement that applies across all of your SMS sends), while campaign- and Canvas-level quiet hours remain available for one-off exceptions.

{% alert important %}
Workspace Quiet Hours is currently available in Early Access. Functionality, configuration options, and UI described in this guide may change before general availability. Contact your Braze account team to request access.
{% endalert %}

## How it works

- **One window per channel:** each channel supports a single workspace quiet hours window, defined by a start time and an end time.
- **Local time zone:** like campaign- and Canvas-level quiet hours, workspace quiet hours apply in each recipient's local time zone, not your company's time zone.
- **Held, not discarded:** a message that would otherwise send during the window is held and delivered later, or aborted, depending on the campaign type (see “What happens to a held message”). Quiet hours never modify message content — they only affect timing.
- **Maximum window length:** a quiet hours window can't exceed 20 hours. This limit exists to prevent accidentally pausing all sending on a channel (for example, by setting the start and end time to the same value).

### Supported channels

You can set a workspace quiet hours window for any of the following channels:

- Content Cards
- Email
- In-app messages
- LINE
- SMS
- Push
    - This covers every push platform in your workspace
    - There is no option to set different quiet hours for individual platforms (for example, iOS vs. Android).

## Prerequisites

Before you can set up workspace quiet hours, confirm you have the following:

- "Edit Quiet Hours" permission to create or update workspace quiet hours. 
    - The "View Quiet Hours" permission lets a user view the configuration without editing it. Existing campaign and Canvas edit permissions are unaffected; those users can still edit quiet hours at the campaign or Canvas level.

## Set up workspace quiet hours


1.  Set a start time, end time, and channel for each workspace quiet hours window. A channel can have at most one workspace quiet hours window at a time.


The applicable workspace quiet hours window is surfaced in the campaign and Canvas editor for any channel in use. From there, you can opt out of the workspace default and apply a campaign- or Canvas-specific window instead, the same way you would opt out of a workspace-level frequency cap.

When you turn on or change a workspace quiet hours window, Braze shows which existing campaigns and Canvases are affected so you can review the impact before it takes effect. Updates to workspace quiet hours are recorded in a changelog, including who made the change and when, since this setting affects every campaign and Canvas on the channel.

Precedence: workspace vs. campaign or Canvas quiet hours
For any given campaign or Canvas, only one quiet hours setting is ever in effect at a time — workspace quiet hours, a campaign- or Canvas-specific window, or none. A campaign- or Canvas-level quiet hours window always takes precedence over the workspace default.
Configuration present
Which quiet hours applies
Campaign or Canvas has its own quiet hours window
The campaign- or Canvas-level window applies. Workspace quiet hours are ignored for that campaign or Canvas.
Campaign or Canvas has no quiet hours window of its own, and a workspace quiet hours window exists for the channel it uses
The workspace quiet hours window applies automatically.
campaign / Canvas is opted out
No quiet hours apply.

### What happens to a held message

What happens to a message that falls inside a quiet hours window depends on how the campaign or Canvas is triggered:

- **Action-triggered campaigns and Canvases:** fallback can be either Abort or Send at the next available time, the same options available today.
- **Scheduled campaigns with a fixed send time:** fallback is Abort. Braze doesn't delay a fixed-time send to the next available slot, since doing so could push a large volume of messages into a compressed sending window once quiet hours end.
- **Campaigns using Intelligent Timing:** no separate fallback is needed. Braze already factors the workspace quiet hours window into the optimal send time it calculates for each user, so messages aren't scheduled inside the window in the first place.
- **API-triggered campaigns and API campaigns:** fallback is Abort by default. Use the opt-out if you don't want workspace quiet hours applied to a request.

### API-triggered and API campaigns

Workspace quiet hours apply to API-triggered campaigns and API campaigns by default. You can't configure a custom, campaign-specific quiet hours window through these APIs, only the workspace default applies, unless you opt out.

To send without regard to a workspace quiet hours window, include the optional `ignore_workspace_quiet_hours` parameter in your request.

For scheduled API-triggered sends using `at_optimal_time`, workspace quiet hours are already factored into the optimal send time, similar to Intelligent Timing.

### Exclusions

The following are never held by workspace quiet hours, regardless of channel:
- Transactional and SLA-backed messages
- SMS auto-responses (for example, STOP or HELP keyword replies)
- Test sends and seed group sends

## Other considerations

- [Scheduled sends in company time]: workspace quiet hours are based on each recipient's local time zone, but a scheduled campaign's send time may be set in your company's time zone. That mismatch means a send time that looks fine in company time could still fall inside quiet hours for some recipients. Review the workspace quiet hours details shown in the campaign editor before sending.
- [Delivery after quiet hours ends]: if a large audience was held during the window, those messages can become eligible to send all at once when the window closes. Plan for this when a channel has a wide audience and a long quiet hours window.
- [Independent of frequency capping and rate limiting]: workspace quiet hours apply independently of frequency capping and rate limiting. A message that clears those controls can still be held by quiet hours, and a message held by quiet hours is still evaluated against rate limits once it's ready to send.


## Related settings

- [Campaign and Canvas quiet hours]: the existing, per-campaign/per-Canvas version of this feature. Workspace quiet hours don't replace it; they set the default that applies when a campaign or Canvas doesn't configure its own window.
- [Intelligent Timing]: calculates an optimal send time per user; when enabled alongside workspace quiet hours (outside the multichannel exceptions), quiet hours are factored into that calculation.
- [Frequency capping and rate limiting]: separate delivery controls that apply independently of quiet hours.

