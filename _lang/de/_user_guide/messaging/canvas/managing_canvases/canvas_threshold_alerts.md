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

## Schritt 1: Eine Benachrichtigung erstellen {#step-1-create-an-alert}

Benachrichtigungen werden auf Canvas-Ebene festgelegt. Sie können sie sowohl für aktive als auch für Entwurfs-Canvases konfigurieren. Um die Seite **Benachrichtigungen verwalten** für ein Canvas zu öffnen, haben Sie zwei Möglichkeiten:

- Gehen Sie zu **Messaging** > **Canvas** und wählen Sie **Benachrichtigungen verwalten** aus dem Kontextmenü eines einzelnen Canvas aus.
- Öffnen Sie bei aktiven Canvases **Canvas Analytics** und wählen Sie **Benachrichtigungen verwalten** aus.

Wählen Sie auf der Seite **Benachrichtigungen verwalten** die Option **Benachrichtigung konfigurieren** aus, um eine neue Benachrichtigung zu erstellen.

## Schritt 2: Benennen Sie Ihre Benachrichtigung und wählen Sie einen Canvas aus {#step-2-name-your-alert-and-select-a-canvas}

Geben Sie Ihrer Benachrichtigung einen Namen und bestätigen Sie den Canvas, für den sie gilt.

![Das Panel „Benachrichtigung konfigurieren“ mit den Feldern für den Benachrichtigungsnamen und den Canvas-Namen, einer leeren Regelgruppe und einer Zusammenfassungs-Seitenleiste für Benachrichtigungsregeln, Zeitplan und Benachrichtigungen.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Schritt 3: Alarmregeln festlegen {#step-3-set-alert-rules}

Alarmregeln definieren den Schwellenwert, der eine Benachrichtigung auslöst. Sie können Regeln mit zwei Metriken erstellen:

- **Nutzer:innen-Eintritte:** Anzahl der Nutzer:innen, die den Canvas betreten haben
- **Gesendete Nachrichten:** Anzahl der vom Canvas gesendeten Nachrichten

Wählen Sie für jede Regel einen Vergleich (kleiner als, größer als, kleiner oder gleich, größer oder gleich oder gleich), eine Einheit und einen Schwellenwert.

- **Volumen:** Vergleicht die absolute Anzahl im aktuellen Prüffenster. Beispiel: „Nutzer:innen-Eintritte kleiner als 3.000“ markiert einen Canvas, der normalerweise Tausende von Nutzer:innen erreicht, aber plötzlich stagniert – ein Hinweis auf ein vorgelagertes Zielgruppen- oder Entry-Problem, das untersucht werden sollte.
- **Prozentsatz:** Vergleicht die aktuelle Anzahl mit einem Referenzwert für diesen Canvas. Der Referenzwert ist der Durchschnitt desselben Zeitfensters über die letzten 7 Tage. Wenn der Alarm beispielsweise alle 3 Stunden prüft, vergleicht eine Prüfung von 14–17 Uhr den Wert mit dem Durchschnitt der vorherigen sieben 14–17-Uhr-Fenster. Eine Regel für „Gesendete Nachrichten kleiner als 50 %“ markiert einen Rückgang auf weniger als die Hälfte des üblichen Volumens.

Schwellenwerte sind ganze Zahlen. Geben Sie bei Prozentsatzregeln mit **kleiner als** oder **kleiner oder gleich** einen Wert von 1 bis 100 ein. Bei **größer als**, **größer oder gleich** oder **gleich** kann der Prozentsatz 0 oder höher sein, einschließlich Werten über 100, sodass Sie bei einem Anstieg im Vergleich zum Referenzwert alarmiert werden können.

Sie können mehrere Regeln gruppieren – einschließlich einer Mischung aus Volumen- und Prozentsatzregeln – und Regelgruppen mit UND- oder ODER-Logik kombinieren, um spezifischere Alarmbedingungen zu erstellen.

## Schritt 4: Zeitplan für die Benachrichtigung festlegen {#step-4-set-the-alert-schedule}

Legen Sie fest, wie oft Ihre Benachrichtigungsregeln überprüft werden. Sie können die Prüfhäufigkeit auf einen Wert zwischen 3 und 12 Stunden (in 1-Stunden-Schritten) oder auf alle 24 Stunden einstellen. Nach der Aktivierung wird die Benachrichtigung so lange in diesem Zeitplan überprüft, wie die Benachrichtigung und der zugehörige Canvas aktiv sind.

## Schritt 5: Benachrichtigungen einrichten {#step-5-set-up-notifications}

Legen Sie fest, wer benachrichtigt werden soll, wenn eine Alarmregel ausgelöst wird, und auf welchem Weg:

- **E-Mail:** Fügen Sie eine oder mehrere E-Mail-Adressen der Empfänger:innen hinzu
- **Webhook:** Geben Sie die Webhook-URL für die Benachrichtigung ein und fügen Sie optional angepasste Anfrage-Header hinzu, die Ihr Webhook-Ziel erfordert

Sie können eine oder beide Benachrichtigungsmethoden für einen einzelnen Alarm aktivieren.

Webhook-Alarme eignen sich, um Benachrichtigungen an externe Plattformen wie einen Slack-Kanal weiterzuleiten – weitere Informationen finden Sie in der Slack-Dokumentation zum [Senden von Nachrichten über eingehende Webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Jede Webhook-Benachrichtigung sendet einen JSON-Payload mit dem Alarmnamen, dem Auswertungszeitraum und den Bedingungen, die den Alarm ausgelöst haben. Jede Bedingung enthält eine `threshold_unit` mit dem Wert `volume` oder `percentage`. Prozentuale Bedingungen enthalten zusätzlich `percentage_metric_value` (die beobachtete Anzahl als ganzzahliger Prozentwert der Baseline). `metric_value` ist immer die absolute Anzahl.

### Beispiel eines Webhook-Payloads {#example-webhook-payload}

Das Folgende ist ein Beispiel für den JSON-Payload, der in einer POST-Anfrage an Ihren Webhook-Endpunkt gesendet wird, wenn ein Alarm ausgelöst wird. Die erste Bedingung ist eine Volumenregel. Die zweite ist eine Prozentregel: 51.235 gesendete Nachrichten, was 57 % der 7-Tage-Baseline im gleichen Zeitfenster entspricht, gemessen an einem Schwellenwert von mehr als 55 %.

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

Das Speichern einer Benachrichtigung aktiviert sie nicht. Um sie einzuschalten, gehen Sie zur Seite **Benachrichtigungen verwalten** und verwenden Sie den **Status**-Schalter für Ihre Benachrichtigung. Eine Benachrichtigung bleibt aktiv, bis Sie sie deaktivieren oder bis der zugehörige Canvas nicht mehr aktiv ist. Die Spalte **Konfigurierte Benachrichtigungen** auf der **Canvas**-Seite zeigt ein Glockensymbol für jeden Canvas mit mindestens einer gespeicherten Benachrichtigung an.

## Überlegungen {#considerations}

- **Canvases im Entwurf:** Sie können eine Schwellenwert-Benachrichtigung für ein Canvas einrichten, das sich noch im Entwurf befindet, aber die Benachrichtigung beginnt erst dann mit der Überprüfung Ihrer Regeln, wenn das Canvas gestartet wird.
- **Prozentuale Basislinie:** Prozentuale Regeln benötigen sieben vollständige vorherige Zeitfenster desselben Typs nach dem Start des Canvas. Solange diese Zeitfenster nicht vorhanden sind oder der Basislinie-Durchschnitt null beträgt (keine Aktivität in diesen vorherigen Zeitfenstern), lösen prozentuale Regeln keine Benachrichtigung aus.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Zählen Canvas-Schwellenwert-Benachrichtigungen zum Webhook-Verbrauch? {#do-canvas-threshold-alerts-count-toward-webhook-usage}

Nein. Canvas-Schwellenwert-Benachrichtigungen werden nicht auf Webhook-Rate-Limits oder Nutzungsmetriken angerechnet.