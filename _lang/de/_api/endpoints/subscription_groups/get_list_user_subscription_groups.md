---
nav_title: "GET: Abo-Gruppen von Nutzer:innen auflisten"
article_title: "GET: Abo-Gruppen von Nutzer:innen auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Abo-Gruppen von Nutzer:innen auflisten“."

---
{% api %}
# Abo-Gruppen von Nutzer:innen auflisten {#list-users-subscription-groups}
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Abo-Gruppen mit dem Verlauf bestimmter Nutzer:innen aufzulisten und abzurufen.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail-Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS-Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.groups.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `external_id` | Erforderlich | String | Die `external_id` der Nutzer:in (muss mindestens eine und darf höchstens 50 `external_ids` enthalten). |
| `email` | Erforderlich* | String | Die E-Mail-Adresse der Nutzer:in. Kann als String-Array übergeben werden. Es muss mindestens eine E-Mail-Adresse angegeben werden (maximal 50). |
| `phone` | Erforderlich* | String im [E.164](https://en.wikipedia.org/wiki/E.164)-Format | Die Telefonnummer der Nutzer:in. Es muss mindestens eine Telefonnummer angegeben werden (maximal 50). |
| `limit` | Optional | Integer | Das Limit für die maximale Anzahl der zurückgegebenen Ergebnisse. Standard (und Maximum) für `limit` ist 100. |
| `offset` | Optional | Integer | Anzahl der Templates, die übersprungen werden sollen, bevor die restlichen Templates zurückgegeben werden, die den Suchkriterien entsprechen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

{% alert tip %}
Wenn mehrere Nutzer:innen (mehrere `external_ids`) dieselbe E-Mail-Adresse haben, werden alle Nutzer:innen als separate Nutzer:innen zurückgegeben (auch wenn sie dieselbe E-Mail-Adresse oder Abo-Gruppe haben).
{% endalert %}

## Beispielanfrage {#example-request}

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Beispielantwort {#example-response}

Nur Abo-Gruppen, für die im Verlauf einer Nutzer:in ein Update des Abo-Status erfolgt ist, werden in einer erfolgreichen Antwort berücksichtigt. Das bedeutet, dass neu erstellte Abo-Gruppen nicht aufgelistet werden.

```json
{
    "users": [
        {
            "email": "test@example.com",
            "phone": "50505050",
            "external_id": "20500",
            "subscription_groups": [
                {
                  "id": "ec2fcc919fca",
                  "name": "ActivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "7d7af9dd5556",
                  "name": "ReactivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "a5e84fd16220",
                  "name": "MarketingGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "64d8cad9176c",
                  "name": "TransactionalGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "b2134cd63942",
                  "name": "BankerMarketingGroup",
                  "channel": "sms",
                  "status": "Subscribed"
                }
            ]
        }
    ],
    "total_count": 1,
    "message": "success"
}
```

{% endapi %}