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

## Schritt 1: Benachrichtigung erstellen {#step-1-create-an-alert}

Benachrichtigungen werden auf Canvas-Ebene festgelegt, und Sie können sie sowohl für aktive als auch für Entwurfs-Canvases konfigurieren. Um die Seite **Benachrichtigungen verwalten** für einen Canvas zu öffnen, haben Sie zwei Möglichkeiten:

- Gehen Sie zu **Messaging** > **Canvas** und wählen Sie **Benachrichtigungen verwalten** aus dem Kontextmenü eines einzelnen Canvas.
- Öffnen Sie bei aktiven Canvases **Canvas Analytics** und wählen Sie **Benachrichtigungen verwalten**.

Wählen Sie auf der Seite **Benachrichtigungen verwalten** die Option **Benachrichtigung konfigurieren**, um eine neue Benachrichtigung zu erstellen.

## Schritt 2: Benachrichtigung benennen und Canvas auswählen {#step-2-name-your-alert-and-select-a-canvas}

Geben Sie Ihrer Benachrichtigung einen Namen und bestätigen Sie den Canvas, für den sie gilt.

![Das Panel „Benachrichtigung konfigurieren“ mit den Feldern für Benachrichtigungsname und Canvas-Name, einer leeren Regelgruppe und einer Zusammenfassungs-Seitenleiste für Benachrichtigungsregeln, Zeitplan und Benachrichtigungen.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Schritt 3: Benachrichtigungsregeln festlegen {#step-3-set-alert-rules}

Benachrichtigungsregeln definieren den Schwellenwert, der eine Benachrichtigung auslöst. Sie können Regeln mit zwei Metriken erstellen:

- **Nutzer:innen-Eintritte:** Anzahl der Nutzer:innen, die in den Canvas eingetreten sind
- **Gesendete Nachrichten:** Anzahl der vom Canvas gesendeten Nachrichten

Wählen Sie für jede Regel einen Vergleich (kleiner als oder größer als) und einen Volumenschwellenwert. Zum Beispiel kennzeichnet eine Regel für „Nutzer:innen-Eintritte kleiner als 3.000“ einen Canvas, der normalerweise Tausende von Nutzer:innen erreicht, aber plötzlich ins Stocken geraten ist – ein Hinweis auf ein vorgelagertes Zielgruppen- oder Entry-Problem, das untersucht werden sollte.

Sie können mehrere Regeln gruppieren und Regelgruppen mit UND- oder ODER-Logik kombinieren, um spezifischere Benachrichtigungsbedingungen zu erstellen.

## Schritt 4: Benachrichtigungszeitplan festlegen {#step-4-set-the-alert-schedule}

Legen Sie fest, wie oft Ihre Benachrichtigungsregeln überprüft werden. Sie können die Prüfhäufigkeit auf 3 bis 12 Stunden (in 1-Stunden-Schritten) oder auf alle 24 Stunden einstellen. Nach der Aktivierung wird eine Benachrichtigung nach diesem Zeitplan so lange geprüft, wie die Benachrichtigung und der zugehörige Canvas aktiv sind.

## Schritt 5: Benachrichtigungen einrichten {#step-5-set-up-notifications}

Wählen Sie aus, wer benachrichtigt werden soll, wenn eine Benachrichtigungsregel erfüllt ist, und wie die Benachrichtigung erfolgt:

- **E-Mail:** Fügen Sie eine oder mehrere Empfänger:innen-E-Mail-Adressen hinzu.
- **Webhook:** Geben Sie die Webhook-URL ein, an die benachrichtigt werden soll, und fügen Sie optional angepasste Anfrage-Header hinzu, die von Ihrem Webhook-Ziel benötigt werden.

Sie können eine oder beide Benachrichtigungsmethoden für eine einzelne Benachrichtigung aktivieren.

![Der Abschnitt „Benachrichtigungen“ des Panels „Benachrichtigung konfigurieren“ mit E-Mail- und Webhook-Umschaltern, einem Feld für E-Mail-Empfänger:innen, einem Webhook-URL-Feld, einem Hinweis zum Payload-Inhalt und optionalen Anfrage-Header-Feldern.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Webhook-Benachrichtigungen sind nützlich, um Benachrichtigungen an externe Plattformen weiterzuleiten, z. B. an einen Slack-Kanal – weitere Informationen finden Sie in der Slack-Dokumentation zum [Senden von Nachrichten über eingehende Webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Jede Webhook-Benachrichtigung enthält einen Payload mit dem Canvas-Namen, der Metrik der Benachrichtigung, der Schwellenwertrichtung, dem Wert, der die Benachrichtigung ausgelöst hat, und einem direkten Link zum Canvas.

## Schritt 6: Benachrichtigung speichern {#step-6-save-your-alert}

Überprüfen Sie Ihre Benachrichtigungsregeln, den Zeitplan und die Benachrichtigungseinstellungen im Zusammenfassungs-Panel und wählen Sie dann **Benachrichtigung speichern**.

## Schritt 7: Benachrichtigung aktivieren {#step-7-activate-the-alert}

Das Speichern einer Benachrichtigung aktiviert sie nicht. Um sie einzuschalten, gehen Sie zur Seite **Benachrichtigungen verwalten** und verwenden Sie den **Status**-Umschalter für Ihre Benachrichtigung. Eine Benachrichtigung bleibt aktiv, bis Sie sie deaktivieren oder bis der zugehörige Canvas nicht mehr aktiv ist. Die Spalte **Konfigurierte Benachrichtigungen** auf der **Canvas**-Seite zeigt ein Glockensymbol für jeden Canvas mit mindestens einer gespeicherten Benachrichtigung.

## Hinweise {#considerations}

- **Entwurfs-Canvases:** Sie können eine Schwellenwert-Benachrichtigung für einen Canvas einrichten, der sich noch im Entwurf befindet, aber die Benachrichtigung beginnt erst mit der Überprüfung Ihrer Regeln, wenn der Canvas gestartet wird.