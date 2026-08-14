---
nav_title: Integrationen in die Dateiablage
article_title: Integrationen in die Dateiablage
description: "Diese Seite behandelt die Braze Cloud-Datenaufnahme und wie Sie relevante Daten von S3 mit Braze synchronisieren."
page_order: 4
page_type: reference

---

# Integrationen in die Dateiablage {#file-storage-integrations}

> Auf dieser Seite erfahren Sie, wie Sie die Cloud-Datenaufnahme einrichten und relevante Daten von S3 mit Braze synchronisieren.

## So funktioniert es {#how-it-works}

Sie können Cloud Data Ingestion (CDI) für S3 verwenden, um einen oder mehrere S3-Buckets in Ihrem AWS-Konto direkt mit Braze zu integrieren. Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an SQS gesendet, und Braze Cloud Data Ingestion nimmt diese neuen Dateien auf.

Cloud Data Ingestion unterstützt Folgendes:

- JSON-Dateien
- CSV-Dateien
- Parquet-Dateien
- Attribut-, angepasste Event-, Kauf-Event-, Nutzerlöschungs- und Katalogdaten

## Voraussetzungen {#prerequisites}

Die Integration erfordert die folgenden Ressourcen:

 - S3-Bucket für die Datenspeicherung
 - SQS-Warteschlange für Benachrichtigungen über neue Dateien
 - IAM-Rolle für den Braze-Zugriff

### AWS-Definitionen {#aws-definitions}

Zunächst werden die Begriffe definiert, die bei dieser Aufgabe verwendet werden.

| Begriff | Definition |
| --- | --- |
| Amazon Resource Name (ARN) | Der ARN ist ein eindeutiger Bezeichner für AWS-Ressourcen. |
| Identity and Access Management (IAM) | IAM ist ein Webdienst, mit dem Sie den Zugriff auf AWS-Ressourcen sicher steuern können. Erstellen Sie in diesem Tutorial eine IAM-Richtlinie und weisen Sie diese einer IAM-Rolle zu, um Ihren S3-Bucket mit der Braze-Datenaufnahme aus der Cloud zu integrieren. |
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

Notieren Sie sich die Region, in der Sie den Bucket erstellt haben – Sie werden im nächsten Schritt eine SQS-Warteschlange in derselben Region erstellen.

### Schritt 2: SQS-Warteschlange erstellen {#step-2-create-sqs-queue}

Erstellen Sie eine SQS-Warteschlange, um nachzuverfolgen, wann Objekte zum erstellten Bucket hinzugefügt werden. Verwenden Sie vorerst die Standardkonfigurationseinstellungen.

Eine SQS-Warteschlange muss global eindeutig sein (es kann beispielsweise nur eine für eine CDI-Synchronisierung verwendet werden und sie kann nicht in einem anderen Workspace wiederverwendet werden).

{% alert important %}
Stellen Sie sicher, dass Sie diese SQS in derselben Region erstellen, in der Sie den Bucket erstellt haben.
{% endalert %}

Notieren Sie sich den ARN und die URL der SQS-Warteschlange – Sie werden sie während dieser Konfiguration häufig benötigen.

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

## Cloud-Datenaufnahme in Braze einrichten {#setting-up-cloud-data-ingestion-in-braze}

1. Erstellen Sie zunächst eine neue Quelle im Braze-Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Quellen**, wählen Sie **Datenquelle hinzufügen** und dann **Amazon S3** aus.
2. Wählen Sie einen Namen für Ihre Quelle und geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Quelle zu erstellen. Geben Sie Folgendes an:

  - Rollen-ARN
  - Externe ID
  - Bucket-Name
  - Region

![Der Abschnitt „S3-Verbindungsdetails“ mit Zugangsdaten (AWS-Einrichtung und Braze-Einrichtung) und Konfigurationsfeldern.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Wählen Sie **Verbindung testen**, um zu bestätigen, dass Braze auf Ihren Bucket zugreifen kann. Wählen Sie nach einem erfolgreichen Test **Mit Quelle verbinden** aus. Falls die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{: start="4"}
4. Erstellen Sie als Nächstes eine neue Synchronisierung. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Synchronisierungen** und wählen Sie **Datensynchronisierung erstellen**.

{: start="5"}
5. Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann eine aktive S3-Quelle aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und dann **Verbindung testen**.

![Eine Option zum Testen der Verbindung mit einer Datenvorschau.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Geben Sie die restlichen Informationen aus dem AWS-Einrichtungsprozess ein. Geben Sie Folgendes an:
- SQS-URL (muss für jede neue Integration eindeutig sein)
- Ordnerpfad (optional, muss workspace-weit über alle Synchronisierungen hinweg eindeutig sein)

7. Wählen Sie einen Datentyp und dann **Verbindung testen**, um zu bestätigen, dass Braze die zur Aufnahme verfügbaren Dateien auflisten kann (nicht die Daten in diesen Dateien). Wählen Sie nach Erfolg **Weiter: Benachrichtigungen**.
8. Fügen Sie Kontakt-E-Mail-Adressen für Benachrichtigungen hinzu, falls die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Optional können Sie Benachrichtigungen für Fehler auf Nutzer:innenebene und erfolgreiche Synchronisierungen aktivieren.
9. Erstellen Sie die Synchronisierung.

## Erforderliche Dateiformate {#required-file-formats}

Cloud Data Ingestion unterstützt JSON-, CSV- und Parquet-Dateien. Die erforderlichen Spalten hängen vom Datentyp ab:

- Nutzerdaten (Attribute, angepasste Events, Kauf-Events) verwenden Nutzer-Bezeichner und ein Payload
- Katalogdaten verwenden Katalog-Bezeichner

Wenn Sie S3 für Katalogdaten verwenden, nutzen Sie diese Seite zusammen mit [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) für katalogspezifische Anforderungen und Verhaltensweisen.

Braze stellt über die von AWS erzwungenen Anforderungen hinaus keine zusätzlichen Anforderungen an Dateinamen. Dateinamen sollten eindeutig sein. Das Anhängen eines Zeitstempels hilft, die Eindeutigkeit sicherzustellen.

Beispiele für alle unterstützten Dateitypen (Attribute, angepasste Events, Käufe, Kataloge und Nutzer-Löschungen) finden Sie in den Beispieldateien unter [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Nutzer-Bezeichner {#user-identifiers}

Für Nutzerdaten-Synchronisierungen (Attribute, angepasste Events, Kauf-Events) benötigt jede Zeile in Ihrer Quelldatei genau einen Nutzer-Bezeichner und eine `PAYLOAD`-Spalte. Eine Quelldatei kann Zeilen mit verschiedenen Bezeichnertypen enthalten, aber jede einzelne Zeile sollte nur einen verwenden.

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit verschiedenen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der Braze-Nutzer-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefonnummer angeben, verwendet Braze die E-Mail als primären Bezeichner. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-Bezeichner" }

Zusätzlich zu einem Bezeichner muss jede Zeile eine `PAYLOAD`-Spalte enthalten, die einen JSON-String der Felder enthält, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

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
Fügen Sie eine optionale `DELETED`-Spalte hinzu. Wenn `DELETED` den Wert `true` hat, wird dieser Katalogartikel aus dem Katalog in Braze entfernt. Die vollständige Liste der erforderlichen Spalten finden Sie unter [Katalog-Bezeichner](#catalog-identifiers). Informationen zum Löschverhalten finden Sie unter [Katalogartikel löschen](#deleting-catalog-items). Einen End-to-End-Ablauf für die Katalogeinrichtung (einschließlich Erstellung des Zielkatalogs und Synchronisierungsverhalten) finden Sie unter [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Daten löschen {#deleting-data}

Cloud-Datenaufnahme für S3 unterstützt das Löschen von Nutzer:innen und Katalogartikeln über Datei-Uploads. Verwenden Sie für jeden Vorgang separate Syncs und Dateiformate.

- **[Nutzer:innen löschen](#deleting-users)** – Erstellen Sie einen Sync mit dem Datentyp **Delete Users** und laden Sie Dateien hoch, die nur Nutzer-Bezeichner enthalten (kein Payload).
- **[Katalogartikel löschen](#deleting-catalog-items)** – Verwenden Sie Ihren bestehenden Katalog-Sync und fügen Sie eine Spalte `deleted` (oder `DELETED`) hinzu, um Artikel zur Entfernung zu markieren.

### Nutzer:innen löschen {#deleting-users}

So löschen Sie Nutzerprofile in Braze mithilfe von Dateien in S3:

1. Erstellen Sie einen neuen Cloud-Datenaufnahme-Sync (dasselbe [AWS- und Braze-Setup](#setting-up-cloud-data-ingestion-in-aws) wie für andere Syncs).
2. Setzen Sie beim Konfigurieren des Syncs in Braze den **Data Type** auf **Delete Users**.
3. Laden Sie Dateien in Ihren S3-Bucket hoch, die nur Spalten mit Nutzer-Bezeichnern enthalten. Fügen Sie keine `PAYLOAD`-Spalte hinzu – der Sync schlägt fehl, wenn ein Payload vorhanden ist, um versehentliche Löschungen zu vermeiden.

Jede Zeile in der Datei muss genau eine:n Nutzer:in über eine der folgenden Optionen identifizieren:

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

1. Verwenden Sie denselben S3-Sync, den Sie zum [Synchronisieren von Katalogdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) verwenden (Datentyp **Catalogs**).
2. Fügen Sie in Ihren CSV- oder JSON-Dateien eine optionale Spalte **`deleted`** (oder **`DELETED`**) hinzu.
3. Setzen Sie `deleted` auf `true` für jeden Katalogartikel, den Sie aus dem Katalog in Braze entfernen möchten.

Jede Zeile benötigt weiterhin `ID` und `PAYLOAD`. Für Zeilen, die zur Löschung markiert sind, kann der Payload minimal sein; Braze entfernt den Artikel anhand der `ID`.

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

- Dateien, die dem S3-Quell-Bucket hinzugefügt werden, sollten 512&nbsp;MB nicht überschreiten. Dateien, die größer als 512&nbsp;MB sind, führen zu einem Fehler und werden nicht mit Braze synchronisiert.
- Es gibt zwar keine zusätzliche Begrenzung für die Anzahl der Zeilen pro Datei, wir empfehlen jedoch die Verwendung kleinerer Dateien, um die Geschwindigkeit Ihrer Synchronisierungen zu verbessern. Beispielsweise würde die Aufnahme einer 500&nbsp;MB großen Datei erheblich länger dauern als die von fünf separaten 100&nbsp;MB großen Dateien.
- Es gibt keine zusätzliche Begrenzung für die Anzahl der Dateien, die in einem bestimmten Zeitraum hochgeladen werden.
- Eine Sortierung innerhalb von oder zwischen Dateien wird nicht unterstützt. Wir empfehlen, Aktualisierungen regelmäßig in Batches zusammenzufassen, wenn Sie auf erwartete Race-Conditions achten.

## Fehlerbehebung {#troubleshooting}

### Hochladen und Verarbeiten von Dateien {#uploading-files-and-processing}

CDI verarbeitet nur Dateien, die nach der Erstellung der Synchronisierung hinzugefügt werden. In diesem Prozess sucht Braze nach neu hinzugefügten Dateien, was eine neue Nachricht an SQS auslöst. Dadurch wird eine neue Synchronisierung gestartet, um die neue Datei zu verarbeiten.

Sie können vorhandene Dateien verwenden, um zu überprüfen, ob Braze auf Ihren Bucket zugreifen und Dateien zur Datenaufnahme erkennen kann. Diese werden jedoch nicht mit Braze synchronisiert. Damit CDI sie verarbeiten kann, müssen Sie alle vorhandenen Dateien, die synchronisiert werden sollen, erneut in S3 hochladen.

### Umgang mit unerwarteten Dateifehlern {#handling-unexpected-file-errors}

Wenn Sie eine hohe Anzahl von Fehlern oder fehlgeschlagenen Dateien beobachten, haben Sie möglicherweise einen anderen Prozess, der Dateien in einem anderen Ordner als dem Zielordner für CDI zum S3-Bucket hinzufügt.

Wenn Dateien in den Quell-Bucket, aber nicht in den Quellordner hochgeladen werden, verarbeitet CDI die SQS-Benachrichtigung, führt jedoch keine Aktion für die Datei aus. Dies kann daher als Fehler erscheinen.

Wenn Ihr Problem mit S3-Benachrichtigungen oder SQS-Zielberechtigungen zusammenhängt (zum Beispiel Fehler bei der Zielvalidierung), lesen Sie die AWS-Dokumentation:

- [Aktivieren und Konfigurieren von Ereignisbenachrichtigungen über die Amazon-S3-Konsole](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Erteilen von Berechtigungen zum Veröffentlichen von Ereignisbenachrichtigungen an ein Ziel](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Fehlerbehebung bei Problemen in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)