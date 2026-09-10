---
nav_title: Knowledge sources
article_title: Knowledge sources
description: "This reference article covers how to create and manage knowledge sources for your BrazeAI agents."
page_type: reference
page_order: 3.5
---

# Knowledge sources

> Knowledge sources help your AI agents interpret catalog data and retrieve the right information to meet your goals. For an introduction to Braze Agents, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). To add knowledge to an agent, see [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources).

## How it works

Knowledge sources are a type of agent context. An AI agent can reference a knowledge source to retrieve data from the catalog more accurately than if the catalog is referenced directly in the agent's instructions. 

Let's say you're building an agent to recommend restaurants in New York City based on a user's favorite cuisine, which is a custom attribute. This agent references the knowledge source for the "nyc_restaurants" catalog. When you create that knowledge source, you include only the fields the agent needs—such as restaurant name, location, and cuisine—and exclude other catalog columns that don't support recommendations.

The agent's instructions clearly describe its role and constraints:

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

If a user's favorite cuisine is pizza, the agent can return the following response based on the knowledge source:

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## Create a knowledge source

To create a knowledge source:

1. Go to **Agent Console** > **Knowledge Sources**.
2. Select **Add Knowledge Source**. In the dropdown, select **Catalog**.
3. Select the catalog from the dropdown.
4. Review the catalog fields and deselect any that don't apply to your agent's use case. We recommend excluding catalog fields that aren't useful for retrieval or generation—limit the knowledge source to only the fields your agent needs.
5. (optional) Add a description to describe what the knowledge source contains.
6. Select **Add Knowledge Source**.

Including every catalog field can add unnecessary context and may reduce output quality. Deselecting fields that aren't relevant to your use case helps the agent focus on the data that matters.

![A knowledge source "nyc_restaurants" that references the catalog "nyc_restaurants".]({% image_buster /assets/img/ai_agent/knowledge_source_example.png %})

You can also create a knowledge source as you're building an agent by going to the **Instructions** section of your agent. Select **Add knowledge** > **Create knowledge source**.

## Use a knowledge source in your AI agent

You can manage knowledge sources from the **Knowledge Sources** section. Here, you can see details such as which knowledge sources are active and when they were last synced. Note that the name of the knowledge source matches the name of the catalog used as the source.

To use a knowledge source in your AI agent:

1. Go to the **Instructions** section of your agent. 
2. Select **+ Agent context** > **Add knowledge**. 
3. From the dropdown, select the knowledge source.

Now, your agent can reference the knowledge source and retrieve the relevant catalog data.

## Frequently asked questions

### How do knowledge sources work?

Converting a catalog into a knowledge source helps Braze Agents understand the true meaning behind the words and phrases in the catalog, so that agents can more effectively find meaningful data to drive better outputs.

### When should I create a knowledge source?

Create a knowledge source when you're setting up a custom agent (Canvas Step Agent or Catalog Agent) that needs catalog data as context. Knowledge sources help agents retrieve catalog data more accurately than referencing the catalog directly in the agent's instructions.

### If an agent has been given a knowledge source as context, do I also need to assign the original catalog as context?

No. The knowledge source replaces the catalog as agent context—you don't need to attach both. When you create the knowledge source, include only the catalog fields your agent needs.

### How should I evaluate the effectiveness of a knowledge source?

Duplicate any existing agent you use that references a regular catalog, and switch it to reference the equivalent knowledge source instead. Run a few test invocations in Agent Console to ensure accuracy, and then consider either replacing the existing agent where it's being deployed, or A/B testing the old agent against the new agent (using Experiment Path step) to understand performance impact.
