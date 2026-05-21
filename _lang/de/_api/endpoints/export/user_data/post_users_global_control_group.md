---
nav_title: "POST: Nutzerprofil nach globaler Kontrollgruppe exportieren"
article_title: "POST: Nutzerprofil nach globaler Kontrollgruppe exportieren"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt „Nutzer:innen in globalen Kontrollgruppen exportieren“."

---
{% api %}
# Nutzerprofil nach globaler Kontrollgruppe exportieren {#export-user-profile-by-global-control-group}
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Nutzer:innen innerhalb einer globalen Kontrollgruppe zu exportieren.

Nutzerdaten werden als mehrere Dateien mit JSON-Objekten für Nutzer:innen exportiert, die durch Zeilenumbrüche getrennt sind (z. B. ein JSON-Objekt pro Zeile). Alle Nutzer:innen einer globalen Kontrollgruppe werden bei jeder Generierung der Dateien berücksichtigt. Braze speichert keinen Verlauf darüber, wann Nutzer:innen zu einer globalen Kontrollgruppe hinzugefügt oder aus ihr entfernt werden.

Um den Segment-Bezeichner Ihrer globalen Kontrollgruppe zu ermitteln, lesen Sie [API-Bezeichnertypen]({{site.baseurl}}/api/identifier_types/?tab=segments#segment-identifier).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `users.export.global_control_group`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Auf Zugangsdaten basierende Antwortdetails {#credentials-based-response-details}

Wenn Sie Ihre [S3-]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) oder [Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)-Zugangsdaten über die entsprechende **Technologie-Partner**-Seite zu Braze hinzugefügt haben, wird jede Datei in Ihrem Bucket als ZIP-Datei mit dem folgenden Schlüsselformat hochgeladen: `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Wenn Sie Azure verwenden, vergewissern Sie sich, dass Sie auf der Übersichtsseite für Azure-Partner in Braze das Kontrollkästchen **Make this the default data export destination** aktiviert haben.

Im Allgemeinen erstellen wir eine Datei pro 5.000 Nutzer:innen, um die Verarbeitung zu optimieren. Das Exportieren kleinerer Segmente innerhalb eines großen Workspace kann zu mehreren Dateien führen. Sie können dann die Dateien extrahieren und bei Bedarf alle `json`-Dateien zu einer einzigen Datei zusammenfügen. Wenn Sie ein `output_format` von `gzip` angeben, wird die Dateiendung `.gz` anstelle von `.zip` verwendet.

{% details Aufschlüsselung der Exportpfade für ZIP %}
**ZIP-Format:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**Beispiel-ZIP:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Eigenschaft                     | Details                                                                              | Im Beispiel dargestellt als            |
| ------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------- |
| `bucket-name`                   | Basierend auf Ihrem Bucket-Namen festgelegt.                                         | `braze.docs.bucket`                    |
| `segment-export`                | Festgelegt.                                                                          | `segment-export`                       |
| `SEGMENT_ID`                    | In der Exportanfrage enthalten.                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | Das Datum, an dem der erfolgreiche Callback eingegangen ist.                         | `2019-04-25`                           |
| `RANDOM_UUID`                   | Eine zufällige UUID, die von Braze zum Zeitpunkt der Anfrage generiert wurde.        | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Unix-Zeit (Sekunden seit 2017-01-01:00:00:00Z), zu der der Export in UTC angefragt wurde. | `1556044807`                           |
| `filename`                      | Zufällig pro Datei.                                                                  | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Auf Zugangsdaten basierende Antwortdetails" }

{% enddetails %}

Wir empfehlen Ihnen dringend, Ihre eigenen S3- oder Azure-Zugangsdaten einzurichten (unter **Partnerintegrationen** > **Technologie-Partner** > Partnerseite), wenn Sie diesen Endpunkt verwenden, um Ihre eigenen Bucket-Richtlinien für den Export durchzusetzen.

![Die Technologie-Partnerseite für Azure mit einem Tab für Amazon S3.]({% image_buster /assets/img/technology_partners_page.png %})

Wenn Sie Ihre Zugangsdaten für den Cloud-Speicher nicht angeben, enthält die Antwort auf die Anfrage die URL, unter der eine ZIP-Datei mit allen Nutzerdateien heruntergeladen werden kann. Die URL wird erst nach Abschluss des Exports zu einem gültigen Speicherort.

Beachten Sie, dass die Menge der Daten, die Sie von diesem Endpunkt exportieren können, begrenzt ist, wenn Sie Ihre Zugangsdaten für den Cloud-Speicher nicht angeben. Je nach den Feldern, die Sie exportieren, und der Anzahl der Nutzer:innen kann die Dateiübertragung fehlschlagen, wenn sie zu groß ist. Am besten legen Sie fest, welche Felder Sie exportieren möchten, indem Sie `fields_to_export` verwenden und nur die Felder angeben, die Sie benötigen, um die Größe der Übertragung gering zu halten. Wenn Sie bei der Generierung der Datei Fehler erhalten, sollten Sie Ihre Nutzerbasis auf der Grundlage einer zufälligen Bucket-Nummer in mehrere Segmente aufteilen (z. B. ein Segment erstellen, bei dem die zufällige Bucket-Nummer kleiner als 1.000 oder zwischen 1.000 und 2.000 ist).

In beiden Szenarien können Sie optional einen `callback_endpoint` angeben, um benachrichtigt zu werden, wenn der Export fertig ist. Wenn der `callback_endpoint` angegeben ist, senden wir eine POST-Anfrage an die angegebene Adresse, sobald der Download bereitsteht. Der Text der Anfrage lautet `"success":true`. Falls Sie Ihre Cloud-Speicher-Zugangsdaten noch nicht zu Braze hinzugefügt haben, enthält der Text der Anfrage zusätzlich das Attribut `url` mit der Download-URL als Wert.

Größere Nutzermengen haben längere Exportzeiten zur Folge. Eine App mit 20 Millionen Nutzer:innen könnte zum Beispiel eine Stunde oder länger dauern.

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, for example, ['first_name', 'email', 'purchases'],
  "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
Individuelle angepasste Attribute können nicht exportiert werden. Allerdings können alle angepassten Attribute exportiert werden, indem custom_attributes in das fields_to_export-Array aufgenommen wird (zum Beispiel `['first_name', 'email', 'custom_attributes']`).
{% endalert %}

## Anfrageparameter {#request-parameters}

| Parameter           | Erforderlich | Datentyp         | Beschreibung                                                                                                                                                              |
| ------------------- | ------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_endpoint` | Optional     | String           | Endpunkt, an den eine Download-URL gesendet wird, wenn der Export verfügbar ist.                                                                                          |
| `fields_to_export`  | Erforderlich* | String-Array    | Name der zu exportierenden Nutzerdatenfelder. Sie können auch angepasste Attribute exportieren. <br><br>*Ab April 2021 müssen neue Konten bestimmte Felder für den Export angeben. |
| `output_format`     | Optional     | String           | Wenn Sie Ihren eigenen S3-Bucket verwenden, können Sie das Dateiformat als `zip` oder `gzip` angeben. Standardmäßig ist das ZIP-Dateiformat eingestellt.                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "callback_endpoint" : "",
  "fields_to_export" : ["email", "braze_id"],
  "output_format" : "zip"
}'
```

## Zu exportierende Felder {#fields-to-export}

Im Folgenden finden Sie eine Liste der gültigen `fields_to_export`. Die Verwendung von `fields_to_export` zur Minimierung der zurückgegebenen Daten kann die Antwortzeit dieses API-Endpunkts verbessern:

| Zu exportierendes Feld | Datentyp        | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                 | Array           | Apps, für die diese:r Nutzer:in Sitzungen protokolliert hat, einschließlich der Felder:<br><br>- `name`: App-Name<br>- `platform`: App-Plattform, z. B. iOS, Android oder Internet<br>- `version`: Versionsnummer oder -name der App <br>- `sessions`: Gesamtzahl der Sitzungen für diese App<br>- `first_used`: Datum der ersten Sitzung<br>- `last_used`: Datum der letzten Sitzung<br><br>Alle Felder sind Strings.                                                                                                                                                                                                                                           |
| `attributed_campaign`  | String          | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für eine bestimmte Werbekampagne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `attributed_source`    | String          | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für die Plattform, auf der die Anzeige geschaltet wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `attributed_adgroup`   | String          | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb der Kampagne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `attributed_ad`        | String          | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb von Kampagne und Anzeigengruppe.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `braze_id`             | String          | Gerätespezifischer eindeutiger Bezeichner, der von Braze für diese:n Nutzer:in festgelegt wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `country`              | String          | Das Land der/des Nutzer:in gemäß dem [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)-Standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`           | String          | Datum und Uhrzeit der Erstellung des Nutzerprofils im ISO-8601-Format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `custom_attributes`    | Objekt          | Angepasste Attribut-Schlüssel-Wert-Paare für diese:n Nutzer:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`        | Array           | Angepasste Events, die dieser/diesem Nutzer:in in den letzten 90 Tagen zugeordnet wurden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `devices`              | Array           | Informationen über das Gerät der/des Nutzer:in, die je nach Plattform Folgendes umfassen können:<br><br>- `model`: Modellname des Geräts<br>- `os`: Betriebssystem des Geräts<br>- `carrier`: Mobilfunkanbieter des Geräts, falls verfügbar<br>- `idfv`: (iOS) Braze-Gerätebezeichner, der Apple Identifier for Vendors, falls vorhanden<br>- `idfa`: (iOS) Identifier for Advertising, falls vorhanden<br>- `device_id`: (Android) Braze-Gerätebezeichner<br>- `google_ad_id`: (Android) Google Play Advertising Identifier, falls vorhanden<br>- `roku_ad_id`: (Roku) Roku Advertising Identifier<br>- `ad_tracking_enabled`: Ob Ad-Tracking auf dem Gerät aktiviert ist, kann true oder false sein |
| `dob`                  | String          | Das Geburtsdatum der/des Nutzer:in im Format `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `email`                | String          | E-Mail-Adresse der/des Nutzer:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `external_id`          | String          | Eindeutiger Bezeichner für identifizierte Nutzer:innen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `first_name`           | String          | Der Vorname der/des Nutzer:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `gender`               | String          | Geschlecht der/des Nutzer:in. Mögliche Werte sind:<br><br>- `M`: männlich<br>- `F`: weiblich<br>- `O`: sonstiges<br>- `N`: nicht anwendbar<br>- `P`: keine Angabe<br>- `nil`: unbekannt                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `home_city`            | String          | Der Heimatort der/des Nutzer:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `language`             | String          | Sprache der/des Nutzer:in gemäß dem ISO-639-1-Standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`     | Array von Gleitkommazahlen | Der letzte Gerätestandort der/des Nutzer:in, formatiert als `[longitude, latitude]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `last_name`            | String          | Der Nachname der/des Nutzer:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `phone`                | String          | Die Telefonnummer der/des Nutzer:in im E.164-Format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `purchase`s            | Array           | Käufe, die diese:r Nutzer:in in den letzten 90 Tagen getätigt hat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `random_bucket`        | Integer         | [Zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/#random-bucket-number-event) der/des Nutzer:in, mit der gleichmäßig verteilte Segmente aus zufälligen Nutzer:innen erstellt werden.                                                                                                                                                                                                                                                                                                                                                                                                |
| `time_zone`            | String          | Die Zeitzone der/des Nutzer:in im gleichen Format wie in der IANA-Zeitzonendatenbank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `total_revenue`        | Gleitkommazahl  | Gesamtumsatz, der dieser/diesem Nutzer:in zugerechnet wird. Der Gesamtumsatz wird auf der Grundlage der Käufe berechnet, die die Nutzer:innen während der Conversion-Fenster für die Campaigns und Canvases, die sie erhalten haben, getätigt haben.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `uninstalled_at`       | Zeitstempel     | Datum und Uhrzeit der Deinstallation der App durch die/den Nutzer:in. Entfällt, wenn die App nicht deinstalliert wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `user_aliases`         | Objekt          | [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/#user-alias-object-specification), das `alias_name` und `alias_label` enthält, falls vorhanden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zu exportierende Felder" }

## Antwort {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that is used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Nachdem die URL bereitgestellt wurde, ist sie nur für einige Stunden gültig. Wir empfehlen Ihnen daher dringend, Ihre eigenen S3-Zugangsdaten zu Braze hinzuzufügen.

### Beispiel für die Ausgabe einer Nutzerexportdatei {#example-user-export-file-output}

Nutzerexportobjekt (wir geben so wenig Daten wie möglich an – wenn ein Feld im Objekt fehlt, sollte davon ausgegangen werden, dass es null oder leer ist):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at" : (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
         "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (string),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "custom_attributes":
      {
        "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
        "loyaltyPoints": "321",
        "loyaltyPointsNumber": 107
      },
    "custom_events": [
      {
          "name": "Loyalty Acknowledgement",
          "first": "2021-06-28T17:02:43.032Z",
          "last": "2021-06-28T17:02:43.032Z",
          "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% endapi %}