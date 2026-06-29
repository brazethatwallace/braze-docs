---
nav_title: Nutzer:innen importieren
article_title: Nutzer:innen importieren
page_order: 3
description: "Erfahren Sie mehr über die verschiedenen Nutzerimport-Optionen von Braze, wie CSV-Import, REST API, Cloud-Datenaufnahme und mehr."

---
# Nutzer:innen importieren {#import-users}

> Erfahren Sie mehr über die verschiedenen Nutzerimport-Optionen von Braze, wie CSV-Import, REST API, Cloud-Datenaufnahme und mehr.

## Importoptionen {#import-options}

Sie können Nutzerattribute und Events über einen CSV-Import in Braze, ein serverloses S3-Lambda-CSV-Importskript, direkte API-Aufrufe oder Cloud-Datenaufnahme aus Ihrem Data Warehouse hochladen.

### Braze-CSV-Import {#braze-csv-import}

Sie können den CSV-Import verwenden, um die folgenden Nutzerattribute und angepassten Events zu erfassen und zu aktualisieren. Informationen zum Einstieg finden Sie unter [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).

| Typ | Definition | Beispiel | Maximale Dateigröße |
|---|---|---|---|
| Standardattribute | Reservierte Nutzerattribute, die von Braze erkannt werden. | `first_name`, `email` | 500 MB |
| Angepasste Attribute | Nutzerattribute, die speziell für Ihr Unternehmen sind. | `last_destination_searched` | 500 MB |
| Angepasste Events | Events, die speziell für Ihr Unternehmen sind und Nutzeraktionen darstellen. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Braze-CSV-Import" }

#### Ihre CSV erstellen {#constructing-your-csv}

Braze akzeptiert Nutzerdaten im Standard-CSV-Format. Importe von Standard- und angepassten Attributen unterstützen Dateien bis zu 500 MB; Importe von angepassten Events unterstützen Dateien bis zu 50 MB. Informationen zu Bezeichnern, Spaltenüberschriften, Validierungsregeln und Beispielen finden Sie unter [CSV-Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import/).

Wenn Sie eine große CSV-Datei über **Nutzer:innen importieren** im Dashboard hochladen, kann die Seite nicht reagieren oder langsam antworten, während Braze die Datei empfängt und den Berechnungsschritt ausführt. Lassen Sie den Upload und die Berechnung abschließen – die Gesamtdauer reicht von wenigen Minuten bis zu einigen Stunden, abhängig von der Dateigröße, und größere Dateien benötigen mehr Zeit für die Berechnung.

{% alert note %}
Beim Import von angepassten Events mit Eigenschaften müssen Sie die Punktnotation in Ihren CSV-Spaltenüberschriften verwenden. Weitere Informationen zur Formatierung von angepassten Events finden Sie unter [Formatierung von angepassten Events verstehen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/?tab=custom%20events#understanding-custom-event-formatting).
{% endalert %}

### Lambda-Nutzer-CSV-Import {#lambda-user-csv-import}

Verwenden Sie unser serverloses S3-Lambda-CSV-Importskript, um Nutzerattribute in Braze hochzuladen. Diese Lösung funktioniert als CSV-Uploader, bei dem Sie Ihre CSVs in einen S3-Bucket ablegen und die Skripte sie über unsere API hochladen.

Die geschätzte Ausführungszeit für eine Datei mit 1.000.000 Zeilen beträgt etwa fünf Minuten. Weitere Informationen finden Sie unter [Nutzerattribut-CSV-zu-Braze-Import]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).

### REST API

Verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um angepasste Events, Nutzerattribute und Käufe für Nutzer:innen zu erfassen.

### Cloud-Datenaufnahme {#cloud-data-ingestion}

Verwenden Sie die Braze [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/), um Nutzerattribute zu importieren und zu pflegen.

## HTML-Validierung {#html-validation}

Beachten Sie, dass Braze HTML-Daten beim Import nicht bereinigt, validiert oder neu formatiert. Das bedeutet, dass Script-Tags aus allen Importdaten entfernt werden müssen, die Sie für die Internet-Personalisierung verwenden.

Wenn Sie Daten in Braze importieren, die speziell für die Personalisierung in einem Webbrowser vorgesehen sind, stellen Sie sicher, dass HTML, JavaScript oder andere Script-Tags entfernt wurden, die bei der Darstellung in einem Webbrowser potenziell böswillig genutzt werden könnten.

Alternativ können Sie für HTML die Braze-Liquid-Filter (`strip_html`) verwenden, um HTML aus gerendertem Text zu entfernen. Zum Beispiel:

{% tabs local %}
{% tab Eingabe %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Ausgabe %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}