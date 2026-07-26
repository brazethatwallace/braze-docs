---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amazon S3, einem hoch skalierbaren Speichersystem, das von Amazon Web Services angeboten wird."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) ist ein hoch skalierbares Speichersystem, das von Amazon Web Services angeboten wird.

{% alert important %}
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren geschäftskunden-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Amazon S3 bietet zwei Integrationsstrategien:

- Nutzen Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), um Ihre Daten dort zu speichern, bis Sie sie mit anderen Plattformen, Tools und Standorten verbinden möchten.
- Verwenden Sie Dashboard-Datenexporte (wie CSV-Exporte und Engagement-Berichte).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amazon S3-Konto | Sie benötigen ein Amazon S3-Konto, um die Vorteile dieser Partnerschaft zu nutzen. |
| Dedizierter S3-Bucket | Vor der Integration mit Amazon S3 müssen Sie einen S3-Bucket für Ihre App erstellen.<br><br>Wenn Sie bereits einen S3-Bucket haben, empfehlen wir Ihnen dennoch, einen neuen Bucket speziell für Braze zu erstellen, damit Sie die Berechtigungen einschränken können. In der folgenden Anleitung erfahren Sie, wie Sie einen neuen Bucket erstellen. |
| Currents | Um Daten zurück in Amazon S3 zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto einrichten lassen. Currents ist nicht erforderlich, wenn Sie nur die Nachrichtenarchivierung einrichten möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erstellen eines neuen S3-Buckets {#creating-a-new-s3-bucket}

Um einen Bucket für Ihre App zu erstellen, gehen Sie wie folgt vor:

1. Öffnen Sie die [Amazon S3-Konsole](https://console.aws.amazon.com/s3/) und folgen Sie den Anweisungen, um sich unter **Sign in** anzumelden oder unter **Create an Account with AWS** ein Konto zu erstellen.
2. Nachdem Sie sich angemeldet haben, wählen Sie **S3** aus der Kategorie **Storage & Content Delivery**.
3. Wählen Sie auf dem nächsten Bildschirm **Create Bucket** aus.
4. Sie werden aufgefordert, Ihren Bucket zu erstellen und eine AWS-Region auszuwählen.

Braze erlaubt es nicht, eine Region im Dashboard auszuwählen oder zu konfigurieren. Die AWS-Region wird beim Erstellen des Buckets in der AWS-Konsole festgelegt. Die Integration sendet Daten an den von Ihnen angegebenen Bucket-Namen, und AWS leitet Anfragen automatisch an die Region des Buckets weiter. Wenn Ihr Konnektor versucht, eine Verbindung zu einer anderen Region als der gewünschten herzustellen (z. B. `eu-west-1` statt `eu-central-1`), erstellen oder verwenden Sie einen S3-Bucket in Ihrer gewünschten Region in AWS. Auf der Braze-Seite muss nichts geändert werden.

{% alert note %}
Currents unterstützt keine Buckets mit konfigurierter [Objektsperre](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
{% endalert %}

## Integration {#integration}

Braze hat zwei verschiedene Integrationsstrategien mit Amazon S3 – eine für [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) und eine für alle Dashboard-Datenexporte (wie CSV-Exporte oder Engagement-Berichte). Beide Integrationen unterstützen zwei verschiedene Authentifizierungs- oder Autorisierungsmethoden:

- [AWS-Geheimschlüssel-Methode](#aws-secret-key-auth-method)
- [AWS-Rollen-ARN-Methode](#aws-role-arn-auth-method)

## AWS-Geheimschlüssel-Authentifizierungsmethode {#aws-secret-key-auth-method}

Diese Authentifizierungsmethode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze ermöglicht, sich als Nutzer:in in Ihrem AWS-Konto zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Nutzer:in erstellen {#secret-key-1}

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten möchten, folgen Sie den Schritten im Tab **Dashboard Data Export**.
{% endalert %}

Um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel abzurufen, [erstellen Sie eine IAM-Nutzer:in und eine Administratorengruppe in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Schritt 2: Zugangsdaten abrufen {#secret-key-2}

Nachdem Sie eine neue Nutzer:in erstellt haben, wählen Sie **Show User Security Credentials**, um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel anzuzeigen. Notieren Sie sich diese Zugangsdaten, oder wählen Sie den Button **Download Credentials**, da Sie diese später in das Braze-Dashboard eingeben müssen.

![AWS-IAM-Seite mit Sicherheitszugangsdaten, die die Zugriffsschlüssel-ID und den geheimen Zugriffsschlüssel anzeigt.]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Schritt 3: Richtlinie erstellen {#secret-key-3}

Navigieren Sie zu **Policies** > **Get Started** > **Create Policy**, um Berechtigungen für Ihre Nutzer:in hinzuzufügen. Wählen Sie anschließend **Create Your Own Policy** aus. Damit erhalten Sie eingeschränkte Berechtigungen, sodass Braze nur auf die angegebenen Buckets zugreifen kann.

![AWS-IAM-Seite zum Erstellen einer Richtlinie mit Richtlinienoptionen für die S3-Integration.]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Für Currents und Dashboard-Datenexport sind unterschiedliche Richtlinien erforderlich. `s3:GetObject` ist erforderlich, damit das Braze-Backend eine Fehlerbehandlung durchführen kann.
{% endalert %}

Geben Sie einen Richtliniennamen Ihrer Wahl an und fügen Sie den folgenden Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie `INSERTBUCKETNAME` durch Ihren Bucket-Namen. Ohne diese Berechtigungen schlägt die Integration bei der Prüfung der Zugangsdaten fehl und kann nicht erstellt werden.

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten möchten, verwenden Sie den Code-Snippet im Tab **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Schritt 4: Richtlinie anhängen {#secret-key-4}

Nachdem Sie eine neue Richtlinie erstellt haben, gehen Sie zu **Users** und wählen Sie Ihre spezifische Nutzer:in aus. Wählen Sie im Tab **Permissions** die Option **Attach Policy** und wählen Sie die neue Richtlinie aus, die Sie erstellt haben. Jetzt können Sie Ihre AWS-Zugangsdaten mit Ihrem Braze-Konto verknüpfen.

![AWS-IAM-Seite mit Nutzer:innenberechtigungen und ausgewählter Aktion „Attach Policy“.]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Schritt 5: Braze mit AWS verknüpfen {#secret-key-5}

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten möchten, folgen Sie den Schritten im Tab **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Currents**.

Wählen Sie dann **Create New Current** und anschließend **Amazon S3 Data Export**.

Benennen Sie Ihren Current. Vergewissern Sie sich im Abschnitt **Credentials**, dass **AWS Secret Access Key** ausgewählt ist, und geben Sie dann Ihre S3-Zugangs-ID, den geheimen AWS-Zugriffsschlüssel und den AWS S3-Bucket-Namen in die entsprechenden Felder ein.

![Braze-Formular zum Erstellen eines neuen Current für Amazon S3 mit Feldern für AWS-Geheimschlüssel-Zugangsdaten.]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Halten Sie Ihre AWS-Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel auf dem neuesten Stand. Wenn die Zugangsdaten Ihres Konnektors ablaufen, sendet der Konnektor keine Ereignisse mehr. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

Sie können auch die folgenden Anpassungen nach Ihren Bedürfnissen vornehmen:

- **Ordnerpfad:** Standardmäßig ist `currents` eingestellt. Wenn dieser Ordner nicht vorhanden ist, erstellt Braze automatisch einen für Sie.
- **Serverseitige AES-256-Verschlüsselung im Ruhezustand:** Standardmäßig ist diese Option ausgeschaltet und enthält den Header `x-amz-server-side-encryption`.

Wählen Sie **Launch Current**, um fortzufahren.

Eine Benachrichtigung informiert Sie darüber, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 ist jetzt für Braze-Currents eingerichtet.

{% endtab %}
{% tab Dashboard Data Export %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Technology Partners** und wählen Sie **Amazon S3**.

Vergewissern Sie sich auf der Seite **AWS Credentials**, dass **AWS Secret Access Key** ausgewählt ist, und geben Sie dann Ihre AWS-Zugangs-ID, den geheimen AWS-Zugriffsschlüssel und den AWS S3-Bucket-Namen in die entsprechenden Felder ein. Wählen Sie bei der Eingabe Ihres geheimen Schlüssels zunächst **Test Credentials**, um sicherzustellen, dass Ihre Zugangsdaten funktionieren, und wählen Sie dann **Save**, wenn der Test erfolgreich war.

![Braze-Seite für Amazon S3-Technologie-Partner-Zugangsdaten mit Test- und Speicheraktionen.]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Sie können jederzeit neue Zugangsdaten abrufen, indem Sie zu Ihrer Nutzer:in navigieren und in der AWS-Konsole im Tab **Security Credentials** die Option **Create Access Key** auswählen.
{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 ist jetzt in Ihr Braze-Konto integriert.

{% endtab %}
{% endtabs %}

## AWS-Rollen-ARN-Authentifizierungsmethode {#aws-role-arn-auth-method}

Diese Authentifizierungsmethode generiert einen Rollen-Amazon-Ressourcennamen (ARN), der es dem Braze-Amazon-Konto ermöglicht, sich als Mitglied der von Ihnen erstellten Rolle zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Richtlinie erstellen {#role-arn-1}

Melden Sie sich zunächst bei der AWS-Verwaltungskonsole als Kontoadministrator an. Navigieren Sie zum IAM-Bereich der AWS-Konsole, wählen Sie in der Navigationsleiste **Policies** und wählen Sie **Create Policy**.

![AWS-IAM-Seite „Policies“ mit ausgewähltem Button „Create Policy“.]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Für Currents und Dashboard-Datenexport sind unterschiedliche Richtlinien erforderlich. `s3:GetObject` ist erforderlich, damit das Braze-Backend eine Fehlerbehandlung durchführen kann.
{% endalert %}

Öffnen Sie den Tab **JSON** und geben Sie den folgenden Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie `INSERTBUCKETNAME` durch Ihren Bucket-Namen. Wählen Sie **Review Policy**, wenn Sie fertig sind.

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten möchten, verwenden Sie den Code-Snippet im Tab **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Geben Sie der Richtlinie dann einen Namen und eine Beschreibung und wählen Sie **Create Policy**.

![AWS-IAM-Schritt zur Überprüfung der Richtlinie mit Feldern für Richtlinienname und Beschreibung.]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![AWS-IAM-Richtlinienliste mit der neu erstellten S3-Richtlinie.]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Schritt 2: Rolle erstellen {#role-arn-2}

Wählen Sie im selben IAM-Bereich der Konsole **Roles** > **Create Role**.

![AWS-IAM-Seite „Roles“ mit ausgewähltem Button „Create Role“.]({{site.baseurl}}/assets/img/create_role_1_list.png)

Rufen Sie Ihre Braze-Konto-ID und Ihre externe ID von Ihrem Braze-Konto ab:

- **Currents:** Gehen Sie in Braze zu **Partnerintegrationen** > **Currents**. Wählen Sie dann **Create New Current** und anschließend **Amazon S3 Data Export**. Hier finden Sie die Bezeichner, die Sie zur Erstellung Ihrer Rolle benötigen.
- **Dashboard-Datenexport:** Gehen Sie in Braze zu **Partnerintegrationen** > **Technology Partners** und wählen Sie **Amazon S3**. Hier finden Sie die Bezeichner, die Sie zur Erstellung Ihrer Rolle benötigen. (Erstellen Sie hier Ihre Rollen, wenn Sie nur die Nachrichtenarchivierung einrichten möchten.)

Wählen Sie in der AWS-Konsole **Another AWS Account** als Typ für die vertrauenswürdige Entität aus. Geben Sie Ihre Braze-Konto-ID ein, aktivieren Sie das Kontrollkästchen **Require external ID** und geben Sie die externe Braze-ID ein. Wählen Sie **Next**, wenn Sie fertig sind.

![Die S3-Seite „Create Role“. Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Schritt 3: Richtlinie anhängen {#role-arn-3}

Hängen Sie als Nächstes die zuvor erstellte Richtlinie an die Rolle an. Suchen Sie in der Suchleiste nach der Richtlinie und setzen Sie ein Häkchen daneben, um sie anzuhängen. Wählen Sie **Next**, wenn Sie fertig sind.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role**.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Sie sehen nun Ihre neu erstellte Rolle in der Liste.

### Schritt 4: Verknüpfung mit Braze AWS {#role-arn-4}

Suchen Sie in der AWS-Konsole Ihre neu erstellte Rolle in der Liste. Wählen Sie den Namen aus, um die Details dieser Rolle zu öffnen.

![AWS-IAM-Seite mit Rollendetails für die neu erstellte Rolle.]({{site.baseurl}}/assets/img/create_role_5_created.png)

Notieren Sie sich den **Role ARN** oben auf der Rollenübersichtsseite.

![AWS-IAM-Rollenübersicht mit dem Wert des Rollen-ARN.]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Kehren Sie zu Ihrem Braze-Konto zurück und kopieren Sie den Rollen-ARN in das dafür vorgesehene Feld.

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten möchten, folgen Sie den Schritten im Tab **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Currents**. Wählen Sie dann **Create New Current** und wählen Sie **Amazon S3 Data Export**.

![Braze-Currents-Einrichtungsseite für Amazon S3 mit Feldern für AWS-Rollen-ARN und Bucket.]({{site.baseurl}}/assets/img/currents-role-arn.png)

Geben Sie Ihrem Current einen Namen. Vergewissern Sie sich dann im Abschnitt **Credentials**, dass **AWS Role ARN** ausgewählt ist, und geben Sie Ihren Rollen-ARN und den AWS S3-Bucket-Namen in die dafür vorgesehenen Felder ein.

Sie können auch die folgenden Anpassungen nach Ihren Bedürfnissen vornehmen:

- Ordnerpfad (Standard: `currents`)
- Serverseitige AES-256-Verschlüsselung im Ruhezustand (Standard: AUS) – Enthält den Header `x-amz-server-side-encryption`

Wählen Sie **Launch Current**, um fortzufahren. Eine Benachrichtigung zeigt an, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 ist jetzt für Braze-Currents eingerichtet.

{% alert important %}
Wenn Sie die Fehlermeldung „S3-Zugangsdaten sind ungültig“ erhalten, kann dies daran liegen, dass Sie die Integration nach der Erstellung einer Rolle in AWS zu schnell durchgeführt haben. Warten Sie und versuchen Sie es erneut. Wenn die Meldung den `PutObject`-Zugriff oder die serverseitige Verschlüsselung bei Dashboard-Datenexporten erwähnt, lesen Sie den Abschnitt [Fehlerbehebung bei S3-Zugangsdaten-Fehlern](#troubleshooting).
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Gehen Sie in Braze zur Seite **Technology Partners** unter **Integrations** und wählen Sie **Amazon S3**.

![Braze-Seite für Amazon S3-Technologie-Partner mit ausgewählten AWS-Rollen-ARN-Zugangsdaten.]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Vergewissern Sie sich auf der Seite **AWS Credentials**, dass der Radiobutton **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den AWS S3-Bucket-Namen in die entsprechenden Felder ein. Wählen Sie zunächst **Test Credentials**, um zu überprüfen, ob Ihre Zugangsdaten ordnungsgemäß funktionieren, und wählen Sie dann **Save**, wenn der Test erfolgreich war.

{% alert tip %}
Sie können jederzeit neue Zugangsdaten abrufen, indem Sie zu Ihrer Nutzer:in navigieren und in der AWS-Konsole im Tab **Security Credentials** die Option **Create Access Key** auswählen.
{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 ist jetzt in Ihr Braze-Konto integriert.

{% endtab %}
{% endtabs %}

## Aktualisierung der Amazon S3-Zugangsdaten für Currents {#updating-currents-credentials}

Sie können die Amazon S3-Zugangsdaten eines bestehenden Braze-Currents-Konnektors aktualisieren, ohne die Integration zu stoppen oder bereits in Ihren Bucket exportierte Daten zu verlieren.

Um Zugangsdaten zu aktualisieren – oder zwischen **AWS Secret Access Key** und **AWS Role ARN** zu wechseln – führen Sie zunächst die IAM- und AWS-seitigen Schritte für Ihre gewählte Methode weiter oben in diesem Artikel durch (Richtlinien, Nutzer:in oder Rolle und Bezeichner nach Bedarf).

Wenn Sie die Zugangsdaten in AWS vorbereitet haben, gehen Sie in Braze zu **Partnerintegrationen** > **Currents**, suchen Sie Ihren Amazon S3-Konnektor in der Liste, wählen Sie **Edit**, aktualisieren Sie die **Credentials** und wählen Sie **Update Current**. Braze validiert die eingegebenen Zugangsdaten; Ihr Konnektor läuft weiter und die bereits in Ihrem Bucket vorhandenen Daten bleiben verfügbar. Weitere Informationen finden Sie unter [Currents aktualisieren in Currents einrichten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

## Exportverhalten {#export-behavior}

Nutzer:innen, die eine Cloud-Datenspeicherlösung integriert haben und APIs, Dashboard-Berichte oder CSV-Berichte exportieren, erleben Folgendes:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Herunterladen an die E-Mail der Nutzer:in gesendet (keine Speicherberechtigungen erforderlich) und im Datenspeicher gesichert.

### Fehler: `Unable to connect to S3, please validate that your credentials are correct` {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

Wenn dieser Fehler beim Herunterladen eines CSV-Exports angezeigt wird, öffnen Sie die [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)-Integration auf der Seite **Technology Partners** und wählen Sie **Test Credentials**. Das Ergebnis erklärt, was bei der Validierung fehlgeschlagen ist – beispielsweise könnte dem Schlüssel die Berechtigung `GetObject` fehlen, was Braze daran hindert, Download-Links zu generieren.

Aktualisieren Sie Ihre IAM-Richtlinie, damit die Integrations-Nutzer:in oder -Rolle `s3:GetObject` auf dem in Ihrer Braze-Integration konfigurierten S3-Bucket und Objektpfad aufrufen kann. Weitere Informationen zu Exportproblemen finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

{% alert important %}
**JSON-Format-Anforderung:** Für JSON-Exporte verwendet Braze das JSONL-Format (Newline-delimited JSON), bei dem jede Zeile ein eigenes JSON-Objekt enthält. Dieses Format unterscheidet sich vom Standard-JSON, das ein einzelnes JSON-Array oder -Objekt ist. Jede Zeile in der exportierten Datei ist ein gültiges JSON-Objekt, aber die Datei als Ganzes ist kein einzelnes gültiges JSON-Dokument. Wenn Sie diese Dateien verarbeiten, parsen Sie jede Zeile einzeln als separates JSON-Objekt, anstatt zu versuchen, die gesamte Datei als ein einziges JSON-Dokument zu parsen.

Currents-Exporte verwenden das Apache-Avro-Format (`.avro`-Dateien), nicht JSON. Diese JSON-Format-Anforderung gilt für Dashboard-Datenexporte und API-Exporte.
{% endalert %}

## Mehrere Konnektoren {#multiple-connectors}

Wenn Sie mehr als einen Currents-Konnektor erstellen möchten, der an Ihren S3-Bucket sendet, können Sie dieselben Zugangsdaten verwenden, müssen aber für jeden einen anderen Ordnerpfad angeben. Sie können diese im selben Workspace erstellen oder sie aufteilen und in mehreren Workspaces erstellen. Sie haben auch die Möglichkeit, eine einzelne Richtlinie für jede Integration zu erstellen oder eine Richtlinie zu erstellen, die beide Integrationen abdeckt.

Wenn Sie denselben S3-Bucket sowohl für Currents als auch für Datenexporte verwenden möchten, müssen Sie zwei separate Richtlinien erstellen, da jede Integration unterschiedliche Berechtigungen erfordert.

## Fehlerbehebung {#troubleshooting}

### Fehler: Konto hat keinen `PutObject`-Zugriff {#error-account-does-not-have-putobject-access}

Wenn beim Speichern von Amazon S3-Zugangsdaten für Dashboard-Datenexporte der folgende Fehler angezeigt wird, kann dies an falschen Berechtigungen oder Einstellungen für die serverseitige Verschlüsselung liegen.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

Um dieses Problem zu beheben, überprüfen Sie die folgenden Bereiche.

#### Falsche Bucket-Richtlinie {#incorrect-bucket-policy}

Vergewissern Sie sich, dass Sie eine Richtlinie mit den korrekten Berechtigungen erstellt haben, wie im Abschnitt [Amazon S3-Integration](#integration) beschrieben (verwenden Sie die Richtlinie **Dashboard Data Export** für Ihre Authentifizierungsmethode).

#### Serverseitige Verschlüsselung {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

Wenn Sie diese Fehlermeldung vom [Braze-Support]({{site.baseurl}}/braze_support) oder in Ihren AWS-Logs erhalten, ist Ihr S3-Bucket mit AWS Key Management Service (SSE-KMS)-Verschlüsselung konfiguriert. Braze unterstützt SSE-KMS weder für Currents noch für Dashboard-Datenexporte. Um dieses Problem zu beheben, deaktivieren Sie SSE-KMS in Ihrem S3-Bucket.

{% alert note %}
Braze unterstützt serverseitige Verschlüsselung mit S3-verwalteten Schlüsseln (SSE-S3), die sowohl mit Currents als auch mit Dashboard-Datenexporten kompatibel ist.
{% endalert %}

#### Zusätzliche Berechtigungen prüfen {#check-additional-permissions}

Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen verfügen, einschließlich `s3:GetBucketLocation` und `s3:PutObject`.