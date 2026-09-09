---
nav_title: Integrationen in die Dateiablage
article_title: Integrationen in die Dateiablage
description: "Diese Seite behandelt die Braze Cloud-Datenaufnahme und wie Sie relevante Daten von Amazon S3, Google Cloud Storage oder Azure Blob Storage mit Braze synchronisieren."
page_order: 4
page_type: reference

---

# Integrationen in die Dateiablage {#file-storage-integrations}

> Auf dieser Seite erfahren Sie, wie Sie die Cloud-Datenaufnahme einrichten, um Daten von Amazon S3, Google Cloud Storage oder Azure Blob Storage mit Braze zu synchronisieren.

## Funktionsweise {#how-it-works}

Sie können Cloud Data Ingestion (CDI) verwenden, um einen oder mehrere Storage-Buckets in Ihrem Cloud-Konto direkt mit Braze zu integrieren. Wenn Sie eine neue Datei zu einem Bucket hinzufügen, veröffentlicht Ihr Cloud-Anbieter eine Benachrichtigung, und Braze Cloud Data Ingestion synchronisiert die Daten.

Der Benachrichtigungsmechanismus hängt von Ihrem Anbieter ab:

- **Amazon S3:** Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an eine Amazon Simple Queue Service (SQS)-Warteschlange gesendet, und Braze verarbeitet diese Nachricht, um die neue Datei aufzunehmen.
- **Google Cloud Storage (GCS):** Wenn neue Dateien im Bucket finalisiert werden, veröffentlicht GCS eine `OBJECT_FINALIZE`-Benachrichtigung an ein Pub/Sub-Topic. Braze verarbeitet diese Benachrichtigungen aus einem Pub/Sub-Abonnement, um die neue Datei aufzunehmen.
- **Azure Blob Storage:** Wenn neue Dateien im Container erstellt werden, veröffentlicht ein Event-Abonnement in Azure Event Grid ein **Blob Created**-Ereignis an eine Azure Storage-Warteschlange. Braze liest diese Nachrichten aus der Warteschlange, um die neue Datei aufzunehmen.

Cloud Data Ingestion unterstützt Folgendes:

- JSON-Dateien
- CSV-Dateien
- Parquet-Dateien
- Attribut-, angepasste Event-, Kauf-Event-, Nutzerlöschungs- und Katalogdaten

## Cloud Data Ingestion einrichten {#setting-up-cloud-data-ingestion}

Die Einrichtungsschritte hängen von Ihrem Dateispeicheranbieter ab. Wählen Sie den Tab für Ihren Anbieter und führen Sie dann die gemeinsame Konfiguration in den folgenden Abschnitten durch.

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
| Identity and Access Management (IAM) | IAM ist ein Webdienst, mit dem Sie den Zugriff auf AWS-Ressourcen sicher steuern können. In diesem Tutorial erstellen Sie eine IAM-Richtlinie und weisen sie einer IAM-Rolle zu, um Ihren S3-Bucket mit Braze Cloud Data Ingestion zu integrieren. |
| Amazon Simple Queue Service (SQS) | SQS ist eine gehostete Warteschlange, mit der Sie verteilte Softwaresysteme und -komponenten integrieren können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWS-Definitionen" }

## Cloud Data Ingestion in AWS einrichten {#setting-up-cloud-data-ingestion-in-aws}

### Schritt 1: Quell-Bucket erstellen {#step-1-create-a-source-bucket}

Erstellen Sie einen S3-Allzweck-Bucket mit Standardeinstellungen in Ihrem AWS-Konto. S3-Buckets können über mehrere Synchronisierungen hinweg wiederverwendet werden, solange der Ordner eindeutig ist.

Die Standardeinstellungen sind:

- ACLs deaktiviert
- Gesamten öffentlichen Zugriff blockieren
- Bucket-Versionierung deaktivieren
- SSE-S3-Verschlüsselung
  - SSE-S3 ist der einzige unterstützte serverseitige Verschlüsselungstyp. Amazon-KMS-Verschlüsselung wird nicht unterstützt.

Notieren Sie sich die Region, in der Sie den Bucket erstellt haben. Sie werden im nächsten Schritt eine SQS-Warteschlange in derselben Region erstellen.

### Schritt 2: SQS-Warteschlange erstellen {#step-2-create-sqs-queue}

Erstellen Sie eine SQS-Warteschlange, um nachzuverfolgen, wann Objekte zum erstellten Bucket hinzugefügt werden. Verwenden Sie vorerst die Standardkonfigurationseinstellungen.

Eine SQS-Warteschlange muss global eindeutig sein (es kann beispielsweise nur eine für eine CDI-Synchronisierung verwendet werden und sie kann nicht in einem anderen Workspace wiederverwendet werden).

{% alert important %}
Stellen Sie sicher, dass Sie diese SQS in derselben Region erstellen, in der Sie den Bucket erstellt haben.
{% endalert %}

Notieren Sie sich den ARN und die URL der SQS-Warteschlange. Sie werden sie während dieser Konfiguration häufig benötigen.

![Auswahl von „Advanced“ mit einem beispielhaften JSON-Objekt zur Definition, wer auf eine Warteschlange zugreifen kann.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Schritt 3: Zugriffsrichtlinie einrichten {#step-3-set-up-access-policy}

Um die Zugriffsrichtlinie einzurichten, wählen Sie **Advanced options**.

Fügen Sie die folgende Anweisung an die Zugriffsrichtlinie der Warteschlange an und ersetzen Sie dabei `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen, `YOUR-SQS-ARN` durch Ihren SQS-Warteschlangen-ARN und `YOUR-AWS-ACCOUNT-ID` durch Ihre AWS-Konto-ID:

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

### Schritt 4: Event-Benachrichtigung zum S3-Bucket hinzufügen {#step-4-add-an-event-notification-to-the-s3-bucket}

1. Gehen Sie im in Schritt 1 erstellten Bucket zu **Properties** > **Event notifications**.
2. Geben Sie der Konfiguration einen Namen. Optional können Sie ein Präfix oder Suffix angeben, wenn nur eine Teilmenge der Dateien von Braze aufgenommen werden soll.
3. Wählen Sie unter **Destination** die Option **SQS queue** und geben Sie den ARN der in Schritt 2 erstellten SQS an.

{% alert note %}
Wenn Sie Ihre Dateien in den Stammordner eines S3-Buckets hochladen und dann einige der Dateien in einen bestimmten Ordner im Bucket verschieben, kann ein unerwarteter Fehler auftreten. Stattdessen können Sie die Event-Benachrichtigungen so konfigurieren, dass sie nur für Dateien im Präfix gesendet werden, keine Dateien außerhalb dieses Präfixes im S3-Bucket ablegen oder die Integration ohne Präfix aktualisieren, wodurch dann alle Dateien aufgenommen werden.
{% endalert %}

### Schritt 5: IAM-Richtlinie erstellen {#step-5-create-an-iam-policy}

Erstellen Sie eine IAM-Richtlinie, um Braze die Interaktion mit Ihrem Quell-Bucket zu ermöglichen. Melden Sie sich zunächst als Kontoadministrator:in bei der AWS-Managementkonsole an.

1. Gehen Sie zum IAM-Bereich der AWS-Konsole, wählen Sie **Policies** in der Navigationsleiste und dann **Create Policy**.<br><br>![Der Button „Create policy“ in der AWS-Konsole.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Öffnen Sie den Tab **JSON** und geben Sie den folgenden Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie dabei `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen und `YOUR-SQS-ARN-HERE` durch den Namen Ihrer SQS-Warteschlange:

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

Um die Einrichtung in AWS abzuschließen, erstellen Sie eine IAM-Rolle und hängen Sie die IAM-Richtlinie aus Schritt 5 daran an.

1. Gehen Sie im selben IAM-Bereich der Konsole, in dem Sie die IAM-Richtlinie erstellt haben, zu **Roles** > **Create Role**.

![Der Button „Create role“.]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Wählen Sie in AWS **Another AWS Account** als Typ der vertrauenswürdigen Entität. Geben Sie Ihre Braze-Konto-ID ein. Aktivieren Sie das Kontrollkästchen **Require external ID**.
3. Gehen Sie in Braze zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Amazon S3** im Abschnitt für Dateiquellen.
4. Kopieren Sie die automatisch generierte **Braze Account ID**.

![Die Seite „Add New Source“ mit den Abschnitten „Source Name“ und „S3 Connection Details“.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Fügen Sie in AWS die Konto-ID ein und wählen Sie dann **Next**.

![Die S3-Seite „Create Role“. Diese Seite enthält Felder für Rollenname, Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und Berechtigungsgrenze.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Hängen Sie die in Schritt 4 erstellte Richtlinie an die Rolle an. Suchen Sie die Richtlinie in der Suchleiste und setzen Sie ein Häkchen neben der Richtlinie, um sie anzuhängen. Wählen Sie **Next**, wenn Sie fertig sind.

![Rollen-ARN mit ausgewählter „new-policy-name“.]({% image_buster /assets/img/create_role_3_attach.png %})

Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role**.

![Eine Beispielrolle mit dem Namen „new-role-name“.]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Notieren Sie sich den ARN der erstellten Rolle und die generierte externe ID, da Sie diese für die Erstellung der Cloud-Data-Ingestion-Integration benötigen.

## Cloud Data Ingestion in Braze einrichten {#setting-up-cloud-data-ingestion-in-braze}

1. Erstellen Sie zunächst eine neue Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Amazon S3**.
2. Geben Sie Ihrer Quelle einen Namen und geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Quelle zu erstellen. Geben Sie Folgendes an:

  - Role ARN
  - External ID
  - Bucket-Name
  - Region

![Der Abschnitt „S3 Connection Details“ mit den Feldern für Zugangsdaten (AWS-Einrichtung und Braze-Einrichtung) und Konfiguration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Wählen Sie **Test connection**, um zu bestätigen, dass Braze auf Ihren Bucket zugreifen kann. Nach einem erfolgreichen Test wählen Sie **Connect to Source**. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{: start="4"}
4. Erstellen Sie als Nächstes eine neue Synchronisierung. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs** und wählen Sie **Create data sync**.

{: start="5"}
5. Geben Sie Ihrer Synchronisierung einen Namen. Wählen Sie dann eine aktive S3-Quelle aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und wählen Sie **Test Connection**.

![Eine Option zum Testen der Verbindung mit einer Datenvorschau.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Geben Sie die restlichen Informationen aus dem AWS-Einrichtungsprozess ein. Geben Sie Folgendes an:
- SQS-URL (muss für jede neue Integration eindeutig sein)
- Ordnerpfad (optional, muss über alle Synchronisierungen in einem Workspace hinweg eindeutig sein)

7. Wählen Sie einen Datentyp und wählen Sie **Test Connection**, um zu bestätigen, dass Braze die zur Aufnahme verfügbaren Dateien auflisten kann (nicht die Daten in diesen Dateien). Nach Erfolg wählen Sie **Next: Notifications**.
8. Fügen Sie Kontakt-E-Mail-Adressen für Benachrichtigungen hinzu, falls die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Optional können Sie Benachrichtigungen für Fehler auf Nutzer:innenebene und erfolgreiche Synchronisierungen aktivieren.
9. Erstellen Sie die Synchronisierung.

{% endtab %}
{% tab Google Cloud Storage %}

Die Integration erfordert die folgenden Ressourcen:

- Einen Cloud-Storage-Bucket für die Datenspeicherung
- Ein Pub/Sub-Topic und ein Abo für Benachrichtigungen über neue Dateien
- Ein Dienstkonto, dessen JSON-Schlüssel Sie in Braze hochladen

### GCP-Definitionen {#gcp-definitions}

| Begriff | Definition |
| --- | --- |
| Google-Cloud-Projekt | Ein Projekt organisiert alle Ihre Google-Cloud-Ressourcen und wird durch eine eindeutige Projekt-ID und Projektnummer identifiziert. |
| Cloud-Storage-Bucket | Ein Bucket ist der Container, der die Datendateien enthält, die Braze aufnehmen soll. |
| Pub/Sub-Topic | Ein Topic ist die benannte Ressource, die Benachrichtigungen über neue Dateien von Ihrem Cloud-Storage-Bucket empfängt. |
| Pub/Sub-Abo | Ein Abo ist an ein Topic angehängt und stellt dessen Nachrichten zu. Braze konsumiert Benachrichtigungen über neue Dateien aus einem Pull-Abo. |
| Dienstkonto | Ein Dienstkonto ist eine nicht-menschliche Identität, die Braze verwendet, um auf Ihren Bucket und Ihr Abo zuzugreifen. Sie laden seinen JSON-Schlüssel in Braze hoch. |
| IAM-Rolle | Eine Identity-and-Access-Management-Rolle (IAM-Rolle) ist eine Sammlung von Berechtigungen, die Sie dem Dienstkonto für Ihren Bucket und Ihr Abo zuweisen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCP-Definitionen" }

## Cloud Data Ingestion in Google Cloud einrichten {#setting-up-cloud-data-ingestion-in-google-cloud}

### Schritt 1: Cloud-Storage-Bucket erstellen {#step-1-create-a-cloud-storage-bucket}

Gehen Sie in der Google-Cloud-Konsole zu **Cloud Storage** > **Buckets** > **Create**. Notieren Sie sich die Projekt-ID und den Bucket-Namen. Sie benötigen beides, wenn Sie die Quelle in Braze konfigurieren. Wir empfehlen, den einheitlichen Zugriff auf Bucket-Ebene zu aktivieren, damit Berechtigungen über IAM verwaltet werden.

Alternativ können Sie den Bucket mit gcloud erstellen:

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### Schritt 2: Pub/Sub-Topic und Abo erstellen {#step-2-create-a-pubsub-topic-and-subscription}

Gehen Sie in der Google-Cloud-Konsole zu **Pub/Sub** > **Topics** > **Create topic**. Sie können Google ein Standard-Abo erstellen lassen oder eines separat anlegen. Erstellen Sie dann ein **Pull**-Abo für dieses Topic.

Alternativ verwenden Sie gcloud:

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

Notieren Sie sich die **Abo-ID**. Braze benötigt das Abo (nicht das Topic), wenn Sie die Synchronisierung erstellen. Das Abo muss ein Pull-Abo sein.

{% alert warning %}
Konfigurieren Sie keine Dead-Letter-Warteschlange für dieses Abo. Braze unterstützt keine Dead-Letter-Warteschlangen für Cloud-Data-Ingestion-Abos. Weitere Informationen finden Sie unter [Dead-Letter-Topics](https://cloud.google.com/pubsub/docs/dead-letter-topics) in der Google-Cloud-Dokumentation.
{% endalert %}

### Schritt 3: Bucket-Benachrichtigungen an das Topic senden {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
Das Erstellen einer Cloud-Storage-zu-Pub/Sub-Benachrichtigung ist in der Google-Cloud-Konsole nicht verfügbar. Sie müssen gcloud (hier gezeigt), Terraform oder die JSON API verwenden. Weitere Informationen finden Sie unter [Pub/Sub-Benachrichtigungen für Cloud Storage konfigurieren](https://cloud.google.com/storage/docs/reporting-changes#enabling) in der Google-Cloud-Dokumentation.
{% endalert %}

Weisen Sie zunächst dem Cloud-Storage-Dienst-Agenten die Berechtigung zum Veröffentlichen im Topic zu und erstellen Sie dann die Benachrichtigung für `OBJECT_FINALIZE`. Das Ereignis `OBJECT_FINALIZE` wird ausgelöst, wenn ein neues Objekt im Bucket erstellt oder finalisiert wird.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Assign it Pub/Sub Publisher on the topic
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

- `YOUR-PROJECT-ID`: Ihre Google-Cloud-Projekt-ID, der für Menschen lesbare Bezeichner (zum Beispiel `my-gcp-project`).
- `YOUR-TOPIC`: Das Pub/Sub-Topic, das Sie in [Schritt 2](#step-2-create-a-pubsub-topic-and-subscription) erstellt haben.
- `YOUR-BUCKET-NAME`: Ihr Cloud-Storage-Bucket-Name.
- `YOUR-PROJECT-NUMBER`: Ihre Projektnummer, der numerische Bezeichner, der in der E-Mail-Adresse des Cloud-Storage-Dienst-Agenten verwendet wird. Diese unterscheidet sich von der Projekt-ID. Sie finden sie auf dem **Dashboard** in der Google-Cloud-Konsole oder können den folgenden Befehl ausführen:

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### Schritt 4: Dienstkonto erstellen {#step-4-create-a-service-account}

Gehen Sie in der Google-Cloud-Konsole zu **IAM & Admin** > **Service Accounts** > **Create service account**.

Alternativ verwenden Sie gcloud:

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### Schritt 5: Berechtigungen zuweisen {#step-5-assign-permissions}

Der Konnektor benötigt genau diese Berechtigungen: `storage.buckets.get`, `storage.objects.get` und `storage.objects.list` für den Bucket sowie `pubsub.subscriptions.consume` für das Abo. Sie können sie entweder mit einer benutzerdefinierten Rolle oder mit vordefinierten Rollen zuweisen.

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

**Vordefinierte Rollen:** Weisen Sie `roles/storage.objectViewer` und `roles/storage.legacyBucketReader` für den Bucket sowie `roles/pubsub.subscriber` für das Abo zu. Die Rolle `objectViewer` gewährt `storage.objects.get` und `storage.objects.list`, und `legacyBucketReader` gewährt `storage.buckets.get`:

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

Öffnen Sie in der Google-Cloud-Konsole das Dienstkonto, gehen Sie zu **Keys** > **Add key** > **Create new key** und wählen Sie **JSON**.

Alternativ verwenden Sie gcloud:

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Cloud Data Ingestion in Braze einrichten {#setting-up-cloud-data-ingestion-in-braze-gcs}

1. Gehen Sie in Braze zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Google Cloud Storage**.

![Der Bildschirm „Add New Source“ mit Google Cloud Storage, ausgewählt aus der Liste der Datenquellen.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. Füllen Sie die Quellenfelder aus:
    - **Bucket:** Ihr Bucket-Name
    - **Project ID:** Ihre GCP-Projekt-ID
    - **Service account JSON key:** Laden Sie die Schlüsseldatei aus Schritt 6 hoch und geben Sie den Zugangsdaten einen Namen

![Das Google-Cloud-Storage-Quellenformular mit den Feldern für Bucket, Projekt-ID und Upload der Zugangsdaten.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. Wählen Sie **Test connection** und dann **Connect to Source**.
4. Erstellen Sie eine Synchronisierung. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs** und wählen Sie **Create data sync**. Geben Sie einen Synchronisierungsnamen und einen **Data Type** an (z. B. **User Attributes**, **Custom Events**, **Purchase Events**, **Catalog** oder **Delete Users**) und wählen Sie dann **Next**.
5. Wählen Sie im Schritt **Data definition** Ihre GCS-Quelle aus und geben Sie dann Folgendes an:
    - **Pub/Sub subscription ID:** die Abo-ID aus Schritt 2 (nicht das Topic)
    - **Folder path** (optional): ein Pfadpräfix innerhalb des Buckets (siehe [Einen Ordner in einem gemeinsam genutzten Bucket synchronisieren](#syncing-a-folder-in-a-shared-bucket))

![Das Google-Cloud-Storage-Synchronisierungsformular mit den Feldern für Pub/Sub-Abo-ID und Ordnerpfad.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. Wählen Sie **Preview and validate**, um zu bestätigen, dass Braze das Abo erreichen und die zur Aufnahme verfügbaren Dateien auflisten kann. Ein erfolgreicher Test listet vorhandene Dateien im Bucket auf, aber diese Dateien werden nicht automatisch synchronisiert.
7. Fügen Sie Kontakt-E-Mail-Adressen für Fehlerbenachrichtigungen hinzu. Google-Cloud-Storage-Synchronisierungen sind ereignisgesteuert, sodass kein Zeitplan erforderlich ist. Braze nimmt neue Dateien auf, sobald sie hochgeladen werden. Überprüfen Sie die Zusammenfassung und wählen Sie dann **Create sync**.

### Einen Ordner in einem gemeinsam genutzten Bucket synchronisieren {#syncing-a-folder-in-a-shared-bucket}

Sie können einen Bucket über mehrere Synchronisierungen hinweg wiederverwenden, aber jede Synchronisierung muss einen eigenen Ordner **und** ein eigenes dediziertes Pub/Sub-Abo verwenden.


{% alert important %}
Der Ordnerpfad und das Abo müssen beide über alle Synchronisierungen in einem Workspace hinweg eindeutig sein, wenn mehrere Synchronisierungen denselben Quell-Bucket nutzen. Wie in [Schritt 2](#step-2-create-a-pubsub-topic-and-subscription) beschrieben, konfigurieren Sie keine Dead-Letter-Warteschlange für diese Abos.
{% endalert %}

Für jeden Ordner, den Sie in einem gemeinsam genutzten Bucket synchronisieren möchten:

1. Setzen Sie das Feld **Folder** der Synchronisierung auf das Pfadpräfix (zum Beispiel `attributes/`). Braze listet und nimmt nur Objekte auf, deren Pfad mit diesem Präfix beginnt.
2. Erstellen Sie ein dediziertes Topic und eine präfixbezogene Benachrichtigung für diesen Ordner und erstellen Sie dann ein Abo für dieses Topic:

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Assign the Cloud Storage service agent publisher on the topic
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

3. Weisen Sie dem Braze-Dienstkonto die Consume-Berechtigung für dieses Abo zu, wie in [Schritt 5](#step-5-assign-permissions):

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    Wenn Sie die benutzerdefinierte Rolle in [Schritt 5](#step-5-assign-permissions) erstellt haben, verwenden Sie stattdessen `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"`.
4. Wenn Sie die Synchronisierung in Braze erstellen, geben Sie die neue **Pub/Sub subscription ID** und den **Folder path** dieses Ordners ein, damit die Synchronisierung nur die Dateien dieses Ordners aufnimmt.


{% endtab %}
{% tab Azure Blob %}

Die Integration erfordert die folgenden Ressourcen:

- Ein Speicherkonto mit einem Blob-Container für die Datenspeicherung
- Eine Azure-Storage-Warteschlange und ein Ereignisabo für Benachrichtigungen über neue Dateien
- Einen Microsoft-Entra-ID-Dienstprinzipal, den CDI zum Lesen des Containers und der Warteschlange verwendet

### Azure-Definitionen {#azure-definitions}

| Begriff | Definition |
| --- | --- |
| Speicherkonto | Ein Speicherkonto ist die übergeordnete Azure-Ressource, die sowohl den Container, aus dem CDI Dateien liest, als auch die Warteschlange, aus der CDI Benachrichtigungen liest, enthält. |
| Container | Ein Container enthält die Datendateien, die CDI aufnehmen soll. Container befinden sich innerhalb eines Speicherkontos. |
| Azure-Storage-Warteschlange | Eine Warteschlange empfängt Benachrichtigungen über neue Dateien aus Ihrem Container. CDI liest und bestätigt Nachrichten aus dieser Warteschlange, um zu wissen, welche Dateien aufgenommen werden sollen. |
| Ereignisabo | Ein Ereignisabo leitet Ereignisse von Ihrem Speicherkonto an ein Ziel weiter, wobei der Azure-Event-Grid-Dienst verwendet wird. Sie konfigurieren es so, dass **Blob Created**-Ereignisse an Ihre Warteschlange gesendet werden. |
| Systemtopic | Ein Systemtopic repräsentiert die Quelle der Ereignisse. Event Grid erstellt eines für Ihr Speicherkonto, wenn Sie das erste Ereignisabo hinzufügen. |
| Dienstprinzipal | Ein Dienstprinzipal ist eine Microsoft-Entra-ID-Identität, als die sich CDI authentifiziert. Sie erstellen ihn über eine App-Registrierung und geben seine Zugangsdaten in Braze ein. |
| Azure-Rollenzuweisung | Eine Rollenzuweisung gewährt einem Dienstprinzipal eine Reihe von Berechtigungen in einem bestimmten Bereich. Sie weisen dem Braze-Dienstprinzipal zwei integrierte Rollen für Ihr Speicherkonto zu. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Azure-Definitionen" }

## Cloud Data Ingestion in Azure einrichten {#setting-up-cloud-data-ingestion-in-azure}

### Schritt 1: Container erstellen {#step-1-create-a-container}

Der Container und die Warteschlange müssen sich im selben Speicherkonto befinden. Sie können ein vorhandenes Speicherkonto wiederverwenden. Wenn Sie noch keines haben, gehen Sie im Azure-Portal zu **Storage accounts** > **+ Create**, um eines zu erstellen.

1. Gehen Sie im Azure-Portal zu Ihrem Speicherkonto und dann zu **Data storage** > **Containers**.
2. Wählen Sie **+ Add container** und geben Sie ihm einen Namen.

Notieren Sie sich den Namen des Speicherkontos und den Containernamen. Sie benötigen beides, wenn Sie die Quelle in Braze konfigurieren.

### Schritt 2: Warteschlange erstellen {#azure-step-2}

1. Gehen Sie im selben Speicherkonto zu **Data storage** > **Queues**.
2. Wählen Sie **+ Queue** und geben Sie ihr einen Namen.

Notieren Sie sich den Warteschlangennamen. Sie benötigen ihn, wenn Sie die Synchronisierung erstellen, und jede Synchronisierung benötigt ihre eigene Warteschlange.

### Schritt 3: Ereignisabo erstellen {#azure-step-3}

Erstellen Sie ein Ereignisabo, damit Ihr Container die Warteschlange benachrichtigt, wenn eine Datei eintrifft.

1. Gehen Sie im selben Speicherkonto zu **Events** und wählen Sie dann **+ Event Subscription**.
2. Geben Sie unter **Event Subscription Details** einen **Name** ein und setzen Sie **Event Schema** auf **Event Grid Schema**.
3. Überprüfen Sie unter **Topic Details** den **System Topic Name**. Wenn Ihr Speicherkonto noch kein Systemtopic hat, geben Sie einen Namen ein, um eines zu erstellen. Wenn bereits eines vorhanden ist, zeigt das Feld diesen Namen an und kann nicht geändert werden. Alle Ereignisabos eines Speicherkontos verwenden dasselbe Systemtopic.
4. Setzen Sie unter **Event Types** den Filter **Filter to Event Types** auf nur **Blob Created**. **Blob Deleted** ist ebenfalls standardmäßig ausgewählt – deaktivieren Sie es.
5. Setzen Sie unter **Endpoint Details** den **Endpoint Type** auf **Storage Queue**. Der Link **Configure an endpoint** erscheint, nachdem Sie einen Endpunkttyp gewählt haben.
6. Wählen Sie **Configure an endpoint** und dann das Speicherkonto, mit dem Sie arbeiten.
7. Wählen Sie **Select existing queue** und dann die Warteschlange, die Sie in Schritt 2 erstellt haben.
8. Wählen Sie **Select**, um den Endpunkt zu bestätigen.
9. Wählen Sie **Create**.

### Schritt 4: Dienstprinzipal erstellen {#step-4-create-a-service-principal}

CDI verbindet sich mit Ihrem Speicherkonto über einen Dienstprinzipal mit Microsoft-Entra-ID-Authentifizierung. Braze benötigt die folgenden Details für die Verbindung:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

Das Registrieren einer Anwendung erfordert die Berechtigung zum Erstellen von App-Registrierungen in Microsoft Entra ID. Wenn Sie diese Berechtigung nicht haben, bitten Sie eine:n Entra-Administrator:in, diesen Schritt abzuschließen und die Zugangsdaten mit Ihnen zu teilen.

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure erlaubt keine unbegrenzte Gültigkeitsdauer für Dienstprinzipal-Secrets. Denken Sie daran, die Zugangsdaten vor Ablauf zu erneuern, um den Datenfluss zu Braze aufrechtzuerhalten.
{% endalert %}

Wir empfehlen, einen Dienstprinzipal zu erstellen, der ausschließlich für CDI verwendet wird, damit sein Zugriff auf den Container und die Warteschlange beschränkt bleibt, die Sie synchronisieren. Wenn Sie bereits einen für eine Microsoft-Fabric-Quelle eingerichtet haben, können Sie ihn wiederverwenden – er hat dann jedoch Zugriff auf beides. In jedem Fall benötigt er die Rollenzuweisungen im nächsten Schritt.

### Schritt 5: Dem Dienstprinzipal Berechtigungen zuweisen {#step-5-assign-permissions-to-the-service-principal}

CDI benötigt nur genügend Zugriff, um Ihre Dateien zu lesen und Warteschlangennachrichten zu verarbeiten. Weisen Sie diese beiden integrierten Rollen auf dem Speicherkonto selbst zu – nicht auf der Abonnement- oder Ressourcengruppenebene, da Rollenzuweisungen nach unten vererbt werden. Weisen Sie keine umfassenderen Rollen wie Storage Blob Data Contributor, Storage Account Contributor oder Owner zu, die Schreib- und Verwaltungsberechtigungen gewähren, die CDI nie benötigt.

1. Gehen Sie zu Ihrem Speicherkonto und dann zu **Access Control (IAM)**.
2. Wählen Sie **Add** > **Add role assignment**.
3. Suchen Sie den Dienstprinzipal, den Sie in Schritt 4 erstellt haben, anhand seines Namens.
4. Weisen Sie ihm die folgenden integrierten Rollen zu:
    - **Storage Blob Data Reader:** Ermöglicht CDI das Lesen der Dateien in Ihrem Container.
    - **Storage Queue Data Message Processor:** Ermöglicht CDI das Anzeigen, Abrufen und Löschen von Nachrichten in Ihrer Warteschlange.

Sie können stattdessen auch eine benutzerdefinierte Rolle verwenden, solange sie nur Lesezugriff auf Blobs im Container und die Möglichkeit gewährt, Nachrichten in der Warteschlange zu empfangen und zu löschen.

{% alert note %}
Wenn **Add role assignment** ausgegraut ist, kann Ihr Konto keine Rollen für dieses Speicherkonto zuweisen. Dies erfordert eine Rolle wie Owner oder User Access Administrator. Bitten Sie eine:n Azure-Administrator:in, diesen Schritt abzuschließen.
{% endalert %}

## Cloud Data Ingestion in Braze einrichten {#setting-up-cloud-data-ingestion-in-braze-azure}

1. Gehen Sie in Braze zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Azure Blob**.

![Der Bildschirm „Add New Source“ mit Azure Blob, ausgewählt aus der Liste der Datenquellen.]({% image_buster /assets/img/cloud_ingestion/abs_source_picker.png %})

{: start="2"}
2. Füllen Sie die Felder unter **Azure Blob Connection Details** aus:
    - **Credentials:** **Tenant ID**, **Principal ID** und **Client Secret**
    - **Configuration:** **Storage account** und **Container**

![Das Azure-Blob-Verbindungsdetailformular mit den Feldern für Mandanten-ID, Prinzipal-ID, Client-Secret, Speicherkonto und Container.]({% image_buster /assets/img/cloud_ingestion/abs_source_form.png %})

{: start="3"}
3. Wählen Sie **Test connection** und dann **Connect to Source**.
4. Erstellen Sie eine Synchronisierung. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs** und wählen Sie **Create data sync**.
5. Wählen Sie unter **Configurations** einen Synchronisierungsnamen, wählen Sie Ihre Azure-Blob-Quelle aus und wählen Sie einen **Data Type** (z. B. **User Attributes**, **Custom Events**, **Purchase Events**, **Catalog** oder **Delete Users**).
6. Geben Sie unter **Data definition** Folgendes an:
    - **Storage queue name:** die Warteschlange, die Sie in [Schritt 2](#azure-step-2) erstellt haben. Jede Synchronisierung benötigt ihre eigene Warteschlange (siehe [Einen Ordner in einem gemeinsam genutzten Container synchronisieren](#syncing-a-folder-in-a-shared-container)).
    - **Folder path (Optional):** ein Pfadpräfix innerhalb des Containers

![Das Azure-Blob-Synchronisierungsformular mit den Feldern für Warteschlangenname und Ordnerpfad.]({% image_buster /assets/img/cloud_ingestion/abs_sync_form.png %})

{: start="7"}
7. Wählen Sie **Preview and validate**, um zu bestätigen, dass CDI die Warteschlange erreichen und die zur Aufnahme verfügbaren Dateien auflisten kann. Ein erfolgreicher Test listet vorhandene Dateien im Container auf, aber diese Dateien werden nicht automatisch synchronisiert. Die Synchronisierung wird erst aktiv, wenn die Verbindung erfolgreich validiert wurde.
8. Fügen Sie unter **Notifications** Kontakt-E-Mail-Adressen für Fehlerbenachrichtigungen hinzu.
9. **Schedule** bietet keine Optionen für Dateispeicher-Synchronisierungen. Azure-Blob-Storage-Synchronisierungen sind ereignisgesteuert, sodass CDI neue Dateien aufnimmt, sobald sie hochgeladen werden.
10. Überprüfen Sie die **Summary** und wählen Sie dann **Create sync**.

### Einen Ordner in einem gemeinsam genutzten Container synchronisieren {#syncing-a-folder-in-a-shared-container}

Sie können einen Container über mehrere Synchronisierungen hinweg wiederverwenden, aber jede Synchronisierung benötigt ihre eigene Speicherwarteschlange und ihren eigenen Ordner.

{% alert important %}
Zwei Synchronisierungen können nicht dieselbe Speicherwarteschlange verwenden. Wenn Sie eine Warteschlange eingeben, die bereits von einer anderen Synchronisierung verwendet wird, kennzeichnet CDI dies und verlinkt auf die bestehende Synchronisierung.
{% endalert %}

Für jeden Ordner, den Sie in einem gemeinsam genutzten Container synchronisieren möchten:

1. Erstellen Sie eine Warteschlange für diesen Ordner, wie in [Schritt 2](#azure-step-2).
2. Erstellen Sie ein Ereignisabo, das die **Blob Created**-Ereignisse des Containers an diese Warteschlange sendet, wie in [Schritt 3](#azure-step-3).
3. Wenn Sie die Synchronisierung in Braze erstellen, geben Sie den **Storage queue name** dieses Ordners ein und setzen Sie **Folder path (Optional)** auf das Ordnerpräfix, z. B. `attributes/`. CDI nimmt nur Dateien auf, deren Pfad mit diesem Präfix beginnt.

{% endtab %}
{% endtabs %}

## Erforderliche Dateiformate {#required-file-formats}

Die erforderlichen Dateiformate sind für Amazon S3, Google Cloud Storage und Azure Blob Storage identisch. Cloud Data Ingestion unterstützt JSON-, CSV- und Parquet-Dateien. Die erforderlichen Spalten hängen vom Datentyp ab:

- Nutzerdaten (Attribute, angepasste Events, Kauf-Events) verwenden Nutzer-Bezeichner und ein Payload
- Katalogdaten verwenden Katalog-Bezeichner

Wenn Sie Dateispeicher für Katalogdaten verwenden, nutzen Sie diese Seite zusammen mit [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) für katalogspezifische Anforderungen und Verhaltensweisen.

Braze stellt keine zusätzlichen Anforderungen an Dateinamen über die Vorgaben Ihres Dateispeicheranbieters hinaus. Dateinamen sollten eindeutig sein. Das Anfügen eines Zeitstempels hilft, die Eindeutigkeit sicherzustellen.

Beispiele für alle unterstützten Dateitypen (Attribute, angepasste Events, Käufe, Kataloge und Nutzer-Löschungen) finden Sie in den Beispieldateien unter [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Nutzer-Bezeichner {#user-identifiers}

Bei Nutzerdaten-Synchronisierungen (Attribute, angepasste Events, Kauf-Events) benötigt jede Zeile in Ihrer Quelldatei genau einen Nutzer-Bezeichner und eine `PAYLOAD`-Spalte. Eine Quelldatei kann Zeilen mit verschiedenen Bezeichnertypen enthalten, aber jede einzelne Zeile sollte nur einen verwenden.

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der Braze-Nutzer-Bezeichner. Dieser wird vom Braze SDK generiert. Neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail als auch Telefonnummer angeben, verwendet Braze die E-Mail als primären Bezeichner. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Updates priorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-Bezeichner" }

Zusätzlich zu einem Bezeichner muss jede Zeile eine `PAYLOAD`-Spalte enthalten, die einen JSON-String mit den Feldern enthält, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

{% alert note %}
Anders als bei Data-Warehouse-Quellen ist die `UPDATED_AT`-Spalte weder erforderlich noch unterstützt für Dateispeicher-Synchronisierungen.
{% endalert %}

### Katalog-Bezeichner {#catalog-identifiers}

Für Katalog-Synchronisierungen muss Ihre Quelldatei die folgenden Spalten enthalten. Katalogdateien verwenden andere Bezeichner als Nutzerdaten-Dateien.

| Spalte | Erforderlich | Beschreibung |
| --- | --- | --- |
| `ID` | Ja | Der eindeutige Bezeichner für den Katalogartikel. Wird zum Erstellen, Aktualisieren oder Löschen des Artikels in Braze verwendet. |
| `PAYLOAD` | Ja | Ein JSON-String mit den Katalogfeldern und -werten, die synchronisiert werden sollen. Muss mit dem Schema Ihres Katalogs in Braze übereinstimmen. |
| `DELETED` | Nein | Wenn `true`, wird der Katalogartikel mit der entsprechenden `ID` aus dem Katalog in Braze entfernt. Lassen Sie diese Spalte weg oder setzen Sie sie auf `false` für Erstellungs- oder Aktualisierungsvorgänge. |
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
Fügen Sie eine optionale `DELETED`-Spalte hinzu. Wenn `DELETED` auf `true` gesetzt ist, wird der entsprechende Katalogartikel aus dem Katalog in Braze entfernt. Die vollständige Liste der erforderlichen Spalten finden Sie unter [Katalog-Bezeichner](#catalog-identifiers). Informationen zum Löschverhalten finden Sie unter [Katalogartikel löschen](#deleting-catalog-items). Einen End-to-End-Ablauf für die Katalogeinrichtung (einschließlich Erstellung des Zielkatalogs und Synchronisierungsverhalten) finden Sie unter [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Daten löschen {#deleting-data}

Cloud-Datenaufnahme für Dateispeicher unterstützt das Löschen von Nutzer:innen und Katalogartikeln über Datei-Uploads. Verwenden Sie separate Syncs und Dateiformate für jeden Typ.

- **[Nutzer:innen löschen](#deleting-users)** – Erstellen Sie einen Sync mit dem Datentyp **Delete Users** und laden Sie Dateien hoch, die nur Nutzer-Bezeichner enthalten (ohne Payload).
- **[Katalogartikel löschen](#deleting-catalog-items)** – Verwenden Sie Ihren bestehenden Katalog-Sync und fügen Sie eine Spalte `deleted` (oder `DELETED`) hinzu, um Artikel zur Entfernung zu markieren.

### Nutzer:innen löschen {#deleting-users}

So löschen Sie Nutzerprofile in Braze mithilfe von Dateien in Ihrem Quell-Bucket:

1. Erstellen Sie einen neuen Cloud-Datenaufnahme-Sync (gleiche Einrichtung wie für andere Syncs).
2. Setzen Sie beim Konfigurieren des Syncs in Braze den **Datentyp** auf **Delete Users**.
3. Laden Sie Dateien in Ihren Quell-Bucket hoch, die nur Spalten mit Nutzer-Bezeichnern enthalten. Fügen Sie keine `PAYLOAD`-Spalte hinzu – der Sync schlägt fehl, wenn eine Payload vorhanden ist, um versehentliche Löschungen zu vermeiden.

Jede Zeile in der Datei muss genau eine:n Nutzer:in anhand einer der folgenden Optionen identifizieren:

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Entspricht der in Braze verwendeten `external_id`. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Beide Spalten zusammen identifizieren die/den Nutzer:in anhand des Alias. |
| `BRAZE_ID` | Von Braze generierte Nutzer-ID (nur bestehende Nutzer:innen). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen löschen" }

{% alert important %}
Das Löschen von Nutzer:innen ist dauerhaft und kann nicht rückgängig gemacht werden. Nehmen Sie nur Nutzer:innen auf, die Sie tatsächlich entfernen möchten. Weitere Details finden Sie unter [Nutzer:innen mit Cloud-Datenaufnahme löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
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

1. Verwenden Sie denselben Sync, den Sie zum [Synchronisieren von Katalogdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) nutzen (Datentyp **Catalogs**).
2. Fügen Sie in Ihren CSV- oder JSON-Dateien eine optionale Spalte **`deleted`** (oder **`DELETED`**) hinzu.
3. Setzen Sie `deleted` auf `true` für jeden Katalogartikel, den Sie aus dem Katalog in Braze entfernen möchten.

Jede Zeile benötigt weiterhin `ID` und `PAYLOAD`. Bei Zeilen, die zum Löschen markiert sind, kann die Payload minimal sein; Braze entfernt den Artikel anhand der `ID`.

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

Wenn der Sync ausgeführt wird, bewirken Zeilen mit `deleted: true`, dass der entsprechende Katalogartikel in Braze gelöscht wird. Das vollständige Verhalten für Katalog-Sync und -Löschung finden Sie unter [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Wissenswertes {#things-to-know}

- Dateien, die dem Quell-Bucket oder -Container hinzugefügt werden, sollten 512&nbsp;MB nicht überschreiten. Dieses Limit gilt für Amazon S3, Google Cloud Storage und Azure Blob Storage. Dateien, die größer als 512&nbsp;MB sind, führen zu einem Fehler und werden nicht mit Braze synchronisiert. Azure Blob Storage selbst erlaubt deutlich größere Dateien, aber CDI wendet dasselbe Limit von 512&nbsp;MB für alle Dateispeicherquellen an.
- Es gibt zwar kein zusätzliches Limit für die Anzahl der Zeilen pro Datei, wir empfehlen jedoch die Verwendung kleinerer Dateien, um die Geschwindigkeit Ihrer Synchronisierungen zu verbessern. Beispielsweise würde die Aufnahme einer 500&nbsp;MB großen Datei erheblich länger dauern als die von fünf separaten 100&nbsp;MB großen Dateien.
- Es gibt kein zusätzliches Limit für die Anzahl der Dateien, die in einem bestimmten Zeitraum hochgeladen werden.
- Eine Sortierung innerhalb oder zwischen Dateien wird nicht unterstützt. Wir empfehlen, Updates periodisch in Batches zusammenzufassen, wenn Sie auf erwartete Race-Conditions achten.

## Fehlerbehebung {#troubleshooting}

### Hochladen und Verarbeiten von Dateien {#uploading-files-and-processing}

CDI verarbeitet nur Dateien, die nach der Erstellung der Synchronisierung hinzugefügt werden. In diesem Prozess sucht Braze nach neu hinzugefügten Dateien, was eine neue Benachrichtigung auslöst. Dies startet eine neue Synchronisierung, um die neue Datei zu verarbeiten. Bei Amazon S3 ist die Benachrichtigung eine Nachricht an SQS. Bei Google Cloud Storage ist es eine `OBJECT_FINALIZE`-Nachricht an Pub/Sub. Bei Azure Blob Storage ist es ein **Blob Created**-Ereignis, das an eine Azure Storage-Warteschlange übermittelt wird.

Sie können vorhandene Dateien verwenden, um zu überprüfen, ob Braze auf Ihren Bucket zugreifen und Dateien zur Aufnahme erkennen kann. Diese werden jedoch nicht mit Braze synchronisiert. Damit CDI sie verarbeiten kann, müssen Sie alle vorhandenen Dateien, die Sie synchronisieren möchten, erneut in den Quell-Bucket hochladen.

### Umgang mit unerwarteten Dateifehlern (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

Wenn Sie eine hohe Anzahl von Fehlern oder fehlgeschlagenen Dateien beobachten, kann es sein, dass ein anderer Prozess Dateien in den S3-Bucket in einen anderen Ordner als den Zielordner für CDI hinzufügt.

Wenn Dateien in den Quell-Bucket hochgeladen werden, aber nicht in den Quellordner, verarbeitet CDI die SQS-Benachrichtigung, führt jedoch keine Aktion an der Datei aus. Dies kann daher als Fehler erscheinen.

Wenn Ihr Problem mit S3-Benachrichtigungen oder SQS-Zielberechtigungen zusammenhängt (z. B. Fehler bei der Zielvalidierung), lesen Sie die AWS-Dokumentation:

- [Enabling and configuring event notifications using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Granting permissions to publish event notification messages to a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Troubleshooting issues in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Umgang mit unerwarteten Dateifehlern (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Wie bei Amazon S3 verarbeitet CDI nur Dateien, die nach der Erstellung der Synchronisierung hochgeladen werden. Jedes neue Objekt löst eine `OBJECT_FINALIZE`-Nachricht an Ihr Pub/Sub-Topic aus. Um bereits im Bucket vorhandene Dateien aufzunehmen, laden Sie diese erneut hoch.

Wenn Dateien nicht aufgenommen werden, überprüfen Sie Folgendes:

- Die Bucket-Benachrichtigung existiert. Listen Sie die Benachrichtigungen für den Bucket mit `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME` auf.
- Der Cloud-Storage-Dienstagent hat `roles/pubsub.publisher` auf dem Topic.
- Das Braze-Dienstkonto hat Nutzungsberechtigung für das Abo (`pubsub.subscriptions.consume`, zugewiesen über die angepasste Rolle oder `roles/pubsub.subscriber`).
- Für das Abo ist keine Dead-Letter-Warteschlange konfiguriert. Braze unterstützt keine Dead-Letter-Warteschlangen für Cloud-Data-Ingestion-Abos.

Weitere Informationen finden Sie unter [Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) in der Google Cloud-Dokumentation.

### Umgang mit unerwarteten Dateifehlern (Azure Blob Storage) {#handling-unexpected-file-errors-azure-blob-storage}

Wie bei Amazon S3 und Google Cloud Storage verarbeitet CDI nur Dateien, die nach der Erstellung der Synchronisierung hochgeladen werden. Jedes neue Blob löst ein **Blob Created**-Ereignis in Ihrer Warteschlange aus. Um bereits im Container vorhandene Dateien aufzunehmen, laden Sie diese erneut hoch.

Wenn Dateien nicht aufgenommen werden, überprüfen Sie Folgendes:

- Das Event-Abo existiert auf dem Speicherkonto und ist auf **Blob Created** gefiltert.
- Das Event-Abo verwendet **Event Grid Schema**. CDI kann keine Ereignisse lesen, die in einem anderen Schema übermittelt werden.
- Der Endpunkt des Event-Abos zeigt auf die Warteschlange, die in der Synchronisierung konfiguriert ist, und nicht auf eine andere Warteschlange.
- Der Braze-Dienstprinzipal hat **Storage Blob Data Reader** und **Storage Queue Data Message Processor** auf dem Speicherkonto.
- Das Client-Geheimnis des Dienstprinzipals ist nicht abgelaufen. Azure erzwingt einen Ablauf für Client-Geheimnisse, und ein abgelaufenes Geheimnis stoppt die Synchronisierung.

Weitere Informationen finden Sie unter [Azure Blob Storage as an Event Grid source](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage) in der Microsoft-Dokumentation.