---
nav_title: Accounts
article_title: Account objects
page_order: 7
page_type: reference
description: "Use account objects to segment users, personalize messages with account data, and manage account records."
---

# Account objects

> Use account objects to segment and personalize messaging with account data.

{% alert important %}
Accounts is in Early Access. These instructions may change as the feature evolves.
{% endalert %}

With account objects, you can:

- Build segments with account criteria
- Personalize messages with account attributes through Liquid
- Manage account records in one place

Account objects are workspace-level data models connected to user profiles. An account record is one specific account and its associated field data.
Use account objects when account context, such as company attributes, helps you target and personalize messaging.
You can also model account hierarchies (such as parent and child accounts) and link one user profile to multiple accounts.

## Why use account objects?

Some use cases require account-level context, even when your campaigns and Canvases send to individual users.

Account objects let you store account data once and reuse it for segmentation and personalization across Braze.

This lets you:

- Segment by account attributes
- Personalize messages with shared account context (such as company name or industry)
- Model relationships between accounts and connect one user profile to multiple accounts

This approach replaces duplicating the same account attributes across many user profiles.

## Prerequisites

Before you start:

- Your workspace must be enabled for Accounts Early Access. Contact your Braze account team.
- You must already have users in Braze.
- After Accounts is enabled, it appears in **Data Settings** > **Accounts**. If this is your first time using Accounts, follow the on-screen initialization instructions.

## Account data model

Each account requires an external ID (`id`) and a name (`name`).

The account fields in this section define the Account object schema. Those fields apply to every individual account record you store in Braze.

Braze includes account objects with standard fields by default. You can add and remove custom fields based on your use case.

| Field name | Field type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Your system ID for the account (for example, CRM ID). Must be unique in your workspace. |
| `name` | string | Yes | Account name. |
| `type` | string | No | Account type, such as customer, partner, or reseller. |
| `annual_revenue` | number | No | Account annual revenue. |
| `industry` | string | No | Account industry. |
| `number_of_employees` | number | No | Employee count. |
| `address` | string | No | Street address. |
| `city` | string | No | City. |
| `state` | string | No | State or province. |
| `postal_code` | string | No | Postal code. |
| `country` | string | No | Country. |
| `notes` | string | No | Additional notes. |
| `website` | string | No | Website URL. |
| `main_phone` | string | No | Primary phone number. |
| `created_date` | time | No | Account creation timestamp. |
| `sic_code` | string | No | Standard Industry Classification code. |
| Custom fields | custom | No | Fields you define and manage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Account data model fields" }

## Data integration options

You can manage account records through:

- REST API endpoints for account records
- In-browser editing in **Data Settings** > **Accounts** for individual records

## Get started

### Step 1: Enable Accounts

Accounts is enabled at the company level. During Early Access, your Braze account team handles one-time enablement.

When Accounts is enabled, go to **Data Settings** > **Accounts** and complete the one-time initialization flow if prompted.

### Step 2: Add account records

Add or update account records through the REST API or in-browser editing.

### Step 3: Create a calculated filter for account criteria

Before segmenting on account data, create a calculated filter that defines your account criteria. For details, see [How calculated filters work]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#how-it-works).

### Step 4: Use the calculated filter in Segment Builder

In Segment Builder, select the calculated filter you created, then add any additional user attribute filters that support your campaign or Canvas targeting.

## Build account-based segments

After your account records and calculated filter are ready:

1. Go to [Segment Builder]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Add your preconfigured calculated filter for account criteria.
3. Add any additional user attribute filters.
4. Save your segment.

For example:

- **Calculated filter:** account `industry` is exactly `healthcare`
- **User attribute filter:** `days_since_last_login` is less than `30`

## Personalize with Liquid

Use the `{% raw %}{% data_object account %}{% endraw %}` Liquid tag to load account data for the user into the `data_objects` array.

{% alert note %}
When using **Preview and Test**, use a segment that includes account data so personalization can resolve correctly.
{% endalert %}

{% raw %}
```liquid
{% data_object account %}
Hi {{${first_name}}},
We'd love to invite you and your peers at {{ data_objects[0].name }}.
```
{% endraw %}

To iterate over all matched accounts:

{% raw %}
```liquid
{% data_object account %}
{% for acct in data_objects %}
- {{ acct.name }}
{% endfor %}
```
{% endraw %}

## API basics

You can use the REST API to manage account records during Early Access.

For endpoint details, refer to [Custom Objects endpoints]({{site.baseurl}}/api/endpoints/custom_objects).

For authentication and REST endpoint basics, refer to [Braze API overview]({{site.baseurl}}/api/basics).

## Frequently asked questions

### Can I add custom fields to accounts?

Yes. You can define and manage custom account fields in your workspace. For field requirements, see [Account data model](#account-data-model).

### Is Accounts a paid add-on?

No. Accounts isn't a paid add-on, and is available on all plans. During Early Access, your Braze account team must enable it for your workspace.
