---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Bluedot, einer Standort-Plattform, die eine genaue und unkomplizierte Geofencing-Plattform für Ihre Apps bietet."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) ist eine Standort-Plattform, die eine genaue und unkomplizierte Geofencing-Plattform für Ihre Apps bietet. Nutzen Sie das SDK von Bluedot, um Nachrichten intelligenter zu gestalten, mobile Bestellvorgänge zu automatisieren, Arbeitsabläufe zu optimieren und reibungslose Erlebnisse zu schaffen.

_Diese Integration wird von Bluedot gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Bluedot erlaubt es Ihnen, die Geofence-Standortdienste von Bluedot zu nutzen, um Nutzer:innen-Events zu erstellen, die zum Aufbau von Journeys, Campaigns und zur Analyse des Kundenverhaltens und der Interessen verwendet werden können. Ereignisse (Eingang/Austritt), die von Nutzer:innen auf ihrem Gerät erzeugt werden, werden sofort mit allen relevanten Informationen an Braze gesendet.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Bluedot-Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein Bluedot-Konto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Anwendungsfälle {#use-cases}

Die von Bluedot bereitgestellten Standortinformationen zu angepassten Events können in Ihren Campaigns verwendet werden, um gängige Anwendungsfälle zu realisieren:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Quick Service Restaurant)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/)

## Integration

### Schritt 1: Erstellen Sie ein Bluedot-Projekt {#step-1-create-a-bluedot-project}
Richten Sie Ihr Bluedot-Konto ein und melden Sie sich bei Ihrem [Bluedot Canvas Dashboard](https://docs.bluedot.io/canvas/) an. Besuchen Sie die [Bluedot-Dokumentation](https://docs.bluedot.io/canvas/creating-a-new-project/), um zu erfahren, wie Sie ein neues Projekt erstellen können.

### Schritt 2: Integration der SDKs {#step-2-integrate-the-sdks}
Integrieren Sie das Bluedot Point SDK und das Braze SDK in Ihre App anhand der Schritte, die in der Dokumentation zur [Integration von Bluedot und Braze](https://docs.bluedot.io/integrations/braze-integration/) beschrieben sind.

### Schritt 3: Authentifizierung des Bluedot SDK {#step-3-authenticate-the-bluedot-sdk}
Verwenden Sie zur Authentifizierung des Bluedot Point SDK die in Schritt 1 erstellte `projectId`.

### Schritt 4: Verwenden Sie Bluedot-Ereignisse in Braze {#step-4-use-bluedot-events-in-braze}

#### Triggern von Nachrichten {#triggering-messages}

Sie können eine Push-Campaign oder ein Canvas einrichten, das auf Standort-Ereignisse reagiert, die vom Bluedot SDK generiert werden. Diese Integration ist ideal für Realtime-Messaging, wenn Nutzer:innen einen Standort oder einen Ort von Interesse betreten, oder für eine verzögerte Folgekommunikation, nachdem sie ihn verlassen haben.

Richten Sie in Braze eine aktionsbasierte Campaign ein, die Nachrichten auf der Grundlage eines bestimmten Standorts versendet. Verwenden Sie für Ihren Trigger ein angepasstes Event von `bluedot_entry` oder `bluedot_exit`, wie im folgenden Screenshot gezeigt:

![Eine aktionsbasierte Campaign im Zustellungsschritt. Hier haben Sie zwei Zeitplan-Optionen, die die Campaign senden, wenn Nutzer:innen ein angepasstes `bluedot_entry`- oder `bluedot_exit`-Event ausführen.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Targeting von Nutzer:innen {#targeting-users}

Stellen Sie sicher, dass Sie **Alle Nutzer:innen** für Ihren Workspace als Zielgruppe auswählen.
![Eine aktionsbasierte Campaign mit dem Schritt „Zielgruppe zusammenstellen“, in dem Sie aufgefordert werden, „Alle Nutzer:innen“ als gewünschtes Segment auszuwählen.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}