---
nav_title: "POST: Nutzerprofil nach Bezeichner exportieren"
article_title: "POST: Nutzerprofil nach Bezeichner exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt „Nutzer:innen nach Bezeichner exportieren“."
---
{% api %}
# Nutzerprofil nach Bezeichner exportieren {#export-user-profile-by-identifier}
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Daten aus einem beliebigen Nutzerprofil zu exportieren, indem Sie einen Nutzer-Bezeichner angeben.

Bis zu 50 `external_ids` oder `user_aliases` können in einer einzigen Anfrage enthalten sein. Wenn Sie `device_id`, `email_address` oder `phone` angeben möchten, kann nur einer dieser Bezeichner pro Anfrage enthalten sein.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `users.export.ids`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export
}
```

{% alert note %}
Für Kund:innen, die am oder nach dem 22. August 2024 das Onboarding mit Braze durchgeführt haben, ist der Anfrageparameter `fields_to_export` erforderlich.
{% endalert %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids` | Optional | String-Array | Externe Bezeichner für Nutzer:innen, die Sie exportieren möchten. |
| `user_aliases` | Optional | Array von Nutzer-Alias-Objekten | [Nutzer-Aliase]({{site.baseurl}}/api/objects_filters/user_alias_object) für Nutzer:innen zum Exportieren. |
| `device_id` | Optional | String | Geräte-Bezeichner, wie er von verschiedenen SDK-Methoden wie `getDeviceId` zurückgegeben wird. |
| `braze_id` | Optional | String | Braze-Bezeichner für eine:n bestimmte:n Nutzer:in. |
| `email_address` | Optional | String | E-Mail-Adresse der Nutzer:in. |
| `phone` | Optional | String im [E.164](https://en.wikipedia.org/wiki/E.164)-Format | Telefonnummer der Nutzer:in. |
| `fields_to_export` | Optional* | String-Array | Name der zu exportierenden Nutzerdatenfelder.<br><br>*Dieses Feld ist erforderlich, um das schnellere Rate-Limit von 40 Anfragen pro Sekunde zu nutzen. Wird es weggelassen, wird stattdessen das Standard-Rate-Limit von 250 Anfragen pro Minute verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

*Erforderlich für Kund:innen, die am oder nach dem 22. August 2024 das Onboarding bei Braze durchgeführt haben.

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@example.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## Zu exportierende Felder {#fields-to-export}

Im Folgenden finden Sie eine Liste der gültigen `fields_to_export`. Die Verwendung von `fields_to_export` zur Minimierung der zurückgegebenen Daten kann die Antwortzeit dieses API-Endpunkts verbessern:

| Zu exportierendes Feld | Datentyp | Beschreibung |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps` | Array | Apps, für die diese:r Nutzer:in Sitzungen protokolliert hat, einschließlich der Felder:<br><br>- `name`: App-Name<br>- `platform`: App-Plattform, z. B. iOS, Android oder Internet<br>- `version`: Versionsnummer oder -name der App<br>- `sessions`: Gesamtzahl der Sitzungen für diese App<br>- `first_used`: Datum der ersten Sitzung<br>- `last_used`: Datum der letzten Sitzung<br><br>Alle Felder sind Strings. |
| `attributed_campaign` | String | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration), falls eingerichtet. Bezeichner für eine bestimmte Werbekampagne. |
| `attributed_source` | String | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration), falls eingerichtet. Bezeichner für die Plattform, auf der die Anzeige geschaltet wurde. |
| `attributed_adgroup` | String | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb der Kampagne. |
| `attributed_ad` | String | Daten aus [Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb von Kampagne und Anzeigengruppe. |
| `push_subscribe` | String | Push-Abo-Status der Nutzer:in. |
| `email_subscribe` | String | E-Mail-Abo-Status der Nutzer:in. |
| `braze_id` | String | Gerätespezifischer eindeutiger Bezeichner, der von Braze für diese:n Nutzer:in festgelegt wurde. |
| `country` | String | Land der Nutzer:in gemäß dem [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)-Standard. |
| `created_at` | String | Datum und Uhrzeit der Erstellung des Nutzerprofils im ISO-8601-Format. |
| `custom_attributes` | Objekt | Schlüssel-Wert-Paare angepasster Attribute für diese:n Nutzer:in. |
| `custom_events` | Array | Angepasste Events, die dieser Nutzer:in in den letzten 90 Tagen zugeordnet wurden. |
| `devices` | Array | Informationen über das Gerät der Nutzer:in, die je nach Plattform Folgendes umfassen können:<br><br>- `model`: Modellname des Geräts<br>- `os`: Betriebssystem des Geräts<br>- `carrier`: Mobilfunkanbieter des Geräts, falls verfügbar<br>- `idfv`: (iOS) Braze-Geräte-Bezeichner, der Apple Identifier for Vendor, falls vorhanden<br>- `idfa`: (iOS) Identifier for Advertising, falls vorhanden<br>- `device_id`: (Android) Braze-Geräte-Bezeichner<br>- `google_ad_id`: (Android) Google Play Advertising Identifier, falls vorhanden<br>- `roku_ad_id`: (Roku) Roku Advertising Identifier<br>- `ad_tracking_enabled`: Ob Ad-Tracking auf dem Gerät aktiviert ist, kann true oder false sein |
| `dob` | String | Geburtsdatum der Nutzer:in im Format `YYYY-MM-DD`. |
| `email` | String | E-Mail-Adresse der Nutzer:in. |
| `external_id` | String | Eindeutiger Bezeichner für identifizierte Nutzer:innen. |
| `first_name` | String | Vorname der Nutzer:in. |
| `gender` | String | Geschlecht der Nutzer:in. Mögliche Werte sind:<br><br>- `M`: männlich<br>- `F`: weiblich<br>- `O`: Sonstiges<br>- `N`: nicht anwendbar<br>- `P`: lieber nicht sagen<br>- `nil`: unbekannt |
| `home_city` | String | Heimatort der Nutzer:in. |
| `language` | String | Sprache der Nutzer:in im ISO-639-1-Standard. |
| `last_coordinates` | Array von Gleitkommazahlen | Letzter Gerätestandort der Nutzer:in, formatiert als `[longitude, latitude]`. |
| `last_name` | String | Nachname der Nutzer:in. |
| `phone` | String | Telefonnummer der Nutzer:in im E.164-Format. |
| `purchases` | Array | Käufe, die diese:r Nutzer:in in den letzten 90 Tagen getätigt hat. |
| `push_tokens` | Array | Eindeutiger anonymer Bezeichner, der angibt, wohin die Benachrichtigungen einer App gesendet werden sollen. |
| `random_bucket` | Integer | [Zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) der Nutzer:in, mit der gleichmäßig verteilte Segmente aus zufälligen Nutzer:innen erstellt werden. |
| `time_zone` | String | Zeitzone der Nutzer:in im gleichen Format wie in der IANA-Zeitzonendatenbank. |
| `total_revenue` | Gleitkommazahl | Gesamtumsatz, der dieser Nutzer:in zugerechnet wird. Der Gesamtumsatz wird auf Grundlage der Käufe berechnet, die die Nutzer:innen während der Conversion-Fenster für die Campaigns und Canvases, die sie erhalten haben, getätigt haben. |
| `uninstalled_at` | Zeitstempel | Datum und Uhrzeit der Deinstallation der App durch die Nutzer:in. Entfällt, wenn die App nicht deinstalliert wurde. |
| `user_aliases` | Objekt | [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object), das `alias_name` und `alias_label` enthält, falls vorhanden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zu exportierende Felder" }

Beachten Sie, dass der Endpunkt `/users/export/ids` das gesamte Nutzerprofil zusammenstellt, einschließlich Daten wie alle erhaltenen Campaigns und Canvases, alle durchgeführten angepassten Events, alle getätigten Käufe und alle angepassten Attribute. Infolgedessen ist dieser Endpunkt langsamer als andere REST-API-Endpunkte.

Abhängig von den angefragten Daten reicht dieser API-Endpunkt aufgrund des Rate-Limits von 250 Anfragen pro Minute möglicherweise nicht aus, um Ihre Anforderungen zu erfüllen. Wenn Sie diesen Endpunkt regelmäßig zum Exportieren von Nutzer:innen verwenden möchten, sollten Sie stattdessen den Export von Nutzer:innen nach Segmenten in Betracht ziehen, der asynchron erfolgt und für größere Datenabrufe optimiert ist.

## Antwort {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

Ein Beispiel für die über diesen Endpunkt zugänglichen Daten finden Sie im folgenden Beispiel.

### Beispiel für die Ausgabe einer Nutzer-Exportdatei {#example-user-export-file-output}

Nutzer-Exportobjekt (wir nehmen so wenig Daten wie möglich auf – wenn ein Feld im Objekt fehlt, wird angenommen, dass es null oder leer ist):

{% tabs %}
{% tab Alle Felder %}

```json
{
    "created_at": (string),
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
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
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
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether foreground push notifications are enabled for this token. `true` means foreground push is enabled for the token, and `false` means foreground push is disabled (for example, background-only). This is device-level and doesn't indicate the user's global push subscription status,
        "provisionally_opted_in": (boolean) included for iOS and Android tokens only. Indicates whether the token is in a provisional push authorization state. `true` means the token is provisionally opted in (notifications are delivered quietly), `false` means the token isn't provisional (the user has explicitly authorized or denied push), and `null` means provisional status isn't set. Provisional authorization applies to iOS; Android tokens report `null`
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" :
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (boolean),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Beispielausgabe %}

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
    "first_name" : "Alex",
    "last_name" : "Smith",
    "email" : "example@example.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+15555550123",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in",
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
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
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true,
        "provisionally_opted_in": null
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
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged":
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted":
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}