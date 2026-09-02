---
nav_title: loplat
article_title: loplat
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und loplat, einer Offline-Plattform für standortbasiertes Marketing, die es Ihnen ermöglicht, Proximity-Marketing-Kampagnen durchzuführen, indem Sie Standortkontext hinzufügen."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/) ist die führende Offline-Plattform für standortbasiertes Marketing. Nutzen Sie das loplat SDK or Software-Development-Kit, um die Besucherzahlen Ihres Shops intelligent zu steigern und Marketing-Kampagnen durchzuführen, die zum Kauf im Laden anregen. Sie können die Performance des Shops durch eine Analyse der Besucherzahlen nach Abschluss der Kampagne messen.

_Diese Integration wird von Loplat gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und loplat ermöglicht es Ihnen, die Standortdienste von loplat (Shop-POI und angepasste Geofences) zu nutzen, um geo-kontextuelle Marketing-Kampagnen auszulösen und angepasste Events mit Offline-Segmentierung zu erstellen. Wenn Nutzer:innen den von Ihnen in loplat X festgelegten Zielstandort besuchen, werden die Kampagnen- und Standortinformationen sofort an Braze gesendet.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| loplat X-Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein loplat X-Konto.<br><br>Senden Sie eine E-Mail an [support@loplat.com](mailto:support@loplat.com), um ein loplat X-Konto anzufordern. |
| loplat SDK or Software-Development-Kit | Das loplat SDK or Software-Development-Kit erkennt die Shop-Besuche von Nutzer:innen, verarbeitet Standort-Events und unterscheidet, ob Nutzer:innen an einem Ort verweilen oder sich bewegen. Sie können das loplat SDK or Software-Development-Kit verwenden, um die Besucherzahlen Ihres Shops zu analysieren, Push-Nachrichten zu senden, wenn Nutzer:innen Ihren Shop betreten, usw.<br><br>Beachten Sie, dass das SDK or Software-Development-Kit nur für Android und iOS verfügbar ist. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit den folgenden Berechtigungen:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Die von loplat bereitgestellten Standortinformationen zu angepassten Events können in Ihren Kampagnen für Anwendungsfälle wie die folgenden verwendet werden:

- [Benachrichtigung für Duty-Free-Aktionen](https://www.loplat.com/loplat-x#usecase)
    - Senden Sie Nutzer:innen, die sich in der Nähe der Boarding-Gates am Flughafen befinden, Rabattcoupons für Duty-Free-Shops.
- Standort-Push für Ladestationen für Elektrofahrzeuge (EV)
    - Legen Sie Geofences um EV-Ladestationen fest und benachrichtigen Sie Nutzer:innen, wenn sie sich in der Nähe einer Station befinden, um sie zum Laden zu ermutigen.

## Integration

### Schritt 1: Integration der SDKs {#step-1-integrate-the-sdks}

Integrieren Sie das loplat SDK or Software-Development-Kit und das Braze SDK or Software-Development-Kit in Ihre App anhand der Schritte, die in der Dokumentation zur [loplat-Braze-Integration](https://developers.loplat.com/braze/) beschrieben sind.

### Schritt 2: Synchronisieren Sie die Dashboards von Braze und loplat X und erstellen Sie eine Kampagne {#step-2-sync-the-braze-and-loplat-x-dashboards-and-create-a-campaign}

Erstellen Sie einen neuen API-Schlüssel im Braze-Dashboard. Kopieren Sie den API-Schlüssel und fügen Sie ihn unter **Settings** > **API Settings** im loplat X-Dashboard ein. Weitere Einzelheiten finden Sie im [Benutzerhandbuch von loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25).

#### API-getriggerte Zustellung {#api-triggered-delivery}

1. Erstellen Sie eine Braze-Kampagne oder ein Canvas, das mit **API-Triggered Delivery** versendet wird, und kopieren Sie die Kampagnen-ID.
2. Starten Sie die Kampagne in Braze, nachdem Sie alle Schritte abgeschlossen haben.
3. Gehen Sie zu loplat X und erstellen Sie eine Kampagne gemäß den Anweisungen im [Benutzerhandbuch von loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Fügen Sie die Braze-Kampagnen-ID unter den **Campaign Message Settings** ein und starten Sie die Kampagne.

![Kampagneneinstellungen in loplat X mit Braze-Kampagnen-ID für API-getriggerte Zustellung.]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### Aktionsbasierte Zustellung {#action-based-delivery}

Mit der Integration können Sie Standortbedingungen anwenden, indem Sie Geofence-Informationen, die Region, den Markennamen oder den Shop-Namen senden. Außerdem können Sie Segmente hinzufügen oder eine Conversion mit dem angepassten Event zuordnen, das Sie erstellt haben.
1. Erstellen Sie eine loplat X-Kampagne gemäß den Anweisungen im [Benutzerhandbuch von loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Fügen Sie ein angepasstes Event unter den **Campaign Message Settings** hinzu und starten Sie die Kampagne.
3. Rufen Sie das Braze-Dashboard auf und erstellen Sie eine Kampagne oder ein Canvas, das mit **Action-Based Delivery** versendet wird.
4. Wählen Sie das angepasste Event aus, das Sie in loplat X erstellt haben, um eine Standort-Trigger or triggern-Aktion festzulegen.

![Einrichtung einer aktionsbasierten Kampagne in Braze mit einem angepassten loplat-Event als Trigger.]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})