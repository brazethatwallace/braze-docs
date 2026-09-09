---
nav_title: Daten an Redshift übertragen
article_title: Datenübertragung an Redshift
page_order: 8
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Daten von Amazon S3 über einen ETL (ETL)-Prozess nach Redshift übertragen."
tool: Currents

---

# Daten an Redshift übertragen

> [Amazon Redshift](https://aws.amazon.com/redshift/) ist ein beliebtes Data Warehouse, das auf Amazon Web Services neben Amazon S3 läuft. Braze-Daten aus Currents sind so strukturiert, dass sie direkt in Redshift übertragen werden können.

Im Folgenden wird beschrieben, wie Daten von Amazon S3 über einen ETL-Prozess (ETL) nach Redshift übertragen werden können. Den vollständigen Quellcode finden Sie im [GitHub-Repository](https://github.com/Appboy/currents-examples) „Currents examples“.

{% alert important %}
Dies ist nur eine von vielen Optionen, die Sie wählen können, wenn es darum geht, Ihre Daten an Orte zu übertragen, die für Sie am vorteilhaftesten sind.
{% endalert %}

## Übersicht über den S3-zu-Redshift-Loader

Das Skript [`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader) verwendet eine separate Manifesttabelle in derselben Redshift-Datenbank, um die bereits kopierten Dateien zu verfolgen. Die allgemeine Struktur ist wie folgt:

1. Listen Sie alle Dateien in S3 auf und identifizieren Sie anschließend die neuen Dateien seit der letzten Ausführung von `s3loader.py`, indem Sie die Liste mit dem Inhalt der Manifesttabelle vergleichen.
2. Erstellen Sie eine [Manifestdatei](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html), die die neuen Dateien enthält.
3. Führen Sie eine `COPY`-Abfrage aus, um die neuen Dateien mithilfe der Manifestdatei von S3 nach Redshift zu kopieren.
4. Fügen Sie die Namen der kopierten Dateien in die separate Manifesttabelle in Redshift ein.
5. Commit.

## Abhängigkeiten

Sie müssen das AWS Python SDK und Psycopg installieren, um den Loader auszuführen:

```bash
pip install boto3
pip install psycopg2
```

## Berechtigungen

### Redshift-Rolle mit S3-Lesezugriff

Falls noch nicht geschehen, folgen Sie der [AWS-Dokumentation](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html), um eine Rolle zu erstellen, die `COPY`-Befehle auf Ihre Dateien in S3 ausführen kann.

### Redshift-VPC-Eingangsregeln

Wenn sich Ihr Redshift-Cluster in einer VPC befindet, müssen Sie die VPC so konfigurieren, dass Verbindungen von dem Server zugelassen werden, auf dem Sie den S3-Loader ausführen. Navigieren Sie zu Ihrem Redshift-Cluster und wählen Sie den VPC-Sicherheitsgruppeneintrag aus, mit dem sich der Loader verbinden soll. Fügen Sie dann eine neue Eingangsregel hinzu: **Type** = Redshift, **Protocol** = TCP, **Port** = der Port Ihres Clusters, **Source** = die IP des Servers, auf dem der Loader läuft (oder „Anywhere“ zum Testen).

### Identity and Access Management (IAM)-Nutzer:in mit S3-Vollzugriff

Der S3-Loader benötigt Lesezugriff auf die Dateien mit Ihren Currents-Daten sowie Vollzugriff auf den Speicherort für die Manifestdateien, die er für die Redshift-`COPY`-Befehle generiert. Erstellen Sie eine:n neue:n Identity and Access Management (IAM)-Nutzer:in mit der Berechtigung `AmazonS3FullAccess` über die [IAM-Konsole](https://console.aws.amazon.com/iam/home#/users). Speichern Sie die Zugangsdaten, da Sie diese an den Loader übergeben müssen.

Sie können die Zugangsdaten über Umgebungsvariablen, die gemeinsame Zugangsdatendatei (`~/.aws/credentials`) oder die [AWS-Konfigurationsdatei](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials) an den Loader übergeben. Alternativ können Sie sie direkt im Loader angeben, indem Sie sie den Feldern `aws_access_key_id` und `aws_secret_access_key` innerhalb eines `S3LoadJob`-Objekts zuweisen. Wir empfehlen jedoch nicht, Zugangsdaten direkt in Ihrem Quellcode fest zu codieren.

## Verwendung

### Beispielverwendung

Das folgende Beispielprogramm lädt Daten für das Ereignis `users.messages.contentcard.Impression` von S3 in die Tabelle `content_card_impression` in Redshift.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### Zugangsdaten

Um den Loader auszuführen, müssen Sie zunächst `host`, `port` und `database` Ihres Redshift-Clusters sowie `user` und `password` einer Redshift-Nutzer:in angeben, die `COPY`-Abfragen ausführen kann. Zusätzlich müssen Sie den ARN der Redshift-Rolle mit S3-Lesezugriff angeben, die Sie in einem vorherigen Abschnitt erstellt haben.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### Job-Konfiguration

Sie müssen den S3-Bucket und das Präfix Ihrer Ereignisdateien sowie den Namen der Redshift-Tabelle angeben, in die Sie `COPY` ausführen möchten.

Um Avro-Dateien mit der Option „auto“ zu kopieren, wie es der Loader erfordert, muss die Spaltendefinition in Ihrer Redshift-Tabelle mit den Feldnamen im Avro-Schema übereinstimmen, wie im Beispielprogramm gezeigt, mit der entsprechenden Typzuordnung (z. B. `string` zu `text`, `int` zu `integer`).

Sie können dem Loader auch eine `batch_size`-Option übergeben, wenn das Kopieren aller Dateien auf einmal zu lange dauert. Durch die Angabe einer `batch_size` kann der Loader inkrementell jeweils einen Batch kopieren und committen, ohne alles gleichzeitig kopieren zu müssen. Die Dauer zum Laden eines Batches hängt von der `batch_size` sowie der Größe Ihrer Dateien und der Größe Ihres Redshift-Clusters ab.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```