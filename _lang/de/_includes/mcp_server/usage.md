# Verwendung des Braze MCP-Servers {#using-the-braze-mcp-server}

> Erfahren Sie, wie Sie mit Ihren Braze-Daten mithilfe von Tools für natürliche Sprache wie Claude und Cursor interagieren können. Weitere allgemeine Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie [den Braze MCP-Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Best Practices

Wenn Sie den Braze MCP-Server über Tools für natürliche Sprache wie Claude und Cursor verwenden, beachten Sie bitte die folgenden Hinweise, um optimale Ergebnisse zu erzielen:

- LLMs können Fehler machen, daher sollten Sie ihre Antworten stets überprüfen.
- Für die Datenanalyse ist es wichtig, den benötigten Zeitbereich genau zu definieren. Kürzere Zeiträume liefern häufig genauere Ergebnisse.
- Verwenden Sie die genaue [Braze-Terminologie](https://www.braze.com/resources/articles/glossary), damit Ihr LLM die richtige Funktion aufruft.
- Sollten die Ergebnisse unvollständig erscheinen, bitten Sie Ihr LLM, fortzufahren oder tiefer zu recherchieren.
- Probieren Sie kreative Prompts aus! Je nach Ihrem MCP-Client können Sie möglicherweise CSV-Dateien oder andere nützliche Dateien exportieren.

## Anwendungsbeispiele {#usage-examples}

Nach [der Einrichtung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} können Sie über Tools wie Claude oder Cursor in natürlicher Sprache mit Braze interagieren. Hier sind einige Beispiele für den Einstieg:

### Welche Braze-Funktionen stehen mir zur Verfügung? {#what-are-my-available-braze-functions}

{% tabs %}
{% tab Claude %}
**Beispiel-Prompt**

`What are my available Braze functions?`

**Beispielantwort**

Ich habe den Braze MCP-Server mit `list_functions` abgefragt und 38 verfügbare API-Funktionen gefunden.

Hier sind einige Beispiele nach Kategorie:

- **Campaign-Analytics und -Verwaltung**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **Canvas-Analytics und -Verwaltung**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **Templates**
  - `create_email_template`
- **Content Blocks**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`
{% endtab %}

{% tab Cursor %}
**Beispiel-Prompt**

`What are my available Braze functions?`

**Beispielantwort**

Ich überprüfe Ihre verfügbaren Funktionen über den Braze MCP-Server.

- `list_functions` aufgerufen

Basierend auf dem Ergebnis stehen Ihnen 38 Braze-API-Funktionen zur Verfügung, die in Kategorien wie die folgenden unterteilt sind:

- Campaign-Analytics und -Verwaltung
- Canvas-Analytics und -Verwaltung
- Templates
- Content Blocks

Beispielfunktionen:

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `list_functions` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Details zu einer Canvas-ID abrufen {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Beispiel-Prompt**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Beispielantwort**

Ich habe die Details für `YOUR-TEST-CANVAS-ID-123` mit `get_canvas_details` abgerufen.

- **Canvas-Name:** `YOUR-TEST-CANVAS-NAME`
- **ID:** `YOUR-TEST-CANVAS-ID-123`
- **Status:** Entwurf (nicht aktiviert)
- **Erstellt am:** 15. Jan. 2026, 10:30 Uhr UTC
- **Zuletzt aktualisiert:** 16. Jan. 2026, 14:45 Uhr UTC
- **Zeitplantyp:** Zeitbasiert
- **Primärer Kanal:** E-Mail

Details zur E-Mail-Nachricht:

- **Betreff:** `YOUR-TEST-SUBJECT-LINE`
- **Von:** `YOUR-TEST-SENDER@example.com`
- **Nachrichten-ID:** `YOUR-TEST-MESSAGE-ID-123`
{% endtab %}

{% tab Cursor %}
**Beispiel-Prompt**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Beispielantwort**

Ich habe diesen Canvas mit `get_canvas_details` abgerufen:

- **Canvas-ID:** `YOUR-TEST-CANVAS-ID-123`
- **Canvas-Name:** `YOUR-TEST-CANVAS-NAME`
- **Status:** Entwurf
- **Kanal:** E-Mail
- **Nachrichten-ID:** `YOUR-TEST-MESSAGE-ID-123`

Zusammenfassung des E-Mail-Inhalts:

1. Header-Bereich mit Markenbild
2. Hauptüberschrift
3. Hero-Bereich mit CTA-Button
4. Feature-Bereich mit ergänzendem Inhalt
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `get_canvas_details` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Meine aktuellen Canvases anzeigen {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Beispiel-Prompt**

`Show me my recent Canvases`

**Beispielantwort**

Ich habe Ihre verfügbaren Tools mit `list_functions` überprüft und dann `get_canvas_list` verwendet, um Ihre zuletzt bearbeiteten Canvases abzurufen.

Neueste Canvases:

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID: `YOUR-TEST-ID-123`
   - Zuletzt bearbeitet: 16. Jan. 2026, 14:45 Uhr UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID: `YOUR-TEST-ID-456`
   - Zuletzt bearbeitet: 15. Jan. 2026, 11:10 Uhr UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID: `YOUR-TEST-ID-789`
   - Zuletzt bearbeitet: 14. Jan. 2026, 20:25 Uhr UTC
{% endtab %}

{% tab Cursor %}
**Beispiel-Prompt**

`Show me my recent Canvases`

**Beispielantwort**

Ich rufe Ihre aktuelle Canvas-Liste vom Braze MCP-Server ab.

- `list_functions` aufgerufen
- `get_canvas_list` aufgerufen

Aktuelle Canvases (sortiert nach zuletzt bearbeitet):

- **Canvas-Name:** `YOUR-TEST-CANVAS-ALPHA`
  - **Zuletzt bearbeitet:** 16. Jan. 2026, 14:45 Uhr UTC
  - **Canvas-ID:** `YOUR-TEST-ID-123`
  - **Tags:** `lifecycle`, `email`
- **Canvas-Name:** `YOUR-TEST-CANVAS-BETA`
  - **Zuletzt bearbeitet:** 15. Jan. 2026, 11:10 Uhr UTC
  - **Canvas-ID:** `YOUR-TEST-ID-456`
  - **Tags:** `promo`
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `get_canvas_list` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Ein E-Mail-Template erstellen {#create-an-email-template}

{% tabs %}
{% tab Claude %}
**Beispiel-Prompt**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Beispielantwort**

Ich habe Ihr Template mit `create_email_template` erstellt.

- **Template-Name:** `YOUR-TEST-TEMPLATE-NAME`
- **Template-ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **Betreffzeile:** `YOUR-TEST-SUBJECT-LINE`
- **Preheader:** `YOUR-TEST-PREHEADER`
- **Erstellt am:** 16. Jan. 2026, 15:10 Uhr UTC

Sie können `YOUR-TEST-TEMPLATE-ID-123` jetzt beim Erstellen oder Aktualisieren von Campaigns und Canvases referenzieren.
{% endtab %}

{% tab Cursor %}
**Beispiel-Prompt**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Beispielantwort**

Ich habe `create_email_template` verwendet und ein neues Template erfolgreich erstellt.

- **Template-ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **Template-Name:** `YOUR-TEST-TEMPLATE-NAME`
- **Betreff:** `YOUR-TEST-SUBJECT-LINE`
- **Beschreibung:** `Onboarding lifecycle template`

Wenn Sie möchten, kann ich auch einen HTML-Startkörper und einen Nur-Text-Fallback für dieses Template generieren.
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `create_email_template` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Einen Content-Block aktualisieren {#update-a-content-block}

{% tabs %}
{% tab Claude %}
**Beispiel-Prompt**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Beispielantwort**

Ich habe Ihren Content-Block mit `update_content_block` aktualisiert.

- **Content-Block-ID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Name:** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **Status:** Aktualisiert
- **Aktualisiert am:** 16. Jan. 2026, 15:25 Uhr UTC

Vorschau:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}

{% tab Cursor %}
**Beispiel-Prompt**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Beispielantwort**

Ich habe `update_content_block` ausgeführt und die Aktualisierung bestätigt.

- **Content-Block-ID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Vorherige Version:** `v1`
- **Aktuelle Version:** `v2`
- **Zuletzt aktualisiert:** 16. Jan. 2026, 15:25 Uhr UTC

Aktualisierte Inhaltsvorschau:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `update_content_block` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}