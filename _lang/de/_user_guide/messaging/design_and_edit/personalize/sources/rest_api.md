---
nav_title: REST-API
article_title: REST-API
page_order: 1
description: "Erfahren Sie, wie Sie Connected-Content verwenden, um Daten aus REST APIs in Ihre Nachrichten zu übertragen und so eine Realtime-Personalisierung zu ermöglichen."
---

# REST-API {#rest-api}

> Rufen Sie Daten aus externen REST APIs zum Sendezeitpunkt direkt in Ihre Nachrichten ab – mit [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). So können Sie Nachrichten mit Realtime-Informationen von Ihren eigenen Servern, Drittanbieter-Diensten oder jedem öffentlich zugänglichen API-Endpunkt personalisieren.

## So funktioniert es {#how-it-works}

{% raw %}
Connected-Content sendet eine HTTP-Anfrage an die von Ihnen angegebene URL und speichert die Antwort, damit Sie sie mit Liquid referenzieren können. Fügen Sie Ihrer Nachricht ein `{% connected_content %}`-Tag hinzu, und Braze ruft den Endpunkt auf, wenn die Nachricht gesendet wird.

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

Connected-Content unterstützt GET- und POST-Anfragen. Braze erwartet, dass der Server innerhalb von zwei Sekunden antwortet – gestalten Sie Ihre Endpunkte daher für niedrige Latenz.

## Häufige Anwendungsfälle {#common-use-cases}

| Anwendungsfall | Beschreibung |
| --- | --- |
| Produktempfehlungen | Personalisierte Produktvorschläge aus einem Empfehlungssystem abrufen |
| Realtime-Preise oder Lagerbestände | Aktuelle Preise oder Verfügbarkeiten zum Sendezeitpunkt anzeigen |
| Wetterbasierte Inhalte | Lokale Wetterdaten abrufen, um Nachrichten individuell anzupassen |
| Treuepunkte-Salden | Aktuelle Rewards- oder Kontostände anzeigen |
| Content-Feeds | Die neuesten Blogbeiträge, Artikel oder Neuigkeiten einfügen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Häufige Anwendungsfälle" }

## Authentifizierung {#authentication}

Braze unterstützt Basic-Authentifizierung, Token-Authentifizierung und OAuth für Connected-Content-Anfragen. Sie können Zugangsdaten sicher im Braze-Dashboard unter **Settings** > **Connected Content** speichern und in Ihren API-Aufrufen referenzieren.

Weitere Informationen finden Sie unter [Einen Connected-Content-API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#authentication-types).

## Fehlerbehandlung {#error-handling}

Wenn der Endpunkt einen Fehler zurückgibt oder eine Zeitüberschreitung auftritt, rendert Braze anstelle der Connected-Content-Antwort einen leeren String. Sie können Fehler erkennen, indem Sie prüfen, ob die gespeicherte Variable null ist, und die Nachricht bedingt abbrechen oder Fallback-Inhalte anzeigen.

Weitere Informationen finden Sie unter [Connected-Content abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/).

## Performance-Überlegungen {#performance-considerations}

Da Braze Nachrichten in großem Umfang versendet, muss Ihr Server Tausende gleichzeitiger Verbindungen verarbeiten können. Nutzen Sie Caching, wo es sinnvoll ist, und setzen Sie Rate-Limits für Ihre Nachrichten, um eine Überlastung externer Endpunkte zu vermeiden.

Die vollständige Connected-Content-Referenz finden Sie unter [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).