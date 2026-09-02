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

Legen Sie einen Volumen- oder Prozentschwellenwert für Nutzer:innen-Eintritte oder gesendete Nachrichten fest, und Braze benachrichtigt Sie per E-Mail oder Webhook, wenn dieser Schwellenwert überschritten wird. Sie können auch mehrere Benachrichtigungen für denselben Canvas erstellen – zum Beispiel eine Benachrichtigung für Nutzer:innen-Eintritte und eine weitere für gesendete Nachrichten.

Sie wissen nicht, wo Sie anfangen sollen? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) kann Sie durch die Einrichtung einer Canvas-Schwellenwert-Benachrichtigung führen.

## Schritt 1: Einen Alert erstellen {#step-1-create-an-alert}

Alerts werden auf Canvas-Ebene festgelegt, und Sie können sie sowohl für aktive als auch für Entwurfs-Canvase konfigurieren. Um die Seite **Alerts verwalten** für ein Canvas zu öffnen, haben Sie zwei Möglichkeiten:

- Gehen Sie zu **Messaging** > **Canvas** und wählen Sie im Kontextmenü eines einzelnen Canvas **Alerts verwalten** aus.
- Öffnen Sie bei aktiven Canvase **Canvas Analytics** und wählen Sie **Alerts verwalten** aus.

Wählen Sie auf der Seite **Alerts verwalten** die Option **Alert konfigurieren** aus, um einen neuen Alert zu erstellen.

## Schritt 2: Benennen Sie Ihren Alert und wählen Sie einen Canvas aus {#step-2-name-your-alert-and-select-a-canvas}

Geben Sie Ihrem Alert einen Namen und bestätigen Sie den Canvas, für den er gelten soll.

![Das Panel „Alert konfigurieren“ mit den Feldern für den Alert-Namen und den Canvas-Namen, einer leeren Regelgruppe und einer Zusammenfassungs-Seitenleiste für Alert-Regeln, Zeitplan und Benachrichtigungen.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Schritt 3: Warnregeln festlegen {#step-3-set-alert-rules}

Warnregeln definieren den Schwellenwert, der eine Benachrichtigung auslöst. Sie können Regeln anhand von zwei Metriken erstellen:

- **Nutzereintritte:** Anzahl der Nutzer:innen, die den Canvas betreten haben
- **Gesendete Nachrichten:** Anzahl der vom Canvas gesendeten Nachrichten

Wählen Sie für jede Regel einen Vergleich (kleiner als, größer als, kleiner oder gleich, größer oder gleich oder gleich), eine Einheit und einen Schwellenwert.

- **Volumen:** Vergleicht die absolute Anzahl im aktuellen Prüffenster. Zum Beispiel kennzeichnet „Nutzereintritte kleiner als 3.000“ einen Canvas, der normalerweise Tausende von Nutzer:innen erreicht, aber plötzlich stagniert – ein Hinweis auf ein vorgelagertes Zielgruppen- oder Entry-Problem, das untersucht werden sollte.
- **Prozentsatz:** Vergleicht die aktuelle Anzahl mit einem Referenzwert für diesen Canvas. Der Referenzwert ist der Durchschnitt desselben Zeitfensters über die vorherigen 7 Tage. Wenn die Warnung beispielsweise alle 3 Stunden prüft, vergleicht eine Prüfung um 14–17 Uhr den Wert mit dem Durchschnitt der vorherigen sieben 14–17-Uhr-Fenster. Eine Regel für „Gesendete Nachrichten kleiner als 50 %“ kennzeichnet einen Rückgang auf unter die Hälfte des üblichen Volumens.

Schwellenwerte sind ganze Zahlen. Für Prozentregeln mit **kleiner als** oder **kleiner oder gleich** geben Sie einen Wert von 1 bis 100 ein. Für **größer als**, **größer oder gleich** oder **gleich** kann der Prozentsatz 0 oder höher sein, einschließlich Werten über 100, sodass Sie bei einem Anstieg im Vergleich zum Referenzwert eine Warnung auslösen können.

Sie können mehrere Regeln zusammenfassen – einschließlich einer Kombination aus Volumen- und Prozentregeln – und Regelgruppen mit UND- oder ODER-Logik verknüpfen, um spezifischere Warnbedingungen zu erstellen.

## Schritt 4: Zeitplan für Benachrichtigungen festlegen {#step-4-set-the-alert-schedule}

Legen Sie fest, wie oft Ihre Benachrichtigungsregeln überprüft werden. Sie können die Prüfhäufigkeit auf einen Wert zwischen 3 und 12 Stunden (in Schritten von 1 Stunde) oder auf alle 24 Stunden einstellen. Sobald eine Benachrichtigung aktiviert ist, wird sie nach diesem Zeitplan so lange geprüft, wie die Benachrichtigung und der zugehörige Canvas aktiv sind.

## Schritt 5: Benachrichtigungen einrichten {#step-5-set-up-notifications}

Legen Sie fest, wer benachrichtigt werden soll, wenn eine Alarmregel ausgelöst wird, und auf welchem Weg:

- **E-Mail:** Fügen Sie eine oder mehrere E-Mail-Adressen der Empfänger:innen hinzu
- **Webhook:** Geben Sie die Webhook-URL für die Benachrichtigung ein und fügen Sie optional angepasste Anfrage-Header hinzu, die von Ihrem Webhook-Ziel benötigt werden

Sie können eine oder beide Benachrichtigungsmethoden für einen einzelnen Alarm aktivieren.

Webhook-Benachrichtigungen sind nützlich, um Benachrichtigungen an externe Plattformen weiterzuleiten, z. B. an einen Slack-Kanal – weitere Informationen finden Sie in der Slack-Dokumentation zum [Senden von Nachrichten über eingehende Webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Jede Webhook-Benachrichtigung sendet einen JSON-Payload mit dem Alarmnamen, dem Auswertungszeitraum und den Bedingungen, die den Alarm ausgelöst haben. Jede Bedingung enthält eine `threshold_unit` mit dem Wert `volume` oder `percentage`. Prozentuale Bedingungen enthalten zusätzlich `percentage_metric_value` (die beobachtete Anzahl als ganzzahliger Prozentsatz der Baseline). `metric_value` ist immer die absolute Anzahl.

### Beispiel für einen Webhook-Payload {#example-webhook-payload}

Das Folgende ist ein Beispiel für den JSON-Payload, der bei einem POST-Request an Ihren Webhook-Endpunkt gesendet wird, wenn ein Alarm ausgelöst wird. Die erste Bedingung ist eine Volumenregel. Die zweite ist eine Prozentregel: 51.235 gesendete Nachrichten, was 57 % der Baseline im selben Zeitfenster der letzten 7 Tage entspricht, bei einem Schwellenwert von mehr als 55 %.

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
      "group_index": 0,
      "threshold_unit": "volume"
    },
    {
      "subject": "messages_sent",
      "operator": "gt",
      "threshold_value": 55,
      "metric_value": 51235.0,
      "group_index": 0,
      "threshold_unit": "percentage",
      "percentage_metric_value": 57
    }
  ]
}
```

## Schritt 6: Benachrichtigung speichern {#step-6-save-your-alert}

Überprüfen Sie Ihre Benachrichtigungsregeln, den Zeitplan und die Benachrichtigungseinstellungen im Zusammenfassungs-Panel und wählen Sie dann **Save alert** aus.

## Schritt 7: Benachrichtigung aktivieren {#step-7-activate-the-alert}

Durch das Speichern einer Benachrichtigung wird diese nicht aktiviert. Um sie einzuschalten, gehen Sie zur Seite **Benachrichtigungen verwalten** und verwenden Sie den **Status**-Schalter für Ihre Benachrichtigung. Eine Benachrichtigung bleibt aktiv, bis Sie sie deaktivieren oder bis der zugehörige Canvas nicht mehr aktiv ist. Die Spalte **Konfigurierte Benachrichtigungen** auf der **Canvas**-Seite zeigt ein Glockensymbol für jeden Canvas mit mindestens einer gespeicherten Benachrichtigung an.

## Überlegungen {#considerations}

- **Canvase im Entwurf:** Sie können eine Schwellenwert-Benachrichtigung für ein Canvas einrichten, das sich noch im Entwurf befindet, aber die Benachrichtigung beginnt erst dann mit der Überprüfung Ihrer Regeln, wenn das Canvas gestartet wird.
- **Prozentuale Basislinie:** Prozentuale Regeln benötigen sieben vollständige vorherige Zeitfenster desselben Typs nach dem Start des Canvas. Solange diese Zeitfenster nicht vorhanden sind oder die durchschnittliche Basislinie null beträgt (keine Aktivität in den vorherigen Zeitfenstern), lösen prozentuale Regeln keine Benachrichtigung aus.