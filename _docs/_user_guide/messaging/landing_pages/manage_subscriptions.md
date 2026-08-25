---
nav_title: Manage Subscriptions block
article_title: Manage Subscriptions block
description: "This article covers how to add and configure the Manage Subscriptions form block on a Braze landing page, so consumers can opt in to and manage their email or SMS subscription groups."
page_order: 5
---

# Manage Subscriptions block

> Add a **Manage Subscriptions** block to a landing page so users can view, opt in to, and update their email or SMS subscription groups.

The **Manage Subscriptions** block supports two main use cases:

- **[Manage existing subscriptions](#update-existing-subscriptions):** Share the landing page's [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/) in an email, SMS, or other channel message. When an identified user opens the page, the block automatically pre-fills each subscription group's checkbox with their current subscription state, so they can review and update their preferences.
- **[Capture new opt-ins](#capture-new-subscribers):** Add the block to a lead generation landing page alongside an **Email Capture** or **Phone Capture** block, so new visitors can choose which subscription groups to join when they submit the form.

{% alert important %}
Each **Manage Subscriptions** block is for one channel: [email]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups) or [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states). To collect both, add two blocks. For RCS or WhatsApp consent, use a [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block instead.
{% endalert %}

## Prerequisites

| Requirements | Description |
| --- | --- |
| Email or SMS subscription groups | At least one [email subscription group]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups) or [SMS subscription group]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) for the channel you add to the block. Create email groups from the dashboard or the [Subscription Group endpoints]({{site.baseurl}}/api/endpoints/subscription_groups). SMS groups are provisioned during [SMS setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups). |
| Landing page permissions | The same [permissions]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) required to create and edit any landing page. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Step 1: Add the Manage Subscriptions block

In the drag-and-drop landing page editor, go to the **Build** section and select **Form Blocks**. Drag **Manage Subscriptions** into a row on your page; it auto-adjusts to the column width.

The block is empty until you add subscription groups to it. To show both email and SMS groups, add a second **Manage Subscriptions** block and assign it the other channel.

## Step 2: Select the channel and subscription groups

With the **Manage Subscriptions** block selected, select **+ Add subscription groups** in the right-hand **Block properties** panel. The **Add subscription groups** modal opens.

1. On **Select channel**, choose **Email** or **SMS**. Each block supports one channel. If a channel already has a **Manage Subscriptions** block on the page, that channel card is disabled and labeled **Added**.
2. On **Select subscription groups**, select the groups to include. The list heading matches the channel (**Email subscription groups** or **SMS subscription groups**).
3. Select **Add selected**.

Each subscription group appears as its own selectable checkbox on the landing page.

If you select **SMS** and your workspace has no SMS subscription groups yet, the modal shows **No SMS subscription groups yet**. Complete [SMS subscription group setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states), then return to the block.

{% alert note %}
The **Manage Subscriptions** block only lists groups you explicitly add. Adding a subscription group to the block doesn't automatically subscribe visitors to it—a visitor must select the group's checkbox and submit the form.
{% endalert %}

## Step 3: Configure the block settings

Use the **Block properties** panel to adjust how the block behaves and appears.

### Subscription groups

- **Reorder groups:** Drag a subscription group by its handle to change the order it appears in the block.
- **Add or remove groups:** Select **+ Add subscription groups** to include more groups, or select the delete icon next to a group to remove it from the block.

### Include descriptions

Turn on **Include descriptions** to display each subscription group's description text alongside its name, giving visitors more context about what they're opting into. Email groups can include a description in Subscription Management. SMS groups in this block don't show description text.

### "Subscribe to all" checkbox

Turn on the **"Subscribe to all" checkbox** setting to add an extra checkbox to the block. When a visitor selects it, every subscription group checkbox in the block is selected—useful for a quick opt-in to all listed groups.

## Update existing subscriptions

To let existing users review and update their email or SMS subscriptions, share the landing page using its [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/) in an email, SMS, Canvas step, or other message. When a user opens the page through that link, Braze identifies them and automatically pre-fills each subscription group checkbox in the **Manage Subscriptions** block to match their current subscription state—similar to an [email preference center]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/).

The user can select or clear checkboxes to update their subscriptions, then submit the form to save their changes.

{% alert note %}
Pre-filling a user's current subscription state in the **Manage Subscriptions** block is included by default and doesn't require the [Landing Pages Pro tier]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). This differs from [Liquid-based pre-fill]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages/#pre-fill-form-fields) for other form fields, which requires Landing Pages Pro.
{% endalert %}

## Capture new subscribers

To collect new subscribers, pair the **Manage Subscriptions** block with a capture field for that channel:

- **Email:** Add an [Email Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block so the page captures the visitor's email address alongside their email subscription group selections.
- **SMS:** Add a [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block so the page captures the visitor's phone number alongside their SMS subscription group selections.

If the visitor isn't identified (for example, they arrive without a landing page Liquid tag), the checkboxes start unselected. When they submit the form, they're subscribed to whichever subscription groups they selected.

## Things to know

- **One channel per block:** You can add one **Manage Subscriptions** block per channel on a page (one for email and one for SMS).
- **RCS and WhatsApp:** This block doesn't list RCS or WhatsApp subscription groups. To collect consent for those channels, use a [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block.
- **Confirmation experience:** Landing pages with form blocks, including **Manage Subscriptions**, need a confirmation experience after submission. [Create a confirmation page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#step-4-create-a-confirmation-page-optional) and link to it from your **Submit** button.
- **Editor blocks reference:** For a full reference of every landing page block and its properties, see [Editor blocks (landing pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
