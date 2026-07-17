---
nav_title: "POST: Campaigns mit API-getriggerter Zustellung versenden"
article_title: "POST: Campaigns mit API-getriggerter Zustellung versenden"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "In diesem Artikel finden Sie Einzelheiten über den Braze-Endpunkt „Campaigns mit API-getriggerter Zustellung versenden“."

---
{% api %}
# Campaign-Nachrichten mit API-getriggerter Zustellung versenden {#send-campaign-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um sofortige, einmalige Nachrichten an bestimmte Nutzer:innen mit Hilfe der API-getriggerten Zustellung zu senden.

Mit der API-getriggerten Zustellung können Sie den Inhalt von Nachrichten innerhalb des Braze-Dashboards unterbringen und gleichzeitig über Ihre API festlegen, wann und an wen eine Nachricht gesendet wird.

Wenn Sie ein Segment ansprechen möchten, wird eine Aufzeichnung Ihrer Anfrage in der [Entwicklungskonsole](https://dashboard.braze.com/app_settings/developer_console/activitylog/) gespeichert. Um Nachrichten mit diesem Endpunkt zu versenden, müssen Sie eine [Campaign-ID]({{site.baseurl}}/api/identifier_types) besitzen, die beim Erstellen einer [API-getriggerten Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) erzeugt wurde.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `campaigns.trigger.send` generieren.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [Campaign-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Optional | String | Siehe [Sende-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `trigger_properties` | Optional | Objekt | Siehe [Trigger-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Personalisierte Schlüssel-Wert-Paare gelten für alle Nutzer:innen in dieser Anfrage. |
| `broadcast` | Optional | Boolescher Wert | Sie müssen `broadcast` auf true setzen, wenn Sie eine Nachricht an das gesamte Segment senden, das im Braze-Dashboard als Zielgruppe der Campaign konfiguriert ist. Dieser Parameter ist standardmäßig auf false eingestellt (Stand: 31. August 2017). <br><br> Wenn `broadcast` auf true gesetzt ist, kann keine `recipients`-Liste einbezogen werden. Seien Sie jedoch vorsichtig, wenn Sie `broadcast: true` setzen, denn wenn Sie dieses Flag unbeabsichtigt setzen, kann dies dazu führen, dass Sie Ihre Nachricht an eine größere Zielgruppe als erwartet senden. |
| `audience` | Optional | Verbundenes Zielgruppen-Objekt | Siehe [Verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience). Wenn Sie `audience` einbeziehen, wird die Nachricht nur an Nutzer:innen gesendet, die den definierten Filtern entsprechen, wie z. B. angepasste Attribute und Abo-Status. |
| `recipients` | Optional | Array | Siehe [Empfänger:innen-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object).<br><br>Wenn `send_to_existing_only` `false` ist, muss ein `attributes`-Objekt enthalten sein.<br><br>Sie können den Abo-Gruppenstatus einer Nutzer:in aktualisieren, indem Sie `subscription_groups` in das verschachtelte `attributes`-Objekt aufnehmen. Weitere Einzelheiten finden Sie unter [Nutzerattribute-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object).<br><br>Wenn `recipients` nicht angegeben und `broadcast` auf true gesetzt ist, wird die Nachricht an das gesamte Segment gesendet, das im Braze-Dashboard als Zielgruppe der Campaign konfiguriert ist.<br><br>Wenn `email` der Bezeichner ist, müssen Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) in das Empfänger:innen-Objekt aufnehmen. |
| `attachments` | Optional | Array | Wenn `broadcast` auf true gesetzt ist, kann die Liste `attachments` nicht einbezogen werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

### Verhalten bei der Empfänger:innen-Auflösung {#recipient-resolution-behavior}

In diesem Abschnitt wird erläutert, wie Braze ein Nutzerprofil für den Versand auswählt und was passiert, wenn kein Profil ausgewählt wird.

Der Abo-Gruppenstatus einer Nutzer:in kann über den Parameter `subscription_groups` innerhalb des `attributes`-Objekts aktualisiert werden. Weitere Einzelheiten finden Sie unter [Nutzerattribute-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens).

#### Empfänger:innen-Limits und Profilerstellung {#recipient-limits-and-profile-creation}

Erfahren Sie mehr darüber, wie Empfänger:innen-Limits und die Profilerstellung für diesen Endpunkt funktionieren.

- Das `recipients`-Array kann bis zu 50 Objekte enthalten, wobei jedes Objekt einen einzelnen `external_user_id`-String und ein `trigger_properties`-Objekt enthält.
- Wenn `send_to_existing_only` `true` ist (Standard), sendet Braze die Nachricht nur an bestehende Nutzer:innen.
- Wenn `send_to_existing_only` `false` ist und ein `attributes`-Objekt bereitgestellt wird, erstellt Braze eine neue Nutzer:in, falls noch keine vorhanden ist.
- **Neue Profile benötigen `attributes` mit `send_to_existing_only: false`.** Braze führt die Erstellung oder Aktualisierung vor dem Versand aus dem `attributes`-Objekt im selben Empfänger:innen-Objekt durch. Wenn Sie `send_to_existing_only` auf `false` setzen, aber `attributes` weglassen (oder ein leeres Objekt senden), hydratisiert Braze die Profildaten nicht auf die gleiche Weise, sodass Sie nicht das kombinierte Verhalten „Nutzer:in erstellen oder aktualisieren, dann senden“ erhalten, für das dieses Muster vorgesehen ist.
- **E-Mail- und SMS-Adressierung.** Für die meisten E-Mail- oder SMS-API-getriggerten Sendungen an Personen, die noch nicht in Braze vorhanden sind, fügen Sie die benötigten Zustellungsfelder in `attributes` ein (z. B. `email` oder die Telefon-Attribute, die Ihr Workspace für SMS verwendet). Sie können dort auch die Abo-Gruppenmitgliedschaft oder den Abo-Status festlegen, wenn sich der Opt-in-Status im selben Aufruf ändern muss.
- **Campaign-Berechtigung.** Nachdem das Profil erstellt oder aktualisiert wurde, muss die Nutzer:in weiterhin der Zielgruppe der Campaign im Dashboard und den Kanal-Senderegeln entsprechen (z. B. Opt-in für E-Mail), damit Braze die Nachricht versendet.
- Die Einstellung `send_to_existing_only` auf `false` wird für Nutzer-Aliase nicht unterstützt. Neue Nutzer:innen, die nur über einen Alias verfügen, können über diesen Endpunkt nicht erstellt werden. Um an eine Nutzer:in zu senden, die nur über einen Alias verfügt, muss diese bereits in Braze vorhanden sein.

#### E-Mail-Bezeichner und Priorisierungs-Gleichstände {#email-identifier-and-prioritization-ties}

Wenn Sie Empfänger:innen per E-Mail identifizieren, verwendet Braze `prioritization`. Braze sendet nur, wenn `prioritization` ein Profil zurückgibt.

- Wenn Sie `email` als Bezeichner verwenden, löst Braze die Empfänger:in über `prioritization` auf.
- Wenn `prioritization` einen Gleichstand ergibt, sendet Braze nicht.
- Braze sendet, nachdem der Gleichstand aufgelöst wurde und `prioritization` ein Profil zurückgibt. Wenn beispielsweise Profilaktualisierungen die Sortierfelder einer Nutzer:in ändern, sendet Braze, sobald `prioritization` ein Profil eindeutig identifizieren kann (siehe [Wiederholungsverhalten und `send_to_existing_only`](#retry-behavior-and-send_to_existing_only)).
- Braze sendet auch nicht, wenn `prioritization` keine Profile zurückgibt.

#### Wiederholungsverhalten und send_to_existing_only {#retry-behavior-and-send_to_existing_only}

Erfahren Sie, was passiert, wenn `prioritization` nicht genau ein Profil zurückgibt.

- Wenn `prioritization` nicht genau ein Nutzerprofil zurückgibt, wiederholt Braze die Auflösung bis zu 40 Mal. Dieses Wiederholungsverhalten ist erwartungsgemäß.
- Die Einstellung `send_to_existing_only` ändert das Gleichstandsverhalten von `prioritization` nicht. Dasselbe Gleichstands- und Wiederholungsverhalten gilt unabhängig davon, ob diese Einstellung `true` oder `false` ist.

Wenn Sie eine reine E-Mail-Campaign für eine Empfänger:in triggern, die über `external_user_id` oder `user_alias` identifiziert wird, und dieses Nutzerprofil zum Zeitpunkt des Aufrufs keine E-Mail-Adresse hat, wiederholt Braze den Versand für bis zu ca. 2 Stunden. Dies deckt das gängige Muster ab, bei dem eine Nutzer:in erstellt und ihre E-Mail-Adresse kurz darauf festgelegt wird. Um ohne Verzögerung zu senden, fügen Sie das `email`-Attribut in `recipients[].attributes` ein, damit die Adresse im selben Aufruf wie der Trigger gesetzt wird.

{% alert note %}
Der Parameter `segment_id` wird für diesen Endpunkt nicht unterstützt. Um ein Segment anzusprechen, konfigurieren Sie das Segment in den Zielgruppen-Einstellungen der Campaign im Braze-Dashboard und verwenden Sie `"broadcast": true`, oder nutzen Sie den `audience`-Parameter mit [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)-Filtern.
{% endalert %}

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## Antwortdetails {#response-details}

Die Antworten der Endpunkte zum Senden von Nachrichten enthalten die `dispatch_id` der Nachricht als Referenz zum Zurückverfolgen des Versands. Die `dispatch_id` ist die ID des Nachrichtenversands – eine eindeutige ID für jede von Braze gesendete Übertragung. Wenn Sie diesen Endpunkt verwenden, erhalten Sie eine einzige `dispatch_id` für eine gesamte Gruppe von Nutzer:innen. Weitere Informationen zu `dispatch_id` finden Sie in unserer Dokumentation über das [Verhalten der Dispatch-ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

Wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors) den Fehlercode und die Beschreibung.

## Attribute-Objekt für Campaigns {#attributes-object-for-campaigns}

Braze verfügt über ein Messaging-Objekt namens `attributes`, mit dem Sie Attribute und Werte für eine Nutzer:in hinzufügen, erstellen oder aktualisieren können, bevor Sie ihr eine API-getriggerte Campaign senden. Verwenden Sie den `campaign/trigger/send`-Endpunkt, da dieser API-Aufruf das Nutzerattribute-Objekt verarbeitet, bevor er die Campaign verarbeitet und versendet. Dadurch wird das Risiko von Problemen, die durch [Race-Conditions]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) verursacht werden, minimiert.

{% alert tip %}
Sie suchen die Canvas-Version dieses Endpunkts? Informieren Sie sich über das [Versenden von Canvas-Nachrichten mit API-getriggerter Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#send-canvas-messages-using-api-triggered-delivery).
{% endalert %}

### Warum wird Liquid nicht gerendert, wenn ich es direkt in meinen JSON-Body einfüge? {#why-doesnt-liquid-render-when-i-put-it-directly-in-my-json-body}

Wenn Ihr Anfragetext gültiges JSON ist, wertet Braze jegliches Liquid im Payload serverseitig aus. Wenn Sie Liquid als Roh-Strings einbetten, setzen Sie diese Strings in Anführungszeichen und escapen Sie sie, damit der Body gültiges JSON bleibt – escapen Sie beispielsweise doppelte Anführungszeichen innerhalb von Strings. Wenn der Body das JSON-Parsing nicht besteht, gibt Braze einen `400`-Fehler zurück, bevor Liquid ausgewertet wird. Übergeben Sie dynamische Werte nach Möglichkeit über [`trigger_properties`]({{site.baseurl}}/api/objects_filters/trigger_properties_object) anstatt Liquid direkt in den Payload einzubetten.

{% endapi %}