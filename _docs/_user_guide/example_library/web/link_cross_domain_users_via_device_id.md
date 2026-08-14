---
nav_title: Link cross-domain Web SDK users
article_title: Link cross-domain Web SDK users through device ID
page_order: 1
page_type: reference
description: "Pass the Braze Web SDK device ID from Kitchenerie's marketing site to a separate shop domain so anonymous activity shares one user profile."
---

# Link cross-domain Web SDK users through device ID

> Pass the Braze Web SDK device ID through the destination URL when two domains cannot share cookies, so anonymous sessions on both sites map to the same Braze user profile.

## About this example

Kitchenerie hosts a marketing site (`kitchenerie.com`) and a shop (`kitchenerie.shop`). Each domain has its own Braze Web SDK integration. Browser cookies do not cross domains, so Braze assigns separate device IDs—and separate anonymous profiles—when the same user moves from the marketing site to the shop.

This pattern:

1. Reads the device ID on the source domain with `getDeviceId` after SDK initialization
2. Appends it to outbound links as a query parameter (for example `brazeDeviceId`)
3. On the destination domain, reads that parameter and passes it to `braze.initialize` through the `deviceId` option

The handoff matters most for anonymous users. After the user logs in on the shop, `changeUser` with an `external_id` becomes the durable identifier across devices. See [Set user IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).

Both domains should use the same Braze workspace API key and SDK endpoint so events land on one profile.

## Considerations

- **Same browser only:** The device ID is per browser. This pattern does not link activity across different browsers, devices, or profiles. Use `external_id` through `changeUser` for authenticated, cross-device identity.
- **Call timing:** Retrieve the device ID only after the Web SDK is initialized on the source domain. Calling `getDeviceId` before `initialize` does not return a value.
- **Initialization-only `deviceId`:** The Web SDK reads `deviceId` once at `initialize`. There is no post-initialization `setDeviceId` that changes the active device ID. Read the URL parameter on the destination domain before calling `initialize`.
- **Missing parameter:** Direct visits, bookmarks, or third-party referrals to the shop without `brazeDeviceId` should fall back to default device ID assignment—expected when there is no source-domain ID to inherit.
- **Privacy and URL exposure:** Query parameters appear in browser history, server logs, and may leak through referrer headers. The device ID is not PII by itself, but strip the parameter after consumption if your privacy team requires it (see Step 2).
- **Test end-to-end:** Confirm Domain 2 events use the expected device ID with network inspection.
- **Illustrative code:** Adapt hostnames, link selectors, and error handling to your site. Test in your development environment before production.

## Setup

### Step 1: Append the device ID to cross-domain links on the source domain

On `kitchenerie.com` (Domain 1), initialize the Web SDK as usual, then append the current device ID to links that point to `kitchenerie.shop` (Domain 2).

Choose a query parameter name that does not collide with your site (this example uses `brazeDeviceId`). The same idea applies to server-rendered links, client-side navigation, or iframe `src` values you control.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

If your SDK version exposes `getDeviceId` synchronously (no callback), call it after initialization instead:

```javascript
const deviceId = braze.getDeviceId();
```

See [Web SDK repository guide — Get Device ID]({{site.baseurl}}/developer_guide/sdk_repository_guides/web/#get-device-id) and [Initialization options — `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web/#initialization-options).

### Step 2: Read the device ID and initialize the Web SDK on the destination domain

On `kitchenerie.shop` (Domain 2), read `brazeDeviceId` from the query string before `initialize`, and pass it in the initialization options when present.

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

When the user logs in, call `changeUser` with their `external_id` so future activity is tied to the identified profile.

### Step 3: Verify the handoff

1. Open Domain 1 in a browser where you are not logged in.
2. Follow a cross-domain link to Domain 2.
3. In the browser network tab, confirm Domain 2 sends events with the same device ID Domain 1 used.
4. Repeat with a direct visit to Domain 2 (no query parameter) and confirm a new device ID is assigned.

## Related articles

- [Web SDK repository guide]({{site.baseurl}}/developer_guide/sdk_repository_guides/web/)
- [Multi-domain integration for the Braze Web SDK]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Set user IDs through the Braze SDK]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/)
- [Anonymous users]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/)
- [User profile lifecycle]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [Web SDK storage]({{site.baseurl}}/developer_guide/storage/)
