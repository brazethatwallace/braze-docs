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
**Example prompt:** `What are my available Braze functions?`

**Example response:** Called `list_functions` and returned categories like Campaign, Canvas, Templates, and Content Blocks with sample functions such as `get_canvas_list` and `create_email_template`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`

**Example response:** Queried `list_functions`, confirmed available function groups, and listed examples including `get_canvas_details` and `update_content_block`.
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `list_functions` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Details zu einer Canvas-ID abrufen {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Used `get_canvas_details` and returned sample metadata (status, channel, created/updated time) for `YOUR-TEST-CANVAS-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response:** Returned Canvas and message details with dummy values like `YOUR-TEST-MESSAGE-ID-123` and `YOUR-TEST-SUBJECT-LINE`.
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `get_canvas_details` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Meine aktuellen Canvases anzeigen {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Called `get_canvas_list` and returned recent items such as `YOUR-TEST-CANVAS-ALPHA` with IDs like `YOUR-TEST-ID-123`.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `Show me my recent Canvases`

**Example response:** Listed recently edited Canvases with sample values for name, last edited time, ID, and tags.
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `get_canvas_list` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Ein E-Mail-Template erstellen {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Create an email template named "YOUR-TEST-TEMPLATE-NAME".`

**Example response:** Created a template via `create_email_template` and returned `YOUR-TEST-TEMPLATE-ID-123`.
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `create_email_template` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Einen Content-Block aktualisieren {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
**Example prompt:** `Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123".`

**Example response:** Updated the block with `update_content_block` and confirmed `YOUR-TEST-CONTENT-BLOCK-ID-123` moved to a new version.
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `update_content_block` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}