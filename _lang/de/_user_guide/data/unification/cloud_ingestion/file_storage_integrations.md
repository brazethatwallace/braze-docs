---
nav_title: Integrationen in die Dateiablage
article_title: Integrationen in die Dateiablage
description: "Diese Seite behandelt die Braze Cloud-Datenaufnahme und wie Sie relevante Daten von Amazon S3 oder Google Cloud Storage mit Braze synchronisieren."
page_order: 4
page_type: reference

---

# Integrationen in die Dateiablage {#file-storage-integrations}

> Auf dieser Seite erfahren Sie, wie Sie die Cloud-Datenaufnahme einrichten, um Daten von Amazon S3 oder Google Cloud Storage mit Braze zu synchronisieren.

## So funktioniert es {#how-it-works}

Sie können Cloud Data Ingestion (CDI) verwenden, um einen oder mehrere Storage-Buckets in Ihrem Cloud-Konto direkt mit Braze zu integrieren. Wenn Sie eine neue Datei zu einem Bucket hinzufügen, veröffentlicht Ihr Cloud-Anbieter eine Benachrichtigung, und Braze Cloud Data Ingestion synchronisiert die Daten.

Der Benachrichtigungsmechanismus hängt von Ihrem Anbieter ab:

- **Amazon S3:** Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an eine Amazon Simple Queue Service (SQS)-Warteschlange gesendet, und Braze verarbeitet diese Nachricht, um die neue Datei aufzunehmen.
- **Google Cloud Storage (GCS):** Wenn neue Dateien im Bucket finalisiert werden, veröffentlicht GCS eine `OBJECT_FINALIZE`-Benachrichtigung an ein Pub/Sub-Topic. Braze verarbeitet diese Benachrichtigungen über ein Pub/Sub-Abo, um die neue Datei aufzunehmen.

Cloud Data Ingestion unterstützt Folgendes:

- JSON-Dateien
- CSV-Dateien
- Parquet-Dateien
- Attribut-, angepasste Event-, Kauf-Event-, Nutzerlöschungs- und Katalogdaten

## Cloud-Datenaufnahme einrichten {#setting-up-cloud-data-ingestion}

Die Einrichtungsschritte hängen von Ihrem Dateispeicheranbieter ab. Wählen Sie den Tab für Ihren Anbieter aus und führen Sie anschließend die gemeinsame Konfiguration in den folgenden Abschnitten durch.

{% tabs %}
{% tab Amazon S3 %}

Die Integration erfordert die folgenden Ressourcen:

- S3-Bucket für die Datenspeicherung
- SQS-Warteschlange für Benachrichtigungen über neue Dateien
- IAM-Rolle für den Braze-Zugriff

### AWS-Definitionen {#aws-definitions}

| Begriff | Definition |
| --- | --- |
| Amazon Resource Name (ARN) | Der ARN ist ein eindeutiger Bezeichner für AWS-Ressourcen. |
| Identity and Access Management (IAM) | IAM ist ein Webdienst, mit dem Sie den Zugriff auf AWS-Ressourcen sicher steuern können. In diesem Tutorial erstellen Sie eine IAM-Richtlinie und weisen sie einer IAM-Rolle zu, um Ihren S3-Bucket mit der Braze Cloud-Datenaufnahme zu integrieren. |
| Amazon Simple Queue Service (SQS) | SQS ist eine gehostete Warteschlange, mit der Sie verteilte Softwaresysteme und -komponenten integrieren können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWS-Definitionen" }

## Cloud-Datenaufnahme in AWS einrichten {#setting-up-cloud-data-ingestion-in-aws}

### Schritt 1: Quell-Bucket erstellen {#step-1-create-a-source-bucket}

Erstellen Sie in Ihrem AWS-Konto einen S3-Bucket für allgemeine Zwecke mit Standardeinstellungen. S3-Buckets können über Synchronisierungen hinweg wiederverwendet werden, solange der Ordner eindeutig ist.

Die Standardeinstellungen sind:

- ACLs deaktiviert
- Gesamten öffentlichen Zugriff blockieren
- Bucket-Versionierung deaktivieren
- SSE-S3-Verschlüsselung
  - SSE-S3 ist der einzige unterstützte serverseitige Verschlüsselungstyp. Die Verschlüsselung mit Amazon KMS wird nicht unterstützt.

Notieren Sie sich die Region, in der Sie den Bucket erstellt haben – Sie erstellen im nächsten Schritt eine SQS-Warteschlange in derselben Region.

### Schritt 2: SQS-Warteschlange erstellen {#step-2-create-sqs-queue}

Erstellen Sie eine SQS-Warteschlange, um zu verfolgen, wann Objekte zu dem von Ihnen erstellten Bucket hinzugefügt werden. Verwenden Sie vorerst die Standard-Konfigurationseinstellungen.

Eine SQS-Warteschlange muss global eindeutig sein (z. B. kann nur eine für eine CDI-Synchronisierung verwendet werden und nicht in einem anderen Workspace wiederverwendet werden).

{% alert important %}
Stellen Sie sicher, dass Sie diese SQS in derselben Region anlegen, in der Sie auch den Bucket erstellt haben.
{% endalert %}

Notieren Sie sich den ARN und die URL der SQS-Warteschlange – Sie benötigen diese während der Konfiguration häufig.

![Auswählen von „Advanced“ mit einem Beispiel-JSON-Objekt, um festzulegen, wer auf eine Warteschlange zugreifen darf.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Schritt 3: Zugriffsrichtlinie einrichten {#step-3-set-up-access-policy}

Um die Zugriffsrichtlinie einzurichten, wählen Sie **Advanced options**.

Fügen Sie die folgende Anweisung an die Zugriffsrichtlinie der Warteschlange an. Achten Sie darauf, `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen, `YOUR-SQS-ARN` durch den ARN Ihrer SQS-Warteschlange und `YOUR-AWS-ACCOUNT-ID` durch Ihre AWS-Konto-ID zu ersetzen:

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### Schritt 4: Ereignisbenachrichtigung zum S3-Bucket hinzufügen {#step-4-add-an-event-notification-to-the-s3-bucket}

1. Gehen Sie in dem in Schritt 1 erstellten Bucket zu **Properties** > **Event notifications**.
2. Geben Sie der Konfiguration einen Namen. Geben Sie optional ein Präfix oder Suffix an, wenn nur eine Teilmenge der Dateien von Braze aufgenommen werden soll.
3. Wählen Sie unter **Destination** die Option **SQS queue** aus und geben Sie den ARN der SQS an, die Sie in Schritt 2 erstellt haben.

{% alert note %}
Wenn Sie Ihre Dateien in den Stammordner eines S3-Buckets hochladen und dann einige der Dateien in einen bestimmten Ordner im Bucket verschieben, kann ein unerwarteter Fehler auftreten. Stattdessen können Sie die Ereignisbenachrichtigungen so ändern, dass sie nur für Dateien im Präfix gesendet werden, keine Dateien außerhalb dieses Präfixes in den S3-Bucket legen oder die Integration ohne Präfix aktualisieren, wodurch dann alle Dateien aufgenommen werden.
{% endalert %}

### Schritt 5: IAM-Richtlinie erstellen {#step-5-create-an-iam-policy}

Erstellen Sie eine IAM-Richtlinie, um Braze die Interaktion mit Ihrem Quell-Bucket zu ermöglichen. Melden Sie sich zunächst bei der AWS-Verwaltungskonsole als Konto-Administrator an.

1. Gehen Sie zum IAM-Bereich der AWS-Konsole, wählen Sie in der Navigationsleiste **Policies** und dann **Create Policy** aus.<br><br>![Der Button „Create Policy“ in der AWS-Konsole.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Öffnen Sie den Tab **JSON** und geben Sie das folgende Code-Snippet in den Abschnitt **Policy Document** ein. Achten Sie darauf, `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen und `YOUR-SQS-ARN-HERE` durch den ARN Ihrer SQS-Warteschlange zu ersetzen:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. Wählen Sie **Review Policy**, wenn Sie fertig sind.

4. Geben Sie der Richtlinie einen Namen und eine Beschreibung und wählen Sie dann **Create Policy**.

![Eine Beispielrichtlinie mit dem Namen „new-policy-name“.]({% image_buster /assets/img/create_policy_3_name.png %})

![Das Beschreibungsfeld für die Richtlinie.]({% image_buster /assets/img/create_policy_4_created.png %})

### Schritt 6: IAM-Rolle erstellen {#step-6-create-an-iam-role}

Um die Einrichtung in AWS abzuschließen, erstellen Sie eine IAM-Rolle und hängen die IAM-Richtlinie aus Schritt 5 an.

1. Gehen Sie in demselben IAM-Bereich der Konsole, in dem Sie die IAM-Richtlinie erstellt haben, zu **Roles** > **Create Role**.

![Der Button „Create Role“.]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Wählen Sie in AWS **Another AWS Account** als Typ für vertrauenswürdige Entitäten aus. Geben Sie Ihre Braze-Konto-ID an. Aktivieren Sie das Kontrollkästchen **Require external ID**.
3. Gehen Sie in Braze zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Sources**, wählen Sie **Add data source** und dann **Amazon S3** im Abschnitt Dateiquellen.
4. Kopieren Sie die automatisch generierte **Braze Account ID**.

![Die Seite „Add New Source“ mit den Abschnitten „Source Name“ und „S3 Connection Details“.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Fügen Sie in AWS die Konto-ID ein und wählen Sie anschließend **Next**.

![Die S3-Seite „Create Role“. Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Hängen Sie die in Schritt 4 erstellte Richtlinie an die Rolle an. Suchen Sie die Richtlinie in der Suchleiste und setzen Sie ein Häkchen neben der Richtlinie, um sie anzuhängen. Wählen Sie anschließend **Next**.

![Rollen-ARN mit der ausgewählten Richtlinie „new-policy-name“.]({% image_buster /assets/img/create_role_3_attach.png %})

Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role**.

![Eine Beispielrolle mit dem Namen „new-role-name“.]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Notieren Sie sich den ARN der erstellten Rolle und die generierte externe ID, da Sie diese für die Erstellung der Cloud-Datenaufnahme-Integration benötigen.

## Cloud-Datenaufnahme in Braze einrichten {#setting-up-cloud-data-ingestion-in-braze}

1. Erstellen Sie zunächst eine neue Quelle im Braze-Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Sources**, wählen Sie **Add data source** und dann **Amazon S3**.
2. Wählen Sie einen Namen für Ihre Quelle und geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Quelle zu erstellen. Geben Sie Folgendes an:

  - Role ARN
  - External ID
  - Bucket-Name
  - Region

![Der Abschnitt „S3 Connection Details“ mit den Feldern für Zugangsdaten (AWS-Einrichtung und Braze-Einrichtung) und Konfiguration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Wählen Sie **Test connection**, um zu bestätigen, dass Braze auf Ihren Bucket zugreifen kann. Nach einem erfolgreichen Test wählen Sie **Connect to Source**. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{: start="4"}
4. Erstellen Sie als Nächstes eine neue Synchronisierung. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Syncs** und wählen Sie **Create data sync**.

{: start="5"}
5. Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann eine aktive S3-Quelle aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und wählen Sie **Test Connection**.

![Eine Option zum Testen der Verbindung mit einer Datenvorschau.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Geben Sie die restlichen Informationen aus dem AWS-Einrichtungsprozess ein. Geben Sie Folgendes an:
- SQS-URL (muss für jede neue Integration eindeutig sein)
- Ordnerpfad (optional, muss über Synchronisierungen in einem Workspace hinweg eindeutig sein)

7. Wählen Sie einen Datentyp und wählen Sie **Test Connection**, um zu bestätigen, dass Braze die zur Aufnahme verfügbaren Dateien auflisten kann (nicht die Daten in diesen Dateien). Nach Erfolg wählen Sie **Next: Notifications**.
8. Fügen Sie Kontakt-E-Mail-Adressen für Benachrichtigungen hinzu, falls die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Optional können Sie Benachrichtigungen für Fehler auf Nutzer:innen-Ebene und erfolgreiche Synchronisierungen aktivieren.
9. Erstellen Sie die Synchronisierung.

{% endtab %}
{% tab Google Cloud Storage %}

Die Integration erfordert die folgenden Ressourcen:

- Einen Cloud Storage-Bucket für die Datenspeicherung
- Ein Pub/Sub-Topic und ein Abo für Benachrichtigungen über neue Dateien
- Ein Dienstkonto, dessen JSON-Schlüssel Sie in Braze hochladen

### GCP-Definitionen {#gcp-definitions}

| Begriff | Definition |
| --- | --- |
| Google Cloud-Projekt | Ein Projekt organisiert alle Ihre Google Cloud-Ressourcen und wird durch eine eindeutige Projekt-ID und Projektnummer identifiziert. |
| Cloud Storage-Bucket | Ein Bucket ist der Container, der die Datendateien enthält, die Braze aufnehmen soll. |
| Pub/Sub-Topic | Ein Topic ist die benannte Ressource, die Benachrichtigungen über neue Dateien von Ihrem Cloud Storage-Bucket empfängt. |
| Pub/Sub-Abo | Ein Abo wird an ein Topic angehängt und liefert dessen Nachrichten. Braze konsumiert Benachrichtigungen über neue Dateien aus einem Pull-Abo. |
| Dienstkonto | Ein Dienstkonto ist eine nicht-menschliche Identität, die Braze verwendet, um auf Ihren Bucket und Ihr Abo zuzugreifen. Sie laden dessen JSON-Schlüssel in Braze hoch. |
| IAM-Rolle | Eine Identity and Access Management (IAM)-Rolle ist eine Sammlung von Berechtigungen, die Sie dem Dienstkonto für Ihren Bucket und Ihr Abo gewähren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCP-Definitionen" }

## Cloud-Datenaufnahme in Google Cloud einrichten {#setting-up-cloud-data-ingestion-in-google-cloud}

### Schritt 1: Cloud Storage-Bucket erstellen {#step-1-create-a-cloud-storage-bucket}

Gehen Sie in der Google Cloud-Konsole zu **Cloud Storage** > **Buckets** > **Create**. Notieren Sie sich die Projekt-ID und den Bucket-Namen – Sie benötigen diese, wenn Sie die Quelle in Braze konfigurieren. Wir empfehlen, den einheitlichen Zugriff auf Bucket-Ebene zu aktivieren, damit Berechtigungen über IAM verwaltet werden.

Alternativ können Sie den Bucket mit gcloud erstellen:

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### Schritt 2: Pub/Sub-Topic und -Abo erstellen {#step-2-create-a-pubsub-topic-and-subscription}

Gehen Sie in der Google Cloud-Konsole zu **Pub/Sub** > **Topics** > **Create topic**. Sie können Google ein Standard-Abo erstellen lassen oder eines separat anlegen. Erstellen Sie dann ein **Pull**-Abo für dieses Topic.

Alternativ verwenden Sie gcloud:

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

Notieren Sie sich die **Abo-ID** – Braze benötigt das Abo (nicht das Topic), wenn Sie die Synchronisierung erstellen. Das Abo muss ein Pull-Abo sein.

### Schritt 3: Bucket-Benachrichtigungen an das Topic senden {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
Das Erstellen einer Cloud Storage-zu-Pub/Sub-Benachrichtigung ist in der Google Cloud-Konsole nicht verfügbar. Sie müssen gcloud (hier gezeigt), Terraform oder die JSON-API verwenden. Weitere Informationen finden Sie unter [Configure Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes#enabling) in der Google Cloud-Dokumentation.
{% endalert %}

Gewähren Sie zunächst dem Cloud Storage-Dienst-Agenten die Berechtigung, in das Topic zu veröffentlichen, und erstellen Sie dann die Benachrichtigung für `OBJECT_FINALIZE`. Das Ereignis `OBJECT_FINALIZE` wird ausgelöst, wenn ein neues Objekt im Bucket erstellt oder finalisiert wird.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Grant it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

Ersetzen Sie die folgenden Platzhalter in diesen Befehlen:

- `YOUR-PROJECT-ID`: Ihre Google Cloud-Projekt-ID, der menschenlesbare Bezeichner (z. B. `my-gcp-project`).
- `YOUR-TOPIC`: Das Pub/Sub-Topic, das Sie in [Schritt 2](#step-2-create-a-pubsub-topic-and-subscription) erstellt haben.
- `YOUR-BUCKET-NAME`: Ihr Cloud Storage-Bucket-Name.
- `YOUR-PROJECT-NUMBER`: Ihre Projektnummer, der numerische Bezeichner, der in der E-Mail-Adresse des Cloud Storage-Dienst-Agenten verwendet wird. Diese unterscheidet sich von der Projekt-ID. Sie finden sie auf dem **Dashboard** in der Google Cloud-Konsole oder führen den folgenden Befehl aus:

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### Schritt 4: Dienstkonto erstellen {#step-4-create-a-service-account}

Gehen Sie in der Google Cloud-Konsole zu **IAM & Admin** > **Service Accounts** > **Create service account**.

Alternativ verwenden Sie gcloud:

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### Schritt 5: Berechtigungen gewähren {#step-5-grant-permissions}

Der Konnektor benötigt genau diese Berechtigungen: `storage.buckets.get`, `storage.objects.get` und `storage.objects.list` für den Bucket sowie `pubsub.subscriptions.consume` für das Abo. Sie können diese entweder mit einer benutzerdefinierten Rolle oder mit vordefinierten Rollen gewähren.

**Benutzerdefinierte Rolle:** Erstellen Sie eine benutzerdefinierte Rolle mit genau diesen Berechtigungen und binden Sie sie an den Bucket und das Abo:

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**Vordefinierte Rollen:** Gewähren Sie `roles/storage.objectViewer` und `roles/storage.legacyBucketReader` für den Bucket sowie `roles/pubsub.subscriber` für das Abo. Die Rolle `objectViewer` stellt `storage.objects.get` und `storage.objects.list` bereit, und `legacyBucketReader` stellt `storage.buckets.get` bereit:

```shell
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.legacyBucketReader"
gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

### Schritt 6: JSON-Schlüssel erstellen {#step-6-create-a-json-key}

Öffnen Sie in der Google Cloud-Konsole das Dienstkonto, gehen Sie zu **Keys** > **Add key** > **Create new key** und wählen Sie **JSON**.

Alternativ verwenden Sie gcloud:

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Cloud-Datenaufnahme in Braze einrichten

1. Gehen Sie in Braze zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Sources**, wählen Sie **Add data source** und dann **Google Cloud Storage**.

![Der Bildschirm „Add New Source“ mit Google Cloud Storage, ausgewählt aus der Liste der Datenquellen.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. Füllen Sie die Quellfelder aus:
    - **Bucket** – Ihr Bucket-Name
    - **Project ID** – Ihre GCP-Projekt-ID
    - **Service account JSON key** – Laden Sie die Schlüsseldatei aus Schritt 6 hoch und geben Sie den Zugangsdaten einen Namen

![Das Google Cloud Storage-Quellformular mit den Feldern für Bucket, Projekt-ID und Upload der Zugangsdaten.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. Wählen Sie **Test connection** und dann **Connect to Source**.
4. Erstellen Sie eine Synchronisierung. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Syncs** und wählen Sie **Create data sync**. Wählen Sie einen Synchronisierungsnamen und einen **Data Type** (z. B. **User Attributes**, **Custom Events**, **Purchase Events**, **Catalog** oder **Delete Users**) und wählen Sie dann **Next**.
5. Wählen Sie im Schritt **Data definition** Ihre GCS-Quelle aus und geben Sie Folgendes an:
    - **Pub/Sub subscription ID** – die Abo-ID aus Schritt 2 (nicht das Topic)
    - **Folder path** (optional) – ein Pfadpräfix innerhalb des Buckets (siehe [Ordner in einem gemeinsam genutzten Bucket synchronisieren](#syncing-a-folder-in-a-shared-bucket))

![Das Google Cloud Storage-Synchronisierungsformular mit den Feldern für Pub/Sub-Abo-ID und Ordnerpfad.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. Wählen Sie **Preview and validate**, um zu bestätigen, dass Braze das Abo erreichen und die zur Aufnahme verfügbaren Dateien auflisten kann. Ein erfolgreicher Test listet vorhandene Dateien im Bucket auf, diese Dateien werden jedoch nicht automatisch synchronisiert.
7. Fügen Sie Kontakt-E-Mail-Adressen für Fehlerbenachrichtigungen hinzu. Google Cloud Storage-Synchronisierungen sind ereignisgesteuert, sodass kein Zeitplan erforderlich ist – Braze nimmt neue Dateien auf, sobald sie hochgeladen werden. Überprüfen Sie die Zusammenfassung und wählen Sie dann **Create sync**.

### Ordner in einem gemeinsam genutzten Bucket synchronisieren {#syncing-a-folder-in-a-shared-bucket}

Sie können einen Bucket über mehrere Synchronisierungen hinweg wiederverwenden, aber jede Synchronisierung muss einen eigenen Ordner **und** ein eigenes dediziertes Pub/Sub-Abo verwenden.


{% alert important %}
Der Ordnerpfad und das Abo müssen über Synchronisierungen in einem Workspace hinweg eindeutig sein, wenn mehrere Synchronisierungen denselben Quell-Bucket verwenden.
{% endalert %}

Für jeden Ordner, den Sie in einem gemeinsam genutzten Bucket synchronisieren möchten:

1. Setzen Sie das Feld **Folder** der Synchronisierung auf das Pfadpräfix (z. B. `attributes/`). Braze listet und nimmt nur Objekte auf, deren Pfad mit diesem Präfix beginnt.
2. Erstellen Sie ein dediziertes Topic und eine präfixbezogene Benachrichtigung für diesen Ordner, und erstellen Sie dann ein Abo für dieses Topic:

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Grant the Cloud Storage service agent publisher on the topic
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # Notification scoped to the folder with --object-prefix
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # One subscription per sync
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. Gewähren Sie dem Braze-Dienstkonto die Berechtigung zum Konsumieren dieses Abos, wie in [Schritt 5](#step-5-grant-permissions):

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    Wenn Sie die benutzerdefinierte Rolle in [Schritt 5](#step-5-grant-permissions) erstellt haben, verwenden Sie stattdessen `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"`.
4. Wenn Sie die Synchronisierung in Braze erstellen, geben Sie die neue **Pub/Sub subscription ID** und den **Folder path** dieses Ordners ein, damit die Synchronisierung nur die Dateien dieses Ordners aufnimmt.


{% endtab %}
{% endtabs %}

## Erforderliche Dateiformate {#required-file-formats}

Die erforderlichen Dateiformate sind für Amazon S3 und Google Cloud Storage identisch. Die Cloud-Datenaufnahme unterstützt JSON-, CSV- und Parquet-Dateien. Die erforderlichen Spalten hängen vom Datentyp ab:

- Nutzerdaten (Attribute, angepasste Events, Kauf-Events) verwenden Nutzer-Bezeichner und einen Payload
- Katalogdaten verwenden Katalog-Bezeichner

Wenn Sie Dateispeicher für Katalogdaten verwenden, nutzen Sie diese Seite zusammen mit [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) für katalogspezifische Anforderungen und Verhaltensweisen.

Braze stellt keine zusätzlichen Anforderungen an Dateinamen über die Vorgaben Ihres Dateispeicheranbieters hinaus. Dateinamen sollten eindeutig sein. Das Anhängen eines Zeitstempels hilft, die Eindeutigkeit sicherzustellen.

Beispiele für alle unterstützten Dateitypen (Attribute, angepasste Events, Käufe, Kataloge und Nutzer-Löschungen) finden Sie in den Beispieldateien unter [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Nutzer-Bezeichner {#user-identifiers}

Für Nutzerdaten-Synchronisierungen (Attribute, angepasste Events, Kauf-Events) benötigt jede Zeile in Ihrer Quelldatei genau einen Nutzer-Bezeichner und eine `PAYLOAD`-Spalte. Eine Quelldatei kann Zeilen mit verschiedenen Bezeichnertypen enthalten, aber jede einzelne Zeile sollte nur einen verwenden.

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit verschiedenen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der Braze-Nutzer-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch die Cloud-Datenaufnahme erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefonnummer angeben, verwendet Braze die E-Mail als primären Bezeichner. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-Bezeichner" }

Zusätzlich zu einem Bezeichner muss jede Zeile eine `PAYLOAD`-Spalte enthalten, die einen JSON-String mit den Feldern enthält, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

{% alert note %}
Im Gegensatz zu Data-Warehouse-Quellen ist die Spalte `UPDATED_AT` für Dateispeicher-Synchronisierungen weder erforderlich noch unterstützt.
{% endalert %}

### Katalog-Bezeichner {#catalog-identifiers}

Für Katalog-Synchronisierungen muss Ihre Quelldatei die folgenden Spalten enthalten. Katalogdateien verwenden andere Bezeichner als Nutzerdaten-Dateien.

| Spalte | Erforderlich | Beschreibung |
| --- | --- | --- |
| `ID` | Ja | Der eindeutige Bezeichner für den Katalogartikel. Wird verwendet, um den Artikel in Braze zu erstellen, zu aktualisieren oder zu löschen. |
| `PAYLOAD` | Ja | Ein JSON-String der Katalogfelder und -werte, die synchronisiert werden sollen. Muss mit dem Schema Ihres Katalogs in Braze übereinstimmen. |
| `DELETED` | Nein | Wenn `true`, wird der Katalogartikel mit der übereinstimmenden `ID` aus dem Katalog in Braze entfernt. Lassen Sie diese Spalte weg oder setzen Sie sie auf `false` für Erstellungs- oder Aktualisierungsvorgänge. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Katalog-Bezeichner" }

### Beispiele {#examples}

{% tabs %}
{% tab JSON-Attribute %}
``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, andernfalls wird die Datei übersprungen.
{% endalert %}
{% endtab %}
{% tab Angepasste JSON-Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, andernfalls wird die Datei übersprungen.
{% endalert %}
{% endtab %}
{% tab JSON-Kauf-Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, andernfalls wird die Datei übersprungen.
{% endalert %}

{% endtab %}
{% tab CSV-Attribute %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV-Kataloge %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Fügen Sie eine optionale `DELETED`-Spalte hinzu. Wenn `DELETED` den Wert `true` hat, wird der entsprechende Katalogartikel aus dem Katalog in Braze entfernt. Die vollständige Liste der erforderlichen Spalten finden Sie unter [Katalog-Bezeichner](#catalog-identifiers). Informationen zum Löschverhalten finden Sie unter [Katalogartikel löschen](#deleting-catalog-items). Einen End-to-End-Ablauf für die Katalogeinrichtung (einschließlich Erstellung des Zielkatalogs und Synchronisierungsverhalten) finden Sie unter [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Daten löschen {#deleting-data}

Cloud-Datenaufnahme für Dateispeicher unterstützt das Löschen von Nutzer:innen und Katalogartikeln über Datei-Uploads. Verwenden Sie für jeden Vorgang separate Syncs und Dateiformate.

- **[Nutzer:innen löschen](#deleting-users)** – Erstellen Sie einen Sync mit dem Datentyp **Delete Users** und laden Sie Dateien hoch, die nur Nutzer-Bezeichner enthalten (kein Payload).
- **[Katalogartikel löschen](#deleting-catalog-items)** – Verwenden Sie Ihren bestehenden Katalog-Sync und fügen Sie eine Spalte `deleted` (oder `DELETED`) hinzu, um Artikel zur Entfernung zu markieren.

### Nutzer:innen löschen {#deleting-users}

So löschen Sie Nutzerprofile in Braze mithilfe von Dateien in Ihrem Quell-Bucket:

1. Erstellen Sie einen neuen Cloud-Datenaufnahme-Sync (gleiche Einrichtung wie bei anderen Syncs).
2. Setzen Sie beim Konfigurieren des Syncs in Braze den **Data Type** auf **Delete Users**.
3. Laden Sie Dateien in Ihren Quell-Bucket hoch, die nur Spalten mit Nutzer-Bezeichnern enthalten. Fügen Sie keine `PAYLOAD`-Spalte hinzu – der Sync schlägt fehl, wenn ein Payload vorhanden ist, um versehentliche Löschungen zu vermeiden.

Jede Zeile in der Datei muss genau eine:n Nutzer:in über einen der folgenden Bezeichner identifizieren:

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Entspricht der in Braze verwendeten `external_id`. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Beide Spalten zusammen identifizieren die/den Nutzer:in über den Alias. |
| `BRAZE_ID` | Von Braze generierte Nutzer-ID (nur bestehende Nutzer:innen). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen löschen" }

{% alert important %}
Das Löschen von Nutzer:innen ist dauerhaft und kann nicht rückgängig gemacht werden. Nehmen Sie nur Nutzer:innen auf, die Sie tatsächlich entfernen möchten. Weitere Informationen finden Sie unter [Nutzer:innen mit Cloud-Datenaufnahme löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
{% endalert %}

**Beispiel – JSON (Nutzer:innen löschen):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Beispiel – CSV (Nutzer:innen löschen):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Wenn der Sync ausgeführt wird, verarbeitet Braze neue Dateien im Bucket und löscht die entsprechenden Nutzerprofile.

### Katalogartikel löschen {#deleting-catalog-items}

So entfernen Sie Artikel aus einem Katalog mithilfe von Dateispeicher:

1. Verwenden Sie denselben Sync, den Sie zum [Synchronisieren von Katalogdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) verwenden (Datentyp **Catalogs**).
2. Fügen Sie in Ihren CSV- oder JSON-Dateien eine optionale Spalte **`deleted`** (oder **`DELETED`**) hinzu.
3. Setzen Sie `deleted` auf `true` für jeden Katalogartikel, den Sie aus dem Katalog in Braze entfernen möchten.

Jede Zeile benötigt weiterhin `ID` und `PAYLOAD`. Bei Zeilen, die zur Löschung markiert sind, kann der Payload minimal sein; Braze entfernt den Artikel anhand der `ID`.

**Beispiel – JSON (Katalogartikel löschen):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Beispiel – CSV (Katalogartikel löschen):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Wenn der Sync ausgeführt wird, bewirken Zeilen mit `deleted: true`, dass der entsprechende Katalogartikel in Braze gelöscht wird. Informationen zum vollständigen Verhalten bei Katalog-Sync und -Löschung finden Sie unter [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Wissenswertes {#things-to-know}

- Dateien, die dem Quell-Bucket hinzugefügt werden, sollten 512&nbsp;MB nicht überschreiten. Dieses Limit gilt sowohl für Amazon S3 als auch für Google Cloud Storage. Dateien, die größer als 512&nbsp;MB sind, führen zu einem Fehler und werden nicht mit Braze synchronisiert.
- Es gibt zwar kein zusätzliches Limit für die Anzahl der Zeilen pro Datei, wir empfehlen jedoch die Verwendung kleinerer Dateien, um die Geschwindigkeit Ihrer Synchronisierungen zu verbessern. Beispielsweise würde die Aufnahme einer 500&nbsp;MB großen Datei erheblich länger dauern als die von fünf separaten 100&nbsp;MB großen Dateien.
- Es gibt kein zusätzliches Limit für die Anzahl der Dateien, die in einem bestimmten Zeitraum hochgeladen werden.
- Eine Sortierung innerhalb von oder zwischen Dateien wird nicht unterstützt. Wir empfehlen, Aktualisierungen regelmäßig in Batches zusammenzufassen, wenn Sie auf erwartete Race-Conditions achten.

## Fehlerbehebung {#troubleshooting}

### Hochladen und Verarbeiten von Dateien {#uploading-files-and-processing}

CDI verarbeitet nur Dateien, die nach der Erstellung der Synchronisierung hinzugefügt werden. In diesem Prozess sucht Braze nach neu hinzugefügten Dateien, was eine neue Benachrichtigung auslöst. Dadurch wird eine neue Synchronisierung gestartet, um die neue Datei zu verarbeiten. Bei Amazon S3 ist die Benachrichtigung eine Nachricht an SQS. Bei Google Cloud Storage handelt es sich um eine `OBJECT_FINALIZE`-Nachricht an Pub/Sub.

Sie können vorhandene Dateien verwenden, um zu überprüfen, ob Braze auf Ihren Bucket zugreifen und Dateien zur Aufnahme erkennen kann. Diese werden jedoch nicht mit Braze synchronisiert. Damit CDI sie verarbeiten kann, müssen Sie alle vorhandenen Dateien, die synchronisiert werden sollen, erneut in den Quell-Bucket hochladen.

### Umgang mit unerwarteten Dateifehlern (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

Wenn Sie eine hohe Anzahl von Fehlern oder fehlgeschlagenen Dateien beobachten, haben Sie möglicherweise einen anderen Prozess, der Dateien in einem anderen Ordner als dem Zielordner für CDI zum S3-Bucket hinzufügt.

Wenn Dateien in den Quell-Bucket, aber nicht in den Quellordner hochgeladen werden, verarbeitet CDI die SQS-Benachrichtigung, führt jedoch keine Aktion für die Datei aus. Dies kann daher als Fehler erscheinen.

Wenn Ihr Problem mit S3-Benachrichtigungen oder SQS-Zielberechtigungen zusammenhängt (z. B. Fehler bei der Zielvalidierung), lesen Sie die AWS-Dokumentation:

- [Aktivieren und Konfigurieren von Ereignisbenachrichtigungen über die Amazon-S3-Konsole](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Erteilen von Berechtigungen zum Veröffentlichen von Ereignisbenachrichtigungen an ein Ziel](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Fehlerbehebung bei Problemen in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Umgang mit unerwarteten Dateifehlern (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Wie bei Amazon S3 verarbeitet CDI nur Dateien, die nach der Erstellung der Synchronisierung hochgeladen werden. Jedes neue Objekt löst eine `OBJECT_FINALIZE`-Nachricht an Ihr Pub/Sub-Topic aus. Um bereits im Bucket vorhandene Dateien aufzunehmen, laden Sie diese erneut hoch.

Wenn Dateien nicht aufgenommen werden, überprüfen Sie Folgendes:

- Die Bucket-Benachrichtigung existiert. Listen Sie die Benachrichtigungen für den Bucket mit `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME` auf.
- Der Cloud-Storage-Dienst-Agent hat `roles/pubsub.publisher` für das Topic.
- Das Braze-Dienstkonto hat die Berechtigung zum Konsumieren des Abos (`pubsub.subscriptions.consume`, erteilt entweder über die benutzerdefinierte Rolle oder `roles/pubsub.subscriber`).

Weitere Informationen finden Sie unter [Pub/Sub-Benachrichtigungen für Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) in der Google-Cloud-Dokumentation.