---
nav_title: Reference
article_title: Reference for agents
description: "Reference key details about Braze Agents."
page_order: 3
---

# Reference for agents

> As you create custom agents, refer to this article for more information on key settings, such as instructions and output schemas. For step-by-step setup, see [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). For an introduction, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) and [Frequently asked questions]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Models

When you set up an agent, you can choose the model it uses to generate responses. You have two options: using a Braze-powered model or bringing your own API key.

{% alert important %}
The Braze-powered **Auto** model is optimized for models whose thinking capabilities are sufficient to perform tasks such as catalog search and segment membership. When using other models, we recommend testing to confirm your model works well for your use case. You may need to adjust your [instructions](#writing-instructions) to give different levels of detail or step-by-step thinking to models with different speeds and capabilities.
{% endalert %}

### Option 1: Use a Braze-powered model

This is the simplest option, with no extra setup required. Braze provides access to large language models (LLMs) directly. To use this option, select **Auto**, which uses Gemini models.

{% alert important %}
If you don't see **Braze Auto** as an option in the **Model** dropdown when creating an agent, contact your customer success manager to learn how to become eligible to use the Braze Auto model.
{% endalert %}

### Option 2: Bring your own API key

With this option, you can connect your Braze account with providers like OpenAI, Anthropic, or Google Gemini. If you bring your own API key from an LLM provider, token costs are billed directly through your provider, not through Braze.

We recommend routinely testing the most recent models, as legacy models may be discontinued or deprecated after a few months. Make sure you have sufficient credits with your provider to run your agents at scale. You can also sign up for Agent Console notifications in [Notification Preferences]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) to be alerted when Braze detects a model is no longer available or encounters billing issues with your LLM provider.

To set this up:

1. Go to **Partner Integrations** > **Technology Partners** and find your provider.
2. Enter your API key from the provider.
3. Select **Save**.

Then, you can return to your agent and select your model.

When you use a Braze-provided LLM, the providers of such a model will be acting as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. If you choose to bring your own API key, the provider of your LLM subscription is considered a Third Party Provider under the contract between you and Braze.

#### Thinking levels

Some LLM providers may allow you to adjust a selected model's thinking level. Thinking levels define the range of thought the model uses before answering—from quick, direct responses to longer chains of reasoning. This affects response quality, latency, and token usage.

| Level | When to use |
|-------|-------------|
| **Minimal** | Simple, well-defined tasks (such as catalog lookup, straightforward classification). Fastest responses and lowest cost. |
| **Low** | Tasks that benefit from a bit more reasoning but don't need deep analysis. |
| **Medium** | Multi-step or nuanced tasks (such as analyzing several inputs to recommend an action). |
| **High** | Complex reasoning, edge cases, or when you need the model to work through steps before answering. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Thinking levels" }

We recommend starting with **Minimal** and testing your agent’s responses. Then, you can adjust the thinking level to **Low** or **Medium** if you find the agent is struggling to provide accurate answers. In rare cases, a **High** thinking level may be needed, although using this level can result in high token costs and longer response times or higher risk of timeout errors. If your agent is struggling to balance multi-step reasoning with reasonable response times, consider breaking your use case apart into more than one agent that can work together in a Canvas or catalog.

Braze uses the same IP ranges for outbound LLM calls as for Connected Content. The ranges are listed in the [Connected Content IP allowlist]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). If your provider supports IP allowlisting, you can restrict the key to those ranges so only Braze can use it.

{% alert important %}
When you use a Braze-provided LLM, the providers of such a model will be acting as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. If you choose to bring your own API key, the provider of your LLM subscription is considered a Third Party Provider under the contract between you and Braze.
{% endalert %}

#### Determine which model to use

Each LLM provider has a slightly different mix of model capabilities, costs, and thinking levels. Here are some general guidelines and best practices:

- For cost efficiency, prioritize testing lower token cost models over higher cost models. Adjust to higher cost models only if lower cost models are struggling with the use case or generate inconsistent or inaccurate outputs.
- For speed and performance efficiency, prioritize testing lower model thinking levels over higher thinking levels. Adjust to higher thinking level models only if lower thinking levels are struggling with the use case or generating inconsistent or inaccurate outputs.
- If lower cost models or model thinking levels are struggling with the use case or generating inconsistent or inaccurate outputs, consider adjusting to higher cost models or thinking level models.
- During testing, make sure to balance the reliability and accuracy with token usage and invocation duration.
- Each use case may have a different optimal model and thinking level. We recommend thoroughly testing to check for consistent quality without timeouts.

### Invocation flow controls

The following invocation flow controls apply per workspace:

- **Braze-powered model:** 5,000 invocations per minute 
- **Bringing your own API key:** 5,000 invocations per minute

When many users enter an Agent step at once, Braze queues invocations according to these limits, so processing may take longer during high-volume sends.

### Daily invocation and credit limits

Each agent has a daily invocation limit (default 250,000; maximum 1,000,000 unless your contract allows higher). Every invocation—including Agent Console previews and Test Canvas runs that use **Simulate response**—counts toward this limit.

In Agent Console, the **Daily action credit cost limit** estimates the maximum credits an agent can consume per day. Braze multiplies your workspace's per-invocation **credit ratio** for the selected model by the daily invocation limit. 

### Monitor credit usage

Go to **Settings** > **Billing** > **Credits Usage** > **Agent Console** to see credit consumption, invocation counts, and per-agent credit ratios. 

Credit ratios come from your contract and appear on the [Credits Usage]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) dashboard (**Credit Ratios** tab and **Agent Console** tab). The estimate updates when you change the model or invocation limit.

To manage spend, lower the daily invocation limit. For [bring-your-own (BYO)](#option-2-bring-your-own-api-key) models, you can also choose a lower-cost model or reduce the [thinking level](#thinking-levels) to lower provider token costs. **Braze Auto** does not support adjusting the thinking level. 

### Rate limit errors

If the LLM provider returns a rate limit error during a Canvas Agent step or Catalog Agent invocation, Braze continuously retries the request using exponential backoff until the call succeeds or Braze determines it cannot be completed.

When Canvas or catalog retries are exhausted, the **Logs** details panel shows **Error** and the provider message (such as `Rate limit exceeded`) in **Output**. Retries are visible in logs, including the very first invocation regardless of its eventual success or failure. For a given user, if it takes four retries to finally get a success, you can search the user ID and see all five (original plus four retries) in the **Logs**, and the original plus the first three retries will show **Error** with `Rate limit exceeded`.

![Agent Console log details showing a rate limit exceeded error in the Output field.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Writing instructions

Instructions are the rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. System instructions can be up to 25 KB.

If you built your agent with [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) using a [starting template]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), review the pre-filled instructions and edit as needed.

Here are some general best practices to get you started with prompting:

1. Start with the end in mind. State the goal first.
2. Give the model a role or persona ("You are a ...").
3. Set clear context and constraints (audience, length, tone, format).
4. Ask for structure ("Return JSON/bullet list/table...").
5. Show, don't tell. Include a few high-quality examples.
6. Break complex tasks into ordered steps ("Step 1... Step 2...").
7. Encourage reasoning ("Think through the steps internally, then provide a concise final answer," or "briefly explain your decision").
8. Pilot, inspect, and iterate. Small tweaks can lead to big quality gains.
9. Handle the edge cases, add guardrails, and add refusal instructions.
10. Measure and document what works internally for reuse and scaling.

### Examples {#examples}

For starting configurations in Agent Console, see [Agent templates built with Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

For full instruction examples you can copy or adapt, see the [use case library for Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Example | Category | Agent type | What it does |
| --- | --- | --- | --- |
| [Write personalized messaging based on a user's context]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Content generation | Canvas Step Agent | Generates coordinated email subject/preheader and push title/body for users who searched but didn't book. |
| [Analyze user feedback to determine next steps]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Data standardization | Canvas Step Agent | Classifies post-trip survey sentiment and topic, then recommends a CRM next step. |
| [Categorize users into interest buckets from existing attributes]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Affinity agent | Canvas Step Agent | Classifies users into interest buckets from attributes and high-intent signals, then recommends the best next experience or item. |
| [Route users to the most relevant Canvas path from recent behavior]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Affinity agent | Canvas Step Agent | Infers motivation from recent behavior and returns the best route key for the user's next Canvas step. |
| [Assign users to interest categories from real-time high-intent actions]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Affinity agent | Canvas Step Agent | Assigns interest categories from high-intent actions and recommends the best next experience or item. |
| [Classify inbound messages for opt-out intent]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Classification and routing | Canvas Step Agent | Returns a strict boolean indicating whether a message is an opt-out request. |
| [Standardize inbound messages into structured data for automation]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Data standardization | Canvas Step Agent | Normalizes inbound SMS or chat into structured intent, entities, and compliance flags for downstream automation. |
| [Write high-converting descriptions that align with brand guidelines]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Content generation | Catalog Agent | Generates short, on-brand descriptions for each catalog row. |
| [Provide translations based on language used by region]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Catalog enrichment | Catalog Agent | Localizes UI and marketing strings per locale and character limit. |
| [Enrich catalog items with descriptions, categories, and tags]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Catalog enrichment | Catalog Agent | Generates enhanced descriptions, categories, and tags from existing catalog item data. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Summary of examples" }

### Using Liquid

Including [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in your agent's instructions can add an extra layer of personalization in its response. You can specify the exact Liquid variable the agent gets and can include it in the context of your prompt. For example, instead of explicitly writing "first name", you can use the Liquid snippet {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

In the **Logs** section of the **Agent Console**, you can review the details for the agent's input and output to understand what value is rendered from the Liquid.

### What data agents receive {#what-data-agents-receive}

Agent context is not open-ended conversational memory. Unlike a chat assistant, an agent only sees the data you explicitly pass in at invocation time—it does not browse user profiles, infer missing fields, or tell you when required information is absent.

Design each agent as a deliberate input-to-output pipeline. Wire every data point the agent needs using one or more of the following:

1. **Liquid in instructions:** Template user attributes ({% raw %}`{{${first_name}}}`{% endraw %}) and [Canvas context variables]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) directly in the agent prompt.
2. **+ Agent context:** Select catalogs, segment membership, brand guidelines, **All Canvas Context**, or user interaction data in Agent Console.
3. [Context steps]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): Set or update `context.*` variables upstream in the Canvas before an Agent step runs.
4. **Additional context on the Agent step:** Pass any additional Liquid-templated values not already specified using the other methods to the agent at send time from the step configuration.

Make sure to either Liquid template these context variables in the agent instructions or select **Add All Canvas Context**. If a value is not passed through one of these channels, the agent does not receive it. List required inputs in your instructions or in [use case prerequisites]({{site.baseurl}}/user_guide/brazeai/agents/use_cases), and verify inputs in **Agent Console** > **Logs** after testing.

![The details for an agent that has Liquid in its instructions.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

For catalog agents, use **Fields** in the **Output** section rather than JSON schema; you can still write instructions that ask the model for key-value output matching those field names.

For more details on prompting best practices, refer to guides from the following model providers:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Outputs

If you built your agent with [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) using a [starting template]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), review the pre-filled output schema and edit as needed.

### Basic schemas

Basic schemas are a simple output that an agent returns. This can be a string, a number, a boolean, an array of strings, or an array of numbers.

For example, if you want to collect user sentiment scores from a simple feedback survey to determine how satisfied your customers are after receiving a product, you can select **Number** as a basic schema to structure the output format.

{% alert important %}
Arrays are only available for Canvas agents, not catalog agents.
{% endalert %}

![Agent Console with number selected as a basic schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Advanced schemas

Advanced schema options include manually structuring fields or using JSON.

- **Fields:** A no-code way to enforce an agent output that you can use consistently.
- **JSON:** A code approach to creating a precise output format, where you can nest variables and objects within the JSON schema. Only available for Canvas agents, not catalog agents.

We recommend using advanced schemas when you want the agent to return a data structure with multiple values defined in a structured manner, rather than a single-value output. This allows the output to be better formatted as a consistent context variable.

### Fallback output

Fallback values are available for **Canvas step agents** only. In the **Output** section of Agent Console for a Canvas Agent, you can define values that Braze uses when an invocation fails.

For **JSON** schemas, Braze reads the schema and generates an input field for each property so you can set a fallback value per key. For **Fields** schemas, you enter a fallback value for each field. For basic schemas, you enter a single fallback value. Canvas agents support Liquid in fallback values.

For setup steps, see [Configure fallback values]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). For runtime behavior in Canvas, see [Error handling and fallback behavior]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

For example, you may use an output format within an agent that is intended to create a sample travel itinerary for a user based on a form they submitted. The output format allows you to define that every agent response should come back with values for `tripStartDate`, `tripEndDate`, and `destination` values. Each of these values can be extracted from context variables and placed in a Message step for personalization using Liquid.

{% tabs %}
{% tab Fields %}

If you want to format responses to a simple feedback survey to determine how likely respondents are to recommend your restaurant's newest ice cream flavor, you can set up the following fields to structure the output format:

| Field name | Value |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Advanced schemas" }

![Agent Console showing three output fields for likelihood score, explanation, and confidence score.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

If you want to collect user feedback for their most recent dining experience at your restaurant chain, you can select **JSON Schema** as the output format and insert the following JSON to return a data object that includes a sentiment variable and reasoning variable.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## Catalogs and fields

Choose specific catalogs for an agent to reference and to give your agent the context it needs to understand your products and other non-user data when relevant. Agents use tools to find the relevant items only and send those to the LLM to minimize token use. For better catalog retrieval, create a [knowledge source]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) and add it as agent context instead of attaching the catalog directly.

![The "restaurants" catalog and "Loyalty_Program" column selected for the agent to search.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

When you deploy a catalog agent to a catalog field, enable the required-input control and choose which selected columns are **required to run** before the agent invokes. The agent skips a row only when one of those required columns is blank or missing—for example, a `gender` field that has not been filled in yet. Selected columns start as required by default, but you can remove columns that may be empty without blocking the run. This prevents wasted tokens on incomplete data.

Catalog agents also respect column order when input fields depend on each other. If column D should be generated from columns B and C, the agent does not run on column D until B and C contain values for that row.

For deployment scenarios and examples, see [Use catalog agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) and [Catalog agent best practices]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Segment membership context

You can select up to five segments for the agent to cross-reference each user's segment membership against when the agent is used in a Canvas. Let's say your agent has segment membership selected for a "Loyalty Users" segment, and the agent is used in a Canvas. When users enter an Agent step, the agent can cross-reference if each user is a member of each segment you specified in the agent console, and use each user's membership (or non-membership) as context for the LLM.

![The "Loyalty Users" segment selected for agent membership access.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Brand guidelines

You can select [brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) for your agent to adhere to in its responses. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.

## User-specific interaction history {#user-history}

A user's interaction data includes their recent campaign and Canvas opens, clicks, and conversion data. For example, you can include this context for an agent to reference when it's evaluated in Canvas. User-specific interaction history can also help influence an agent when its job is to write personalized message copy.

## Version history {#version-history}

Agent Console records a new version each time you save agent changes. The **Version history** tab lists every saved version and the edits between saves.

1. Open the agent in Agent Console.
2. Select the **Version history** tab.
3. Select a version to review its configuration.

To inspect what changed in a version, select **View**. Braze displays a code-style inline diff that highlights additions and deletions. Deleted content appears with red strikethrough styling.

If you need to restore instructions from a previous version, open **View** for that version, copy the instruction text, and paste it into your current **Instructions** field.

{% alert tip %}
In the inline diff view, press <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) or <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows) to select all instructions without the red deletion markup, so you can copy and restore the clean text.
{% endalert %}

## Duplicate agents

Duplicate an agent to test improvements or iterations side by side against the original. Use [version history](#version-history) to review or restore earlier configurations. To duplicate an agent:

1. Hover over the agent's row and select the <i class="fas fa-ellipsis-vertical"></i> menu.
2. Select **Duplicate**.

## Archive agents

As you create more custom agents, you can organize the **Agent Management** page by archiving agents that aren't actively being used. To archive an agent:

1. Hover over the agent's row and select the <i class="fas fa-ellipsis-vertical"></i> menu.
2. Select **Archive**.

