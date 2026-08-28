# Braze MCP server functions

> The Braze MCP server exposes read and write tools that map to specific Braze REST API endpoints. For more information, see [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
The Braze MCP server includes tools that are only available to customers participating in beta programs. If you try to access a tool that is part of a beta program and your account does not have the feature enabled, you may receive an error response. To join a beta program, contact your account manager.
{% endalert %}

## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Available Braze API functions

Your MCP client references these tools to interact with the Braze MCP server.

### Workspaces

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | read | Discover which Braze workspaces the current OAuth access token can reach. Call this first: each returned workspace `id` is the `app_group_id` every other tool requires. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Workspaces" }

### Campaigns

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | read | Export a list of campaigns with name, campaign API identifier, API-campaign flag, and tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | read | Retrieve relevant information on a specified campaign by `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | read | Daily series of campaign stats over time (sends, opens, clicks, conversions by channel). |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | create | Duplicate an existing campaign. |
| `create_campaign`<sup>*</sup> | N/A | create | Create a new campaign. |
| `edit_campaign`<sup>*</sup> | N/A | update | Edit an existing campaign. |
| `launch_campaign`<sup>*</sup> | N/A | update | Launch a campaign. |
| `stop_campaign`<sup>*</sup> | N/A | update | Stop a running campaign. |
| `archive_campaign`<sup>*</sup> | N/A | update | Archive a campaign. |
| `unarchive_campaign`<sup>*</sup> | N/A | update | Unarchive a campaign. |
| `get_campaign_draft`<sup>*</sup> | N/A | read | Retrieve draft campaign details. |
| `get_campaign_live_details`<sup>*</sup> | N/A | read | Retrieve live campaign details. |
| `create_campaign_message`<sup>*</sup> | N/A | create | Create a message within a campaign. |
| `update_campaign_message`<sup>*</sup> | N/A | update | Update a campaign message. |
| `delete_campaign_message`<sup>*</sup> | N/A | delete | Delete a campaign message. |
| `create_campaign_message_variation`<sup>*</sup> | N/A | create | Create a message variation within a campaign. |
| `update_campaign_message_variation`<sup>*</sup> | N/A | update | Update a campaign message variation. |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | delete | Delete a campaign message variation. |
| `update_campaign_distribution`<sup>*</sup> | N/A | update | Update campaign distribution settings. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

<sup>*</sup> This tool is only available to customers participating in the campaign APIs beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.
{: .reset-td-br-1 }

### Canvases

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | read | Export a list of Canvases with name, Canvas API identifier, and tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | read | Export Canvas metadata: name, time created, current status, and more. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | read | Export time series data for a Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | Export rollups of Canvas time series data for a concise results summary. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvases" }

### Catalogs

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | List catalogs in a workspace. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | Return multiple catalog items and their content. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | Return a single catalog item and its content. |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | create | Create a catalog. |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | delete | Delete a catalog. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | create | Create multiple fields in a catalog. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | delete | Delete a catalog field. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | create | Create multiple items in a catalog. Up to 50 items per request. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | update | Edit multiple existing items in a catalog. Up to 50 items per request. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | update | Replace multiple items in a catalog. Creates items if they don't exist. Up to 50 items per request. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | delete | Delete multiple items in a catalog. Up to 50 items per request. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | create | Create a selection in a catalog. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | delete | Delete a catalog selection. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalogs" }

### Custom attributes

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | read | Export custom attributes recorded for your app, in groups of 50, alphabetical. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Custom attributes" }

### Custom events

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | read | Export custom events recorded for your app, in groups of 50, alphabetical (cursor pagination). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | read | Export custom event names, in groups of 250, alphabetical (page pagination). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | read | Occurrences of a custom event over a designated time period. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Custom events" }

### CDI integrations

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | read | List existing Cloud Data Ingestion integrations, 10 per call. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | read | Past sync statuses for a given CDI integration, 10 per call. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | write | Trigger a sync for a given CDI integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI integrations" }

### KPI

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | read | Daily series of unique active users per date. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | Daily series of unique active users over a 30-day rolling window. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | Daily series of total new users per date. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | Daily series of total uninstalls per date. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Media library

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | create | Upload an asset to the Braze media library through external URL or base64 file content. Exactly one upload mode must be provided. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Media library" }

### Purchases

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | read | Paginated list of product IDs. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | read | Total number of purchases in your app over a time range. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | read | Total money spent in your app over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Purchases" }

### Segments

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | read | Export segments with name, Segment API identifier, and analytics-tracking flag. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | read | Retrieve relevant information on a segment by `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | read | Daily series of a segment's estimated size over time. |
| `get_segment_filters`<sup>*</sup> | N/A | read | Retrieve segment filter definitions. |
| `create_segment`<sup>*</sup> | N/A | create | Create a new segment. |
| `edit_segment`<sup>*</sup> | N/A | update | Edit an existing segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

<sup>*</sup> This tool is only available to customers participating in the segment APIs beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.
{: .reset-td-br-1 }

### Sends

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | read | Daily stats for a tracked `send_id` (API campaigns). Braze stores send analytics for 14 days after the send. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sends" }

### Sessions

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | read | Number of sessions for your app over a designated time period. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessions" }

### Templates

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | read | List available email templates in your Braze account. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | read | Get information for a specific email template. Drag-and-drop editor templates are not accepted. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | create | Create an email template on the Braze dashboard. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | update | Update an existing email template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Templates" }

### Content blocks

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | read | List existing content block information. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | Get information for an existing content block, optionally with campaign or Canvas inclusion data. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | Create a content block. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | update | Update a content block. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content blocks" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}
