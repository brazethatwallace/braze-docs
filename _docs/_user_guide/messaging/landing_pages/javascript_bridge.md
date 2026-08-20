---
nav_title: JavaScript bridge
article_title: JavaScript bridge for landing pages
page_order: 5
page_type: reference
description: "Learn how to use the brazeBridge JavaScript bridge to log events, set custom attributes, and trigger Braze actions from a landing page's Custom Code block."
---

# JavaScript bridge for landing pages

> Landing pages support a JavaScript "bridge" for connecting your custom code (HTML, CSS, and JavaScript) to the Braze SDK. 

Access the bridge by using `brazeBridge` in a Custom Code block to log events, set custom attributes, identify users, and more when a visitor interacts with your landing page.

## How it works

Landing pages let you add custom HTML, CSS, and JavaScript to a **Custom Code** block for greater control over the look, feel, and behavior of your page. Custom Code blocks can use the [JavaScript bridge](#supported-methods) to log events, set custom attributes, identify users, and more:
- Log custom events and purchases
- Set standard and custom user attributes
- Track clicks and form submissions
- Identify users

If you reuse `brazeBridge` code from in-app messages or Banners, it should still run on landing pages. Methods that don't apply to landing pages are ignored and log a browser console warning instead of causing an error. For details, see [Methods not supported on landing pages](#methods-not-supported-on-landing-pages).

{% alert important %}
The landing page bridge is asynchronous; each method returns a Promise. That differs from the [custom HTML in-app message bridge]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), whose methods return immediately. If the next step in your script depends on a bridge call finishing—such as redirecting the page, submitting a form, or sending data to Braze—use `await` or `.then()` and don't assume the call completed synchronously.
{% endalert %}

## Bridge availability

When a visitor opens your landing page, `brazeBridge` is already available in your **Custom Code** JavaScript. Call bridge methods directly in landing pages—you don't need to wait for a separate ready event like in-app messages use with `ab.BridgeReady`.

Having the bridge object available doesn't mean the Braze SDK is initialized for that visitor. The SDK initializes for a landing page visit in either of these cases:

- The visitor opens the page through a [landing page Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) sent through a Braze channel (email, SMS, push, and so on). The SDK initializes automatically when the page loads.
- The visitor submits the page's form—for example, by clicking a **Submit** button that sends form data. This includes `brazeBridge` calls made inside a [custom form block's]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) `registerFormInput` callbacks, since those run as part of form submission.

If a visitor opens the landing page directly, without a landing page Liquid tag, and never submits the form, the page is anonymous to Braze, and bridge method calls have no effect.

{% alert note %}
`window.lpBridge` and `window.appboyBridge` reference the same bridge object, but both are deprecated. Use `window.brazeBridge`.
{% endalert %}

## Example

Because the methods are asynchronous, use an async handler and `await` the calls when order or completion matters:

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## Supported methods

The following `brazeBridge` methods return a promise and are supported in landing page **Custom Code** blocks. `await` them or use `.then()` when you need to sequence work or guarantee completion.

### Top-level methods

| Method | Description |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | Identify the user with a unique ID. |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | Log a custom event. |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | Log a purchase. |
| `brazeBridge.requestImmediateDataFlush(callback?)` | Flush queued data to the Braze servers. |
| `brazeBridge.logClick(trackingId)` | Log a landing page click (`lp_c`) for the given tracking ID. See [Click tracking](#click-tracking). |
| `brazeBridge.logSubmit()` | Log a landing page form submission (`lp_fs`). Landing page-specific. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Top-level methods" }

### `getUser()` methods

{% alert note %}
`brazeBridge.getUser()` returns a plain object synchronously, so you don't `await getUser()`; the methods on the returned object (such as `getUser().setEmail(email)`) return Promises.
{% endalert %}

`getUser()` returns an object exposing the following user methods. Each method returns a Promise.

| Method | Description |
| --- | --- |
| `getUser().setFirstName(firstName)` | Set the user's first name. |
| `getUser().setLastName(lastName)` | Set the user's last name. |
| `getUser().setEmail(email)` | Set the user's email address. |
| `getUser().setPhoneNumber(phoneNumber)` | Set the user's phone number. |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | Set the user's gender: male, female, other, unknown, not applicable, or prefer not to say, respectively. |
| `getUser().setDateOfBirth(year, month, day)` | Set the user's date of birth. |
| `getUser().setCountry(country)` | Set the user's country. |
| `getUser().setHomeCity(city)` | Set the user's home city. |
| `getUser().setLanguage(language)` | Set the user's language. |
| `getUser().setCustomUserAttribute(key, value, merge?)` | Set a custom user attribute. |
| `getUser().addToCustomAttributeArray(key, value)` | Add a value to a custom attribute array. |
| `getUser().removeFromCustomAttributeArray(key, value)` | Remove a value from a custom attribute array. |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | Increment a numeric custom attribute. |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | Set a custom location attribute. |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | Add the user to an email or SMS subscription group. |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | Remove the user from an email or SMS subscription group. |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Set the email notification subscription status. |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Set the push notification subscription status. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="getUser() methods" }

## Click tracking

Use `brazeBridge.logClick(trackingId)` to track clicks on your landing page. Each call logs a landing page click event (`lp_c`) tagged with the tracking ID you pass:

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
Landing page click tracking differs from in-app messages, which use `logClick('0')` and `logClick('1')` as conventional IDs for "Button 1" and "Button 2". Landing pages have no equivalent special button IDs. Every `logClick(trackingId)` call logs an `lp_c` event keyed by the tracking ID you provide.
{% endalert %}

## Methods not supported on landing pages

The following methods work in in-app messages and Banners but aren't supported on landing pages. If your code calls one on a landing page, Braze ignores the call. Your page keeps working, but you may see a warning in the browser's developer console.

| Method | Notes |
| --- | --- |
| `brazeBridge.closeMessage()` | There's no message UI to close on a landing page. |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | Push permission isn't requested from a landing page. |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | Web push registration isn't available on landing pages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Methods not supported on landing pages" }

## Related content

- [Create custom form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) covers a more advanced use of this bridge: connecting a fully custom UI to a landing page form.
- [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
