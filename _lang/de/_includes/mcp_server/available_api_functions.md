# Funktionen des Braze MCP-Servers {#braze-mcp-server-functions}

> Der Braze MCP-Server stellt eine Reihe von API-Funktionen bereit, die bestimmten Braze REST API-Endpunkten zugeordnet sind. MCP-Clients wie Claude und Cursor können diese Funktionen aufrufen, um Daten ohne PII abzurufen und – mit den entsprechenden Berechtigungen – Schreibaktionen ohne PII durchzuführen. Weitere allgemeine Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie [den Braze MCP-Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Verfügbare Braze-API-Funktionen {#available-braze-api-functions}

Ihr MCP-Client referenziert die folgenden API-Funktionen, um mit dem Braze MCP-Server zu interagieren.

### Allgemeine Funktionen {#general-functions}

Diese Funktionen helfen Ihrem MCP-Client, die verfügbaren Braze-API-Funktionen zu erkennen und auszuführen.

| Funktion | Beschreibung |
|----------|-------------|
| `list_functions` | Listet alle verfügbaren Braze-API-Funktionen mit ihren Beschreibungen und Parametern auf. |
| `call_function` | Ruft eine bestimmte schreibgeschützte Braze-API-Funktion mit den angegebenen Parametern auf. |
| `call_write_function` | Ruft eine bestimmte schreibfähige Braze-API-Funktion mit den angegebenen Parametern auf. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General functions" }

### Campaigns

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Exportiert eine Liste der Campaigns mit Metadaten. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Ruft detaillierte Informationen zu bestimmten Campaigns ab. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Ruft Zeitreihen-Analytics-Daten für Campaigns ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campaigns" }

### Canvases

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | Exportiert eine Liste der Canvases mit Metadaten. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Ruft detaillierte Informationen zu bestimmten Canvases ab. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Ruft zusammenfassende Analytics zur Canvas-Performance ab. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Ruft Zeitreihen-Analytics-Daten für Canvases ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvases" }

### Kataloge {#catalogs}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Gibt eine Liste der Kataloge in einem Workspace zurück. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Gibt mehrere Katalogartikel und deren Inhalt mit Unterstützung für Paginierung zurück. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Gibt einen bestimmten Katalogartikel und dessen Inhalt anhand der ID zurück. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalogs" }

### Cloud-Datenaufnahme {#cloud-data-ingestion}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | Gibt eine Liste der vorhandenen CDI-Integrationen zurück. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | Gibt die vergangenen Synchronisierungsstatus für eine bestimmte CDI-Integration zurück. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cloud Data Ingestion" }

### Content Blocks

Die Funktionen `create_content_block` und `update_content_block` sind Schreibfunktionen. Ihr MCP-Client muss sie mit `call_write_function` aufrufen, und Ihr API-Schlüssel muss die entsprechende Berechtigung `content_blocks.create` bzw. `content_blocks.update` besitzen.

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Listet Ihre verfügbaren Content Blocks auf. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Ruft Informationen zu Ihren Content Blocks ab. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Erstellt einen Content-Block. Erfordert `name` und `content`. Optionale Felder sind `description`, `state` (muss `active` oder `draft` sein) und `tags`. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Aktualisiert einen vorhandenen Content-Block. Erfordert `content_block_id` und mindestens ein aktualisierbares Feld: `name`, `content`, `description`, `state` (muss `active` oder `draft` sein) oder `tags`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Blocks" }

### Angepasste Attribute {#custom-attributes}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | Exportiert die für Ihre App gespeicherten angepassten Attribute. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom Attributes" }

### Events

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Exportiert eine Liste der für Ihre App aufgezeichneten angepassten Events. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Ruft Zeitreihendaten für angepasste Events ab. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | Ruft detaillierte Event-Daten mit Unterstützung für Paginierung ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Events" }

### KPIs

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Tägliche Serie der Anzahl neuer Nutzer:innen. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | Zeitreihendaten zu den täglich aktiven Nutzer:innen. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Zeitreihendaten zu den monatlich aktiven Nutzer:innen. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Zeitreihendaten zur Deinstallation von Apps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="KPIs" }

### Medienbibliothek {#media-library}

Die Funktion `create_media_library_asset` ist eine Schreibfunktion. Ihr MCP-Client muss sie mit `call_write_function` aufrufen, und Ihr API-Schlüssel muss die Berechtigung `media_library.create` besitzen.

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | Lädt ein Asset in Ihre Braze-Medienbibliothek hoch. Sie können entweder eine öffentlich zugängliche URL (`asset_url`) oder eine Base64-kodierte Datei (`asset_file_base64`) angeben, aber nicht beides. Bilder haben ein Größenlimit von 5 MB. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Media Library" }

### Nachrichten {#messages}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Listet bevorstehende geplante Campaigns und Canvases auf. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages" }

### Präferenzzentren {#preference-centers}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Listet Ihre verfügbaren Präferenzzentren auf. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | Zeigt Details für ein bestimmtes Präferenzzentrum an, einschließlich HTML-Inhalten und Optionen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preference Centers" }

### Käufe {#purchases}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Exportiert eine paginierte Liste von Produkt-IDs. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Zeitreihendaten zur Umsatzanalyse. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Zeitreihendaten zur Kaufmenge. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Purchases" }

### Segmente {#segments}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Exportiert eine Liste der Segmente mit Analytics-Tracking-Status. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Zeitreihen-Analytics-Daten für Segmente. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Detaillierte Informationen zu bestimmten Segmenten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segments" }

### Sendungen {#sends}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Tägliche Analytics für nachverfolgte Campaign-Sendungen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sends" }

### Sitzungen {#sessions}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Zeitreihendaten für die Anzahl der App-Sitzungen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sessions" }

### SDK-Authentifizierungsschlüssel {#sdk-authentication-keys}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | Listet alle SDK-Authentifizierungsschlüssel für Ihre App auf. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SDK Authentication Keys" }

### Abo {#subscription}

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Listet die Abo-Gruppen einer bestimmten Nutzerin bzw. eines bestimmten Nutzers auf und ruft sie ab. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Ruft den Abo-Status einer Nutzerin bzw. eines Nutzers in einer Abo-Gruppe ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscription" }

### Templates

Die Funktionen `create_email_template` und `update_email_template` sind Schreibfunktionen. Ihr MCP-Client muss sie mit `call_write_function` aufrufen, und Ihr API-Schlüssel muss die entsprechende Berechtigung `templates.email.create` bzw. `templates.email.update` besitzen.

| Funktion | Endpunkt | Beschreibung |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Listet Ihre verfügbaren E-Mail-Templates auf. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Ruft Informationen zu Ihren E-Mail-Templates ab. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Erstellt ein E-Mail-Template. Erfordert `template_name`, `subject` und `body`. Optionale Felder sind `plaintext_body`, `preheader`, `tags` und `should_inline_css`. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Aktualisiert ein vorhandenes E-Mail-Template. Erfordert `email_template_id` und mindestens ein aktualisierbares Feld: `template_name`, `subject`, `body`, `plaintext_body`, `preheader`, `tags` oder `should_inline_css`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Templates" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}