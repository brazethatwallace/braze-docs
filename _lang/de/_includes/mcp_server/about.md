# Der Braze MCP-Server {#the-braze-mcp-server}

> Erfahren Sie mehr über den Braze MCP-Server, eine sichere Remote-Verbindung, über die KI-Tools wie Claude und Cursor auf nicht PII-bezogene Braze-Daten zugreifen können, um Fragen zu beantworten, Trends zu analysieren, Insights zu gewinnen und Inhalte zu erstellen.

{% alert important %}
Der Remote-MCP-Server befindet sich im Early Access. Kontaktieren Sie Ihren Account Manager, um Zugang anzufordern.
{% endalert %}

## Was ist das Model Context Protocol (MCP)? {#what-is-model-context-protocol-mcp}

​​Model Context Protocol, oder MCP, ist ein Standard, der es KI-Agenten ermöglicht, sich mit Daten einer anderen Plattform zu verbinden und damit zu arbeiten. Es besteht aus zwei Hauptteilen:

- **MCP-Client:** Die Anwendung, in der der KI-Agent ausgeführt wird, wie z. B. Cursor oder Claude.
- **MCP-Server:** Ein Dienst, der von einer anderen Plattform wie Braze bereitgestellt wird und definiert, welche Tools die KI nutzen kann und auf welche Daten sie zugreifen kann.

## Über den Braze MCP-Server {#about-the-braze-mcp-server}

Nach dem [Einrichten des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} können Sie KI-Tools wie Agenten, Assistenten und Chatbots direkt mit Braze verbinden, sodass diese aggregierte Daten wie Canvas- und Campaign-Analytics, angepasste Attribute, Segmente und mehr lesen können. Der Braze MCP-Server eignet sich hervorragend für:

- Die Entwicklung KI-gestützter Tools, die Braze-Kontext benötigen.
- CRM-Entwickler:innen, die mehrstufige Agenten-Workflows erstellen.
- Technische Marketer, die mit natürlichsprachlichen Abfragen experimentieren.

Der Braze MCP-Server umfasst sowohl Lese- als auch Schreib-Tools. Diese Tools geben keine Daten aus Braze-Nutzerprofilen zurück. Ihre Agenten übernehmen Ihre Braze-Dashboard-Nutzerberechtigungen. Die vollständige Liste der verfügbaren Tools finden Sie unter [Verfügbare API-Funktionen]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Tools, die PII auf Nutzerebene offenlegen, sind nicht verfügbar.
{% endalert %}

Verwenden Sie den MCP-Server, um Fragen zur Performance von Campaigns und Canvas zu stellen, Ihre Segmente und angepassten Attribute zu erkunden, Berichte zu erstellen und Inhalte wie E-Mail-Templates, Content Blocks und Medienbibliothek-Assets in natürlicher Sprache zu erstellen.

## Ist der Beta-MCP-Server veraltet? {#is-the-beta-mcp-server-deprecated}

Ja. Der lokal gehostete MCP-Server, der im August 2025 veröffentlicht wurde, ist veraltet und wird keine weiteren Updates erhalten. Sie können ihn weiterhin verwenden, aber Braze empfiehlt die Migration zur remote gehosteten Version.

### Wie unterscheidet sich der Remote-Server? {#how-is-the-remote-server-different}

Der bisherige Braze-MCP-Server lief lokal auf Ihrem Rechner. Sie mussten ein Paket installieren, eine Konfigurationsdatei verwalten und einen Braze-API-Schlüssel mit den richtigen Berechtigungen erstellen. Der Remote-MCP-Server macht dieses lokale Setup überflüssig.

Verbinden Sie sich von einem unterstützten MCP-Client in weniger als einer Minute. Die Authentifizierung erfolgt über OAuth. Der Zugriff ist an Ihr Braze-Dashboard-Nutzerkonto gebunden, nicht an einen gemeinsam genutzten API-Schlüssel. Was ein Agent sehen und tun kann, entspricht also Ihren Dashboard-Berechtigungen. Wenn ein:e Dashboard-Nutzer:in den Zugriff in Braze verliert, verliert auch der Client den Zugriff.

Die wichtigsten Unterschiede sind:

- **Setup:** Fügen Sie eine Braze-URL ein, anstatt ein Paket zu installieren und Konfigurationsdateien zu bearbeiten.
- **Authentifizierung:** Melden Sie sich mit Ihrem Braze-Konto an, anstatt einen API-Schlüssel zu erstellen.
- **Berechtigungen:** Der Zugriff basiert auf Ihrem Dashboard-Nutzerkonto anstelle von API-Schlüssel-Berechtigungen.
- **Workspace-Targeting:** Der Workspace-Kontext wird pro Anfrage übergeben, anstatt in der lokalen Konfiguration festgelegt zu sein.

## Häufig gestellte Fragen (FAQ) {#faq}

### Welche MCP-Clients werden unterstützt? {#which-mcp-clients-are-supported}

Jeder MCP-Client, der Remote-MCP-Server mit OAuth unterstützt, kann verwendet werden. Braze hat folgende Clients verifiziert:

- Claude über benutzerdefinierte Konnektoren
- ChatGPT über benutzerdefinierte Konnektoren
- Cursor
- OpenAI Codex
- Claude Code
- Visual Studio Code

### Auf welche Braze-Daten hat mein MCP-Client Zugriff? {#what-braze-data-can-my-mcp-client-access}

MCP-Clients können auf Tools zugreifen, die keine PII auf Nutzerebene zurückgeben.

### Kann mein MCP-Client Braze-Daten ändern? {#can-my-mcp-client-change-braze-data}

Ja, wenn Ihr Dashboard-Nutzerkonto über die entsprechenden Berechtigungen verfügt.

### Benötige ich weiterhin einen Braze-API-Schlüssel? {#do-i-still-need-a-braze-api-key}

Nicht für MCP. API-Schlüssel funktionieren weiterhin für die REST API und werden nicht eingestellt.

### Welche Regionen werden unterstützt? {#which-regions-are-supported}

Beide Braze-Cluster werden unterstützt. Derzeit sind zwei Endpunkte verfügbar:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

Jeder Endpunkt kann jeden Braze-Cluster erreichen.

### Kann ich den Braze Remote-MCP-Server mit anderen Tools als den verifizierten verwenden? {#can-i-use-the-braze-remote-mcp-server-with-tools-other-than-the-verified-list}

Sie können es versuchen, aber die Authentifizierung könnte blockiert werden. Braze pflegt derzeit eine Zulassungsliste unterstützter Domains aus Sicherheitsgründen. Wenn Ihr Tool nicht auf der Liste steht und Sie auf Authentifizierungsprobleme stoßen, kontaktieren Sie [mcp-product@braze.com](mailto:mcp-product@braze.com).

### Unterstützt der Remote-Server mehrere Workspaces? {#does-the-remote-server-support-multiple-workspaces}

Ja. Geben Sie den Workspace pro Konversation oder pro Anfrage an. Eine Verbindung deckt alle Workspaces ab, auf die Sie zugriffsberechtigt sind.

### Kann mein Agent auf PII auf Nutzerebene zugreifen? {#can-my-agent-access-user-level-pii}

Nein. Derzeit sind Tools, die PII offenlegen, nicht verfügbar.

### Was passiert, wenn sich meine Berechtigungen ändern? {#what-happens-when-my-permissions-change}

Der Agentenzugriff ändert sich mit dem Dashboard-Nutzerkonto. Berechtigungsänderungen werden bei der nächsten Anfrage wirksam. Deaktivierte Dashboard-Nutzer:innen verlieren den MCP-Zugriff.

### Warum sehe ich den Braze-Konnektor nicht im Verzeichnis meines Clients? {#why-do-i-not-see-the-braze-connector-in-my-clients-directory}

Verzeichniseinträge werden nach Beginn des Early Access ausgerollt. Sie können sich jederzeit manuell über die Braze-MCP-URL verbinden.

### Mein Unternehmen verwendet IP-Allowlisting. Können wir den Remote-MCP-Server nutzen? {#my-company-uses-ip-allowlisting-can-we-use-the-remote-mcp-server}

Derzeit nicht. Kund:innen, die [IP-Allowlisting](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) verwenden, können nicht am Early-Access-Programm teilnehmen.

{% multi_lang_include mcp_server/legal_disclaimer.md %}