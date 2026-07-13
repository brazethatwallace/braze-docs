---
nav_title: WSC Sports
article_title: WSC Sports
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und WSC Sports, einer Plattform für Sportvideos, die es Ihnen ermöglicht, reichhaltige und robuste Sportmedien in Ihre Braze-Push-Benachrichtigungen einzubinden."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> Die [WSC Sports-Plattform](https://wsc-sports.com/) generiert personalisierte Sportvideos für jede digitale Plattform und jeden Sportfan – automatisch und in Realtime.

_Diese Integration wird von WSC Sports gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und WSC Sports ermöglicht es Ihnen, reichhaltige und robuste Sportmedien in Ihre Braze-Push-Benachrichtigungen einzubinden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| WSC-Konto | Um diese Partnerschaft zu nutzen, ist ein WSC-Konto erforderlich. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit Berechtigungen für **Nachrichten**, **Segmente**, **Kampagnen** und **Canvas**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die WSC Sports-Anwendung übernimmt den End-to-End-Prozess, von der Auswahl des Videos bis zum Eintreffen der Push-Benachrichtigung auf dem Gerät der Endnutzer:innen.

### Schritt 1: Sendeeinstellungen auswählen {#step-1-select-send-settings}

![WSC Sports Sendeeinstellungen-Panel mit Braze-Campaign- und Segment-Auswahl.]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Bevor Sie mit der Integration beginnen, stellen Sie sicher, dass Sie die gewünschten Campaigns und Nutzersegmente in Braze erstellt haben. Wählen Sie anschließend in der WSC Sports-Plattform das gewünschte Video aus und wählen Sie in den Sendeeinstellungen das Braze-Nutzersegment und die Campaign-ID, die Sie verwenden möchten. Wählen Sie abschließend den Zeitpunkt, zu dem Ihre Push-Nachricht versendet werden soll.

#### API-Aufruf {#api-call}

Nach dem Versand stellt WSC Sports die Push-Benachrichtigung an die ausgewählten Nutzersegmente über die folgenden Braze-Endpunkte zu, basierend auf den ausgewählten Optionen:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

Der resultierende Nachrichtentext sieht wie folgt aus:
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Schritt 2: Testversand {#step-2-test-send}

Zu diesem Zeitpunkt sollte Ihre Campaign bereit zum Testen und Versenden sein. Prüfen Sie die Braze-Fehlermeldungsprotokolle, falls Fehler auftreten.