---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "This reference article outlines the partnership between Braze and Better Email, a collaborative email creation platform built around an Email Design System that lets you export production-ready templates to Braze."
page_type: partner
search_tag: Partner
---

# Better Email

> [Better Email](https://www.betteremail.dev) is a collaborative email creation platform built around an Email Design System. Teams can design, manage, and export production-ready emails from a shared system of blocks and styles, ensuring brand consistency at scale without relying on developers or agencies.

_This integration is maintained by Better Email._

## About the integration

The Braze and Better Email integration allows you to create and manage email templates in Better Email's collaborative editor and export them directly to Braze as ready-to-use email templates.

Re-exporting an email updates the existing Braze template instead of creating a duplicate, so your template library stays clean.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Better Email account | A Better Email account with admin access to create integrations |
| Braze REST API key | A Braze REST API key with full **Templates** permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Use the REST host, not the dashboard URL—for example, `rest.fra-01.braze.eu`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Use cases

Better Email is built for marketing teams who want to manage emails through a design system and export them to Braze without manual HTML work. It's great for those who:

- Maintain a large library of email templates and need consistency across all of them
- Want to enforce brand guidelines through a shared Email Design System
- Collaborate across teams—designers, marketers, and developers—on email production
- Use Braze for campaign execution and want to remove the handoff bottleneck between design and deployment

## Integrate Better Email with Braze

### Step 1: Find your Braze values

In your Braze dashboard, collect the following:

- **Instance URL** — Use the REST host, not the dashboard URL (for example, `rest.fra-01.braze.eu`).
- **API key** — A REST API key with full **Templates** permissions, created under **Settings** > **API Keys**.

### Step 2: Set up the integration in Better Email

1. Go to **Integrations**.
2. Create a new integration.
3. Enter a name for the integration (for example, `Braze`).
4. Select **Braze** as the type.
5. Optionally, restrict the integration to specific users or groups under **Access**.
6. Select **Save**.
7. Enter the **Instance URL** and **API Key**.
8. Enable the integration.
9. Select **Save** again.

### Step 3: Export to Braze

When the integration is active, open any email in Better Email and select **Export** > **Braze**.

Better Email creates or updates the corresponding Braze email template. After the first export, Better Email stores the Braze template ID—re-exporting the same email updates that template rather than creating a duplicate.

### Optional: Sync recipient fields from Braze

Better Email can sync Braze custom attributes for use as merge tags and segmentation fields.

1. Open the Braze integration in Better Email.
2. Enable **Sync recipient fields**.
3. Select **Save**.
4. Go to **Recipient Fields**.
5. Run **Sync from** your integration name.

Better Email reads the available Braze custom attributes and maps them into recipient fields.

## Troubleshooting

If an export or sync fails, verify the following:

- The **Instance URL** is the REST URL, not the dashboard URL
- The API key is still active and has the necessary **Templates** permissions
- The integration is enabled in Better Email
- The correct users or groups have access to the integration

For further support, contact [support@better.email](mailto:support@better.email).

## Use the integration

You can find your exported Better Email templates in Braze under **Templates & Media** > **Email Templates**. Use them in any Braze campaign or Canvas.
