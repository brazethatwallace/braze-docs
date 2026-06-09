---
nav_title: Convercus
article_title: Convercus
description: "This reference article outlines the partnership between Braze and Convercus, a loyalty and coupon platform that enriches Braze with real-time loyalty data and lets Braze campaigns trigger loyalty actions in Convercus."
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en) is a SaaS loyalty and coupon platform that helps brands and retailers grow customer frequency, basket value, and repurchase rates through omnichannel loyalty programs and personalized coupon campaigns.

_This integration is maintained by Convercus._

## About the integration

The Braze and Convercus integration is bidirectional: loyalty data flows into Braze in real time as custom attributes, custom events, and purchases, and Braze Canvases and campaigns can trigger loyalty actions in Convercus through webhooks. Use synced member tier, points balance, purchases, and coupon activity in Segments, Liquid, and Connected Content. From Braze journeys, you can also assign coupons, book, earn, and burn point transactions, and update email subscription preferences in Convercus.

Convercus hosts the integration, so you do not install additional infrastructure. Where most loyalty connectors only push data one way, Convercus closes the loop: react in Braze to a loyalty event, take an action in Convercus, and measure the result back in Braze.

## Use cases

1. **Tier-up celebration:** When a member moves up a loyalty tier in Convercus, trigger a personalized Braze Canvas with a welcome message, a tier-exclusive perk, and the member's new tier and points balance.
2. **Birthday and milestone bonuses:** From a Braze journey, book bonus points in Convercus on a member's birthday or anniversary, then send a celebratory message confirming the new balance.
3. **Lapsed-member win-back:** For inactive members, have Braze assign a personalized coupon in Convercus through a webhook and deliver it across email, push, and in-app messages.
4. **Live points balance in messaging:** Use Connected Content to pull a member's real-time points balance into Braze Liquid, powering cadences such as "you're X points away from your next reward".

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A Convercus account | An active Convercus program. Contact your Convercus account manager if you are not yet a customer. |
| A Braze REST API key | A Braze REST API key with the `users.track` permission. Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

You need a consistent user identifier between systems: the value used as `external_id` (or the chosen identifier type) in Braze must match the corresponding member identifier in Convercus. Otherwise, events do not attribute to the correct profile.

## Integration

### Step 1: Configure Braze in Convercus Selfservice

In Convercus Selfservice (the customer-facing admin UI—open it using the URL your Convercus account manager provides), open the program you want to connect to Braze and use the **Braze integration card** to:

1. Configure the Braze connection by completing the integration form:

   | Field | Description |
   | --- | --- |
   | `apiKey` | Your Braze REST API key (with the `users.track` permission). |
   | `apiEndpoint` | Your Braze REST endpoint, for example `https://rest.iad-01.braze.com`. |
   | Identifier type | Either `external_id` or `user_alias`. Determines how Convercus members are matched to Braze user profiles. |
   | `defaultOptins` | Multi-select of the program's opt-in channels (from `membershipOptins`). Used as the default for the email subscription webhook when the request omits `optins`. The Braze config is treated as **incomplete** until at least one is selected. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Configure Braze in Convercus Selfservice" }

2. Create an API key for inbound calls. Create a per-program `X-Convercus-Key` credential. The raw key is shown once at creation, prefixed `cvc_` (format: `cvc_<base64url>`). Store it in Braze when you configure the webhook campaigns and Connected Content blocks in Step 2. Keys can be revoked at any time from the same card; revocation takes effect immediately.

After you save the Braze connection, Convercus immediately starts streaming loyalty events for that program to Braze. No additional infrastructure setup is required.

{% alert note %}
Each Convercus program is configured independently. A single Convercus tenant can connect different programs to different Braze workspaces, each with its own API key.
{% endalert %}

### Step 2: Configure webhooks in Braze

To trigger Convercus actions from a Canvas or campaign, create Braze webhook actions that call the Convercus integration service. All requests must include the following headers:

- `X-Convercus-Key: cvc_…` - the API key generated in Step 1.
- `Content-Type: application/json`

All endpoints live under the base URL `<SERVICE_HOST>/v1/programs/{programId}`. Replace `<SERVICE_HOST>` with the host provided by your Convercus account manager and `{programId}` with your Convercus program ID.

| Action | Endpoint |
| --- | --- |
| Assign a coupon to a member | `POST /campaigns/{couponId}/assign` — returns `{ "couponCode": "..." }`. |
| Assign a coupon to multiple members | `POST /campaigns/{couponId}/assign/batch` — up to 500 members in one call; body accepts optional `valid_from` / `valid_to`. Returns `{ "batchId": "..." }`. |
| Book earn / burn points | `POST /members/{accountId}/bookings` — create an `EARNBOOKING` or `BURNBOOKING` on a member account. Returns `{ "bookingId": "..." }`. |
| Sync email subscription preferences | `POST /subscriptions/email` — set the member's opt-ins to `allowed` or `declined`. Opt-in channels resolve as request `optins` > `defaultOptins`. Returns `200` (all OK), `207` (partial — see `succeeded` / `failed`), or `400` (unknown opt-ins or none configured). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure webhooks in Braze" }

Example — assign a coupon to a member:

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

The other actions follow the same pattern, changing only the endpoint and the body. For example, a points booking posts to `/members/{accountId}/bookings` with `booking_type` (`EARNBOOKING` or `BURNBOOKING`), `booking_type_code`, `points`, and `reason`; the email subscription webhook posts to `/subscriptions/email` with `account_id` and `status` (`allowed` or `declined`).

#### Error responses and retries

| Status | Meaning |
| --- | --- |
| `200` | Success. |
| `207` | Multi-Status — for the email subscription webhook only, when some memberships were updated and others failed. |
| `400` | Request body failed validation. |
| `401` | `X-Convercus-Key` is missing or invalid. |
| `5xx` | The upstream Convercus call failed. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Error responses and retries" }

{% alert warning %}
5xx responses are **not safe to retry without confirming success**—these operations are not idempotent, and retries may double-assign coupons or double-credit point bookings. Disable Braze auto-retry on 5xx for these webhooks, or configure a very low maximum retry count.
{% endalert %}

### Step 3: Verify data in Braze

1. Trigger a loyalty event in Convercus—for example, a status level change, a points transaction, or a coupon redemption.
2. Open the matching user in Braze and confirm that the expected custom attribute, custom event, or purchase appears on the profile. Users are matched by `external_id` (or the identifier type chosen in Step 1).
3. To verify the opposite direction, run a Braze test send that calls one of the webhooks from Step 2 and confirm the action in Convercus (coupon assigned, points booked, or subscription updated).

## Use Convercus with Braze

### Step 1: Personalize messages with synced loyalty data

After the integration is live, Convercus events arrive on each user profile in Braze through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint and can be used like any other native data:

1. Use loyalty custom attributes (for example, `convercus_status_level`, `convercus_balance`) in **Segments** to target tier holders, high-balance members, or recently downgraded users.
2. Use custom events (for example, `convercus_status_level_changed`, coupon and membership events) as **trigger steps** in Canvas or as filters in re-engagement campaigns.
3. Reference any of these fields in **Liquid** for in-message personalization (subject lines, body copy, push titles).
4. Use `purchase` events streamed from Convercus to drive product-aware journeys (replenishment, category upsell, post-purchase review requests).

#### Custom attributes

| Attribute | Description |
| --- | --- |
| `convercus_account_id` | The member's Convercus account ID — unique within a Convercus program / Braze workspace. |
| `convercus_user_id` | The Convercus user ID identifying the underlying person across multiple Convercus programs. |
| `convercus_partner_id` | Identifier of the Convercus Partner (merchant/brand) through which this member enrolled. Useful for segmentation in coalition programs. |
| `convercus_member_role` | The member's role within the loyalty program. |
| `convercus_status_level` | The member's current tier or status level. |
| `convercus_balance` | Object with the member's current `points`, `lockedPoints`, and `statusPoints`. |
| `email_subscribe` | Email subscription state derived from Convercus opt-ins (`opted_in`, `subscribed`, or `unsubscribed`). |
| `push_subscribe` | Push subscription state derived from Convercus push token events (`opted_in` or `unsubscribed`). |
| Standard profile fields | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| Custom user properties | Any custom properties defined on the Convercus user object are forwarded as Braze custom attributes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom attributes" }

{% alert note %}
Within a Braze workspace, members are uniquely identified by `convercus_account_id`. `convercus_user_id` identifies the underlying person across multiple Convercus programs and is provided for cross-program analytics; for segmentation within Braze, use `convercus_account_id`.
{% endalert %}

**`email_subscribe` mapping**

| Convercus state | Braze `email_subscribe` |
| --- | --- |
| `allowedOptins` entry for `email consent` or `newsletter` | `opted_in` |
| `declinedOptIns` entry for those channels (and no allowed entry) | `unsubscribed` |
| No record either way | `subscribed` (Braze's neutral default) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom attributes" }

#### Custom events

| Event | Triggered when |
| --- | --- |
| `convercus_account_created` | A new account is created in Convercus. |
| `convercus_membership_added` | An existing account joins a loyalty program. |
| `convercus_membership_created` | A new membership is created. |
| `convercus_membership_changed` | A membership's data changes. |
| `convercus_membership_optins_changed` | A member's opt-in preferences change. |
| `convercus_membership_terminated` | A membership ends. |
| `convercus_status_level_changed` | A member's tier or status level changes. |
| `convercus_balance_changed` | A member's points balance changes. |
| `convercus_account_transaction` | A loyalty transaction is rated. |
| `convercus_coupon_assigned` | A coupon is assigned to the member. |
| `convercus_coupon_redeemed` | The member redeems a coupon. |
| `convercus_user_logged_in` | The member signs in to a Convercus-powered surface. |
| `convercus_user_logged_out` | The member signs out. |
| `convercus_user_created` | A new user is created. |
| `convercus_user_changed` | A user's profile data changes. |
| `convercus_push_token_created` | A push token is registered for the member. |
| `convercus_push_token_deleted` | A push token is removed. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom events" }

#### Purchases

Convercus transactions of type `EARNTRANSACTION` (points earned from customer spend) are reported to Braze as [purchases]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#purchase-object-specification) and counted in Braze revenue analytics, RFM segmentation, and predictive features—using the transaction ID as the product identifier and the transaction amount and currency as price and currency.

Transactions of type `PAYWITHPOINTSTRANSACTION` (points burn) are **not** reported as purchases—they flow as the `convercus_account_transaction` custom event so they remain available for segmentation. Reversals and cancellations of earn transactions are reported as negative-price purchases, keeping Braze revenue aligned with Convercus.

### Step 2: Fetch live loyalty data with Connected Content

For values that must be fresh at send time—current points balance, active coupons, latest tier—call Convercus from Braze using [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) instead of relying on the most recently synced attribute. Both endpoints sit under the same base URL as the webhooks and require the `X-Convercus-Key` header.

| Data | Endpoint | Returns |
| --- | --- | --- |
| Member profile | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| Member coupons | `GET /members/{accountId}/coupons` | List of active, redeemable coupons (status, value, validity window, title, description). Append `?lang=<code>` (for example, `?lang=de`) to localize `title`/`description`; defaults to `en`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Fetch live loyalty data with Connected Content" }

Connected Content endpoints always return HTTP 200 on expected failures so Liquid templates can branch on the `error` field:

| Response | Meaning |
| --- | --- |
| `200` + payload | Success. |
| `200 { "error": "member_not_found" }` | The account does not exist in this program. |
| `200 { "error": "internal_error" }` | Upstream or unexpected failure. |
| `401` | `X-Convercus-Key` is missing or invalid (handle at integration time, not in Liquid). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Fetch live loyalty data with Connected Content" }

Example — render a member's loyalty status (tier, points, and active offers):

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

Always wrap Connected Content in conditionals (check `member.error` and empty `coupons`) so a temporary lookup failure never ships a broken message. Cache the profile (`cache_max_age 300`) but not coupons (`cache_max_age 0`), since coupon status can change between sends.

## Considerations

- **Latency:** Convercus-to-Braze events propagate through Kafka and reach Braze in seconds under normal load.
- **Braze rate limits:** The integration retries automatically on `429` responses, honoring Braze's `x-ratelimit-retry-after` header with exponential backoff.
- **Connected Content caching:** Braze caches Connected Content responses for several minutes by default. For values that must be exact at send time (such as points balance), shorten or bypass the cache window in the Connected Content call.
- **One configuration per program:** Each loyalty program maps to a single Braze workspace. To connect a second workspace, configure it on a separate program.
- **Observability:** Per-program API call statistics and error history (both directions) are retained for 90 days and available from the Braze integration card in Selfservice.

## Troubleshooting

- **Events do not appear in Braze:** Verify that the value used as the identifier (selected in Step 1) matches the user's `external_id` (or chosen identifier type) in Braze. Mismatched identifiers cause events to be attributed to the wrong profile or dropped.
- **Webhook returns `401`:** The `X-Convercus-Key` header is missing or the `cvc_…` API key has been revoked. Regenerate the key in Selfservice and update the webhook action in Braze.
- **Webhook returns `400`:** The request is missing `Content-Type: application/json`, or the payload does not match the documented schema. For the email subscription webhook, a `400` also means the requested opt-ins are unknown to the program or none are configured.
- **Deeper debugging:** Review the per-program API call statistics and error history on the Braze integration card in Selfservice, or contact your Convercus representative.
