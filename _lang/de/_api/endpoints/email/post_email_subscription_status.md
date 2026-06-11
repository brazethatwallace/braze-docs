---
nav_title: "POST: Status des E-Mail-Abos ändern"
article_title: "POST: Status des E-Mail-Abos ändern"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Status des E-Mail-Abos von Nutzer:innen ändern“."

---
{% api %}
# Status des E-Mail-Abos ändern {#change-email-subscription-status}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Status des E-Mail-Abos für Ihre Nutzer:innen festzulegen.

Nutzer:innen können `opted_in`, `unsubscribed` oder `subscribed` sein (ohne spezielles Opt-in oder Opt-out).

Sie können den Status des E-Mail-Abos für eine E-Mail-Adresse festlegen, die noch keiner Ihrer Nutzer:innen in Braze zugeordnet ist. Wenn diese E-Mail-Adresse anschließend mit einer/einem Nutzer:in verknüpft wird, wird der von Ihnen hochgeladene Status des E-Mail-Abos automatisch übernommen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.status`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `email` | Erforderlich | String oder Array | Zu ändernde String-E-Mail-Adresse oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen. |
| `subscription_state` | Erforderlich | String | Entweder „subscribed“, „unsubscribed“ oder „opted_in“. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Fehlerbehebung bei SendGrid-E-Mail-Blockierungen {#troubleshooting-sendgrid-email-blocks}

Wenn SendGrid eine/n Empfänger:in blockiert, aktualisieren Sie den Abo-Status mit diesem Endpunkt und überprüfen Sie das Engagement mithilfe von Segment-Filtern. Verwenden Sie Soft-Bounce-Ereignisse von [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) zur Überwachung der Zustellbarkeit und bestätigen Sie den Abo-Status, bevor Sie den Versand erneut versuchen.

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}