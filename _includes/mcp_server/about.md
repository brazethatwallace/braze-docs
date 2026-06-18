# The Braze MCP server

> Learn about the Braze MCP server, a secure connection that lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, and provide insights.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert important %}
## Sunsetting the locally hosted Braze MCP server

This summer, Braze is launching a remote, Braze-hosted MCP server in Early Access. It replaces the locally hosted beta server (`braze-mcp-server` on [PyPI](https://pypi.org/project/braze-mcp-server/) and the Claude Desktop extension directory).

**What this means for you:**

- The locally hosted server will continue to work, but it is no longer supported. We won't be adding new endpoints or fixing issues in the beta.
- When the remote server is available in Early Access, you'll need to switch to it. The remote server requires no local installation, uses OAuth instead of static API keys, and works with MCP clients like Claude, Copilot, Gemini CLI, Codex, and Cursor.
- Watch this page for Early Access availability, or contact your Braze account team to express interest.
{% endalert %}

## What is Model Context Protocol (MCP)?

​​Model Context Protocol, or MCP, is a standard that lets AI agents connect to and work with data from another platform. It has two main parts:

- **MCP client:** The application where the AI agent runs, such as Cursor or Claude.
- **MCP server:** A service provided by another platform, like Braze, that defines which tools the AI can use and what data it can access.

## About the Braze MCP server

After [setting up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, you can connect AI tools like agents, assistants, and chatbots directly to Braze, allowing them to read aggregated data such as Canvas and Campaign analytics, custom attributes, segments, and more. The Braze MCP server is great for:

- Building AI-powered tools that need Braze context.
- CRM engineers creating multi-step agent workflows.
- Technical marketers experimenting with natural language queries.

The Braze MCP server includes both read-only and write endpoints. They do not return data from Braze user profiles. You choose which endpoints to assign to your Braze API key, and that choice controls what an agent can read, create, or update. For the full list of available endpoints and their required permissions, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Only assign the API key permissions you want your agent to have. If you don't want your agent to make changes in Braze, leave any write permissions off when you create your API key. Agents may try to write data through any write permission you grant.
{% endalert %}

## Usage example

You can interact with Braze through natural language using tools like Claude or Cursor. For other examples and best practices, see [Using the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Used `list_functions` and returned the available Braze MCP function categories.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Queried `list_functions` and listed functions such as `get_canvas_list`.
{% endtab %}
{% endtabs %}

## Frequently Asked Questions (FAQ) {#faq}

### Which MCP clients are supported?

Only [Claude](https://claude.ai/) and [Cursor](https://cursor.com/) are officially supported. You must have an account for one of these clients to use the Braze MCP server.

### What Braze data can my MCP client access?

MCP clients can access endpoints that don't return PII. You control which endpoints an agent can use through the permissions you assign to your API key.

### Can my MCP client change Braze data?

Yes. The server exposes a focused set of write endpoints that let agents create or update content in your workspace, such as media library assets, email templates, and content blocks. Each write endpoint requires its own API key permission. If you don't want your agent to make a given change in Braze, leave that permission off when you create your API key. For the full list of write functions and their required permissions, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

### Can I use a third-party MCP server for Braze?

Using a third-party MCP server for Braze data is not recommended. Only use the official Braze MCP server hosted on [PyPi](https://pypi.org/project/braze-mcp-server/).

### Why doesn't the Braze MCP server offer PII access?

To protect user data while supporting valuable use cases, the server is limited to endpoints that don't typically return PII. This reduces risk for your workspace and the people in it.

### Can I reuse my API keys?

No. You'll need to create a new API key for your MCP client. Remember to only give your AI tools access to what you’re comfortable with, and avoid elevated permissions.

### Is the Braze MCP server hosted locally or remotely?

The currently available Braze MCP server is hosted locally. A remote, Braze-hosted MCP server is coming to Early Access this summer and will replace the locally hosted beta server.

### Why is Cursor only listing functions?

Check if you're in ask mode or agent mode. To use the MCP server, you need to be in agent mode.

### What do I do when the agent returns an answer that looks incorrect?

When working with tools like Cursor, you may want to try changing the model used. For example, if you have it set to auto, try changing it to a specific model and experiment to find which model performs best for your use case. You can also try starting a new chat and retrying the prompt. 

If issues persist, you can email us at [mcp-product@braze.com](mailto:mcp-product@braze.com) to let us know. If possible, include a video and expand the call functions so we can see what calls the agent attempted.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
