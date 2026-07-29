# The Braze MCP server

> Learn about the Braze MCP server, a secure remote connection that lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, provide insights, and create content.

{% alert important %}
The remote MCP server is in Early Access. Contact your account manager to request access.
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

The Braze MCP server includes both read and write tools. These tools do not return data from Braze user profiles. Your agents inherit your Braze dashboard user permissions. For the full list of available tools, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Tools that expose user-level PII are not available.
{% endalert %}

Use the MCP server to ask questions about campaign and Canvas performance, explore your segments and custom attributes, generate reports, and create content such as email templates, content blocks, and media library assets through natural language.

## Is the beta MCP server deprecated?

Yes. The locally hosted MCP server released in August 2025 is deprecated and will not receive additional updates. You can continue using it, but Braze recommends migrating to the remote-hosted version.

### How is the remote server different?

The previous Braze MCP server ran locally on your machine. You needed to install a package, manage a config file, and create a Braze API key with the right permissions. The remote MCP server removes that local setup.

Connect from a supported MCP client in under a minute. Authentication uses OAuth. Access is tied to your Braze dashboard user account, not a shared API key, so what an agent can see and do mirrors your dashboard permissions. If a dashboard user loses access in Braze, the client loses access too.

The key differences are:

- **Setup:** Paste a Braze URL instead of installing a package and editing config files.
- **Auth:** Sign in with your Braze account instead of creating an API key.
- **Permissions:** Access is based on your dashboard user account instead of API key permissions.
- **Workspace targeting:** Workspace context is passed per request instead of being fixed in local config.

## Frequently Asked Questions (FAQ) {#faq}

### Which MCP clients are supported?

Any MCP client that supports remote MCP servers with OAuth can work. Braze has verified:

- Claude through custom connectors
- ChatGPT through custom connectors
- Cursor
- OpenAI Codex
- Claude Code
- Visual Studio Code

### What Braze data can my MCP client access?

MCP clients can access tools that do not return user-level PII.

### Can my MCP client change Braze data?

Yes, if your dashboard user has those permissions.

### Do I still need a Braze API key?

Not for MCP. API keys still work for the REST API and are not being deprecated.

### Which regions are supported?

Both Braze clusters are supported. Two endpoints are available today:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

Either endpoint can reach any Braze cluster.

### Can I use the Braze remote MCP server with tools other than the verified list?

You can try, but authentication may be blocked. Braze currently maintains an allowlist of supported domains for security. If your tool is not on the list and you run into authentication issues, contact [mcp-product@braze.com](mailto:mcp-product@braze.com).

### Does the remote server support multiple workspaces?

Yes. Specify the workspace per conversation or per request. One connection covers all workspaces you are authorized to access.

### Can my agent access user-level PII?

No. As of now, tools that expose PII are not available.

### What happens when my permissions change?

Agent access changes with the dashboard user. Permission changes apply on the next request. Deactivated dashboard users lose MCP access.

### Why do I not see the Braze connector in my client's directory?

Directory listings roll out after Early Access begins. You can always connect manually using the Braze MCP URL.

### My company uses IP allowlisting. Can we use the remote MCP server?

Not right now. Customers who use [IP Allowlisting](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) cannot participate in the Early Access program.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
