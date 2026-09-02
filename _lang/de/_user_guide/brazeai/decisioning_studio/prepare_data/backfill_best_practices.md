---
nav_title: Best Practices für Backfilling
article_title: Best Practices für Backfilling
page_order: 7
page_type: reference
description: "Erfahren Sie, wie Sie historische Daten für BrazeAI Decisioning Studio korrekt nachfüllen (Backfilling), einschließlich Anforderungen, häufiger Fallstricke und wie Sie Datenqualitätsprobleme vermeiden, die die Performance von KI-Modellen beeinträchtigen."
---

# Best Practices für Backfilling {#backfill-best-practices}

> Aus verschiedenen Gründen kann es erforderlich sein, Daten nachzufüllen (Backfilling) – sei es aufgrund von Datenfehlern, neuen Informationen (z. B. neuen Features) oder der Abstimmung von Daten zwischen zwei Systemen. Wenn ein Backfilling durchgeführt wird, befolgen Sie die Grundsätze in diesem Artikel, um die Datenqualität und die Performance des Modells aufrechtzuerhalten.

## Wann Backfilling erforderlich ist {#when-backfilling-is-needed}

Backfilling ist der Prozess, einen Datensatz nachträglich mit historischen Daten zu befüllen. Häufige Szenarien sind:

| Szenario | Beschreibung | Beispiel |
|----------|-------------|---------|
| **Neue Features** | Sie haben eine neue Metrik identifiziert, die für Ihr Modell wichtig ist, und verfügen über die historischen Rohdaten, um sie zu berechnen. | Sie fügen „Klick, der-through-Rate“ als Feature hinzu und benötigen drei Monate an Verlaufsdaten, damit das Modell genügend Daten zum Lernen hat. |
| **Datenwiederherstellung** | Ihre Datenpipeline ist an bestimmten Tagen ausgefallen und hat Lücken in den an Decisioning Studio gelieferten Daten verursacht. | Ein Pipeline-Ausfall am Dienstag hat eine Lücke hinterlassen. Nach der Bereitstellung des Fixes füllen Sie die fehlenden Datensätze aus dem Quellsystem nach. |
| **Logikänderungen** | Sie haben die Formel für eine Feature-Berechnung aktualisiert oder eine Ereignisdefinition geändert. | Sie haben „aktive:r Nutzer:in“ neu definiert und müssen historische Daten erneut exportieren, damit das Modell auf der aktualisierten Definition trainiert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="When backfilling is needed" }

## Anforderungen {#requirements}

Damit Decisioning Studio korrekt funktioniert, müssen alle eingehenden Daten das Backfilling für historische Zeiträume unterstützen. Das erforderliche Lookback-Fenster (gemessen in Monaten) hängt von den Trainingsanforderungen des KI-Modells ab. Wenden Sie sich an Ihr KI Decisioning Services-Team, um den korrekten Wert für Ihren Anwendungsfall zu bestätigen.

Bei der Durchführung eines historischen Backfills sind die folgenden Standards verpflichtend:

- **Prozesskonsistenz:** Historische Feature-Snapshots müssen mit einem Prozess erstellt werden, der vollständig konsistent mit der Erstellung von Live-Snapshots ist. Wenn Ihre Live-Pipeline Transformationen, Aggregationen oder Filter anwendet, müssen dieselben Schritte auch auf die nachgefüllten Daten angewendet werden.
- **Schema-Konsistenz:** Das Schema für nachgefüllte Daten muss exakt mit der normalen täglichen Pipeline übereinstimmen, einschließlich derselben Felder, Datentypen und Spaltenbenennungskonventionen.

## Häufige Fallstricke {#common-pitfalls}

### Data Leakage (Look-Ahead-Bias) {#data-leakage-look-ahead-bias}

Data Leakage ist der kritischste Fehler beim Backfilling. Er tritt auf, wenn der Backfill-Prozess versehentlich Informationen einbezieht, die zum Zeitpunkt der Erstellung des historischen Datensatzes nicht verfügbar gewesen wären.

#### Warum das wichtig ist {#why-it-matters}

Wenn das Modell auf Daten trainiert, die „die Zukunft kennen“, scheint es während des Trainings gut abzuschneiden, liefert aber in der Produktion schlechte Ergebnisse, da Realtime-Entscheidungen keinen Zugriff auf zukünftige Daten haben.

Betrachten Sie beispielsweise die Berechnung eines historischen „LTV“-Features unter Verwendung der Gesamtausgaben einer Kund:in bis heute und die anschließende Nutzung dieses Werts zur Vorhersage von Verhalten, das Monate zuvor aufgetreten ist. Zum Zeitpunkt dieses historischen Ereignisses war der vollständige LTV noch nicht bekannt.

Dies lässt sich vermeiden, indem Sie historische Features immer nur mit den Informationen rekonstruieren, die zum historischen Zeitstempel verfügbar gewesen wären – nicht mit Informationen, die sich danach angesammelt haben.

### Schema- und Logik-Drift {#schema-and-logic-drift}

Datenstrukturen und Geschäftsdefinitionen entwickeln sich im Laufe der Zeit weiter. Inkonsistenzen zwischen historischen und Live-Daten können die Modellqualität schleichend verschlechtern.

- **Schema-Drift:** Wenn ein Feld (z. B. `zip_code`) erst kürzlich zu Ihrer Datenbank hinzugefügt wurde, enthalten nachgefüllte Datensätze aus der Zeit vor dieser Änderung Nullwerte für dieses Feld. Stellen Sie sicher, dass Ihre Pipeline fehlende Felder ordnungsgemäß behandelt und dass das Modell nicht übermäßig von Feldern mit lückenhafter historischer Abdeckung abhängt.
- **Logik-Drift:** Wenn sich die Definition einer Metrik zu einem bestimmten Zeitpunkt geändert hat (z. B. wurde „aktive:r Nutzer:in“ im Jahr 2024 neu definiert), kann die einheitliche Anwendung der neuen Definition auf ältere Daten (z. B. Datensätze aus 2022) künstliche Spitzen oder Einbrüche erzeugen, die tatsächlich nicht aufgetreten sind. Wenden Sie nach Möglichkeit die Definition an, die zum Zeitpunkt des jeweiligen historischen Datensatzes gültig war, oder dokumentieren Sie den Bruchpunkt klar, damit das Modell ihn berücksichtigen kann.

### Doppelte Datensätze durch fehlgeschlagene Backfill-Jobs {#duplicate-records-from-failed-backfill-jobs}

Backfill-Jobs, die mitten in der Ausführung fehlschlagen und neu gestartet werden, können doppelte Datensätze erzeugen, wenn der Prozess nicht darauf ausgelegt ist, dies zu verhindern. Doppelte Datensätze blähen Metriken künstlich auf und führen zu Rauschen im Modelltraining.

**Die Lösung:** Gestalten Sie alle Backfill-Skripte idempotent: Das zweimalige Ausführen desselben Jobs sollte dasselbe Ergebnis liefern wie eine einmalige Ausführung. Verwenden Sie eines der folgenden Muster:

- **Upsert (Update oder Insert):** Basierend auf einer eindeutigen Transaktions-ID oder einem Zeitstempel, sodass das erneute Einfügen eines vorhandenen Datensatzes diesen aktualisiert, anstatt ein Duplikat zu erstellen.
- **Delete then Insert:** Löschen Sie vorhandene Datensätze für den Zielzeitraum vor dem Einfügen, sodass der Datensatz immer sauber ersetzt wird.