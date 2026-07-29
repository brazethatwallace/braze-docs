---
nav_title: Custom code and JavaScript bridge
article_title: Custom code and JavaScript bridge for in-app messages
page_order: 2
page_type: reference
description: "Learn how to use the Custom code editor block in drag-and-drop in-app messages and the JavaScript bridge to log clicks and trigger Braze actions."
channel:
  - in-app messages
---

# Custom code and JavaScript bridge for in-app messages

> When you use the **Custom code** editor block in the drag-and-drop in-app message editor, you must call `brazeBridge` methods from within your custom HTML to log clicks and trigger SDK actions. The same JavaScript bridge is used for [custom HTML in-app messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) in the traditional editor.

If you add custom HTML, CSS, or JavaScript through a **Custom code** block, the Braze SDK cannot automatically attach click listeners to elements inside your code. You must explicitly call `brazeBridge.logClick()` for any clickable elements (links, buttons, and similar) that you want to track in campaign analytics.

For example, to log a click when a user taps a button in your custom HTML:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

For the full JavaScript bridge reference, including all available methods and click tracking options, see [JavaScript bridge](#javascript-bridge).

## Trigger SDK actions on submit

Built-in editor blocks handle common submit flows—for example, the [phone capture block]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages#phone-capture) subscribes users to an SMS or WhatsApp [subscription group]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) when they submit their phone number.

To run other SDK actions on submit—such as adding a user to a subscription group from a custom form—add a **Custom code** block and attach an `onclick` handler to your submit button. Wait for the `ab.BridgeReady` event before calling `brazeBridge` methods so the bridge is available.

Replace `YOUR-SUBSCRIPTION-GROUP-ID` with the subscription group ID from your Braze dashboard (**Audience** > **Subscription Group Management** > select a subscription group). For more information, see [SMS and RCS subscription groups]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

```html
<button id="submit-opt-in" type="button">Subscribe</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  document.querySelector("#submit-opt-in").onclick = function(){
    // Track the submit button click for analytics
    brazeBridge.logClick("subscribe");
    // Add the user to a subscription group
    brazeBridge.getUser().addToSubscriptionGroup("YOUR-SUBSCRIPTION-GROUP-ID");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

{% alert note %}
`addToSubscriptionGroup` was introduced in Android SDK v15.0.0, Web SDK v3.4.0, and iOS SDK v4.3.3. For web in-app messages, your app must set the [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) initialization option to `true`. For more information, see [Prerequisites]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#prerequisites) for the drag-and-drop editor.
{% endalert %}

{% alert tip %}
For SMS, RCS, or WhatsApp phone-number opt-in, use the [SMS, RCS, and WhatsApp sign-up form]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) template or the built-in phone capture block instead of custom JavaScript.
{% endalert %}

## JavaScript bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}
