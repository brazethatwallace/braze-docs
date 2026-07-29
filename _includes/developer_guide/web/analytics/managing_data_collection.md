## Disabling data tracking

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
To disable data-tracking activity on the Web SDK, use the method [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). This will sync any data logged before `disableSDK()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored.
{% endtab %}

{% tab google tag manager %}
Use the **Disable Tracking** or **Resume Tracking** tag type to disable or re-enable web tracking, respectively. These two options call [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) and [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Best practices

To provide users with the option to stop tracking, we recommend building a simple page with two links or buttons: one that calls `disableSDK()` when clicked, and another that calls `enableSDK()` to allow users to opt back in. You can use these controls to start or stop tracking via other data sub-processors as well.

{% alert note %}
The Braze SDK does not need to be initialized to call `disableSDK()`, allowing you to disable tracking for fully anonymous users. Conversely,`enableSDK()` does not initialize the Braze SDK so you must also call `initialize()` afterward to enable tracking.
{% endalert %}

## Resuming data tracking

To resume data collection, you can use the [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) method.

## Logout and Unregister Push

The Braze SDK provides methods to stop targeting a device when a user unregisters from push notifications or logs out. These methods remove push registration data from the current user on the Braze server and the SDK, so Braze no longer sends future push notification campaigns to that user.

### Logout {#logout}

When a user logs out from an application, call the SDK's `logout` method to remove the device's push registration from the current user and automatically perform cleanup actions on the SDK. The `logout` method performs the following:

- Unregisters the device's push token from the current user on the Braze server.
- If the unregister call succeeds, the SDK wipes locally-stored SDK data and disables the SDK.
- On failure, invokes the `errorCallback` to allow the integrator to take action.

The following example shows callback-based `logout` handling. Use it when you need immediate success and error handling, and replace the logging with your app flow.

```javascript
import { logout } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully logged out');
};

const errorCallback = () => {
  console.log('Failed to log out');
};

logout(successCallback, errorCallback);
```

#### Re-enable tracking and push after `logout`

After a successful `logout`, call [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk), then re-register for notifications with your operating system (OS) or push provider by following [Web push setup]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

#### Avoid immediate unregister calls

Avoid calling `logout` or `unregisterPush` directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister Push {#unregister-push}

To stop sending push to a device without additional automated cleanup, use the `unregisterPush` method. This removes the device's push token from the current user on Braze's server, and clears the locally-stored token.

The following example shows callback-based `unregisterPush` handling. Use it when you need immediate success and error handling, and replace the logging with your app flow.

```javascript
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully unregistered from push');
};

const errorCallback = () => {
  console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);
```

#### Re-register push after `unregisterPush`

After calling `unregisterPush`, re-register for notifications with your OS or push provider by following [Web push setup]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) before sending Braze push notifications again.

{% alert note %}
On supported browsers, when an active push subscription exists, `unregisterPush` also unregisters the Braze-managed service worker after unsubscribing from the browser Push API. If you set `manageServiceWorkerExternally` to `true`, the SDK does not unregister the service worker for you.
{% endalert %}

#### Avoid immediate unregister calls

Avoid calling `logout` or `unregisterPush` directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.
