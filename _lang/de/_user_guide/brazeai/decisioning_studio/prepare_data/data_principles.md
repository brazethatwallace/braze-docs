---
nav_title: Allgemeine Grundsätze
article_title: Allgemeine Datengrundsätze für Decisioning Studio
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die allgemeinen Datengrundsätze, die für alle Datenbestände gelten, die von BrazeAI Decisioning Studio verwendet werden."
---

# Allgemeine Grundsätze {#general-principles}

> Gut strukturierte Daten sind die Grundlage eines effektiven Decisioning Studio Agents. Bevor Sie sich mit den spezifischen Anforderungen an einzelne Datenbestände befassen, ist es hilfreich, die vier Kernprinzipien zu verstehen, die für alle Daten gelten, die Sie an Decisioning Studio senden. Verstöße gegen eines dieser Prinzipien gehören zu den häufigsten Ursachen für eine verschlechterte Modell-Performance.

## Ein einheitlicher Kundenbezeichner über alle Datenbestände hinweg {#one-consistent-customer-identifier-across-all-assets}

Jeder Datenbestand (Kundenprofile, Aktivierungen, Engagements, Conversions) muss denselben Kundenbezeichner referenzieren. Es sollte genau einen primären Bezeichner geben, der jede geschäftskunden eindeutig und konsistent über alle Datenbestände hinweg identifiziert.

| Anforderung | Auswirkung bei Verstoß |
|-------------|------------------------|
| Ein einzelner, eindeutiger Kundenbezeichner muss in jedem Datenbestand vorhanden sein | Wenn verschiedene Datenbestände unterschiedliche ID-Systeme verwenden (zum Beispiel eine Warehouse-ID für Features, aber eine Plattform-ID für Aktivierungen), kann die Decisioning Studio Engine diese nicht zuverlässig verknüpfen. Dies unterbricht die Feedback-Schleife und verschlechtert sowohl das Modelltraining als auch die Berichtsgenauigkeit. Wenn sich die Abbildung zwischen den beiden ID-Systemen als Many-to-Many statt One-to-Many herausstellt, können die daraus resultierenden Datenintegritätsprobleme schwerwiegend sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ein einheitlicher Kundenbezeichner über alle Datenbestände hinweg" }

Siehe [Externe Braze-ID verwenden]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id) für Hinweise dazu, welchen Bezeichner Sie verwenden sollten.

## Event-Daten müssen als inkrementeller Stream übergeben werden, nicht als Snapshot {#event-data-must-be-passed-as-an-incremental-stream-not-as-a-snapshot}

Events wie Conversions, Engagements und Aktivierungen stellen diskrete Ereignisse dar, die zu einem bestimmten Zeitpunkt stattgefunden haben. Sie müssen als inkrementeller (Append-only) Stream einzelner Datensätze an Decisioning Studio übermittelt werden, nicht als aggregierter Snapshot.

| Anforderung | Auswirkung bei Verstoß |
|-------------|------------------------|
| Event-Daten müssen als einzelne, mit Zeitstempel versehene Datensätze strukturiert und inkrementell übermittelt werden | Wenn Event-Daten in einem Snapshot aggregiert werden (zum Beispiel durch Speicherung eines Attributs „Letzter Sendezeitpunkt“ anstelle einzelner Sendedatensätze), geht die genaue zeitliche Zuordnung jedes Events verloren. Dadurch wird es unmöglich, Ergebnisse präzise bestimmten Entscheidungen zuzuordnen, was die Feedback-Schleife unterbricht, die das Modell zum Lernen benötigt. Ohne präzise Event-Zeitstempel können Sie nicht genau wissen, wann eine Conversion stattgefunden hat oder welche Empfehlung sie ausgelöst hat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Event-Daten müssen als inkrementeller Stream übergeben werden, nicht als Snapshot" }

Siehe [Snapshots versus Event-Streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) für eine vollständige Erklärung der Unterscheidung sowie Beispiele für korrekte und inkorrekte Muster.

## Snapshot-Daten müssen nach einem regelmäßigen, zeitgesteuerten Zeitplan aktualisiert werden {#snapshot-data-must-be-updated-on-a-regular-time-driven-schedule}

Snapshot-Daten (wie Kundenprofile und Features) repräsentieren den aktuellen Zustand einer geschäftskunden zu einem bestimmten Zeitpunkt. Aktualisierungen von Snapshot-Daten sollten durch einen regelmäßigen Zeitplan gesteuert werden (zum Beispiel täglich), nicht durch Event-Trigger.

| Anforderung | Auswirkung bei Verstoß |
|-------------|------------------------|
| Snapshots müssen für alle Kund:innen nach einem regelmäßigen Zeitplan aktualisiert werden, unabhängig davon, ob eine geschäftskunden an diesem Tag ein Event hatte | Wenn Snapshot-Aktualisierungen nur durch ein Event getriggert werden, werden Features, die vom Zeitverlauf abhängen (wie „Tage seit dem letzten Kauf“ oder „Tage seit der Registrierung“), für Kund:innen veralten, die kein kürzliches Event hatten. Das Modell wird dann mit veralteten Feature-Werten trainiert, was seine Fähigkeit verringert, genaue und zeitnahe Empfehlungen zu geben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Snapshot-Daten müssen nach einem regelmäßigen, zeitgesteuerten Zeitplan aktualisiert werden" }

## Alle Datenbestände müssen Mindestanforderungen an Datenqualität und -integrität erfüllen {#all-assets-must-meet-minimum-data-quality-and-integrity-requirements}

Über die Struktur hinaus müssen die Daten selbst intern konsistent und vollständig genug sein, um nützlich zu sein.

| Anforderung | Auswirkung bei Verstoß |
|-------------|------------------------|
| Jeder Datenbestand muss die Felder enthalten, die zur Festlegung eines Primärschlüssels und, wo zutreffend, von Verknüpfungsschlüsseln zu anderen Datenbeständen erforderlich sind. Doppelte Datensätze müssen vor der Aufnahme entfernt oder dedupliziert werden. | Doppelte oder nicht zuordenbare Datensätze fügen dem Modelltraining Rauschen hinzu und können zu fehlerhafter Attribution führen. Fehlende Schlüssel verhindern, dass die Engine Ereignisse über die gesamte geschäftskunden Journey hinweg verknüpfen kann – von der Empfehlung bis zur Conversion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alle Datenbestände müssen Mindestanforderungen an Datenqualität und -integrität erfüllen" }

Speziell für Event-Stream-Daten muss jeder Datensatz mindestens Folgendes enthalten:

**Erforderliche Felder:**
- Kundenbezeichner
- Zeitstempel, wann das Event stattgefunden hat (nicht wann der Datensatz in Ihrem System erstellt wurde; dies sind unterschiedliche Werte; siehe [Snapshots versus Event-Streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) für eine Erklärung, warum dies wichtig ist)
- Zeitstempel, wann der Datensatz in Ihrem System erstellt wurde (wird für zuverlässiges Aufteilen inkrementeller Exporte verwendet)
- Event-Typ
- Felder, die ausreichen, um auf die spezifischen Events zu filtern, die für Sie relevant sind

**Empfohlene Felder:**
- Zusätzliche Event-Metadaten, die eine zuverlässige Zuordnung zwischen Event-Typen ermöglichen (zum Beispiel die Verknüpfung eines Konversions-Events mit der spezifischen Aktivierung, die ihm vorausging)