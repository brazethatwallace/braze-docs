# Einrichtung des Braze MCP-Servers {#setting-up-the-braze-mcp-server}

> Erfahren Sie, wie Sie eine Verbindung zum Remote-Braze-MCP-Server herstellen, sich mit OAuth authentifizieren und Braze-Tools in Ihrem MCP-Client nutzen. Weitere Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Unterstützter MCP-Client | Jeder Client, der Remote-MCP-Server mit OAuth unterstützt, kann verwendet werden. Braze hat Claude, ChatGPT, Cursor, OpenAI Codex, Claude Code und Visual Studio Code verifiziert. |
| Braze-Dashboard-Konto | Sie melden sich mit Ihren normalen Braze-Zugangsdaten an, einschließlich SSO oder SAML, falls Ihr Unternehmen dies verwendet. Es gibt keine separate MCP-Anmeldung. |
| Auswahl des Server-Endpunkts | Wählen Sie `https://mcp.braze.com/mcp` (US) oder `https://mcp.braze.eu/mcp` (EU). Beide Endpunkte können jeden Braze-Cluster erreichen. |
| Kein IP-Allowlisting | Kund:innen, die [IP-Allowlisting](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) verwenden, können den Braze MCP-Server derzeit nicht nutzen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert note %}
Der Zugriff Ihres Agenten entspricht Ihren Dashboard-Berechtigungen. Wenn Ihr Dashboard-Zugriff auf ein Team statt auf einen vollständigen Workspace beschränkt ist, funktionieren einige Tools möglicherweise nicht.
{% endalert %}

## Zugriffsverwaltung (für Admins) {#managing-access-for-admins}

{% alert note %}
Bevor Nutzer:innen eine Verbindung herstellen können, muss ein Unternehmensadmin **MCP-OAuth-Zugriff** unter **Einstellungen** > **Administratoreinstellungen** > **OAuth** aktivieren. Weitere Informationen finden Sie unter [OAuth-Einstellungen verwalten]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).
{% endalert %}

### Zugriff gewähren {#grant-access}

Admins steuern den Zugriff auf den MCP-Server über die Berechtigung „Use MCP Server“. Standardmäßig verfügen Nutzer:innen nicht über diese Berechtigung, und sie muss explizit erteilt werden.

### Zugriff widerrufen {#revoke-access}

Um den Zugriff zu widerrufen, entfernen Sie die Berechtigung „Use MCP Server“ von der bzw. dem Nutzer:in. Wenn Sie Dashboard-Berechtigungen von Nutzer:innen entfernen, werden diese Funktionen bei der nächsten Anfrage auch von allen verbundenen Agenten entfernt.

### Nutzung überprüfen {#audit-usage}

Wenn sich Nutzer:innen erfolgreich über OAuth verbinden, wird ein Ereignis im [Sicherheitsereignisbericht](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report) protokolliert.

## Verbinden Sie Ihren Client {#connect-your-client}

### Schritt 1: Berechtigungen und Workspace-Zugriff bestätigen {#step-1-confirm-permissions-and-workspace-access}

1. Sie oder Ihre Unternehmensadministration müssen bestätigen, dass Sie die Berechtigung „Use MCP Server“ besitzen.
2. Wenn Sie Zugriff auf mehrere Workspaces benötigen, stellen Sie sicher, dass die Berechtigung für alle relevanten Workspaces aktiviert ist.

### Schritt 2: Braze als Remote-MCP-Konnektor hinzufügen {#step-2-add-braze-as-a-remote-mcp-connector}

Fügen Sie in Ihrem MCP-Client einen neuen Remote-Server oder einen angepassten Konnektor hinzu und geben Sie Ihre Braze-MCP-URL ein. In Claude können Sie beispielsweise zu **Settings** > **Connectors** > **Add custom connector** navigieren und die URL einfügen.

Es sind keine Client-ID, kein Client-Secret und kein API-Schlüssel erforderlich. Ihr Client registriert sich automatisch bei Braze.

Braze-MCP-Endpunkt-Optionen:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

{% alert tip %}
EU-Kund:innen sollten den EU-Endpunkt verwenden. Nicht-EU-Kund:innen können beide Endpunkte nutzen.
{% endalert %}

Einrichtungsanleitungen für Clients:

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)
- [Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

### Schritt 3: Über OAuth bei Braze anmelden {#step-3-sign-in-to-braze-through-oauth}

Wenn Ihr Agent zum ersten Mal ein Braze-Tool aufruft, öffnet Ihr Client ein Browserfenster und leitet Sie zur Anmeldung bei Braze weiter.

1. Melden Sie sich wie gewohnt bei Braze an, einschließlich SSO, falls erforderlich.
2. Wenn Ihre Anmeldung Zugriff auf mehr als ein Unternehmen im selben Cluster ermöglicht, wählen Sie das gewünschte Unternehmen aus.
3. Überprüfen Sie auf dem Zustimmungsbildschirm den Zugriff, den die Anwendung anfordert.
4. Aktivieren Sie das Bestätigungskontrollkästchen, um der Braze-Datenschutzrichtlinie zuzustimmen, und wählen Sie dann **Continue**, um zu Ihrem MCP-Client zurückzukehren.

![Der Braze-Zustimmungsbildschirm, der zeigt, dass Claude Desktop Zugriff auf Braze-Kontoinformationen und umfassenden Zugriff auf Braze-Daten anfordert, mit einem Kontrollkästchen zur Bestätigung der Datenschutzrichtlinie sowie den Buttons „Cancel“ und „Continue“.]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: style="max-width:65%;"}

Ihre Sitzung verwendet kurzlebige Zugriffstoken, die automatisch aktualisiert werden. Gelegentlich müssen Sie sich möglicherweise erneut anmelden.

### Schritt 4: Ihrem Agenten mitteilen, welchen Workspace er verwenden soll {#step-4-tell-your-agent-which-workspace-to-use}

Wenn Ihr Konto Zugriff auf mehr als einen Workspace hat, geben Sie den Workspace in Ihrem Prompt an. Zum Beispiel:

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

Wenn Sie keinen Workspace angeben, fragt Ihr Agent möglicherweise nach.

### Schritt 5: Einen Testprompt senden {#step-5-send-a-test-prompt}

Senden Sie nach der Einrichtung einen kurzen Validierungsprompt, zum Beispiel:

- `List the Braze tools available in this workspace.`
- `Show my recent Canvases from the Production workspace.`

Weitere Beispiele finden Sie unter [Verwendung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

## Beispiel: Mit Claude verbinden {#example-connect-with-claude}

Die Verbindung mit einem Client erfordert nur wenige Schritte. Die folgende Anleitung verwendet Claude, aber der Ablauf ist bei anderen unterstützten Clients ähnlich.

1. Gehen Sie in Claude zu **Settings** > **Connectors** > **Add custom connector**.
2. Geben Sie einen Namen ein, z. B. `Braze`, und fügen Sie dann Ihre Braze MCP-URL ein: `https://mcp.braze.com/mcp` für US oder `https://mcp.braze.eu/mcp` für EU. Sie benötigen keine Client-ID, kein Client-Secret und keinen API-Schlüssel.
3. Wählen Sie **Add** aus, um den Konnektor zu speichern. Claude registriert sich automatisch bei Braze.
4. Wählen Sie **Connect** aus, um die Authentifizierung zu starten. Claude öffnet ein Browserfenster und leitet Sie zur Anmeldung bei Braze weiter.
5. Melden Sie sich mit Ihren üblichen Zugangsdaten bei Braze an, einschließlich SSO, falls Ihr Unternehmen es nutzt. Wenn Ihre Anmeldung Zugriff auf mehr als ein Unternehmen im selben Cluster hat, wählen Sie das Unternehmen aus, das Sie verwenden möchten.
6. Überprüfen Sie auf dem Zustimmungsbildschirm den angeforderten Zugriff, aktivieren Sie das Bestätigungskontrollkästchen und wählen Sie dann **Continue** aus. Claude kehrt zu Ihrem Chat zurück, und Ihr Agent kann nun die Braze-Tools verwenden.

Um die Verbindung zu bestätigen, senden Sie einen Testprompt wie `Show my recent Canvases from the Production workspace`.

## Migration vom lokalen Beta-Server {#migrating-from-the-local-beta-server}

Sie können den lokalen Beta-Server und den remote gehosteten Server während der Migration parallel betreiben. Möglicherweise müssen Sie Ihrem Agenten explizit mitteilen, welchen Server er verwenden soll.

Der remote gehostete Server enthält neue Tools, die im lokalen Beta-Server nicht vorhanden sind. Wenn Sie Skills für den lokalen Server erstellt haben, müssen Sie diese möglicherweise aktualisieren, damit sie auf die neuen Tool-Namen und das neue Verhalten verweisen.

Nachdem Sie bestätigt haben, dass Ihre Workflows und Skills auf dem Remote-Server funktionieren, deaktivieren Sie den lokal gehosteten Server.

## Fehlerbehebung {#troubleshooting}

### Authentifizierung schlägt in einem unterstützten Client fehl {#authentication-fails-in-a-supported-client}

1. Bestätigen Sie, dass Ihr Unternehmensadmin **MCP-OAuth-Zugriff** in den [OAuth-Einstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin) aktiviert hat.
2. Bestätigen Sie, dass Ihre Nutzer:in die Berechtigung „Use MCP Server“ besitzt.
3. Versuchen Sie die Anmeldung und Autorisierung erneut.

### Authentifizierung wird in einem nicht verifizierten Client blockiert {#authentication-is-blocked-in-an-unverified-client}

Braze pflegt eine Zulassungsliste unterstützter Client-Domains aus Sicherheitsgründen. Wenn Sie sich von einem Client aus verbinden, der nicht auf der Zulassungsliste steht, kann die Authentifizierung blockiert werden. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="support for your MCP client" %}

Clients, die lokal auf Ihrem Rechner ohne ein benutzerdefiniertes Schema ausgeführt werden, wie Claude Code und OpenAI Codex, sollten ebenfalls funktionieren.

### Tools werden in Ihrem Client nicht angezeigt {#tools-dont-appear-in-your-client}

Wenn Ihr Agent die Braze-Tools nicht auflisten kann, warten Sie einige Minuten und versuchen Sie es erneut. Diese Probleme sind oft vorübergehend und lösen sich von selbst.

Wenn das Problem weiterhin besteht, nehmen Sie ein Video auf und senden Sie es zur Untersuchung an [mcp-product@braze.com](mailto:mcp-product@braze.com).

### Agent kann nicht auf erwartete Tools zugreifen {#agent-cannot-access-expected-tools}

1. Bestätigen Sie, dass Ihre Dashboard-Nutzer:in über die erforderlichen Berechtigungen verfügt. Ihr Agent kann nur Tools verwenden, die zu Ihrem eigenen Dashboard-Zugriff passen.
2. Bestätigen Sie, dass Sie den erwarteten Workspace in Ihrem Prompt ausgewählt haben.
3. Bitten Sie Ihren Agenten, `get_workspaces` aufzurufen, und überprüfen Sie die verfügbaren Workspace-IDs.

### Agent verwendet den falschen Workspace {#agent-uses-the-wrong-workspace}

Wenn Ihr Konto auf mehr als einen Workspace zugreifen kann, benennen Sie den Workspace in Ihrem Prompt mit dem exakten Namen, der im Braze-Dashboard angezeigt wird. Wenn Sie keinen Workspace angeben, fragt Ihr Agent möglicherweise nach oder verwendet einen unerwarteten.

{% alert important %}
Bevor Ihr Agent mit der Arbeit beginnt, bestätigen Sie immer, welchen Workspace er verwendet. In einigen Fällen kann ein Agent einen anderen Workspace auswählen als den, den Sie beabsichtigt haben.
{% endalert %}

### Zu einem anderen Unternehmen wechseln {#switching-to-a-different-company}

Ihr Unternehmen wird bei der ersten Autorisierung festgelegt. Um in einem anderen Unternehmen auf demselben Cluster zu arbeiten, trennen Sie den Braze-Konnektor in Ihrem Client, autorisieren Sie sich erneut und wählen Sie das andere Unternehmen bei der Anmeldung aus.

{% multi_lang_include mcp_server/legal_disclaimer.md %}