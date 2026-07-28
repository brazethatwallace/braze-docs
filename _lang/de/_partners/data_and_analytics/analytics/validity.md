---
nav_title: Validity
article_title: Validity
alias: /partners/validity/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Validity, einer Plattform für E-Mail-Zustellbarkeit, die Everest-Seed-Listen mit Braze synchronisiert und Inbox-Placement-Tests für Campaigns und Canvases automatisiert."
page_type: partner
search_tag: Partner
---

# Validity

> [Validity Everest](https://www.validity.com/everest/) ist eine Plattform für E-Mail-Zustellbarkeit, die Ihnen hilft, das Inbox-Placement zu messen und Ihre Absenderreputation zu schützen. Die Integration von Braze und Validity synchronisiert Ihre Everest-Seed-Liste mit Braze, führt automatisch Seedings für qualifizierende Campaigns und Canvases durch und überträgt Engagement-Metriken zurück in Validity Inbox, damit Sie das Seed-basierte Placement mit dem tatsächlichen Abonnent:innen-Engagement vergleichen können.

_Diese Integration wird von Validity gepflegt._

## Über die Integration {#about-the-integration}

Validity erstellt und pflegt E-Mail-Seed-List-Nutzer:innen in Braze, damit Seed-Adressen aktiv und nicht unterdrückt bleiben. Wenn eine Campaign oder ein Canvas für das Seeding bereit ist, sendet Validity eine Kopie an diese Seed-Liste und zeigt Engagement-Metriken – zugestellt, Bounces, Öffnungen, Klicks und Abmeldungen – in Validity Inbox zusammen mit den Inbox-Placement-Daten an.

## Anwendungsfälle {#use-cases}

### Auto-Seeding

Mit dem Auto-Seeding von Validity erkennt Validity, wenn eine Braze-Campaign oder ein Canvas ein qualifizierendes Sendevolumen erreicht, und sendet eine Kopie des Campaign-Inhalts an Ihre Validity-Seed-Liste. Seed-Sends richten sich an Nutzer:innen, bei denen das angepasste Attribut `validity_seed` auf `true` gesetzt ist.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| ----------- | ----------- |
| Ein Validity-Konto | Ein Validity-Konto ist erforderlich, um diese Partnerschaft zu nutzen. |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den folgenden Berechtigungen: `users.track`, `users.delete`, `email.bounce.remove`, `email.spam.remove`, `campaigns.list`, `campaigns.details`, `campaigns.data_series`, `canvas.list`, `canvas.details`, `canvas.data_series`, `content_blocks.list`, `content_blocks.info` und `messages.send`. <br><br> Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner**. |
| Ein Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. Zum Beispiel `rest.iad-01.braze.com`. |
| Ein Braze-App-Bezeichner | Der Braze-App-Bezeichner, dem Seed-Sends zugeordnet werden sollen. Sie finden ihn unter **Einstellungen** > **APIs und Bezeichner** > **App-Bezeichner**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Validity integrieren {#integrating-validity}

### Schritt 1: Braze-Zugangsdaten mit Validity teilen {#step-1-share-braze-credentials-with-validity}

Validity benötigt drei Zugangsdaten aus **Einstellungen** > **APIs und Bezeichner** in Ihrem Braze-Dashboard:

- Ihren REST-API-Schlüssel (mit den unter [Voraussetzungen](#prerequisites) aufgeführten Berechtigungen)
- Ihren REST-Endpunkt
- Ihren App-Bezeichner

Teilen Sie diese Zugangsdaten mit Ihrer Validity-Vertretung, die die Einrichtung der Integration für Sie abschließt. Validity validiert die Zugangsdaten mit einem Live-Testaufruf an Braze, bevor die Integration aktiviert wird. Wenn Sie nicht sicher sind, wer Ihre Validity-Kontaktperson ist, senden Sie eine E-Mail an [support@validity.com](mailto:support@validity.com).

Nachdem die Integration aktiviert wurde, synchronisiert Validity Ihre Everest-Seed-Liste in einem wiederkehrenden Zyklus (alle 10 Minuten) mit Braze. Validity erstellt, aktualisiert und entfernt Seed-Nutzer:innen in Braze, um sie mit Ihrer aktuellen Seed-Liste in Everest abzugleichen.

### Schritt 2: Optional ein Braze-Segment für Validity-Seed-Nutzer:innen erstellen {#step-2-optionally-create-a-braze-segment-for-validity-seed-users}

Das Erstellen eines Segments ist optional. Auto-Seeding sendet Test-E-Mails über ein [Connected-Audience]({{site.baseurl}}/api/objects_filters/connected_audience)-Objekt, das nach dem angepassten Attribut `validity_seed` gefiltert wird, sobald ein qualifizierender Send erkannt wird. Sie müssen kein Segment erstellen oder es Ihren Campaigns zuordnen.

Wenn Sie diese Zielgruppe in Braze als Referenz anzeigen möchten, erstellen Sie ein Segment unter **Zielgruppe** > **Segmente** mit dem Filter `validity_seed` ist `true`.

Validity erstellt Nutzer:innen über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt mit folgendem Schema:

```bash
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
  -d '{
    "attributes": [
      {
        "email": "example1@example.com",
        "validity_seed": true
      },
      {
        "email": "example2@example.com",
        "validity_seed": true
      }
    ],
    "events": [
      {
        "email": "example1@example.com",
        "name": "validity_seed_event",
        "time": "2026-07-02T18:00:00.000Z"
      }
    ]
  }'
```

Diese Nutzer:innen enthalten immer das angepasste Attribut `validity_seed` mit dem booleschen Wert `true`. Validity sendet außerdem ein angepasstes Event `validity_seed_event` für jede:n Seed-Nutzer:in, damit diese als aktive Nutzer:innen in Ihrem Braze-Konto registriert werden.

## Hinweise {#considerations}

### Wie Seed-Sends funktionieren {#how-seed-sends-work}

Validity ruft den Campaign-Body, den Betreff und die Absenderadresse über die Campaign- und Canvas-Detail-Endpunkte ab und liefert dann eine Kopie dieses Inhalts über den Braze-Endpunkt [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) an die Seed-Liste. Ihr Braze-Dashboard zeigt weiterhin nur die ursprüngliche Campaign an.

### Auto-Seeding-Schwellenwert {#auto-seeding-threshold}

Validity erkennt, wenn eine Campaign oder ein Canvas Ihren konfigurierten Sendevolumen-Schwellenwert überschreitet (standardmäßig 10.000 Sends), und sendet den Seed-Test zu diesem Zeitpunkt. Sie müssen die Seed-Zielgruppe nicht zu Ihren Campaigns oder Canvases hinzufügen.

Ein Seed-Test sendet Ihre E-Mail-Campaign an die Adressen auf der Seed-Liste, sammelt Placement-Daten und hilft Ihnen, Probleme vor oder parallel zu Sends an Ihre Zielgruppe zu identifizieren. Inbox-Placement-Metriken zeigen, ob Ihre Campaign im Posteingang oder im Spam-Ordner landet oder verloren geht. Nutzen Sie diese Metriken, um das Inbox-Placement zu bestätigen und Zustellbarkeitsprobleme zu erkennen.

Seed-Tests können Ihnen auch helfen zu diagnostizieren, warum E-Mails im Spam-Ordner landen oder verloren gehen. Die Überprüfung von Header-Daten, Authentifizierung (SPF, DKIM und DMARC), Link-Validierung und Design-Rendering kann aufzeigen, welche Schritte Sie unternehmen sollten, um Ihre Inbox-Placement-Rate zu verbessern.

### Seed-Listen-Zustand {#seed-list-health}

Validity überwacht Seed-Listen-Nutzer:innen und kann sie aktualisieren oder entfernen, wenn sie an Effektivität verlieren – zum Beispiel, wenn E-Mail-Anbieter (ESPs) beginnen, Mitglieder der Seed-Listen-Zielgruppe als Spam zu markieren. Diese Berechtigungen ermöglichen es Validity, den Zustand der Seed-Liste zu überwachen und die Liste entsprechend zu aktualisieren.

### Umgang mit dynamischem Content {#how-dynamic-content-is-handled}

Braze-E-Mails verwenden häufig Liquid-Personalisierung, die an das Profil einer echten Empfängerin oder eines echten Empfängers gebunden ist. Da Seed-Adressen diese Profildaten nicht haben, lässt Validity jede E-Mail vor dem Seeding durch einen Sanitizer laufen. Der Sanitizer löst Content Blocks auf, wertet grundlegende Liquid-Logik aus und ersetzt alles, was er nicht auflösen kann (z. B. einen Vornamen), durch einen sichtbaren `[REDACTED]`-Platzhalter. Abschnitte, die vollständig aus Live-Connected-Content-APIs aufgebaut sind, werden im Seed leer dargestellt.

Sie können den Sanitizer ein- oder ausschalten. Wenn er ausgeschaltet ist, löst Braze die Liquid-Personalisierung für Seed-Sends genauso auf wie für echte Empfänger:innen.

### Inbox-Aggregat

Die Aktivierung von Auto-Seeding aktiviert auch Inbox Aggregate. Dieses Feature ruft Engagement-Metriken – gesendet, zugestellt, Bounces, Öffnungen, Klicks und Abmeldungen – aus Ihren echten Braze-Sends (getrennt von Seed-Sends) ab und zeigt sie in Validity Inbox zusammen mit Ihren Inbox-Placement-Daten an. Die beiden Features laufen auf unabhängigen Zeitplänen und müssen nicht separat verwaltet werden.