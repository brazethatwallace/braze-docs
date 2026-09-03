---
nav_title: Embedded signup
article_title: WhatsApp Embedded Signup
page_order: 1
description: "This reference article covers how to access the WhatsApp embedded signup workflow in Braze, what to prepare before Meta signup, and what happens after signup completes."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp embedded signup

> Use embedded signup to connect Braze to a WhatsApp Business Account (WABA) through Meta's hosted signup flow.

The WhatsApp embedded signup workflow opens when you first [integrate WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) into your Braze workspace, and when you [add a WhatsApp Business account or phone number]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) to an existing integration.

{% alert note %}
You can add [multiple WhatsApp Business Accounts]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts) to a Braze workspace. However, each specific WhatsApp Business Account can be added to only one Braze workspace.
{% endalert %}

## Accessing the workflow

1. Go to **Partner Integrations** > **Technology Partners**.
2. Search for and select **WhatsApp**.
3. Select the option that matches your use case:
   - **First-time integration:** Select **Begin Integration**.
   - **Additional account or number:** On the **WhatsApp Messaging Integration** page, select **Add account or number** or **Add WhatsApp Business Account**.

The Meta embedded signup flow is the same after you launch it from either entry point. Your workspace may also show integration tabs, such as **Native Integration** or **BYO Connector - Infobip**, depending on your configuration. Select the tab that matches your setup before you begin.

## Prepare for signup

When you select **Begin Integration**, Braze opens an onboarding window. Review each slide, then select **Begin Integration** again to launch Meta embedded signup.

Before you start, prepare the following:

- **Meta Business Manager access:** Most companies use Meta Business Manager to manage Facebook Pages, Ads, and related business assets. If you don't have access, ask an admin to grant permissions or create a Business Manager account during signup.
- **Phone number:** Use a number that meets [Meta's WhatsApp phone number requirements](https://developers.facebook.com/docs/whatsapp/phone-numbers). You'll receive a one-time verification code by text message or phone call during signup.

{% alert important %}
You'll only complete the initial embedded signup once per integration path, so enter your business details as accurately as possible.
{% endalert %}

## WhatsApp embedded signup workflow {#whatsapp-embedded-signup-workflow}

After Braze launches Meta embedded signup, sign in with a Meta account that has access to your company's Business Manager. Meta hosts the signup screens; Braze doesn't control their layout or labels.

{% alert note %}
Meta may change embedded signup screens without notice. If the workflow differs from this article, follow Meta's prompts and refer to [Meta's embedded signup documentation](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow).
{% endalert %}

In general, Meta guides you through:

1. **Sign in and grant permissions.** Authenticate with Meta and allow Braze to connect to your WhatsApp Business Account.
2. **Select your business portfolio.** Connect the Business Manager portfolio that should own the WhatsApp Business Account. If you don't see the portfolio you expect, confirm your Meta permissions.
3. **Connect or create a WhatsApp Business Account.** Create a new account or select an unused account when prompted. Don't select a WhatsApp Business Account that's actively connected to another messaging provider; that connection won't succeed in Braze. To [migrate a number from another provider]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number), contact your Braze account team before you begin.
4. **Provide business and display details.** Enter the account name, display name, and category Meta requests for your WhatsApp Business Account.
5. **Verify your phone number.** Add the number you want to use for WhatsApp messaging and complete verification by text message or phone call.

When Meta finishes embedded signup, control returns to Braze.

## Complete the Braze integration

After embedded signup, Braze runs setup steps automatically. On the **WhatsApp Messaging Integration** page, you may see progress messages such as **Sign-up flow completed, integration with WhatsApp in progress** while Braze does the following:

- Retrieves your WhatsApp Business Account ID and phone numbers from Meta
- Adds the Braze system user to your WhatsApp Business Account
- Registers phone numbers and subscribes to webhook events
- Creates a Braze [subscription group]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) for each connected number

Wait until integration completes before you send messages. If setup fails, review the error on the integration page and see [WhatsApp setup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) for general guidance.

## Next steps

- [Acquire or migrate a WhatsApp phone number]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/)
- [Create a WhatsApp message]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [Manage subscription groups]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
