---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Fivetran, einem Tool zur Workflow-Automatisierung, das Sie bei der datengestützten Entscheidungsfindung unterstützen kann, indem es abfragefertige Daten in Ihr Cloud Warehouse liefert."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) ist eine weltweit anerkannte Marke, deren auf Analysten ausgerichtete Produkte und vollständig verwaltete Pipelines datengestützte Entscheidungen ermöglichen, indem sie abfragefertige Daten in Ihr Cloud Warehouse liefern.

Die Integration von Braze und Fivetran ermöglicht es Nutzer:innen, eine wartungsfreie Pipeline zu erstellen, mit der Sie Braze-Daten sammeln und analysieren können, indem Sie alle Ihre Anwendungen und Datenbanken mit einem zentralen Warehouse verbinden. Nachdem die Daten im zentralen Warehouse gesammelt wurden, können Datenteams Braze-Daten mithilfe ihrer bevorzugten Business-Intelligence-Tools effektiv untersuchen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Fivetran-Konto | Ein [Fivetran-Konto](https://fivetran.com/login?next=%2Fdashboard) ist erforderlich, um diese Partnerschaft zu nutzen. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit den folgenden Berechtigungen:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- Canvas.list<br>- Canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Representational State Transfer-Endpunkt  | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#api-definitions) ab. |
| Braze-Currents | [Braze-Currents](https://www.braze.com/product/data-agility-management/currents/) sollte entweder mit Amazon S3 oder Google Cloud Storage verbunden sein. |
| Amazon S3 oder Google Cloud Storage | Diese Integration setzt voraus, dass Sie Zugang zu einem Amazon S3 oder Google Cloud Storage haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die folgende Currents-Integration wird sowohl für [Amazon S3](#setting-up-braze-currents-for-s3) als auch für [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage) unterstützt.

### Einrichten von Braze-Currents für S3 {#setting-up-braze-currents-for-s3}

#### 1. Schritt: Externe ID ermitteln {#step-one}

Wählen Sie im [Fivetran-Dashboard](https://fivetran.com/dashboard) **+ Connector** und dann den **Braze**-Konnektor aus, um das Einrichtungsformular zu starten. Wählen Sie anschließend **Amazon S3** aus. Notieren Sie sich die hier angezeigte externe ID – Sie benötigen sie, um Fivetran den Zugriff auf Ihren S3-Bucket zu ermöglichen.

![Das Fivetran-Einrichtungsformular für den Braze-Konnektor. Das für diesen Schritt benötigte Feld für die externe ID befindet sich in der Mitte der Seite in einem hellgrauen Kasten.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### 2. Schritt: Fivetran Zugriff auf einen bestimmten S3-Bucket gewähren {#step-2-give-fivetran-access-to-a-specified-s3-bucket}

##### IAM-Richtlinie erstellen {#creating-an-iam-policy}

Öffnen Sie die [Amazon IAM-Konsole](https://console.aws.amazon.com/iam/home#home) und navigieren Sie zu **Policies > Create Policy**.

![Amazon IAM-Konsole mit der Liste der Richtlinien.]({% image_buster /assets/img/fivetran_as3_iam.png %})

Öffnen Sie als Nächstes den Tab **JSON** und fügen Sie die folgende Richtlinie ein. Ersetzen Sie dabei `{your-bucket-name}` durch den Namen Ihres S3-Buckets.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Wählen Sie abschließend **Review Policy** aus und geben Sie der Richtlinie einen eindeutigen Namen und eine Beschreibung. Wählen Sie **Create Policy**, um Ihre Richtlinie zu erstellen.

![Felder zum Benennen der Richtlinie und Angeben einer Beschreibung.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### IAM-Rolle erstellen {#step-two}

Navigieren Sie in AWS zu **Roles** und wählen Sie dann **Create New Role**.

![Die Seite „Roles“ mit dem Button zum Erstellen einer neuen Rolle.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Wählen Sie **Another AWS Account** und geben Sie die Fivetran-Konto-ID `834469178297` ein. Aktivieren Sie das Kontrollkästchen **Require external ID**. Geben Sie hier die externe ID ein, die Sie in Schritt 1 ermittelt haben.

![Das Feld zur Eingabe Ihrer „Account ID“, ein Kontrollkästchen zum Anfordern der externen ID und ein leeres Textfeld zur Eingabe Ihrer „External ID“.]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Wählen Sie dann **Next: Permissions**, um die soeben erstellte Richtlinie auszuwählen.

![Liste der Richtlinien.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Wählen Sie **Next: Review**, benennen Sie Ihre neue Rolle (z. B. Fivetran) und wählen Sie **Create Role**. Nachdem die Rolle erstellt wurde, wählen Sie sie aus und notieren Sie sich den angezeigten Role ARN.

![Der in der Rolle aufgeführte Amazon S3 ARN.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Sie können Berechtigungen für den Role ARN festlegen, den Sie für Fivetran bestimmen. Wenn Sie dieser Rolle selektive Berechtigungen erteilen, kann Fivetran nur das synchronisieren, wofür es berechtigt ist.
{% endalert %}

#### 3. Schritt: Fivetran-Konnektor vervollständigen {#step-3-complete-the-fivetran-connector}

Wählen Sie in Fivetran **+ Connector** und dann den **Braze**-Konnektor aus, um das Einrichtungsformular zu starten. Füllen Sie im Formular die angegebenen Felder mit den entsprechenden Werten aus:
- `Destination schema`: Ein eindeutiger Schemaname.
- `API URL`: Ihr Braze Representational State Transfer-API-Endpunkt.
- `API Key`: Ihr Braze Representational State Transfer-API-Schlüssel.
- `External ID`: Die externe ID, die in [Schritt 2](#step-two) der Currents-Einrichtungsanleitung festgelegt wurde. Diese ID ist ein fester Wert.
- `Bucket`: Zu finden in Ihrem Braze-Konto unter **Partnerintegrationen** > **Datenexport** > Name Ihres aktuellen Currents.
- `Role ARN`: Den Role ARN finden Sie in [Schritt 1](#step-one) der Currents-Einrichtungsanleitung.

{% alert important %}
Stellen Sie sicher, dass **Amazon S3** als **Cloud Storage**-Option ausgewählt ist.
{% endalert %}

Wählen Sie abschließend **Save & Test** aus, und Fivetran erledigt den Representational State Transfer, indem es die Daten aus Ihrem Braze-Konto synchronisiert!

### Einrichten von Braze-Currents für Google Cloud Storage {#setting-up-braze-currents-for-google-cloud-storage}

#### 1. Schritt: Fivetran-E-Mail-Adresse aus Google Cloud Storage abrufen {#step-one2}

Wählen Sie im [Fivetran-Dashboard](https://fivetran.com/dashboard) **+ Connector** und dann den **Braze**-Konnektor aus, um das Einrichtungsformular zu starten. Wählen Sie anschließend **Google Cloud Storage** aus. Notieren Sie sich die angezeigte E-Mail-Adresse.

![Das Fivetran-Einrichtungsformular für den Braze-Konnektor. Das für diesen Schritt erforderliche E-Mail-Feld befindet sich in der Mitte der Seite in einem hellgrauen Kasten.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### 2. Schritt: Bucket-Zugriff gewähren {#step-2-grant-bucket-access}

Navigieren Sie zu Ihrer [Google Storage Console](https://console.cloud.google.com/storage/browser), wählen Sie den Bucket aus, für den Sie Braze-Currents konfiguriert haben, und wählen Sie **Edit bucket permissions**.

![Die in der Google Storage Console verfügbaren Buckets. Suchen Sie einen Bucket und wählen Sie das vertikale Drei-Punkte-Symbol aus, um das Dropdown-Menü zu öffnen, mit dem Sie die Bucket-Berechtigungen bearbeiten können.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Gewähren Sie als Nächstes `Storage Object Viewer`-Zugriff auf die E-Mail aus [Schritt 1](#step-one2), indem Sie die E-Mail als Mitglied hinzufügen. Notieren Sie sich den Bucket-Namen – Sie benötigen ihn im nächsten Schritt, um Fivetran zu konfigurieren.

![Bucket mit Berechtigungen.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### 3. Schritt: Fivetran-Konnektor vervollständigen

Wählen Sie in Fivetran **+ Connector** und dann den **Braze**-Konnektor aus, um das Einrichtungsformular zu starten. Füllen Sie im Formular die angegebenen Felder mit den entsprechenden Werten aus:
- `Destination schema`: Ein eindeutiger Schemaname.
- `API URL`: Ihr Braze Representational State Transfer-API-Endpunkt.
- `API Key`: Ihr Braze Representational State Transfer-API-Schlüssel.
- `Bucket Name`: Zu finden in Ihrem Braze-Konto unter **Partnerintegrationen** > **Datenexport** > Name Ihres aktuellen Currents.
- `Folder`: Zu finden in Ihrem Braze-Konto unter **Partnerintegrationen** > **Datenexport** > Name Ihres aktuellen Currents.

{% alert important %}
Stellen Sie sicher, dass **Google Cloud Storage** als **Cloud Storage**-Option ausgewählt ist.
{% endalert %}

Wählen Sie abschließend **Save & Test** aus, und Fivetran erledigt den Representational State Transfer, indem es die Daten aus Ihrem Braze-Konto synchronisiert!