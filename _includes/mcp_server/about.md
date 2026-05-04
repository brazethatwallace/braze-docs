# The Braze MCP server

> Learn about the Braze MCP server, a secure connection that lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, and provide insights.

{% multi_lang_include mcp_server/beta_alert.md %}

## What is Model Context Protocol (MCP)?

​​Model Context Protocol, or MCP, is a standard that lets AI agents connect to and work with data from another platform. It has two main parts:

- **MCP client:** The application where the AI agent runs, such as Cursor or Claude.
- **MCP server:** A service provided by another platform, like Braze, that defines which tools the AI can use and what data it can access.

## About the Braze MCP server

After [setting up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, you can connect AI tools like agents, assistants, and chatbots directly to Braze, allowing them to read aggregated data such as Canvas and Campaign analytics, custom attributes, segments, and more. The Braze MCP server is great for:

- Building AI-powered tools that need Braze context.
- CRM engineers creating multi-step agent workflows.
- Technical marketers experimenting with natural language queries.

The Braze MCP server supports 39 endpoints that do not return data from Braze user profiles. You can choose which endpoints to assign to your Braze API key to control what an agent can access or change.

{% alert warning %}
Only assign the API key permissions you want your agent to have. If you don't want your agent to make changes in Braze, ensure you leave write permissions off. Agents may try to write data through any permission you grant.
{% endalert %}

## Usage example

You can interact with Braze through natural language using tools like Claude or Cursor. For other examples and best practices, see [Using the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!['What are my available Braze functions?' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['What are my available Braze functions' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Frequently Asked Questions (FAQ) {#faq}

### Which MCP clients are supported?

Only [Claude](https://claude.ai/) and [Cursor](https://cursor.com/) are officially supported. You must have an account for one of these clients to use the Braze MCP server.

### What Braze data can my MCP client access?

MCP clients can access endpoints that don't return PII. You control which endpoints an agent can use through the permissions you assign to your API key.

### Can my MCP client change Braze data?

The server only exposes the `/media_library/create` write endpoint, which enables you to upload media assets into your media library. If you don't want your agent to make those changes in Braze, leave the `media_library.create` permission unchecked when you create your API key.

### Can I use a third-party MCP server for Braze?

Using a third-party MCP server for Braze data is not recommended. Only use the official Braze MCP server hosted on [PyPi](https://pypi.org/project/braze-mcp-server/).

### Why doesn't the Braze MCP server offer PII access?

To protect user data while supporting valuable use cases, the server is limited to endpoints that don't typically return PII. This reduces risk for your workspace and the people in it.

### Can I reuse my API keys?

No. You'll need to create a new API key for your MCP client. Remember to only give your AI tools access to what you’re comfortable with, and avoid elevated permissions.

### Is the Braze MCP server hosted locally or remotely?

The Braze MCP server is hosted locally.

### Why is Cursor only listing functions?

Check if you're in ask mode or agent mode. To use the MCP server, you need to be in agent mode.

### What do I do when the agent returns an answer that looks incorrect?

When working with tools like Cursor, you may want to try changing the model used. For example, if you have it set to auto, try changing it to a specific model and experiment to find which model performs best for your use case. You can also try starting a new chat and retrying the prompt. 

If issues persist, you can email us at [mcp-product@braze.com](mailto:mcp-product@braze.com) to let us know. If possible, include a video and expand the call functions so we can see what calls the agent attempted.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
