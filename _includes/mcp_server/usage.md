# Using the Braze MCP server

> Learn how to interact with your Braze data through natural language using tools like Claude and Cursor. For more general information, see [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Best practices

When using the Braze MCP server through natural-language tools like Claude and Cursor, keep these tips in mind to get the best results:

- LLMs can make mistakes, so always be sure to double-check their answers.
- For data analysis, be clear about the time range you need. Shorter ranges often give more accurate results.
- Use exact [Braze terminology](https://www.braze.com/resources/articles/glossary) so your LLM calls the right function.
- If results seem incomplete, prompt your LLM to continue or dig deeper.
- Try creative prompts! Depending on your MCP client, you may be able to export a CSV or other useful files.

## Usage examples

After [setting up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, you can interact with Braze through natural language using tools like Claude or Cursor. Here's some examples to get you started:

### What are my available Braze functions?

{% tabs %}
{% tab Claude %}
!['What are my available Braze functions?' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['What are my available Braze functions' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

For more information on the `list_functions` function, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Get details about a Canvas ID

{% tabs %}
{% tab Claude %}
!['Get details about a canvas ID' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Get details about a canvas ID' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

For more information on the `get_canvas_details` function, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Show me my recent Canvases

{% tabs %}
{% tab Claude %}
!['Show my recent canvases' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Show my recent canvases' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

For more information on the `get_canvas_list` function, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Create an email template

{% tabs %}
{% tab Cursor %}
!['Create an email template' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/create_an_email_template.png %})
{% endtab %}
{% endtabs %}

For more information on the `create_email_template` function, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Update a content block

{% tabs %}
{% tab Cursor %}
!['Update a content block' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/update_a_content_block.png %})
{% endtab %}
{% endtabs %}

For more information on the `update_content_block` function, see [Available API functions]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
