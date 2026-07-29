# Setting up the Braze MCP server

> Learn how to connect to the Braze remote MCP server, authenticate with OAuth, and start using Braze tools from your MCP client. For more information, see [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prerequisites

Before you start, make sure you have the following:

| Prerequisite | Description |
|--------------|-------------|
| Early Access enrollment | Your account manager can enroll your company in the Early Access program. |
| Supported MCP client | Any client that supports remote MCP servers with OAuth can work. Braze has verified Claude, ChatGPT, Cursor, OpenAI Codex, and Claude Code. |
| Braze dashboard account | You sign in with your normal Braze credentials, including SSO or SAML if your company uses it. There is no separate MCP login. |
| Server endpoint selection | Choose `https://mcp.braze.com/mcp` (US) or `https://mcp.braze.eu/mcp` (EU). Either endpoint can reach any Braze cluster. |
| No IP allowlisting | Customers who use [IP Allowlisting](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) cannot participate in Early Access at this time. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert note %}
Your agent's access mirrors your dashboard permissions. If your dashboard access is scoped to a team rather than a full workspace, some tools may not work during Early Access.
{% endalert %}

## Managing access (for admins)

### Grant access

Admins control access to the MCP server through the **Use MCP Server** permission. By default, users do not have this permission and it must be explicitly granted.

If an admin does not see this permission, contact your Braze account manager to request Early Access enrollment.

### Revoke access

To revoke access, remove the **Use MCP Server** permission from the user. Removing dashboard permissions from a user also removes those capabilities from any connected agent on the next request.

### Audit usage

When a user successfully connects through OAuth, an event is logged to the [security event report](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report).

## Connect your client

### Step 1: Confirm permissions and workspace access

1. You or your company admin need to confirm you have the **Use MCP Server** permission.
2. If you need access to multiple workspaces, make sure the permission is enabled for all relevant workspaces.

### Step 2: Add Braze as a remote MCP connector

In your MCP client, add a new remote server or custom connector and enter your Braze MCP URL. For example, in Claude you can go to **Settings** > **Connectors** > **Add custom connector** and paste the URL.

No client ID, client secret, or API key is required. Your client registers itself with Braze automatically.

Braze MCP endpoint options:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

{% alert tip %}
EU customers should use the EU endpoint. Non-EU customers can use either endpoint.
{% endalert %}

Client setup guides:

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)

### Step 3: Sign in to Braze through OAuth

The first time your agent calls a Braze tool, your client opens a browser window and sends you to Braze to sign in.

1. Sign in to Braze as you normally would, including SSO if required.
2. If your login can access more than one company on the same cluster, select the company you want to use.
3. On the consent screen, review the access the application is requesting.
4. Select the acknowledgment checkbox to agree to the Braze Privacy Policy, then select **Continue** to return to your MCP client.

![The Braze consent screen showing that Claude Desktop is requesting access to Braze account information and broad access to Braze data, with a Privacy Policy acknowledgment checkbox and Cancel and Continue buttons.]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: style="max-width:65%;"}

Your session uses short-lived access tokens that refresh automatically. You may occasionally need to sign in again.

### Step 4: Tell your agent which workspace to use

If your account can access more than one workspace, specify the workspace in your prompt. For example:

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

If you do not specify a workspace, your agent may ask you to clarify.

### Step 5: Send a test prompt

After setup, send a quick validation prompt such as:

- `List the Braze tools available in this workspace.`
- `Show my recent Canvases from the Production workspace.`

For more examples, see [Using the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

## Example: Connect with Claude

Connecting a client takes only a few steps. The following walkthrough uses Claude, but the flow is similar for other supported clients.

1. In Claude, go to **Settings** > **Connectors** > **Add custom connector**.
2. Enter a name, such as `Braze`, then paste your Braze MCP URL: `https://mcp.braze.com/mcp` for US or `https://mcp.braze.eu/mcp` for EU. You don't need a client ID, client secret, or API key.
3. Select **Add** to save the connector. Claude registers itself with Braze automatically.
4. Select **Connect** to start authentication. Claude opens a browser window and sends you to Braze to sign in.
5. Sign in to Braze with your usual credentials, including SSO if your company uses it. If your login can access more than one company on the same cluster, select the company you want to use.
6. On the consent screen, review the requested access, select the acknowledgment checkbox, then select **Continue**. Claude returns to your chat, and your agent can now use Braze tools.

To confirm the connection, send a test prompt such as `Show my recent Canvases from the Production workspace`.

## Migrating from the local beta server

You can run the local beta server and the remote-hosted server side by side during migration. You may need to explicitly tell your agent which one to use.

The remote-hosted server includes new tools that do not exist in the local beta server. If you built skills for the local server, you may need to update those skills to reference new tool names and behavior.

After you confirm your workflows and skills are working on the remote server, disable the local-hosted server.

## Troubleshooting

### Authentication fails in a supported client

1. Confirm your company is enrolled in Early Access.
2. Confirm your user has the **Use MCP Server** permission.
3. Retry sign-in and authorization.

### Authentication is blocked in an unverified client

During Early Access, Braze maintains an allowlist of supported client domains for security. If you connect from a client that isn't on the allowlist, authentication may be blocked. If you believe your client should be supported, contact [mcp-product@braze.com](mailto:mcp-product@braze.com).

Clients that run locally on your machine without a custom scheme, such as Claude Code and OpenAI Codex, should also work.

### Tools don't appear in your client

If your agent can't list the Braze tools, wait a few minutes and try again. These issues are often temporary and resolve on their own.

If the problem continues, record a video and send it to [mcp-product@braze.com](mailto:mcp-product@braze.com) for investigation.

### Agent cannot access expected tools

1. Confirm your dashboard user has the required permissions. Your agent can only use tools that match your own dashboard access.
2. Confirm you selected the expected workspace in your prompt.
3. Ask your agent to call `get_workspaces` and verify the available workspace IDs.

### Agent uses the wrong workspace

If your account can access more than one workspace, name the workspace in your prompt using the exact name shown in the Braze dashboard. If you don't specify a workspace, your agent may ask you to clarify or use an unexpected one.

{% alert important %}
Before your agent starts work, always confirm which workspace it is using. In some cases, an agent may select a different workspace than the one you intended.
{% endalert %}

### Switching to a different company

Your company is set when you first authorize. To work in a different company on the same cluster, disconnect the Braze connector in your client, re-authorize, and select the other company during sign-in.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
