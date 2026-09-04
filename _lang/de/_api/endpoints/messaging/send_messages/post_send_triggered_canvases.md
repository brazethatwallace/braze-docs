---
nav_title: "POST: Canvas-Nachrichten mit API-getriggerter Zustellung senden"
article_title: "POST: Canvas-Nachrichten mit API-getriggerter Zustellung senden"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts zum Senden von Canvases mit API-getriggerter Zustellung."

---
{% api %}
# Canvas-Nachrichten mit API-getriggerter Zustellung senden {#send-canvas-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Canvas-Nachrichten mit API-getriggerter Zustellung zu versenden.

Die API-getriggerte Zustellung ermöglicht es Ihnen, den Inhalt von Nachrichten im Braze-Dashboard zu speichern und gleichzeitig über Ihre API zu bestimmen, wann und an wen eine Nachricht gesendet wird.

Bevor Sie mit diesem Endpunkt Nachrichten versenden können, müssen Sie über eine [Canvas-ID]({{site.baseurl}}/api/identifier_types#canvas-identifier) verfügen (die beim Erstellen eines Canvas generiert wird).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `canvas.trigger.send` generieren.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) Canvas context properties that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) Canvas context properties for this user; key-value pairs override any keys that conflict with the parent `context`,
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an `attributes` object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `context` | Optional | Objekt | Canvas-Kontext-Eigenschaften für alle Empfänger:innen in dieser Anfrage. Personalisierte Schlüssel-Wert-Paare gelten für alle Nutzer:innen, es sei denn, ein empfängerspezifisches `context`-Objekt überschreibt einen Schlüssel. Das `context`-Objekt kann bis zu 50 KB groß sein. |
| `broadcast` | Optional | Boolescher Wert | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an das gesamte Segment senden, das im Braze-Dashboard als Zielgruppe des Canvas konfiguriert ist. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann keine `recipients`-Liste angegeben werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, denn wenn Sie dieses Flag unbeabsichtigt setzen, kann dies dazu führen, dass Sie Ihre Nachricht an eine größere Zielgruppe als erwartet senden. |
| `audience` | Optional | Verbundenes Zielgruppen-Objekt | Siehe [Verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience). Wenn Sie `audience` angeben, wird die Nachricht nur an Nutzer:innen gesendet, die den definierten Filtern entsprechen, wie z. B. angepasste Attribute und Abo-Status. |
| `recipients` | Optional | Array | Siehe [Empfänger:innen-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object). <br><br> Wenn `send_to_existing_only` auf `false` gesetzt ist, muss ein `attributes`-Objekt für die Empfänger:in angegeben werden. <br><br> Wenn nicht angegeben und `broadcast` auf `true` gesetzt ist, wird die Nachricht an das gesamte Segment gesendet, das im Braze-Dashboard als Zielgruppe des Canvas konfiguriert ist.<br><br> Das Array `recipients` kann bis zu 50 Objekte enthalten. Jedes Objekt muss genau eines der Felder `external_user_id`, `user_alias` oder `email` enthalten und kann ein empfängerspezifisches `context`-Objekt für Canvas-Kontext-Eigenschaften beinhalten (empfängerspezifische Schlüssel überschreiben das übergeordnete `context`-Objekt bei Konflikten). <br><br> Wenn `email` der Bezeichner ist, müssen Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) in das Empfänger:innen-Objekt aufnehmen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
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
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Antwortdetails {#response-details}

Die Antworten der Endpunkte zum Senden von Nachrichten enthalten die `dispatch_id` der Nachricht, um den Versand zurückverfolgen zu können. Die `dispatch_id` ist die ID des Nachrichtenversands (eindeutige ID für jede von der Braze-Plattform gesendete „Übertragung“). Weitere Informationen finden Sie unter [Verhalten der Dispatch-ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `201` könnte den folgenden Antworttext zurückgeben. Wenn der Canvas archiviert, gestoppt oder pausiert ist, wird er nicht über diesen Endpunkt gesendet.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Wenn Ihr Canvas archiviert ist, wird folgende `notice`-Nachricht angezeigt: „The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect.“ Wenn Ihr Canvas nicht aktiv ist, wird folgende `notice`-Nachricht angezeigt: „The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.“

Wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors) den Fehlercode und die Beschreibung.

## Hinweise {#considerations}

Beachten Sie Folgendes, wenn Sie API-Aufrufe zum Senden von Canvas-Nachrichten mit API-getriggerter Zustellung durchführen:

- **Versand an bestehende Nutzer:innen**: Wenn `send_to_existing_only` auf `true` gesetzt ist (Standardwert), wird die Nachricht ausschließlich an bereits in Braze vorhandene Nutzer:innen gesendet.
- **Neue Nutzer:innen erstellen**: Wenn `send_to_existing_only` auf `false` gesetzt ist, müssen Sie ein `attributes`-Objekt angeben. Sollte eine Nutzer:in mit der angegebenen ID nicht vorhanden sein, erstellt Braze vor dem Versenden der Nachricht ein Profil mit dieser ID und den entsprechenden Attributen.
- **Neue Profile benötigen `attributes` mit `send_to_existing_only: false`.** Braze führt das Erstellen oder Aktualisieren vor dem Versand aus dem `attributes`-Objekt im selben Empfänger:innen-Objekt durch. Wenn Sie `send_to_existing_only` auf `false` setzen, aber `attributes` weglassen (oder ein leeres Objekt senden), hydratisiert Braze die Profildaten nicht auf die gleiche Weise, sodass Sie nicht das kombinierte Verhalten „Nutzer:in erstellen oder aktualisieren, dann senden“ erhalten, für das dieses Muster vorgesehen ist.
- **E-Mail- und SMS-Adressierung.** Für die meisten E-Mail- oder SMS-API-getriggerten Sendungen an Personen, die noch nicht in Braze vorhanden sind, geben Sie die benötigten Zustellungsfelder innerhalb von `attributes` an (z. B. `email` oder die Telefon-Attribute, die Ihr Workspace für SMS verwendet). Sie können dort auch die Abo-Gruppen-Mitgliedschaft oder den Abo-Status festlegen, wenn sich der Opt-in-Status im selben Aufruf ändern muss.
- **Canvas-Berechtigung.** Nachdem das Profil erstellt oder aktualisiert wurde, muss die bzw. der Nutzer:in weiterhin der im Dashboard konfigurierten Zielgruppe des Canvas und den Kanal-Senderegeln entsprechen (z. B. Opt-in für E-Mail), damit Braze die Nachricht sendet.
- **Einschränkung bei Nutzer-Aliasen**: Das Flag `send_to_existing_only` kann nicht mit Nutzer-Aliasen verwendet werden. Um an eine Nutzer:in zu senden, die nur über einen Alias verfügt, muss diese Nutzer:in bereits in Braze vorhanden sein.
- **Segment-Targeting**: Der Parameter `segment_id` wird für diesen Endpunkt nicht unterstützt. Um ein Segment anzusprechen, konfigurieren Sie das Segment in den Zielgruppeneinstellungen des Canvas im Braze-Dashboard und verwenden Sie `broadcast: true` oder den Parameter `audience` mit [Connected-Audience]({{site.baseurl}}/api/objects_filters/connected_audience)-Filtern.
- **Kombiniertes Targeting**: Wenn Sie sowohl den Parameter `recipients` angeben als auch ein Zielsegment im Dashboard konfigurieren, wird die Nachricht nur an Nutzerprofile gesendet, die im API-Aufruf angegeben sind und gleichzeitig den Filtern des Segments entsprechen.
- **Server-zu-Server-Aufrufe**: Wenn Sie Server-zu-Server-Aufrufe durchführen, müssen Sie möglicherweise die entsprechende API-URL auf die Allowlist setzen, falls Sie sich hinter einer Firewall befinden.

## Attribute-Objekt für Canvas {#attributes-object-for-canvas}

Verwenden Sie das Messaging-Objekt `attributes`, um Attribute und Werte für eine Nutzer:in hinzuzufügen, zu erstellen oder zu aktualisieren, bevor Sie über den Endpunkt `canvas/trigger/send` ein API-getriggertes Canvas senden. Dieser API-Aufruf verarbeitet das Nutzerattribute-Objekt, bevor er das Canvas verarbeitet und sendet. Dadurch wird das Risiko von Problemen, die durch [Race-Conditions]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) verursacht werden, minimiert. Standardmäßig können Abo-Gruppen jedoch nicht auf diese Weise aktualisiert werden.

{% alert note %}
Sie suchen die Campaign-Version dieses Endpunkts? Informieren Sie sich über den [Versand von Campaign-Nachrichten mit API-getriggerter Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).
{% endalert %}

{% endapi %}