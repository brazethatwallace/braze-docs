---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung beim Export
page_order: 6
page_type: reference
description: "Diagnostizieren Sie CSV- und API-Exportfehler mithilfe eines Symptomverzeichnisses, eines standardmäßigen Untersuchungspfads und speicherspezifischer Fehlerbehebung."
---

# Fehlerbehebung beim Export {#export-troubleshooting}

> Verwenden Sie diese Seite, um CSV- und API-Exportprobleme im Dashboard und den Export-APIs zu diagnostizieren. Informationen zu Export-Workflows und -Limits finden Sie unter [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) und [Export-APIs]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_apis).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

Suchen Sie das Verhalten, das Sie beobachten, in der Tabelle und navigieren Sie dann zum entsprechenden Abschnitt für gezielte Prüfungen.

| Symptom | Gehe zu |
| --- | --- |
| CSV-Download-Link gibt `AccessDenied`, `ExpiredToken` oder „Datei existiert nicht mehr“ zurück | [Standardexport: CSV-Fehler](#defaultexport_csv-exports) oder [Cloud-Speicher: CSV-Fehler](#csv-exports-1) |
| API-Export-Download-URL gibt `403 Forbidden` zurück | [ZIP-Datei eines exportierten Segments kann nicht heruntergeladen werden](#cant-download-an-exported-segment-zip-from-a-braze-url) |
| Segment-Export schlägt fehl oder meldet, dass das Segment zu groß ist | [Segment ist zu groß](#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users) |
| Keine E-Mail zum Segment-Export erhalten | [Keine E-Mail zum Segment-Export](#not-receiving-segment-export-emails) |
| CSV-Zeilenanzahl stimmt nicht mit Campaign-Analytics überein | [Campaign- und Canvas-Analytics-Abweichung](#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients) |
| Erwartete Spalten fehlen in der Exportdatei | [Fehlende Spalten](#expected-columns-are-missing-from-a-segment-export-file) |
| Cloud-Speicher-Export zeigt `AccessDenied` oder `ExpiredToken` | [Cloud-Speicher verbunden: API-Fehler](#common-errors-1) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Export-Symptome" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow für jeden Export-Vorfall. Beginnen Sie bei Schritt 1.

1. Stellen Sie fest, ob Sie in den Standard-S3-Bucket von Braze oder zu einem verbundenen Cloud-Speicher-Partner exportieren. Link-Ablauf und Wiederholungsverhalten unterscheiden sich zwischen beiden Varianten.
2. Stellen Sie bei Dashboard-CSV-Exporten sicher, dass Sie im Braze-Dashboard angemeldet sind, wenn Sie den Download-Link öffnen. Links zum Standard-Bucket erfordern eine aktive Dashboard-Sitzung.
3. Prüfen Sie, wie lange der Export bereits abgeschlossen ist. Per E-Mail versandte Dashboard-Download-Links verfallen nach vier Stunden, unabhängig davon, ob Sie den Standard-Bucket von Braze oder einen verbundenen Speicherpartner verwenden. Wenn ein Speicherpartner verbunden ist, liefert Braze auch eine Kopie an Ihren Bucket; diese Kopie unterliegt Ihren Aufbewahrungsrichtlinien und kann auch nach Ablauf des E-Mail-Links noch verfügbar sein.
4. Stellen Sie bei umfangreichen Segment-Exporten sicher, dass die Zielgruppe unter dem Dashboard-CSV-Exportlimit von 500.000 Nutzer:innen liegt. Schätzungen des Segment-Builders können von der Auswertung der Export-Pipeline abweichen.
5. Warten Sie bei API-Exporten, bis die Verarbeitung abgeschlossen ist, bevor Sie den Download starten. Verwenden Sie `callback_endpoint` bei [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) oder fragen Sie mit exponentiellem Backoff ab, anstatt die URL sofort aufzurufen.
6. Wenn Sie weiterhin blockiert sind, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support) mit dem Exporttyp (CSV oder API), der Segment- oder Campaign-ID, dem Zeitstempel (mit Zeitzone) und der genauen Fehlermeldung.

## Speicherziele {#cloud-storage-connected}

Verwenden Sie die Tabs, um auszuwählen, ob Sie in den Standard-S3-Bucket von Braze oder zu einem Cloud-Speicher-Partner exportieren. Für Anleitungen zum Cloud-Speicher öffnen Sie den Tab **Cloud-Speicher verbunden** und lesen Sie die Abschnitte zu CSV und API.

{% sdktabs %}
{% sdktab Default export %}

Wenn Sie keinen Speicherpartner als Standard-Exportziel festgelegt haben, verwendet Braze seinen eigenen Amazon S3-Bucket, um Ihre Exportdateien zu speichern. Die Dateien in dieser Konfiguration sind temporär und verfallen nach vier Stunden.

### CSV-Exporte {#csv-exports}

Symptom: Eine E-Mail zum Dashboard-CSV-Export trifft ein, aber der Download-Link funktioniert nicht, oder der Export wird nicht abgeschlossen.


Wenn Sie eine CSV-Datei aus dem Dashboard exportieren, sendet Braze einen Download-Link per E-Mail an die angemeldete Nutzer:in. Dieser Link verweist auf eine ZIP-Datei, die im S3-Bucket von Braze gehostet wird. Die ZIP-Datei enthält mehrere kleinere Dateien, die zusammen Ihren Export bilden.

Sie müssen im Braze-Dashboard angemeldet sein, um den Link nutzen zu können, und die Datei ist nur vier Stunden lang verfügbar. Danach ist der Link nicht mehr funktionsfähig und die Daten werden gelöscht. Sollten bei sehr umfangreichen Exporten (über 500.000 Nutzer:innen) wiederholt Fehler auftreten, kann der Export fehlschlagen. In diesem Fall empfehlen wir, den Export in kleinere Gruppen oder Felder aufzuteilen oder die Einrichtung eines Speicherpartners in Betracht zu ziehen.

#### Häufige Fehler {#common-errors}

- Wenn Sie einen `AccessDenied`-Fehler sehen, ist die Datei möglicherweise bereits abgelaufen, oder Sie haben versucht, sie zu öffnen, bevor sie bereit war. Größere Berichte benötigen mehr Zeit für die Erstellung – warten Sie einige Minuten und versuchen Sie es erneut.
- Ein `ExpiredToken`-Fehler bedeutet, dass das vierstündige Zeitfenster abgelaufen ist. Führen Sie den Export erneut aus, um einen neuen Link zu generieren.
- Die Nachricht `Looks like the file doesn't exist anymore` wird in der Regel angezeigt, wenn die E-Mail gesendet wurde, die Datei jedoch noch nicht vollständig auf S3 hochgeladen wurde. In der Regel lässt sich das Problem durch einige Minuten Wartezeit beheben.
- Apostrophe am Anfang bestimmter Felder (wie `-`, `=`, `+` oder `@`) sind erwartetes Verhalten. Beispielsweise wird `-1943` in der CSV-Datei zu `'-1943`. Braze tut dies, um zu verhindern, dass Tabellenkalkulationsprogramme die Daten falsch interpretieren. Dies gilt nicht für JSON-Exporte, wie sie etwa vom [Endpunkt `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) zurückgegeben werden.

### API-Exporte {#api-exports}

Symptom: Ein Export-API-Aufruf ist erfolgreich, aber die Download-URL funktioniert nicht oder gibt leere Daten zurück.


Wenn Sie über die Export-APIs ohne Cloud-Speicher exportieren, speichert Braze die Dateien in seinem S3-Bucket. Sie erhalten keine E-Mail – stattdessen enthält die API-Antwort eine temporäre Download-URL. Der Export erfolgt als ZIP-Datei, die mehrere JSON-Dateien enthält, wobei jede Datei eine Nutzer:in pro Zeile enthält.

Wie bei CSV-Exporten verfallen auch Links aus der API nach vier Stunden. Wenn Sie den Link zu früh öffnen, können Fehler auftreten, da die Datei noch nicht bereit ist. Sie können in Ihrer Anfrage einen `callback_endpoint` angeben, falls Sie von Braze benachrichtigt werden möchten, sobald die Datei verfügbar ist.

Umfangreiche API-Exporte können ebenfalls zu Zeitüberschreitungen führen. Sollte dies der Fall sein, versuchen Sie, kleinere Anfragen zu stellen, oder verbinden Sie einen Speicherpartner, um das Volumen zu bewältigen.

#### Häufige Fehler

- `AccessDenied` oder `ExpiredToken` bedeutet in der Regel, dass der Link abgelaufen oder noch nicht verfügbar war. Führen Sie den Export erneut durch oder warten Sie etwas länger.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Wenn Sie einen Speicherpartner (wie Amazon S3, Google Cloud Storage oder Azure Blob) verbinden und ihn auf der Seite **Technologie-Partner** im Dashboard als Ihr Standard-Exportziel markieren, schreibt Braze Ihre Exporte direkt in Ihren Bucket. Diese Konfiguration ist in der Regel für umfangreichere Exporte zuverlässiger.

### CSV-Exporte {#csv-exports-1}

Symptom: Der per E-Mail versandte CSV-Link funktioniert nicht, aber Dateien erscheinen (oder erscheinen nicht) in Ihrem verbundenen Bucket.


Bei CSV-Exporten sendet Ihnen Braze einen Download-Link per E-Mail. Dieser Link läuft nach einer kurzen Zeitspanne ab (in der Regel nach etwa vier Stunden). Wenn Sie einen Speicherpartner verbunden und als Standard-Exportziel festgelegt haben, liefert Braze auch eine Kopie des Exports an Ihren verbundenen Bucket. Diese Kopie wird in Ihrer eigenen Infrastruktur gespeichert, wobei Ablauf und Aufbewahrung Ihren Speicherrichtlinien entsprechen.

Im Cloud-Speicher werden CSV-Exporte in einer ZIP-Datei gebündelt. Die ZIP-Datei enthält mehrere kleinere CSV-Dateien. Umfangreiche Exporte werden häufig in Teile aufgeteilt (beispielsweise jeweils etwa 5.000 Nutzer:innen), wobei die Größe der Teile variieren kann. Kleinere Dateien bedeuten nicht, dass Daten fehlen. Sollte der per E-Mail versandte Link nicht funktionieren, die Kopie in Ihrem Speicher jedoch erfolgreich sein, können Sie Ihre Daten jederzeit direkt aus Ihrem Bucket abrufen.

#### Häufige Fehler

- `AccessDenied` bedeutet, dass Braze nicht in Ihren Bucket schreiben konnte. Überprüfen Sie, ob Ihre Zugangsdaten und Berechtigungen weiterhin gültig sind.
- `ExpiredToken` wird angezeigt, wenn Braze den Zugriff auf Ihren Bucket verloren hat. Aktualisieren Sie Ihre Zugangsdaten im Braze-Dashboard.
- Sollten einige Dateien kleiner als erwartet erscheinen, ist dies normales Verhalten. Der Exportvorgang teilt Dateien aus Stabilitätsgründen absichtlich auf.
- Apostrophe am Anfang bestimmter Felder (wie `-`, `=`, `+` oder `@`) sind erwartetes Verhalten. Beispielsweise wird `-1943` in der CSV-Datei zu `'-1943`. Braze tut dies, um zu verhindern, dass Tabellenkalkulationsprogramme die Daten falsch interpretieren. Dies gilt nicht für JSON-Exporte, wie sie etwa vom [Endpunkt `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) zurückgegeben werden.

### API-Exporte

Symptom: API-Exporte erscheinen nicht in Ihrem Bucket oder Dateien sind unvollständig.


Wenn Sie Daten über die APIs mit einem verbundenen Speicherpartner exportieren, werden die Exportdateien in Ihren Bucket geschrieben. Es wird keine E-Mail versendet. Die zugrunde liegenden Objekte werden in Ihrem Speicher aufbewahrt und unterliegen Ihren Aufbewahrungseinstellungen, auch wenn die von Braze zurückgegebenen Download-URLs möglicherweise weiterhin zeitlich begrenzt sind.

Dateien erscheinen in der Regel in Ihrem Bucket, während der Export läuft, sodass Sie nicht warten müssen, bis der gesamte Vorgang abgeschlossen ist, bevor Sie auf Teilergebnisse zugreifen. Braze lädt jeden abgeschlossenen Batch inkrementell hoch, anstatt alles bis zum Ende zurückzuhalten. Umfangreiche Exporte werden in mehrere komprimierte Dateien (ZIP oder GZIP) aufgeteilt, die jeweils JSON-Objekte enthalten, eines pro Zeile. Das macht diese Methode für umfangreiche Exporte zuverlässiger.

#### Häufige Fehler {#common-errors-1}

- `AccessDenied` tritt auf, wenn Braze nicht in Ihren Bucket schreiben kann oder die Objekte anschließend gelöscht wurden. Überprüfen Sie die Berechtigungen und stellen Sie sicher, dass keine externen Prozesse Dateien löschen.
- `ExpiredToken` bedeutet, dass die Zugangsdaten von Braze für Ihren Bucket veraltet sind. Aktualisieren Sie diese im Dashboard.
- Sollten Dateien fehlen oder kleiner als erwartet sein, überprüfen Sie zunächst, ob Objekte außerhalb von Braze gelöscht werden. Kleinere Dateigrößen selbst sind erwartetes Verhalten.

{% endsdktab %}
{% endsdktabs %}

## Campaign- und Canvas-Analytics {#campaign-and-canvas-analytics}

### Anzahl der Nutzer:innen im CSV-Export stimmt nicht mit *Gesendete Nachrichten* oder *Eindeutige Empfänger:innen* überein {#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients}

Symptom: Der CSV-Export einer Campaign zeigt eine andere Nutzer:innenanzahl als *Gesendete Nachrichten* oder *Eindeutige Empfänger:innen* auf der Analytics-Seite.


Der CSV-Export einer Campaign kann aus folgenden Gründen eine andere Anzahl von Nutzer:innen anzeigen als *Gesendete Nachrichten* und *Eindeutige Empfänger:innen*:

#### Erneute Berechtigung ist aktiviert {#re-eligibility-is-turned-on}

Wenn Nutzer:innen die Campaign mehr als einmal erhalten können (oder konnten), stimmen die Analytics-Zahlen der Campaign und die Anzahl der Zeilen im Nutzerdaten-Export nicht überein. *Gesendete Nachrichten* zählt jeden Versand, auch wenn dieselbe Nutzer:in mehrfach angeschrieben wird. Der Download **Nutzerdaten als CSV exportieren** listet eindeutige Nutzer:innen auf – eine Zeile pro Profil, das die Campaign erhalten hat – nicht eine Zeile pro Versand. Wenn beispielsweise *Gesendete Nachrichten* 12 beträgt und die CSV-Datei 10 Zeilen enthält, wurden diese 12 Sendungen an 10 verschiedene Nutzer:innen zugestellt (einige Nutzer:innen haben die Campaign mehr als einmal erhalten).

#### Nutzer:innen wurden seit dem Versand der Campaign oder des Canvas gelöscht oder zusammengeführt {#users-were-deleted-or-merged-since-the-campaign-or-canvas-sent}

Der CSV-Export liefert eine Momentaufnahme der vorhandenen Nutzer:innen, die eine bestimmte Campaign oder einen bestimmten Canvas erhalten haben. Da Nutzer:innen gelöscht oder zusammengeführt werden können, kann die Anzahl im CSV-Export niedriger sein als die Anzahl der eindeutigen Empfänger:innen. Wenn beispielsweise 1.000 Nutzer:innen eine Campaign erhalten, zeigt die Campaign 1.000 eindeutige Empfänger:innen an, und der CSV-Export am selben Tag enthält ebenfalls 1.000 Nutzer:innen. Werden einen Monat später 50 dieser 1.000 Nutzer:innen gelöscht, enthält der CSV-Export 950 Nutzer:innen, während die kumulierte Anzahl eindeutiger Empfänger:innen weiterhin 1.000 beträgt.

## E-Mails zum Dashboard-Segment-Export {#dashboard-segment-export-emails}

### Segment ist zu groß oder der Export schlägt fehl, obwohl mein Segment unter 500.000 Nutzer:innen liegt {#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users}

Symptom: Der Dashboard-Segment-Export schlägt fehl oder zeigt einen Größenfehler an, obwohl die Segment-Schätzung akzeptabel erscheint.


Die Größe eines Dashboard-Segments ist **eine Schätzung**. Der CSV-Export verwendet diese Schätzung, um das [Exportlimit von 500.000 Nutzer:innen]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details) durchzusetzen; die Export-Pipeline kann die Größe zudem anders bewerten als die Segment-Builder-Oberfläche. Wenn Exporte für ein Segment nahe an diesem Schwellenwert fehlschlagen, verwenden Sie [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) oder teilen Sie die Zielgruppe in kleinere Segmente auf, oder nutzen Sie den [Endpunkt `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) wie unter [Große Segmente exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-large-segments) beschrieben.

### Warum erhalte ich keine E-Mails zum Segment-Export? {#not-receiving-segment-export-emails}

Symptom: Ein Segment-CSV-Export wurde ausgelöst, aber es ist keine E-Mail eingetroffen.


Überprüfen Sie zunächst Ihren Spam-Ordner auf eine E-Mail von `no-reply@alerts.braze.com`. Wenn die E-Mail dort ist, fügen Sie diese Adresse zu Ihrer Liste sicherer Absender hinzu, damit zukünftige Export-Nachrichten nicht gefiltert werden.

Wenn die E-Mail nicht in Ihrem Spam-Ordner ist, prüfen Sie, ob eine andere Person in Ihrem Team den Export empfangen kann. Falls nicht, berücksichtigen Sie die Größe Ihres Exports. Die Zustellzeit variiert je nach Exportgröße. Sollte die E-Mail nach einer Stunde noch nicht eingetroffen sein, wenden Sie sich an den [Support]({{site.baseurl}}/braze_support).

## API-Downloads für Segment-Exporte {#segment-export-api-downloads}

### ZIP-Datei eines exportierten Segments kann nicht von einer Braze-URL heruntergeladen werden {#cant-download-an-exported-segment-zip-from-a-braze-url}

Symptom: Ein `403 Forbidden`-Fehler beim Herunterladen über die Antwort-URL von `/users/export/segment`.


Wenn Sie beim Verwenden des [Endpunkts `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) einen `403 Forbidden`-Fehler erhalten, ist die Datei möglicherweise noch nicht bereit. Umfangreiche Exporte können einige Zeit in Anspruch nehmen. Warten Sie bis zu einer Stunde, bevor Sie den Download erneut versuchen.

Wenn Sie ein automatisiertes Skript zum Abrufen der Datei verwenden, kann ebenfalls ein `403 Forbidden`-Fehler auftreten, wenn Sie die URL zu früh aufrufen. Wenn Sie regelmäßig Segmentdaten exportieren, sollten Sie eine eigene S3-Bucket-Integration einrichten und die Dateien in Ihre eigene ETL-Pipeline (Extract, Transform, Load) überführen.

Exporte benötigen Zeit bis zur Fertigstellung, daher schlägt ein sofortiger Zugriff über ein Skript häufig fehl. Sie können:

- Die Download-URL mit exponentiellem Backoff abfragen, oder
- den [Parameter `callback_endpoint`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#request-parameters) verwenden und auf einen Dienst verweisen, der Ihr Skript ausführt, sobald der Export bereit ist.

## Felder bei Segment- und Nutzer:innen-Export-APIs {#segment-and-user-export-api-fields}

### Erwartete Spalten fehlen in einer Segment-Exportdatei {#expected-columns-are-missing-from-a-segment-export-file}

Symptom: Ein API- oder Dashboard-Export enthält nicht die erwarteten Felder.


Der Dashboard-Download **Nutzerdaten als CSV exportieren** aus einem Segment verwendet einen festen Spaltensatz (siehe [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#data-included-in-export)). Er enthält keine `fields_to_export`-Spalte und keinen entsprechenden Parameter.

Für API-Segment-Exporte müssen Sie `fields_to_export` im Anfragekörper übergeben. Einige Felder ziehen automatisch zugehörige Daten nach – wenn Sie beispielsweise `canvases_received` anfordern, werden auch Journey-Zusammenfassungsdaten im Nutzerprofil benötigt. Gültige Feldnamen und Anforderungen finden Sie in der Referenz zum [Endpunkt `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

Wenn Spalten in einer API-Export-ZIP-Datei fehlen, überprüfen Sie, ob das Array `fields_to_export` in Ihrer Anfrage jedes benötigte Feld enthält und ob Ihr Workspace über die erforderlichen Exportberechtigungen verfügt.

## Wann Sie den Support kontaktieren sollten {#when-to-contact-support}

Wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support), wenn Sie den [standardmäßigen Untersuchungspfad](#standard-investigation-path) abgeschlossen haben und weiterhin Hilfe benötigen. Geben Sie den Exporttyp, die Segment- oder Campaign-ID, den Zeitstempel (mit Zeitzone) und die genaue Fehlermeldung oder den HTTP-Statuscode an.