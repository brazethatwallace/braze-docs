---
nav_title: Canvas-Benachrichtigungen
article_title: Canvas-Schwellenwert-Benachrichtigungen
page_order: 4
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Schwellenwert-Benachrichtigungen für einen Canvas einrichten, damit Sie proaktiv informiert werden, wenn Nutzer:innen-Eintritte oder gesendete Nachrichten außerhalb Ihres erwarteten Bereichs liegen."
tool: Canvas
channel:
- email
- webhooks
---

# Canvas-Schwellenwert-Benachrichtigungen {#canvas-threshold-alerts}

> Canvas-Schwellenwert-Benachrichtigungen informieren Sie, wenn etwas in einem Canvas nicht wie geplant läuft, sodass Sie eine ins Stocken geratene Journey oder einen unerwarteten Abfall erkennen können, bevor Ihre Kund:innen davon betroffen sind.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

Legen Sie einen Volumenschwellenwert für Nutzer:innen-Eintritte oder gesendete Nachrichten fest, und Braze benachrichtigt Sie per E-Mail oder Webhook, wenn dieser Schwellenwert überschritten wird. Sie können auch mehrere Benachrichtigungen für denselben Canvas erstellen – zum Beispiel eine Benachrichtigung für Nutzer:innen-Eintritte und eine weitere für gesendete Nachrichten.

Sie wissen nicht, wo Sie anfangen sollen? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) kann Sie durch die Einrichtung einer Canvas-Schwellenwert-Benachrichtigung führen.

## Schritt 1: Eine Benachrichtigung erstellen {#step-1-create-an-alert}

Benachrichtigungen werden auf Canvas-Ebene festgelegt, und Sie können sie sowohl für aktive als auch für Entwurfs-Canvases konfigurieren. Um die Seite **Benachrichtigungen verwalten** für ein Canvas zu öffnen, haben Sie zwei Möglichkeiten:

- Gehen Sie zu **Messaging** > **Canvas** und wählen Sie **Benachrichtigungen verwalten** aus dem Kontextmenü eines einzelnen Canvas aus.
- Öffnen Sie bei aktiven Canvases **Canvas Analytics** und wählen Sie **Benachrichtigungen verwalten** aus.

Wählen Sie auf der Seite **Benachrichtigungen verwalten** die Option **Benachrichtigung konfigurieren** aus, um eine neue Benachrichtigung zu erstellen.

## Schritt 2: Benennen Sie Ihren Alert und wählen Sie einen Canvas aus {#step-2-name-your-alert-and-select-a-canvas}

Geben Sie Ihrem Alert einen Namen und bestätigen Sie den Canvas, für den er gelten soll.

![Das Panel „Alert konfigurieren“ mit den Feldern für den Alert-Namen und den Canvas-Namen, einer leeren Regelgruppe und einer Zusammenfassungs-Seitenleiste für Alert-Regeln, Zeitplan und Benachrichtigungen.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Schritt 3: Alarmregeln festlegen {#step-3-set-alert-rules}

Alarmregeln definieren den Schwellenwert, der eine Benachrichtigung auslöst. Sie können Regeln mit zwei Metriken erstellen:

- **Nutzer:innen-Eintritte:** Anzahl der Nutzer:innen, die den Canvas betreten haben
- **Gesendete Nachrichten:** Anzahl der vom Canvas gesendeten Nachrichten

Wählen Sie für jede Regel einen Vergleich (kleiner als, größer als, kleiner oder gleich, größer oder gleich oder gleich) und einen Volumenschwellenwert. Zum Beispiel kennzeichnet eine Regel wie „Nutzer:innen-Eintritte kleiner als 3.000“ einen Canvas, der normalerweise Tausende von Nutzer:innen erreicht, aber plötzlich ins Stocken geraten ist – ein Hinweis auf ein vorgelagertes Zielgruppen- oder Entry-Problem, das untersucht werden sollte.

Sie können mehrere Regeln gruppieren und Regelgruppen mit UND- oder ODER-Logik kombinieren, um spezifischere Alarmbedingungen zu erstellen.

## Schritt 4: Zeitplan für Benachrichtigungen festlegen {#step-4-set-the-alert-schedule}

Legen Sie fest, wie oft Ihre Benachrichtigungsregeln überprüft werden. Sie können die Prüfhäufigkeit auf einen Wert zwischen 3 und 12 Stunden (in 1-Stunden-Schritten) oder auf alle 24 Stunden einstellen. Nach der Aktivierung wird eine Benachrichtigung so lange in diesem Zeitplan überprüft, wie die Benachrichtigung und der zugehörige Canvas aktiv sind.

## Schritt 5: Benachrichtigungen einrichten {#step-5-set-up-notifications}

Wählen Sie aus, wer benachrichtigt werden soll, wenn eine Alarmregel erfüllt ist, und auf welchem Weg:

- **E-Mail:** Fügen Sie eine oder mehrere E-Mail-Adressen der Empfänger:innen hinzu
- **Webhook:** Geben Sie die Webhook-URL für die Benachrichtigung ein und fügen Sie optional angepasste Anfrage-Header hinzu, die von Ihrem Webhook-Ziel benötigt werden

Sie können eine oder beide Benachrichtigungsmethoden für einen einzelnen Alarm aktivieren.

![Der Abschnitt „Benachrichtigungen“ im Panel „Alarm konfigurieren“ mit E-Mail- und Webhook-Umschaltern, einem Feld für E-Mail-Empfänger:innen, einem Webhook-URL-Feld, einem Hinweis zum Payload-Inhalt und optionalen Anfrage-Header-Feldern.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Webhook-Alarme sind nützlich, um Benachrichtigungen an externe Plattformen weiterzuleiten, z. B. an einen Slack-Kanal – weitere Informationen finden Sie in der Slack-Dokumentation zum [Senden von Nachrichten über eingehende Webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Jede Webhook-Benachrichtigung sendet einen JSON-Payload mit dem Alarmnamen, dem Auswertungszeitraum und den Bedingungen, die den Alarm ausgelöst haben.

### Beispiel-Webhook-Payload {#example-webhook-payload}

Das Folgende ist ein Beispiel für den JSON-Payload, der in einer POST-Anfrage an Ihren Webhook-Endpunkt gesendet wird, wenn ein Alarm ausgelöst wird:

```json
{
  "alert": {
    "name": "Canvas Alert - August 6, 2026",
    "target_type": "CANVAS"
  },
  "evaluation_window_start": "2026-08-06T10:28:01Z",
  "evaluation_window_end": "2026-08-06T13:28:01Z",
  "conditions": [
    {
      "subject": "user_entries",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    },
    {
      "subject": "messages_sent",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    }
  ]
}
```

## Schritt 6: Benachrichtigung speichern {#step-6-save-your-alert}

Überprüfen Sie Ihre Benachrichtigungsregeln, den Zeitplan und die Benachrichtigungseinstellungen im Zusammenfassungs-Panel und wählen Sie dann **Save alert** aus.

## Schritt 7: Benachrichtigung aktivieren {#step-7-activate-the-alert}

Durch das Speichern einer Benachrichtigung wird diese nicht aktiviert. Um sie einzuschalten, gehen Sie zur Seite **Benachrichtigungen verwalten** und verwenden Sie den **Status**-Schalter für Ihre Benachrichtigung. Eine Benachrichtigung bleibt aktiv, bis Sie sie deaktivieren oder bis der zugehörige Canvas nicht mehr aktiv ist. Die Spalte **Konfigurierte Benachrichtigungen** auf der **Canvas**-Seite zeigt ein Glockensymbol für jeden Canvas mit mindestens einer gespeicherten Benachrichtigung an.

## Überlegungen {#considerations}

- **Canvases im Entwurf:** Sie können eine Schwellenwert-Benachrichtigung für ein Canvas einrichten, das sich noch im Entwurf befindet. Die Benachrichtigung beginnt jedoch erst dann mit der Überprüfung Ihrer Regeln, wenn das Canvas gestartet wird.