---
article_title: Rate Limiting for Push Campaigns and Multichannel Canvases
permalink: /rate_limiting_v3/
page_type: reference
description: "This article describes the delivery speed rate limits for push campaigns and multichannel Canvases."
---

# Rate limiting for push campaigns and multichannel Canvases

> This page covers rate limiting for push campaigns and multichannel Canvases, including considerations to keep in mind as you regulate your messages.

When setting the delivery speed rate limits for push campaigns and multichannel Canvases, you can now choose between setting either:

- Per-channel rate limits
- An overall rate limit that's shared across all message channels. 

{% alert important %}
Rate limiting for push campaigns and multichannel Canvases is in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

The following abilities **aren't** included in this early access:

- Setting per-channel rate limits on multichannel campaigns of any type and API-triggered Canvases
- Setting a global rate limit
- Setting per-Message step rate limits in Canvas

## Considerations

- This rate limiting update doesn't prevent you from setting a very low rate limit. This means without this prevention in place, you would be able to set a rate limit, and, depending on the audience size, could cause your messages to be sent at an extremely slow rate.
- The **Send Settings** summaries for campaigns and Canvases may contain inaccurate descriptions for the rate limits that have been set: <br><br>![Send Settings for campaigns where there are no limitations on the rate at which users will receive messages.]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- Rate limiting for multichannel campaigns (not Canvases or push campaigns) will reflect the [non-updated multichannel campaign rate limiting behavior]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). We recommend avoiding creating rate-limited multichannel campaigns while part of this stage of early access.


