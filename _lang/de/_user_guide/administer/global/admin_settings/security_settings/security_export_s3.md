---
nav_title: Export von Sicherheitsereignissen mit S3
article_title: Sicherheitseinstellungen-Export mit S3
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Sicherheitsereignisse jeden Tag um Mitternacht UTC automatisch nach Amazon S3 exportieren können."
---

# Export von Sicherheitsereignissen mit Amazon S3 {#security-events-export-with-amazon-s3}

> Sie können Sicherheitsereignisse automatisch zu Amazon S3, einem Cloud-Speicheranbieter, exportieren, wobei ein täglicher Job um Mitternacht UTC ausgeführt wird. Nach der Einrichtung müssen Sie Sicherheitsereignisse nicht mehr manuell aus dem Dashboard exportieren. Der Job exportiert die Sicherheitsereignisse der letzten 24 Stunden im CSV-Format in Ihren konfigurierten S3-Speicher. Die CSV-Datei weist dieselbe Struktur auf wie ein manuell exportierter Bericht.

{% alert note %}
Die Begrenzung auf 10.000 Zeilen gilt ausschließlich für den manuellen Download von CSV-Berichten über das Dashboard. Sicherheitsereignis-Exporte nach S3 unterliegen dieser Zeilenbegrenzung nicht.
{% endalert %}

Braze unterstützt zwei verschiedene S3-Authentifizierungs- und Autorisierungsmethoden für die Einrichtung des Amazon-S3-Exports:

- AWS-Methode mit geheimem Zugriffsschlüssel
- AWS-Rollen-ARN-Methode

## AWS-Methode mit geheimem Zugriffsschlüssel {#aws-secret-access-key-method}

Diese Methode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze erlaubt, sich als Nutzer:in in Ihrem AWS-Konto zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### 1. Schritt: Erstellen Sie eine:n IAM-Nutzer:in (Identity and Access Management) {#step-1-create-an-identity-and-access-management-iam-user}

Um Ihren geheimen Zugriffsschlüssel und Ihre Zugriffsschlüssel-ID abzurufen, müssen Sie eine:n IAM-Nutzer:in erstellen. Folgen Sie dazu den Anweisungen unter [Einrichten Ihres AWS-Kontos](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### 2. Schritt: Zugangsdaten abrufen {#step-2-get-credentials}

1. Nachdem Sie eine:n neue:n Nutzer:in erstellt haben, generieren Sie den Zugriffsschlüssel und laden Sie Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel herunter.

![Eine Übersichtsseite für eine Rolle namens „liyu-chen-test“.]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. Notieren Sie sich diese Zugangsdaten oder laden Sie die Zugangsdaten-Dateien herunter, da Sie diese später in Braze eingeben müssen.

![Felder mit dem Zugriffsschlüssel und dem geheimen Zugriffsschlüssel.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### 3. Schritt: Richtlinie erstellen {#step-3-create-policy}

1. Gehen Sie zu **IAM** (Identity and Access Management) > **Policies** > **Create Policy**, um Berechtigungen für Ihre:n Nutzer:in hinzuzufügen.
2. Wählen Sie **Create Your Own Policy**, um eingeschränkte Berechtigungen zu vergeben, sodass Braze nur auf die angegebenen Buckets zugreifen kann.
3. Geben Sie einen Richtliniennamen Ihrer Wahl an.
4. Fügen Sie das folgende Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie dabei „INSERTBUCKETNAME“ durch Ihren Bucket-Namen. Ohne diese Berechtigungen schlägt die Integration bei der Prüfung der Zugangsdaten fehl und wird nicht erstellt.

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

### 4. Schritt: Richtlinie anhängen {#step-4-attach-policy}

1. Nachdem Sie eine neue Richtlinie erstellt haben, gehen Sie zu **Users** und wählen Sie Ihre:n spezifische:n Nutzer:in aus.
2. Wählen Sie im Tab **Permissions** die Option **Add Permissions**, hängen Sie die Richtlinie direkt an und wählen Sie dann diese Richtlinie aus.

Jetzt können Sie Ihre AWS-Zugangsdaten mit Ihrem Braze-Konto verknüpfen!

### 5. Schritt: Braze mit AWS verknüpfen {#step-5-link-braze-to-aws}

1. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und scrollen Sie zum Abschnitt **Sicherheitsereignis-Download**.
2. Aktivieren Sie **Export zu AWS S3** unter **Export in Cloud-Speicher** und wählen Sie **AWS geheimer Zugriffsschlüssel**, um den S3-Export zu aktivieren.
3. Geben Sie Folgendes ein:

- AWS-Zugriffsschlüssel-ID
- AWS-Bucket-Name
- Geheimer AWS-Zugriffsschlüssel
    - Wählen Sie bei der Eingabe dieses Schlüssels zunächst **Zugangsdaten testen**, um zu bestätigen, dass Ihre Zugangsdaten funktionieren.

![Die Seite „Sicherheitsereignis-Download“ mit ausgefüllten Braze-Konto- und externen Braze-IDs.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. Wählen Sie **Änderungen speichern**.

Sie haben AWS S3 in Ihr Braze-Konto integriert!

## AWS-Rollen-ARN-Methode {#aws-role-arn-method}

Die AWS-Rollen-ARN-Methode generiert einen Amazon Resource Name (ARN) für eine Rolle, der es dem Braze-Amazon-Konto ermöglicht, sich als Mitglied dieser Rolle zu authentifizieren.

### 1. Schritt: Richtlinie erstellen {#step-1-create-policy}

1. Melden Sie sich als Kontoadministrator bei der AWS-Managementkonsole an.
2. Gehen Sie in der AWS-Konsole zum Abschnitt **IAM** (Identity and Access Management) > **Policies** und wählen Sie dann **Create Policy**.

![Eine Seite mit einer Liste von Richtlinien und einem Button „Create policy“.]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. Öffnen Sie den Tab **JSON** und fügen Sie das folgende Code-Snippet in den Abschnitt **Policy Document** ein. Ersetzen Sie dabei `INSERTBUCKETNAME` durch Ihren Bucket-Namen.

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
4. Wählen Sie **Next**, nachdem Sie die Richtlinie überprüft haben.

![Eine Seite, auf der Sie Ihre Richtlinie überprüfen und optional Berechtigungen hinzufügen können.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. Geben Sie der Richtlinie einen Namen und eine Beschreibung und wählen Sie dann **Create Policy**.

![Eine Seite zum Überprüfen und Erstellen Ihrer Richtlinie.]({% image_buster /assets/img/security_export/review_and_create.png %})

### 2. Schritt: Rolle erstellen {#step-2-create-role}

1. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und scrollen Sie zum Abschnitt **Sicherheitsereignis-Download**.
2. Wählen Sie **AWS Role ARN**.
3. Notieren Sie sich die Bezeichner, die Braze-Konto-ID und die externe Braze-ID, die zum Erstellen Ihrer Rolle benötigt werden.

![Die Seite „Sicherheitsereignis-Download“ mit ausgefüllten Braze-Konto- und externen Braze-IDs.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. Gehen Sie in der AWS-Konsole zum Abschnitt **IAM** (Identity and Access Management) > **Roles** > **Create Role**.
5. Wählen Sie **Another AWS Account** als Typ der vertrauenswürdigen Entität.
6. Geben Sie Ihre Braze-Konto-ID ein, aktivieren Sie das Kontrollkästchen **Require external ID** und geben Sie dann Ihre externe Braze-ID ein.
7. Wählen Sie **Next**, wenn Sie fertig sind.

![Eine Seite mit Optionen zur Auswahl eines vertrauenswürdigen Entitätstyps und zur Eingabe von Informationen zu Ihrem AWS-Konto.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### 3. Schritt: Richtlinie anhängen {#step-3-attach-policy}

1. Suchen Sie in der Suchleiste nach der zuvor erstellten Richtlinie und setzen Sie ein Häkchen neben die Richtlinie, um sie anzuhängen.
2. Wählen Sie **Next**.

![Eine Liste von Richtlinien mit Spalten für Typ und Beschreibung.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role**.

![Felder zur Eingabe von Rollendetails wie Name, Beschreibung, Vertrauensrichtlinie, Berechtigungen und Tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Ihre neu erstellte Rolle erscheint in der Liste!

### 4. Schritt: Mit Braze AWS verknüpfen {#step-4-link-to-braze-aws}

1. Suchen Sie in der AWS-Konsole Ihre neu erstellte Rolle in der Liste. Wählen Sie den Namen, um die Details dieser Rolle zu öffnen, und notieren Sie sich den **ARN**.

![Die Übersichtsseite für eine Rolle namens „security-event-export-olaf“.]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und scrollen Sie zum Abschnitt **Sicherheitsereignis-Download**.

![Abschnitt „Sicherheitsereignis-Download“ mit aktiviertem Schalter für „Export zu AWS S3“.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. Stellen Sie sicher, dass **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den AWS-S3-Bucket-Namen in die vorgesehenen Felder ein.
4. Wählen Sie **Zugangsdaten testen**, um zu bestätigen, dass Ihre Zugangsdaten ordnungsgemäß funktionieren.
5. Wählen Sie **Änderungen speichern**.

Sie haben AWS S3 in Ihr Braze-Konto integriert!