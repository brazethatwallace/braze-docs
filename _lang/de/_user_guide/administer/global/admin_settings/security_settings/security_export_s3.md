---
nav_title: Export von Sicherheitsereignissen mit S3
article_title: Sicherheitseinstellungen-Export mit S3
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Sicherheitsereignisse jeden Tag um Mitternacht UTC automatisch nach Amazon S3 exportieren können."
---

# Export von Sicherheitsereignissen mit Amazon S3 {#security-events-export-with-amazon-s3}

> Sie können Sicherheitsereignisse automatisch zu Amazon S3, einem Cloud-Speicheranbieter, exportieren, wobei ein täglicher Job um Mitternacht UTC ausgeführt wird. Nach der Einrichtung müssen Sie Sicherheitsereignisse nicht mehr manuell aus dem Dashboard exportieren. Der Job exportiert die Sicherheitsereignisse der letzten 24 Stunden im CSV-Format in Ihren konfigurierten S3-Speicher. Die CSV-Datei weist dieselben Spalten auf wie ein manuell exportierter Bericht, zuzüglich einer Spalte `Version`.

{% alert important %}
Die Verfügbarkeit des Exports von Sicherheitsereignissen mit Amazon S3 hängt von Ihrer Plattform-Edition ab. Wenn dieses Feature in Ihrem Workspace nicht verfügbar ist, wenden Sie sich an Ihren Customer-Success-Manager, um weitere Informationen zu erhalten.
{% endalert %}

Braze unterstützt zwei verschiedene S3-Authentifizierungs- und Autorisierungsmethoden für die Einrichtung des Amazon-S3-Exports:

- AWS-Methode mit geheimem Zugriffsschlüssel
- AWS-Rollen-ARN-Methode

{% alert note %}
Sicherheitsereignis-Exporte nach S3 unterliegen nicht der Begrenzung auf 10.000 Zeilen, die für den manuellen Download von CSV-Berichten über das Dashboard gilt.
{% endalert %}

## Methode mit geheimem AWS-Zugriffsschlüssel {#aws-secret-access-key-method}

Diese Methode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze ermöglicht, sich als Nutzer:in in Ihrem AWS-Konto zu authentifizieren und Daten in Ihren Bucket zu schreiben.

### Schritt 1: IAM-Nutzer:in erstellen {#step-1-create-an-identity-and-access-management-iam-user}

Um Ihren geheimen Zugriffsschlüssel und Ihre Zugriffsschlüssel-ID abzurufen, müssen Sie eine:n IAM-Nutzer:in (Identity and Access Management) erstellen. Folgen Sie dazu den Anweisungen unter [Einrichten Ihres AWS-Kontos](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Schritt 2: Zugangsdaten abrufen {#step-2-get-credentials}

1. Nachdem Sie eine:n neue:n Nutzer:in erstellt haben, generieren Sie den Zugriffsschlüssel und laden Sie Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel herunter.

![Eine Übersichtsseite für eine Rolle namens „liyu-chen-test“.]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. Notieren Sie sich diese Zugangsdaten oder laden Sie die Zugangsdaten-Dateien herunter, da Sie diese später in Braze eingeben müssen.

![Felder mit der Zugriffsschlüssel-ID und dem geheimen Zugriffsschlüssel.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Schritt 3: Richtlinie erstellen {#step-3-create-policy}

1. Gehen Sie zu **IAM** (Identity and Access Management) > **Policies** > **Create Policy**, um Berechtigungen für Ihre:n Nutzer:in hinzuzufügen.
2. Wählen Sie **Create Your Own Policy** aus, um eingeschränkte Berechtigungen festzulegen, sodass Braze nur auf die angegebenen Buckets zugreifen kann.
3. Geben Sie einen Richtliniennamen Ihrer Wahl an.
4. Fügen Sie das folgende Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie dabei „INSERTBUCKETNAME“ durch Ihren Bucket-Namen. Ohne diese Berechtigungen schlägt die Integration bei der Zugangsdatenprüfung fehl und wird nicht erstellt.

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

### Schritt 4: Richtlinie anhängen {#step-4-attach-policy}

1. Nachdem Sie eine neue Richtlinie erstellt haben, gehen Sie zu **Users** und wählen Sie Ihre:n spezifische:n Nutzer:in aus.
2. Wählen Sie im Tab **Permissions** die Option **Add Permissions** aus, fügen Sie die Richtlinie direkt an und wählen Sie dann diese Richtlinie aus.

Jetzt können Sie Ihre AWS-Zugangsdaten mit Ihrem Braze-Konto verknüpfen!

### Schritt 5: Braze mit AWS verknüpfen {#step-5-link-braze-to-aws}

1. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und scrollen Sie zum Abschnitt **Sicherheitsereignis-Download**.
2. Aktivieren Sie **In AWS S3 exportieren** unter **In Cloud-Speicher exportieren** und wählen Sie **Geheimer AWS-Zugriffsschlüssel** aus, um den S3-Export zu aktivieren.
3. Geben Sie Folgendes ein:

- AWS-Zugriffsschlüssel-ID
- AWS-Bucket-Name
- Geheimer AWS-Zugriffsschlüssel
    - Wählen Sie bei der Eingabe dieses Schlüssels zunächst **Zugangsdaten testen** aus, um zu bestätigen, dass Ihre Zugangsdaten funktionieren.

![Die Seite „Sicherheitsereignis-Download“ mit ausgefüllten Feldern für Braze-Konto und externe Braze-IDs.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. Wählen Sie **Änderungen speichern** aus.

Sie haben AWS S3 in Ihr Braze-Konto integriert!

## AWS-Rollen-ARN-Methode {#aws-role-arn-method}

Die AWS-Rollen-ARN-Methode erzeugt einen Amazon Resource Name (ARN) für eine Rolle, der es dem Braze-Amazon-Konto ermöglicht, sich als Mitglied dieser Rolle zu authentifizieren.

### Schritt 1: Richtlinie erstellen {#step-1-create-policy}

1. Melden Sie sich als Kontoadministrator:in bei der AWS-Managementkonsole an.
2. Gehen Sie in der AWS-Konsole zum Bereich **IAM** (Identity and Access Management) > **Policies** und wählen Sie dann **Create Policy** aus.

![Eine Seite mit einer Liste von Richtlinien und einem Button „Create policy“.]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. Öffnen Sie den Tab **JSON** und geben Sie das folgende Code-Snippet in den Bereich **Policy Document** ein. Ersetzen Sie dabei `INSERTBUCKETNAME` durch Ihren Bucket-Namen.

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

{: start="4"}
4. Wählen Sie **Next** aus, nachdem Sie die Richtlinie überprüft haben.

![Eine Seite, auf der Sie Ihre Richtlinie überprüfen und optional Berechtigungen hinzufügen können.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. Geben Sie der Richtlinie einen Namen und eine Beschreibung und wählen Sie dann **Create Policy** aus.

![Eine Seite zum Überprüfen und Erstellen Ihrer Richtlinie.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Schritt 2: Rolle erstellen {#step-2-create-role}

1. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und scrollen Sie zum Bereich **Sicherheitsereignis-Download**.
2. Wählen Sie **AWS Role ARN** aus.
3. Notieren Sie sich die Bezeichner, die Braze-Konto-ID und die externe Braze-ID, die zum Erstellen Ihrer Rolle benötigt werden.

![Die Seite „Sicherheitsereignis-Download“ mit ausgefüllten Feldern für die Braze-Konto-ID und die externe Braze-ID.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. Gehen Sie in der AWS-Konsole zum Bereich **IAM** (Identity and Access Management) > **Roles** > **Create Role**.
5. Wählen Sie **Another AWS Account** als Typ der vertrauenswürdigen Entität aus.
6. Geben Sie Ihre Braze-Konto-ID ein, aktivieren Sie das Kontrollkästchen **Require external ID** und geben Sie dann Ihre externe Braze-ID ein.
7. Wählen Sie **Next** aus, wenn alles abgeschlossen ist.

![Eine Seite mit Optionen zur Auswahl eines vertrauenswürdigen Entitätstyps und zur Eingabe von Informationen zu Ihrem AWS-Konto.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Schritt 3: Richtlinie anhängen {#step-3-attach-policy}

1. Suchen Sie in der Suchleiste nach der zuvor erstellten Richtlinie und setzen Sie ein Häkchen neben die Richtlinie, um sie anzuhängen.
2. Wählen Sie **Next** aus.

![Eine Liste von Richtlinien mit Spalten für ihren Typ und ihre Beschreibung.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role** aus.

![Felder zur Eingabe von Rollendetails wie Name, Beschreibung, Vertrauensrichtlinie, Berechtigungen und Tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Ihre neu erstellte Rolle wird in der Liste angezeigt!

### Schritt 4: Mit Braze AWS verknüpfen {#step-4-link-to-braze-aws}

1. Suchen Sie in der AWS-Konsole Ihre neu erstellte Rolle in der Liste. Wählen Sie den Namen aus, um die Details dieser Rolle zu öffnen, und notieren Sie sich den **ARN**.

![Die Übersichtsseite für eine Rolle namens „security-event-export-olaf“.]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und scrollen Sie zum Bereich **Sicherheitsereignis-Download**.

![Der Bereich „Sicherheitsereignis-Download“ mit einem aktivierten Umschalter für „Export to AWS S3“.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. Stellen Sie sicher, dass **AWS role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den AWS-S3-Bucket-Namen in die vorgesehenen Felder ein.
4. Wählen Sie **Test Credentials** aus, um zu bestätigen, dass Ihre Zugangsdaten korrekt funktionieren.
5. Wählen Sie **Save Changes** aus.

Sie haben AWS S3 in Ihr Braze-Konto integriert!