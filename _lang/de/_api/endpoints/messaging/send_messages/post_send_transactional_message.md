---
nav_title: "POST: Transaktions-E-Mails mit API-getriggerter Zustellung senden"
article_title: "POST: Transaktions-E-Mails mit API-getriggerter Zustellung senden"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Senden von Transaktions-E-Mails mit API-getriggerter Zustellung."
---

{% api %}
# Transaktions-E-Mails mit API-getriggerter Zustellung senden {#send-transactional-emails-using-api-triggered-delivery}
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um sofortige, einmalige transaktionsbezogene Nachrichten an eine:n bestimmte:n Nutzer:in zu senden.

Dieser Endpunkt wird zusammen mit der Erstellung einer Braze-[Transaktions-E-Mail-Campaign]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) und der entsprechenden Campaign-ID verwendet.

{% alert important %}
Transaktions-E-Mails sind derzeit als Teil ausgewählter Braze-Pakete verfügbar. Wenden Sie sich für weitere Informationen an Ihren Braze-Customer-Success-Manager.
{% endalert %}

Ähnlich wie beim [Endpunkt zum Senden getriggerter Campaigns]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) können Sie mit diesem Campaign-Typ den Nachrichteninhalt im Braze-Dashboard hinterlegen und gleichzeitig über Ihre API festlegen, wann und an wen eine Nachricht gesendet wird. Im Gegensatz zum Endpunkt „Getriggerte Campaign senden“, der eine Zielgruppe oder ein Segment akzeptiert, an das Nachrichten gesendet werden, muss eine Anfrage an diesen Endpunkt eine:n einzelne:n Nutzer:in entweder über `external_user_id` oder `user_alias` angeben, da dieser Campaign-Typ für 1:1-Nachrichten wie Bestellbestätigungen oder Passwortzurücksetzungen konzipiert ist.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `transactional.send` generieren.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Pfad-Parameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `campaign_id` | Erforderlich | String | ID der Campaign |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfad-Parameter" }

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## Anfrage-Parameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_send_id` | Optional | String | Ein Base64-kompatibler String. Wird anhand der folgenden Regex validiert:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Dieses optionale Feld ermöglicht es Ihnen, einen internen Bezeichner für diesen bestimmten Versand zu übergeben, der in Ereignissen enthalten ist, die vom Transactional-HTTP-Event-Postback gesendet werden. Bei Übergabe wird dieser Bezeichner auch als Deduplizierungsschlüssel verwendet, den Braze für 24 Stunden speichert. <br><br>Die Übergabe desselben Bezeichners in einer weiteren Anfrage führt 24 Stunden lang nicht zu einer neuen Versandinstanz durch Braze. |
| `trigger_properties` | Optional | Objekt | Siehe [Trigger-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Personalisierungs-Schlüssel-Wert-Paare, die für die:den Nutzer:in in dieser Anfrage gelten. |
| `recipient` | Erforderlich | Objekt | Die:der Nutzer:in, an die:den Sie diese Nachricht senden möchten. Kann `attributes` und ein einzelnes `external_user_id` oder `user_alias` enthalten.<br><br>Beachten Sie: Wenn Sie eine externe ID angeben, die noch nicht in Braze vorhanden ist, wird durch die Übergabe beliebiger Felder an das `attributes`-Objekt dieses Nutzerprofil in Braze erstellt und die Nachricht an die:den neu erstellte:n Nutzer:in gesendet. <br><br>Wenn Sie mehrere Anfragen an dieselbe:n Nutzer:in mit unterschiedlichen Daten im `attributes`-Objekt senden, werden die Attribute `first_name`, `last_name` und `email` synchron aktualisiert und in Ihre Nachricht eingefügt. Angepasste Attribute verfügen nicht über diesen Schutz. Gehen Sie daher vorsichtig vor, wenn Sie eine:n Nutzer:in über diese API aktualisieren und verschiedene Werte für angepasste Attribute in schneller Folge übergeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrage-Parameter" }

## Beispielanfrage {#example-request}

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Antwort {#response}

Der Endpunkt „Transaktions-E-Mails senden“ antwortet mit der `dispatch_id` der Nachricht, die die Instanz dieses Versands darstellt. Dieser Bezeichner kann zusammen mit den Ereignissen aus dem Transactional-HTTP-Event-Postback verwendet werden, um den Status einer einzelnen E-Mail zu verfolgen, die an eine:n einzelne:n Nutzer:in gesendet wurde.

### Beispielantworten {#example-responses}

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Fehlerbehebung {#troubleshooting}

Der Endpunkt kann in einigen Fällen auch einen Fehlercode und eine lesbare Nachricht zurückgeben, wobei es sich meist um Validierungsfehler handelt. Hier finden Sie einige häufige Fehler, die bei ungültigen Anfragen auftreten können.

| Fehler | Fehlerbehebung |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | Die angegebene Campaign-ID ist nicht für eine transaktionale Campaign. |
| `The external reference has been queued.  Please retry to obtain send_id.` | Die external_send_id wurde kürzlich erstellt. Versuchen Sie eine neue external_send_id, wenn Sie eine neue Nachricht senden möchten. |
| `Campaign does not exist` | Die angegebene Campaign-ID entspricht keiner bestehenden Campaign. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | Die angegebene Campaign-ID entspricht einer archivierten Campaign. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | Die angegebene Campaign-ID entspricht einer pausierten Campaign. |
| `campaign_id must be a string of the campaign api identifier` | Die angegebene Campaign-ID hat kein gültiges Format. |
| `Error authenticating credentials` | Der angegebene API-Schlüssel ist ungültig. |
| `Invalid whitelisted IPs `| Die IP-Adresse, von der die Anfrage gesendet wird, steht nicht auf der IP-Whitelist (falls diese verwendet wird). |
| `You do not have permission to access this resource` | Der verwendete API-Schlüssel hat keine Berechtigung, diese Aktion durchzuführen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

Die meisten Endpunkte bei Braze verfügen über eine Rate-Limit-Implementierung, die einen 429-Antwortcode zurückgibt, wenn zu viele Anfragen gestellt werden. Der Endpunkt für den Transaktionsversand verfügt über ein bezahltes Stundenkontingent, das in Einheiten gemessen wird (beispielsweise 50.000 Einheiten pro Stunde, abhängig von Ihrem Paket). Für diesen Endpunkt gibt es kein separates Rate-Limit pro Endpunkt: Sie können über Ihr zugewiesenes Volumen hinaus senden, jedoch wird nur das zugewiesene Volumen durch die SLA abgedeckt. Anfragen, die über dieses Kontingent hinausgehen, werden weiterhin gesendet, sind jedoch nicht durch die SLA abgedeckt. Anfragen an diesen Endpunkt werden auf Ihr [Gesamt-Rate-Limit für externe API-Anfragen]({{site.baseurl}}/api/api_limits) angerechnet. Wenn Sie dieses Limit überschreiten (beispielsweise 250.000 Anfragen pro Stunde über alle Endpunkte hinweg), gibt Braze den Statuscode 429 zurück und drosselt die Anfragen, bis das Limit zurückgesetzt wird. Das Transaktionsvolumen wird stündlich zurückgesetzt. Wenden Sie sich an den Braze-Support, wenn Sie weitere Informationen zu dieser Funktion benötigen.

## Transaktionelles HTTP-Ereignis-Postback {#transactional-http-event-postback}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}

{% endapi %}