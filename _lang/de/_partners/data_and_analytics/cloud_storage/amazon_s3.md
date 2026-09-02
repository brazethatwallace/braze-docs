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
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Amazon S3 bietet zwei Integrationsstrategien:

- Nutzen Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), um Ihre Daten dort zu speichern, bis Sie sie mit anderen Plattformen, Tools und Standorten verbinden möchten.
- Verwenden Sie Dashboard-Datenexporte (wie CSV-Exporte und Engagement-Berichte).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amazon S3-Konto | Sie benötigen ein Amazon S3-Konto, um diese Partnerschaft nutzen zu können. |
| Dedizierter S3-Bucket | Bevor Sie Amazon S3 integrieren, müssen Sie einen S3-Bucket für Ihre App erstellen.<br><br>Wenn Sie bereits einen S3-Bucket haben, empfehlen wir dennoch, einen neuen Bucket speziell für Braze zu erstellen, damit Sie die Berechtigungen einschränken können. In den folgenden Anweisungen erfahren Sie, wie Sie einen neuen Bucket erstellen. |
| Currents | Um Daten zurück nach Amazon S3 zu exportieren, muss [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) für Ihr Konto eingerichtet sein. Currents ist nicht erforderlich, wenn Sie nur die Nachrichtenarchivierung einrichten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Einen neuen S3-Bucket erstellen {#creating-a-new-s3-bucket}

Gehen Sie wie folgt vor, um einen Bucket für Ihre App zu erstellen:

1. Öffnen Sie die [Amazon S3-Konsole](https://console.aws.amazon.com/s3/) und folgen Sie den Anweisungen, um sich **anzumelden** oder **ein Konto bei AWS zu erstellen**.
2. Wählen Sie nach der Anmeldung **S3** aus der Kategorie **Storage & Content Delivery** aus.
3. Wählen Sie auf dem nächsten Bildschirm **Create Bucket** aus.
4. Erstellen Sie Ihren Bucket, wenn Sie dazu aufgefordert werden, und wählen Sie eine AWS-Region aus.

Braze ermöglicht es Ihnen nicht, eine Region im Dashboard auszuwählen oder zu konfigurieren. Die AWS-Region wird dadurch festgelegt, wo Sie den Bucket in der AWS-Konsole erstellen. Die Integration sendet Daten an den von Ihnen angegebenen Bucket-Namen, und AWS leitet Anfragen automatisch an die Region des Buckets weiter. Wenn Ihr Konnektor versucht, sich mit einer anderen Region zu verbinden als gewünscht (zum Beispiel `eu-west-1` statt `eu-central-1`), erstellen oder verwenden Sie einen S3-Bucket in Ihrer gewünschten Region in AWS. Auf der Braze-Seite muss nichts geändert werden.

{% alert note %}
Currents unterstützt keine Buckets, bei denen [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) konfiguriert ist.
{% endalert %}

## Integration {#integration}

Braze bietet zwei verschiedene Integrationsstrategien mit Amazon S3 – eine für [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) und eine für alle Dashboard-Datenexporte (wie CSV-Exporte oder Engagement-Berichte). Beide Integrationen unterstützen zwei verschiedene Authentifizierungs- bzw. Autorisierungsmethoden:

- [Methode mit geheimem AWS-Zugriffsschlüssel](#aws-secret-key-auth-method)
- [Methode mit AWS-Rollen-ARN](#aws-role-arn-auth-method)

## Authentifizierungsmethode mit geheimem AWS-Schlüssel {#aws-secret-key-auth-method}

Diese Authentifizierungsmethode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze ermöglicht, sich als Nutzer:in in Ihrem AWS-Konto zu authentifizieren und Daten in Ihren Bucket zu schreiben.

### Schritt 1: Nutzer:in erstellen {#secret-key-1}

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten, folgen Sie den Schritten im Tab **Dashboard Data Export**.
{% endalert %}

Um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel abzurufen, [erstellen Sie eine:n IAM-Nutzer:in und eine Administratorgruppe in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Schritt 2: Zugangsdaten abrufen {#secret-key-2}

Nachdem Sie eine:n neue:n Nutzer:in erstellt haben, wählen Sie **Show User Security Credentials** aus, um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel anzuzeigen. Notieren Sie sich diese Zugangsdaten anschließend oder wählen Sie den Button **Download Credentials**, da Sie diese später im Braze-Dashboard eingeben müssen.

![AWS-IAM-Seite mit Sicherheits-Zugangsdaten, auf der die Zugriffsschlüssel-ID und der geheime Zugriffsschlüssel angezeigt werden.]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Schritt 3: Richtlinie erstellen {#secret-key-3}

Navigieren Sie zu **Policies** > **Get Started** > **Create Policy**, um Berechtigungen für Ihre:n Nutzer:in hinzuzufügen. Wählen Sie anschließend **Create Your Own Policy** aus. Dadurch werden eingeschränkte Berechtigungen vergeben, sodass Braze nur auf die angegebenen Buckets zugreifen kann.

![AWS-IAM-Bildschirm zum Erstellen einer Richtlinie mit Richtlinienoptionen für die S3-Integration.]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Für Currents und Dashboard Data Export sind unterschiedliche Richtlinien erforderlich. `s3:GetObject` ist erforderlich, damit das Braze-Backend eine Fehlerbehandlung durchführen kann.
{% endalert %}

Geben Sie einen Richtliniennamen Ihrer Wahl an und fügen Sie den folgenden Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie `INSERTBUCKETNAME` unbedingt durch Ihren Bucket-Namen. Ohne diese Berechtigungen schlägt die Integration bei der Prüfung der Zugangsdaten fehl und wird nicht erstellt.

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten, verwenden Sie den Code-Snippet im Tab **Dashboard Data Export**.
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

Nachdem Sie eine neue Richtlinie erstellt haben, gehen Sie zu **Users** und wählen Sie Ihre:n spezifische:n Nutzer:in aus. Wählen Sie im Tab **Permissions** die Option **Attach Policy** aus und wählen Sie die neue Richtlinie, die Sie erstellt haben. Jetzt können Sie Ihre AWS-Zugangsdaten mit Ihrem Braze-Konto verknüpfen.

![AWS-IAM-Tab für Nutzerberechtigungen mit der ausgewählten Aktion „Attach Policy“.]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Schritt 5: Braze mit AWS verknüpfen {#secret-key-5}

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten, folgen Sie den Schritten im Tab **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Currents**.

Wählen Sie dann **Create New Current** und anschließend **Amazon S3 Data Export** aus.

Benennen Sie Ihren Current. Stellen Sie im Abschnitt **Credentials** sicher, dass **AWS Secret Access Key** ausgewählt ist, und geben Sie Ihre S3-Zugriffs-ID, Ihren geheimen AWS-Zugriffsschlüssel und Ihren AWS-S3-Bucket-Namen in die entsprechenden Felder ein.

{% multi_lang_include currents/contact_email_notifications.md %}

![Braze-Formular zum Erstellen eines neuen Currents für Amazon S3 mit Feldern für AWS-Zugangsdaten mit geheimem Schlüssel.]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Halten Sie Ihre AWS-Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel stets aktuell. Wenn die Zugangsdaten Ihres Konnektors ablaufen, sendet der Konnektor keine Ereignisse mehr. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

Sie können außerdem je nach Bedarf die folgenden Anpassungen vornehmen:

- **Ordnerpfad:** Standardmäßig `currents`. Wenn dieser Ordner nicht existiert, erstellt Braze automatisch einen für Sie.
- **Serverseitige AES-256-Verschlüsselung im Ruhezustand:** Standardmäßig AUS; enthält den Header `x-amz-server-side-encryption`.

Wählen Sie **Launch Current** aus, um fortzufahren.

Eine Benachrichtigung informiert Sie, ob Ihre Zugangsdaten erfolgreich überprüft wurden. AWS S3 ist jetzt für Braze-Currents eingerichtet.

{% endtab %}
{% tab Dashboard Data Export %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Amazon S3** aus.

Stellen Sie auf der Seite **AWS Credentials** sicher, dass **AWS Secret Access Key** ausgewählt ist, und geben Sie Ihre AWS-Zugriffs-ID, Ihren geheimen AWS-Zugriffsschlüssel und Ihren AWS-S3-Bucket-Namen in die entsprechenden Felder ein. Wenn Sie Ihren geheimen Schlüssel eingeben, wählen Sie zuerst **Test Credentials** aus, um sicherzustellen, dass Ihre Zugangsdaten funktionieren, und wählen Sie dann bei Erfolg **Save** aus.

![Braze-Seite für Amazon-S3-Technologie-Partner-Zugangsdaten mit Test- und Speicher-Aktionen.]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Sie können jederzeit neue Zugangsdaten abrufen, indem Sie zu Ihrem/Ihrer Nutzer:in navigieren und im Tab **Security Credentials** in der AWS-Konsole **Create Access Key** auswählen.
{% endalert %}

Eine Benachrichtigung informiert Sie, ob Ihre Zugangsdaten erfolgreich überprüft wurden. AWS S3 ist jetzt in Ihr Braze-Konto integriert.

{% endtab %}
{% endtabs %}

## AWS-Rollen-ARN-Authentifizierungsmethode {#aws-role-arn-auth-method}

Diese Authentifizierungsmethode generiert einen Rollen-Amazon-Ressourcennamen (ARN), der es dem Braze-Amazon-Konto ermöglicht, sich als Mitglied der von Ihnen erstellten Rolle zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Richtlinie erstellen {#role-arn-1}

Melden Sie sich zunächst als Kontoadministrator bei der AWS-Managementkonsole an. Navigieren Sie zum IAM-Bereich der AWS-Konsole, wählen Sie **Policies** in der Navigationsleiste und anschließend **Create Policy** aus.

![AWS-IAM-Seite „Policies“ mit ausgewähltem Button „Create Policy“.]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Für Currents und den Dashboard-Datenexport sind unterschiedliche Richtlinien erforderlich. `s3:GetObject` wird benötigt, damit das Braze-Backend die Fehlerbehandlung durchführen kann.
{% endalert %}

Öffnen Sie den Tab **JSON** und geben Sie das folgende Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie dabei `INSERTBUCKETNAME` durch Ihren Bucket-Namen. Wählen Sie **Review Policy**, wenn Sie fertig sind.

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten, verwenden Sie das Code-Snippet im Tab **Dashboard-Datenexport**.
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
{% tab Dashboard-Datenexport %}

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

Geben Sie der Richtlinie anschließend einen Namen und eine Beschreibung und wählen Sie **Create Policy**.

![AWS-IAM-Schritt zur Überprüfung der Richtlinie mit Feldern für den Namen und die Beschreibung der Richtlinie.]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![AWS-IAM-Richtlinienliste mit der neu erstellten S3-Richtlinie.]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Schritt 2: Rolle erstellen {#role-arn-2}

Wählen Sie im selben IAM-Bereich der Konsole **Roles** > **Create Role**.

![AWS-IAM-Seite „Roles“ mit ausgewähltem Button „Create Role“.]({{site.baseurl}}/assets/img/create_role_1_list.png)

Rufen Sie Ihre Braze-Konto-ID und externe ID aus Ihrem Braze-Konto ab:

- **Currents:** Gehen Sie in Braze zu **Partnerintegrationen** > **Currents**. Wählen Sie dann **Create New Current** und anschließend **Amazon S3 Data Export**. Hier finden Sie die Bezeichner, die Sie zum Erstellen Ihrer Rolle benötigen.
- **Dashboard-Datenexport:** Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Amazon S3**. Hier finden Sie die Bezeichner, die Sie zum Erstellen Ihrer Rolle benötigen. (Erstellen Sie Ihre Rollen hier, wenn Sie nur die Nachrichtenarchivierung einrichten.)

Wählen Sie zurück in der AWS-Konsole **Another AWS Account** als Typ der vertrauenswürdigen Entität aus. Geben Sie Ihre Braze-Konto-ID ein, aktivieren Sie das Kontrollkästchen **Require external ID** und geben Sie die externe Braze-ID ein. Wählen Sie **Next**, wenn Sie fertig sind.

![Die S3-Seite „Create Role“. Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und Berechtigungsgrenzen.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Schritt 3: Richtlinie anhängen {#role-arn-3}

Hängen Sie als Nächstes die zuvor erstellte Richtlinie an die Rolle an. Suchen Sie über die Suchleiste nach der Richtlinie und setzen Sie ein Häkchen neben der Richtlinie, um sie anzuhängen. Wählen Sie **Next**, wenn Sie fertig sind.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role**.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Ihre neu erstellte Rolle wird jetzt in der Liste angezeigt.

### Schritt 4: Mit Braze AWS verknüpfen {#role-arn-4}

Suchen Sie in der AWS-Konsole Ihre neu erstellte Rolle in der Liste. Wählen Sie den Namen aus, um die Details dieser Rolle zu öffnen.

![AWS-IAM-Rollendetailseite für die neu erstellte Rolle.]({{site.baseurl}}/assets/img/create_role_5_created.png)

Notieren Sie sich den **Role ARN** oben auf der Zusammenfassungsseite der Rolle.

![AWS-IAM-Rollenzusammenfassung mit dem Wert des Rollen-ARN.]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Kehren Sie zu Ihrem Braze-Konto zurück und kopieren Sie den Rollen-ARN in das dafür vorgesehene Feld.

{% alert note %}
Wenn Sie nur die Nachrichtenarchivierung einrichten, folgen Sie den Schritten im Tab **Dashboard-Datenexport**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Currents**. Wählen Sie dann **Create New Current** und anschließend **Amazon S3 Data Export**.

![Braze-Currents-Einrichtungsbildschirm für Amazon S3 mit Feldern für AWS-Rollen-ARN und Bucket.]({{site.baseurl}}/assets/img/currents-role-arn.png)

Geben Sie Ihrem Current einen Namen. Stellen Sie dann im Abschnitt **Zugangsdaten** sicher, dass **AWS Role ARN** ausgewählt ist, und geben Sie Ihren Rollen-ARN und den AWS-S3-Bucket-Namen in die dafür vorgesehenen Felder ein.

{% multi_lang_include currents/contact_email_notifications.md %}

Sie können außerdem je nach Bedarf die folgenden Anpassungen hinzufügen:

- Ordnerpfad (Standard: `currents`)
- Serverseitige AES-256-Verschlüsselung im Ruhezustand (standardmäßig AUS) – umfasst den Header `x-amz-server-side-encryption`

Wählen Sie **Launch Current**, um fortzufahren. Eine Benachrichtigung zeigt an, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 ist jetzt für Braze-Currents eingerichtet.

{% alert important %}
Wenn Sie den Fehler „S3 credentials are invalid“ erhalten, kann dies daran liegen, dass die Integration zu schnell nach dem Erstellen einer Rolle in AWS erfolgt ist. Warten Sie einen Moment und versuchen Sie es erneut. Wenn die Meldung den `PutObject`-Zugriff oder die serverseitige Verschlüsselung bei Dashboard-Datenexporten erwähnt, lesen Sie [Fehlerbehebung bei S3-Zugangsdaten-Fehlern](#troubleshooting).
{% endalert %}

{% endtab %}
{% tab Dashboard-Datenexport %}

Gehen Sie in Braze auf die Seite **Technologie-Partner** unter **Integrationen** und wählen Sie **Amazon S3**.

![Braze-Technologie-Partnerseite für Amazon S3 mit ausgewählten AWS-Rollen-ARN-Zugangsdaten.]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Stellen Sie auf der Seite **AWS Credentials** sicher, dass das Optionsfeld **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den AWS-S3-Bucket-Namen in die dafür vorgesehenen Felder ein. Wählen Sie zunächst **Test Credentials**, um zu bestätigen, dass Ihre Zugangsdaten ordnungsgemäß funktionieren, und wählen Sie dann bei Erfolg **Save**.

{% alert tip %}
Sie können jederzeit neue Zugangsdaten abrufen, indem Sie zu Ihrem Nutzer:innenprofil navigieren und im Tab **Security Credentials** in der AWS-Konsole **Create Access Key** auswählen.
{% endalert %}

Eine Benachrichtigung informiert Sie, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 ist jetzt in Ihr Braze-Konto integriert.

{% endtab %}
{% endtabs %}

## Aktualisierung der Amazon S3-Zugangsdaten für Currents {#updating-currents-credentials}

Sie können die Amazon S3-Zugangsdaten eines bestehenden Braze-Currents-Konnektors Update or aktualisieren or aktualisieren, ohne die Integration zu stoppen oder bereits in Ihren Bucket exportierte Daten zu verlieren.

Um Zugangsdaten zu Update or aktualisieren or aktualisieren – oder zwischen **AWS Secret Access Key** und **AWS Role ARN** zu wechseln – führen Sie zunächst die IAM- und AWS-seitigen Schritte für Ihre gewählte Methode weiter oben in diesem Artikel durch (Richtlinien, Nutzer:in oder Rolle und Bezeichner nach Bedarf).

Wenn Sie die Zugangsdaten in AWS vorbereitet haben, gehen Sie in Braze zu **Partnerintegrationen** > **Currents**, suchen Sie Ihren Amazon S3-Konnektor in der Liste, wählen Sie **Edit**, Update or aktualisieren or aktualisieren Sie die **Zugangsdaten** und wählen Sie **Update or aktualisieren Current**. Braze validiert die eingegebenen Zugangsdaten; Ihr Konnektor läuft weiter und die bereits in Ihrem Bucket vorhandenen Daten bleiben verfügbar. Weitere Informationen finden Sie unter [Currents Update or aktualisieren or aktualisieren in Currents einrichten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

## Exportverhalten {#export-behavior}

Nutzer:innen, die eine Cloud-Datenspeicherlösung und Export-APIs, Dashboard-Berichte oder CSV-Berichte integriert haben, erleben Folgendes:

- Alle API-Exporte geben keine Download-URL im Antworttext zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail der Nutzer:innen gesendet (keine Speicherberechtigungen erforderlich) und im Datenspeicher gesichert.

### Fehler `Unable to connect to S3, please validate that your credentials are correct` {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

Wenn Sie diesen Fehler beim Herunterladen eines CSV-Exports sehen, öffnen Sie die [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)-Integration auf der Seite **Technologie-Partner** und wählen Sie **Test Credentials** aus. Das Ergebnis erklärt, was bei der Validierung fehlgeschlagen ist – beispielsweise könnte dem Schlüssel die Berechtigung `GetObject` fehlen, was Braze daran hindert, Download-Links zu generieren.

Update or aktualisieren or aktualisieren Sie Ihre IAM-Richtlinie, damit die Integrations-Nutzer:in oder -Rolle `s3:GetObject` auf dem in Ihrer Braze-Integration konfigurierten S3-Bucket und Objektpfad aufrufen kann. Weitere Informationen zu Exportproblemen finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

{% alert important %}
**Anforderung an das JSON-Format:** Für JSON-Exporte verwendet Braze das JSONL-Format (durch Zeilenumbrüche getrenntes JSON), bei dem jede Zeile ein separates JSON-Objekt enthält. Dieses Format unterscheidet sich von Standard-JSON, das ein einzelnes JSON-Array oder -Objekt ist. Jede Zeile in der exportierten Datei ist ein gültiges JSON-Objekt, aber die Datei als Ganzes ist kein einzelnes gültiges JSON-Dokument. Beim Verarbeiten dieser Dateien sollten Sie jede Zeile einzeln als separates JSON-Objekt parsen, anstatt zu versuchen, die gesamte Datei als ein einzelnes JSON-Dokument zu parsen.

Currents-Exporte verwenden das Apache-Avro-Format (`.avro`-Dateien), nicht JSON. Diese Anforderung an das JSON-Format gilt für Dashboard-Datenexporte und API-Exporte.
{% endalert %}

## Mehrere Konnektoren {#multiple-connectors}

Wenn Sie mehr als einen Currents-Konnektor erstellen möchten, um Daten an Ihren S3-Bucket zu senden, können Sie dieselben Zugangsdaten verwenden, müssen jedoch für jeden Konnektor einen anderen Ordnerpfad angeben. Sie können diese im selben Workspace erstellen oder sie aufteilen und in mehreren Workspaces erstellen. Außerdem haben Sie die Möglichkeit, für jede Integration eine eigene Richtlinie zu erstellen oder eine einzelne Richtlinie zu erstellen, die beide Integrationen abdeckt.

Wenn Sie denselben S3-Bucket sowohl für Currents als auch für Datenexporte verwenden möchten, müssen Sie zwei separate Richtlinien erstellen, da jede Integration unterschiedliche Berechtigungen erfordert.

## Fehlerbehebung {#troubleshooting}

### Fehler: Konto hat keinen `PutObject`-Zugriff {#error-account-does-not-have-putobject-access}

Wenn beim Speichern von Amazon S3-Zugangsdaten für Dashboard-Datenexporte der folgende Fehler angezeigt wird, kann dies an falschen Berechtigungen oder serverseitigen Verschlüsselungseinstellungen liegen.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

Um dieses Problem zu beheben, überprüfen Sie die folgenden Bereiche.

#### Falsche Bucket-Richtlinie {#incorrect-bucket-policy}

Vergewissern Sie sich, dass Sie eine Richtlinie mit den korrekten Berechtigungen erstellt haben, wie in [Amazon S3-Integration](#integration) beschrieben (verwenden Sie die Richtlinie für **Dashboard Data Export** für Ihre Authentifizierungsmethode).

#### Serverseitige Verschlüsselung {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

Wenn Sie diese Fehlermeldung vom [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder in Ihren AWS-Protokollen erhalten, ist Ihr S3-Bucket mit AWS Key Management Service (SSE-KMS)-Verschlüsselung konfiguriert. Braze unterstützt SSE-KMS weder für Currents noch für Dashboard-Datenexporte. Um dies zu beheben, deaktivieren Sie SSE-KMS in Ihrem S3-Bucket.

{% alert note %}
Braze unterstützt serverseitige Verschlüsselung mit S3 Managed Keys (SSE-S3), die sowohl mit Currents als auch mit Dashboard-Datenexporten kompatibel ist.
{% endalert %}

#### Zusätzliche Berechtigungen überprüfen {#check-additional-permissions}

Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen verfügen, einschließlich `s3:GetBucketLocation` und `s3:PutObject`.