# Der Braze MCP-Server {#the-braze-mcp-server}

> Erfahren Sie mehr über den Braze MCP-Server, eine sichere Verbindung, über die KI-Tools wie Claude und Cursor auf nicht PII-bezogene Braze-Daten zugreifen können, um Fragen zu beantworten, Trends zu analysieren und Insights zu gewinnen.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert important %}
## Sunsetting des lokal gehosteten Braze MCP-Servers {#sunsetting-the-locally-hosted-braze-mcp-server}

In diesem Sommer wird Braze einen remote, von Braze gehosteten MCP-Server im Early Access veröffentlichen. Er ersetzt den lokal gehosteten Beta-Server (`braze-mcp-server` auf [PyPI](https://pypi.org/project/braze-mcp-server/) und im Claude Desktop-Erweiterungsverzeichnis).

**Was das für Sie bedeutet:**

- Der lokal gehostete Server funktioniert weiterhin, wird aber nicht mehr unterstützt. Wir werden keine neuen Endpunkte hinzufügen oder Probleme in der Beta beheben.
- Sobald der Remote-Server im Early Access verfügbar ist, müssen Sie zu diesem wechseln. Der Remote-Server erfordert keine lokale Installation, verwendet OAuth anstelle statischer API-Schlüssel und funktioniert mit MCP-Clients wie Claude, Copilot, Gemini CLI, Codex und Cursor.
- Behalten Sie diese Seite im Blick, um über die Early-Access-Verfügbarkeit informiert zu werden, oder kontaktieren Sie Ihr Braze-Account-Team, um Ihr Interesse zu bekunden.
{% endalert %}

## Was ist das Model Context Protocol (MCP)? {#what-is-model-context-protocol-mcp}

​​Das Model Context Protocol (MCP) ist ein Standard, der es KI-Agenten ermöglicht, sich mit Daten aus einer anderen Plattform zu verbinden und mit diesen zu arbeiten. Es besteht aus zwei Hauptteilen:

- **MCP-Client:** Die Anwendung, in der der KI-Agent ausgeführt wird, wie beispielsweise Cursor oder Claude.
- **MCP-Server:** Ein Dienst, der von einer anderen Plattform wie Braze bereitgestellt wird und festlegt, welche Tools die KI verwenden und auf welche Daten sie zugreifen kann.

## Informationen zum Braze MCP-Server {#about-the-braze-mcp-server}

Nach [der Einrichtung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} können Sie KI-Tools wie Agenten, Assistenten und Chatbots direkt mit Braze verbinden, sodass diese aggregierte Daten wie Canvas- und Campaign-Analytics, angepasste Attribute, Segmente und mehr lesen können. Der Braze MCP-Server eignet sich hervorragend für:

- Entwicklung von KI-gestützten Tools, die den Kontext von Braze erfordern.
- CRM-Ingenieur:innen, die mehrstufige Agenten-Workflows erstellen.
- Technische Marketer, die mit Abfragen in natürlicher Sprache experimentieren.

Der Braze MCP-Server umfasst sowohl Lese- als auch Schreib-Endpunkte. Sie geben keine Daten aus Braze-Nutzerprofilen zurück. Sie können auswählen, welche Endpunkte Sie Ihrem Braze-API-Schlüssel zuweisen, und diese Auswahl steuert, was ein Agent lesen, erstellen oder aktualisieren kann. Die vollständige Liste der verfügbaren Endpunkte und der erforderlichen Berechtigungen finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Weisen Sie dem API-Schlüssel nur die Berechtigungen zu, die Ihr Agent haben soll. Wenn Sie nicht möchten, dass Ihr Agent Änderungen in Braze vornimmt, lassen Sie beim Erstellen Ihres API-Schlüssels alle Schreibberechtigungen deaktiviert. Agenten könnten versuchen, Daten über jede Schreibberechtigung zu schreiben, die Sie gewähren.
{% endalert %}

## Anwendungsbeispiel {#usage-example}

Sie können mit Braze über natürliche Sprache interagieren, indem Sie Tools wie Claude oder Cursor verwenden. Weitere Beispiele und Best Practices finden Sie unter [Verwendung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![„Welche Braze-Funktionen stehen mir zur Verfügung?“ – diese Frage wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen (FAQ) {#faq}

### Welche MCP-Clients werden unterstützt? {#which-mcp-clients-are-supported}

Nur [Claude](https://claude.ai/) und [Cursor](https://cursor.com/) werden offiziell unterstützt. Sie benötigen ein Konto für einen dieser Clients, um den Braze MCP-Server nutzen zu können.

### Auf welche Braze-Daten hat mein MCP-Client Zugriff? {#what-braze-data-can-my-mcp-client-access}

MCP-Clients können auf Endpunkte zugreifen, die keine PII zurückgeben. Sie steuern über die Berechtigungen, die Sie Ihrem API-Schlüssel zuweisen, welche Endpunkte ein Agent verwenden kann.

### Kann mein MCP-Client Braze-Daten ändern? {#can-my-mcp-client-change-braze-data}

Ja. Der Server stellt eine gezielte Auswahl an Schreib-Endpunkten bereit, mit denen Agenten Inhalte in Ihrem Workspace erstellen oder aktualisieren können, z. B. Medienbibliothek-Assets, E-Mail-Templates und Content Blocks. Jeder Schreib-Endpunkt erfordert eine eigene API-Schlüssel-Berechtigung. Wenn Sie nicht möchten, dass Ihr Agent eine bestimmte Änderung in Braze vornimmt, lassen Sie die entsprechende Berechtigung beim Erstellen Ihres API-Schlüssels deaktiviert. Die vollständige Liste der Schreibfunktionen und der erforderlichen Berechtigungen finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

### Kann ich einen MCP-Server eines Drittanbieters für Braze verwenden? {#can-i-use-a-third-party-mcp-server-for-braze}

Die Verwendung eines MCP-Servers eines Drittanbieters für Braze-Daten wird nicht empfohlen. Bitte verwenden Sie ausschließlich den offiziellen Braze MCP-Server, der auf [PyPi](https://pypi.org/project/braze-mcp-server/) gehostet wird.

### Warum bietet der Braze MCP-Server keinen PII-Zugriff an? {#why-doesnt-the-braze-mcp-server-offer-pii-access}

Um Nutzerdaten zu schützen und gleichzeitig wertvolle Anwendungsfälle zu unterstützen, ist der Server auf Endpunkte beschränkt, die in der Regel keine PII zurückgeben. Dies verringert das Risiko für Ihren Workspace und die darin enthaltenen Personen.

### Kann ich meine API-Schlüssel wiederverwenden? {#can-i-reuse-my-api-keys}

Nein. Sie müssen einen neuen API-Schlüssel für Ihren MCP-Client erstellen. Gewähren Sie Ihren KI-Tools nur Zugriff auf das, womit Sie einverstanden sind, und vermeiden Sie erweiterte Berechtigungen.

### Wird der Braze MCP-Server lokal oder remote gehostet? {#is-the-braze-mcp-server-hosted-locally-or-remotely}

Der derzeit verfügbare Braze MCP-Server wird lokal gehostet. Ein remote, von Braze gehosteter MCP-Server wird in diesem Sommer im Early Access verfügbar sein und den lokal gehosteten Beta-Server ersetzen.

### Warum listet Cursor ausschließlich Funktionen auf? {#why-is-cursor-only-listing-functions}

Überprüfen Sie, ob Sie sich im Abfrage-Modus oder im Agenten-Modus befinden. Um den MCP-Server nutzen zu können, müssen Sie sich im Agenten-Modus befinden.

### Was soll ich tun, wenn der Agent eine Antwort zurückgibt, die mir unkorrekt erscheint? {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Bei der Arbeit mit Tools wie Cursor empfiehlt es sich, das verwendete Modell zu ändern. Wenn Sie beispielsweise die automatische Einstellung verwenden, versuchen Sie, auf ein bestimmtes Modell umzustellen, und experimentieren Sie, um herauszufinden, welches Modell die beste Performance für Ihren Anwendungsfall bietet. Sie können auch versuchen, einen neuen Chat zu starten und den Prompt erneut auszuführen.

Sollten die Probleme weiterhin bestehen, senden Sie uns bitte eine E-Mail an [mcp-product@braze.com](mailto:mcp-product@braze.com), um uns darüber zu informieren. Wenn möglich, fügen Sie bitte ein Video hinzu und erweitern Sie die Aufruffunktionen, damit wir sehen können, welche Aufrufe der Agent getätigt hat.

{% multi_lang_include mcp_server/legal_disclaimer.md %}