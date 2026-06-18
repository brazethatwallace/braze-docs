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

## Das Sync-Log-Dashboard verstehen {#understanding-the-sync-log-dashboard}

Die Hauptseite **Sync Log** bietet einen umfassenden Überblick über alle Ihre Synchronisierungsläufe, einschließlich einer Übersicht über die letzten Synchronisierungen nach ihrem aktuellen oder endgültigen Status.

* **Running:** Synchronisierungsaufträge, die derzeit ausgeführt werden.
* **Success:** Synchronisierungsaufträge, die abgeschlossen wurden und bei denen alle Zeilen erfolgreich verarbeitet wurden.
* **Partial Success:** Synchronisierungsaufträge, die abgeschlossen wurden, bei denen jedoch eine oder mehrere Zeilen einen Fehler verursacht haben.
* **Error:** Synchronisierungsaufträge, die nicht abgeschlossen werden konnten.
* **Limit Exceeded:** Synchronisierungsaufträge, deren Verarbeitung gestoppt wurde, weil ein Datenlimit überschritten wurde.

![Ein Beispiel für Sync-Protokolle mit insgesamt 6.576 erfolgreichen Vorgängen.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Sync-Protokolle enthalten außerdem die folgenden Details zu jeder Synchronisierung:

* **Sync-Name:** Der Name der Synchronisierungskonfiguration.
* **Run-ID:** Ein eindeutiger Bezeichner für eine bestimmte Ausführung der Synchronisierung. Wählen Sie diese ID aus, um weitere Details anzuzeigen. Sie kann auch in den [CDI-API-Endpunkten]({{site.baseurl}}/api/endpoints/cdi/) verwendet werden oder um einen Synchronisierungslauf mit Braze Support zu referenzieren.
* **Status:** Der Status des Laufs (Success, Partial Success, Error, Running).
* **Neue Zeilen aus der Quelle gelesen:** Die Anzahl der neuen Zeilen, die für diesen Durchlauf aus Ihrem Data Warehouse abgerufen wurden.
* **Ergebnisse:** Eine Aufschlüsselung der Anzahl der erfolgreichen und fehlgeschlagenen Zeilen innerhalb des Durchlaufs.
* **Letzter `UPDATED_AT`:** Der Zeitstempel des letzten Datensatzes, der in diesem Synchronisierungslauf verarbeitet wurde.
* **Startzeit des Laufs:** Wann der Synchronisierungsauftrag begonnen hat.
* **Laufdauer:** Die Gesamtzeit, die der Synchronisierungsauftrag bis zum Abschluss benötigt hat.

### Datenaufbewahrung {#data-retention}

Sync-Protokolldaten, einschließlich aller Payloads auf Zeilenebene und Fehlerdetails, werden bis zu **30 Tage** lang aufbewahrt. Protokolle, die älter als 30 Tage sind, werden automatisch gelöscht.

Metadaten zu Synchronisierungsläufen, wie beispielsweise die Anzahl der verarbeiteten Zeilen, werden mindestens 12 Monate lang aufbewahrt.

### Sync-Protokolle filtern {#filtering-sync-logs}

Sie können die Sync-Protokolltabelle filtern, um bestimmte Durchläufe zu finden. Die verfügbaren Filter umfassen:

* **Startdatum des Auftrags:** Wählen Sie einen vordefinierten Zeitraum (z. B. „Letzte 30 Tage“) oder einen angepassten Datumsbereich aus.
* **Status:** Filtern Sie nach einem oder mehreren Synchronisierungsstatus (z. B. nur **Error**- und **Partial Success**-Status anzeigen).
* **Sync-Name:** Suchen Sie nach einer bestimmten Synchronisierung anhand ihres Namens.

Um eine bestimmte Synchronisierung zu untersuchen, wählen Sie die entsprechende **Run ID** aus der Sync-Protokolltabelle aus. Auf der Seite **Run details** finden Sie ein detailliertes Protokoll der Synchronisierung, das Zeile für Zeile aufgeführt ist.

### Laufübersicht {#run-overview}

Dieser Abschnitt fasst den ausgewählten Lauf zusammen, einschließlich Startzeit, Endzeit, Dauer und Gesamtzahl der aus der Quelle gelesenen Zeilen. Er gibt auch an, wie viele Zeilen erfolgreich verarbeitet wurden und wie viele zu einem Fehler geführt haben.

### In diesem Lauf verarbeitete Zeilen {#rows-processed-in-this-run}

Diese Tabelle bietet Transparenz auf Zeilenebene hinsichtlich der während der Synchronisierung verarbeiteten Daten, sodass Sie einzelne Datensätze überprüfen können.

* **Suchen:** Sie können mithilfe der Suchleiste **Search by user ID** innerhalb der Ergebnisse des Durchlaufs nach bestimmten Nutzer:innen suchen.
* **Verfügbare Details:**
  * **`UPDATED_AT`:** Der Zeitstempel aus der `UPDATED_AT`-Spalte für diese bestimmte Zeile.
  * **ID:** Die Nutzer-Bezeichner (wie `external_id`, `email` oder `alias_name`), die verwendet werden, um den Datensatz mit einem Braze-Nutzerprofil abzugleichen.
  * **Status:** Der individuelle Verarbeitungsstatus für diese Zeile (**Success** oder **Error**).
  * **Quell-Payload:** Ein Link zum Anzeigen des Daten-Payloads.
  * **Fehlergrund:** Wenn der Status **Error** lautet, enthält diese Spalte eine Nachricht, die erklärt, warum die Zeile nicht synchronisiert werden konnte.

#### Payloads anzeigen {#viewing-payloads}

Um die genauen Daten anzuzeigen, die für eine bestimmte Zeile an Braze gesendet wurden, wählen Sie **View payload** in der Spalte **Source** payload aus. Hiermit wird der rohe JSON-Payload angezeigt, der für diese:n Nutzer:in verarbeitet wurde.

#### Sync-Protokolle exportieren {#exporting-sync-logs}

Wählen Sie **Export rows** aus, um die Protokolle auf Zeilenebene für einen Synchronisierungslauf zu exportieren. Wählen Sie anschließend die Exportmethode:

* **Zeilen mit Fehlern:** Lädt eine Datei herunter, die ausschließlich die Zeilen mit dem Status **Error** enthält.
* **Alle Zeilen:** Lädt eine Datei herunter, die alle in diesem Durchlauf verarbeiteten Zeilen enthält.

{% multi_lang_include early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Protokolle können nicht direkt aus dem Dashboard exportiert werden. Nach der Erstellung des Exports erhalten Sie eine E-Mail mit einem Link zum Herunterladen der Protokollexportdatei.

## Benachrichtigungen {#notifications}

Sie können E-Mail-Benachrichtigungen konfigurieren, um über den Status Ihrer CDI-Synchronisierungen auf dem Laufenden zu bleiben. Diese Einstellungen werden beim Erstellen einer Synchronisierung konfiguriert und können jederzeit aktualisiert werden.

### Fehlerbenachrichtigungen {#error-notifications}

Es ist mindestens eine E-Mail-Adresse als Kontakt erforderlich, um Benachrichtigungen über Fehler auf Synchronisierungsebene zu erhalten. Diese Benachrichtigungen werden versendet, wenn ein gesamter Synchronisierungsauftrag nicht ausgeführt oder abgeschlossen werden kann oder wenn bei der Synchronisierung ein Fehler auftritt, der ein Eingreifen erfordert, beispielsweise abgelaufene Zugangsdaten oder eine fehlende Quelltabelle.

Weitere Benachrichtigungen umfassen:

- **Zeilenfehler:** Erhalten Sie Benachrichtigungen, wenn ein bestimmter Prozentsatz der Zeilen bei einer Synchronisierung nicht aktualisiert werden kann.
- **Fehlerschwelle (%):** Geben Sie den Prozentsatz der Zeilenfehler an, der eine Benachrichtigung triggern soll. Wenn Sie diesen Wert beispielsweise auf **1** setzen, wird eine Benachrichtigung gesendet, wenn 1 % oder mehr der Zeilen in einem Synchronisierungslauf zu einem Fehler führen.
- **Synchronisierung erfolgreich:** Erhalten Sie eine Benachrichtigung, sobald eine Synchronisierung erfolgreich abgeschlossen wurde.
- **Benachrichtigung auch ohne Zeilenänderungen:** Erhalten Sie eine Benachrichtigung, auch wenn bei einer erfolgreichen Synchronisierung keine neuen oder aktualisierten Zeilen verarbeitet werden.