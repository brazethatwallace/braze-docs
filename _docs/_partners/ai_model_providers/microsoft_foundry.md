---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "This reference article outlines the partnership between Braze and Microsoft Foundry, which lets you connect Foundry-managed AI models to Braze for use with custom AI agents."
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) is a unified Azure platform-as-a-service offering for enterprise AI operations, model builders, and application development.

{% multi_lang_include early_access_beta_alert.md feature='The Microsoft Foundry integration' %}

## About the integration

The Braze and Microsoft Foundry integration lets you use generative AI models managed in Microsoft Foundry when building custom AI agents. The integration currently supports two models: gpt-5.4-mini and gpt-5.4-nano. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using Foundry-managed models.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Prerequisites

| Requirements | Description |
|---|---|
| An Azure account with an active subscription | For help, contact your admin or see [Azure account options](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account). |
| Microsoft Foundry instance | A Microsoft Foundry instance to create a project. |
| Microsoft Foundry project | A project within your Foundry instance to house the deployed models. |
| Deployed models | At least one of the supported models deployed within the Foundry project. |
| Braze instance | You can find your Braze instance on the [API overview page]({{site.baseurl}}/api/basics/#endpoints) or from your Braze onboarding manager. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Deploy supported models in Foundry

The Braze integration with Microsoft Foundry supports two models: gpt-5.4-mini and gpt-5.4-nano. Both must be deployed in a Foundry project within the Foundry instance you're integrating.

To create the Foundry project and deploy the models, follow the [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal):

1. Sign in to Microsoft Foundry through your Azure portal.
2. In Microsoft Foundry, create a project to house the models you want to integrate with Braze.
3. Decide whether to use gpt-5.4-mini, gpt-5.4-nano, or both.
4. For each model you want to use, deploy it using the Microsoft Foundry documentation. Do not change the default deployment name, or the integration for that model may break.

## Integration

To connect your Foundry instance to Braze:

1. Go to **Partner Integrations** > **Technology Partners** in the Braze dashboard and find **Microsoft Foundry**.
2. Enter your **Microsoft Foundry API Key**.
3. Enter your **Microsoft Foundry instance name**. This is the subdomain before `.services.ai.azure.com`.
4. Select **Save**.

After you save, Braze displays a connected status with the date and time of the connection. You can select Foundry models when [creating a custom agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) in the Agent Console.

{% alert important %}
To use gpt-5.4-mini or gpt-5.4-nano, you must deploy each model in your Foundry project without changing the default deployment name.
{% endalert %}

To confirm the integration is working, go to the Agent Console and create a test agent using one of your deployed models. Enter a simple instruction, such as "Tell me a joke," and run a test invocation to verify the model responds as expected.

To remove the integration, select **Disconnect** on the **Microsoft Foundry Integration** page.

Contact [Azure support](https://azure.microsoft.com/en-us/support/options/) with any issues or questions regarding your integration.
