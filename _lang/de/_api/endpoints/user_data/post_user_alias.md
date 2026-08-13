---
nav_title: "POST: Neuen Nutzer-Alias erstellen"
article_title: "POST: Neuen Nutzer-Alias erstellen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Neuen Nutzer-Alias erstellen“."

---
{% api %}
# Neuen Nutzer-Alias erstellen {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um neue Nutzer-Aliase für bestehende identifizierte Nutzer:innen hinzuzufügen oder um neue nicht identifizierte Nutzer:innen zu erstellen.

Pro Anfrage können bis zu 50 Nutzer-Aliase angegeben werden.

**Um einen Nutzer-Alias für bestehende Nutzer:innen hinzuzufügen**, muss eine `external_id` im neuen Nutzer-Alias-Objekt enthalten sein. Wenn die `external_id` im Objekt vorhanden ist, es aber keine Nutzer:innen mit dieser `external_id` gibt, wird der Alias keinen Nutzer:innen hinzugefügt. Wenn keine `external_id` vorhanden ist, werden Nutzer:innen trotzdem erstellt, müssen aber später identifiziert werden. Dazu können Sie den Endpunkt „Nutzer:innen identifizieren“ und den Endpunkt `users/identify` verwenden.

**Um neue Nutzer:innen zu erstellen, die nur über einen Alias verfügen**, muss die `external_id` im neuen Nutzer-Alias-Objekt weggelassen werden. Nachdem die Nutzer:innen erstellt wurden, verwenden Sie den Endpunkt `/users/track`, um die Alias-Nutzer:innen mit Attributen, Ereignissen und Käufen zu verknüpfen, und den Endpunkt `/users/identify`, um die Nutzer:innen mit einer `external_id` zu identifizieren.

Sie können API-getriggerte Campaigns über `user_alias` an Nutzer:innen senden, indem Sie den Endpunkt [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) verwenden.

## Wenn `alias_label` und `alias_name` bereits existieren {#when-alias_label-and-alias_name-already-exist}

Die Kombination aus `alias_label` und `alias_name` muss in Ihrer Nutzerbasis eindeutig sein. Weitere Informationen finden Sie unter [Nutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases).

Wenn Sie eine Anfrage senden, bei der das Paar aus `alias_label` und `alias_name` bereits für Nutzer:innen existiert (ob bei denselben oder anderen Nutzer:innen), gibt der Endpunkt trotzdem eine erfolgreiche Antwort zurück (z. B. `"aliases_processed": 1`, `"message": "success"`). In diesem Fall wird den Nutzer:innen in der Anfrage kein neuer Alias hinzugefügt. Da das Paar aus `alias_label` und `alias_name` bereits verwendet wird, nimmt die Anfrage keine Änderungen vor, und es kann so aussehen, als ob der Alias den betreffenden Nutzer:innen nie hinzugefügt wurde.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key) mit der Berechtigung `users.alias.new`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Erforderlich | Array mit neuen Nutzer-Alias-Objekten | Siehe [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> Weitere Informationen zu `alias_name` und `alias_label` finden Sie in unserer Dokumentation zu [Nutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

### Anfragetext des Endpunkts mit Spezifikation des neuen Nutzer-Alias-Objekts {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Antwort {#response}

Wenn ein Alias übersprungen wird, weil dieselbe Kombination aus `alias_label` und `alias_name` bereits für Nutzer:innen existiert, kann der Antworttext trotzdem Erfolg anzeigen. Weitere Details finden Sie unter [Wenn Alias-Label und -Name bereits existieren](#when-the-alias-label-and-name-already-exist).

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

## Fehlerbehebung {#troubleshooting}

### Warum werden meine Attribute nicht aktualisiert, nachdem ich mit diesem Endpunkt einen Nutzer-Alias erstellt habe? {#why-are-my-attributes-not-updating-after-i-create-a-user-alias-using-this-endpoint}

Dies geschieht in der Regel, wenn auf `/users/alias/new` eine separate `/users/track`-Anfrage folgt, die versucht, Attribute über den Alias zu aktualisieren. Die Track-Anfrage kann verarbeitet werden, bevor Braze das neue Paar aus `alias_label` und `alias_name` konsistent einem Profil zuordnen kann, sodass die Attribute nicht bei den erwarteten Nutzer:innen ankommen.

**Empfohlener Ansatz:** Verwenden Sie einen einzelnen [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Aufruf nur dann, wenn Sie ein reines Alias-Profil erstellen oder ein Profil über einen bereits vorhandenen Alias aktualisieren möchten. Fügen Sie im `attributes`-Array `user_alias` und Ihre Profilfelder in dasselbe [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object) ein, damit Braze die Nutzer:innen auflöst und die Aktualisierung in einem Schritt durchführt.

Setzen Sie `_update_existing_only` auf `false`, wenn Sie aus diesem Objekt möglicherweise ein reines Alias-Profil erstellen müssen. Wenn Sie es weglassen und dabei `user_alias` verwenden, verhält sich Braze standardmäßig so, dass nur aktualisiert und kein reines Alias-Profil erstellt wird. Wenn der Alias bereits bei Nutzer:innen in Ihrem Workspace existiert, aktualisiert dieselbe Anfrage dieses Profil mit Ihren neuen Attributen.

Sie können `/users/track` nicht verwenden, um bestehenden Nutzer:innen, die über eine `external_id` identifiziert werden, einen neuen Alias hinzuzufügen. In einem Nutzerattribut-Objekt schließen sich `external_id` und `user_alias` gegenseitig aus. Um identifizierten Nutzer:innen einen Alias hinzuzufügen, rufen Sie zuerst `/users/alias/new` auf. Nachdem der Alias zugeordnet wurde, können Sie dieses Profil mit `/users/track` über die `external_id` oder den vorhandenen Alias aktualisieren.

Das folgende `/users/track`-Body erstellt beispielsweise ein reines Alias-Profil, wenn der Alias noch nicht existiert, oder aktualisiert das vorhandene Profil, das diesen Alias bereits hat:
```json
{
  "attributes": [
    {
      "user_alias": {
        "alias_name": "example@example.com",
        "alias_label": "email"
      },
      "_update_existing_only": false,
      "string_attribute": "test_alias_only_update"
    }
  ]
}
```

{% endapi %}