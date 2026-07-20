---
nav_title: APIs und Bezeichner
article_title: APIs und Bezeichner
page_order: 0
page_type: reference
description: "Dieser Artikel behandelt die Seite „APIs und Bezeichner“, auf der API-Bezeichner für Ihren Workspace angezeigt werden."

---

# API-Schlüssel {#api-keys}

> Die Seite **APIs und Bezeichner** ist Ihre zentrale Anlaufstelle für die Verwaltung all Ihrer REST-API-Schlüssel an einem Ort. Hier können Sie auf die API-Schlüssel und App-Bezeichner jedes Workspaces zugreifen.

Sie finden die Seite **APIs und Bezeichner** unter **Einstellungen**.

## API-Schlüssel

Dieser Abschnitt enthält die REST-API-Schlüssel Ihres Workspaces – die eindeutigen Bezeichner, die Ihnen den Zugriff auf die Daten eines Workspaces ermöglichen. Bei jeder Anfrage an die Braze API ist ein REST-API-Schlüssel erforderlich. Weitere Informationen zum Erstellen und Verwenden von API-Schlüsseln finden Sie in unserer [Übersicht zu REST-API-Schlüsseln]({{site.baseurl}}/api/api_key).

### IP-Allowlisting für APIs {#api-ip-allowlisting}

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen angeben, die REST-API-Anfragen für einen bestimmten REST-API-Schlüssel senden dürfen. Dies wird als Allowlisting oder Whitelisting bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie diese beim Erstellen eines neuen REST-API-Schlüssels im Abschnitt **Whitelist IPs** hinzu:

![Abschnitt „API IP Whitelisting“ beim Erstellen eines neuen API-Schlüssels]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Wenn Sie keine angeben, können Anfragen von jeder IP-Adresse gesendet werden.

{% alert tip %}
Sie erstellen einen Braze-zu-Braze-Webhook und verwenden Allowlisting? Sehen Sie sich unsere Liste der [IPs für das Whitelisting]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) an.
{% endalert %}

### API-Nutzungsbenachrichtigungen {#api-usage-alerts}

Richten Sie API-Nutzungsbenachrichtigungen ein, um wichtige API-Aktivitäten zu überwachen und Probleme frühzeitig zu erkennen. Diese Benachrichtigungen helfen Ihnen, unerwartete Traffic-Muster zu erkennen, bevor sie Ihr Kundenerlebnis beeinträchtigen.

Sie können zwei Arten von API-Aktivitäten verfolgen:

- **REST-API-Endpunkte:** Aktionen wie das Senden von Nachrichten, das Erstellen von Kampagnen oder das Exportieren von Daten.
- **SDK-API-Anfragen:** Ereignisse aus Ihrem Kundenerlebnis, wie das Triggern von In-App-Nachrichten oder das Synchronisieren von Nutzerprofilen. *Dieses Feature ist verfügbar, wenn Sie Monthly Active Users (CY 24–25) erworben haben.*

Nachdem Sie ausgewählt haben, was Sie verfolgen möchten, können Sie Benachrichtigungsbedingungen definieren. Lassen Sie sich beispielsweise benachrichtigen, wenn Fehlerantworten innerhalb einer Stunde um 20 % ansteigen. Sie erhalten eine Benachrichtigung per E-Mail, Webhook oder beides, je nach Ihren Einstellungen. Informationen zum Einstieg finden Sie unter [API-Nutzungsbenachrichtigungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts).

## App-Bezeichner {#app-identifiers}

Dieser Abschnitt enthält eine Liste von Bezeichnern, die verwendet werden, um bestimmte Apps in Anfragen an die Braze API zu referenzieren. Weitere Informationen zu App-Bezeichnern finden Sie unter [App-Bezeichner-API-Schlüssel]({{site.baseurl}}/api/identifier_types).

## Weitere Bezeichner {#other-identifiers}

Für die Integration mit unserer API können Sie nach Bezeichnern suchen, die mit Segmenten, Campaigns, Content Cards und mehr verknüpft sind und auf die Sie über die externe Braze API zugreifen möchten. Alle Nachrichten sollten die [UTF-8](https://en.wikipedia.org/wiki/UTF-8)-Kodierung verwenden. Nachdem Sie einen Bezeichner ausgewählt haben, wird er unterhalb des Dropdown-Menüs angezeigt.

Weitere Informationen finden Sie unter [API-Bezeichnertypen]({{site.baseurl}}/api/identifier_types).