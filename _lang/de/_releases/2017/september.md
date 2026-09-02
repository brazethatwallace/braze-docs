---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2017."
---

# September 2017

## Neue Funktionalität für Engagement-Berichte {#new-functionality-for-engagement-reports}

Sie können jetzt [Engagement-Berichte]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports#engagement-reports) verwenden, um Metriken für eine Campaign über bestimmte Zeiträume hinweg zu aggregieren. Sie können z. B. die Gesamtzahl der Öffnungen aus einem Quartal oder die Gesamtzahl der Klicks aus der gesamten Lifetime einer Campaign oder eines Canvas exportieren. Alles, was Sie tun müssen, ist:
- Einen Zeitrahmen auswählen, aus dem Sie Daten exportieren möchten,
- einen Zeitplan für einen Engagement-Bericht erstellen, der regelmäßig an eine:n oder mehrere Empfänger:innen gesendet wird, und
- Campaigns und Canvases auf der Grundlage ihrer Tags zu Ihrem Bericht hinzufügen.

## Updates für die Seite „Kundenprofil“ {#updates-to-user-profile-page}

Die [Seite „Kundenprofil“]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles) wurde aktualisiert.

## Web-Push-Benachrichtigungen, die eine Aktion der Nutzer:innen erfordern, um sie zu schließen {#web-push-notifications-that-require-user-action-to-dismiss}

Sie können jetzt für Chrome-Web-Pushes ein Verhalten zum Schließen von Nachrichten einrichten, bei dem die Empfänger:innen mit der Nachricht interagieren müssen, um sie zu schließen. Dieses Feature erfordert Web SDK Version 1.6.13 oder höher.

## E-Mail-Preheader {#email-preheaders}

Wenn Sie eine E-Mail-Nachricht in Braze erstellen, können Sie jetzt ganz einfach einen Preheader im Abschnitt **Sending Info** einfügen.

## Neuer API-Endpunkt für den Export von Rohdaten {#new-api-endpoint-for-raw-event-export}

Wir haben einen neuen [API-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues#whitelisting-brazes-api-endpoint-ip-ranges) hinzugefügt, `/raw_data/status`, mit dem Sie abfragen können, ob ein bestimmter Tag in den Raw Event Export geladen wurde. Sie können damit überprüfen, ob die Rohdaten eines bestimmten Tages verfügbar sind, um die Fehlersuche und Automatisierung zu erleichtern.