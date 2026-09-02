---
nav_title: Juli
page_order: 6
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juli 2016."
---

# Juli 2016 {#july-2016}

## Filterung des Fehlerprotokolls der Entwicklungskonsole nach Fehlertyp {#filtering-the-developer-consoles-error-log-by-error-type}

Dieses Upgrade erleichtert Ihnen die Verwendung des Nachrichten-Fehlerprotokolls in der Entwicklungskonsole, um Probleme mit Ihren Braze-Integrationen zu beheben. Dieses Update für die Benutzerfreundlichkeit ermöglicht es Ihnen, das Nachrichten-Fehlerprotokoll nach Typ zu filtern, und erleichtert das Auffinden und die Identifizierung spezifischer Integrationsprobleme wesentlich.

## Zeitstempel für den letzten gesendeten Push für Uninstall-Tracking hinzugefügt {#added-timestamp-for-last-uninstall-tracking-push-sent}

Braze erkennt Deinstallationen, indem es einen stillen Push an die Apps einer Kund:in sendet, um zu sehen, welche Geräte reagieren. Dieses Feature fügt einen unauffälligen Zeitstempel hinzu, der anzeigt, wann das Uninstall-Tracking zuletzt ausgeführt wurde. Diesen Zeitstempel finden Sie auf Ihrer Einstellungsseite, auf der das Uninstall-Tracking konfiguriert ist. Erfahren Sie mehr über [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

![Uninstall-Tracking-Kontrollkästchen]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## Verbesserungen der Webhook-Tests hinzugefügt {#added-webhook-testing-enhancements}

Sie können jetzt eine Live-Webhook-Nachricht von Braze senden, bevor Sie eine Kampagne in Betrieb nehmen. Durch das Senden einer Testnachricht können Sie überprüfen, ob Ihre Nachrichten und Server-Endpunkte in einer sicheren Sandbox-Umgebung richtig konfiguriert wurden. Erfahren Sie mehr über [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook).

## Empfangene Nachrichtenvariante zum CSV-Export der Kampagnen-Empfänger:innen hinzugefügt {#added-message-variation-received-to-campaign-recipients-csv-export}

Wir haben dem CSV-Export für Kampagnen-Empfänger:innen eine Spalte hinzugefügt, die die empfangene Nachrichtenvariante angibt. Erfahren Sie mehr über den [Export von Daten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/) aus Braze.

## Ungefähres Limit für die Anzahl der Impressionen {#approximate-limit-on-number-of-impressions}

Sobald eine In-App-Nachricht eine bestimmte Anzahl von Impressionen erhalten hat, erlaubt Braze den Nutzer:innen nicht mehr, für den Empfang dieser Nachricht infrage zu kommen. Erfahren Sie mehr darüber, wie Sie ungefähre [Grenzen für Impressionen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap) festlegen.

![Obergrenze für IAM-Impressionen]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})