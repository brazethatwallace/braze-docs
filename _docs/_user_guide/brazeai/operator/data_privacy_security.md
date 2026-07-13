---
nav_title: Data privacy and security
article_title: Data privacy and security for BrazeAI Operator
page_order: 5
page_type: reference
description: "This reference article covers how BrazeAI Operator handles data, including HIPAA compliance, data retention, PII minimization, and governance."
---

# Data privacy and security for BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> integrates with OpenAI to provide AI-powered assistance. This article covers how Operator handles data, what information is shared with OpenAI, and how to minimize PII exposure and control access.

## How Operator accesses data

Operator's access to customer data is strictly event-driven and invocation-scoped, not persistent. Each user message or navigation event while Operator is open triggers a discrete HTTP request to OpenAI. There is no standing connection or persistent data feed.

OpenAI does not have direct access to Braze data stores or the full User Table. The LLM receives only the specific payload associated with the active request.

### What data is included in each request

Each request payload sent to OpenAI may include the following:

- **System metadata:** Braze-authored system prompts and tool schemas (definitions of tools the LLM can invoke).
- **Dashboard user message:** The typed input from the dashboard user.
- **Tool outputs:** Search results containing names, IDs, and related data.
- **Scraped page content:** Content from the active dashboard page, truncated to approximately 4,000 characters.
- **Page context strings:** Contextual strings from the active dashboard page.

## Data sub-processors

### Model providers as sub-processors or third-party providers

When you use an integration with an LLM provider provided by Braze through the Braze Services ("Braze-provided LLM"), the providers of such Braze-provided LLM act as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. BrazeAI Operator<sup>TM</sup> integrates with OpenAI.

### How data is used with OpenAI

To generate AI output through BrazeAI features that leverage OpenAI ("Output"), Braze will send certain information ("Input") to OpenAI. Input consists of your prompts, the content displayed in the dashboard, and workspace data relevant to your queries. Per [OpenAI's API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI's API through Braze is not used to train or improve OpenAI models. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

## HIPAA compliance and data retention

### HIPAA compliance

If you use Braze's US-02 cluster, Operator is covered by Braze's Business Associate Agreement (BAA), and Personal Health Information (PHI) can be submitted to the feature in line with HIPAA requirements. Don't submit PHI subject to HIPAA when using Operator in other Braze clusters.

### PII redaction

There is no automated PII redaction layer in the Operator request pipeline. Data is sent completely raw and is not anonymized before transmission to OpenAI. Access is scoped to the active dashboard page or the dashboard user's input, but no content filtering is applied before transmission.

### OpenAI data retention

How long OpenAI retains data sent through Operator depends on your cluster:

| Cluster | Retention |
| --- | --- |
| US-02 (HIPAA customers) | Zero Data Retention (ZDR). Data is not stored by OpenAI after processing. |
| All other clusters | 30 days for abuse monitoring. This is an industry-standard retention period imposed by OpenAI. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="OpenAI data retention by cluster" }

### Model training

Data sent to OpenAI's API through Braze is not used to train or improve OpenAI models. This is governed by contractual agreements between Braze and OpenAI and OpenAI's API platform commitments. OpenAI acts as a Braze sub-processor, and all Personal Data is subject to the DPA between Braze and its clients.

### EU data routing

EU data routing is not currently implemented for Operator, and there are no current plans to implement it.

## Minimize PII exposure

There are several steps you can take to limit PII exposure when using Operator:

- **Disable the View PII setting** for any users who use Operator. If a user cannot view PII, Operator cannot access it either.
- **Do not open Operator on a user profile page.** Page content is scraped and included in each request sent to OpenAI.
- **When testing, use a custom user profile** rather than selecting an existing one. This is Operator's default behavior.
- **Do not type or paste PII** directly into the Operator prompt. Operator does not block PII included in user prompts. If a user manually types PII into a request, that content is sent to the underlying language model.
- **Disable auto-approval for actions** to maintain control over what Operator can access and execute.
- **Do not ask Operator to display preview values for attributes** when building a segment or writing Liquid.

## Governance and access control

### Restrict access to Operator

Access to Operator is managed at the workspace level through [Granular User Permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Administrators can grant or revoke the "Use BrazeAI Operator" permission for individual users, ensuring that only authorized personnel can interact with the tool. Without these specific permissions, the Operator interface is completely suppressed and backend endpoints remain secured.

### Human-in-the-loop model

By default, Operator requires explicit approval before committing any change. Proposed modifications are presented as [action cards]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) for review. If a user rejects a proposal, no changes occur. If a user accepts a proposal, the dashboard updates, but the changes remain pending and must be manually saved or launched to become persistent.

Users can enable **Auto-approve actions** in the Operator chat panel, which causes suggested actions to execute immediately without manual review. Even with auto-approve enabled, some actions always require explicit approval for safety, including generating images and modifying workspace-level settings.

### User permission inheritance

Operator fully inherits the permission profile of the logged-in user. It is restricted from viewing data or executing actions, such as campaign modifications, that the user is not already authorized to perform independently.

### View PII permission

Operator does not require the "View PII" permission to function, and this is intentional. Operator has no direct access to your data store and does not query your database independently. Instead, it makes requests to the same backend endpoints as the rest of the dashboard using the authenticated user's session credentials. This means Operator is fully bounded by the user's existing [permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) and cannot access anything the user cannot already see.

PII can only reach Operator in two ways:

- The user types PII directly into a prompt.
- The user is already viewing PII in the dashboard when they use Operator.

If a user does not have the "View PII" permission, Operator cannot surface PII to them. Keep in mind that Operator does not filter content typed directly into prompts—PII entered manually is sent to the underlying language model. To reduce this risk, see [Minimize PII exposure](#minimize-pii-exposure).

### Audit team usage

Download Braze's [Security Event Report]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) to monitor team usage. The "Requested BrazeAI Operator Response" event provides a comprehensive audit trail, allowing you to review the exact inputs provided to the Operator.
