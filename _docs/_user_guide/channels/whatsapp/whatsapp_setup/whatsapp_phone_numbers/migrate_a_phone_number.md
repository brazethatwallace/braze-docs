---
nav_title: "Migrate a number"
article_title: "Migrate a WhatsApp phone number"
page_order: 2
description: "This reference article covers how to migrate your WhatsApp phone number."
page_type: reference
channel:
  - WhatsApp
---

# Migrate a WhatsApp phone number

> Migrate your WhatsApp phone number between WhatsApp Business Accounts by using Meta's Embedded Signup.

## Prerequisites

Your phone number must meet Meta's requirements to be eligible for migration:

- Your Meta Business Account is verified.
- Your existing WhatsApp Business Account is approved.
- Your existing WhatsApp Business Account has a valid payment method in **Payment Settings**.
- Your business phone number has two-step verification turned off. If you own your WhatsApp Business Account, you can turn off two-step verification on their number in the WhatsApp Manager. Otherwise, you must ask your Solution Provider to turn it off for you.

For information on migrating your WhatsApp phone number, see Meta's documentation for [Migrating phone numbers between WhatsApp Business Accounts via Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migrate between WhatsApp Business Accounts {#migrate-between-whatsapp-business-accounts}

1. In the WhatsApp Manager, select the WhatsApp Business Account (WABA) associated with your phone number, then go to **Account tools** > **Phone numbers**.
2. Select **Turn off two-step verification** and complete the steps that follow.<br><br>![WhatsApp Business Manager opened to the "Phone numbers" page.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> If you're migrating a phone number to a different WhatsApp Business Group and Meta's embedded signup requires the display name to match, take note of the existing display name on the **Phone Numbers** page. You'll enter that name during the next step.<br><br>![The WhatsApp Business Manager's Phone Numbers page with a display name of "Braze" listed next to a phone number.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Continue Meta's embedded signup workflow to completion.

## Migrate from another Business Solution Provider (BSP) {#migrate-from-another-business-solution-provider}

If your WhatsApp phone number is registered with another BSP, you must migrate the number to a Braze-connected WhatsApp Business Account before Braze can send on that number.

### Before you migrate

- Know that a phone number can be active on one BSP at a time. Migrating moves sending to Braze; your prior BSP loses access to the number.
- Review contracts and billing with your current provider. Message history and templates may not transfer automatically.
- Turn off two-step verification on the number per Meta's requirements.
- If you need separate support and marketing numbers, see [Integrations, data, and reporting]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) in the WhatsApp FAQ.

### Migration paths

| Current setup | Recommended path |
|---|---|
| Number on another BSP, moving fully to Braze | Migrate through [embedded signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) into a new or existing Braze WABA |
| Number on Braze native integration, moving to Infobip billing | [BYO WhatsApp connector]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (Infobip only) |
| Marketing on Braze, support on another WABA | Keep separate WABAs and phone numbers; see the [WhatsApp FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) and [WhatsApp and external systems]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Migration paths" }

## Development and production workspaces

Braze recommends separate WhatsApp Business Accounts for development and production when possible:

- Don't bind your production phone number to a sandbox or development workspace.
- Use a dedicated test WABA and phone number for integration testing.
- Template approvals apply per WABA; approve templates in the WABA tied to the workspace where you send.

