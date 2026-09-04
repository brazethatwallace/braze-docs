---
nav_title: Agent
article_title: Agent Step
alias: /agent_step/
page_order: 2
page_type: reference
description: "This reference article covers how to use the Agent step in Canvas to generate content or make intelligent decisions in real time."
tool: Canvas
toc_headers: h2
---

# Agent step  

> The Agent step lets you add AI-powered decisioning and content generation directly into your Canvas workflow. For more general information, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). 

![An Agent step in a Canvas user journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Prerequisites

Agent steps use [Canvas context variables]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) to ingest relevant context and output a variable that can be leveraged in the Canvas.

## How it works

When a user reaches an Agent step in a Canvas, Braze sends the input data you’ve configured (full context or selected fields) to your chosen agent. The agent then processes the input using its model and instructions, and returns an output. That output is stored in the output variable you defined in the step.

You can then use this variable in three main ways:

- **Decisioning:** Route users down different Canvas paths based on the agent’s response. For example, a lead scoring agent might return a lead category of "Sales Ready", "Marketing Qualified", or "Disqualified". You might use this assignment to trigger a Slack alert or automated message for "Sales Ready" leads while dropping "Disqualified" leads from the journey.
- **Personalization:** Insert the agent’s response directly into a message. For example, an agent could analyze customer feedback and generate an empathetic follow-up email that references the customer’s comment and suggests a resolution.
- **Processing user data:** Analyze and standardize your user data, then store it on the user profile or send it using a webhook. For example, an agent could return a sentiment score or product affinity assignment. You can store that data in a user profile for future usage.

## Creating an Agent step

### Step 1: Add a step

Drag and drop the **Agent** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Agent**.  

### Step 2: Choose your agent  

Select the agent that will process data in this step. For setup guidance, see [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

In the agent list, each agent is labeled with its [daily invocation limit]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Hover over the limit to see today's progress toward that limit, including the percentage used and the number of invocations used today compared to the limit.

![The Configure Agent Step panel showing the agent dropdown with two agents listed. Each agent is labeled with its daily invocation limit. A tooltip on the first agent shows the percentage used and invocations used today.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Step 3: Set your agent's output {#define-the-output-variable}

Agent outputs are called "output variables" and are stored in a [context variable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-filters) for easy access. To define the output variable, give the variable a name.

Note that the output variable's data type is set from the [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents). Agent outputs can be saved as strings, numbers, booleans, or objects. This makes them flexible for both text personalization and conditional logic in your Canvas. Here are some common uses for each type:

| Data type | Common uses |
| --- | --- |
| String | Message personalization (subject lines, copy, responses) |
| Number | Scoring, thresholds, routing in [Audience Paths]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Boolean | Yes/No branching in [Decision Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Object | Leverage one or more of the earlier in this section data types with a single LLM call in a predictable data structure |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Set your agent's output #define-the-output-variable" }

You can use an output variable throughout the Canvas by using the same template syntax as you would with a context variable. Either use the **Context Variable** segment filter, or template agent responses directly using Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

To use a specific property from an object output variable, use dot notation to access that property using Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agent step for Body HTML Writer with an object data type output for the variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Step 4: Add optional step instructions

You can include optional step instructions for anything your agent needs to know that is specific to this step and not already covered in the agent's main instructions. You can enter any Liquid templated values that you would normally use in a Canvas.

### Step 5: Test the agent {#step-5-test-the-agent}

You can test an Agent step in two ways:

**In-step preview (Canvas builder):** After configuring the step, use the step preview to see agent output for a random user, an existing user, or a custom user. This tests the step in isolation without walking the full Canvas path.

**Test Canvas (full journey):** Select **Test Canvas** in the Canvas footer to preview the user path end-to-end. When the test reaches your Agent step, Braze asks **Do you want to run the agent "{agentName}"?**

- Select **Yes** to optionally add context, then select **Simulate response** to invoke the agent for the preview user. You can describe sample inputs in plain language (for example, cart contents or message text) to supplement the test user's profile and any Canvas context already set upstream.
- Select **No** to skip the live invocation and use the agent's configured **fallback output** from Agent Console instead.

Invocations from **Simulate response** count toward the agent's daily invocation limit and appear in **Agent Console** > **Logs**. For full Test Canvas behavior, see [Preview user paths]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps).

![Preview the agent output as a random user.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Error handling {#error-handling}

For how Braze handles agent failures, rate limit errors, and invocation flow controls, see [Error handling and fallback behavior]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) in Deploy agents and [Error handling]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) in Braze Agents.

- If the connected model returns a [rate limit error]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) from the LLM provider, Braze continuously retries the request using exponential backoff until the call succeeds or Braze determines it cannot be completed; users then proceed to the next Canvas step.
- For other failures (such as a timeout error or invalid API key), or when an agent reaches its daily invocation limit, the output variable is set to `null` unless the agent has [fallback values configured]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in Agent Console. When fallback values are configured, Braze renders the fallback with Liquid per user and stores the result in the output variable, including when the daily limit blocks an invocation.
- If you do not configure fallback values, use [default Liquid values]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) in downstream Message steps to handle null outputs. For example, in the **Add Personalization** modal, you can enter a default Liquid value such as {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} or {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Responses are cached for identical inputs and may be reused for repeated identical invocations within a few minutes.
    - Responses that use cached values do still count toward total and daily invocations.
- Agent steps may take time to process a large batch of users. Braze queues invocations according to [invocation flow controls]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), so users may remain pending during high-volume sends. Check your logs to verify that invocations are happening.

## Analytics  

Refer to the following metrics to track how your Agent steps perform:  

| Metric | Description |
| --- | --- |
| _Entered_ | The number of times users entered the Agent step. |
| _Proceeded to Next Step_ | The number of users that proceeded to the next step in the flow after passing through the Agent step. |
| _Exited Canvas_ | The number of users that exited the Canvas after passing through the Agent step. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }

## Best practices

### Split tasks between agents for complicated use cases

If you find that an agent is struggling with the complexity of tasks you’re asking it to do, split the work across more than one Agent step. When one prompt mixes data cleanup, routing logic, and full message writing, those goals compete and output quality can vary.

The following pattern uses three agents for a travel example: someone searched in your app recently but didn’t book, and you want retargeting copy that nudges them toward checkout.

- Agent 1 summarizes Canvas context. It reads fields such as loyalty tier, last city searched, and high-intent search behavior, and returns a short structured summary as an output variable that later steps can reuse.
- Agent 2 returns a routing value your Canvas can branch on. Use a number, boolean, or structured object so the output matches how you branch. Map that value to an [Audience Paths]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) or [Decision Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) step. For example, consider separate paths for loyalty-led messaging versus deal-led messaging.
- Agent 3 drafts generated message text only on branches where you want it. Pass the Agent 1 summary (and any branch-specific context) so this agent focuses on tone and channel limits instead of normalizing inputs and choosing strategy in the same prompt.

### Use the Experiment Paths step to test agentic journeys at small scale

To test your agent's performance and credit consumption against your existing journeys, add an [Experiment Paths]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) step so only part of your audience enters the branch that contains your Agent step. 

For example, you can start by sending a few thousand users per day down a path with the agent and send the rest to a control path or a path without the agent. Gather data for 1-2 weeks and compare key performance indicators (KPIs), counter-metrics, and agent credit consumption between paths. This way, you can build confidence and prove ROI before you increase traffic to the agent-enabled branch, and limit invocation consumption to do it.

## Frequently asked questions

### When should I use an Agent step?

In general, we recommend using an Agent step when you want to feed particular contextual data into an LLM and have it agentically assign a Canvas context variable intelligently at a scale impossible for humans.

Let’s say you’re sending a personalized message to recommend a new ice cream flavor to a user who previously ordered chocolate and strawberry. Here’s the difference between using an Agent step versus AI item recommendations:

- **Agent step:** Uses LLMs to make a qualitative decision on what the user might want based on the instructions and context data points given to the agent. In this example, an Agent step might recommend a new flavor based on the possibility of the user wanting to try different flavors.
- **AI item recommendations:** Uses machine learning models to predict the products that a user is most likely to want based on past user events, such as purchases. In this example, AI item recommendations would suggest a flavor (vanilla) based on the user’s previous two orders (chocolate and strawberry) and how those compare to the behaviors of other users in your workspace.

### How do Agent steps use input data?

An Agent step analyzes the context data that the agent is configured to use, as well as any [optional step instructions](#step-4-add-optional-step-instructions) you add to the step.

## Related articles  

- [Braze Agents overview]({{site.baseurl}}/user_guide/brazeai/agents)  
- [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)  
- [Deploy agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)  
- [Reference for agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)
