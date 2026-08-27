---
nav_title: Meta Direct Billing
article_title: Meta Direct Billing
page_order: 7
description: "This reference article covers how to set up Meta Direct Billing so you pay for WhatsApp messaging costs with your own debit or credit card instead of a Braze or partner credit line."
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Meta Direct Billing

> Meta Direct Billing lets you pay for WhatsApp messaging costs directly with your own debit or credit card, instead of billing through a Braze or partner credit line.

## Prerequisites

Before setting up Meta Direct Billing, make sure you have the following:

| Requirement | Description |
| --- | --- |
| Braze workspace access | You'll need access to **Partner Integrations** > **Technology Partners** in Braze to start the embedded sign-up flow. |
| Meta Business Manager account | Billing is configured in Meta Business Manager, under **Billing & payments**. |
| Debit or credit card | A valid card is required to complete setup. Monthly invoicing may appear as an option on some accounts, but isn't guaranteed. |
| Complete business information | Your business name, address, and currency must be filled in and accurate. Meta reviews this before enabling messaging. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Setup

### Step 1: Select Meta Direct Billing

1. In Braze, go to **Partner Integrations** > **Technology Partners**, search for **WhatsApp**, and open the **WhatsApp Messaging Integration** page.
2. Select the **Meta Direct Billing** tab. This means that your billing relationship is directly with Meta, rather than through Braze or an Infobip billing line, so it's important to select this tab before continuing, rather than trying to change it later.
3. Under **Add a WhatsApp Business Account or phone number**, select **Add account or number**. This launches Meta's embedded sign-up, where you'll log in to Meta, select your business portfolio, create or select your WhatsApp Business Account (WABA), and verify your phone number.

### Step 2: Go to Billing & payments

After you complete Meta's embedded sign-up, do one of the following:

- Select **Add payment method**, which leads you to the Meta Business Manager
- In Meta Business Manager, go to **Billing & payments** > **Accounts**, and select your WABA.

### Step 3: Add a payment method

1. Select **Add payment method**.
2. In the window that opens, confirm the **Business location and currency** (for example, **Canada, US Dollars USD**), which determines the currency you're billed in. Select **Edit** if this needs to change.
3. Under **Select payment method**, you may see existing credit lines. These aren't available for your use; don't select them. For details, see [billing line restrictions](#billing-line-restrictions).

![The Select payment method window with Debit or credit card selected and existing Infobip and Braze credit lines left unselected.]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. Under **Add payment method**, select **Debit or credit card**, then select **Next**.
5. Enter your card details, and then select **Save**.
6. Your card appears under **Payment methods**, marked **Default**, with the masked card number and expiration date shown.

{% alert note %}
Closing the setup window after adding your payment method doesn't disconnect your phone number. The linked number is retained.
{% endalert %}

### Step 4: Confirm your business information

Meta reviews your business name, address, and currency before enabling messaging. Incomplete or inaccurate business information can result in messages failing or an invalid business information error.

## Billing line restrictions

Credit lines shown in the payment method list (for example, "Infobip Limited" or "BRAZE INC.") are owned by that specific business, not by you. They appear because of how your account is connected, but they can't be selected.

## Meta resources

- [Meta Business Help Center: Billing and payments](https://business.facebook.com/business/help/535561817791563)
- [Meta Business Help Center: Adding a payment method](https://www.facebook.com/business/help/832746984379005)
