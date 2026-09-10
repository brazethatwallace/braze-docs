---
nav_title: APIs und Bezeichner
article_title: APIs und Bezeichner
page_order: 0
page_type: reference
description: "Dieser Artikel behandelt die Seite „APIs und Bezeichner“, auf der API-Bezeichner für Ihren Workspace angezeigt werden."
---

# APIs und Bezeichner {#apis-and-identifiers}

> Die Seite **APIs und Bezeichner** ist Ihre zentrale Anlaufstelle für die Verwaltung all Ihrer REST-API-Schlüssel an einem Ort. Hier können Sie auf die API-Schlüssel und App-Bezeichner jedes Workspaces zugreifen.

Sie finden die Seite **APIs und Bezeichner** unter **Einstellungen** > **Einrichtung und Tests** > **APIs und Bezeichner**.

## API-Schlüssel {#api-keys}

Dieser Abschnitt enthält die REST-API-Schlüssel Ihres Workspace – die eindeutigen Bezeichner, die Ihnen den Zugriff auf die Daten eines Workspace ermöglichen. Ein REST-API-Schlüssel ist bei jeder Anfrage an die Braze-API erforderlich. Weitere Informationen zum Erstellen und Verwenden von API-Schlüsseln finden Sie in unserer [Übersicht zu REST-API-Schlüsseln]({{site.baseurl}}/api/basics).

### API-IP-Allowlisting {#api-ip-allowlisting}

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen angeben, die REST-API-Anfragen für einen bestimmten REST-API-Schlüssel senden dürfen. Dies wird als IP-Allowlisting bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie diese beim Erstellen eines neuen REST-API-Schlüssels im Bereich **Allowlist IPs** hinzu:

![Bereich für API-IP-Allowlisting beim Erstellen eines neuen REST-API-Schlüssels]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Wenn Sie keine angeben, können Anfragen von jeder IP-Adresse gesendet werden.

{% alert tip %}
Sie erstellen einen Braze-zu-Braze-Webhook und verwenden Allowlisting? Sehen Sie sich unsere Liste der [zulässigen IPs]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) an.
{% endalert %}

### API-Nutzungsbenachrichtigungen {#api-usage-alerts}

Richten Sie API-Nutzungsbenachrichtigungen ein, um wichtige API-Aktivitäten zu überwachen und Probleme frühzeitig zu erkennen. Diese Benachrichtigungen helfen Ihnen, unerwartete Traffic-Muster zu erkennen, bevor sie Ihr Erlebnis beeinträchtigen.

Sie können zwei Arten von API-Aktivitäten verfolgen:

- **REST-API-Endpunkte:** Aktionen wie das Senden von Nachrichten, das Erstellen von Campaigns oder das Exportieren von Daten.
- **SDK-API-Anfragen:** Ereignisse aus Ihrem Kundenerlebnis, wie das Triggern von In-App-Nachrichten oder das Synchronisieren von Nutzerprofilen. *Dieses Feature ist verfügbar, wenn Sie Monthly Active Users (CY 24–25) erworben haben.*

Nachdem Sie ausgewählt haben, was Sie verfolgen möchten, können Sie Benachrichtigungsbedingungen definieren. Sie können sich beispielsweise benachrichtigen lassen, wenn Fehlerantworten innerhalb einer Stunde um 20 % zunehmen. Sie erhalten eine Benachrichtigung per E-Mail, Webhook oder beides, je nach Ihren Einstellungen. Informationen zum Einstieg finden Sie unter [API-Nutzungsbenachrichtigungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts).

## App-Bezeichner {#app-identifiers}

Dieser Abschnitt enthält eine Liste von Bezeichnern, die verwendet werden, um bestimmte Apps in Anfragen an die Braze API zu referenzieren. Weitere Informationen zu App-Bezeichnern finden Sie unter [App-Bezeichner-API-Schlüssel]({{site.baseurl}}/api/identifier_types).

## Andere Bezeichner {#other-identifiers}

Um die Integration mit unserer API durchzuführen, können Sie nach Bezeichnern suchen, die mit Segments, Campaigns, Content Cards und mehr zusammenhängen und auf die Sie über die externe Braze-API zugreifen möchten. Alle Nachrichten sollten die [UTF-8](https://en.wikipedia.org/wiki/UTF-8)-Codierung verwenden. Nachdem Sie einen Bezeichner ausgewählt haben, wird dieser unterhalb des Dropdown-Menüs angezeigt.

Weitere Informationen finden Sie unter [API-Bezeichnertypen]({{site.baseurl}}/api/identifier_types).