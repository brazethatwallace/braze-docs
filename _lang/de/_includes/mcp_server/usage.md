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
![„Welche Braze-Funktionen stehen mir zur Verfügung?“ – diese Frage wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `list_functions` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#general-functions){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#general-functions){% endif %}.

### Details zu einer Canvas-ID abrufen {#get-details-about-a-canvas-id}

{% tabs %}
{% tab Claude %}
![„Details zu einer Canvas-ID abrufen“ wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![„Details zu einer Canvas-ID abrufen“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `get_canvas_details` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Meine aktuellen Canvases anzeigen {#show-me-my-recent-canvases}

{% tabs %}
{% tab Claude %}
![„Meine aktuellen Canvases anzeigen“ wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![„Meine aktuellen Canvases anzeigen“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `get_canvas_list` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#canvases){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#canvases){% endif %}.

### Ein E-Mail-Template erstellen {#create-an-email-template}

{% tabs %}
{% tab Cursor %}
![„Ein E-Mail-Template erstellen“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/create_an_email_template.png %})
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `create_email_template` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

### Einen Content-Block aktualisieren {#update-a-content-block}

{% tabs %}
{% tab Cursor %}
![„Einen Content-Block aktualisieren“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/update_a_content_block.png %})
{% endtab %}
{% endtabs %}

Weitere Informationen zur Funktion `update_content_block` finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#content-blocks){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#content-blocks){% endif %}.

{% multi_lang_include mcp_server/legal_disclaimer.md %}