# Funktionen des Braze MCP-Servers {#braze-mcp-server-functions}

> Der Braze MCP-Server stellt Lese- und Schreibfunktionen bereit, die bestimmten Braze REST API-Endpunkten zugeordnet sind. Weitere Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie den [Braze MCP-Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Verfügbare Braze-API-Funktionen {#available-braze-api-functions}

Ihr MCP-Client referenziert diese Tools, um mit dem Braze MCP-Server zu interagieren.

### Workspaces

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | Lesen | Ermitteln Sie, welche Braze-Workspaces das aktuelle OAuth-Zugriffstoken erreichen kann. Rufen Sie dies zuerst auf: Jede zurückgegebene Workspace-`id` ist die `app_group_id`, die jedes andere Tool benötigt. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Workspaces" }

### Campaigns

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Lesen | Exportieren Sie eine Liste von Campaigns mit Name, Campaign-API-Bezeichner, API-Campaign-Flag und Tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Lesen | Rufen Sie relevante Informationen zu einer bestimmten Campaign anhand der `campaign_id` ab. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Lesen | Tägliche Zeitreihe der Campaign-Statistiken (Sends, Öffnungen, Klicks, Konversionen nach Kanal). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

### Canvases

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Lesen | Exportieren Sie eine Liste von Canvases mit Name, Canvas-API-Bezeichner und Tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Lesen | Exportieren Sie Canvas-Metadaten: Name, Erstellungszeitpunkt, aktueller Status und mehr. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Lesen | Exportieren Sie Zeitreihendaten für ein Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Lesen | Exportieren Sie aggregierte Canvas-Zeitreihendaten für eine kompakte Ergebniszusammenfassung. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvases" }

### Kataloge {#catalogs}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Lesen | Kataloge in einem Workspace auflisten. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Lesen | Mehrere Katalogartikel und deren Inhalt zurückgeben. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Lesen | Einen einzelnen Katalogartikel und dessen Inhalt zurückgeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kataloge" }

### Angepasste Attribute {#custom-attributes}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | Lesen | Exportieren Sie angepasste Attribute, die für Ihre App aufgezeichnet wurden, in Gruppen von 50, alphabetisch sortiert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Angepasste Attribute" }

### Angepasste Events {#custom-events}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | Lesen | Exportieren Sie angepasste Events, die für Ihre App aufgezeichnet wurden, in Gruppen von 50, alphabetisch sortiert (Cursor-Paginierung). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Lesen | Exportieren Sie Namen angepasster Events, in Gruppen von 250, alphabetisch sortiert (Seiten-Paginierung). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Lesen | Vorkommen eines angepassten Events über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Angepasste Events" }

### CDI-Integrationen {#cdi-integrations}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | Lesen | Vorhandene Cloud-Datenaufnahme-Integrationen auflisten, 10 pro Aufruf. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | Lesen | Vergangene Synchronisierungsstatus für eine bestimmte CDI-Integration, 10 pro Aufruf. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI-Integrationen" }

### KPI

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Lesen | Tägliche Zeitreihe der eindeutigen aktiven Nutzer:innen pro Tag. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Lesen | Tägliche Zeitreihe der eindeutigen aktiven Nutzer:innen über ein rollendes 30-Tage-Fenster. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Lesen | Tägliche Zeitreihe der neuen Nutzer:innen insgesamt pro Tag. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Lesen | Tägliche Zeitreihe der Deinstallationen insgesamt pro Tag. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Medienbibliothek {#media-library}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | Erstellen | Laden Sie ein Asset über eine externe URL oder base64-kodierten Dateiinhalt in die Braze-Medienbibliothek hoch. Es muss genau ein Upload-Modus angegeben werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Medienbibliothek" }

### Käufe {#purchases}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Lesen | Paginierte Liste von Produkt-IDs. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Lesen | Gesamtzahl der Käufe in Ihrer App über einen Zeitraum. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Lesen | Gesamter Umsatz in Ihrer App über einen Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Käufe" }

### Segments

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Lesen | Exportieren Sie Segmente mit Name, Segment-API-Bezeichner und Analytics-Tracking-Flag. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Lesen | Rufen Sie relevante Informationen zu einem Segment anhand der `segment_id` ab. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Lesen | Tägliche Zeitreihe der geschätzten Größe eines Segments über die Zeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

### Sends

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Lesen | Tägliche Statistiken für eine getrackte `send_id` (API-Campaigns). Braze speichert Send-Analytics 14 Tage nach dem Versand. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sends" }

### Sessions

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Lesen | Anzahl der Sessions für Ihre App über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessions" }

### Abo-Gruppen {#subscription-groups}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Lesen | Abo-Status einer Nutzerin oder eines Nutzers in einer Abo-Gruppe. |
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Lesen | Abo-Gruppen einer Nutzerin oder eines Nutzers auflisten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abo-Gruppen" }

### Templates

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Lesen | Verfügbare E-Mail-Templates in Ihrem Braze-Konto auflisten. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Lesen | Informationen zu einem bestimmten E-Mail-Template abrufen. Templates aus dem Drag-and-Drop-Editor werden nicht akzeptiert. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | Erstellen | Ein E-Mail-Template im Braze-Dashboard erstellen. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Aktualisieren | Ein vorhandenes E-Mail-Template aktualisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Templates" }

### Content Blocks

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Lesen | Informationen zu vorhandenen Content Blocks auflisten. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Lesen | Informationen zu einem vorhandenen Content-Block abrufen, optional mit Daten zur Verwendung in Campaigns oder Canvases. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | Erstellen | Einen Content-Block erstellen. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | Aktualisieren | Einen Content-Block aktualisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}