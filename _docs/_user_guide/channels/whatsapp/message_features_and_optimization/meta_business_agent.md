---
nav_title: Meta Business Agent
article_title: Meta Business Agent and Braze WhatsApp
page_order: 8
description: "This guide explains how Meta Business Agent interacts with a WhatsApp Business phone number connected to Braze, and what to expect if you enable it."
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business Agent and Braze WhatsApp

> Meta Business Agent can reply to WhatsApp inbound messages on a number that's also connected to Braze. This article covers how those two systems share message visibility, how to enable the agent in Meta's tools, and how billing is split. It reflects Meta's Business Agent product functionality and documentation as of August 2026. 

Meta continues to actively develop Meta Business Agent, so some details may change; see [Meta's Business Agent documentation](https://developers.facebook.com/documentation/meta-business-agent/overview) for the latest.

## What is Meta Business Agent?

Meta Business Agent is an AI-powered responder that Meta operates directly on a WhatsApp Business phone number. When enabled for an eligible number, it can reply to inbound messages from users on the business's behalf, using knowledge (business info, FAQs, files, website content) and connectors configured in Meta's tools.

Enabling Meta Business Agent is entirely set up in WhatsApp Manager and Meta Business Suite, and is separate from your Braze workspace. Braze isn't required for setup, and there's currently no Braze dashboard control for it.

## How it interacts with your Braze-connected number

Meta Business Agent and Braze can coexist on the same WhatsApp Business phone number, but don't share visibility into every message today.

- **Braze-initiated outbound messages are unaffected.** Braze continues to send WhatsApp template messages and response messages through campaigns and Canvases exactly as it does today, regardless if Meta Business Agent is enabled.
- **Inbound messages are routed by Meta Business Agent.** For each inbound message from a user, Meta Business Agent decides whether to pass it to Braze or handle it itself.
  - **If Meta routes the message to Braze:** It is processed the same way any inbound WhatsApp message is today. Existing campaign and Canvas action-based triggers and Action Paths fire according to the logic you've already built.
  - **If Meta Business Agent handles the message itself:** Braze doesn't currently process the separate channel (standby messages and message echoes) that would carry that activity. Inbound messages the agent decides to handle, and its own replies to those messages, aren't currently visible in any Braze surfaces.

| Message flow | What happens today |
| --- | --- |
| WhatsApp template messages and response messages sent through campaigns or Canvas steps | Unaffected; Braze continues sending as configured |
| Inbound message Meta routes to Braze | Processed normally; existing triggers and Action Paths apply |
| Inbound message Meta Business Agent handles itself | Not currently visible to Braze; existing triggers and Action Paths for inbounds won't fire |
| Outbound message sent by Meta Business Agent | Not currently visible to Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message flow" }

## Enable Meta Business Agent

Meta Business Agent is enabled per phone number in Meta's tools, not in Braze:

1. Check eligibility and enable it for a phone number in [WhatsApp Manager](https://business.facebook.com/wa/manage/home/), accepting the Meta Business Agent Terms of Service.
2. Configure the agent's knowledge and skills (business info, FAQs, files, connectors) through Meta's [agent configuration APIs](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills).
3. Turn the agent on using [Agent Settings](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings).

## Things to weigh before enabling it

- **No Braze-side toggle:** Enabling, configuring, and disabling Meta Business Agent all happen in Meta's tools; there's nothing to turn on or off in Braze.
- **Billing:** With the introduction of Meta Business Agent, non-templated messages are now classified in one of two categories: Service (existing category) or Meta Business Agent (new category).
  - Non-templated responses handled by Braze are charged as service messages starting October 1, 2026.
    - If you respond to an inbound with a marketing, utility, or auth template, it is billed as such.
  - Meta Business Agent messages are billed directly by Meta starting August 1, 2026. Refer to their pricing for details.
  - Messages are classified into only one category, so you're never billed twice for the same message.
