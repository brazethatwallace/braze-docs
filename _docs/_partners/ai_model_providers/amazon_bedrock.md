---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "This reference article outlines the partnership between Braze and Amazon Bedrock, which lets you connect Bedrock models to Braze for use with custom AI agents."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> [Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed AWS service that provides access to foundation models from leading AI companies through a unified API, so brands can build and scale generative AI applications on AWS.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## About the integration

The Braze and Amazon Bedrock integration lets you connect your Amazon Bedrock credentials to Braze so you can use Bedrock-hosted models when building custom AI agents. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using models available through Amazon Bedrock. 

When you connect Amazon Bedrock, Braze shows a curated set of Bedrock models for custom agents. The models available in Braze may differ from the full catalog in your AWS account.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Prerequisites

| Requirements | Description |
|---|---|
| An AWS account with Amazon Bedrock access | An AWS account with access to Amazon Bedrock in the AWS region where your models are hosted. For help, contact your admin or [AWS Support](https://aws.amazon.com/support). |
| Amazon Bedrock model access | Access in your AWS account to the Bedrock models you plan to use. Some models, like those from Anthropic, require access to be granted on your AWS account. Not all models are available in every AWS region. |
| Authentication credentials | Either a long-term [Amazon Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html), or—when IAM role authentication is enabled for your workspace—an IAM role that Braze can assume. |
| Braze instance | You can find your Braze instance on the [API overview page]({{site.baseurl}}/api/basics/#endpoints) or from your Braze onboarding manager. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

To connect Amazon Bedrock to Braze:

1. Go to **Partner Integrations** > **Technology Partners** in the Braze dashboard, then search for and select **Amazon Bedrock**.
2. For **Authentication method**, choose **API key** or **AWS IAM role** (when available).
3. Complete setup for your chosen method:
   - **API key:** Enter your long-term **Amazon Bedrock API key**. Select the **AWS region** where your Bedrock models are hosted. Select **Save**.
   - **AWS IAM role:** Use the values Braze displays to configure your IAM role trust policy, then enter the role details in Braze:
     1. Copy the **Braze AWS account ID** and trust that account in your IAM role's trust policy.
     2. Copy the **Braze external ID** and require it in your role's trust policy with an `sts:ExternalId` condition. Select **Generate new external ID** if you need a new value.
     3. Enter the **AWS role ARN** for the IAM role that has Amazon Bedrock permissions. The ARN must match `arn:aws:iam::<account-id>:role/<role-name>`.
     4. Select the **AWS region** where your Bedrock models are hosted.
     5. Select **Save**.

{% alert note %}
**AWS IAM role** appears only for workspaces where this authentication option is enabled. With IAM role authentication, Braze assumes your role to generate short-lived Amazon Bedrock credentials and does not store a long-term API key.
{% endalert %}

After you save, Braze displays a connected status with the date and time of the connection. You can select Amazon Bedrock models when [creating a custom agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) in the Agent Console.

{% alert note %}
Not all Amazon Bedrock models are available in every AWS region. Choose a region that supports the models you plan to use. Models that aren't available in your connected region return errors during agent invocation.
{% endalert %}

To confirm the integration is working, go to the Agent Console and create a test agent using one of your Bedrock models. Enter an instruction such as "Tell me a joke," and run a test invocation to verify the model responds as expected.

To remove the integration, select **Disconnect** on the **Amazon Bedrock integration** page.

For issues with your Amazon Bedrock account or credentials, contact [AWS Support](https://aws.amazon.com/support).
