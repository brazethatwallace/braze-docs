---
nav_title: Notify
article_title: Notify
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Notify, einer Realtime-Omnichannel-Personalisierungslösung, die Personalisierung über den gesamten Kundenlebenszyklus bietet."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/) ist eine KI-gesteuerte Softwarelösung, die sich nahtlos in Management-Tools für Kundenbeziehungen integrieren lässt, um Marketing-Strategien zu verbessern und das Engagement über mehrere Kanäle hinweg zu fördern.

Die Integration von Braze und Notify ermöglicht es Marketern, das Engagement über verschiedene Plattformen hinweg effektiv zu steigern. Anstatt sich auf traditionelle Marketing-Methoden zu verlassen, kann eine durch die Braze API getriggerte Campaign die Funktionen von Notify nutzen, um personalisierte Nachrichten über mehrere Kanäle zuzustellen, darunter E-Mail, SMS, Push-Benachrichtigungen und mehr.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `users.export.segment` und `campaigns.trigger.send`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| CNAME-Konfiguration | Für das Tracking-Pixel, das in der E-Mail für Notify verwendet wird, um das Engagement der Nutzer:innen beim Messaging zu verfolgen und das Modell weiter zu informieren, muss eine Subdomain erstellt werden. Geben Sie die URL der Subdomain nach ihrer Erstellung an Notify weiter. |
| Datenbank-Opt-in-Export | Senden Sie die Campaign- und Kaufdaten des vergangenen Jahres (12 Monate) an Notify. ​Dieser Export wird verwendet, um das Vorhersagemodell von Notify zu trainieren. <br><br> **Felder:** <br><br> **E-Mail:** Ein SHA256-Hash der E-Mail, konvertiert in Kleinbuchstaben und ohne führende oder nachfolgende Leerzeichen.<br><br>**Segment:** Die Segmentinformationen, die den Grad der Aktivität (aktiv oder inaktiv) definieren.<br><br>**Untersegment:** Alle weiteren relevanten Aktivitätsinformationen, wie z. B. die Höhe der Kaufaktivität.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Campaign erstellen {#step-1-create-your-campaign}

Erstellen Sie eine [API-getriggerte Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) in Braze. Teilen Sie dann den `api_identifier` der Campaign mit Notify.

### 2. Schritt: Segment in Braze erstellen {#step-2-create-your-segment-in-braze}

Erstellen Sie als Nächstes das Segment der Nutzer:innen, die Sie mit der in [Schritt 1](#step-1-create-your-campaign) erstellten Campaign ansprechen möchten. Teilen Sie dann die Segment-ID mit Notify.

### 3. Schritt: Segment abrufen {#step-3-fetch-your-segment}

Anschließend exportiert Notify die Nutzer:innen des Segments, das der Campaign zugeordnet ist.

### 4. Schritt: Notify triggert die Campaign {#step-4-notify-triggers-the-campaign}

Über den Endpunkt `/campaigns/trigger/send` triggert die KI von Notify die in [Schritt 1](#step-1-create-your-campaign) erstellte Braze-Campaign, um sie zu dem Zeitpunkt an die Nutzer:innen zu senden, zu dem diese sich am ehesten engagieren.