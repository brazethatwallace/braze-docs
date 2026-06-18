# Einrichtung des Braze MCP-Servers {#setting-up-the-braze-mcp-server}

> Erfahren Sie, wie Sie den Braze MCP-Server einrichten, um mit Ihren Braze-Daten mithilfe von Tools für natürliche Sprache wie Claude und Cursor zu interagieren. Weitere allgemeine Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Braze-API-Schlüssel | Ein Braze-API-Schlüssel mit den erforderlichen Berechtigungen. Sie erstellen einen neuen Schlüssel, wenn Sie [Ihren Braze MCP-Server einrichten](#create-api-key). |
| MCP-Client | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) und [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) werden offiziell unterstützt. Sie benötigen ein Konto für einen dieser Clients, um den Braze MCP-Server nutzen zu können. |
| Terminal | Eine Terminal-App, mit der Sie Befehle ausführen und Tools installieren können. Verwenden Sie Ihre bevorzugte Terminal-App oder die auf Ihrem Computer vorinstallierte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichtung des Braze MCP-Servers

### 1. Schritt: `uv` installieren {#step-1-install-uv}

Installieren Sie zunächst `uv`&#8212;ein [Befehlszeilentool von Astral](https://docs.astral.sh/uv/getting-started/installation/) für die Abhängigkeitsverwaltung und die Handhabung von Python-Paketen.

{% tabs local %}
{% tab MacOS and Linux %}
Öffnen Sie Ihre Terminal-Anwendung, fügen Sie den folgenden Befehl ein und drücken Sie <kbd>Enter</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Die Ausgabe sieht in etwa wie folgt aus:

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Öffnen Sie Windows PowerShell, fügen Sie den folgenden Befehl ein und drücken Sie <kbd>Enter</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Die Ausgabe sieht in etwa wie folgt aus:

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### 2. Schritt: API-Schlüssel erstellen {#create-api-key}

Der Braze MCP-Server umfasst sowohl Lese- als auch Schreib-Endpunkte. Sie geben keine Daten aus Braze-Nutzerprofilen zurück. Schreib-Endpunkte ermöglichen es Agenten, Inhalte in Ihrem Workspace zu erstellen oder zu aktualisieren.

So erstellen Sie Ihren API-Schlüssel:

1. Navigieren Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Erstellen Sie einen neuen Schlüssel.
3. Weisen Sie Ihrem Schlüssel einige oder alle der folgenden Berechtigungen zu.

{% alert important %}
Weisen Sie nur die Berechtigungen zu, die Ihr Agent verwenden soll. Um zu verhindern, dass Ihr Agent Änderungen in Braze vornimmt, lassen Sie alle Schreibberechtigungen weg, wenn Sie Ihren API-Schlüssel erstellen.
{% endalert %}

{% details Liste der unterstützten Berechtigungen %}
#### Campaigns

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

#### Canvas

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas" }

#### Kataloge {#catalogs}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalogs" }

#### Cloud-Datenaufnahme {#cloud-data-ingestion}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cloud Data Ingestion" }

#### Content Blocks

Die Berechtigungen `content_blocks.create` und `content_blocks.update` sind Schreibberechtigungen. Fügen Sie sie nur hinzu, wenn Ihr Agent Content Blocks in Ihrem Workspace erstellen oder aktualisieren soll.

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | `content_blocks.info` |
| [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | `content_blocks.create` |
| [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | `content_blocks.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

#### Angepasste Attribute {#custom-attributes}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom Attributes" }

#### Ereignisse {#events}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Events" }

#### KPIs

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KPIs" }

#### Medienbibliothek {#media-library}

Die Berechtigung `media_library.create` ist eine Schreibberechtigung. Fügen Sie sie nur hinzu, wenn Ihr Agent Assets in Ihre Medienbibliothek hochladen soll.

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | `media_library.create` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Media Library" }

#### Nachrichten {#messages}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

#### Präferenzzentrum {#preference-center}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preference Center" }

#### Käufe {#purchases}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Purchases" }

#### Segments

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segments" }

#### Sendungen {#sends}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sends" }

#### Sitzungen {#sessions}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sessions" }

#### SDK-Authentifizierungsschlüssel {#sdk-authentication-keys}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDK Authentication Keys" }

#### Abo {#subscription}

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription" }

#### Templates

Die Berechtigungen `templates.email.create` und `templates.email.update` sind Schreibberechtigungen. Fügen Sie sie nur hinzu, wenn Ihr Agent E-Mail-Templates in Ihrem Workspace erstellen oder aktualisieren soll.

| Endpunkt | Erforderliche Berechtigung |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | `templates.email.info` |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | `templates.email.create` |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | `templates.email.update` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Templates" }
{% enddetails %}

{% alert warning %}
Verwenden Sie keinen bereits vorhandenen API-Schlüssel wieder. Erstellen Sie einen speziell für Ihren MCP-Client. Weisen Sie nur die Berechtigungen zu, die Ihr Agent benötigt. Agenten versuchen möglicherweise, jede Berechtigung zu nutzen, die Sie gewähren. Lassen Sie daher alle Schreibberechtigungen weg, wenn Ihr Agent keine Änderungen in Braze vornehmen soll.
{% endalert %}

### 3. Schritt: Bezeichner und Endpunkt abrufen {#step-3-get-your-identifier-and-endpoint}

Wenn Sie Ihren MCP-Client konfigurieren, benötigen Sie den Bezeichner Ihres API-Schlüssels und den REST-Endpunkt Ihres Workspaces. Um diese Informationen abzurufen, kehren Sie zur Seite **API-Schlüssel** im Dashboard zurück&#8212;lassen Sie diese Seite geöffnet, damit Sie im [nächsten Schritt](#configure-client) darauf zurückgreifen können.

![Die Seite „API-Schlüssel“ in Braze mit einem neu erstellten API-Schlüssel und dem REST-Endpunkt der Nutzer:innen.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### 4. Schritt: MCP-Client konfigurieren {#configure-client}

Konfigurieren Sie Ihren MCP-Client mithilfe der bereitgestellten Konfigurationsdatei.

{% tabs %}
{% tab Claude %}
Richten Sie Ihren MCP-Server mithilfe des [Claude Desktop](https://claude.ai/download)-Konnektor-Verzeichnisses ein.

1. Gehen Sie in Claude Desktop zu **Settings** > **Connectors** > **Browse Connectors** > **Desktop Extensions** > **Braze MCP Server** > **Install**.
2. Geben Sie Ihren API-Schlüssel und Ihre Basis-URL ein.
3. Speichern Sie die Konfiguration und starten Sie Claude Desktop neu.

{% endtab %}

{% tab Cursor %}
Gehen Sie in [Cursor](https://cursor.com/) zu **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP** und fügen Sie das folgende Snippet hinzu:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

Ersetzen Sie `key-identifier` und `rest-endpoint` durch die entsprechenden Werte von der Seite **API-Schlüssel** in Braze. Ihre Konfiguration sollte in etwa wie folgt aussehen:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Wenn Sie fertig sind, speichern Sie die Konfiguration und starten Sie Cursor neu.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI liest Nutzer:innen-Einstellungen aus `~/.gemini/settings.json`. Falls diese Datei nicht vorhanden ist, können Sie sie erstellen, indem Sie Folgendes in Ihrem Terminal ausführen:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Ersetzen Sie als Nächstes `yourname` durch den genauen String vor `@BZXXXXXXXX` in Ihrer Terminal-Eingabeaufforderung. Ersetzen Sie dann `key-identifier` und `rest-endpoint` durch die entsprechenden Werte von der Seite **API-Schlüssel** in Braze.

Ihre Konfiguration sollte in etwa wie folgt aussehen:

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Wenn Sie fertig sind, speichern Sie die Konfiguration und starten Sie Gemini CLI neu. Führen Sie anschließend in Gemini die folgenden Befehle aus, um zu überprüfen, ob der Braze MCP-Server aufgeführt ist und die Tools und das Schema zur Verwendung verfügbar sind:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Sie sollten den `braze`-Server mit den verfügbaren Tools und Schemata aufgelistet sehen.

{% endtab %}
{% endtabs %}

### 5. Schritt: Test-Prompt senden {#step-5-send-a-test-prompt}

Nachdem Sie den Braze MCP-Server eingerichtet haben, senden Sie einen Test-Prompt an Ihren MCP-Client. Weitere Beispiele und Best Practices finden Sie unter [Verwendung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![„Welche Braze-Funktionen stehen mir zur Verfügung?“ – diese Frage wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Gemini CLI gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Fehlerbehebung {#troubleshooting}

### Terminalfehler {#terminal-errors}

#### `uvx`-Befehl nicht gefunden {#uvx-command-not-found}

Wenn Sie die Fehlermeldung erhalten, dass der `uvx`-Befehl nicht gefunden wurde, installieren Sie `uv` erneut und starten Sie Ihr Terminal neu.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT`-Fehler {#spawn-uvx-enoent-error}

Wenn Sie `spawn uvx ENOENT`-Fehler erhalten, müssen Sie möglicherweise den Dateipfad in der Konfigurationsdatei Ihres Clients aktualisieren. Öffnen Sie zunächst Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
which uvx
```

Der Befehl sollte eine Nachricht ähnlich der folgenden zurückgeben:

```bash
/Users/alex-lee/.local/bin/uvx
```

Kopieren Sie die Nachricht in Ihre Zwischenablage und öffnen Sie [die Konfigurationsdatei Ihres Clients](#configure-client). Ersetzen Sie `"command": "uvx"` durch den kopierten Pfad und starten Sie anschließend Ihren Client neu. Zum Beispiel:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Paketinstallation schlägt fehl {#package-installation-fails}

Wenn die Paketinstallation fehlschlägt, versuchen Sie stattdessen, eine bestimmte Python-Version zu installieren.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Client-Konfiguration {#client-configuration}

#### „Diese Erweiterung ist nicht mit Ihrem Gerät kompatibel“ {#this-extension-is-not-compatible-with-your-device}

Wenn dieser Fehler bei der Installation der Braze MCP-Server-Erweiterung angezeigt wird, kann dies auf Folgendes hinweisen:

- **Ihr Gerät erfüllt die Anforderungen nicht**: Einige MCP-Server-Erweiterungen erfordern bestimmte Betriebssystemversionen oder Hardware.
- **Fehlende Entwicklertools (nur macOS)**: Unter macOS benötigt die Installation der Erweiterung Befehlszeilen-Entwicklertools, um Python-Befehle auszuführen. Wenn diese Tools nicht installiert sind, schlägt die Installation mit diesem Fehler fehl.

Um die Befehlszeilen-Entwicklertools unter macOS zu installieren, führen Sie Folgendes in Ihrem Terminal aus:

```bash
xcode-select --install
```

Starten Sie nach Abschluss der Installation Ihren MCP-Client neu und versuchen Sie erneut, die Erweiterung zu installieren.

#### MCP-Client kann den Braze-Server nicht finden {#mcp-client-cant-find-the-braze-server}

1. Überprüfen Sie, ob die Syntax Ihrer MCP-Client-Konfiguration korrekt ist.
2. Starten Sie Ihren MCP-Client nach Konfigurationsänderungen neu.
3. Überprüfen Sie, ob `uvx` in Ihrem System-`PATH` enthalten ist.

#### Authentifizierungsfehler {#authentication-errors}

1. Überprüfen Sie, ob Ihr `BRAZE_API_KEY` korrekt und aktiv ist.
2. Stellen Sie sicher, dass Ihre `BRAZE_BASE_URL` mit Ihrer Braze-Instanz übereinstimmt.
3. Überprüfen Sie, ob Ihr API-Schlüssel über die [erforderlichen Berechtigungen](#create-api-key) verfügt.

#### Verbindungs-Timeouts oder Netzwerkfehler {#connection-timeouts-or-network-errors}

1. Überprüfen Sie, ob Ihre `BRAZE_BASE_URL` für Ihre Instanz korrekt ist.
2. Überprüfen Sie Ihre Netzwerkverbindung und Firewall-Einstellungen.
3. Stellen Sie sicher, dass Sie HTTPS in Ihrer Basis-URL verwenden.

{% multi_lang_include mcp_server/legal_disclaimer.md %}