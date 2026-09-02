---
nav_title: APIs und Bezeichner
article_title: APIs und Bezeichner
page_order: 0
page_type: reference
description: "Dieser Artikel behandelt die Seite „APIs und Bezeichner“, auf der API-Bezeichner für Ihren Workspace angezeigt werden."
---

# API-Schlüssel {#api-keys}

> Die Seite **APIs und Bezeichner** ist Ihre zentrale Anlaufstelle für die Verwaltung all Ihrer Representational State Transfer-API-Schlüssel an einem Ort. Hier können Sie auf die API-Schlüssel und App-Bezeichner jedes Workspaces zugreifen.

Sie finden die Seite **APIs und Bezeichner** unter **Einstellungen**.

## API-Schlüssel

Dieser Abschnitt enthält die Representational State Transfer-API-Schlüssel Ihres Workspace – die eindeutigen Bezeichner, die Ihnen den Zugriff auf die Daten eines Workspace ermöglichen. Ein Representational State Transfer-API-Schlüssel ist bei jeder Anfrage an die Braze-API erforderlich. Weitere Informationen zum Erstellen und Verwenden von API-Schlüsseln finden Sie in unserer [Übersicht über Representational State Transfer-API-Schlüssel]({{site.baseurl}}/api/basics).

### IP-Zulassungsliste für die API {#api-ip-allowlisting}

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen angeben, die Representational State Transfer-API-Anfragen für einen bestimmten Representational State Transfer-API-Schlüssel senden dürfen. Dies wird als Zulassungsliste (Allowlisting bzw. Whitelisting) bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie diese beim Erstellen eines neuen Representational State Transfer-API-Schlüssels im Abschnitt **Whitelist IPs** hinzu:

![Abschnitt „IP-Whitelisting“ der API beim Erstellen eines neuen API-Schlüssels]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Wenn Sie keine Angaben machen, können Anfragen von jeder beliebigen IP-Adresse gesendet werden.

{% alert tip %}
Sie erstellen einen Braze-zu-Braze-Webhook und verwenden Zulassungslisten? Sehen Sie sich unsere Liste der [IPs für das Whitelisting]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) an.
{% endalert %}

### API-Nutzungsbenachrichtigungen {#api-usage-alerts}

Richten Sie API-Nutzungsbenachrichtigungen ein, um wichtige API-Aktivitäten zu überwachen und Probleme frühzeitig zu erkennen. Diese Benachrichtigungen helfen Ihnen, unerwartete Verkehrsmuster zu erkennen, bevor sie sich auf Ihr Erlebnis auswirken.

Sie können zwei Arten von API-Aktivitäten verfolgen:

- **Representational State Transfer-API-Endpunkte:** Aktionen wie das Senden von Nachrichten, das Erstellen von Campaigns oder das Exportieren von Daten.
- **SDK or Software-Development-Kit-API-Anfragen:** Ereignisse aus Ihrem Kundenerlebnis, wie das Trigger or triggern or triggern von In-App-Nachrichten oder das Synchronisieren von Nutzerprofilen. *Dieses Feature ist verfügbar, wenn Sie Monthly Active Users (CY 24–25) erworben haben.*

Sobald Sie festgelegt haben, was Sie verfolgen möchten, können Sie Benachrichtigungsbedingungen definieren. Lassen Sie sich beispielsweise benachrichtigen, wenn die Fehlerantworten innerhalb einer Stunde um 20 % ansteigen. Sie erhalten eine Benachrichtigung per E-Mail, Webhook oder beides, je nach Ihren Einstellungen. Informationen zu den ersten Schritten finden Sie unter [API-Nutzungsbenachrichtigungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts).

## App-Bezeichner {#app-identifiers}

Dieser Abschnitt enthält eine Liste von Bezeichnern, die verwendet werden, um in Anfragen an die Braze API auf bestimmte Apps zu verweisen. Weitere Informationen zu App-Bezeichnern finden Sie unter [App-Bezeichner-API-Schlüssel]({{site.baseurl}}/api/identifier_types).

## Weitere Bezeichner {#other-identifiers}

Um unsere API zu integrieren, können Sie nach den Bezeichnern suchen, die mit Segments, Campaigns, Content Cards und mehr zusammenhängen, auf die Sie über die externe Braze-API zugreifen möchten. Alle Nachrichten sollten die [UTF-8](https://en.wikipedia.org/wiki/UTF-8)-Kodierung verwenden. Nachdem Sie einen davon ausgewählt haben, wird der Bezeichner unterhalb des Dropdown-Menüs angezeigt.

Weitere Informationen finden Sie unter [API-Bezeichnertypen]({{site.baseurl}}/api/identifier_types).