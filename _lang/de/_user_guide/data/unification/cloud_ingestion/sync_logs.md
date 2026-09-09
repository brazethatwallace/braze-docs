---
nav_title: Sync-Protokolle und Observability
article_title: Sync-Protokolle und Observability
page_order: 8
page_type: reference
description: "Diese Seite bietet eine Übersicht über die in CDI verfügbaren Observability-Features."
---

# Sync-Protokolle und Observability {#sync-logs-and-observability}

> Über das **Sync Log**-Dashboard der Cloud-Datenaufnahme (CDI) können Sie alle von CDI verarbeiteten Daten überwachen, überprüfen, ob die Daten erfolgreich synchronisiert wurden, und Probleme mit „fehlerhaften“ oder fehlenden Daten diagnostizieren.

Um auf die Sync-Protokolle zuzugreifen, navigieren Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** und wählen Sie den Tab **Sync Log** aus.

<!-- support-analyzer-phase2:cdi_updated_at_row_sync -->
{% alert note %}
Wenn die Zeilenanzahl im Data Warehouse nicht mit **Rows Synced** übereinstimmt oder Sie Durchläufe mit **Partial Success** sehen, öffnen Sie die **Run ID** im Sync Log und überprüfen Sie die **Error reason**-Werte auf Zeilenebene. CDI wählt Zeilen anhand von `UPDATED_AT` aus – Zeilen mit bereits verarbeiteten Zeitstempeln, unverändertem `UPDATED_AT` nach Bearbeitungen oder Schreibvorgänge während eines aktiven Syncs können übersprungen werden. Häufige Fälle finden Sie unter [Warum stimmt „Rows Synced“ nicht mit der Anzahl in meinem Data Warehouse überein?]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs#why-doesnt-rows-synced-match-the-number-in-my-warehouse) und [Cloud-Datenaufnahme – FAQ]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs).
{% endalert %}

## Das Sync-Log-Dashboard verstehen {#understanding-the-sync-log-dashboard}

Die Hauptseite **Sync-Log** bietet eine allgemeine Übersicht über alle Ihre Sync-Durchläufe, einschließlich einer Übersicht der letzten Syncs nach ihrem aktuellen oder endgültigen Status.

* **Running:** Sync-Jobs, die derzeit ausgeführt werden.
* **Success:** Sync-Jobs, die abgeschlossen wurden und bei denen alle Zeilen erfolgreich verarbeitet wurden.
* **Partial Success:** Sync-Jobs, die abgeschlossen wurden, bei denen jedoch eine oder mehrere Zeilen einen Fehler aufwiesen.
* **Error:** Sync-Jobs, die nicht abgeschlossen werden konnten.
* **Limit Exceeded:** Sync-Jobs, die die Verarbeitung gestoppt haben, weil ein Datenlimit überschritten wurde.

![Ein Beispiel für Sync-Logs mit insgesamt 6.576 erfolgreichen Durchläufen.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Sync-Logs liefern außerdem die folgenden Details für jeden Sync:

* **Sync name:** Der Name der Sync-Konfiguration.
* **Run ID:** Ein eindeutiger Bezeichner für eine bestimmte Ausführung des Syncs. Wählen Sie diese ID aus, um weitere Details anzuzeigen oder um einen Sync-Durchlauf beim Braze-Support zu referenzieren.
* **Status:** Der Status des Durchlaufs (Success, Partial Success, Error, Running).
* **New rows read from source:** Die Anzahl der neuen Zeilen, die für diesen Durchlauf aus Ihrem Data Warehouse abgerufen wurden.
* **Results:** Eine Aufschlüsselung, wie viele Zeilen innerhalb des Durchlaufs erfolgreich waren oder fehlgeschlagen sind.
* **Last "UPDATED_AT":** Der Zeitstempel des zuletzt verarbeiteten Datensatzes in diesem Sync-Durchlauf.
* **Run start time:** Wann der Sync-Job gestartet wurde.
* **Run duration:** Die Gesamtdauer, die der Sync-Job bis zum Abschluss benötigt hat.

### Datenaufbewahrung {#data-retention}

Sync-Log-Daten, einschließlich aller Payloads auf Zeilenebene und Fehlerdetails, werden bis zu **30 Tage** aufbewahrt. Logs, die älter als 30 Tage sind, werden automatisch gelöscht.

Metadaten zu Sync-Durchläufen, wie die Anzahl der verarbeiteten Zeilen, werden mindestens 12 Monate aufbewahrt.

### Sync-Logs filtern {#filtering-sync-logs}

Sie können die Sync-Log-Tabelle filtern, um bestimmte Durchläufe zu finden. Die verfügbaren Filter umfassen:

* **Job start date:** Wählen Sie einen vordefinierten Zeitraum (wie „Letzte 30 Tage“) oder einen benutzerdefinierten Datumsbereich aus.
* **Status:** Filtern Sie nach einem oder mehreren Sync-Status (z. B. nur **Error**- und **Partial Success**-Status anzeigen).
* **Sync name:** Suchen Sie nach einem bestimmten Sync anhand seines Namens.

Um einen bestimmten Sync zu untersuchen, wählen Sie die entsprechende **Run ID** aus der Sync-Log-Tabelle aus. Auf der Seite **Run details** finden Sie ein detailliertes, zeilenweises Protokoll des Syncs.

### Übersicht des Durchlaufs {#run-overview}

Dieser Abschnitt fasst den ausgewählten Durchlauf zusammen, einschließlich Startzeit, Endzeit, Dauer und der Gesamtanzahl der aus der Quelle gelesenen Zeilen. Er zeigt außerdem, wie viele Zeilen erfolgreich waren und wie viele zu einem Fehler geführt haben.

### In diesem Durchlauf verarbeitete Zeilen {#rows-processed-in-this-run}

Diese Tabelle bietet Einblick auf Zeilenebene in die während des Syncs verarbeiteten Daten und ermöglicht es Ihnen, einzelne Datensätze zu überprüfen.

* **Suche:** Sie können innerhalb der Ergebnisse des Durchlaufs nach einer bestimmten Nutzer:in suchen, indem Sie die Leiste **Search by user ID** verwenden.
* **Verfügbare Details:**
  * **UPDATED_AT:** Der Zeitstempel aus der `UPDATED_AT`-Spalte für die jeweilige Zeile.
  * **ID:** Die Nutzer:innen-Bezeichner (wie `external_id`, `email` oder `alias_name`), die verwendet werden, um den Datensatz einem Braze-Kundenprofil zuzuordnen.
  * **Status:** Der individuelle Verarbeitungsstatus für diese Zeile (**Success** oder **Error**).
  * **Source payload:** Ein Link zum Anzeigen des Daten-Payloads.
  * **Error reason:** Wenn der Status **Error** ist, enthält diese Spalte eine Meldung, die erklärt, warum die Zeile nicht synchronisiert werden konnte.

#### Payloads anzeigen {#viewing-payloads}

Um die genauen Daten zu sehen, die für eine bestimmte Zeile an Braze gesendet wurden, wählen Sie **View payload** in der Spalte **Source** payload aus. Dies zeigt den rohen JSON-Payload an, der für diese Nutzer:in verarbeitet wurde.

#### Sync-Logs exportieren {#exporting-sync-logs}

Wählen Sie **Export rows** aus, um die Protokolle auf Zeilenebene für einen Sync-Durchlauf zu exportieren. Wählen Sie dann den Export nach:

* **Rows with errors:** Lädt eine Datei herunter, die nur die Zeilen mit dem Status **Error** enthält.
* **All rows:** Lädt eine Datei herunter, die jede im Durchlauf verarbeitete Zeile enthält.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Logs können nicht direkt aus dem Dashboard exportiert werden. Nachdem der Export erstellt wurde, erhalten Sie eine E-Mail mit einem Link zum Herunterladen der Log-Exportdatei.

## Benachrichtigungen {#notifications}

Sie können E-Mail-Benachrichtigungen konfigurieren, um über den Status Ihrer CDI-Synchronisierungen informiert zu bleiben. Diese Einstellungen werden beim Erstellen einer Synchronisierung konfiguriert und können jederzeit aktualisiert werden.

### Fehlerbenachrichtigungen {#error-notifications}

Mindestens eine E-Mail-Adresse als Kontakt ist erforderlich, um Benachrichtigungen über Fehler auf Synchronisierungsebene zu erhalten. Diese Warnungen werden gesendet, wenn ein gesamter Synchronisierungsauftrag nicht ausgeführt oder abgeschlossen werden kann, oder wenn bei der Synchronisierung ein Fehler auftritt, der ein Eingreifen der Nutzer:innen erfordert, z. B. abgelaufene Zugangsdaten oder eine fehlende Quelltabelle.

Zusätzliche Benachrichtigungen umfassen:

- **Zeilenfehler:** Erhalten Sie Warnungen, wenn ein bestimmter Prozentsatz an Zeilen innerhalb einer Synchronisierung nicht aktualisiert werden kann.
- **Fehlerschwellenwert (%):** Geben Sie den Prozentsatz an Zeilenfehlern an, der eine Warnung auslösen soll. Wenn Sie diesen Wert beispielsweise auf **1** setzen, wird eine Benachrichtigung gesendet, wenn 1 % oder mehr der Zeilen in einem Synchronisierungslauf zu einem Fehler führen.
- **Synchronisierung erfolgreich:** Erhalten Sie eine Benachrichtigung nach dem erfolgreichen Abschluss einer Synchronisierung.
- **Warnung auch wenn keine Zeilen geändert werden:** Erhalten Sie eine Benachrichtigung, auch wenn ein erfolgreicher Synchronisierungslauf keine neuen oder aktualisierten Zeilen verarbeitet.