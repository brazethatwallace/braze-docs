# Using the Braze MCP server

> Learn how to interact with your Braze data through natural language after connecting to the remote Braze MCP server. For more information, see [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Best practices

When using the Braze MCP server through natural-language tools, keep these tips in mind:

- Confirm the workspace in your prompt, especially when you have access to multiple workspaces.
- Be specific about date ranges and metrics when requesting analytics.
- Ask the agent to confirm which tools it used when validating outputs.
- Compare high-impact recommendations against source data in the Braze dashboard.

## Usage examples

After [setting up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, you can interact with Braze through natural language. Here are examples to get started.

### Which workspaces can I access?

{% tabs %}
{% tab Example prompt %}

`Show my available Braze workspaces and tell me which one to use for production campaign analytics.`
{% endtab %}
{% tab Example response %}

I called `get_workspaces` and found these workspaces:

- `Marketing - Production` (`app_group_id`: `YOUR-APP-GROUP-ID-1`)
- `Marketing - Staging` (`app_group_id`: `YOUR-APP-GROUP-ID-2`)

Use `Marketing - Production` for production campaign analytics prompts.
{% endtab %}
{% endtabs %}

For more information, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}.

### Show me campaign performance for last week

{% tabs %}
{% tab Example prompt %}

`In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.`
{% endtab %}
{% tab Example response %}

I used `get_campaign_list` and `get_campaign_dataseries` for the requested workspace and date range.

Summary:

- Total sends: `YOUR-TEST-SENDS`
- Total opens: `YOUR-TEST-OPENS`
- Total clicks: `YOUR-TEST-CLICKS`
- Top campaign by opens: `YOUR-TEST-CAMPAIGN-NAME`

I can break this down by campaign, channel, or day if needed.
{% endtab %}
{% endtabs %}

For more information, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}.

### Create an email template

{% tabs %}
{% tab Example prompt %}

`In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab Example response %}

I used `create_email_template` and created your template.

- **Template ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **Template name:** `YOUR-TEST-TEMPLATE-NAME`
- **Workspace:** `Marketing - Production`
{% endtab %}
{% endtabs %}

For more information, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates-email){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates-email){% endif %}.

## Example workflows

These examples combine multiple tools to complete a task from start to finish.

### Report across multiple workspaces

{% tabs %}
{% tab Example prompt %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab Example response %}

I called `get_workspaces` to confirm access, then ran `get_campaign_dataseries` for each workspace over the past seven days.

- `US Prod`: `YOUR-TEST-SENDS` sends, `YOUR-TEST-OPEN-RATE` open rate
- `EU Prod`: `YOUR-TEST-SENDS` sends, `YOUR-TEST-OPEN-RATE` open rate

`US Prod` sent more messages this week, while `EU Prod` had the higher open rate. I can break either workspace down by campaign or channel.
{% endtab %}
{% endtabs %}

### Copy templates from staging to production

{% tabs %}
{% tab Example prompt %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab Example response %}

I used `get_email_templates` and `get_email_template_info` to read the templates in `Staging`, then `create_email_template` to recreate each one in `Production`.

- `YOUR-TEST-TEMPLATE-NAME-1`: created in `Production` (`YOUR-TEST-TEMPLATE-ID-1`)
- `YOUR-TEST-TEMPLATE-NAME-2`: created in `Production` (`YOUR-TEST-TEMPLATE-ID-2`)

I skipped drag-and-drop editor templates, which `get_email_template_info` doesn't support. Let me know if you'd like me to review the copied templates.
{% endtab %}
{% endtabs %}

### Summarize weekly campaign health

{% tabs %}
{% tab Example prompt %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab Example response %}

I used `get_campaign_list` and `get_campaign_dataseries` to pull the past seven days of activity in `Production`.

- Total sends: `YOUR-TEST-SENDS`
- Open rate: `YOUR-TEST-OPEN-RATE`
- Click rate: `YOUR-TEST-CLICK-RATE`
- Top campaign by conversions: `YOUR-TEST-CAMPAIGN-NAME`

Sends were up week over week. I can add a channel breakdown or flag any campaigns with declining engagement.
{% endtab %}
{% endtabs %}

## How the remote MCP server works

When you send a request, a few steps happen behind the scenes:

1. **You prompt your client.** You type a request in natural language, such as asking for last week's campaign performance.
2. **The client's model selects tools.** The AI model in your client interprets your request and translates it into one or more Braze tool calls, such as `get_campaign_list` and `get_campaign_dataseries`.
3. **Braze runs the tool call.** The remote MCP server receives each tool call over your authenticated OAuth session, applies the workspace you specified, and runs it against the matching Braze REST API endpoint.
4. **Braze returns the result.** The server sends the data back to your client, which formats and presents it to you.

Your access is the intersection of two things:

- **The scopes granted when you authorized the connection**, such as `mcp:tools`.
- **Your own dashboard user permissions.** If you can't view campaigns in the dashboard, your agent can't either. If you can create email templates, your agent can too. An agent can never exceed your own access.

Workspace context is passed with each request rather than stored in a local config file, so one connection can work across every workspace you're authorized to access.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
