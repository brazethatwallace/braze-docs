---
nav_title: "POST: Geplante Nachrichten erstellen"
article_title: "POST: Geplante Nachrichten erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Geplante Nachrichten erstellen“."

---
{% api %}
# Geplante Nachrichten erstellen {#create-scheduled-messages}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Campaign, ein Canvas oder eine andere Nachricht zu planen, die zu einem bestimmten Zeitpunkt gesendet werden soll. Der Endpunkt gibt Ihnen einen Bezeichner zurück, mit dem Sie die Nachricht für Updates referenzieren können.

Wenn Sie ein Segment als Zielgruppe verwenden, wird ein Datensatz Ihrer Anfrage in der [Entwicklungskonsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert, nachdem alle geplanten Nachrichten gesendet wurden.

{% alert tip %}
Wenn Sie Nachrichten sofort an bestimmte Nutzer:innen senden möchten, verwenden Sie stattdessen den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `messages.schedule.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `broadcast` | Optional | Boolescher Wert | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an ein gesamtes Segment senden, auf das eine Campaign oder ein Canvas abzielt. Dieser Parameter ist standardmäßig auf `false` eingestellt. <br><br> Wenn `broadcast` auf `true` gesetzt ist, kann keine Empfängerliste angegeben werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, da ein unbeabsichtigtes Setzen dieses Flags dazu führen kann, dass Ihre Nachricht an eine größere Zielgruppe als erwartet gesendet wird. |
| `external_user_ids` | Optional | String-Array | Siehe [externer Nutzer-Bezeichner]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Optional | Array von Nutzer-Alias-Objekten | Siehe [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Optional | Verbundenes Zielgruppen-Objekt | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Optional | String | Siehe [Segment-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id` | Optional | String | Siehe [Campaign-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Optional | String | Siehe [Sende-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Optional | Boolescher Wert | Frequency-Capping für Kampagnen ignorieren, Standardwert ist false |
| `recipient_subscription_state` | Optional | String | Verwenden Sie diesen Parameter, um Nachrichten nur an Nutzer:innen zu senden, die sich angemeldet haben (`opted_in`), nur an Nutzer:innen, die abonniert oder angemeldet sind (`subscribed`), oder an alle Nutzer:innen, einschließlich abgemeldeter Nutzer:innen (`all`). <br><br>Die Verwendung von `all` ist nützlich für Transaktions-E-Mails. Standardmäßig ist `subscribed` eingestellt. |
| `schedule` | Erforderlich | Zeitplan-Objekt | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Optional | Messaging-Objekt | Siehe [verfügbare Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## Antwort {#response}

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}