---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Google Cloud Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) ist ein massiv skalierbarer Objektspeicher für unstrukturierte Daten, der von Google als Teil der Cloud-Computing-Produkt-Suite angeboten wird.

{% alert important %}
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren Customer-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Google Cloud Storage erlaubt es Ihnen, Currents-Daten zu Google Cloud Storage zu streamen. Sie können später einen ETL-Prozess (Extract, Transform, Load) verwenden, um Ihre Daten an andere Ziele zu übertragen, z. B. Google BigQuery.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Google Cloud Storage-Konto | Ein Google Cloud Storage-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Currents | Um Daten zurück in Google Cloud Storage zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet haben. Currents ist nicht erforderlich, wenn Sie nur die Nachrichtenarchivierung einrichten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Für die Integration mit Google Cloud Storage müssen Sie die entsprechenden Zugangsdaten einrichten, die es Braze erlauben, Informationen über die Speicher-Buckets zu erhalten, in die geschrieben wird (`storage.buckets.get`), und Objekte innerhalb dieses Buckets zu erstellen (`storage.objects.create`).

{% alert note %}
Workload Identity Federation (WIF) wird als Authentifizierungsmethode für Currents nicht unterstützt. Sie müssen ein Dienstkonto mit einem JSON Private Key verwenden.
{% endalert %}

Verwenden Sie dazu die folgenden Anweisungen, die Sie durch die Erstellung einer Rolle und eines Dienstkontos führen, die einen Private Key für Ihre Currents-Integration erzeugen.

### 1. Schritt: Rolle erstellen {#step-1-create-role}

Erstellen Sie eine neue Rolle in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Roles** > **+ Create Role** navigieren.

![Google Cloud IAM-Rollenseite mit der Aktion „Create Role“.]({% image_buster /assets/img/gcs1.png %})

Geben Sie der Rolle einen Namen, wählen Sie dann **+Add Permissions** und wählen Sie Folgendes aus:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
Die Berechtigung `storage.objects.delete` ist optional. Sie erlaubt es Braze, unvollständige Dateien zu bereinigen.<br><br>In seltenen Fällen kann es vorkommen, dass Google Cloud die Verbindung vorzeitig beendet, was dazu führt, dass Braze unvollständige Dateien in Google Cloud Storage schreibt. In den meisten Fällen wird Braze einen neuen Versuch unternehmen und eine neue Datei mit den richtigen Daten erstellen, wobei die alte Datei in Google Cloud Storage verbleibt.
{% endalert %}

{% alert important %}
Wenn Ihr Bucket einen [hierarchischen Namespace](https://cloud.google.com/storage/docs/hns-overview) verwendet, müssen Sie außerdem die Berechtigung `storage.folders.create` hinzufügen. Bei diesen Buckets sind Ordner verwaltete Ressourcen, sodass Braze diese Berechtigung benötigt, um die Ordnerstruktur für Ihre exportierten Dateien zu erstellen. Ohne diese Berechtigung kann Braze nicht in den Bucket schreiben und die Integration kann keine Daten exportieren.
{% endalert %}

Wenn Sie fertig sind, wählen Sie **Create**.

![Editor für angepasste Google Cloud-Rollen mit ausgewählten Speicherberechtigungen.]({% image_buster /assets/img/gcs2.png %})

### 2. Schritt: Ein neues Dienstkonto erstellen {#step-2-create-a-new-service-account}

#### Schritt 2.1: Dienstkonto erstellen {#step-21-create-the-service-account}

Erstellen Sie ein neues Dienstkonto in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Service Accounts** navigieren und **Create Service Account** auswählen.

![Google Cloud-Dienstkontenseite mit ausgewähltem „Create Service Account“.]({% image_buster /assets/img/gcs3.png %})

Als Nächstes geben Sie dem Dienstkonto einen Namen und gewähren ihm Zugriff auf Ihre neu erstellte angepasste Rolle.

![Auf der Google Cloud Platform geben Sie auf der Seite „Dienste erstellen“ den Namen Ihrer Rolle in das Feld „Select a Role“ ein.]({% image_buster /assets/img/gcs4.png %})

#### Schritt 2.2: Schlüssel erstellen {#step-22-create-a-key}

Verwenden Sie unten auf der Seite den Button **Create Key**, um einen **JSON** Private Key zur Verwendung in Braze zu erstellen. Nachdem der Schlüssel erstellt wurde, wird er auf Ihren Computer heruntergeladen.

![Dialog zur Erstellung eines Google Cloud-Dienstkontoschlüssels mit dem Schlüsseltyp JSON.]({% image_buster /assets/img/gcs5.png %})

### 3. Schritt: Currents in Braze einrichten {#step-3-set-up-currents-in-braze}

Navigieren Sie in Braze zu **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** und geben Sie den Namen Ihrer Integration und Ihre Kontakt-E-Mail an.

{% multi_lang_include currents/contact_email_notifications.md %}

Als Nächstes laden Sie Ihren JSON Private Key unter **GCS JSON Credentials** hoch und geben den GCS-Bucket-Namen und das GCS-Präfix (optional) an. Beachten Sie, dass Sie diese Zugangsdaten über Google Cloud Platform generieren müssen, wie in den vorherigen Schritten beschrieben.

{% alert important %}
Es ist wichtig, dass Sie Ihre Zugangsdaten immer auf dem neuesten Stand halten. Wenn die Zugangsdaten für Ihren Konnektor ablaufen, sendet der Konnektor keine Ereignisse mehr. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

![Die Google Cloud Storage Currents-Seite in Braze. Auf dieser Seite gibt es Felder für den Integrationsnamen, die Kontakt-E-Mail, die GCS-JSON-Zugangsdaten, den GCS-Bucket-Namen und das Präfix.]({% image_buster /assets/img/gcs6.png %})

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Nachrichten-Engagement-Ereignisse oder Kundenverhalten-Ereignisse Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### 4. Schritt: Google Cloud Storage-Exporte einrichten {#step-4-set-up-google-cloud-storage-exports}

Um Google Cloud Storage (GCS)-Exporte einzurichten, gehen Sie zu **Technologie-Partner** > **Google Cloud Storage**, geben Sie Ihre GCS-Zugangsdaten ein und wählen Sie **Make this the default data export destination**.

Denken Sie daran, dass die Organisation und der Inhalt der exportierten Dateien bei der Integration von AWS S3, Microsoft Azure und Google Cloud Storage identisch sind.

{% alert important %}
Achten Sie darauf, dass Sie den vollständigen JSON-Wert eingeben, der [von Google Cloud generiert](https://cloud.google.com/iam/docs/keys-create-delete) wird.
{% endalert %}

![Die Google Cloud Storage-Seite im Braze-Dashboard.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### 5. Schritt: Zugangsdaten des Dienstkontos testen (optional) {#step-5-test-your-service-account-credentials-optional}

Ihr Google Cloud IAM-Dienstkonto muss über die folgenden Berechtigungen verfügen:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Um diese Berechtigungen im Braze-Dashboard zu überprüfen, gehen Sie auf die Seite **Google Cloud Storage** und wählen Sie **Test Credentials**.

![Der Abschnitt mit den Zugangsdaten für Google Cloud Storage im Braze-Dashboard.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Exportverhalten {#export-behavior}

Nutzer:innen, die eine Cloud-Datenspeicherlösung integriert haben und APIs, Dashboard-Berichte oder CSV-Berichte exportieren möchten, erleben Folgendes:

- Alle API-Exporte geben keine Download-URL im Antworttext zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail der Nutzer:innen gesendet (keine Speicherberechtigungen erforderlich) und im Datenspeicher gesichert.

{% alert important %}
**JSON-Formatanforderung**: Für JSON-Exporte verwendet Braze das JSONL-Format (Newline-delimited JSON), bei dem jede Zeile ein separates JSON-Objekt enthält. Dieses Format unterscheidet sich von Standard-JSON, das ein einzelnes JSON-Array oder -Objekt ist. Jede Zeile in der exportierten Datei ist ein gültiges JSON-Objekt, aber die Datei als Ganzes ist kein einzelnes gültiges JSON-Dokument. Beim Verarbeiten dieser Dateien sollte jede Zeile einzeln als separates JSON-Objekt geparst werden, anstatt zu versuchen, die gesamte Datei als ein einzelnes JSON-Dokument zu parsen.

Currents-Exporte verwenden das Apache-Avro-Format (`.avro`-Dateien), nicht JSON. Diese JSON-Formatanforderung gilt für Dashboard-Datenexporte und API-Exporte, die das JSON-Format verwenden.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Google Cloud Storage-Zugangsdaten sind ungültig {#google-cloud-storage-credentials-are-invalid}

Wenn Sie beim Eingeben Ihrer Zugangsdaten die folgende Fehlermeldung erhalten:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Stellen Sie sicher, dass Ihr Google Cloud IAM-Dienstkonto die folgenden Berechtigungen hat:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Nach der Überprüfung können Sie [Ihre Zugangsdaten im Braze-Dashboard testen](#step-5-test-your-service-account-credentials-optional).