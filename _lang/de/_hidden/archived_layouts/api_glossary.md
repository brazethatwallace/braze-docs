---
title: API- oder Code-Glossar
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Dies ist die Beschreibung für die Google-Suche. Zeichen nach 160 werden abgeschnitten, fassen Sie sich kurz."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 E-Mail-Template erstellen {#1-create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Post,Email,Create,Template,REST,API
{% endapitags %}

Verwenden Sie die E-Mail-Template-REST-APIs, um die E-Mail-Templates, die Sie in den Braze-Dashboards auf der Seite Templates und Medien gespeichert haben, programmatisch zu verwalten. Braze bietet zwei Endpunkte zum Erstellen und Aktualisieren Ihrer E-Mail-Templates.

Die Antwort von diesem Endpunkt enthält ein Feld für `email_template_id`, das zum Aktualisieren des Templates in nachfolgenden API-Aufrufen verwendet werden kann.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGEKÖRPER {#request-body}
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### BEISPIELANTWORT {#example-response}
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### PARAMETER-DETAILS

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `modified_after`  | Nein | String in ISO 8601 | Ruft nur Templates ab, die zum oder nach dem angegebenen Zeitpunkt aktualisiert wurden. |
| `modified_before`  |  Nein | String in ISO 8601 | Ruft nur Templates ab, die zum oder vor dem angegebenen Zeitpunkt aktualisiert wurden. |
| `limit` | Nein | Positive Zahl | Maximale Anzahl der abzurufenden Templates. Standard ist 100, wenn nicht angegeben; der maximal zulässige Wert ist 1000. |
| `offset`  |  Nein | Positive Zahl | Anzahl der Templates, die übersprungen werden sollen, bevor der Rest der Templates zurückgegeben wird, die den Suchkriterien entsprechen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parameter-Details" }


{% endapi %}
{% api %}
## 2 Verfügbare E-Mail-Templates auflisten {#2-list-available-email-template}
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Get,Email,Template,List,REST
{% endapitags %}

Verwenden Sie die folgenden Endpunkte, um eine Liste der verfügbaren Templates abzurufen.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGEKÖRPER
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### BEISPIELANTWORT
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### PARAMETER-DETAILS

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `email_template_id`  | Ja | String | Der API-Bezeichner Ihres E-Mail-Templates. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parameter-Details" }

{% endapi %}


{% api %}
## 3 Campaigns per Trigger senden {#3-campaigns-trigger-send}
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Post, Campaigns, Trigger,Send{% endapitags %}

Die API-getriggerte Zustellung ermöglicht es Ihnen, Nachrichteninhalte im Braze-Dashboard zu hinterlegen und gleichzeitig über Ihre API festzulegen, wann und an wen eine Nachricht gesendet wird.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGEKÖRPER
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### BEISPIELANTWORT
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "context": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "context": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent context)
    },
    ...
  ]
}
```


#### PARAMETER-DETAILS

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `email_template_id`  | Ja | String | Der API-Bezeichner Ihres E-Mail-Templates. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parameter-Details" }

{% endapi %}


{% api %}
## 4 Campaigns per Trigger senden {#4-campaigns-trigger-send}
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campaigns, Trigger, Send{% endapitags %}

Dieser Endpunkt kann verwendet werden, um angepasste Events, Nutzerattribute und Käufe für Nutzer:innen aufzuzeichnen. Sie können bis zu 75 Attribute-, Event- und Kauf-Objekte pro Anfrage einschließen. Das heißt, Sie können nur Attribute für bis zu 75 Nutzer:innen gleichzeitig senden, aber im selben API-Aufruf können Sie auch bis zu 75 Events und bis zu 75 Käufe bereitstellen.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGEKÖRPER
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### BEISPIELANTWORT
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Alex",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### PARAMETER-DETAILS

| Kundenprofil-Feld | Datentyp-Spezifikation |
| ---| --- |
| country | (String) Wir verlangen, dass Ländercodes im [ISO-3166-1-alpha-2-Standard][17] an Braze übergeben werden. |
| current_location | (Objekt) In der Form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (Datum, an dem die Nutzer:in die App zum ersten Mal verwendet hat) String im ISO-8601-Format oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| date_of_last_session | (Datum, an dem die Nutzer:in die App zuletzt verwendet hat) String im ISO-8601-Format oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| dob | (Geburtsdatum) String im Format „JJJJ-MM-TT“, zum Beispiel 1980-12-21. |
| email | (String) |
| email_subscribe | (String) Verfügbare Werte sind „opted_in“ (explizit für den Empfang von E-Mail-Nachrichten registriert), „unsubscribed“ (explizit von E-Mail-Nachrichten abgemeldet) und „subscribed“ (weder Opt-in noch Opt-out). |
| external_id | (String) Der eindeutige Nutzer-Bezeichner. |
| facebook | Hash mit beliebigen der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| first_name | (String) |
| gender | (String) „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (möchte ich nicht angeben) oder nil (unbekannt). |
| home_city | (String) |
| image_url | (String) URL des Bildes, das mit dem Kundenprofil verknüpft werden soll. |
| language | (String) Wir verlangen, dass die Sprache im [ISO-639-1-Standard][24] an Braze übergeben wird. <br>[Liste der akzeptierten Sprachen](/docs/user_guide/data_and_analytics/user_data_collection/language_codes/) |
| last_name | (String) |
| marked_email_as_spam_at | (String) Datum, an dem die E-Mail der Nutzer:in als Spam markiert wurde. Erscheint im ISO-8601-Format oder im Format yyyy-MM-dd'T'HH:mm:ss:SSSZ. |
| phone | (String) |
| push_subscribe | (String) Verfügbare Werte sind „opted_in“ (explizit für den Empfang von Push-Nachrichten registriert), „unsubscribed“ (explizit von Push-Nachrichten abgemeldet) und „subscribed“ (weder Opt-in noch Opt-out). |
| push_tokens | Array von Objekten mit `app_id` und `token` String. Sie können optional eine `device_id` für das Gerät angeben, mit dem dieses Token / Textbaustein verknüpft ist, zum Beispiel `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Wenn keine `device_id` angegeben wird, wird eine zufällig generiert. |
| time_zone | (String) Name der Zeitzone aus der [IANA-Zeitzonendatenbank][26] (zum Beispiel „America/New_York“ oder „Eastern Time (US & Canada)“). Es werden nur gültige Zeitzonenwerte gesetzt. |
| twitter | Hash mit beliebigen der folgenden Werte: `id` (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parameter-Details" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/