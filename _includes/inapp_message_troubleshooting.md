### Troubleshooting display {#troubleshooting-in-app-message-display}

If your app is requesting and receiving in-app messages but they aren't showing, device-side logic may be preventing display:

1. Is the trigger event firing as expected? To test, configure the message to trigger on a different action (such as session start) and verify whether it displays.
{% if include.sdk == "iOS" %}
2. Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit), which defaults to 30 seconds.
{% elsif include.sdk == "Android" %}
2. Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit), which defaults to 30 seconds.
{% elsif include.sdk == "Web" %}
2. Triggered in-app messages are rate-limited based on the [minimum time interval between triggers]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit), which defaults to 30 seconds.
{% endif %}
3. Failed image downloads prevent in-app messages with images from displaying. Check device logs for download failures. Try removing the image temporarily to see if the message displays.
{% case include.sdk %}
  {% when "iOS" %}
4. If you've set a delegate to customize in-app message handling, confirm it isn't suppressing display. See [Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift).
  {% when "Android" %}
4. If you've set a delegate to customize in-app message handling, confirm it isn't suppressing display. See [Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
  {% when "Web" %}
4. If you use custom in-app message handling through [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), verify the callback isn't suppressing display. See [Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web).
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. If device orientation doesn't match the in-app message setting, the message won't display.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Depending on network conditions, images may download before display. On slow connections or low-performance devices, allow extra time or optimize asset size.
{% endcase %}

{% if include.sdk == "iOS" %}
### Impressions and clicks aren't being logged

If you've set an in-app message delegate to manually handle message display or click actions, you must manually [log clicks](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) and [impressions](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) on the in-app message.
{% elsif include.sdk == "Android" %}
### Impressions and clicks aren't being logged

If you've set an in-app message delegate to manually handle message display or click actions, you must manually log clicks and impressions on the in-app message.
{% endif %}
