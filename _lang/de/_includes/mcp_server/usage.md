# Verwendung des Braze MCP-Servers {#using-the-braze-mcp-server}

> Erfahren Sie, wie Sie nach der Verbindung mit dem Remote-Braze-MCP-Server über natürliche Sprache mit Ihren Braze-Daten interagieren können. Weitere Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie den [Braze MCP-Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Best Practices

Wenn Sie den Braze MCP-Server über Tools für natürliche Sprache verwenden, beachten Sie die folgenden Tipps:

- Bestätigen Sie den Workspace in Ihrem Prompt, insbesondere wenn Sie Zugriff auf mehrere Workspaces haben.
- Geben Sie bei Analytics-Anfragen genaue Datumsbereiche und Metriken an.
- Bitten Sie den Agenten zu bestätigen, welche Tools er bei der Validierung der Ergebnisse verwendet hat.
- Gleichen Sie Empfehlungen mit hoher Auswirkung mit den Quelldaten im Braze-Dashboard ab.

## Anwendungsbeispiele {#usage-examples}

Nach der [Einrichtung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} können Sie über natürliche Sprache mit Braze interagieren. Hier finden Sie Beispiele für den Einstieg.

### Auf welche Workspaces habe ich Zugriff? {#which-workspaces-can-i-access}

{% tabs %}
{% tab Beispiel-Prompt %}

`Show my available Braze workspaces and tell me which one to use for production campaign analytics.`
{% endtab %}
{% tab Beispielantwort %}

Ich habe `get_workspaces` aufgerufen und folgende Workspaces gefunden:

- `Marketing - Production` (`app_group_id`: `YOUR-APP-GROUP-ID-1`)
- `Marketing - Staging` (`app_group_id`: `YOUR-APP-GROUP-ID-2`)

Verwenden Sie `Marketing - Production` für Analytics-Prompts zu Produktions-Campaigns.
{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#workspaces){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#workspaces){% endif %}.

### Campaign-Performance der letzten Woche anzeigen {#show-me-campaign-performance-for-last-week}

{% tabs %}
{% tab Beispiel-Prompt %}

`In the Marketing - Production workspace, show campaign performance for the last seven days, including sends, opens, clicks, and top performers.`
{% endtab %}
{% tab Beispielantwort %}

Ich habe `get_campaign_list` und `get_campaign_dataseries` für den angeforderten Workspace und Zeitraum verwendet.

Zusammenfassung:

- Gesamtversand: `YOUR-TEST-SENDS`
- Gesamtöffnungen: `YOUR-TEST-OPENS`
- Gesamtklicks: `YOUR-TEST-CLICKS`
- Top-Campaign nach Öffnungen: `YOUR-TEST-CAMPAIGN-NAME`

Ich kann dies bei Bedarf nach Campaign, Kanal oder Tag aufschlüsseln.
{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#campaigns){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#campaigns){% endif %}.

### Ein E-Mail-Template erstellen {#create-an-email-template}

{% tabs %}
{% tab Beispiel-Prompt %}

`In the Marketing - Production workspace, create an onboarding email template named "YOUR-TEST-TEMPLATE-NAME".`
{% endtab %}
{% tab Beispielantwort %}

Ich habe `create_email_template` verwendet und Ihr Template erstellt.

- **Template-ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **Template-Name:** `YOUR-TEST-TEMPLATE-NAME`
- **Workspace:** `Marketing - Production`
{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/#templates){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/#templates){% endif %}.

## Beispiel-Workflows {#example-workflows}

Diese Beispiele kombinieren mehrere Tools, um eine Aufgabe von Anfang bis Ende abzuschließen.

### Berichte über mehrere Workspaces hinweg {#report-across-multiple-workspaces}

{% tabs %}
{% tab Beispiel-Prompt %}

`Get me an analytics report for the past week from my US Prod workspace and my EU Prod workspace, and compare total sends and open rates.`
{% endtab %}
{% tab Beispielantwort %}

Ich habe `get_workspaces` aufgerufen, um den Zugriff zu bestätigen, und dann `get_campaign_dataseries` für jeden Workspace über die letzten sieben Tage ausgeführt.

- `US Prod`: `YOUR-TEST-SENDS` Sendungen, `YOUR-TEST-OPEN-RATE` Öffnungsrate
- `EU Prod`: `YOUR-TEST-SENDS` Sendungen, `YOUR-TEST-OPEN-RATE` Öffnungsrate

`US Prod` hat diese Woche mehr Nachrichten gesendet, während `EU Prod` die höhere Öffnungsrate hatte. Ich kann jeden Workspace nach Campaign oder Kanal aufschlüsseln.
{% endtab %}
{% endtabs %}

### Templates von Staging nach Production kopieren {#copy-templates-from-staging-to-production}

{% tabs %}
{% tab Beispiel-Prompt %}

`Copy the email templates from my Staging workspace to my Production workspace.`
{% endtab %}
{% tab Beispielantwort %}

Ich habe `get_email_templates` und `get_email_template_info` verwendet, um die Templates in `Staging` zu lesen, und dann `create_email_template`, um jedes einzelne in `Production` neu zu erstellen.

- `YOUR-TEST-TEMPLATE-NAME-1`: erstellt in `Production` (`YOUR-TEST-TEMPLATE-ID-1`)
- `YOUR-TEST-TEMPLATE-NAME-2`: erstellt in `Production` (`YOUR-TEST-TEMPLATE-ID-2`)

Ich habe Drag-and-Drop-Editor-Templates übersprungen, die von `get_email_template_info` nicht unterstützt werden. Lassen Sie mich wissen, ob ich die kopierten Templates überprüfen soll.
{% endtab %}
{% endtabs %}

### Wöchentliche Zusammenfassung der Campaign-Performance {#summarize-weekly-campaign-health}

{% tabs %}
{% tab Beispiel-Prompt %}

`Give me a weekly campaign health summary for the Production workspace.`
{% endtab %}
{% tab Beispielantwort %}

Ich habe `get_campaign_list` und `get_campaign_dataseries` verwendet, um die Aktivitäten der letzten sieben Tage in `Production` abzurufen.

- Gesamtsendungen: `YOUR-TEST-SENDS`
- Öffnungsrate: `YOUR-TEST-OPEN-RATE`
- Klickrate: `YOUR-TEST-CLICK-RATE`
- Top-Campaign nach Conversions: `YOUR-TEST-CAMPAIGN-NAME`

Die Sendungen sind im Wochenvergleich gestiegen. Ich kann eine Aufschlüsselung nach Kanal hinzufügen oder Campaigns mit rückläufigem Engagement kennzeichnen.
{% endtab %}
{% endtabs %}

## So funktioniert der Remote-MCP-Server {#how-the-remote-mcp-server-works}

Wenn Sie eine Anfrage senden, laufen im Hintergrund einige Schritte ab:

1. **Sie geben Ihrem Client einen Prompt.** Sie formulieren eine Anfrage in natürlicher Sprache, z. B. nach der Campaign-Performance der letzten Woche.
2. **Das Modell des Clients wählt Tools aus.** Das KI-Modell in Ihrem Client interpretiert Ihre Anfrage und übersetzt sie in einen oder mehrere Braze-Tool-Aufrufe, wie z. B. `get_campaign_list` und `get_campaign_dataseries`.
3. **Braze führt den Tool-Aufruf aus.** Der Remote-MCP-Server empfängt jeden Tool-Aufruf über Ihre authentifizierte OAuth-Sitzung, wendet den von Ihnen angegebenen Workspace an und führt ihn gegen den entsprechenden Braze REST API-Endpunkt aus.
4. **Braze gibt das Ergebnis zurück.** Der Server sendet die Daten an Ihren Client zurück, der sie formatiert und Ihnen präsentiert.

Ihr Zugriff ergibt sich aus der Schnittmenge zweier Faktoren:

- **Die Berechtigungen (Scopes), die bei der Autorisierung der Verbindung gewährt wurden**, wie z. B. `mcp:tools`.
- **Ihre eigenen Dashboard-Nutzer:innenberechtigungen.** Wenn Sie Campaigns im Dashboard nicht anzeigen können, kann Ihr Agent das auch nicht. Wenn Sie E-Mail-Templates erstellen können, kann Ihr Agent das ebenfalls. Ein Agent kann Ihren eigenen Zugriff niemals überschreiten.

Der Workspace-Kontext wird mit jeder Anfrage übergeben, anstatt in einer lokalen Konfigurationsdatei gespeichert zu werden. So kann eine einzelne Verbindung über alle Workspaces hinweg funktionieren, für die Sie autorisiert sind.

{% multi_lang_include mcp_server/legal_disclaimer.md %}