---
nav_title: Lytics
article_title: Lytics
description: "Dieser Referenzartikel behandelt die Integration von Braze und Lytics. Lytics ist eine unternehmensweite Customer Data Platform für Marketer, Analyst:innen und Technolog:innen. Diese Integration ermöglicht es Marken, ihre Lytics-Daten direkt mit Braze zu synchronisieren und abzubilden."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/) ist die Customer Data Platform (CDP) der Wahl für die nächste Generation kundenorientierter Unternehmen. Die Lösungen Lytics Decision Engine, Conductor und Cloud Connect bieten Marketern und Datenteams die Möglichkeit, Identitätsauflösung, Orchestrierung und Kampagnenoptimierung in Realtime und unter Wahrung des Datenschutzes durchzuführen.

_Diese Integration wird von Lytics gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Lytics bietet eine einheitliche Sicht auf Ihre Kund:innen, um leistungsstarke Personalisierung zu ermöglichen und optimierte Kampagnen mithilfe der Next-Best-Action-Orchestrierung und -Entscheidungsfindung zu fahren.

Die Integration ermöglicht es Marken:

- Zielgruppen direkt aus Lytics nach Braze zu exportieren
- Ereignisse aus Braze-Campaigns oder Canvases in Realtime an Lytics zu senden, um personalisierte Kampagnen durchzuführen und umfassende Nutzer:innen-Profile zu erstellen

## Anwendungsfälle {#use-cases}

Verbinden Sie Braze mit Lytics, um E-Mail-, SMS- und Push-Aktivitäten zu [importieren](#importing-data-from-braze-to-lytics) und Lytics-Nutzer:innen-Profile anzureichern. Wenn Sie Braze und Lytics zusammen verwenden, können Sie auch die kanalübergreifenden, verhaltensgestützten Zielgruppen von Lytics [exportieren](#integration), um anhand von First-Party-Daten hochgradig personalisierte Braze-Customer-Journeys zu erstellen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lytics-Konto | Um die Vorteile dieser Integration zu nutzen, ist ein Lytics-Konto erforderlich. |
| Lytics-Kontonummer | Für die Konfiguration der Webhook-Endpunkt-URL ist eine Lytics-Kontonummer erforderlich. |
| Lytics-API-Token | Ein Lytics-REST-API-Token mit Data-Manager:in-Berechtigungen. <br><br> Dieses kann im Lytics-Dashboard unter **Account Settings Console** > **Access Tokens** > **Create New Token** erstellt werden. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Wenden Sie sich an Ihre:n Braze-Onboarding-Manager:in:in, wenn Sie sich nicht sicher sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration {#integration}

In diesem Abschnitt wird beschrieben, wie Sie Lytics-Daten nach Braze exportieren.

### Schritt 1: Eine Autorisierung erstellen {#step-1-create-an-authorization}

Navigieren Sie in Lytics zum Dashboard **Authorization** innerhalb der **Data**-Konsole in der Navigationsleiste. Wählen Sie **Create New Authorization**, suchen Sie nach **Braze** und wählen Sie es aus.

Geben Sie in der daraufhin erscheinenden Aufforderung **Configure Authorization** eine Bezeichnung und eine Beschreibung ein und geben Sie Ihren REST-API-Schlüssel und Ihre Braze-Instanz ein. Wählen Sie **Complete**, wenn Sie fertig sind.

![Lytics-Aufforderung „Configure Authorization“ für Braze mit Feldern für Bezeichnung, Beschreibung, REST-API-Schlüssel und Braze-Instanz.]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Schritt 2: Einen neuen Auftrag erstellen {#step-2-create-a-new-job}

Navigieren Sie in Lytics zum Dashboard **Jobs** innerhalb der **Data**-Konsole in der Navigationsleiste. Wählen Sie **Create New Job**, suchen Sie nach **Braze** und wählen Sie es aus. Wählen Sie in der daraufhin angezeigten Aufforderung **Select Job Type** die Option **Export Audience**.

![Lytics-Aufforderung „Select Job Type“ für einen neuen Braze-Auftrag mit ausgewählter Option „Export Audience“.]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

Wählen Sie dann eine Autorisierung aus den Optionen unter **Select Authorization** aus.

![Lytics-Schritt „Select Authorization“ mit der Braze-Autorisierung, die für den Exportauftrag verwendet werden soll.]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Schritt 3: Den Auftrag konfigurieren {#step-3-configure-the-job}

Geben Sie in der Aufforderung **Configure Job** eine Bezeichnung und optional eine Beschreibung ein. Wählen Sie als Nächstes im Eingabefeld **Braze External User ID Field** das Feld in Lytics aus, das die externe Braze-Nutzer:innen-ID enthält (`braze_id`). Der nächste Schritt ist der wichtigste – wählen Sie im selben Dialog über die Zielgruppenauswahl die Zielgruppen aus, die Sie nach Braze exportieren möchten.

Wählen Sie schließlich die gewünschte Option für das Kontrollkästchen **Existing Users**. Wenn Sie dieses Kästchen aktiviert lassen, werden Nutzer:innen hinzugefügt, die bereits in der ausgewählten Lytics-Zielgruppe vorhanden sind. Wenn diese Option nicht markiert ist, werden Nutzer:innen nur dann nach Braze exportiert, wenn sie die Zielgruppe nach Beginn des Workflows betreten oder verlassen.

{% alert note %}
Wenn Sie dieses Kästchen markieren, werden alle vorhandenen Nutzer:innen der ausgewählten Zielgruppe an Braze gesendet. Wenn Ihre Braze-Preise Datenpunkte enthalten, überwachen Sie die Datenpunkt-Nutzung entsprechend.
{% endalert %}

Wählen Sie **Complete**, wenn Sie fertig sind, um den Export zu starten und zu speichern.

![Lytics-Exportauftrag-Zusammenfassung mit der Schaltfläche „Complete“ und Optionen zum Speichern oder Ausführen des Braze-Zielgruppen-Exports.]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Nachdem der Exportauftrag konfiguriert wurde, sendet Lytics die ausgewählten Zielgruppen über die native Integration an Braze. Nachfolgend sehen Sie eine Beispielzielgruppe, die die JSON-Struktur der an Braze gesendeten Zielgruppe zeigt.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Für jede `external_id`, die im Zielgruppen-Export enthalten ist und noch nicht in Braze existiert, wird ein:e neue:r Nutzer:in in Braze erstellt.

## Daten aus Braze in Lytics importieren {#importing-data-from-braze-to-lytics}

Sie können Zielgruppendaten aus Braze mit den folgenden Methoden in Lytics importieren:

- [Webhooks verwenden](#using-webhooks)
- [Aus einer CSV-Datei](#from-a-csv-file)

### Webhooks verwenden {#using-webhooks}

#### Schritt 1: Ein Lytics-API-Token erstellen {#step-1-create-a-lytics-api-token}

Navigieren Sie zum Lytics-Kontomenü, indem Sie Ihren Kontonamen auswählen, und wählen Sie im Dropdown-Menü **Access Tokens** aus. Wählen Sie als Nächstes **Create API Token**.

![Lytics-Bildschirm „Access Tokens“ mit ausgewählter Option „Create API Token“ im Kontomenü.]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Geben Sie einen Namen, eine optionale Beschreibung und eine Gültigkeitsdauer für den Token ein. Aktivieren Sie als Nächstes den Bereich **Data Manager:in** für API-Berechtigungen und wählen Sie **Generate Token**. Kopieren Sie den Token und bewahren Sie ihn an einem sicheren Ort auf.

![Lytics-API-Token-Berechtigungen mit aktiviertem Bereich „Data Manager“ vor der Token-Generierung.]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Schritt 2: Die Lytics-Webhook-URL konfigurieren {#step-2-configure-the-lytics-webhook-url}

Die Lytics-Webhook-URL wird von Braze verwendet, um eine Nachricht von Braze an die Lytics-API zu senden. Diese Nachricht kann zur Personalisierung Ihrer Kampagnen in Lytics oder zur Anreicherung Ihres Lytics-Kundenprofils verwendet werden. Die folgenden zwei Parameter müssen in der Lytics-Webhook-URL hinzugefügt werden:

- Lytics-Kontonummer
- Lytics-API-Token

Konfigurieren Sie Ihre Webhook-URL wie folgt:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Ersetzen Sie `<ACCOUNT-NUMBER>` durch Ihre Kontonummer und `<LYTICS-API-TOKEN>` durch Ihr Lytics-API-Token.

#### Schritt 3: Einen Webhook in Braze erstellen {#step-3-create-a-webhook-on-braze}

Erstellen Sie in Braze eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook). Fügen Sie die Lytics-Webhook-URL in das Feld **Webhook URL** ein.

Nachdem Sie den Anfragetyp (HTTP-`POST`-Methode) definiert und die restlichen Webhook-Details konfiguriert haben, ist Ihr Webhook bereit zum Testen und Bereitstellen. Hier sehen Sie einen Beispieltext für die POST-Anfrage nach der Konfiguration des Webhooks in Braze:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "Alex",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@example.com",
  "braze_id": "xxxxxx"
}
```

### Aus einer CSV-Datei {#from-a-csv-file}

Dieser Abschnitt beschreibt, wie Sie Braze-Nutzerdaten aus einem Segment in Lytics importieren.

#### Schritt 1: Eine Autorisierung erstellen

Navigieren Sie in Lytics zum Dashboard **Authorization** innerhalb der **Data**-Konsole in der Navigationsleiste. Wählen Sie **Create New Authorization**, suchen Sie nach **Custom Integrations** und wählen Sie diese aus.

Wählen Sie die bevorzugte Art der SFTP-Autorisierung auf der Grundlage Ihrer Geschäfts- und Sicherheitsanforderungen aus. Die folgenden Autorisierungstypen werden für den Import von Dateien in Lytics über SFTP unterstützt:

- Client SFTP Server Authorization
- Client SFTP Server Authorization mit PGP Private Key
- Lytics Managed SFTP Server Authorization

Public-Key-SFTP-Autorisierungen gelten nur für den SFTP-Export.

![Lytics-SFTP-Autorisierungsmethoden für den Import über Custom Integrations, einschließlich Client- und Lytics-verwalteter Serveroptionen.]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

Geben Sie in der daraufhin erscheinenden Aufforderung **Configure Authorization** eine Bezeichnung und eine Beschreibung ein und vervollständigen Sie die restlichen Konfigurationsanforderungen. Wählen Sie **Complete**, wenn Sie fertig sind.

#### Schritt 2: Ihre Segmentdaten als CSV exportieren {#step-2-export-your-segment-data-to-csv}

Navigieren Sie in Braze zu **Zielgruppe** > **Segments**. Suchen Sie das Segment, das Sie exportieren möchten, und wählen Sie dann <i class="fas fa-gear" aria-label="Einstellungen"></i> und dann **Nutzerdaten als CSV exportieren**. Sie können bis zu 500.000 Nutzer:innen in einem Segment exportieren. Weitere Informationen finden Sie unter [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

#### Schritt 3: Einen CSV-Importauftrag konfigurieren {#step-3-configure-a-csv-import-job}

Navigieren Sie in Lytics zum Dashboard **Jobs** innerhalb der **Data**-Konsole in der Navigationsleiste. Wählen Sie **Create New Job**, suchen Sie nach **Custom Integrations** und wählen Sie diese aus.

Wählen Sie dann den Auftragstyp aus. Um Braze-CSV-Dateien in Lytics zu importieren, wählen Sie als Auftragstyp **Import CSV** aus.

![Lytics-Auftragseinrichtung für Custom Integrations mit ausgewähltem Auftragstyp „Import CSV“.]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Geben Sie schließlich eine Bezeichnung und eine optionale Beschreibung für den Auftrag ein und konfigurieren Sie alle anderen erforderlichen Details. Wählen Sie **Complete**, um den Auftrag zu starten und zu speichern.