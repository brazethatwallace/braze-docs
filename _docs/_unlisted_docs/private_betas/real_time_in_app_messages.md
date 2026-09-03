---
nav_title: Real-time in-app message delivery
article_title: Real-time in-app message delivery
permalink: "/real_time_in_app_messages/"
description: "This page covers the real-time in-app message delivery early access, which delivers in-app messages to a device as soon as a user becomes eligible instead of waiting for the next session start."
page_type: reference
hidden: true
noindex: true
---

# Real-time in-app message delivery

> With real-time delivery, Braze sends an in-app message to the device as soon as the user becomes eligible for it. Users no longer need to start a new session to receive an in-app message they became eligible for mid-session.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Real-time in-app message delivery' type='early_access' %}

## How it works

Without real-time delivery, the SDK requests eligible in-app messages at session start and caches them on the device. A user who becomes eligible partway through a session doesn't receive the message until their next session begins. For more information on this behavior, see [Trigger in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).

With real-time delivery, Braze pushes the message to the device over a live connection that the SDK maintains during the session. Braze sends a message in two cases:

- A user becomes eligible for an in-app message campaign.
- A user advances to an in-app message step in a Canvas.

Real-time delivery changes when a message reaches the device. Display behavior stays the same: the message waits for its trigger event before it appears.

### What this means for your campaigns

| Scenario | Without real-time delivery | With real-time delivery |
| --- | --- | --- |
| A user becomes eligible for an in-app message campaign mid-session | The message arrives at the next session start | The message arrives during the current session |
| A user reaches an in-app message step in a Canvas mid-session | The message arrives at the next session start | The message arrives during the current session |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Real-time in-app message delivery comparison" }

## SDK requirements

Real-time delivery requires the following minimum SDK versions:

{% sdk_min_versions swift:18.0.0 android:43.1.1 %}

Devices continue to receive in-app messages at session start regardless of SDK version.

## Current limitations

- **The Web SDK isn't yet supported:** Real-time delivery is available for the Swift and Android SDKs during early access.
- **Edits to a live campaign apply at the next session start:** If you change an in-app message that a device has already received, that device keeps the version it has until the user's next session begins.

## Participate in early access

1. Contact your Braze account manager to have your workspace added to early access.
2. Upgrade your app to the minimum SDK version for your platform.
3. Release the upgraded app to your users.

Real-time delivery requires no dashboard configuration, campaign changes, or SDK code changes. After your workspace is added to early access, real-time delivery applies to your existing in-app message campaigns and Canvases.

## Share feedback

Braze is actively developing this feature, and your feedback shapes what ships at general availability. Send your account manager your observations on delivery timing, anything that behaved differently than you expected, and the scenarios you'd like real-time delivery to cover next.
