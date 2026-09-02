# Funktionen des Braze MCP-Servers {#braze-mcp-server-functions}

> Der Braze MCP-Server stellt Lese- und Schreibfunktionen bereit, die bestimmten Braze Representational State Transfer API-Endpunkten zugeordnet sind. Weitere Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
Der Braze MCP-Server enthält Tools, die nur für Kund:innen verfügbar sind, die an Beta-Programmen teilnehmen. Wenn Sie versuchen, auf ein Tool zuzugreifen, das Teil eines Beta-Programms ist, und Ihr Konto das Feature nicht aktiviert hat, erhalten Sie möglicherweise eine Fehlerantwort. Um an einem Beta-Programm teilzunehmen, wenden Sie sich an Ihren Account Manager:in.
{% endalert %}

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie den [Braze MCP-Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Verfügbare Braze-API-Funktionen {#available-braze-api-functions}

Ihr MCP-Client referenziert diese Tools, um mit dem Braze MCP-Server zu interagieren.

### Workspaces

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | read | Ermitteln Sie, welche Braze Workspaces das aktuelle OAuth-Zugriffstoken erreichen kann. Rufen Sie dieses Tool zuerst auf: Jede zurückgegebene Workspace-`id` ist die `app_group_id`, die alle anderen Tools benötigen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Workspaces" }

### Campaigns

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | read | Exportieren Sie eine Liste von Campaigns mit Name, Campaign-API-Bezeichner, API-Campaign-Flag und Tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | read | Rufen Sie relevante Informationen zu einer bestimmten Campaign anhand der `campaign_id` ab. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | read | Tägliche Reihe von Campaign-Statistiken über die Zeit (Sends, Öffnungen, Klicks, Konversionen nach Kanal). |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | create | Duplizieren Sie eine bestehende Campaign. |
| `create_campaign`<sup>*</sup> | N/A | create | Erstellen Sie eine neue Campaign. |
| `edit_campaign`<sup>*</sup> | N/A | Update or aktualisieren | Bearbeiten Sie eine bestehende Campaign. |
| `launch_campaign`<sup>*</sup> | N/A | Update or aktualisieren | Starten Sie eine Campaign. |
| `stop_campaign`<sup>*</sup> | N/A | Update or aktualisieren | Stoppen Sie eine laufende Campaign. |
| `archive_campaign`<sup>*</sup> | N/A | Update or aktualisieren | Archivieren Sie eine Campaign. |
| `unarchive_campaign`<sup>*</sup> | N/A | Update or aktualisieren | Heben Sie die Archivierung einer Campaign auf. |
| `get_campaign_draft`<sup>*</sup> | N/A | read | Rufen Sie Entwurfsdetails einer Campaign ab. |
| `get_campaign_live_details`<sup>*</sup> | N/A | read | Rufen Sie Live-Details einer Campaign ab. |
| `create_campaign_message`<sup>*</sup> | N/A | create | Erstellen Sie eine Nachricht innerhalb einer Campaign. |
| `update_campaign_message`<sup>*</sup> | N/A | Update or aktualisieren | Update or aktualisieren or aktualisieren Sie eine Campaign-Nachricht. |
| `delete_campaign_message`<sup>*</sup> | N/A | delete | Löschen Sie eine Campaign-Nachricht. |
| `create_campaign_message_variation`<sup>*</sup> | N/A | create | Erstellen Sie eine Nachrichtenvariante innerhalb einer Campaign. |
| `update_campaign_message_variation`<sup>*</sup> | N/A | Update or aktualisieren | Update or aktualisieren or aktualisieren Sie eine Campaign-Nachrichtenvariante. |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | delete | Löschen Sie eine Campaign-Nachrichtenvariante. |
| `update_campaign_distribution`<sup>*</sup> | N/A | Update or aktualisieren | Update or aktualisieren or aktualisieren Sie die Verteilungseinstellungen einer Campaign. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

<sup>*</sup> Dieses Tool steht nur Kund:innen zur Verfügung, die am Betaprogramm für Campaign-APIs teilnehmen. Wenn dieses Feature für Ihr Konto nicht aktiviert ist, erhalten Sie möglicherweise eine Fehlermeldung, wenn Sie versuchen, es zu verwenden. Um am Betaprogramm teilzunehmen, wenden Sie sich an Ihren Account Manager:in.
{: .reset-td-br-1 }

### Canvase

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | read | Exportieren Sie eine Liste von Canvase mit Name, Canvas-API-Bezeichner und Tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | read | Exportieren Sie Canvas-Metadaten: Name, Erstellungszeitpunkt, aktueller Status und mehr. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | read | Exportieren Sie Zeitreihendaten für ein Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | Exportieren Sie Zusammenfassungen von Canvas-Zeitreihendaten für eine kompakte Ergebnisübersicht. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvase" }

### Kataloge {#catalogs}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | Listen Sie Kataloge in einem Workspace auf. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | Geben Sie mehrere Katalogartikel und deren Inhalte zurück. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | Geben Sie einen einzelnen Katalogartikel und dessen Inhalt zurück. |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | create | Erstellen Sie einen Katalog. |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | delete | Löschen Sie einen Katalog. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | create | Erstellen Sie mehrere Felder in einem Katalog. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | delete | Löschen Sie ein Katalogfeld. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | create | Erstellen Sie mehrere Artikel in einem Katalog. Bis zu 50 Artikel pro Anfrage. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | Update or aktualisieren | Bearbeiten Sie mehrere bestehende Artikel in einem Katalog. Bis zu 50 Artikel pro Anfrage. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | Update or aktualisieren | Ersetzen Sie mehrere Artikel in einem Katalog. Erstellt Artikel, wenn sie nicht vorhanden sind. Bis zu 50 Artikel pro Anfrage. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | delete | Löschen Sie mehrere Artikel in einem Katalog. Bis zu 50 Artikel pro Anfrage. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | create | Erstellen Sie eine Auswahl in einem Katalog. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | delete | Löschen Sie eine Katalogauswahl. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kataloge" }

### Angepasste Attribute {#custom-attributes}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | read | Exportieren Sie angepasste Attribute, die für Ihre App aufgezeichnet wurden, in Gruppen von 50, alphabetisch sortiert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Angepasste Attribute" }

### Angepasste Events {#custom-events}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | read | Exportieren Sie angepasste Events, die für Ihre App aufgezeichnet wurden, in Gruppen von 50, alphabetisch sortiert (Cursor-Paginierung). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | read | Exportieren Sie Namen angepasster Events, in Gruppen von 250, alphabetisch sortiert (Seiten-Paginierung). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | read | Vorkommen eines angepassten Events über einen festgelegten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Angepasste Events" }

### CDI-Integrationen {#cdi-integrations}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | read | Listen Sie bestehende Cloud-Datenaufnahme-Integrationen auf, 10 pro Aufruf. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | read | Vergangene Synchronisierungsstatus für eine bestimmte CDI-Integration, 10 pro Aufruf. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | write | Lösen Sie eine Synchronisierung für eine bestimmte CDI-Integration aus. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI-Integrationen" }

### KPI or Leistungskennzahl or Leistungskennzahlen

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | read | Tägliche Reihe eindeutiger aktiver Nutzer:innen pro Datum. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | Tägliche Reihe eindeutiger aktiver Nutzer:innen über ein rollendes 30-Tage-Fenster. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | Tägliche Reihe der Gesamtzahl neuer Nutzer:innen pro Datum. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | Tägliche Reihe der Gesamtzahl an Deinstallationen pro Datum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI or Leistungskennzahl or Leistungskennzahlen" }

### Medienbibliothek {#media-library}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | create | Laden Sie ein Asset über eine externe URL oder base64-kodierten Dateiinhalt in die Braze-Medienbibliothek hoch. Es muss genau ein Upload-Modus angegeben werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Medienbibliothek" }

### Käufe {#purchases}

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | read | Paginierte Liste von Produkt-IDs. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | read | Gesamtanzahl der Käufe in Ihrer App über einen Zeitraum. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | read | Gesamtbetrag der Ausgaben in Ihrer App über einen Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Käufe" }

### Segments

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | read | Exportieren Sie Segmente mit Name, Segment-API-Bezeichner und Analytics-Tracking-Flag. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | read | Rufen Sie relevante Informationen zu einem Segment anhand der `segment_id` ab. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | read | Tägliche Reihe der geschätzten Größe eines Segments über die Zeit. |
| `get_segment_filters`<sup>*</sup> | N/A | read | Rufen Sie die Filterdefinitionen eines Segments ab. |
| `create_segment`<sup>*</sup> | N/A | create | Erstellen Sie ein neues Segment. |
| `edit_segment`<sup>*</sup> | N/A | Update or aktualisieren | Bearbeiten Sie ein bestehendes Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

<sup>*</sup> Dieses Tool steht nur Kund:innen zur Verfügung, die am Betaprogramm für Segment-APIs teilnehmen. Wenn dieses Feature für Ihr Konto nicht aktiviert ist, erhalten Sie möglicherweise eine Fehlermeldung, wenn Sie versuchen, es zu verwenden. Um am Betaprogramm teilzunehmen, wenden Sie sich an Ihren Account Manager:in.
{: .reset-td-br-1 }

### Sends

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | read | Tägliche Statistiken für eine getrackte `send_id` (API-Campaigns). Braze speichert Send-Analytics 14 Tage nach dem Versand. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sends" }

### Sessions

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | read | Anzahl der Sessions für Ihre App über einen festgelegten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessions" }

### Templates

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | read | Listen Sie verfügbare E-Mail-Templates in Ihrem Braze-Konto auf. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | read | Rufen Sie Informationen zu einem bestimmten E-Mail-Template ab. Templates des Drag-and-Drop-Editors werden nicht akzeptiert. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | create | Erstellen Sie ein E-Mail-Template im Braze-Dashboard. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Update or aktualisieren | Update or aktualisieren or aktualisieren Sie ein bestehendes E-Mail-Template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Templates" }

### Content Blocks

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | read | Listen Sie bestehende Content-Block-Informationen auf. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | Rufen Sie Informationen zu einem bestehenden Content-Block ab, optional mit Campaign- oder Canvas-Einbindungsdaten. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | Erstellen Sie einen Content-Block. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | Update or aktualisieren | Update or aktualisieren or aktualisieren Sie einen Content-Block. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

### Operator

| Tool | API-Endpunkt | Zugriff | Beschreibung |
| --- | --- | --- | --- |
| `send_operator_prompt` | N/A | Update or aktualisieren | Senden Sie einen Prompt in natürlicher Sprache an den BrazeAI Operator. Übermittelt einen Hintergrundjob und gibt eine job_id zurück. |
| `get_operator_result` | N/A | read | Fragen Sie das Ergebnis eines übermittelten Operator-Jobs anhand seiner job_id ab. |
| `cancel_operator_job` | N/A | Update or aktualisieren | Brechen Sie einen laufenden Operator-Job ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Operator" }

{% alert important %}
Diese Tools stehen nur Kund:innen zur Verfügung, die am Operator-Betaprogramm teilnehmen. Wenn dieses Feature für Ihr Konto nicht aktiviert ist, erhalten Sie möglicherweise eine Fehlermeldung, wenn Sie versuchen, es zu verwenden. Um am Betaprogramm teilzunehmen, wenden Sie sich an Ihren Account Manager:in.
{% endalert %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}