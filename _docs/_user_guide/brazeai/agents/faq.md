---
nav_title: FAQ
article_title: Agents FAQ
description: "This article provides answers to frequently asked questions about Braze Agents."
page_order: 10
toc_headers: h2
---

# Agents frequently asked questions

> This article answers frequently asked questions about Braze Agents.

## General

### What is the difference between Canvas Agents and Catalog Agents?

When creating an agent, you specify if you want to create a Canvas Agent or Catalog Agent. This determines the types of instructions and options the agent can support. Canvas Agents process users in real-time within journeys, while Catalog Agents enrich catalog data by adding or updating columns with processed information.

### What are the benefits of using Auto model versus bring-your-own (BYO) model?

Benefits of using the Braze Auto model include:

- Not requiring any retrieval or entry of API keys or integration setup
- Automatic routing of each invocation to the most effective model to do the job

### Where can I find my current agent usage?

Go to **Settings** > **Billing** > **Credits Usage** > **Agent Console** to see credit consumption, invocation counts, and per-agent credit ratios. See [Daily invocation and credit limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) for more details.

### Can I use conditional Liquid statements in agent instructions?

No, attempting to write Liquid blocks like {% raw %}`{% if %}{% endraw %} statements can result in a validation error. Agents can handle different scenarios through natural language descriptions in the prompt instead.

### Can agents access user data beyond the specific Liquid attributes or Canvas context that I pass to them?

No. Agents only receive the specific user data points that are passed using Liquid in instructions, [+ Agent context]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources) selections, upstream [Context steps]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) in Canvas, or additional context on the Agent step. Agents cannot search user profiles for attributes you did not configure them to receive.

Agents also cannot warn you when required data is missing—they proceed with whatever is in the prompt. Treat agent setup as deliberate input-to-output design: pass every field the agent needs and verify inputs in **Agent Console** > **Logs**. For guidance, see [What data agents receive]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Troubleshooting

### Why did my agent not follow my instructions or rules?

Consider using [Operator]({{site.baseurl}}/user_guide/brazeai/operator) to troubleshoot why your agent is not following your instructions. Operator can provide step-by-step instructions and detailed explanations.

### Why did my catalog agent skip some rows?

Catalog agents skip a row when a column you marked **required to run** is blank or missing—for example, a `gender` field that has not been filled in. After you select input columns, enable the required-input control for the catalog field and choose which columns must contain values before the agent runs; selected columns start as required by default, but you can remove columns that are allowed to be empty without blocking the invocation. This avoids wasted tokens on incomplete data.

The agent also respects column dependencies. If an output column depends on other columns (for example, column D requires values in columns B and C), the agent does not run until those upstream columns are populated for that row.

For more details, see [Catalog agent best practices]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### My agent is struggling with a complex task. How might I improve its performance? {#subagent-approach}

If you find that the agent is struggling with the tasks you're asking it to do, consider a sub-agent approach. For example, you could use three agents to do the following:

- Agent 1 standardizes and transforms inbound unstructured Canvas context data.
- Agent 2 references a catalog of item details and identifies which items might be relevant.
- Agent 3 references a different catalog that has a variety of possible descriptions for each item and identifies the item description most relevant to the user to place in an email.

### What might cause a custom agent to frequently time out?

A custom agent may time out if:

- The agent instructions have incomplete or contradictory instructions
- The agent instructions do not cover off on all scenarios or include a fallback condition (such as "If all inputs are blank, output 'Could not personalize'")
- The agent instructions ask the agent to output a different output format than the one specified in the **Output** tab (for example, if the agent instructions ask for a string, but in **Output** tab the output is defined as a number)
- The agent's task is too complex and would benefit from a [sub-agent approach](#subagent-approach) instead

For Canvas agents, configure [fallback values]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in Agent Console so users still receive output when an invocation fails.

### Why did my agent do fine in testing but isn't getting any user-specific data when I launch it in a Canvas?

If your agent works correctly during testing but does not receive user-specific data in a live Canvas, try these troubleshooting steps:

- Make sure the user-specific data you want the agent to receive is entered as Liquid variables in the agent instructions.
- If you have important data in Canvas context, use the **Add all Canvas context** option in the agent configuration to ensure the agent receives the entire Canvas context.
- Make sure any Canvas context you want the agent to access is stored as Canvas context. Use a context step before the agent step to store this data.

## Compliance

### Is Agent Console GDPR/CCPA compliant?

Yes. When a Customer uses Braze Auto model (powered by Gemini), Google will be acting as a Braze Sub-processor, subject to the terms of the Data Processing Addendum (DPA) between the Customer and Braze.

### Is Agent Console HIPAA compliant?

Yes. When using the Braze Auto model, we have a specific HIPAA agreement, the Business Associate Addendum (BAA), with Google covering Gemini, which powers our Auto model.

Our BAA applies only to customers using the Braze Auto model. If customers use their own LLM key, Braze does not send Protected Health Information (PHI) subject to HIPAA to an LLM on their behalf; customers send it directly. In this case, the BAA between Braze and Google does not apply. Data processing through their own LLM key is governed by the customer's contract and any BAA they have directly with their LLM provider.